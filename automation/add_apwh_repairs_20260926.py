#!/usr/bin/env python3
"""One-shot: fold the APWH repairs record (2026-09-21 to 09-26) into retro.html (round R12), lessons.html, SPEC.md
(R12) and updates.json. Same shape as add_apwh_findings_20260921.py. Every number is copied from the private run folder
(INCEPT/out/apwh-repairs-20260923/OVERNIGHT-LOG.md, witness/DONE.md, state/apwh.DONE, lanes/), the Codex walk and
recheck files (INCEPT/out/apwh-student-review-20260923/, -20260925/, -20260926/), the 09-26 accuracy review
(accuracy-20260926/FINDINGS.md) and the ap-one pull requests named in the text. The same ten rules are NEW-COURSE.md
rules 31-40 in Course Builder release 2026-09-15.75 (InceptTrilogy/ap-four-course-dashboard)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AP = 'https://github.com/InceptTrilogy/ap-one/pull/'
NC = 'https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/NEW-COURSE.md'

RETRO = f'''  <section id="apwh-repairs-20260921-20260926"><h2>APWH, September 21–26: repairing a dark course from three student walks and an accuracy review</h2>
    <p>Evidence window: 2026-09-21 05:10 UTC (the cut of the R9 record) to 2026-09-26 08:45 UTC. Course: AP World History, native TimeBack course <code>ap-world-history-native-202608-v1</code>, still dark. The work began from a Codex student walk on 09-23 that reported six findings, plus three owner reports. Sources: the run log, the frozen definition of done and its check, the lane folders, the Codex walks and rechecks of 09-23, 09-25 and 09-26, and the 09-26 accuracy review, all in the private run folders; and the ap-one pull requests named below. This entry names mechanisms, not people. <a href="lessons.html#apwh-repairs-lessons-20260926">Lessons into practice</a>.</p>
    <h3>What landed</h3>
    <ul class="work-list">
      <li><b>Done by the frozen definition at 04:42 UTC on 09-26.</b> The check printed PASS on all six rows. 210 waves wrote to the live course, and each has a read-back and a zero-write replay; one was undone and has a zero-write undo replay. All 880 article-page check copies equal their live items. Hosted Course QC run 20 read 0.9937 and was stable by the builder's stop rule, and it was submitted after the last item write. Every wave's plan digest is on ap-one main.</li>
      <li><b>26 APWH pull requests merged on ap-one</b>, from <a href="{AP}1212">#1212</a> on 09-24 to <a href="{AP}1259">#1259</a> on 09-26. Each carried the code for waves already live. The owner's 09-24 rule was to land each change as it is implemented; four combined landings (#1228, #1229, #1231, #1248) folded queued lanes on owner approval.</li>
      <li><b>Every 09-23 finding fixed and walked again.</b> Unit 3's hidden lessons came back when the withdrawn lesson-fold operator's own undo reversed the 42 rows it had written on 09-21. Sibling lessons follow the CED's sub-point order (63 sort changes), so WWI casualties now come before WWII. Writing items show criteria, not scorer text, in the grader's own rubric format, and the mock DBQ asks for four documents and two sourced. Drills sit after their teaching, source lines are back, and row titles state question counts and the 80% bar.</li>
      <li><b>Work the walks and owner reports added.</b> Writing skills are taught before they are asked (49 rows). Every LEQ offers a choice of three prompts. The five unit DBQs are served. Lane GB2 wrote per-choice feedback on 2,067 items that had carried stock text. No passage is cut at 1,200 characters any more (0 across 659 tests and 880 checks). An image census checked 331 images and flagged 67: lane IM replaced 173 item images (<a href="{AP}1222">#1222</a>), lane IMP rebuilt 11 figures and 62 checks (<a href="{AP}1224">#1224</a>), and four checks keep labelled AI images by decision. Article checks give two tries with a hint first, and their question stems are bold. Practice text was rewritten to grade 8-12: 1,853 PowerPath 100 questions, 383 article sections and 58 writing asks.</li>
      <li><b>Videos.</b> All nine unit openers were re-rendered. On the owner's P0 rule, every lesson narration was then scanned in course order for lessons not yet taught, and 76 fixed videos went live on the fleet service on 09-24. On 09-25 a second pass rewrote 71 hook narrations as one connected story and rendered them on our own route (the ap-video-openrouter skill), each swap checked by sha.</li>
      <li><b>Hosted QC.</b> Run 10, the first cold run after the repairs, read 0.8953 on 5,893 questions. The burndown then ran through the builder's route. Run 17 hit the halt rule unstable at 0.9910; 30 of its 53 fails were one false-reject class, filed as ap-complete-qc-system #37 with an exclusion row. Runs 19 and 20 read stable at 0.9937.</li>
      <li><b>Walks.</b> Codex ran the course-walk skill on 09-24 (19 pass, 4 fail, 1 unmeasured) and six follow-ups, until no course fail was open. The 09-25 final walk found five findings; two rechecks closed eight in all, six fixed and two shared player behaviors.</li>
      <li><b>After done.</b> A Codex walk minutes after the done check found five more findings. Recheck 1 at 07:10 UTC verified all five fixed (<a href="{AP}1259">#1259</a>, merged 08:24 UTC) and raised four new ones (F6 to F9). The accuracy review found seven live factual errors and more candidates. By 08:45 UTC the accuracy lanes had written 14 + 6 items and 4 article pages (the Engels date, the Condorcet adapted label, a Rousseau answer key, a Lesson 1 check), 30 Unit 1-4 items, 9 Unit 5-9 items and 18 writing items, each with a zero-write replay.</li>
    </ul>
    <h3>What failed, why, and the correction that worked</h3>
    <ul class="work-list">
      <li><b>Main went red twice in one hour.</b> <a href="{AP}1248">#1248</a> changed mock Form 1 without its stored hash. <a href="{AP}1250">#1250</a> fixed the hash, which moved the source capture past its pin. Both merged while their pytest job still ran, because the merge gate refuses only a finished red job. Correction: <a href="{AP}1251">#1251</a> re-pinned; an ap-one pre-push gate now runs three factory verifiers in about 4 seconds; and a data-file PR waits for its pytest to finish green on the exact head (builder rule 31).</li>
      <li><b>The done list had no accuracy row.</b> It stopped invented work, as the owner asked, but it never asked whether the content was true. The walk after done and the accuracy review then found 5 findings and 7 factual errors. Correction: the next done list carries an outside-source accuracy row (rules 32 and 33).</li>
      <li><b>The two judges disagreed on one item.</b> The factory judge passed the rewrite of final-exam Q27 on two runs; hosted run 21 failed it on a weak distractor. Correction: only hosted QC closes a hosted fail (rule 34).</li>
      <li><b>Measures that did not read the live population.</b> A census counted 71 reading rows already marked for deletion. A feedback census counted stock text as feedback and missed 3,177 questions. Unit tests pointed at 36 items that did not exist. Video fixes covered only the flagged rows until the owner found review openers in others. Correction: a census of the live population comes first (rule 39).</li>
      <li><b>Tasks that referred to material they did not show:</b> an SAQ routine's flawed response, an LEQ routine's new prompt, three revise-loop models, and "In the passage" stems with no passage. Correction: every referent resolves inside its item (rule 36).</li>
      <li><b>Scoring text narrower than the College Board rubric</b>, in five places across two walks, a recheck and the accuracy review. Correction: copy the rule from the CED and label an exercise's own constraint (rule 37).</li>
      <li><b>Lanes lost to the machine.</b> A macOS reboot at about 12:43 UTC on 09-23 wiped /tmp. Later the command line stopped every background agent 600 seconds after a turn ended. Correction: lane briefs on disk, foreground agents and pushed branches.</li>
      <li><b>Two drivers on one course.</b> A headless copy of the orchestrator ran beside the interactive window for about an hour and left a dirty page-publish edit in the integration worktree. It stood down at 02:04 UTC on 09-24 and moved its unsealed half-plan aside. Correction: one driver per course, handed off in writing.</li>
      <li><b>A paid video batch stopped on the owner's word.</b> The REMEMBER box overflowed on every first-pass video. The paid parts were reused, so the re-render paid only for 7 unfinished videos, and uploads waited for the owner's gallery review.</li>
      <li><b>Walk transport.</b> The first 09-25 walk attempt measured nothing: the browser connector refused the login, and native Chrome showed another course. The walk that worked copied the Chrome profile and drove headless Chrome over CDP (rule 35).</li>
    </ul>
    <h3>What remains open</h3>
    <ul class="work-list">
      <li>At 08:45 UTC the accuracy lanes' ap-one branches were local, not yet on main. The 23-item mock wave (accuracy rows, recheck F6 to F9 and a Q27 redraft) had a read-only plan and no write. The Unit 5-9 page wave was writing. Codex had not yet rechecked F6 to F9.</li>
      <li>Acronym hovers: the census found 1,167 bare course-written acronyms in 485 items and pages; writes wait on the shared approach's review.</li>
      <li>Residue outside the done list: two gate items with weak distractors (unchanged across runs 18 to 20), tag mis-maps on gate Form 2 (not linked for students), one table with no grid lines, and two shared player behaviors (a reload before "Mark as completed" pays 0 XP; video rows are labelled "Read the article").</li>
      <li>The course stays dark. The owner was told it can go to the learning-science reviewers; publishing, enrollment and activation wait on the owner.</li>
    </ul>
    <h3>How the next course reuses this</h3>
    <ul class="work-list">
      <li>The ten rules are <a href="{NC}">NEW-COURSE.md rules 31 to 40</a> in Course Builder release 2026-09-15.75, and entries on <a href="lessons.html#apwh-repairs-lessons-20260926">the lessons page</a>.</li>
      <li>The short version: wait for pytest on data-file PRs; freeze the done list with an accuracy row; check facts against outside sources; close hosted fails only with hosted QC; take a census before fixing a class; keep every referent inside its item; quote the official rubric; and preview in the real player.</li>
    </ul>
  </section>
'''


def li(anchor, rule, body, step, receipt):
    return (f'      <li id="{anchor}"><b>{rule}</b> {body} <i>Builder step:</i> {step}. '
            f'Receipt: {receipt}.</li>\n')


RULES = [
    ('apwh-r12-pytest-green-on-head-20260926',
     'A data-file PR merges only after its pytest job finishes green on that exact head.',
     f'<a href="{AP}1248">#1248</a> changed mock Form 1 in the bank file without its <code>form_sha256</code>; APWH dropped out of the ready set and 36 tests failed. <a href="{AP}1250">#1250</a> re-hashed it, which moved the source capture, and 112 ingest tests refused until <a href="{AP}1251">#1251</a> re-pinned. Both merged while pytest still ran, because the merge gate refuses only a finished red job. An ap-one pre-push gate now runs three factory verifiers (the feedback catalog, the APWH source pins, the HumGeo rubric pins) in about 4 seconds, but it does not replace pytest. Push once per head: rebase, run the gate and the test files that read the edited file, push, and wait for green. Each push restarts a CI run of about 25 minutes.',
     'land step', f'NEW-COURSE rule 31; <a href="{AP}1259">#1259</a> landed this way'),
    ('apwh-r12-done-list-accuracy-row-20260926',
     'Freeze the done list, and give it a content-accuracy row.',
     'APWH froze six rows, each with a runnable check, on 2026-09-25. That stopped new finish lists. Its halt rule stopped the QC loop at run 17 while the fail set still changed, and runs 19 and 20 then read stable by the builder stop rule. The check passed at 04:42 UTC on 09-26. Minutes later a Codex walk found five new findings, and an outside-source review found seven live factual errors. No row asked whether the content was true, and the walk row rested on samples (25 of 1,012 activity bodies on 09-25).',
     'close-out (definition of done)', '<code>apwh-repairs-20260923/witness/DONE.md</code>, <code>state/apwh.DONE</code>'),
    ('apwh-r12-outside-source-accuracy-20260926',
     'Check facts against outside sources; the judges do not.',
     'The 09-26 review read each claim against a named authority and found seven live errors: Locke listed among the deists in a misconception box, an Engels passage dated 1845 that describes 1850-1870, Self-Strengthening said to start after a rebellion that ended in 1864, the Grand Canal called a Song innovation, a table that erased division of labor before factories, a Haiti paraphrase that overstated abolition, and a DBQ thesis row that required a concession. The final exam also showed a caption reading "verify before publication"; its values were right, but the note reached students. Hosted run 20, which closed the done list, had no content-accuracy fail at all, and the factory judge passed two of the captioned items. Before done, check each claim in articles, tables, items, scorer examples and captions against a named authority in a ledger, and scan served text for authoring notes first.',
     'close-out / p6 QC loop', '<code>accuracy-20260926/FINDINGS.md</code>, <code>lanes/MK26/SOURCE-VERIFICATION-set-5.7.md</code>'),
    ('apwh-r12-hosted-closes-hosted-20260926',
     'Only a hosted QC run closes a hosted QC fail.',
     'The factory judge passed the rewrite of final-exam Q27 on two runs; hosted run 21 failed it on a weak distractor, and that one fail made the split unstable. After any rewrite, re-run hosted QC and keep the item in the burndown until a hosted run passes it. Quote each score with its cache hits: run 9 read 0.9843 warm (5,468 cache hits); run 10, the first cold run after the 09-23 repairs, read 0.8953. The content also changed between them, so the drop cannot be split between cache and content.',
     'p6 QC loop', '<code>lanes/MK26/CERT-100-MK26.md</code>, run log 09-24 04:41 and 09-26 07:17 UTC'),
    ('apwh-r12-walker-recheck-closes-20260926',
     "A walk finding closes only on the walker's own recheck.",
     'Codex runs the course-walk skill from <code>codex exec ... &lt; /dev/null</code>, with the headless route (a copied Chrome profile, headless Chrome over CDP) written into its brief; on 09-25 an attempt that fell back to the browser connector measured nothing. Each recheck writes <code>CLOSURE.json</code> with every finding marked fixed-verified, not-a-defect or still-failing. A finding that shows the same way on other courses is player behavior: record and file it, but do not repair the course. A reading that stays locked after its checks change is a test-account artifact: relaunch the browser first.',
     'p7 learner acceptance', '<code>apwh-student-review-20260925/recheck-1</code> and <code>recheck-2/CLOSURE.json</code>'),
    ('apwh-r12-referents-inside-item-20260926',
     'Every reference in a task resolves inside the same item.',
     'APWH tasks pointed at things the student did not have: an SAQ routine\'s flawed response (the publisher adds model material only to revise loops), an LEQ routine\'s new prompt, three revise-loop models, and MCQ stems that begin "In the passage" with no passage. Before publish, scan each item for references to a passage, document, model, response or prompt, and assert the material is in the served item or on the same page.',
     'p5 verify', '09-26 walk F1, 09-25 recheck F7, lane K2, <code>lanes/SWEEP/scan/mcq</code>'),
    ('apwh-r12-quote-official-rubric-20260926',
     "Scoring text quotes the official rubric, and an exercise's own constraint says so.",
     'Five times APWH stated a rule narrower than the College Board rubric: "Only the first earns the point" for sourcing, complexity required "throughout", "woven throughout or substantially developed" on the final LEQ, a thesis row that required a concession, and ten LEQ reasoning rows plus five DBQ complexity rows. Copy each scoring rule from the current CED. After scorer and student texts are split, check that each student criterion still names the task and the reasoning: 29 criteria had shrunk to bare verbs such as "Explains."',
     'content step (writing rubrics)', '09-25 walk F1, recheck F6, 09-26 walk F4 and F5, accuracy L-F01, waves W6, W26 and W27'),
    ('apwh-r12-practice-readable-exam-hard-20260926',
     'Readability rewrites are for practice; exam forms keep exam difficulty.',
     'Owner, 2026-09-25: "yes i want practice items made easier to read, but the mock and exam-style forms kept at exam difficulty". Scope a grade 8-12 campaign by form membership from the live test item lists: an item on any exam form keeps exam wording, even when practice also uses it. Quality fixes still apply there. APWH had to restore 35 unit-assessment SAQs it had simplified.',
     'content step (readability campaign)', 'NEW-COURSE rule 38; lane F4'),
    ('apwh-r12-census-before-class-fix-20260926',
     'A class fix starts from a census of the whole live population.',
     'Four APWH measures did not read the live course as it was: video fixes covered only flagged rows until the owner found more, and a full narration scan flagged 75; a feedback census counted stock text as feedback and missed 3,177 questions; a measure counted 71 rows already marked for deletion; and nine unit tests listed 90 items while 54 existed. The census reads live test item refs, counts active rows only, treats stock text as missing, resolves every item ref, and scans video narration as well as articles.',
     'every repair lane (measure before fix)', 'lanes VX, GB2, G, J and J2 in <code>apwh-repairs-20260923/lanes/</code>'),
    ('apwh-r12-player-is-the-preview-20260926',
     "The student's player is the only preview.",
     'A render harness that swaps an item\'s XML into the live player with no write showed that a <code>&lt;section&gt;</code> under the prompt is deleted, headings render as body text, lists lose their numbers, and paragraph margins drop to 0. Use inline-styled boxes and check the render before any wave. A same-key video swap needs <code>Cache-Control: no-cache</code>, or Chrome keeps playing the old narration; APWH set the header on 91 swapped hooks.',
     'p5 verify / video step', '<code>apwh-writing-format-20260926/probe</code>, lane CC'),
]

LESSONS = (
    '  <section id="apwh-repairs-lessons-20260926"><h2>September 21 to 26: what the APWH repairs teach the next course build</h2>\n'
    '    <p>Source: the APWH repairs (<a href="retro.html#apwh-repairs-20260921-20260926">retrospective</a>): the run log, the frozen definition of done, three Codex student walks with their rechecks, and the 09-26 accuracy review, read against this page and <a href="' + NC + '">NEW-COURSE.md</a> rules 1 to 30 on 2026-09-26. Rules already stated there (the re-pin in rule 25, the per-course writer lock in rule 22, the headless walk in rule 16) are not repeated. This entry carries ten new rules, the same text as NEW-COURSE.md rules 31 to 40 in Course Builder release 2026-09-15.75.</p>\n'
    '    <h3>New rules</h3>\n'
    '    <ul class="work-list">\n'
    + ''.join(li(*r) for r in RULES)
    + '    </ul>\n'
    '  </section>\n'
)

SPEC_ADD = '''### R12. Rules learned on the APWH repairs (2026-09-21 to 09-26)

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
'''

UPDATE = {'ts': '2026-09-26T09:00Z', 'course': 'APWH', 'writer': 'dashboard curation',
          'text': 'Retro R12, lessons and spec R12: the APWH repairs record (2026-09-21 to 09-26) folded: done by the frozen definition on 09-26, 26 ap-one landings, and ten new rules (Course Builder NEW-COURSE.md rules 31-40, release .75).'}


def patch(path: Path, anchor: str, block: str):
    s = path.read_text()
    assert s.count(anchor) == 1, (path, anchor[:60], s.count(anchor))
    path.write_text(s.replace(anchor, block + anchor))


if 'apwh-repairs-20260921-20260926' not in (ROOT / 'retro.html').read_text():
    patch(ROOT / 'retro.html', '  <section id="apush-lean-route-build-20260919-20260921">', RETRO)
lessons = ROOT / 'lessons.html'
if 'apwh-repairs-lessons-20260926' not in lessons.read_text():
    s = lessons.read_text()
    first = s.index('  <section id="', s.index('<main'))
    anchor = s[first:s.index('>', first) + 1]
    patch(lessons, anchor, LESSONS)
spec = ROOT / 'SPEC.md'
s = spec.read_text()
if '### R12.' not in s:
    s = s.replace('\n## 2b. Where the build stands and what remains', '\n' + SPEC_ADD.rstrip('\n') + '\n\n## 2b. Where the build stands and what remains', 1)
    assert '"spec_version": "2026-09-22.47"' in s
    s = s.replace('"spec_version": "2026-09-22.47"', '"spec_version": "2026-09-26.48"')
    spec.write_text(s)
upd = ROOT / 'updates.json'
rows = json.loads(upd.read_text())
if not any(r.get('text') == UPDATE['text'] for r in rows):
    upd.write_text(json.dumps([UPDATE] + rows, indent=2, ensure_ascii=False))
print('patched retro.html, lessons.html, SPEC.md, updates.json')
