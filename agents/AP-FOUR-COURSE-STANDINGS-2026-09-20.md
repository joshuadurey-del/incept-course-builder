# AP Four-Course Standings — 2026-09-20

Refresh cut at 2026-09-20 08:12 UTC. Every number below was read the same morning from GitHub, from the private
local event log (`INCEPT/events.jsonl`, row ids cited), or from a peer window's report. Owner dispositions are the
owner's words typed on 2026-09-20. Nothing here is a Learning Science (LS) verdict; "ready for LS review" is the
owner's readiness call, not acceptance.

## TLDR

- **HumGeo**: at the hosted QC ceiling and **ready for LS review** (owner). Hosted Course QC run 10 reads 0.9802 pass,
  0.9805 severe pass over 2,978 unique items; the 58 remaining severe fails are extended-text items judged with MCQ
  checks, filed as an instrument defect (ap-complete-qc-system #25). Findings merged in
  [humgeo-rebuild #103](https://github.com/ilmych/humgeo-rebuild/pull/103); operators merged in
  [ap-one #1184](https://github.com/InceptTrilogy/ap-one/pull/1184). Left: the owner's hand steps and 17 queued video renders.
- **APWH**: the native TimeBack course is live dark and the **lesson-shape upgrade is running now** in three windows under
  a 24-hour owner authorization; target is a course the owner can walk on 2026-09-21. Not yet ready for LS review.
- **APUSH**: **build planned, starts when APWH is done** (owner). Sources unmoved: 49 of 249 article positions accepted.
  The 2026-09-20 plan fans out every content lane in parallel and ends in one typed Course Builder line on the lean route.
- **Psych**: owner review done; **waiting on Jayesh's response** to findings F-017 and F-018 (FRQ grader lane and
  certification). **Technically ready for LS review as is** (owner).

## HumGeo — Prove (p7)

| What | Receipt |
| --- | --- |
| Hosted Course QC run 10: pass 0.9802, severe 0.9805, 2,919 of 2,978 pass every check, 58 severe + 1 mild fail | [run10/summary.json @ c8750360](https://github.com/ilmych/humgeo-rebuild/blob/c8750360f509670abb0ce792c47e15e91466d79c/out/publish/course_qc/run10/summary.json) |
| Ceiling: (2,978 − 58) / 2,978 = 0.9805 while extended-text items get MCQ verdicts | event row for run 10 (2026-09-19 17:52Z); filing ap-complete-qc-system #25 |
| Item replacement batches 3–11: 462 items replaced through the sealed operator, each read back and replayed with zero writes | event row 94f68bbefde7f037 (batch 11) and the batch rows before it |
| Article XP repair (72 writes), FRQ Technique rebuild (80 writes), video shape repair (187 resources, 376 links) | ap-one #1184 body; event rows 2026-09-18/19 |
| Presenter videos: 187 re-rendered, 170 published by 06:00Z 2026-09-20, 17 pending the video service queue | retro.html section "humgeo-closeout-20260920" |
| Landings 2026-09-20: humgeo-rebuild #103 merged 05:08Z (c8750360); ap-one #1184 merged 05:50Z (0811d834), suite 13,344 passed | GitHub PR pages |
| Owner disposition | "humgeo ready" (for LS review), 2026-09-20 |

Not measured in this refresh: live enrollment state, learner-surface readback, LS verdict.

## APWH — Assemble (p5), upgrade in progress

| What | Receipt |
| --- | --- |
| Native course ap-world-history-native-202608-v1, publishStatus testing; checkpoint re-bound to the folded first-cut producer, 8,659 rows verified live-equal, 0 writes (2026-09-19 18:20Z) | event row cf9062c5ec42a7ef |
| 50 producer-rejected lessons now carry the AP One article body (50 writes, replay 0) | Window A report; PLAN.md |
| Video is row 1 of every lesson: 342 rows re-ordered, read back, replay zero-write (2026-09-20 07:54Z) | event row 43265ae7541d72f3 |
| Hosted QC on record: job_55359534677242b1b5f2bee58fe82480 (2026-09-18) 0.584 on 1,988 gate items only, stale. New cold baseline job_bae0235ae09a45efa2e58cbcb6d0cf15 submitted 07:56Z, running | Window C report |
| ap-one main 0811d834; branch apwh/gateundo-20260918 remote head 144d359f, local commits unpushed; [PR #1183](https://github.com/InceptTrilogy/ap-one/pull/1183) open | GitHub |
| Open owner decisions: boundary-check rule, boundary-check funding, Train Your Eye dialect (needs-human ledger); D1 and D2 run on defaults | needs-human.json; PLAN.md |
| Authorization: owner grant 2026-09-20 for spend, PRs and merges for 24 hours; every gate still runs | plan folder INCEPT/out/apwh-lesson-shape-20260920/ |

Not measured: the new cold QC result (running), the pilot article pages (in progress).

## APUSH — Synthesize (content), build planned

| What | Receipt |
| --- | --- |
| Article ledger: 249 records, 49 accepted (36 legacy dual review, 13 server strict), 200 pending; units 4, 6, 7, 8 at zero accepted | [ledger.json @ 98842f41](https://github.com/ilmych/apush-build-outputs/blob/98842f41d90138846ca8a584e2d60d8d54719e0f/phase2/article-acceptance-ledger-v2-succ11/ledger.json) |
| PIPELINE.md pre-publication at apush-course-build main 319e0777 (unmoved since 2026-09-10) | GitHub |
| Builder release 2026-09-15.64 installed; lean route dry run stops at publish/lean-package.json with seven content work orders | event row b43aa749a97ea869 |
| Build plan 2026-09-20: parallel lanes for 249 articles, MCQ seating, FRQs, 249 presenter videos; one typed builder line at the end | INCEPT/out/apush-lean-route-20260920/APUSH-BUILD-PLAN.md |
| Owner sequencing | "latest plan for apush which will start when apwh is done", 2026-09-20 |

Nothing serves for APUSH.

## Psych — Prove (p7), waiting on Jayesh

| What | Receipt |
| --- | --- |
| Handoff 2026-09-16: build, publish and QC done; repo main [834f8262](https://github.com/InceptTrilogy/ap-psychology-fall-2025-v1/commit/834f82629c1bf7112350884f98b91b928ad7c565), [PR #194](https://github.com/InceptTrilogy/ap-psychology-fall-2025-v1/pull/194); publish audit carries rows for units 1–5 | event row fe11b9bfa78d5d5b; publish_audit.jsonl |
| Acceptance bar (owner, 2026-09-17): independent review plus verified fixes; the cold Course-QC run is a receipt, not a gate | event row fe11b9bfa78d5d5b |
| Findings sheet: 11 rows plus F-017 and F-018 (2026-09-18): every published FRQ points ExternalApiScore at the banned cs-autograder; ap-grader lists ap-psychology as not AI-only ready | event row a0571efd1d15cd41 |
| Owner disposition | "waiting on Jayesh's response to my findings but it is technically ready for LS review", 2026-09-20 |

Not measured: fresh platform probe, enrollment breadth, LS verdict.

## Cross-course

- **Feed repair.** The local event dispatcher had posted to the public repository since the 2026-09-10 rename, while the
  receiving workflow and its secret live only in the private repository. Every local event and needs-human update since
  2026-09-09 10:02Z was dropped silently (GitHub returns 204 for a dispatch nobody receives). Re-pointed on 2026-09-20; the
  held rows replay through the same signed corridor.
- **Event log hygiene.** 37 hand-appended HumGeo rows carried kinds outside the contract or ids that no longer matched
  their bytes; repaired in place (kind mapped to the nearest contract kind, three over-long texts trimmed, ids re-derived)
  so the log passes its own verifier again. The old-to-new id map is kept beside the refresh receipts.
