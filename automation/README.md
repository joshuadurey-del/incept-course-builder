# Private-repository activity automation

Phase A polls the private source repositories every ten minutes and on
`repository_dispatch: course-event`. It reads with a classic owner PAT, keeps an
opaque hashed cursor in this repository, appends derived public-safe activity rows
to `updates.json`, and projects the newest typed and repository events into the
matching primary claim in `data.json`. The course workspace and course pages render that
shared projection. Every row carries a bounded public writer attestation:
`repository-event automation`, `INCEPT event projection`, or `dashboard curation`.
Titles, bodies, commit
messages, webhook bodies, tokens, and receipt paths never enter this repository.
The monitored private-repository inventory is an Actions secret.

Required Actions secrets:

- `SOURCE_REPO_READ_TOKEN` — owner-minted classic PAT with `repo` read access.
- `SOURCE_REPOSITORY_INVENTORY_JSON` — `dashboard-source-inventory/v1` JSON
  mapping private `owner/repo` names to `humgeo`, `apwh`, `apush`, `psych`, or
  `cross`.
- `LOCAL_EVENT_DISPATCH_SECRET` — HMAC secret shared only with the local INCEPT
  appender through macOS Keychain.

Set each secret interactively; never place its value on a command line:

```sh
gh secret set SOURCE_REPO_READ_TOKEN -R InceptTrilogy/ap-four-course-dashboard
gh secret set SOURCE_REPOSITORY_INVENTORY_JSON -R InceptTrilogy/ap-four-course-dashboard
```

After all three secrets exist, enable the workflow:

```sh
gh variable set DASHBOARD_AUTOMATION_ENABLED --body true -R InceptTrilogy/ap-four-course-dashboard
```

Set that variable to `false` for the kill switch. The workflow explicitly
requests a legacy Pages build after each verified dashboard push. Serving
completes asynchronously and is verified separately.

The first event-stream run publishes the newest verified event per course and
baselines older observed event IDs. Later runs publish unseen events, capped at
40 rows per run; overflow remains unprocessed for the next run. Single-writer
workflow concurrency, event-ID cursors, and exact-row dedup prevent duplicates. Actual
event-to-decision latency is recorded by each run; the ten-minute schedule is a
target, not a promise.

Course pages keep repository activity and local-log freshness separate. Repository
events include pushes, pull-request actions/reviews, issue actions/comments,
releases, other GitHub repository events, and completed workflow runs. Shared-repo
classification uses private metadata but publishes only the derived course label
and safe event fields.

Local landings use authenticated `repository_dispatch: course-event`. The
receipt-free signed payload contract is fixed in `automation/ADR.md`; hashed row
IDs are persisted with the dashboard cursor. Local `backfill` rows baseline as
NOOP. A semantic update commits `updates.json` and `data.json` in the same
transaction; the course workspace and course pages then render the same attested event.
The formal lifecycle fields remain manual. The dashboard snapshot uses evidence
time, not workflow or commit time. On Actions, precommit proves the formal claim
bytes are unchanged and permits only `snapshot`, `current_event`, and
`repository_event`; local claim curation still runs the full claims linter.

Phase B replaces `SOURCE_REPO_READ_TOKEN` repo by repo with short-lived,
read-only GitHub App installation tokens. External real-time webhook ingress is
not required and remains separately gated.

The needs-human strip uses the existing signed `course-event` dispatch corridor,
not a new ingress. `needs_human.py add`, `resolve`, and `project` send the exact
public projection after writing it. The serialized receiver accepts newer documents,
ignores older redeliveries, and fails closed on equal-timestamp conflicts.

For recovery, a local dashboard update can still validate and fold the projection:

```sh
python3 automation/poll_repositories.py fold-needs-human --source "$INCEPT_ZONE/needs-human.public.json"
```

The source ledger and private details never enter this repository. A missing or stale
projection is visible as a typed UI hold; no background copier or new event host exists.

## Live source sync (September 10, 2026)

The dashboard's **Sync sources** control opens the private [Sync live course sources workflow](https://github.com/InceptTrilogy/ap-four-course-dashboard/actions/workflows/dashboard-repo-poll.yml). Sign in to GitHub and select **Run workflow** on main. **Refresh results** then reloads the public site's published JSON, including the check timestamp and source revisions. It does not itself dispatch a job. GitHub may delay scheduled runs; this is an on-demand snapshot, not a streaming feed.

The existing ten-minute workflow reads remote main once per configured repository, fetches source files at those immutable SHAs, and rechecks heads before recording a successful sync. It uses the existing source read credential. `sync_sources.py` produces only reviewed inventory summaries and hashes; source bodies stay in memory. Every mapped row retains a direct source URL. Failure preserves the old value/date and labels the failed check. Unmapped populations link to their source repository and remain mapping gaps. This is not an exhaustive search for new native schemas or successor ledgers.

Claims with an exact file hash are compared with current bytes separately from their formal status. Claims lacking a mapped verifier stay explicitly unverified. Identical source bytes do not renew QC, a receipt date, a stage, or learner acceptance. Historical calibration, acceptance-ledger and Unit 3 receipts retain their named scope. No source repository or platform is mutated.

The same serialized job updates the private dashboard, then uses `EVIDENCE_REPO_WRITE_TOKEN` to publish only the validated population/source-check projection and a fixed update row to `joshuadurey-del/incept-course-builder`. It first checks that credential's public-repo write access. Public claims, needs-human decisions, other updates, code and course sources are not copied from the private tree. Each repository's own precommit and remote-drift checks run before pushing. Public Pages is requested after the push; workflow completion alone does not certify learner state. Missing write permission fails visibly, leaving the last public evidence date intact. Never place a PAT in browser JavaScript.

Local authenticated check: `SOURCE_REPO_READ_TOKEN=... python3 automation/sync_sources.py refresh` from the dashboard checkout. Regression: `python3 automation/sync_sources.py selftest`. Adding a new population requires its owning native source path, schema, scope and metadata-only reader; absence of a reader is not absence of course work.

### Public publication control

The new public-publishing leg is disabled by default. A signed-in operator can explicitly select **Publish course counts, source links, hashes and check times to the public dashboard** in the manual Run workflow form. Scheduled public publishing also requires repository variable `PUBLIC_SOURCE_SYNC_ENABLED=true`, set only after owner approval and a successful publication pilot. Source reads and the existing private update continue independently. This prevents a schedule from substituting for approval of a blocked manual publication attempt.
