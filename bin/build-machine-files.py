#!/usr/bin/env python3
"""Build the dashboard's machine files from the ASAP-edition public-safe contract projection.

The phase objects below project `asap_runbook.phases`; internal operational pointers
are omitted. Source:
RUNBOOK-ASAP.md at sha256 9dad48b882a79dacf1c8093f759ea190679bf1b42489a4841890951a12b2508d.
Run from anywhere: build-machine-files.py DASHBOARD_DIR UTC_STAMP.
"""
import json
import sys
from pathlib import Path

DASH = Path(sys.argv[1])
STAMP = sys.argv[2]
EDITION = "ASAP edition (2026-09-01)"
SOURCE_SHA256 = "5de7939b33a121f2aca872019c32f2e6c0ecc7bd67e35f834c18b38855470d9d"

# Public-safe projection verified against the source YAML; private operational pointers omitted.
ASAP_PHASES = [{'id': 'p0'}, {'id': 'p12', 'name': 'tree-and-pricing', 'state': 'done-all-four', 'verify': "Blueprint predicates and each child plan's live state, re-earned from the owning repository's current main."}, {'id': 'p3', 'name': 'bank-gates', 'verify': ['phase-bank-validation skill (answer-shape + key balance)', 'QTI parse + assertions (original §3.6) — NOT skippable: LearnWith marks a failed embedded item COMPLETE']}, {'id': 'p4'}, {'id': 'p5', 'name': 'publish-dark', 'steps': ['bank-gates', 'assets-qti', 'images', 'tree', 'drift-preflight', 'OWNER_WORD', 'push-dark', 'verify-live', 'post-push', 'xp', 'evidence-bundle'], 'verify': ['verify-live readback reconciles push bundle exactly (APES pub_stage7_verify_live.py pattern)', 'publishStatus == testing', 'enrollments == 0', 'evidence bundle README in course repo (Bio/APES format)', 'every native write carries three receipts under one sealed plan digest: capture prior state (zero writes), execute with readback, replay with zero writes (restored from the cut list 2026-09-14)', 'one writer per course surface, enforced by the writer lock; operator PR lands before the seal PR', 'every assessment link and resource carries a lessonType from the fleet enum (quiz, powerpath-100, unit-test, test-out, placement, map-adaptive, alpha-read-article); section components under a mock exam carry the mock_section kind; checked by diffing against a fleet course the owner can see (HumGeo Final row-shape repair, 2026-09-22)', "getAssessmentProgress returns a question count equal to the QTI test's item count for every assessment link, before the phase closes (a toolProvider or launchUrl left on a QTI resource returns zero questions)", 'a re-point overwrites or nulls every OneRoster launch-shape key (toolProvider, launchUrl); a PUT merges metadata and cannot drop a key by omitting it'], 'shape': 'one course holds all units (APES: unit 1 mints, later units pin --course-id)'}, {'id': 'p6', 'name': 'live-qc-gauntlet', 'instrument': "fleet course-QC harness (APES reports/step5_courseqc/ job pattern) — reuse, don't build", 'loop': 'judge -> remediate (1-repair/2-regenerate) -> re-push -> re-judge until bar', 'repush_rules': ['denylist: every QC-dropped ID recorded at drop time; push tooling refuses denylisted IDs', 'drift: never re-push a tree that mismatches last verified state (APES pub_preflight_drift.py)']}, {'id': 'p7', 'name': 'walk-and-accept', 'verify': ['factory walkthrough PASS on the staging deployment after the reversible flag PR (answers save; feedback choice-specific, non-leaking; keys unskewed)', 'one human pass: start/middle/end + longest reading + each writing geometry', 'XP spot-check: <80%=0, >=80%=base once, 100%=1.25x once, reload adds nothing', 'recreate receipt lists every enrolled learner across all classes; no-plan learners noted'], 'account': 'ONE owner test account, enrolled additively'}, {'id': 'p8', 'name': 'demo-and-flip', 'verify': ['Ilma demo done from test account', 'her word recorded', 'then broader enrollment']}]

