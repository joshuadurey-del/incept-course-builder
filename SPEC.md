# Incept Course Builder — Spec Sheet

| | |
|---|---|
| **Version** | 2026-09-15.1 (package); contract 2026-09-15.1 |
| **Direction** | One typed line, a few hours, a course live on TimeBack at the full Incept bar. The front end is a 1995 terminal program. The back end is a make-style dependency graph of files: every step a target, a check and a recipe. A model is called only on a work order, as a compiler, and a script decides. No human in the loop. |
| **Status** | Working spec. Changes after the first course ships through it. |
| **Product** | One command installs the builder on macOS, shows a numbered menu of course ids read live from the factory, takes three hidden credential strings, and builds the course through four steps on Alpha's native factory. Run it again to continue. |
| **Users** | The course owner first; every authorized Alpha builder next. No person names, no one user's history, no one machine's paths anywhere in the package. |
| **Not in scope** | A second generator, judge, publisher, scheduler or gate. Course, spend or release authority. Any per-user firewall or zone tooling. |
| **Governing route** | The ASAP publication runbook, in plain names: align (blueprint, tree, pricing), content, bank gates, publish dark, cold QC, walk and accept, demo and open. Phase ids appear only in machine files. |

Readers: a builder deciding whether to install; a maintainer reading `course.rules`. Both read the same rows.

## 1. The method

You build a course the way a good teacher does. Decide what students must know, write the test, map the units, write lessons that get students past the test, then put it in front of them. The Course Builder is that method installed, with the factory doing the heavy lifting and a receipt closing each step.

| Step | Teacher language | Factory phase | Closes when |
|---|---|---|---|
| 0 | Onboard and discover | setup, align | Mission recorded; credentials inventoried by name; every content family counted or marked UNMEASURED; existing material located |
| 1 | Standards, essential knowledge, assessments | align | Blueprint reconciled on nine dimensions; coverage matrix has no orphan; media rule written |
| 2 | Course map | align | Profile, tree and pricing exist for this course; every unit has an assessment milestone; owner launch path named |
| 3 | Lessons with checks | content, bank gates | One lesson proven end to end; every article has its profile count of judge-passed checks; every form complete with one owner; bank gates pass on one candidate SHA |
| 4 | Host and present | publish dark, cold QC, walk and accept, demo and open | Published dark with three receipts per write; cold QC at the bar with failures triaged; owner walk and XP check; designated reviewer decision; enrollment read back |

## 2. Requirements

### R1. The build (no model in the loop)

- R1.1 `make.py` reads `course.rules`, a build file in the 1995 shape: `target : prerequisites` followed by indented recipe rows. Six verbs: `ask`, `fetch`, `render`, `run`, `author`, `check`. A target is rebuilt when it is missing, older than a prerequisite, or failing its check. Run again any time; only what is missing or stale rebuilds. A prerequisite must be defined above the target that needs it, so one pass builds everything; the parser refuses a rules file that breaks this.
- R1.2 Every value follows one order of resort, and a model is next to last: factory bytes fetched at live main and pinned by sha; derivation from those bytes (copy, select, count, render); the answer file; the owner, asked once and saved, never asked again; a model called on a work order and checked by a script, three tries; a person. Steps 0 to 2 never pass the fourth level by construction; a package test proves it on a throwaway install with no model configured.
- R1.3 Every target carries a provenance: `fetched`, `derived`, `answered`, `authored` or `person`. The last line of every run prints the counts. `authored 0` is the normal case when the factory's bytes are complete; a rising count is the signal that bytes are missing upstream, and the work-order list says which.
- R1.4 Receipts are built from files by `receipt.py`, never typed, and validated field by field (references non-empty, hashes 64 hex, times ISO UTC, counts integers, exact literals where required). Each of the eleven steps closes with `receipts/<step>.json`; a later step's rule names the earlier receipt as a prerequisite, so skipping is impossible by construction.
- R1.5 Five stops and nothing else is printed to the owner: 0 the course is live; 1 a check failed (target, check, observed, expected); 2 network or sign-in (the exact command); 3 work orders open (file, what, shape, last finding); 4 an answer is needed (the one line to add). No ids, hashes or state codes outside those lines.
- R1.6 The local page is a glance view over the same files: a progress bar, the five step groups (done, building, upcoming), the next target, the provenance counts, open work orders, and the course map with every lesson's parts labeled. It reads `make.py --status`; it never launches work or calls paid services.
- R1.7 Typing the one command is the owner word. The build records a standing authorization (account, time, course, scope: factory spend, pull requests and merges, native writes with three receipts, publish dark, open when every receipt is valid, until the course is live) and every paid call, landing and native write cites its sha. It grants no skip of any gate.
- R1.8 What the factory has not committed becomes a work order: `workorders/<target>.json` with every fact the artifact needs and its exact shape, sized for a local 30B model. `author.py` fills it when an author seat exists (a local OpenAI-style server on port 1234 or 11434, detected once and recorded, or any `{prompt_file}` command), the free prescreen checks the result, the paid judge decides, and a refusal re-opens the lesson for another pass, three at most. What no seat can fill waits for a person. Too big means split, never escalate.
- R1.9 Authored content pays down intelligence debt: a judged, accepted artifact is handed to the course's producer route so the next build of the same course reads it as bytes. An authored article stays open until its disposition row lands; the build says so in one line.
- R1.10 The walk and the open decision are mechanisms, not words. The learner-acceptance operator walks start, middle, end and the three XP cases on the profile's owner canary account and reads each back. The open decision is a rule over receipts: every receipt from bank gates through the walk valid and cold QC with zero severe failures; then the activation operator runs and reads back.
- R1.11 Course facts are never hard-coded. Anything that differs between courses (source repository, blueprint path, checks per article, operators, canary accounts, forms) is read from the course profile, blueprint or pricing manifest at live main. The profile names its own source repository and operators, so nothing beyond the course id is asked.
- R1.12 Tools are interchangeable across courses. Every shared tool takes `course-rules.json` (`--rules`: task verbs, skill-code shape, article sections, checks per article, spec-code patterns, each with its source). The package ships rules for the known courses; step 1 writes one for a new course. A tool that refuses a course is a defect in the tool, never a reason to skip a gate.
- R1.13 An operator the profile marks not implemented is a factory pull request, never authored here. The build stops at that target with one line and resumes when the profile reads implemented.

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
| Course map | `course-map.json` built by `course_map.py`: units, topics, lessons, gates and milestones read from the ap-one price manifest, gate map and framework titles | ours over factory data |
| Titles | `templates/titles.json`: from the framework titles file, never invented | ours over factory data |
| Article | EK-Article template v1.1 and its binary rubric, pinned by repository, ref and sha256 in `templates/article-template.json` | factory |
| Course rules | `templates/course-rules.<course>.json` (shipped for known courses; `course-rules.template.json` for a new one): the course facts every shared tool reads with `--rules` | ours over course bytes |
| Checks | `templates/check-set.md`: the check count per article is read from the course profile (`article_checks.required_per_substantive_concept_article`; HumGeo 5, APWH 1), one judge request per check, four options, one key, distractors from named misconceptions, rationale each | ours over the judge contract |
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
| Item and check | free prescreens, then the judge; count per article from the course profile | at authoring, before banking |
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

