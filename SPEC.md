# Incept Course Builder — Spec Sheet

| | |
|---|---|
| **Version** | 2026-09-15.70 (package); contract 2026-09-15.1 |
| **Direction** | Create and launch new courses through native factory tools. The small test exercises the real TimeBack pipeline with bounded content. Paid calls, course creation, learner acceptance and launch have explicit owner decisions; elapsed time and live success are measured per run. |
| **Status** | Working spec. Changes after the first course ships through it. |
| **Product** | One command installs the builder on macOS and creates and launches new courses, offers a small full-pipeline test, and resumes only its own builds. Existing courses are never imported or monitored. |
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
- R1.7 Starting or resuming a build authorizes preparation only. The test route binds paid calls to a separate exact cost envelope, creation to its frozen new-object plan, and launch to learner acceptance. A menu choice or entered course ID cannot grant spend, merge, or existing-course write authority. Governed legacy engine callers retain their own explicit authorization contract.
- R1.8 What the factory has not committed becomes a work order: `workorders/<target>.json` with every fact the artifact needs and its exact shape, sized for a local 30B model. `author.py` fills it when an author seat exists (a local OpenAI-style server on port 1234 or 11434, detected once and recorded, or any `{prompt_file}` command), the free prescreen checks the result, the paid judge decides, and a refusal re-opens the lesson for another pass, three at most. What no seat can fill waits for a person. Too big means split, never escalate.
- R1.9 Authored content pays down intelligence debt: a judged, accepted artifact is handed to the course's producer route so the next build of the same course reads it as bytes. An authored article stays open until its disposition row lands; the build says so in one line.
- R1.10 The walk and the open decision are mechanisms, not words. The learner-acceptance operator walks start, middle, end and the three XP cases on the profile's owner canary account and reads each back. The open decision is a rule over receipts: every receipt from bank gates through the walk valid and cold QC with zero severe failures; then the activation operator runs and reads back.
- R1.11 Course facts are never hard-coded. Anything that differs between courses (source repository, blueprint path, checks per article, operators, canary accounts, forms) is read from the course profile, blueprint or pricing manifest at live main. The profile names its own source repository and operators, so nothing beyond the course id is asked.
- R1.12 Tools are interchangeable across courses. Every shared tool takes `course-rules.json` (`--rules`: task verbs, skill-code shape, article sections, checks per article, spec-code patterns, each with its source). The package ships rules for the known courses; step 1 writes one for a new course. A tool that refuses a course is a defect in the tool, never a reason to skip a gate.
- R1.13 An operator the profile marks not implemented is a factory pull request, never authored here. The build stops at that target with one line and resumes when the profile reads implemented.
- R1.14 Startup and test controls follow R7.3. During a governed engine build, one screen shows the course, completed and missing work, current action and saved inputs. The local page describes only the selected Builder-owned run; foreign workspaces are not adopted or monitored.
- R1.15 No step starts until the previous step's receipt exists. Every rule declares its step; the page and the screen group by that declaration. Setup and discover share the Step 0 gate because the setup receipt needs the course profile. A step that is open shows k of m pieces and names what is still to build.
- R1.16 Every course carries at least one full mock exam whose section counts match the blueprint's exam form; lessons do not close without it. A file the factory has not produced for a course (a 404 at live main) or a profile field it does not carry is a work order in owner words, never a sign-in error.

