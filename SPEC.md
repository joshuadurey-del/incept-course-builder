# Incept Course Builder — Spec Sheet

| | |
|---|---|
| **Version** | 2026-09-14.8 (tracks the publication runbook contract version) |
| **Status** | Working spec. Changes after the first course ships through it. |
| **Product** | One command installs a local workspace and dashboard on macOS; any tool-capable agent then builds one course through four steps on Alpha's native factory. |
| **Users** | The course owner first; every authorized Alpha builder next. No person names, no one user's history, no one machine's paths anywhere in the package. |
| **Not in scope** | A second generator, judge, publisher, scheduler or gate. Course, spend or release authority. Any per-user firewall or zone tooling. |
| **Governing route** | The ASAP publication runbook, in plain names: align (blueprint, tree, pricing), content, bank gates, publish dark, cold QC, walk and accept, demo and open. Phase ids appear only in machine files. |

Readers: a builder deciding whether to install; an agent deciding what to do next. Both read the same rows.

## 1. The method

You build a course the way a good teacher does. Decide what students must know, write the test, map the units, write lessons that get students past the test, then put it in front of them. The Course Builder is that method installed, with the factory doing the heavy lifting and a receipt closing each step.

| Step | Teacher language | Factory phase | Closes when |
|---|---|---|---|
| 0 | Onboard and discover | setup, align | Mission recorded; credentials inventoried by name; every content family counted or marked UNMEASURED; existing material located |
| 1 | Standards, essential knowledge, assessments | align | Blueprint reconciled on nine dimensions; coverage matrix has no orphan; media rule written |
| 2 | Course map | align | Profile, tree and pricing exist for this course; every unit has an assessment milestone; owner launch path named |
| 3 | Lessons with checks | content, bank gates | One lesson proven end to end; every article has five judge-passed checks; every form complete with one owner; bank gates pass on one candidate SHA |
| 4 | Host and present | publish dark, cold QC, walk and accept, demo and open | Published dark with three receipts per write; cold QC at the bar with failures triaged; owner walk and XP check; designated reviewer decision; enrollment read back |

## 2. Requirements

### R1. Deterministic loop (agent-neutral)

- R1.1 A script, not the agent, chooses the step. `next.py` reads the workspace receipts and prints one card: goal, ordered actions, files to load, skills, tools, the receipt template, and the exact close command.
- R1.2 A step closes only through `next.py --close <step> --receipt <file>`. The receipt is validated field by field (references non-empty, hashes 64 hex, times ISO UTC, counts integers, exact literals where required). Empty templates are refused.
- R1.3 No skipping. Closing step N while an earlier step is open returns HOLD naming the open steps.
- R1.4 Receipts are written only by the script into `receipts/`. Hand edits are out of contract.
- R1.5 The same loop is delivered to every host: the launch prompt leads with it; the workspace carries `AGENTS.md` (Codex) and `CLAUDE.md` (Claude Code) with identical text; Hermes and custom hosts receive it through the prompt file.
- R1.6 The dashboard shows the step table and the current card from the same script. Counts come from receipts, not from prose.

### R2. Start from what exists

- R2.1 Every course, new or existing, walks steps 0 to 4 in order. Existing work does not skip a step; it closes the step faster.
- R2.2 Steps 1, 2 and 3 require an intake file before they close. Every existing piece is sorted into one bin: keep, modify, replace or discard.
- R2.3 The bin is decided by the named factory check (provenance scan, blueprint lint and oracle, rubric hard gates, judge receipt, bank gates), never by opinion. Keep and modify carry the passing check receipt; discard carries the rule that dropped it.
- R2.4 Licensed source text is discarded before authoring starts. The course writes its own.

### R3. Templates (so a small model fills, not designs)

| Artifact | Template | Owner |
|---|---|---|
| Mission | `templates/mission.json`: course, framework, learners, standards, families, existing material, approved sources, release approver role | ours |
| Intake row | `templates/intake-rows.json`: id, kind, bin, check, receipt or reason | ours |
| Blueprint | `course-blueprint/v1.2` schema, sixteen sections, nine mandatory; lint and oracle | factory |
| Course profile | course profile JSON with UNMEASURED placeholders; the tree is TimeBack's own course, components, resources | factory pattern |
| Titles | `templates/titles.json`: from the framework titles file, never invented | ours over factory data |
| Article | EK-Article template v1.1 and its binary rubric, pinned by repository, ref and sha256 in `templates/article-template.json` | factory |
| Five checks | `templates/five-check-set.md`: one judge request per check, four options, one key, distractors from named misconceptions, rationale each | ours over the judge contract |
| Forms | `templates/form-templates.json`: quiz, unit test, mock; numbers read from the blueprint and framework, never invented | ours over factory data |
| Stimulus | data table, quoted source or figure in the shape two live courses render | factory |
| Receipts | `templates/receipts/<step>.json`, generated from the step table so template and validator cannot drift | ours |
| Credentials | `templates/credentials.example.env`: names only | ours |

### R4. The numbers come from the blueprint

- R4.1 Lessons: one per essential knowledge statement, grouped by framework topic and unit. The coverage matrix is the check.
- R4.2 Article or video: the blueprint content mix names each kind's job. Every lesson gets an article. A video is added only where the blueprint names a demand the article cannot meet, decided per lesson in step 1 before any media job.
- R4.3 Stimuli: the retrieval format map assigns format by knowledge type; the share per form comes from the test blueprints that mirror the exam. Three shapes render today.
- R4.4 Stimulus sources, in order: data the course already owns; public-domain or openly licensed sources on the approved list, cited in the caption; constructed data for practice items when internally consistent and labeled. Never licensed text or figures. Never a fact the stimulus does not show.