### R7. Installer

- R7.1 One command on macOS: installs `gh` and Python privately if missing, signs in to GitHub, verifies an alpha.school email and private-repo access, downloads the release at an exact commit with checksums, and starts the build.
- R7.2 The build asks for exactly two things and only when absent: the course id, from a numbered menu of the ap-one manifests at live main; and the TimeBack client id, client secret and organization id, with hidden input into an owner-only credential file. `--course <id>` on the install line and the names in the environment remove every prompt. The Content Factory key is asked only when an authored check needs the paid judge.
- R7.3 `incept-course-builder` builds; `open` shows the local page; `status` prints the build as JSON; `credentials` re-enters the TimeBack strings; `stop` ends the local page. There is no onboarding, no agent choice and no settings file.
- R7.4 The GitHub sign-in must carry the `user:email` scope so the installer can verify the alpha.school address. A host without a terminal cannot add that scope itself; run `gh auth refresh -h github.com -s user:email` once in a terminal.
- R7.5 Re-running the install command updates the package in place; the workspace and the credential file are preserved and the next build continues where it left off.
- R7.6 The package carries no person names, usernames, or machine or external-drive paths. A package test fails on any of them. Roles are used instead: course owner, merge approver, designated reviewer, fleet contact, platform lead.
- R7.7 No firewall, zone classifier or personal-tooling step is part of the install.

## 2b. Where the build stands and what remains

Measured on 2026-09-15 by running the build unattended against AP World History on a throwaway install with no model configured.

| Layer | Today (2026-09-15.1) | Remaining |
|---|---|---|
| Install to course map | One menu number and three hidden strings; 41 targets fetched or derived; receipts onboard, discover, step 1 and step 2 valid; `authored 0` | none |
| Lessons | 176 lessons: 126 articles copied from accepted disposition rows, 176 lessons with a judged check each, 176 prescreens; 50 lessons whose article the producer QC rejected stand as work orders for the author seat | the author seat fills them when a local model is present; each authored article then needs the course producer's disposition row (factory route) |
| Bank gates | answer shape, key balance (incept-test-builder's own module), option length and QTI byte-match run on the fetched banks; 1,988 items | none |
| Publish dark | the profile names the operators; APWH's status reads not implemented, so the build stops with one work order line | the factory's operator PR for the course; HumGeo's operators exist and run through the same rows |
| Cold QC, walk, open | rules written against the measured fleet QC contract and the operator twins' command lines | first exercised on a course whose operators are implemented |

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
  "spec_version": "2026-09-14.14",
  "tool_rule": "every shared tool takes --rules <course-rules.json>; no course list in any tool",
  "procedure_rule": "rows of run|write with expect and on_fail; exceptions via next.py --exception compose the owner message with why and next step",
  "owner_message_rule": "composed by next.py: what is needed, how to give it; no ids, hashes, codes or paths",
  "drafting_rule": "draft locally, prescreen free, judge in parallel batches; paid calls are judge calls only",
  "ask_rule": "resolve_from sources read at live main and cited per field before any owner request; next.py --request gates it",
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