- R1.17 The Step 1 gate is the course's own contract: the conformance oracle runs inside the pinned checkout and the step passes when no FAIL row is NEW against the course's committed conformance report (`conformance/conformance_report.md`). A recorded FAIL row is open work in the source repository; it prints on the screen with the factory's closer and the counts measured from the same bytes, and it never stops the build. A row the report does not carry stops the step as a work order.
- R1.18 The write layer the oracle asks for is built by the build (`write_layer.py`, three `run` targets in Step 3). From the A-116 carrier contract it splits the mandatory EKs into declare (an assess-tier task with a passing receipt, declared by script with zero calls), draft (one terminal constructed-response task per remaining EK, appended as an ordered `write_activity_key` list, which the platform serves), no-host (an EK with no served lesson: request brief) and factory. A-097 gets one row-6 and one row-7 drill on free lessons before the first complexity lesson; rubric rows allowed per host follow spine rank; row 9 is authored only inside the assembled three-part task, in the factory's own link-state wording (A-099: every shipped row-9 criterion asks for the link state), never free-hand in a drill. The free prescreen reads the oracle's own row-wording rules and its non-scored co-tag rule from the pinned oracle; the judge is the factory's own request and poster; a pass counts only with both check counts on the receipt. The record check also reads the oracle's own SAQ rules (every short-answer part tagged [R1:task-verb=identify|describe|explain], A-073; rows 2, 3, 8 and 5, 6, 7 never score a short-answer task, A-094), and an already accepted record is re-checked on every pass: one the rules now refuse is removed and re-drafted, so no free-draft record from an earlier day reaches the landing. Landing resets its staging clones to each repository's live main (a refused attempt leaves nothing behind) and stages both with every untouched row byte-identical, then performs the platform repository's own s4 re-pin in the same change (its profile consumer prescribes it: the profile's write-activity, map and delivery-package hashes re-derived from the staged bytes by the factory's capture function, the consumer's pinned constant and the XP module's pinned total moved with dated comments, the XP price manifest re-emitted by the factory's XP tool, and the course's own tests run in the staged clone as the proof), and when one of those platform tools refuses the staged bytes the landing is held and reported with the tool's own words and the cited read sites, nothing pushed, proves the rows on the staged bytes, opens two pull requests, merges the source repository first, and re-pins.
- R1.19 The graph layer closes A-202 from the factory's committed pieces (`graph_layer.py`, four `run` targets in Step 3). It pins the merged knowledge graph at the graph repository's live main and refuses unless the pre-delta copy is the graph the committed census pins by sha; lists the concepts and atoms the typing overlay lacks; types atoms by the slot rule and derives every concept field the README rules decide, while the three judged fields (history_kct, theme, scale) are author-seat work orders recorded as worker-classified with a rationale, never a replay of the rule the factory refused to certify; recounts the census and edge map whole from the graph with the old source kept beside untouched sections; adds path flags to the factory's edge exporter and re-exports; lets the oracle's own join function name the joins and asks the seat for a three-beat bridge or a typed refusal per unbridged join; rebuilds the carrier contract fail-closed, proves every row against the baseline, and lands one pull request. Once the oracle no longer records A-202 on the pinned bytes, the plan records nothing and apply lands nothing, whatever an earlier build left in the graph folder.
- R1.20 A local server that lists no model is not an author seat, however it answers a probe. Every model call names a listed model. A seat failure gives the try back; only a refused draft spends one. Orders whose tries were burned by a seat that never answered are restored by the build itself.
- R1.21 Nothing lands except through the landing gate (`write_layer.gate`): the pull request head is the exact commit this build pushed; every check on that commit is finished and green and at least one check exists (the gate waits up to 45 minutes, longer than the platform repository's 21-minute offline test run); the receipt (`receipts/landing-<repo>-<n>.json`: head, checks, proof, authorization) is written before the merge and a LANDING line prints the moment the gate passes, not at the end of the run. The graph layer's apply and the write layer's land merge only through it; a held gate is reported with its reason and nothing lands.
- R1.22 A terminal task is a slot fill, not a free draft. The seat supplies only the history (for parts A, B and C: the question, the object, two examples, the generic non-answer and the full-credit answer) into the factory's passing three-part shape (`templates/terminal-order.md`, copied from a shipped task that passed every judge check); the script assembles the record: rows R1+R4 for A, R1+R9 with the course's own link-state wording for B and C, one point each summing to three, skill-mapped rows, no documents. The free prescreen refuses what the judge refuses before any paid call (openings, stimulus words, framework codes, sentence counts, an answer that names none of its examples, repeated parts); a judge refusal comes back to the order as that check's own question from the pinned engine's `qc_checks.json`. The seat's only fact source is the lesson's framework statement, its accepted article sections and its gate checks. When `AUTHOR_PILOT` is set in the answer file (the owner install sets 10), each pass tries that many open tasks and writes the pilot result (tried, passed, rate, refusal tally) to `write/batch-state.json` for the screen; at 90 percent or more the build clears the cap itself and the rest run at full slots; under it the template is refined before the next pilot. The two rubric-row drills are slot fills in the same way (`templates/drill-row7-order.md`, `templates/drill-row6-order.md`, copied from the course's own shipped sourcing and grouping drills): the seat supplies the documents as original summaries in its own words plus the sourcing move or the grouping, and the script builds the record with the course's row-7 or row-5 plus row-6 wording, the shipped closing line (covered by the criterion, so every sub-part of the prompt is scored: judge check F1), and every document repeated in the stimulus. A stimulus reference is refused only when the words point at a document the student does not have; a lesson's own use of a word such as sources is content. The default seat is hermes on DeepSeek V4.1 Flash through OpenRouter.
- R1.23 An accepted seat draft stands until the factory supplies its own row. When a prerequisite such as the re-fetched article manifest makes a lesson target stale and the tool still reports no factory-accepted row for it, the build keeps the existing draft whose work order ends in a judge acceptance, byte for byte, as an authored target; it never re-drafts or re-judges it. Only a draft the judge never accepted is rebuilt. (Found 2026-09-16: one manifest re-fetch re-drafted 20 accepted articles.)

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
| Write task | shape, rubric row tags inside the allowed set, the oracle's row-wording rules and co-tag rule, documents shipped and labelled, declaration exact; then the factory judge | at authoring, before landing |
| Graph typing and bridge | enums, rationale on every judged field, scale where the template requires it; three full beats or a typed refusal class | at authoring, before the join count |
| Video | the video skill's free battery | before upload |
| Publish batch (apone route) | capture, execute with readback, replay with zero writes | every write |
| Published course (lean route) | replay identity and readback; confirmed lesson-plan recreation | before cold QC |
| Cold QC burndown | policy-directed split, redraft, replacement and remeasurement; stop on instrument-only or unchanged failures, or the run cap | after publication |
| Published course | cold course QC at the bar; walk and XP | before release |

The standard: a known-bad fixture proves each gate fires.

### R6. Publication contract (publish dark through demo and open)

- R6.1 Every sealed AP One native write is one sealed operation with three receipts: capture prior state (zero writes), execute once with readback (verified and writes counts), replay the identical operation (writes zero). One plan digest per operation.
- R6.2 Operator code lands in its own PR; the plan digest and constants land in a separate seal PR.
- R6.3 One writer per course surface, enforced by the writer lock. A refusal is correct and is never cleared by hand.
- R6.4 Interrupted execute: classify the pending row read-only and resume through the operator's admission path. Never resend.
- R6.5 Cold QC failures are sorted into content, context, checker, provider or selection before any repair. Removal is never a passing verdict. Checker fixes are factory code and need their own review and landing.
- R6.6 Walk and accept keeps the owner walk on one test account with three XP cases and a reload. Demo and open keeps the designated reviewer decision. Nothing automates the flip.

- R6.7 The cold QC burndown follows `qc_burndown.py` and the course rules. `qc_burndown_max_runs` caps runs; instrument-only and unchanged failure sets stop the loop.
- R6.8 Two routes reach `COURSE-LIVE`: `apone` uses sealed AP One operators; `lean` uses the course repository publisher. `@step` resets route filtering, so the release decision and activation rows are shared. `native_roles.activation.mode` selects the operator or PUT. Every `ask` and the human walk stay unchanged.
- R6.9 Lean Step 3 uses the shared materialize, author, prescreen, judge, forms and completion tools. The map joins `out/publish/unit_N/course_subtree.json` article resource IDs to `article_stim_manifest.json`; curriculum codes are read, never inferred from IDs. `publish.inventory` declares course-relative JSON paths for `articles` (disposition rows), `questions` (accepted handoff items), `blueprint`, `mock_bank`, `gate_bank`, `pricing`, `coverage`, and `qti_receipts`, retaining the existing tools' schemas. Missing content opens work orders; missing pricing, coverage or QTI evidence reports UNMEASURED and cannot close its check.
- R6.10 Lean bank gates read exactly `publish.bank_path` for every ruled unit under `.make/src`. Candidate identity binds source revision, paths and bytes. Answer shape, key balance, option length and QTI checks bind that candidate. Each report binds the candidate, option rules and checker bytes, plus its QTI evidence or factory checker dependency; target checks rebuild stale reports and receipt validation rejects them; QTI receipts cover the declared bank identities and source hashes. Inventory-only receipts no longer close content or bank gates.
- R6.11 Lean replay repeats the existing publisher's documented idempotent upserts and readback, binding the original push, course ID, source revision and tree digest. AP One retains zero-write replay; upsert counts are not zero-write evidence. `publish/lesson-plans.json` confirms recreation or the existing personalized-plan exclusion with results preserved and successful learner enumeration before cold QC. Listing failures, malformed active-student records or a population at the existing query limit leave enumeration incomplete. Both routes use the same row and receipt validator. Recreation requires boolean success; canonical progress fingerprints must match before and after, following the native projection (omitted results means empty; null or malformed results refuse). Enrollment role/status must be classifiable under OneRoster. Operations and progress list fields must be present before recreation. The walk-time recreate remains.

### R7. Installer

- R7.1 One command on macOS: installs `gh` and Python privately if missing, signs in to GitHub, verifies an alpha.school email and private-repo access, downloads the release at an exact commit with checksums, and opens the startup menu. A saved course never bypasses that menu.
- R7.2 Intake asks for a new course brief or the small test title and owner email. Test service connections save TimeBack, Content Factory and AlphaVideo values with hidden input in the selected owner-only credential file. Native media hosting uses the existing AWS credential provider. Blank entries preserve saved values; unavailable services hold only dependent actions.
- R7.3 Startup offers Start a new course build, Create a new test course, and Resume a course built here. Foreign workspaces stay untouched and cannot be adopted by entering an ID. A new design saves the native mission/brief/work order; its platform identity remains unset until native creation. Only the strict new-course route can publish from this UI; legacy upsert publishers are not reachable by attaching a repository or ID.
- R7.3a The test route has one instructional lesson, article, video, five article checks, four distinct placement/mastery/unit/final MCQs and one graded written response. It uses the actual content/render/QC services, native QTI and TimeBack SDK, XP and owner enrollment. Small populations do not certify a complete AP curriculum. The only ongoing build state shown belongs to this Builder.
- R7.3b Freeze configuration, tools, per-lane requests, approvals and whole responses inside the run. Record actual hosted IDs immediately. Paid requests require a priced, approved envelope including optional item QC, video QC, storage and one learner written-response grade; unpublished prices remain unmeasured. Resume missing transport verdicts with GET-only readback, never blanket resubmission, model substitution or text truncation.
- R7.3c Native preparation mints and freezes every new identity under an exclusive run lock. Creation checks the complete graph for active/deleted collisions and permits only exact collection POSTs. Course/org/owner binding is checked live. Activation permits one exact testing-to-published update only on the course created and read back by this run, after fresh graph/learner checks and explicit owner acceptance. Existing courses cannot be targeted. The test does not claim E2E acceptance from generation, upload or local tests alone.
- R7.3d Before a new render, read the shared principal's active video rows and measured capacity. Cancel only exact owner-confirmed abandoned IDs; preserve other work. A cancellation error remains unresolved until read back, never an automatic retry. Watch uses the pinned native HTML renderer, new conditional uploads, served-byte hashes and the native browser readiness check before learner review; raw video QC remains separately bound to the render.
- R7.4 The GitHub sign-in must carry the `user:email` scope so the installer can verify the alpha.school address. A host without a terminal cannot add that scope itself; run `gh auth refresh -h github.com -s user:email` once in a terminal.
- R7.5 Re-running the install command updates the package in place, preserves every workspace and the credential file, and returns to the startup menu. An explicit `--course <id>` can address only a build created here; it never adopts an existing course.
- R7.6 The package carries no person names, usernames, or machine or external-drive paths. A package test fails on any of them. Roles are used instead: course owner, merge approver, designated reviewer, fleet contact, platform lead.
- R7.7 No firewall, zone classifier or personal-tooling step is part of the install.

### R8. Landing and close-out rules learned on HumGeo (2026-09-17 to 09-20)

- R8.1 The cold QC step computes the reachable ceiling before any redraft: split fails by route (redraftable choice, instrument-defect extended-text, no-topic-code), ceiling = (items - instrument fails) / items. A run within one item of the ceiling is terminal; the remaining instrument fails ride the filing, not a redraft.
- R8.2 A single hosted run is not a trigger. New fails on untouched items need a second run before a redraft campaign (HumGeo run 7: 99 flips, run 8: none).
- R8.3 Small remainders are redrafted in seat: the draft is written into the campaign's response.raw.txt with the drafting model recorded, then gate, emit, judge once. No paid drafting call for fewer than ten items.
- R8.4 Every sealed operation's plan, capture, execute and replay receipts are committed to the course repository as digest-and-count files beside the findings; text that states an execution count cites that path.
- R8.5 The review receipt binds to the exact head. A pin-only commit after an APPROVE takes one more closing slot on the new head (or lands before the review). No owner waiver is invented for it.
- R8.6 Landing prep compares the suite's failure set on origin/main with the head's; an identical set is recorded as pre-existing on base and the landing proceeds through the merge gate with that fact in the cert, instead of refusing.
- R8.7 Waiters count new occurrences of an exact sentinel line; a presence grep on a shared log and any substring match on a status word are refused patterns.
- R8.8 Batch and pin scripts read the current dirnames tuple and digest map from the file with a pattern and append; copied literal anchors are refused.
- R8.9 Video edits: a 202 is queued, not scheduled. The fixer polls finished_at against the submission time, the publish loop runs independently of the render engine, and a service-side full-disk error is recorded as the service owner's incident with no client retry storm (retries do not burn the edit cap).
- R8.10 Resume rule: list live sessions and read the last commit on every tree the handoff names before the first write; two writers split by tree by message.
- R8.11 After any wave that adds or removes course components, recreate every enrolled learner's lesson plan (POST lessonPlans/{id}/recreate); link and resource field edits show live without it.

### R9. Rules learned on APWH (2026-08-04 to 09-21)

- R9.1 Name the student destination and every object kind (videos, practice, checks, mock, writing, XP) in the course profile before the first hand-off. (L1; amends lessons.html, unanchored section "Lessons — the 24 hours after the Psych sync", item 1)
- R9.2 Publish the whole shape and diff source against live, object by object, before calling publish done. (L2; amends lessons.html#humgeo-postassembly-20260916)
- R9.3 Fix the content bar (mock shape, stimulus share, practice cap) in the course profile before the bank is generated. On APWH the mock ruling arrived on day 38 and retired 2,172 items. (L3)
- R9.4 Decide the lesson shape with both the student player and the QC reader in view; never reshape the live course for a reader. (L4; amends retro.html#humgeo-closeout-20260920)
- R9.5 The acceptance instrument (the Faultless Bar) must run from a pushed ref before any content work depends on its verdicts; the step 1 oracle gate fails closed when it does not. (L5)
- R9.6 Run the structural prerequisites (rationales, skill codes) before any paid judge sweep; the order is generate, tag, rationales, verdict, bank. (L6; amends lessons.html#morning-retro-20260910, dispatch card)
- R9.7 Every served item carries a factory judge verdict on its served bytes; the bank gate refuses one without it. (L7; amends lessons.html, unanchored section "What changed")
- R9.8 Read the hosted QC reader's code (checks.py, timeback_reader.py) and run one small hosted job before any structural write; ship the hidden article-text block, static check XML and the stimulus in every judge payload from the first publish. (L8)
- R9.9 Once a namespace publish exists, cold QC judges the native course id, never the source course id. (L9)
- R9.10 The hosted verdict cache is part of the instrument: its key is prompt version, course, question and lesson context, with no cold flag; above about 2,000 items the job record reads FAILED and no email is sent, so the loop polls on report presence. (L10)
- R9.11 Measure the whole item population before quoting a ceiling; a gate-only score hides the largest class. (L12; amends lessons.html#publish-faster-20260920)
- R9.12 Judge fails feed the next generation at once; stop redrafting a code that returns no reasoning after a zero-pass round. (L13; amends lessons.html#morning-retro-20260910, retry card)
- R9.13 Read the stored fatal codes before any paid re-judge; never call the judge poster with an empty slot file, because it judges the whole pool. (L14)
- R9.14 Name the course's own defect classes from its own bytes before reusing another course's scanner; a fixed-string class gets a free scanner before any model critic; a zero from a filter needs a positive control. (L15)
- R9.15 Budget a source fold and re-pin beside every live item wave; a live rewrite breaks the publication envelope, so each wave needs a source landing plus a republish (about 2,300 writes, about 65 minutes on APWH). (L16)
- R9.16 Any write-activity change lands with the source re-pin in the same pull request, or CI is red whatever the content; every course ships a re-pin script. (L17)
- R9.17 Census live ids before any operator embeds items by id; normalize static check XML before publishing it as an asset; verify rendering with a browser click-through against a live hybrid article. (L18)
- R9.18 Video comes first in every lesson; articles carry headings, bold key ideas and a table or figure; a producer rejection is not a content verdict. (L20; amends lessons.html#design-assumption-article-coverage-20260912)
- R9.19 Run every unattended publish detached; re-bind on a recut mismatch instead of stopping; shard operators at about 400 rows. (L21; amends lessons.html#humgeo-postassembly-20260916)
- R9.20 Every step reads the committed factory profile at live main before it may ask the owner anything. (L22; amends lessons.html, unanchored section "Factory-canonical operating rules")
- R9.21 A platform fact learned live becomes a builder rule the same day; the next course reads the list before its first live write. (L23; amends lessons.html#humgeo-postassembly-20260916)
- R9.22 Owner grants are standing authority until the course is live, recorded once in a grant file every window reads; every gate still runs; no clock on the owner's words. (L24)
- R9.23 Local gates are never stronger than the factory's, the certification gate excepted; every local gate runs in shadow; progress is stated only in the runbook's phase names. (L25)
- R9.24 Keep the landing ceremony at its floor: two review rounds at most, no drafts, no merge before the BFF check finishes, recover a capped report from disk. (L26; amends lessons.html#review-28-rounds)
- R9.25 Every review finding carries a tested, deterministic, class-closing fix; a validator is one total rule with a mutation test. (L27; amends lessons.html#review-28-rounds)
- R9.26 Budget platform CI: the suite uses most of the 25-minute cap; never fork a process pool inside an xdist worker; use a small-course fixture; test under CI's Python version before pushing. (L29)
- R9.27 A shared Course Builder install is one surface: land on main first, message the other lane with the sha, never install a branch build into the shared root. (L30)
- R9.28 Fan out content lanes (videos, articles, items, FRQs) as parallel shards; scripts and per-item files before agents; every workflow agent carries a fixed-task line. (L32)
- R9.29 Every decision row carries a deadline and a default; every work order names a closing owner; a superseded destination closes with a pointer the day the route changes. (L33; amends lessons.html#coverage-first-builder-20260910)
- R9.30 When the close bar sits in another team's write corridor, file the fallback route in the same issue; ask for the capability, not the token; check a fork is current before declaring code unreachable. (L34)
- R9.31 Measure the queue place on the shared pool before every paid step and write the wait into the estimate; each course gets its own controller lease and lock. (L35; amends lessons.html#morning-retro-20260910, report card)
- R9.32 Repair the measurement layer on intake day: a committed report is a claim, a regenerated report must be shown to have changed, and MISSING never becomes PASS. (L36; amends lessons.html, unanchored section "Lessons — the 24 hours after the Psych sync", item 6)
- R9.33 A zero returned by a filter is not evidence until a positive control shows the filter can hit. (L37; amends lessons.html, unanchored section "Lessons — the 24 hours after the Psych sync", item 6)
- R9.34 Check the recorded diagnosis and the spec premise against bytes before building the fix. (L38; amends lessons.html#morning-retro-20260910, retry card)
- R9.35 Read the factory's answer from bytes first; walk the false-absence ladder before declaring a tool missing. (L39; amends lessons.html, unanchored section "Factory-canonical operating rules")
- R9.36 Never present a mechanism choice to the owner when a live course holds the precedent; a named blocker needs an exhaustion receipt. (L40; amends lessons.html, unanchored section "Factory-canonical operating rules")
- R9.37 Persist full request and response bodies at capture; bind the consumer contract before spend; never re-judge a deterministic fail. (L41; amends lessons.html#morning-retro-20260910, retry card)
- R9.38 Every status view pairs the current hold with a 'landed so far' line fed from receipts; the event log points at a receiver that exists, and a dispatch nobody receives is an error. (L42)
- R9.39 Size paid checks from recorded per-batch durations; outward estimates use the cautious end. (L43; amends lessons.html#morning-retro-20260910, report card)
- R9.40 A high-severity automated security finding at merge time gets a written disposition on the pull request before the merge. (L44)
- R9.41 Link every out-of-GitHub review round from the pull request so wait and rework are countable. (L45)
- R9.42 File instrument-contract mismatches on day one with a reproduction; keep acceptance evidence in a repository that will not be recreated. (L46; amends lessons.html#publish-faster-20260920)
- R9.43 A frozen blueprint is still a document with errors: reconcile it against the authoritative rubric in week one and register a measurable oracle predicate for every requirement at the start. (L47)
- R9.44 Describe QA work in QA terms; write worker prompts through the codex-prompt skill with the shortest read path; owner asks are two plain sentences. (L49)
- R9.45 Defer nothing: no deferred findings in a pull request; a plan date is an intent, not a state. (L50)
- R9.46 Never freeze an expectation of factory behavior; suspect our own environment before calling another repository's tests broken. (L51; amends lessons.html, unanchored section "Lessons — the 24 hours after the Psych sync", item 2)
- R9.47 Commit the status file, the publication runbook and a per-phase module inventory to the course repository at intake. (L52; amends retro.html#humgeo-closeout-20260920)
- R9.48 The lever on elapsed time is the wait between landings, not the review round count. (L53; amends lessons.html#review-28-rounds)
- R9.49 Before a render wave, read the video service's queue for the shared principal and clear stale rows; budget against the service's measured state. (L54; amends lessons.html#publish-faster-20260920)
- R9.50 Mock forms carry the real exam's option count and everything else carries four; the count is read from the course profile, never converted after generation. (L55)
- R9.51 Articles from a source that needs a license are excluded; the course writes its own; a provenance scan runs before any outside body enters a keep or import column. (L56)
- R9.52 A contributor's activity on a course repository is a coordination fact, never ownership or permission; ownership is read from the profile and the remote at intake. (L57)
- R9.53 Cap attempts at the factory's own bounds, then rebuild: one tagging pass per item ended a retry loop; an exhaustion receipt ended a re-post loop that spent about 75 candidates for 0 accepted. (period 2 lesson, not in the 57-row table)
- R9.54 Rule at the plan stage on any step whose evidence the factory does not hold; never hold on it. The grader-evidence hold ran 66.4 hours for receipts the factory does not produce. (period 3 lesson, not in the 57-row table)
- R9.55 Name the student destination and the full object inventory in the course profile before the first hand-off; when the close bar sits in another team's write corridor, file the fallback route in the same issue. (cause C1, the one change for the next build)
- R9.56 Run the acceptance instrument from a pushed ref on a 200-question slice in the first week; read checks.py and timeback_reader.py before any structural write; carry the reader's known needs from the first publish. (cause C2, the one change for the next build)
- R9.57 Give each course its own controller lease, lock locator and install root; measure the queue place before every paid step and write the wait into the ETA. (cause C3, the one change for the next build)
- R9.58 Standing authority until the course is live, recorded once in a grant file every window reads; gates still run; no clock on the owner's words; an open decision blocks the publish step or carries a typed default. (cause C4, the one change for the next build)
- R9.59 State progress only in the publication runbook's phase names; every local gate runs in shadow except the certification gate; a base-red suite gets an adjudication row, not a refusal. (cause C5, the one change for the next build)
- R9.60 Make the re-pin a step of the item-campaign operator (plan, seal, execute, replay, re-pin) and keep the publisher's checkpoint in the repository so a re-pin republishes only what changed. (cause C6, the one change for the next build)
- R9.61 Re-derive every quoted number from the live remote in the same turn; assert that a regenerated report changed; pair every hold with a 'landed so far' line; point the event log at a receiver that exists. (cause C7, the one change for the next build)
- R9.62 Every review finding returns with a deterministic, tested fix; a capped lane writes its report file first; PRs post ready-for-review; a small-course fixture keeps the suite under the CI cap; out-of-GitHub rounds are linked from the PR. (cause C8, the one change for the next build)
- R9.63 Commit the publication runbook and a per-phase module inventory (exists or missing) to the course repository on intake day; plan from that inventory, never from an assumed pipeline. (cause C9, the one change for the next build)
- R9.64 Run every unattended chain detached with progress visible from its checkpoint; refusal identity includes release and operator bytes with a retry budget; one install root per lane; free-space preflight before any sealed execute. (cause C10, the one change for the next build)
- R9.65 Pilot one lesson, verify on the rendered course and one QC read, then scale; keep the operator's undo ready; a step that needs evidence the factory does not hold is ruled at the plan stage, not held. (cause C11, the one change for the next build)
- R9.66 Write the content bar (exam shape of the mock, stimulus share, lesson row order, article format) into the course profile before generation, and show the owner one rendered lesson before the bank is generated. (cause C12, the one change for the next build)
- R9.67 Every decision row carries a deadline and a default; every work order names a closing owner; superseded destinations close with a pointer the day the route changes. (cause C13, the one change for the next build)

### R10. Rules learned on HumGeo not yet in R8 or R9 (2026-09-17 to 09-20)

- R10.1 Cite private evidence by identity and hash; secure rubrics, answer keys, credentials and signed report URLs never enter the course record. (H2)
- R10.2 Report unique-item counts and occurrence counts separately; raw finding counts overlap within items and are never summed as repair counts. (H3)
- R10.3 An instrument defect is ruled per finding class with item and check fingerprints, source evidence and a reviewer; it is never a blanket exemption. (H5)
- R10.4 Every failed item gets one of four decisions (repair, drop candidate, retain-with-ruling, defer); a ruling clears zero QC points, a defer keeps the defect, and any changed input reopens the ruling. (H8)
- R10.5 Read the floor per pool from the course's own blueprint and manifests, never from another course; land a floor verifier that censuses every lesson and gate form, counts a moved-and-dropped item once and goes red on a forced known-bad before the first drop. (H11)
- R10.6 A render check row whose page never mounted its root is not content evidence; uncaptured FRQs stay unmeasured; a render run never stands in for grading, result isolation or XP checks. (H16)
- R10.7 Bind test identity, the permitted capture and submission behavior and the secure-content boundary before launching a render capture, because the capture workflow can submit answers. (H17)
- R10.8 Compare QC numbers only under the same check scope; another course's percentage with checks disabled is not this course's acceptance, and missing reviews, unresolved findings and local rulings are reported as separate facts. (H18)
- R10.9 Filter a rewrite worklist by question type and pre-screen the live shape before any drafting spend; an MCQ redraft can never replace an extended-text item. (H22)
- R10.10 Review every not-taught finding against the topic's teaching text with one quoted evidence sentence before redrafting; a taught item is a false reject and stays as served. (H25)
- R10.11 A render run where no row mounted its root is an instrument null; freeze it and run render checks after the replacements land, never before. (H26)
- R10.12 Record a deferred defect class once with its census, its route and the expectation that it keeps failing every run; change embedded checks by editing the authored source, rebuilding assets and republishing to the new key. (H28)
- R10.13 Pilot each drafting model on a handful of items and pick by its measured structural pass rate before spending on the full run. (H33)
- R10.14 Treat the factory item judge as the gate and the hosted run as the acceptance; a judge pass can still fail the hosted reader, and the run's cache-miss count shows which items it judged fresh. (H37)
- R10.15 Report the Faultless Bar's sign-off gates apart from its automated checks; a red sign-off gate is a pending signature, not a content failure. (H38)
- R10.16 Wire one visible mastery-gate form per topic; the blueprint's extra forms are alternates for rotation, not extra gates. (H41)
- R10.17 Every renumbering pass checks for sort-order collisions with the passes before it; sub-lessons run instruction, practice, gate with no duplicate positions. (H42)
- R10.18 Rule ordering findings by class (assessment-only lessons, title heuristics, real prerequisite drift), state the residue the ruling predicts, and confirm it on the next run. (H45)
- R10.19 Shard redraft loop inputs so no command line carries the whole worklist; a hung loop is stopped and its items recorded as fails, not waited on. (H52)
- R10.20 Where the render instrument cannot reach a resource kind, accept it as presentation-unverified by the instrument and record the owner's walk as an enrolled student once as the evidence. (H53)
- R10.21 A hosted FAIL opens a queue row, not a verdict: keep the raw verdict, record the review decision and the live action in separate columns, and keep independent rows moving while one is blocked. (H4; amends lessons.html#publish-faster-20260920)
- R10.22 A provider error or an oversized context is a missing verdict, not a fail: retry inside a bounded, supported envelope; never rerun the whole pool blind, swap the model automatically or truncate the teaching text. (H6; amends retro.html#humgeo-native-publication-20260914)
- R10.23 Prove a defect class with one canary and one unchanged control per rendering path, then sweep every member; a ruled false alarm leaves the raw score unchanged. (H7; amends lessons.html#design-assumption-article-coverage-20260912)
- R10.24 Triage every fail on two axes before ruling: its pool (which fixes the floor and whether a drop is even possible) and its class (which fixes the route); run the floor checker with the drops list before any drop lands. (H9; amends lessons.html#publish-faster-20260920)
- R10.25 A drop suppresses the item from publication and keeps its bank record, id and ordinal; every serving reference is rebuilt on both sides of a move and read back; deletion is a separate admitted operation, and unlinking never authorizes it. (H12; amends lessons.html#review-28-rounds)
- R10.26 Record the hosted job id the moment it exists and never invent one; freeze its configuration, input fingerprints, reports and email state in the run folder; define the changed set as payload, stimulus, placement pointer and judging context together. (H13; amends lessons.html#apwh-qc-cache-is-instrument-20260921, lessons.html#publish-faster-20260920)
- R10.27 Account for every run in four parts: denominator changes, repaired-item gains, provider errors and movement on untouched controls; explain any denominator change before comparing two runs. (H14; amends lessons.html#publish-faster-20260920)
- R10.28 Quote every hosted number with its cache state; the cold run is a receipt for where the course stands, not a gate, and the cold population is measured and disclosed before any paid run. (H15; amends lessons.html#apwh-qc-cache-is-instrument-20260921)
- R10.29 A missing shared capability holds only the action that depends on it; every other row keeps moving, and the course record never authorizes a platform change, a release or a timer. (H19; amends lessons.html#apwh-fallback-in-same-issue-20260921)
- R10.30 Verify every factory repair before it lands: clear of the original class, no new structural fail, stem unchanged; a repair that still echoes a stem word or adds an absolute term is rejected and joins the rewrite worklist. (H20; amends lessons.html#apwh-fails-feed-next-round-20260921)
- R10.31 Census where each item's text lives before picking a replacement route (standalone item, video check in a static document, article check, writing slot); one operator reaches one shape. (H21; amends lessons.html#apwh-census-ids-before-embed-20260921)
- R10.32 Compose every redraft with the campaign item rules, the lesson's own teaching text and the QC findings; a rewrite that changes the stem routes through the judge and a full-item replacement, not the choice-text operator. (H23; amends lessons.html#apwh-fails-feed-next-round-20260921)
- R10.33 When a render or QC walker fails a whole kind of resource, read how it resolves ids and check the syllabus before calling it an outage; a walker that parses only URL test ids misses ids carried in the sourcedId. (H27; amends lessons.html#apwh-read-reader-first-20260921)
- R10.34 Certify a repair by byte-level readback of the served XML; a row the render instrument never reached is recorded as presentation-unverified with a named decision for a person. (H29; amends lessons.html#native-terminal-receipts-20260914)
- R10.35 Never rewrite judge records while a judge run is open; back up the judged records first and restore unchanged ones byte for byte, because the judge drops a verdict whose record changed between send and write. (H30; amends lessons.html#review-28-rounds)
- R10.36 Quote the target EK's own CED description into every redraft prompt as a hard constraint; the EK code and the judge's reasons alone left six items failing for five rounds. (H32; amends lessons.html#apwh-fails-feed-next-round-20260921)
- R10.37 When one check fires on nearly every item, report the content result with that check set aside, read the reader's code for the cause, prove the class on a fleet course with the same shape, then file it with the blast radius. (H36; amends lessons.html#apwh-read-reader-first-20260921, lessons.html#apwh-file-mismatch-day-one-20260921)
- R10.38 Census every quiz resource against a working sibling course's shape (vendor, host, id prefix, url, title) before students see it; a row with no url or a bare id will not open. (H39; amends lessons.html#apwh-live-facts-become-rules-20260921)
- R10.39 Diagnose a student-facing complaint from the live course tree, expect more than one cause, and keep owner-approved removals recorded where the next diagnosis will read them. (H40; amends lessons.html#apwh-lesson-shape-two-readers-20260921)
- R10.40 Expect the platform to merge resource metadata on PUT: a candidate that drops a key never reads back, the player labels a row from activityType, and an escaped ampersand in an iframe src breaks the page. (H48; amends retro.html#humgeo-closeout-20260920)
- R10.41 When a rendering difference is explained by a field whose renderer rule was never read in bytes, record it as a correlation and leave the owner's choice open; never write it as the cause. (H49; amends retro.html#humgeo-closeout-20260920)
- R10.42 Read an operator's refusal as a readback of live state: a re-plan that refuses because the candidate is already live, or an enrollment that refuses because the learner already has the course, confirms the state without a write. (H54; amends lessons.html#publish-faster-20260920)
- R10.43 Write technique checks as exam-form questions with the technique taught in the explanation, because the judge reads a which-response-earns-the-point stem as a meta-question; page checks inside an article do not move the hosted score. (H56; amends retro.html#humgeo-closeout-20260920)
- R10.44 For a wording class on items that already pass, change only the flagged option and measure that stem, key and other options are byte-identical; a redraft that fails the judge leaves the served item as it stands. (H58; amends lessons.html#apwh-own-defect-classes-20260921)
- R10.45 Treat a rewrite of passing items as a regression risk: it clears no old fails, so read each new fail as a real regression or reader variance before the next redraft. (H59; amends lessons.html#publish-faster-20260920)

### R12. Rules learned on the APWH repairs (2026-09-21 to 09-26)

- R12.1 A data-file PR merges only after its pytest job finishes green on that exact head; the pre-push gate does not replace it; push once per head. (NEW-COURSE rule 31; ap-one #1248, #1250, #1251)
- R12.2 Freeze the done list at the start, and give it a content-accuracy row or state that accuracy is outside done. (rule 32)
- R12.3 Check each claim in articles, tables, items, scorer examples and captions against a named outside authority before done; scan served text for authoring notes first. (rule 33)
- R12.4 Only a hosted QC run closes a hosted QC fail; a `/v1/qc` pass does not predict it; quote each hosted score with its cache hits. (rule 34)
- R12.5 A walk finding closes only on the walker's own recheck (`CLOSURE.json`); a finding shared by every course is player behavior, recorded and filed, not repaired. (rule 35)
- R12.6 Every reference in a task (passage, document, model, response, prompt) resolves inside the same item or page. (rule 36)
- R12.7 Scoring text quotes the current official rubric; an exercise's own constraint is labeled as such; each student criterion still names the task and the reasoning after the scorer split. (rule 37)
- R12.8 Readability rewrites are for practice; an item on any exam form keeps exam difficulty. (rule 38)
- R12.9 A class fix starts from a census of the whole live population: active rows only, stock text counted as missing, every item ref resolved, video narration scanned. (rule 39)
- R12.10 The student's player is the only preview: check item layout with the render harness before a wave; same-key video swaps carry `Cache-Control: no-cache`. (rule 40)

### R13. Rules learned on the HumGeo student-review record, second pass (2026-09-26)

- R13.1 A new services/ingest module needs the import-safety test run by name, and a LIBRARY_MODULES entry if it has no CLI; ap-one #1258's first head went red on this, fixed before the merge. (rule 41)
- R13.2 Push once, with the final rebased head, only when given the merge slot; merge-gate checks the PUSHED head, not a local-only rebase. (rule 42)
- R13.3 Name pytest's test files literally in the command; the guard is a PreToolUse hook that reads the command string before the shell expands a variable. (rule 43)
- R13.4 Lane clones get the pre-push gate from the global `core.hooksPath`; don't let `scripts/ship.py`'s local override beat it. (rule 44)
- R13.5 A same-key rewrite of a page's stimulus must rebuild the hidden article-text block, not only the visible one, or hosted Course QC cannot see the new content. (rule 45)
- R13.6 Check a writing bank carries `lo_codes`, `skill_codes` and a `model_answer` before sending it to `/v1/qc`; where it never has (HumGeo), use that course's own writing judge on a before-and-after pair, with the deployed grader confirming identical scores. (rule 46)
- R13.7 Read a page through its current href, not a saved crawl — a moved object key can make a stale-URL search report real content as missing. (rule 47)
- R13.8 A definition padded to clear a reading-grade floor still has to read like a sentence; read every generated definition as a student would before it ships. (rule 48)
- R13.9 A table's title must not share a header cell with its column label. (rule 49)
- R13.10 A question naming a map, chart or scatterplot needs a real rendered image, not a text description. (rule 50)

## 2b. Where the build stands and what remains

Measured on 2026-09-15 by running the build unattended on the owner's install after release .20 (goal-fit reviews by Codex and Grok on the make, the write layer and the graph layer were folded before each was built).

| Layer | Today (2026-09-15.20) | Remaining |
|---|---|---|
| Install to Step 0 | one menu number, three hidden strings, an optional judge key; setup and discover close on bytes for APWH and HumGeo in under a minute | none |
| Step 1, APWH | passes on the course's own contract: no FAIL row is new against the committed conformance report; the three recorded rows (A-097 teaching order, A-116 terminal carriers, A-202 graph joins) print with their closers and measured counts | none in the gate; the rows close through the two layers below |
| Course map, APWH | 9 units, 176 lessons, 6,576 XP from the pricing manifest; every unit has a milestone | none |
| Step 0, HumGeo | its blueprint is located by pattern; pricing needs the sealed publication plan (private corridor package) before ap-one humgeo_native_timeback_xp.py can price it; no tree tool exists; titles and coverage cannot be derived from its blueprint shape | the corridor inputs the course keeps privately |
| Lessons | every factory-accepted article and check set materialized (APWH: 126 articles, 933 checks); 50 article work orders open for the rows the factory's own QC rejected | an author seat |
| Write layer (A-116, A-097) | 37 assess-tier tasks declared by script with zero calls; 114 work orders written (112 terminal tasks, one row-6 drill, one row-7 drill); staging, list-key placement, byte-identity, model-answer stripping and the oracle's five-site list-key repair proven on staged copies (no crash on list keys, grouping stage at rank 5) | an author seat; then judge calls (ceiling 342) and the two pull requests the build opens and merges |
| Graph layer (A-202) | merged graph pinned at the graph repository's live main (953 concepts, 531 atoms; pre-delta copy matches the census by sha); 28 concept typings and 15 atom rows planned; on a temp copy with placeholder judgments the overlay became total, all seven typing rows and the edge-map row passed, the oracle counted 145 joins with 3 new | an author seat for 28 typings and the bridges the join count names; then one pull request |
| Author seat | hermes on gpt-5.6-sol (the sanctioned route) is the default when installed, 50 orders in flight; a local server with no model is refused; no seat is ever a menu choice | none: the seat is set once in the answer file |
| Bank gates | per bank, the course option count, exactly one key, the factory's own key-balance module, zero uniquely-longest keys, mock forms matched to the exam shape; PASS on APWH's banks | QTI is the factory's committed receipts, not a re-emit |
| Publish dark, cold QC, walk, open | rules follow the operator twins' argument lists; the publish package, corridor and assets are explicit produce targets; the QC bar (pass ≥ 0.95, severe = 0 measured, cold, all checkers) sits on the QC receipt and nothing below it walks or opens | never executed on a real course; APWH's publication operators are a factory pull request the profile still marks not implemented |

Review provenance: Codex reproduced ten defects on the make offline and all ten are fixed; on the write layer Codex and Grok converged on placement by list keys, no declaration without a record check and a receipt, row 8 never earlier, the judge fed through the factory's shape, a restart-safe retry cap and two-repository recovery; on the graph layer both refused any replayed typing and asked for a whole recount, path flags and work orders before the merge. Every finding is in the code; the plans and reviews sit beside this spec in the course-builder packet.

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
  "spec_version": "2026-09-26.49",
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
  "qc_ceiling_rule": "ceiling = (items - instrument-defect fails) / items; a run within one item of it is terminal",
  "landing_rules": ["review receipt bound to the exact head", "receipts committed as digest-and-count files", "base-red suite adjudicated not refused", "waiters count new exact sentinel lines"],
  "forbidden_in_package": ["person names", "usernames", "machine paths", "external-drive paths", "credential values", "firewall steps"]
}
```
