#!/usr/bin/env python3
"""One-shot: fold the HumGeo student-review record, second pass (2026-09-26, after release .74), into
retro.html (round R13), lessons.html, SPEC.md (R13) and updates.json. Same shape as
add_apwh_repairs_20260926.py. Every number is copied from the private run folder
(INCEPT/out/humgeo-student-review-20260923/lanes/retro/RETRO-20260926b-humgeo-student-review.md,
FINISH-CRITERIA.md, WIND-DOWN.md, lanes/) and the ap-one pull requests named in the text. The same ten
rules are NEW-COURSE.md rules 41-50 in Course Builder release 2026-09-15.76
(InceptTrilogy/ap-four-course-dashboard)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AP = 'https://github.com/InceptTrilogy/ap-one/pull/'
NC = 'https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/NEW-COURSE.md'

RETRO = f'''  <section id="humgeo-student-review-second-pass-20260926"><h2>HumGeo, September 26 (second pass): acronym hovers, a review screen fixed, and a reading-grade floor that read stilted</h2>
    <p>Evidence window: 2026-09-26 02:27 UTC to 08:55 UTC, continuing the student-review window closed out in Course
    Builder release .74. Course: AP Human Geography, native TimeBack course <code>ap-human-geography-native-202608-v3</code>,
    still dark. The window fixed a Codex walk finding, built acronym hovers to an owner spec agreed with the APWH and
    APUSH windows, and formatted the Technique Drill and FRQ screens. Sources: the retrospective, the finish
    criteria and wind-down files, the lane folders, and the ap-one pull requests named below. This entry names
    mechanisms, not people. <a href="lessons.html#humgeo-retro2-lessons-20260926">Lessons into practice</a>.</p>
    <h3>What landed</h3>
    <ul class="work-list">
      <li><b>Three ap-one pull requests merged.</b> <a href="{AP}1255">#1255</a> (writing-layout template and rubric
      rows; 327 of 327 writing items already served), <a href="{AP}1257">#1257</a> (the cumulative-FRQ successor fix
      for the review-screen finding below), and <a href="{AP}1258">#1258</a> (the acronym-hover gate code, pushed
      three times: a first head that went red, a fix, then a final rebase). The owner's push-once rule arrived
      partway through the window and governed each PR's final push from then on: rebase onto current main, run the
      gate and the reading test files by hand, push once, wait for the merge slot.</li>
      <li><b>A review screen that showed a score but no answers, fixed.</b> Two completed cumulative-FRQ attempts
      showed in the gradebook, but every question panel in their review read "(no response)". The operator that
      repoints a test's items had kept the test's id while swapping its three item references, so an old attempt's
      stored answers had no question id to attach to. The fix copies the successor-identity pattern AP Lit and APWH
      already use: a changed test gets a new id bound to the new items, the old id keeps the old items, and a new
      guard refuses the old in-place swap once any attempt exists.</li>
      <li><b>Acronym hovers, wave 1 and wave 2 live.</b> Following an owner spec agreed with the APWH and APUSH
      windows (every acronym inside a lesson gets a hover with the full words; exam forms carry none; a page's
      acronym list gives a sourced definition the first time and the full words only after that), wave 1 put hovers
      on 25 article checks, 7 video checks and 30 article pages (265 hovers plus the page list), and wave 2 put them
      on 207 PowerPath practice items. Both waves read back equal to their candidates, and both replays wrote 0.</li>
      <li><b>A 29-acronym definitions file, drafted and checked.</b> Each definition is sourced from the course's own
      text or, for FAO/USDA/GPS, the organization's own source; Gemini's accuracy check caught and fixed two errors
      (GNP's citizenship and location reversed; GPS credited to the wrong service); four definitions were trimmed so
      they do not give away an answer on their own page.</li>
    </ul>
    <h3>What failed, why, and the correction that worked</h3>
    <ul class="work-list">
      <li><b>A new PR's first head went red on a mechanical gap, caught before the merge.</b> <a href="{AP}1258">#1258</a>
      added two new <code>services/ingest</code> modules with no CLI. The repository's import-safety test reads
      every module under that folder by glob, but pytest only runs the test files a command names, so a local run
      that named only the touched files never included it, and the PR's first head went red on two tests.
      Correction: list a CLI-less module in <code>LIBRARY_MODULES</code> with a reason before the merge, and the
      pre-push gate now runs that test itself whenever a <code>services/ingest</code> file changes (builder rule 41).</li>
      <li><b>A local rebase does not count until it is pushed.</b> merge-gate's freshness check reads the PUSHED
      head, not the local one. A lane rebased its branch locally and ran the gate before pushing that commit, so the
      gate still read the old, unpushed remote head and refused it as behind main. Correction: when given the merge
      slot, rebase onto <code>origin/main</code>, run the gate and the tests that read the change, then push that
      commit once and wait for its CI (builder rule 42); each push restarts a roughly 25-30 minute CI run and a
      second push mid-run cancels it.</li>
      <li><b>A hand-typed pytest command hid its own file names from the guard.</b> The pytest guard is a Claude
      Code PreToolUse hook: it reads the command string before the shell runs it, so it never sees what a shell
      variable expands to. A command that built a variable of test file paths and passed the variable to
      <code>pytest</code> showed the guard the variable's literal name, not a <code>.py</code> path, and it blocked
      as "no test file named". Correction: type the file paths directly in the command (builder rule 43).</li>
      <li><b>A standalone lane clone's push skipped the shared pre-push chain.</b> A clone under
      <code>~/repos/incept-scratch/</code> with its own <code>.git</code> had no <code>core.hooksPath</code> set, so
      four early pushes reached GitHub without running the chain at all. Correction: <code>core.hooksPath</code> is
      now set globally, so every clone on the machine runs it; one caveat found the same day, <code>scripts/ship.py</code>
      sets a local override that beats the global (builder rule 44).</li>
      <li><b>A same-key page rewrite left the hosted QC reader blind to its own new content.</b> Wave 1 wrote 30
      pages with a same-key S3 PUT that changed only the visible acronym list. The hosted Course QC reader reads a
      hidden text block inside the stimulus, not the rendered page, and that block was not rebuilt, so the reader
      still saw the old page. Correction: the page-write route now rebuilds the hidden block on every page it
      touches (builder rule 45).</li>
      <li><b>The factory's writing-item judge cannot score HumGeo's writing bank.</b> Before spending on it, a lane
      read the factory's own check code and found the FRQ check needs three fields (learning-objective codes, skill
      codes, a graded model answer) that HumGeo's writing bank has never carried, so every call would have failed on
      request shape, not content. Correction: use the course's own writing judge instead — for HumGeo, the W8 judge
      on a before-and-after pair, counting a new finding against the change only when it quotes text the change
      added, with the deployed FRQ grader giving identical scores before and after (builder rule 46).</li>
      <li><b>A false alarm from a stale crawl.</b> A report that two live pages had lost their acronym list turned
      out to be a byte search against page URLs from an earlier crawl; wave 1 had already moved both pages to new
      object keys, so the search read orphaned copies. Correction: re-read the live page index for the current href
      before reporting a page defect (builder rule 47).</li>
      <li><b>Definitions written to clear the reading-grade floor read garbled to a person.</b> All 29 drafted
      definitions passed the automated grade-8 check, but a human read of every row as a student would caught one
      garbled definition (an exam-question type described as "graded in prose rather than essay format") and four
      more that named "this course" instead of stating the fact plainly. Correction: read every generated definition
      as a student would before it ships, and never let course-referencing filler stand in for the fact (builder
      rule 48).</li>
      <li><b>A ledger-backstop flag was a false positive on quoted item data.</b> A duration-sounding phrase ("women
      spent 34 hours on unpaid work, compared with 12 for men") tripped a receipt-claim scan; it is an answer
      rationale quoting an item's own chart, byte-identical to the live course, not an unsourced duration claim, so
      it was left as it was written.</li>
    </ul>
    <h3>What remains open</h3>
    <ul class="work-list">
      <li>Definitions are final: 29 written, 25 placed (24 on pages and 1 on a writing task, by the first-list rule
      that a definition appears once per course, in course order).</li>
      <li>Acronym page rebuild is in progress: 28 pages plus 5 held pages get their definitions and their hidden
      text block rebuilt together; writing-task hovers are next.</li>
      <li>The table-title fix is LIVE: 7 pages and 8 checks, all 15 read back equal to their candidates.</li>
      <li>Map images are in progress: 148 places, 285 visuals, 22 of them on exam forms; two free rendering routes
      run in parallel at roughly 100 to 130 images an hour each.</li>
      <li>The Technique Drill and FRQ layout is FINISHED: all 327 writing items carry the template
      (<a href="{AP}1255">#1255</a> merged).</li>
      <li>The final hosted Course QC run, after all of the above, is still to come.</li>
      <li>The course stays dark. No enrollment or activation changed.</li>
    </ul>
    <h3>How the next course reuses this</h3>
    <ul class="work-list">
      <li>The ten rules are <a href="{NC}">NEW-COURSE.md rules 41 to 50</a> in Course Builder release 2026-09-15.76,
      and entries on <a href="lessons.html#humgeo-retro2-lessons-20260926">the lessons page</a>.</li>
      <li>The short version: run the import-safety test by name for any new ingest module; push once, with the
      final rebased head, when given the merge slot; name pytest files literally; keep every lane clone on the
      shared hooks path; rebuild a page's hidden text block on every in-place rewrite; check a writing bank's
      fields before paying for a factory judge call; read a page through its current href; read a generated
      definition as a student would; keep a table's title out of its header cell; and render a described map or
      chart as a real image.</li>
    </ul>
  </section>
'''


def li(anchor, rule, body, step, receipt):
    return (f'      <li id="{anchor}"><b>{rule}</b> {body} <i>Builder step:</i> {step}. '
            f'Receipt: {receipt}.</li>\n')


RULES = [
    ('humgeo-r13-import-safety-by-name-20260926',
     'A new services/ingest module needs the import-safety test run by name, and a LIBRARY_MODULES entry if it has no CLI.',
     f'ap-one\'s <code>tests/ingest/test_import_safety.py</code> reads every module under <code>services/ingest/</code> by glob, and pytest runs only the test files a command names, so a local run that names only the touched files never includes it. <a href="{AP}1258">#1258</a> added two pure-library modules with no <code>main()</code>, and its first head went red on 2 tests; the fix landed before the merge. List a new library module in <code>LIBRARY_MODULES</code> with a reason, and run this test by hand after any new file lands under <code>services/ingest/</code>.',
     'land step', f'NEW-COURSE rule 41; <a href="{AP}1258">#1258</a>'),
    ('humgeo-r13-push-before-slot-20260926',
     'Push once, with the final rebased head, only when you are given the merge slot.',
     f'merge-gate\'s <code>base-fresh</code> row refuses a PR whose head does not contain current <code>origin/main</code>, and it checks the PUSHED head: a rebase that exists only in the local clone does not count. <a href="{AP}1257">#1257</a> hit this once: the lane had rebased locally but the PR head was still the old commit. Each merge of another PR puts every open PR behind main again, and each push starts a CI run of about 25-30 minutes (a push mid-run cancels it). So when given the slot: rebase onto <code>origin/main</code>, run the gate and the tests that read the change, then push that commit once and wait for its CI.',
     'land step', f'NEW-COURSE rule 42; <a href="{AP}1257">#1257</a>'),
    ('humgeo-r13-literal-pytest-files-20260926',
     "Name pytest's test files literally; a shell variable hides them from the pytest guard.",
     'The pytest guard is a Claude Code PreToolUse hook: it reads the command string before the shell runs it, so it never sees what a shell variable expands to. A command that built <code>files=$(grep -rl ...)</code> and ran <code>pytest $files</code> showed the guard the literal token <code>$files</code>, not a <code>.py</code> path, so it blocked as "no test file named" even though real files were meant. Type the test file paths directly in the pytest command.',
     'land step', 'NEW-COURSE rule 43'),
    ('humgeo-r13-lane-clone-hookspath-20260926',
     "Lane clones get the pre-push gate from the global hooks path; don't let ship.py override it.",
     'A standalone clone (its own <code>.git</code>, not a worktree of the shared checkout) has no <code>core.hooksPath</code> by default, so a push from it never runs ap-one\'s pre-push chain; four HumGeo heads reached GitHub ungated this way. <code>core.hooksPath</code> is now set GLOBAL to <code>~/.claude/scripts/apone-hooks</code>, so every clone runs the chain automatically. One exception: <code>scripts/ship.py</code> sets a LOCAL <code>core.hooksPath=.githooks</code> in the clone it runs in, which overrides the global — do not run <code>ship.py</code> in a lane clone, or unset the local key right after.',
     'land step', 'NEW-COURSE rule 44'),
    ('humgeo-r13-rebuild-hidden-block-20260926',
     "A same-key rewrite of a page's stimulus must rebuild the hidden article-text block, not only the visible one.",
     'The hosted Course QC reader reads a hidden <code>article-text</code> block inside the stimulus, not the rendered page. A same-key S3 PUT that changed only the visible acronym list on 30 pages left the old hidden block in place, so the reader could not see the new content at all. Every operator that edits a page\'s stimulus in place must call the same hidden-block builder the page\'s original publish step used.',
     'p5 verify', 'NEW-COURSE rule 45'),
    ('humgeo-r13-vqc-writing-fields-20260926',
     'Check a writing bank carries lo_codes, skill_codes and a model_answer before sending it to /v1/qc.',
     'The factory\'s FRQ check fails every call (checks S1, S2, F2) on a writing bank missing any of the three, whatever the content quality — the failure means the request is the wrong shape, not that the writing is bad. Read the factory\'s own check code for the exact field names before paying for a call. Where a course\'s bank does not carry them (HumGeo\'s never has), use that course\'s own writing judge: for HumGeo, the W8 judge on a before-and-after pair. A new finding counts against the change only when it quotes text the change added, and the deployed FRQ grader must give identical scores to the same responses before and after.',
     'p6 QC loop', 'NEW-COURSE rule 46'),
    ('humgeo-r13-live-href-not-crawl-20260926',
     'Read a page through its current href, not a saved crawl.',
     'After a page write moves a page to a new object key, a byte search against an earlier crawl\'s URLs reads the old, orphaned object and can report a page as missing content it actually still has — as happened on a report of two "list-less" pages that in fact both carried the list. Re-read the live page index for the current href before reporting a page defect.',
     'p6 QC loop', 'NEW-COURSE rule 47'),
    ('humgeo-r13-read-definitions-as-student-20260926',
     'A definition padded to clear a reading-grade floor still has to read like a sentence.',
     'All 29 drafted acronym definitions passed the automated grade-8 checker; a human read as a student would still caught one garbled definition and four that named "this course" instead of stating the fact. Read every generated definition or rewrite as a student would before it ships; state the fact plainly, never by pointing at the course itself.',
     'content step (readability campaign)', 'NEW-COURSE rule 48'),
    ('humgeo-r13-table-title-header-cell-20260926',
     "A table's title must not share a header cell with a column label.",
     'A table titled "Example table (illustrative): downtown workers by home distance" put both the title and the header label for its data column in one cell, so a plain read runs them together as one phrase. Give the table a caption or heading OUTSIDE the header row, and let the header row hold only its column labels.',
     'content step (stimulus build)', 'NEW-COURSE rule 49'),
    ('humgeo-r13-map-needs-real-image-20260926',
     'A question that names a map, chart or scatterplot needs a real rendered image, not a text description standing in for it.',
     'Standing ruling 2026-09-02: "we can use tables but if it mentions an image or scatterplot etc then we need to use the factory tooling." Before writing an item that refers to a visual, check whether the real exam would show it as an actual image; if so, render it with the factory\'s own image tooling instead of describing it in prose.',
     'content step (stimulus build)', 'NEW-COURSE rule 50'),
]

LESSONS = (
    '  <section id="humgeo-retro2-lessons-20260926"><h2>September 26 (second pass): what the HumGeo acronym-hover and review-screen repairs teach the next course build</h2>\n'
    '    <p>Source: the HumGeo student-review record, second pass (<a href="retro.html#humgeo-student-review-second-pass-20260926">retrospective</a>): the retrospective, the finish criteria and wind-down files, and the ap-one pull requests, read against this page and <a href="'
    + NC + '">NEW-COURSE.md</a> rules 1 to 40 on 2026-09-26. This entry carries ten new rules, the same text as NEW-COURSE.md rules 41 to 50 in Course Builder release 2026-09-15.76.</p>\n'
    '    <h3>New rules</h3>\n'
    '    <ul class="work-list">\n'
    + ''.join(li(*r) for r in RULES)
    + '    </ul>\n'
    '  </section>\n'
)

SPEC_ADD = '''### R13. Rules learned on the HumGeo student-review record, second pass (2026-09-26)

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
'''

UPDATE = {'ts': '2026-09-26T09:05Z', 'course': 'HumGeo', 'writer': 'dashboard curation',
          'text': 'Retro R13, lessons and spec R13: the HumGeo student-review record, second pass (2026-09-26), folded: a review-screen fix, acronym hovers on the agreed spec, and ten new rules (Course Builder NEW-COURSE.md rules 41-50, release .76).'}


def patch(path: Path, anchor: str, block: str):
    s = path.read_text()
    assert s.count(anchor) == 1, (path, anchor[:60], s.count(anchor))
    path.write_text(s.replace(anchor, block + anchor))


if 'humgeo-student-review-second-pass-20260926' not in (ROOT / 'retro.html').read_text():
    patch(ROOT / 'retro.html', '  <section id="apwh-repairs-20260921-20260926">', RETRO)
lessons = ROOT / 'lessons.html'
if 'humgeo-retro2-lessons-20260926' not in lessons.read_text():
    s = lessons.read_text()
    first = s.index('  <section id="', s.index('<main'))
    anchor = s[first:s.index('>', first) + 1]
    patch(lessons, anchor, LESSONS)
spec = ROOT / 'SPEC.md'
s = spec.read_text()
if '### R13.' not in s:
    s = s.replace('\n## 2b. Where the build stands and what remains', '\n' + SPEC_ADD.rstrip('\n') + '\n\n## 2b. Where the build stands and what remains', 1)
    assert '"spec_version": "2026-09-26.48"' in s
    s = s.replace('"spec_version": "2026-09-26.48"', '"spec_version": "2026-09-26.49"')
    spec.write_text(s)
upd = ROOT / 'updates.json'
rows = json.loads(upd.read_text())
if not any(r.get('text') == UPDATE['text'] for r in rows):
    upd.write_text(json.dumps([UPDATE] + rows, indent=2, ensure_ascii=False))
print('patched retro.html, lessons.html, SPEC.md, updates.json')