# 2026-09-14.8: p6 failure triage classes recorded before repair.
# 2026-09-15.1: standing authorization mode (the typed install command is the owner word); p7 operator walk; p8 decision rule. No human in the loop.
next(phase for phase in ASAP_PHASES if phase["id"] == "p6").update({'triage_classes': ['content', 'context', 'checker', 'provider', 'selection']})

# 2026-09-08.7: preserve cold-run and checker-execution evidence in the public projection.
next(phase for phase in ASAP_PHASES if phase["id"] == "p6").update({'receipt_required': ['job_id', 'course_id', 'request_body_sha256', 'submitted_at', 'terminal_at', 'status', 'per_checker_status_all_five_executed_or_errored', 'pass_rate', 'llm_questions_checked', 'llm_cache_hits', 'llm_cache_dir', 'cold_or_warm', 's3_report_keys_sha256', 'cold_route_A_or_B'], 'final_run': 'cold', 'all_checkers_executed': True})

DISPLAY_NAMES = {"p0": "CUT", "p4": "CUT"}

# Presentation only: current course positions and acceptance stay in their native records.
ASAP_VIEWS = [
    {"id": "align", "label": "Align", "letter": "A", "native_phases": ["p12"],
     "summary": "Know the whole course before choosing the next step.",
     "scope": "Reconcile the current population census, blueprint, curriculum coverage, teaching design, tree and pricing.",
     "proof": "Every applicable population has a current inventory and a course-owned requirement. Earlier courses grant a new course no completion credit."},
    {"id": "synthesize", "label": "Synthesize", "letter": "S", "native_phases": ["content", "p3"],
     "summary": "Create and accept every required content population.",
     "scope": "Author and repair content, verify items and complete forms, and satisfy native bank and QTI checks.",
     "proof": "Acceptance is measured separately for each population. A gate-bank PASS does not prove practice, writing, media or whole-course readiness."},
    {"id": "assemble", "label": "Assemble", "letter": "A", "native_phases": ["p5"],
     "summary": "Connect accepted content to the learner experience.",
     "scope": "Compile native assets and use the course-owned publication route with exact readback, media, structure and XP evidence.",
     "proof": "Integrated, published and served coverage require their own receipts. Partial publication does not establish complete assembly."},
    {"id": "prove", "label": "Prove", "letter": "P", "native_phases": ["p6", "p7", "p8"],
     "summary": "Verify the final course and retain required human decisions.",
     "scope": "Final cold course QC, native learner acceptance, the human walkthrough and the recorded release decision.",
     "proof": "Use the native cold-QC bar and checker evidence, learner and XP readbacks, and the required human acceptance. A phase label cannot grant release authority."},
]
ASAP_GUIDES = {
    "align": {"skills": ["ap-toolbox", "course-deficit-burndown", "reverse-engineer"], "tools": ["Native census and blueprint selectors", "Course-owned source and teaching contracts"]},
    "synthesize": {"skills": ["item-pipeline", "item-regen", "factory-batch-dispatch", "enrichment", "phase-bank-validation"], "tools": ["Current native generation and item QC", "Whole-form and population validators"]},
    "assemble": {"skills": ["native-assets-build", "publish-course-dark", "land-a-change", "100"], "tools": ["Course-owned asset and QTI compilation", "Native publisher and exact served readback"]},
    "prove": {"skills": ["course-qc-gauntlet", "100"], "tools": ["Native course QC and learner acceptance", "Course-owned walkthrough and release decisions"]},
}
for view in ASAP_VIEWS:
    view.update(ASAP_GUIDES[view["id"]])
POPULATION_SCOPE = ["Gate MCQs", "Practice", "PowerPath / PP100", "Unit assessments", "Mock / exam forms", "Articles", "Embedded checks", "Videos / media", "Writing activities", "Writing scoring", "Train Your Eye"]


def required_artifacts(phase):
    items = []
    for key in ("steps", "verify", "repush_rules", "receipt_required"):
        value = phase.get(key, [])
        items.extend(value if isinstance(value, list) else [value])
    for key in ("instrument", "loop", "shape", "account"):
        if phase.get(key):
            items.append(phase[key])
    return items


