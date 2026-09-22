#!/usr/bin/env python3
"""One-shot: record five lessons from the HumGeo Final Exam row-shape repair (2026-09-22)
in lessons.html. Same shape as add_humgeo_closeout_20260920.py: one <section> with an
<h2>, a Source paragraph, and a <ul class="work-list"> of <li><b>lesson.</b> explanation.
<i>Builder change:</i> what changed.</li>. Sources: receipts under
~/.incept/humgeo-native/private/final-row-shape-repair-20260922/ and ap-one branch
humgeo/final-native-mock-tests-20260922 (commits 10e4b468, 0fe3640b, 1296be9d); memory
timeback-player-renders-rows-by-lessontype-and-section-kind-20260922."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
p = ROOT / 'lessons.html'
t = p.read_text()

SECTION = '''  <section id="humgeo-final-render-20260922"><h2>September 22: the HumGeo Final Exam was in the course but not on the screen</h2>
    <p>Source: receipts under <code>~/.incept/humgeo-native/private/final-row-shape-repair-20260922/</code> and ap-one branch <code>humgeo/final-native-mock-tests-20260922</code> (commits 10e4b468, 0fe3640b, 1296be9d); memory <code>timeback-player-renders-rows-by-lessontype-and-section-kind-20260922</code>.</p>
    <ul class="work-list">
      <li><b>Data present is not rendered.</b> The Final Exam component existed in the course, in the PowerPath syllabus, and in the owner's recreated lesson plan, yet the learner app showed no unit while the APWH mock exam rendered for the same learner. The only differences were labels: APWH section components carry <code>metadata.kind</code> <code>mock_section1</code> and <code>mock_section2</code>, and its link and resource carry <code>metadata.lessonType</code> <code>"quiz"</code> with XP; HumGeo's resource said <code>"mock_exam"</code> and its links had no <code>lessonType</code>. <i>Builder change:</i> p5 verify now requires every assessment link and resource to carry a lessonType from the fleet enum (quiz, powerpath-100, unit-test, test-out, placement, map-adaptive, alpha-read-article) and section components under a mock exam to carry the mock_section kind, checked by diffing against a fleet course the owner can see.</li>
      <li><b>A QTI resource must not carry toolProvider or launchUrl.</b> With labels fixed the sections opened but read "No questions are available for this lesson yet". GET <code>/powerpath/getAssessmentProgress</code> echoed <code>toolProvider</code> and returned zero questions; the Unit 3 practice resource with neither key returned its ten. They were the AP One launch shape a re-point overwrote instead of removing. <i>Builder change:</i> p5 verify requires getAssessmentProgress for every assessment link to return a question count equal to the QTI test's item count before the phase closes.</li>
      <li><b>A OneRoster PUT merges metadata and cannot drop a key; write null to remove.</b> TimeBack omits null fields on readback, so the sealed runner's readback rule treats a null resource metadata value as absent. <i>Builder change:</i> the operator contract note in p5 says re-points must overwrite or null every launch-shape key, never omit it.</li>
      <li><b>Structure changes need a lesson-plan rebuild for every learner with a plan; field changes show live.</b> POST <code>/powerpath/lessonPlans/{plan}/recreate</code> per learner after adding or re-parenting components; scan every class on the course when listing learners, because a learner enrolled through a second class was missed until the recreate receipt showed a no-plan row. Link and resource field edits (lessonType, XP, URL) need no rebuild. <i>Builder change:</i> p7 verify adds "recreate receipt lists every enrolled learner across all classes; no-plan learners noted".</li>
      <li><b>Fix the live defect first, land the PR after.</b> Three owner-reported defects arrived after the Codex review rounds closed. Each was fixed by a small sealed operator on the branch, executed against the local commit with exact readback and zero-write replay, then folded into the same landing (prep re-run). The round cap is not a reason to hold a live fix. <i>Builder change:</i> none in code; the landing skill's failure playbook records it.</li>
    </ul>
  </section>
'''

ANCHOR = '  <section id="humgeo-lessons-20260922">'
assert ANCHOR in t, 'anchor section not found'
assert 'id="humgeo-final-render-20260922"' not in t, 'section already present'
t = t.replace(ANCHOR, SECTION + ANCHOR, 1)
p.write_text(t)
print('lessons.html updated')
