#!/bin/sh
# Pre-commit gate for the dashboard: every claim must carry its own date, then
# refresh the published digests. Point .git/hooks/pre-commit at this file.
#
# Blocks on a claim with no parseable observed_at / status_at, because an undated
# row silently inherited the manifest snapshot and got rejuvenated by a republish
# (postmortem C11). It does NOT block on age: a claim can legitimately describe
# something old. Escape hatch: SKIP_CLAIMS_LINT=1 git commit ...
cd "$(git rev-parse --show-toplevel)" || exit 1
LINT="${INCEPT_ZONE:-$HOME/repos/social-studies/INCEPT}/tools/claims_staleness_lint.py"

# The page's "Last updated" line reads the newest entry in updates.json, not the
# manifest snapshot. A claims change with no feed entry is therefore INVISIBLE on
# the surface agents read first (caught by Josh 2026-08-17, 46 minutes after a
# republish left the timestamp untouched).
STAGED=$(git diff --cached --name-only)

if ! python3 - <<'PY'
import datetime
import json
import re
import urllib.parse

with open('updates.json') as f:
    updates = json.load(f)

assert isinstance(updates, list), 'updates.json must contain a JSON array'
writers = {'dashboard curation', 'INCEPT event projection', 'repository-event automation'}
for index, update in enumerate(updates):
    assert isinstance(update, dict), f'update {index} must be an object'
    for field in ('ts', 'course', 'text', 'writer'):
        assert isinstance(update.get(field), str) and update[field].strip(), \
            f'update {index} needs a non-empty {field}'
    assert update['writer'] in writers, f"update {index} has invalid writer: {update['writer']}"
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z', update['ts']), \
        f"update {index} has invalid ts: {update['ts']}"
    datetime.datetime.fromisoformat(update['ts'].replace('Z', '+00:00'))
    event_fields = {'event_type', 'evidence_url'} & update.keys()
    assert not event_fields or event_fields == {'event_type', 'evidence_url'}, \
        f'update {index} must carry event_type and evidence_url together'
    if event_fields:
        assert update['event_type'] in {'push', 'pull_request', 'issues', 'release', 'workflow_run', 'repository'}, \
            f'update {index} has invalid event_type'
        url = urllib.parse.urlparse(update['evidence_url'])
        assert url.scheme == 'https' and url.hostname == 'github.com' and url.path.strip('/'), \
            f'update {index} has invalid evidence_url'
    local_fields = {'phase', 'kind'} & update.keys()
    assert not local_fields or local_fields == {'phase', 'kind'}, \
        f'update {index} must carry phase and kind together'
    if local_fields:
        assert not event_fields, f'update {index} cannot be both local and GitHub activity'
        assert update['kind'] in {'landed', 'merged', 'filed', 'closed', 'receipt-sealed', 'state-change', 'milestone', 'hold', 'executor-step', 'note'}, \
            f'update {index} has invalid local kind'
        assert isinstance(update['phase'], str), f'update {index} has invalid phase'

with open('data.json') as f:
    data = json.load(f)
claims = {row.get('claim_id'): row for row in data.get('claims', [])}
for claim_id in ('humgeo.blueprint.audit', 'apwh.blueprint.audit', 'apush.blueprint.audit', 'psych.blueprint.audit'):
    claim = claims.get(claim_id, {})
    step = claim.get('next_step')
    assert isinstance(step, dict) and set(step) == {'verb', 'tool', 'args', 'gate'}, f'{claim_id} needs typed next_step'
    assert all(isinstance(step[field], str) and step[field].strip() for field in ('verb', 'tool', 'gate')), f'{claim_id} has invalid next_step'
    assert isinstance(step['args'], list) and all(isinstance(arg, str) for arg in step['args']), f'{claim_id} has invalid args'
    assert isinstance(claim.get('freshness_limit_hours'), int) and claim['freshness_limit_hours'] > 0, f'{claim_id} needs freshness limit'
    current = claim.get('current_event')
    if current is not None:
        assert isinstance(current, dict) and set(current) == {'ts', 'phase', 'kind', 'text', 'writer'}, f'{claim_id} has invalid current_event fields'
        assert current['writer'] in writers and current['kind'] in {'landed', 'merged', 'filed', 'closed', 'receipt-sealed', 'state-change', 'milestone', 'hold', 'executor-step', 'note'}, f'{claim_id} has invalid current_event authority'
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z', current['ts']) and isinstance(current['phase'], str) and isinstance(current['text'], str) and current['text'].strip(), f'{claim_id} has invalid current_event value'
        assert not any(token in current['text'] for token in ('/Users/', 'file://', '-----BEGIN', 'ghp_', 'github_pat_')), f'{claim_id} current_event crosses the public boundary'
    repository = claim.get('repository_event')
    if repository is not None:
        assert isinstance(repository, dict) and set(repository) == {'ts', 'event_type', 'text', 'evidence_url', 'writer'}, f'{claim_id} has invalid repository_event fields'
        assert repository['writer'] == 'repository-event automation' and repository['event_type'] in {'push', 'pull_request', 'issues', 'release', 'workflow_run', 'repository'}, f'{claim_id} has invalid repository_event authority'
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z', repository['ts']) and isinstance(repository['text'], str) and repository['text'].strip(), f'{claim_id} has invalid repository_event value'
        url = urllib.parse.urlparse(repository['evidence_url'])
        assert url.scheme == 'https' and url.hostname == 'github.com' and url.path.strip('/'), f'{claim_id} has invalid repository_event URL'