stages = []
for phase in ASAP_PHASES:
    cut = phase["id"] in DISPLAY_NAMES
    stages.append({
        "id": phase["id"],
        "name": DISPLAY_NAMES[phase["id"]] if cut else phase["name"],
        "state": "cut" if cut else phase.get("state", "required"),
        "contract_status": "CUT" if cut else ("DONE_ALL_FOUR" if phase.get("state") == "done-all-four" else "REQUIRED"),
        "required_artifacts": required_artifacts(phase),
        "automated": False,
    })

manifest = json.loads((DASH / "data.json").read_text())
claims = {row["claim_id"]: row for row in manifest["claims"]}
courses = {}
for course_id, label, priority in (("humgeo", "AP Human Geography", 1), ("apwh", "AP World History", 2), ("apush", "AP US History", 3), ("psych", "AP Psychology", "parallel")):
    claim = claims[course_id + ".blueprint.audit"]
    position = claim["process_position"]
    assert isinstance(position["current_stage"], str) and position["current_stage"].strip()
    courses[course_id] = {"label": label, **position, "as_of": claim.get("observed_at") or claim["status_at"], "detail": claim["value"], "priority": priority}


process = {
    "schema_version": 2,
    "generated_utc": STAMP,
    "label": EDITION,
    "runbook_version": "2026-09-15.1",
    "source_sha256": SOURCE_SHA256,
    "authority_note": "Publication runbook, ASAP edition, 2026-09-01. Version 2026-09-15.1. Requirements only; current course positions are re-earned from the per-course plans.",
    "route": ["content", "p3", "p5", "p6", "p7", "p8"],
    "bar": {"strict_pass_min": 0.95, "severe_fails": 0, "final_run": "cold", "all_checkers_executed": True, "confirm": "Josh"},
    "phases": ASAP_PHASES,
    "stages": stages,
    "asap_stages": ASAP_VIEWS,
    "population_scope": POPULATION_SCOPE,
    "courses": courses,
}

# The only public home for retired phase names: historical label -> ASAP destination.
crosswalk_rows = [
    {"old_id": "p0", "old_name": "Establish authority", "new_ids": ["p0"], "disposition": "cut"},
    {"old_id": "p1", "old_name": "Map the complete course tree", "new_ids": ["p12"], "disposition": "combined"},
    {"old_id": "p2", "old_name": "Price activities", "new_ids": ["p12"], "disposition": "combined"},
    {"old_id": "p3", "old_name": "Generate hosted assets and QTI", "new_ids": ["content", "p3"], "disposition": "split; only bank/QTI gates remain in p3"},
    {"old_id": "p4", "old_name": "Seal the publication plan", "new_ids": ["p4"], "disposition": "cut"},
    {"old_id": "p5", "old_name": "Capture live all-absent state", "new_ids": ["p5"], "disposition": "folded"},
    {"old_id": "p6", "old_name": "Dark publication and exact replay", "new_ids": ["p5"], "disposition": "folded"},
    {"old_id": "p7", "old_name": "Owner-controlled canary enrollment", "new_ids": ["p7"], "disposition": "folded"},
    {"old_id": "p8", "old_name": "Private activation", "new_ids": ["p8"], "disposition": "folded"},
    {"old_id": "p9.1-9.5", "old_name": "Fresh-learner acceptance", "new_ids": ["p7"], "disposition": "folded"},
    {"old_id": "p9.6", "old_name": "Broader enrollment", "new_ids": ["p8"], "disposition": "folded"},
    {"old_id": "p10", "old_name": "Repair and rollback", "new_ids": ["p6"], "disposition": "folded into the gauntlet loop"},
]
crosswalk = {
    "schema_version": 2,
    "generated_utc": STAMP,
    "label": f"Original publication runbook -> {EDITION}",
    "rule": "Historical mappings preserve evidence scope and grant no current ASAP phase credit.",
    "stage_ids": [phase["id"] for phase in ASAP_PHASES],
    "counts": {"total": len(crosswalk_rows)},
    "rows": crosswalk_rows,
}

