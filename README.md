<p align="center">
  <img src="docs/assets/incept-banner.svg" alt="Incept Course Builder" width="100%">
</p>

<h1 align="center">Incept Course Builder</h1>

<p align="center">Create a new TimeBack course, test the complete pipeline on a small course, and resume builds you started here.</p>

<p align="center">
  <a href="#quick-start"><strong>Install</strong></a> ·
  <a href="docs/getting-started.md">Setup guide</a> ·
  <a href="SPEC.md#r7-installer">Build contract</a> ·
  <a href="https://joshuadurey-del.github.io/incept-course-builder/about.html">About</a>
</p>

<p align="center"><sub>macOS · Native factory services · Alpha / Incept team access</sub></p>

## Quick start

Paste into Terminal:

```bash
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash
```

Sign in with a GitHub account that has a verified **@alpha.school** email and access to the [private package](https://github.com/InceptTrilogy/ap-four-course-dashboard). Setup opens three choices:

| Choice | What happens |
| :--- | :--- |
| **Start a new course build** | Save a brief, mission and native blueprint-design work order. This route currently pauses at design; no platform course has been created. |
| **Create a new test course** | Start a small course using the real content, video, QC and TimeBack services. Continue through publication, owner enrollment, learner checks and launch. |
| **Resume a course built here** | Reopen a Builder-created draft or test run with its saved files and receipts. |

Existing TimeBack courses cannot be imported or targeted by entering an ID. Each test creates fresh platform identities; activation is limited to the course created by that run.

## A small course with the real workflow

The test includes one instructional lesson, one article, one video, five article checks, four distinct MCQs across placement, mastery, unit and final assessments, and one graded written response. It exercises grading, XP, progress and completion without requiring a full AP item bank. Its small scope does not certify an AP curriculum.

Before paid calls, connect TimeBack, Content Factory, AlphaVideo and AWS media storage, then approve a supported cost estimate for the exact run. Missing prices remain unmeasured; the Builder cannot enforce a dollar cap within external services.

The Builder asks you to watch the generated video before upload, review its native QC report, and approve creation of the new course. Before launch, use your own learner account to complete the activities and verify scores, feedback, XP and completion. Record those results in the Builder and approve launch. A generated file or passing local test is not learner acceptance.

## Continue from saved evidence

```bash
~/.local/bin/incept-course-builder              # create or resume
~/.local/bin/incept-course-builder status       # selected build's saved status
~/.local/bin/incept-course-builder open         # local page for your selected build
~/.local/bin/incept-course-builder credentials  # configure service connections
```

Configuration, requests, actual hosted job IDs, approvals and complete responses stay in the run folder. A blocked service holds its dependent work while independent content lanes can continue. Resuming reads saved jobs rather than submitting the whole batch again.

The local page displays the selected Builder-owned build. Updates preserve workspaces and credentials and return to the startup menu. [Setup and everyday use →](docs/getting-started.md)

<details>
<summary><strong>For maintainers: source map and local checks</strong></summary>

| Path | Purpose |
| :--- | :--- |
| [app.py](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/app.py) | Startup, workspace ownership and local application |
| [install.py](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/install.py) | Installer and managed updates |
| [course-runbook/test_course.py](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/test_course.py) | Small native course workflow and frozen run state |
| [course-runbook/test_native.py](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/test_native.py) | Fresh course creation, readback, owner enrollment and guarded activation |
| [course-runbook/factory/](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/factory/) | Bundled native and workflow skills |
| [SPEC.md](SPEC.md) | Product and build requirements |
| [Core package](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook-core.zip) · [Full package](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook.zip) | Downloadable releases |

```bash
python3 -B test_course_picker.py
python3 -B test_test_course.py
python3 -B test_test_native.py
python3 -B test_test_media.py
python3 -B test_test_queue.py
node test_asap_ui.cjs
```

These offline checks use synthetic inputs. Native SDK validation and live learner acceptance are separate checks.

</details>

---

<sub>Public documentation for the private Alpha / Incept package; credentials and local run receipts stay in the authorized workspace.</sub>
