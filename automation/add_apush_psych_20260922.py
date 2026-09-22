#!/usr/bin/env python3
"""One-shot: record the APUSH lean-route build (2026-09-19 to 09-21) and the Psych review (09-16 to 09-18) in retro.html,
and refresh the header version and the route section. Numbers are copied from the receipts named in the text
(APUSH MORNING-REPORT.md 2026-09-21 02:3xZ, lane receipts L7/L15, the 20:00Z state record; Psych PSYCH-STATUS 2026-09-18)."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
p = ROOT / 'retro.html'; t = p.read_text()

OLD_SUB = 'Source contract version 2026-09-14.8, checked 2026-09-14. Version .8 restores'
NEW_SUB = 'Installed Course Builder release 2026-09-15.66 (dashboard main 9636d23d), checked 2026-09-22. Two publication routes since .63 (see Current route). Version .8 restored'
assert OLD_SUB in t; t = t.replace(OLD_SUB, NEW_SUB)

OLD_ROUTE = '<section><h2>Current route</h2><p><code>content → p3 → p5 → p6 → p7 → p8</code></p><p>The route is a requirement sequence, not permission and not course credit. Each course page shows only its re-earned position.</p></section>'
NEW_ROUTE = '''<section id="current-route"><h2>Current routes</h2><p><code>content → p3 → p5 → p6 → p7 → p8</code>, by one of two routes chosen at onboard.</p><ul class="work-list"><li><b>Route apone</b> (HumGeo, APWH): the course has an ap-one manifest; the builder authors and judges lessons against the factory, runs the bank gates, and publishes through ap-one's sealed operators with capture, execute/readback and zero-write replay. As of release .66 this route has no release rows of its own.</li><li><b>Route lean</b> (Psych precedent, APUSH): the course repository holds the bytes; the builder runs the repository's own publish scripts, reads back, checks lesson shape, runs the hosted cold QC loop as a receipt, and owns the release rows (decision, activation PUT with readback, COURSE-LIVE). As of .66 its content and bank-gate steps are inventory receipts, not authoring rows.</li></ul><p>The route is a requirement sequence, not permission and not course credit. Each course page shows only its re-earned position. Closing the gap between the two routes is the next builder change (measured 2026-09-22).</p></section>'''
assert OLD_ROUTE in t; t = t.replace(OLD_ROUTE, NEW_ROUTE)

SECTIONS = '''  <section id="apush-lean-route-build-20260919-20260921"><h2>APUSH, September 19–21: the first course built on the lean route, dark on TimeBack in about 40 hours</h2>
    <p>Evidence window: owner authority granted 2026-09-20 09:02 UTC, state record 2026-09-21 20:00 UTC. Course: AP United States History (Fall 2026), TimeBack native, no ap-one manifest, so the builder's lean route (course repository holds the bytes) was the only route. Sources: the run's morning report and lane receipts (lanes L1 to L28) in the private run folder; Course Builder release notes .63 to .66.</p>
    <h3>What landed</h3>
    <ul class="work-list">
      <li><b>Whole course live dark.</b> Nine units and the course level pushed with exact readbacks (2026-09-21 02:3x UTC: 752 components, 656 links, 1,469 items, 0 drift). After the lesson-shape fold at 20:00 UTC the same day: 249 lessons, 544 named components, 697 links, 1,642 items, 457 old leaves soft-deleted, one owner enrollment with its lesson plan recreated.</li>
      <li><b>Content produced by the repository pipeline, not by hand in the builder.</b> Banks: 1,470 judge-PASS MCQs after three hosted-QC replacement rounds, every one of 87 lesson topics at 15 or more, key balance PASS on all nine units. Articles: 243 of 249 positions staged, 194 of 200 pending accepted through the factory judge at 5 of 5 checks; 249 articles carried openers, bold key ideas, a table and an SVG figure by the fold, 112 with an image. FRQs: 88 of 88 on the ap-grader ap-us-history lane; grader battery on unit 1 graded 93 of 93 with 0 false passes. Stimulus sets: 63 judge-PASS items in 22 sets; Section I seats exactly 55.</li>
      <li><b>Hosted cold Course QC, six measured runs.</b> 0.8534 (unit 1) → 0.8771 → 0.8592 (whole course, 1,634 questions) → 0.9293 → 0.9169 → 0.8683 on run 6 after the fold, with learning_science PASS and the ordering class cut from 407 to 195 by-design rows. Run 7 (the 224-item replacement wave) was pending at the window's end.</li>
      <li><b>Course Builder releases .63 to .66 came out of this run.</b> .63 added the lean route (route chosen at onboard, the repository's publish scripts in their own venv, receipt-mode cold QC, enrollment readback, one-field activation PUT). .65 folded the unit-1 live measurements (lesson-shape check on readback, release authority by route, replace-family split by route, measured publish expectations: create 4.1 s, skeleton 6.3 s, unit-1 artifacts 73.7 s for 157 records, tree 27.1 s for 128 mutations, readback about 94 s, hosted QC 122 s). .66 folded the APWH window's builder branches. Dashboard PR #1 merged 2026-09-20 21:11 UTC.</li>
      <li><b>Enrollment root cause found.</b> The admin's Enroll Student button failed three times because it created the course's default class under the course org, where the owner's account has no role; the working enrollments all sit under the school where the student role lives. Calling the same enroll route with that school succeeded at 02:32 UTC.</li>
    </ul>
    <h3>What failed, why, and the correction that worked</h3>
    <ul class="work-list">
      <li><b>The builder did not drive the run.</b> The ported publish scripts were run by hand for units 1 and 2 because the installed builder could not yet list a course with no ap-one manifest. Correction: every manual step became a builder fix (.63 to .65) and the builder drove from unit 3; the remaining gap (content and bank-gate rows are receipts on the lean route) is the next builder change.</li>
      <li><b>Wrong lesson shape for a TimeBack-native course.</b> Read and Check Your Knowledge published as sibling components (the HumGeo and APWH shape) raised 407 "practice without local instruction" findings on run 5. The owner ruled that a TimeBack-native course takes Psych and AP Lit as its reference, so lessons folded to one component holding video, article and quiz. Correction held: the class dropped to 195 by-design rows on run 6.</li>
      <li><b>Video service out of disk, then down.</b> The fleet video service refused writes from 10:10 UTC on 09-20 and answered HTTP 502 to every call from about 04:50 UTC on 09-21; the owner filed the storage fix with the platform team. Correction: narrations were redrafted to the presenter bar (243 of 249 in the 40-55 word band) so rendering resumes without a second authoring pass; lessons start at the Read row until the clips land.</li>
      <li><b>Shared install clobbered a branch build.</b> Installing .65 from main over another window's branch build of the shared builder. Correction, now a rule: install only from dashboard main, and message the other live course windows before any install.</li>
      <li><b>Two certification slips.</b> Units 2 and 8 were pushed while a certification record read HOLD or before a GREEN execution record. Disclosed with superseded records; the rule tightened from unit 6 on.</li>
      <li><b>A sweep followed a failed manifest build.</b> Correction: a sweep never follows a failed build; guards on another lane's manifest assert its shape first.</li>
    </ul>
    <h3>What remains open</h3>
    <ul class="work-list">
      <li>Videos: 248 presenter videos, one per key-concept lesson, blocked only by the video service; the loop resubmits when it can.</li>
      <li>Six article positions HOLD after five to seven judge rounds; eight image rows HOLD on the visual check; five served items keep their fail codes after repeated rounds (the same non-yielding residue class APWH measured).</li>
      <li>The owner walk and the release word. Activation is one PUT from testing to published with readback, on the owner's word.</li>
    </ul>
    <h3>How the next course reuses this</h3>
    <ul class="work-list">
      <li>A course with no ap-one manifest publishes through the lean route from one typed line once its repository carries publish scripts in the Psych shape; APUSH's ported scripts are the template.</li>
      <li>Decide the lesson shape from the destination's own live courses before the first push, not from the sibling course that happens to be furthest along.</li>
      <li>Hosted QC order: land article and context changes, take one cold baseline, then run item campaigns through the builder's draft-judge pre-check.</li>
    </ul>
  </section>
  <section id="psych-review-20260916-20260918"><h2>Psych, September 16–18: reviewing a course another team built</h2>
    <p>AP Psychology (Fall 2025) was built by the platform team and published dark on TimeBack. The review (live walk plus API reads, 2026-09-16 to 09-18) is the Course Builder's first use as a reader of someone else's course, and Psych is the lean route's offline fixture (repository commit 834f8262: 21 receipts, 121 audit rows, drift 0). Source: the review's status and machine files in the private review folder.</p>
    <h3>What the review found</h3>
    <ul class="work-list">
      <li><b>Shape:</b> Units 0 to 5, 248 lesson components, each holding video then article then quiz inside one component. This is the shape APUSH later adopted.</li>
      <li><b>16 findings:</b> 10 required, 5 improvements, 1 reporting note. Two block students until fixed together: all 15 FRQs grade through the autograder endpoint the factory banned on 2026-08-10, and the sanctioned grader will not grade the subject until it is certified. Either alone scores every FRQ zero.</li>
      <li><b>Hosted QC number:</b> result 5 scored 90.09% pooled, which hides Unit 0 at 84.6% against Units 1 to 5 at 90.4%; the two figures are quoted separately.</li>
    </ul>
    <h3>How the next course reuses this</h3>
    <ul class="work-list">
      <li>For any course published outside ap-one's operators, read one FRQ's grader definition before trusting FRQ grading; the lean route carries this as a guard.</li>
      <li>Acceptance for a reviewed course is the review plus verified fixes; the cold QC score is a receipt, not a gate.</li>
    </ul>
  </section>
'''
ANCHOR = '  <section id="humgeo-structural-repairs-20260917-20260918">'
assert ANCHOR in t and 'id="apush-lean-route-build' not in t
t = t.replace(ANCHOR, SECTIONS + ANCHOR, 1)
p.write_text(t); print('retro.html updated')