training = {
    "schema_version": 1,
    "generated_utc": STAMP,
    "what_this_is": "Register of training and eval corpora for the course-build model program: the catalog, never the data.",
    "boundary": "No corpus file is ever published to this site. A SHA-256 here lets a holder of the private bytes verify identity.",
    "assets": [
        {"id": "repair_pairs.v0", "purpose": "Repair model: failing item + structural repair + accepted retry, full content inline.", "rows": 431, "sha256": "6f60e664f94aee78d7ecbba20ebe09a05714077e282495999c37daea0efd963a", "snapshot": "2026-08-26", "status": "GO at pilot scale", "home": "Alpha workspace, training-data census 2026-08-26"},
        {"id": "prescreen_labels.v0", "purpose": "Verdict prediction: predict the factory verdict before spend.", "rows": 444, "sha256": "257a95ca64010f493000fd59ff7e28ebc146446c4984ebe14aeced9f5e885121", "snapshot": "2026-08-26", "status": "NOT trainable yet: 437 pass vs 7 fail — failures get repaired out of the bank", "home": "Alpha workspace, training-data census 2026-08-26"},
        {"id": "decision_events.v0", "purpose": "Content-free typed controller events, each source-traceable to its ledger line.", "rows": 161, "sha256": "efa01c2024cd99146b731340ab999f8b592546181665d2d294bfdc77d812ac22", "snapshot": "2026-08-27", "status": "GROWING with publication-route events", "home": "Alpha workspace, decision-log v0 2026-08-27"},
        {"id": "historical_fails.v0", "purpose": "Mine the fail class for verdict prediction.", "rows": None, "sha256": None, "snapshot": None, "status": "PLANNED, not started", "home": "Workspace receipts and git history"},
        {"id": "cross_course_verdicts.v0", "purpose": "Verdict evidence for APWH, APUSH, and Psychology.", "rows": None, "sha256": None, "snapshot": None, "status": "PLANNED, not started; historical assessment receipts are the named leads", "home": "Private evidence homes"},
    ],
    "observability": {"langfuse": "https://us.cloud.langfuse.com", "evidence_repo": "https://github.com/joshuadurey-del/ap-ss-evidence"},
}

training["assets"].extend([{'id': 'article_labels.v2', 'purpose': 'Article labels', 'rows': 640, 'sha256': '2f0f6d09eb1dd99949a42a8c481b6df24005cf6eb8ad32b567a4f730d1a77630', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}, {'id': 'prescreen_labels.v2', 'purpose': 'Prescreen labels', 'rows': 2551, 'sha256': 'da19dd044caf0a9f80494acfb5e0b8f0f1d0b6c4dc00ae483bf9075caedcdfb4', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}, {'id': 'regen_pairs.v2', 'purpose': 'Regen pairs', 'rows': 1945, 'sha256': 'adbb8fc14c56cd011372163eabdda428747f11c0418439d7da551f47f57ee61d', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}, {'id': 'repair_pairs.v2', 'purpose': 'Repair pairs', 'rows': 361, 'sha256': '1a1256d47666c0b6b42c029c055a071a0015d9812d23f073db3fd9bb3d29536b', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}, {'id': 'unverified_pool.v2', 'purpose': 'Unverified pool', 'rows': 468, 'sha256': '587e5e8b436ae44ae577c587a4e22dc7522891c245c4f2addf788b7329297e5e', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}, {'id': 'write_labels.v2', 'purpose': 'Write labels', 'rows': 834, 'sha256': '7cb3a282edabbe8f566b4443e320c160ddd73512491b56844f7e79f16ae518a0', 'snapshot': '2026-09-08', 'status': 'COMPILED; training readiness not assessed', 'home': 'Private Alpha workspace, v2 corpus register'}])

assert [phase["id"] for phase in ASAP_PHASES] == ["p0", "p12", "p3", "p4", "p5", "p6", "p7", "p8"]
assert {stage["id"] for stage in stages if stage["state"] == "cut"} == {"p0", "p4"}
assert next(phase for phase in ASAP_PHASES if phase["id"] == "p12")["state"] == "done-all-four"

for name, document in (("process.json", process), ("crosswalk.json", crosswalk), ("training.json", training)):
    destination = DASH / name
    destination.write_text(json.dumps(document, indent=1) + "\n")
    json.load(destination.open())
    print(name, destination.stat().st_size, "bytes, valid")
print("crosswalk rows:", crosswalk["counts"]["total"])