with open('process.json') as f:
    process = json.load(f)
assert process.get('stages') and all(isinstance(row.get('automated'), bool) for row in process['stages']), 'process steps need automated booleans'

print(f'UPDATES OK: {len(updates)} schema-valid entries')
PY
then
  echo "pre-commit: BLOCKED — updates.json violates its published schema."
  exit 1
fi

if ! python3 automation/poll_repositories.py validate-needs-human; then
  echo "pre-commit: BLOCKED — needs-human.json violates needs-human-public/v1."
  exit 1
fi

# The feed-row rule is for people. The automation projection (DASHBOARD_AUTOMATION_PROJECTION=1)
# proves below that formal claims are byte-identical, and its own "Source sync checked" feed row
# is keyed to the minute (sync_sources.write), so a second check inside one minute changes
# data.json stamps only and adds no row. Two runs in one minute (a dispatch landing seconds before
# a scheduled run) made runs 35500811976 and 35516981556 (#1809) fail here on 2026-09-20.
if [ -z "$SKIP_CLAIMS_LINT" ] && [ "$DASHBOARD_AUTOMATION_PROJECTION" != "1" ] \
   && echo "$STAGED" | grep -qx 'data.json' \
   && ! echo "$STAGED" | grep -qx 'updates.json'; then
  echo "pre-commit: BLOCKED — data.json changed but updates.json has no new entry."
  echo "  The page's Last-updated line and the agent-facing feed both read updates.json."
  echo "  Add an entry describing the change, or commit with SKIP_CLAIMS_LINT=1."
  exit 1
fi

if [ -n "$SKIP_CLAIMS_LINT" ]; then
  echo "pre-commit: claims lint SKIPPED by SKIP_CLAIMS_LINT"
elif ! echo "$STAGED" | grep -qx 'data.json'; then
  echo "pre-commit: claims lint not needed (data.json unchanged)"
elif [ "$DASHBOARD_AUTOMATION_PROJECTION" = "1" ]; then
  python3 - <<'PY' || exit 1
import json
import subprocess

def load(spec):
    return json.loads(subprocess.check_output(['git', 'show', spec]))

def formal(document):
    document.pop('snapshot', None)
    document.pop('source_sync', None)
    document.pop('population_coverage', None)
    for claim in document.get('claims', []):
        if claim.get('claim_id') in {
            'humgeo.blueprint.audit', 'apwh.blueprint.audit',
            'apush.blueprint.audit', 'psych.blueprint.audit',
        }:
            claim.pop('current_event', None)
            claim.pop('repository_event', None)
    return document

import sys
sys.path.insert(0, 'automation')
from sync_sources import validate_projection
before, after = load('HEAD:data.json'), load(':data.json')
if before.get('source_sync') != after.get('source_sync') or before.get('population_coverage') != after.get('population_coverage'):
    validate_projection(after)
assert formal(load('HEAD:data.json')) == formal(load(':data.json')), \
    'automation may update only validated source projection and snapshot/current_event/repository_event'
print('CLAIMS OK: automation changed display projection only; formal claims are byte-identical')
PY
elif [ ! -f "$LINT" ]; then
  echo "pre-commit: BLOCKED — claims linter not found at $LINT."
  echo "  Set INCEPT_ZONE, or commit with SKIP_CLAIMS_LINT=1 and say so in the message."
  exit 1
elif ! python3 "$LINT" data.json --hygiene; then
  echo "pre-commit: BLOCKED — every claim needs observed_at (OBSERVED) or status_at"
  echo "  (PLANNED/BLOCKED), in ISO form. Undated rows above."
  exit 1
fi

exec env HASH_REF=: bin/update-hashes.sh write
