<p align="center">
  <img src="docs/assets/incept-banner.svg" alt="Incept Course Builder — One line. A few hours. A course live." width="100%">
</p>

<h1 align="center">Incept Course Builder</h1>

<p align="center">One typed line. A few hours later a course is live on TimeBack, at the full Incept bar.</p>

<p align="center">
  <a href="#quick-start"><strong>Install</strong></a> ·
  <a href="docs/getting-started.md">Setup guide</a> ·
  <a href="https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/START.md">How the build works</a> ·
  <a href="https://joshuadurey-del.github.io/incept-course-builder/courses.html">Courses</a> ·
  <a href="https://joshuadurey-del.github.io/incept-course-builder/about.html">About</a>
</p>

<p align="center"><sub>macOS · One command · No model in the loop · Alpha / Incept team access</sub></p>

## Quick start

Paste into Terminal:

```bash
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash
```

**Sign in → pick the course from a menu → three hidden TimeBack strings → the build runs.**

Use a GitHub account with a verified **@alpha.school** email and access to the [private package](https://github.com/InceptTrilogy/ap-four-course-dashboard). Setup checks your machine, reuses existing tools, and installs missing runtime components. [Access or setup help →](docs/getting-started.md)

```bash
~/.local/bin/incept-course-builder
```

No agent is needed. The build is a 1995-style make: every step is a target file, a check and a recipe. A model is called only on a work order, as a compiler, and a script decides.

Every value follows one order of resort: factory bytes at live main, derivation, the answer file, you once, a model on a work order, a person. The last line of every run counts targets by provenance; `authored 0` is the normal case.

Typing the one line is the owner word: a standing authorization is recorded and every paid call, landing and native write cites it. No gate is skipped because of it.

## Your course, in one customized dashboard

<p align="center">
  <img src="docs/assets/workspace-preview.png" alt="Shared course workspace showing course stages, next actions and verification dates." width="100%">
  <br><sub>Public progress view, captured September 10, 2026. Open a course for population coverage and source evidence. Your installed workspace runs locally.</sub>
</p>

| What you get | What it helps you do |
| :--- | :--- |
| **One command** | Install, choose the course, and build; run it again to continue. |
| **The factory's own tools** | Bank gates, the conformance oracle, the judge, the native operators: fetched at a pinned sha and run here. |
| **Whole-course discovery** | Find missing populations before accepting a plan’s progress claims. |
| **An executable runbook** | Plan independent work in parallel; keep integration and publication in order. |
| **A local page** | A progress bar, the four steps, the next target, the provenance counts and open work orders. |

## One front end for the Alpha stack

Step 2 of the build checks Content Factory, GitHub, AWS/S3 and the native TimeBack route and saves the report in the workspace.

## From brief to verified course

| Align | Synthesize | Assemble | Prove |
| :--- | :--- | :--- | :--- |
| Create the blueprint, or reconcile existing sources and coverage. | Author, repair and judge missing content. | Integrate accepted work into the course. | Run native publication and learner checks. |

The build walks these stages with each course’s native tooling. Current permissions, budgets and release gates govern execution. Course completion requires verified learner-facing results.

[Explore the runbook →](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/START.md) · [See reusable value & ROI →](https://joshuadurey-del.github.io/incept-course-builder/economics.html)

## Find your next step

| I want to… | Open |
| :--- | :--- |
| Install, update, change the course or troubleshoot sign-in | [Setup & everyday use](docs/getting-started.md) |
| Understand the build: targets, checks, recipes, the order of resort | [How the build works](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/START.md) |
| Understand the product and access model | [About Incept](https://joshuadurey-del.github.io/incept-course-builder/about.html) |
| Check published course progress | [Course workspace](https://joshuadurey-del.github.io/incept-course-builder/courses.html) |
| Inspect evidence or improve the next build | [Claims](https://joshuadurey-del.github.io/incept-course-builder/claims.html) · [Lessons](https://joshuadurey-del.github.io/incept-course-builder/lessons.html) |

<details>
<summary><strong>For maintainers: source map and local checks</strong></summary>

| Path | Purpose |
| :--- | :--- |
| [app.py](app.py) · [dashboard_service.py](dashboard_service.py) | Local application and persistent macOS dashboard |
| [install.py](install.py) | Installer and managed updates |
| [course-runbook/START.md](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/START.md) | How the build works |
| [course-runbook/factory/](course-runbook/factory/) | Bundled native and workflow skills |
| [course-runbook/make.py](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/make.py) · [course.rules](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/course.rules) | The build runner and the whole build on one screen |
| [COURSE-BUILD-RUNBOOK.md](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/COURSE-BUILD-RUNBOOK.md) | Full narrative runbook |
| [Core package](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook-core.zip) · [Full evidence package](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook.zip) | Downloadable packages |

```bash
python3 -B test_local_builder.py
python3 -B test_coverage.py
python3 -B test_connections.py
node test_asap_ui.cjs
```

With Playwright available, `node test_asap_ui.cjs --browser --local` checks the public reference pages and local dashboard. These checks use synthetic inputs and make no model or factory calls.

```bash
python3 course-runbook/check.py --checkpoint /path/to/workspace/course-state.json
python3 course-runbook/check.py --report /path/to/report.json --checkpoint /path/to/workspace/course-state.json
```

</details>

---

<sub>Private Alpha / Incept distribution. The public dashboard is a separate, read-only view; local course work and credentials stay out of it.</sub>
