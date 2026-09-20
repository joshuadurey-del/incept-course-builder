#!/usr/bin/env python3
"""One-shot: record the HumGeo 2026-09-17 to 09-20 close-out in retro.html, lessons.html and SPEC.md.
Every number below is copied from receipts named in the text (events.jsonl rows, hosted result summaries, landing lane files)."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parent.parent

RETRO = """  <section id="humgeo-closeout-20260920"><h2>HumGeo, September 17–20: hosted QC to the instrument ceiling, presenter videos, two landings</h2>
    <p>Evidence window ends September 20, 2026, 06:10 UTC. Course: the HumGeo v3 native TimeBack course. Every live change ran one sealed course operator committed in the platform repository, from a local sealed commit, with capture, execute/readback and zero-write replay receipts; the platform PR followed the writes. <a href="lessons.html#publish-faster-20260920">Lessons into practice</a>.</p>
    <h3>What landed</h3>
    <ul class="work-list">
      <li><b>Hosted Course QC burndown, ten measured runs.</b> Pass rate 0.8956 after the structural repairs (run 2) to 0.9802 (runs 9 and 10); severe pass rate 0.9805 on run 10, which is the ceiling while the hosted service applies MCQ checks to 58 extended-text items (filed as ap-complete-qc-system #25). Item replacement batches 3 to 11 replaced 462 items in nine sealed operations (200, 107, 17, 10, 1, 23, 94, 9, 1), each read back and replayed with zero writes. 2,919 of 2,978 unique items pass every check.</li>
      <li><b>Loop that produced it.</b> Measure with the hosted service and freeze the result; split fails by route before drafting (choice items with topic codes to redraft, extended-text items to the instrument filing, items with no topic code to authored codes); redraft through the structural gate and the factory judge; replace through the sealed operator; re-measure. Campaign 11 redrafted the last choice fail in seat with no drafting spend and passed the judge at 0.979.</li>
      <li><b>Article XP repair:</b> 72 of 189 live articles moved to the fleet formula (words/200 plus 0.5 per question), 72 writes, replay 0. <b>FRQ Technique lessons:</b> ten pages rebuilt to the Section II shape with 50 replaced checks, 80 writes, replay 0. <b>Video shape repair:</b> 187 resources reshaped to the fleet video shape and 376 links retitled so rows read Video and Reading.</li>
      <li><b>Presenter videos:</b> 187 lesson videos re-rendered on the fleet video service with the presenter prompt; 170 published to the same S3 keys with sha-verified refetch by 06:00 UTC on September 20, so the live player pages swapped without a TimeBack write.</li>
      <li><b>Two landings, both merged September 20.</b> Platform PR #1184 (four operators, the interleaved page renderer, batch pins, six test files; suite 13,344 passed; codex review chain 8-3-5-2-1-1-1-2-0-1-0 to APPROVE; deploy run completed and the served version reads the merge commit). Course docs PR #103 (findings through run 10, eight frozen hosted results, campaign recipes, operator receipts as digest and counts; codex text review 7 then 1 findings to APPROVE).</li>
    </ul>
    <h3>What failed, why, and the correction that worked</h3>
    <ul class="work-list">
      <li><b>Two orchestrators on one worktree.</b> A resume note said the previous window was cleared; it was alive and its landing agent committed 29 seconds after the new window did. Correction: before the first write on any resume, list live sessions and read <code>git log -1</code> on every tree the handoff names; split by tree by message. No bytes were lost.</li>
      <li><b>Video service out of disk, twice.</b> The fleet video service refused every edit with HTTP 500 (its own run disk) from 14:27 to 21:55 UTC and again from 17:17 UTC; 487 refusals. Edits accepted afterwards sat queued for hours because a 202 means queued, not scheduled. Correction: the fixer retries without burning attempts, polls <code>finished_at</code> against the submission time before trusting <code>succeeded</code>, and the publish loop is kept alive independently of the render engine.</li>
      <li><b>Receipt named the wrong head.</b> A pin-only commit after the APPROVE moved the branch head; the landing tool refused because the review receipt named the earlier head. Correction: one more closing slot on the exact head (it found a real fold finding: a component's live parent was never compared with the selected topic; fixed with 18 regression cases).</li>
      <li><b>Wait loops matched the wrong thing.</b> A batch waiter grepped for a completion phrase already present in the other course's log and would have taken the writer lock mid-chain; a follow-up waiter aborted because the word "stopped" appeared in a skip message. Correction: count new occurrences of an exact sentinel line, and use exact exit lines instead of substrings.</li>
      <li><b>Docs repo suite red on main.</b> The landing tool's prep refused on 23 tests that are red on origin/main itself (identical failure set, no test or script touched). Correction: compare the failure sets on base and head; when they match, land through the merge gate directly, as the previous docs PR did.</li>
      <li><b>Uncommitted receipts are not evidence.</b> The text reviewer refused execution counts whose receipts lived only in the private root. Correction: copy each operation's digest-and-count receipts into the course repository beside the findings.</li>
    </ul>
    <h3>What remains open</h3>
    <ul class="work-list">
      <li>17 lesson videos still serve their previous render until the video service runs the queued edits; the fixer and publish loop finish them without a human step.</li>
      <li>The owner's hand steps: LS notice, enrollment, walk as a student, activation, release flip.</li>
    </ul>
    <h3>How the next course reuses this</h3>
    <p>The burndown loop, the split rule and the ceiling computation are recorded in the course repository's QC progression ledger and method note; the builder's cold QC step should stop at the computed ceiling, not at 1.0. Receipts are committed as digest-and-count files, review receipts are bound to the exact head, and every waiter counts new sentinel lines.</p>
  </section>
"""

LESSONS = """  <section id="publish-faster-20260920"><h2>September 19–20: publish a course from the platform to TimeBack faster and more deterministically</h2>
    <p>Source: the HumGeo close-out (<a href="retro.html#humgeo-closeout-20260920">retrospective</a>). Each lesson names the practice and the builder change it asks for.</p>
    <ul class="work-list">
      <li><b>Compute the QC ceiling before chasing the score.</b> Split every failed item by route first: choice items with a topic code are redraftable; extended-text items judged with MCQ checks are an instrument defect (file it); items with no topic code need authored codes, not redrafts. The reachable ceiling is (items minus instrument fails) divided by items. HumGeo: 0.9805, reached on run 10. <i>Builder change:</i> the cold QC step records the ceiling and stops there; a run within noise of the ceiling is terminal.</li>
      <li><b>One run carries noise; a second run confirms.</b> Run 7 flipped 99 untouched items; run 8 flipped none. Never redraft on a single run's new fails without a second measurement.</li>
      <li><b>Seat drafts for single items cost nothing.</b> The last choice fail was redrafted in seat (write the draft into the campaign's <code>response.raw.txt</code> with the model recorded), gated, judged once, replaced. <i>Builder change:</i> the redraft step accepts a seat draft for small remainders instead of a paid call.</li>
      <li><b>Execute from the local sealed commit; land the PR after.</b> Batches 10 and 11 ran and replayed before their PR existed. The platform only needs the pin in the local head. <i>Builder change:</i> already the rule; keep it.</li>
      <li><b>Bind the review receipt to the exact head.</b> A pin-only commit after an APPROVE moves the head; the landing tool refuses on purpose. Budget one more closing slot per pin commit, or land the pin before the review. The extra slot on HumGeo found a real finding.</li>
      <li><b>Commit the receipts you cite.</b> Digest-and-count receipts (plan, capture, execute, replay) belong in the course repository beside the findings; a reviewer cannot read the operator's private root.</li>
      <li><b>Waiters count new sentinel lines.</b> A grep for a phrase that already exists in another lane's log passes at once; a substring like "stop" inside "stopped" aborts a follow-up. Count occurrences of an exact line and wait for the count to rise.</li>
      <li><b>Generate pins from the file, not from a copied anchor.</b> A batch script cloned by text replacement failed on the dirnames tuple its own predecessor had changed. Read the current tuple with a pattern and append to it.</li>
      <li><b>A 202 from the video service means queued, not scheduled.</b> After an outage the accepted edits sat for hours. Poll <code>finished_at</code> against the submission time, keep the publish loop alive independently of the engine, and budget hours for the service to drain. The full-disk error is the service owner's incident; nothing client-side drains it.</li>
      <li><b>Base-red suites need an adjudication, not a refusal.</b> When the identical failure set is red on origin/main, a docs landing proceeds through the merge gate with that fact in the cert. <i>Builder change:</i> prep compares failure sets on base and head and records "pre-existing on base" instead of refusing.</li>
      <li><b>Check for a live peer before the first write on any resume.</b> List sessions and read the last commit on every handoff tree; a note that says the other window is gone is intent, not state.</li>
      <li><b>Per-learner lesson plans snapshot the graph.</b> After any wave that adds or removes components, recreate each enrolled learner's plan; link and resource edits show live without it. (Measured on APWH the same week.)</li>
    </ul>
  </section>
"""

SPEC_ADD = """
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
"""

def patch(path: Path, anchor: str, block: str, before=True):
    s = path.read_text()
    assert s.count(anchor) == 1, (path, anchor[:60], s.count(anchor))
    s = s.replace(anchor, block + anchor if before else anchor + block)
    path.write_text(s)

if "humgeo-closeout-20260920" not in (ROOT / "retro.html").read_text():
    patch(ROOT / "retro.html", '  <section id="humgeo-end-sprint-20260916">', RETRO)
if "publish-faster-20260920" not in (ROOT / "lessons.html").read_text():
    patch(ROOT / "lessons.html", '    <section id="humgeo-postassembly-20260916">', LESSONS.replace("\n  <section id=", "\n    <section id=").replace("\n  </section>\n", "\n    </section>\n"))
spec = ROOT / "SPEC.md"
s = spec.read_text()
if "### R8." not in s:
    s = s.replace("\n## 2b. Where the build stands and what remains", SPEC_ADD + "\n## 2b. Where the build stands and what remains", 1)
    s = s.replace('"spec_version": "2026-09-14.14"', '"spec_version": "2026-09-20.45"')
    s = s.replace('"triage_classes": ["content", "context", "checker", "provider", "selection"],',
                  '"triage_classes": ["content", "context", "checker", "provider", "selection"],\n  "qc_ceiling_rule": "ceiling = (items - instrument-defect fails) / items; a run within one item of it is terminal",\n  "landing_rules": ["review receipt bound to the exact head", "receipts committed as digest-and-count files", "base-red suite adjudicated not refused", "waiters count new exact sentinel lines"],')
    spec.write_text(s)
print("patched retro.html, lessons.html, SPEC.md")