### R5. QC embedded from the start

| Artifact | Check inside the template | Runs |
|---|---|---|
| Blueprint | lint, nine-dimension reconciliation, coverage matrix | before step 2 |
| Course map | oracle diff; every unit has a milestone | before step 3 |
| Article | rubric hard gates (accuracy, EK alignment, scope); compiler structure | at authoring |
| Item and check | free prescreens, then the judge | at authoring, before banking |
| Form | answer shape, key balance, option length, no two items from one standard | before step 4 |
| Video | the video skill's free battery | before upload |
| Publish batch | capture, execute with readback, replay with zero writes | every write |
| Published course | cold course QC at the bar; walk and XP | before release |

The standard: a known-bad fixture proves each gate fires.

### R6. Publication contract (publish dark through demo and open)

- R6.1 Every native write is one sealed operation with three receipts: capture prior state (zero writes), execute once with readback (verified and writes counts), replay the identical operation (writes zero). One plan digest per operation.
- R6.2 Operator code lands in its own PR; the plan digest and constants land in a separate seal PR.
- R6.3 One writer per course surface, enforced by the writer lock. A refusal is correct and is never cleared by hand.
- R6.4 Interrupted execute: classify the pending row read-only and resume through the operator's admission path. Never resend.
- R6.5 Cold QC failures are sorted into content, context, checker, provider or selection before any repair. Removal is never a passing verdict. Checker fixes are factory code and need their own review and landing.
- R6.6 Walk and accept keeps the owner walk on one test account with three XP cases and a reload. Demo and open keeps the designated reviewer decision. Nothing automates the flip.

### R7. Installer and onboarding

- R7.1 One command on macOS: installs `gh` and Python privately if missing, signs in to GitHub, verifies an alpha.school email and private-repo access, downloads the release at an exact commit with checksums.
- R7.2 Onboarding asks for step 1 inputs in plain questions and writes `mission.json`; unknowns stay null. It reports which credential names are present (TimeBack, AWS profile, GitHub) and offers hidden entry for TimeBack into an owner-only credential file. Values never appear in settings, prompts, Git or the dashboard.
- R7.3 Non-interactive hosts: `install.sh --no-onboard`, then `incept-course-builder onboard --mission-file <filled mission.json> --agent <codex|claude|hermes|prompt>`. No prompts; the Step 0 receipt is written from the file.
- R7.4 The GitHub sign-in must carry the `user:email` scope so the installer can verify the alpha.school address. A host without a terminal cannot add that scope itself; run `gh auth refresh -h github.com -s user:email` once in a terminal, then the agent path works. A token from the environment that lacks the scope makes the installer stop with that instruction.
- R7.5 `incept-course-builder build` scans installed tools and skills, installs missing bundled skills without touching existing ones, writes the agent adapters into the workspace, and launches the chosen agent with the loop and the current card.
- R7.6 The package carries no person names, usernames, or machine or external-drive paths. A package test fails on any of them. Roles are used instead: course owner, merge approver, designated reviewer, fleet contact, platform lead.
- R7.7 No firewall, zone classifier or personal-tooling step is part of the install.

## 3. Evidence behind the spec

- Nine sealed native operations on the HumGeo v3 course, 2026-09-12 to 2026-09-14, each with capture, execute and zero-write replay receipts; the final census capture listed every replay receipt as a precondition.
- The 2026-09-10 dark publication stopped on HTTP 422 after 9,654 of 12,552 rows; the namespace re-cut, digest seal and read-only preflight fixed it, and no landed operation repeated the failure.
- First-pass PR rates since 2026-08-01: ap-one course PRs 117 of 163, humgeo-rebuild 65 of 81, apwh-blueprint-build 64 of 65. First-pass PRs are single-commit with a sealed digest and one bot approval; amended PRs are operator-plus-plan PRs or integration PRs over ten commits.
- Four pilot items on HumGeo caught a QC poster dropping the stimulus field before a 130-item campaign.
- 1,113 HumGeo videos were generated before the media decision; the editorial packet then recommended cutting all of them.
- The first cold QC run judged 7,070 items: 1,026 failed, including 36 provider errors, so failures needed triage before repair.

## 4. Machine summary

```json
{
  "spec_version": "2026-09-14.8",
  "route": ["content", "p3", "p5", "p6", "p7", "p8"],
  "route_names": {"p12": "align", "content": "content", "p3": "bank gates", "p5": "publish dark", "p6": "cold QC", "p7": "walk and accept", "p8": "demo and open"},
  "steps": ["onboard", "discover", "s1-blueprint", "s2-map", "s3-pilot", "s3-content", "p3-bank-gates", "p5-publish-dark", "p6-cold-qc", "p7-walk", "p8-release"],
  "loop": ["next.py", "do the card", "fill the receipt template", "next.py --close <step> --receipt <file>", "repeat"],
  "intake_bins": ["keep", "modify", "replace", "discard"],
  "write_contract": ["capture", "execute_with_readback", "replay_zero_writes"],
  "triage_classes": ["content", "context", "checker", "provider", "selection"],
  "forbidden_in_package": ["person names", "usernames", "machine paths", "external-drive paths", "credential values", "firewall steps"]
}
```
