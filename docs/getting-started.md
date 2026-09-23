# Setup and everyday use

[← Incept Course Builder](../README.md) · [Build contract](../SPEC.md#r7-installer)

## What you need

- A Mac and a GitHub account with a verified **@alpha.school** email and access to the private package.
- For the real test: your TimeBack account email, client ID, client secret and organization ID; Content Factory and AlphaVideo access; and AWS access to the media bucket through your existing profile or SSO sign-in.
- The native test tools use `uv`, the AWS CLI and FFmpeg/ffprobe. The Builder installs the pinned TimeBack SDK in a runtime inside the test run. Missing tools or access leave the dependent step open.

## Install and choose a build

```bash
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash
```

Setup checks your Mac, connects GitHub, installs the pinned package and opens the startup menu, including after an update:

1. **Start a new course build** — enter a title, subject, learners, curriculum and goals. The Builder saves the brief, mission and native blueprint-design work order. This route currently pauses for design; the platform identity remains unset.
2. **Create a new test course** — use the default title *Automated Test Course 01* or supply your own, enter your TimeBack account email, and choose the credential file. This starts the small real-service workflow described below.
3. **Resume a course built here** — choose a saved Builder-created draft or test run. It retains its original workspace and receipts.

Existing TimeBack courses are not imported or monitored. Supplying an existing course ID cannot adopt it into this Builder or authorize changes to it.

## Run the complete small test

The test menu offers **Continue this build**, **Show scope, status and costs**, and **Configure service connections**. Configure the connections before continuing. Secret input is hidden; Return keeps each saved value.

The course contains one instructional lesson, one article, one video, five article checks, four MCQs allocated to placement, mastery, unit and final assessments, and one written response with native grading. These small populations exercise the real pipeline; they do not establish AP curriculum coverage.

Continue works through these stages:

1. **Bind your account and approve costs.** TimeBack resolves your account and organization. Supply a supported estimate covering generation, rendering, QC and storage, then approve that exact envelope. An unknown price stays unmeasured. The Builder cannot enforce the entered dollar limit within external services.
2. **Generate and judge content.** The Builder runs the native services, records each hosted job ID and keeps complete responses. It reads the shared video queue before a new render. Only exact jobs you explicitly confirm as abandoned may be canceled; other work is preserved.
3. **Watch and review the video.** Watch the complete saved render before upload. The Builder uploads only a new media object, runs native video QC and shows the report for your disposition.
4. **Create the new course.** Review the small course goals and publication plan. The native adapter mints new identities, refuses active or deleted identity collisions, creates the course and enrolls your bound owner account. It reads the created objects back.
5. **Walk and launch.** Use that account to read the article, play the video, complete the checks and assessments, and submit the written response. Verify grading, feedback, XP, progress and completion. Record the results in the Builder, accept the learner checks and approve launch. Activation can update only this run's newly created course.

If a service is unavailable, independent lanes can continue. A timed-out or ambiguous submission retains its receipt and hosted ID for readback; it is not blindly resubmitted. A finished process, generated file or successful upload is not proof that the course passed its learner checks.

## Everyday commands

```bash
~/.local/bin/incept-course-builder              # create a course or resume your build
~/.local/bin/incept-course-builder status       # selected build's saved status as JSON
~/.local/bin/incept-course-builder open         # open the local page
~/.local/bin/incept-course-builder credentials  # configure service connections
~/.local/bin/incept-course-builder stop         # stop the local page; files stay
```

Use the startup menu to resume a test. `--course <id>` cannot import an outside course or connect a design draft to a legacy publisher.

The local page reads the selected Builder-owned workspace. It does not start generation or paid calls. A menu exit can return success without launching a course; launch status comes from the native readback and recorded owner acceptance.

## Saved files and updates

The installation lives under `~/.local/share/incept-course-builder/`. Its `workspaces/` directory holds separate drafts and test runs, `workspace.json` records the selection, and `releases/<commit>/` holds the pinned package. The chosen credential file is owner-only.

Each test's `test-run/` folder freezes its configuration, tools, requests, approvals, source responses and actual hosted IDs. Keep these files when a step is held; they are the evidence for safe continuation.

To update, rerun the install command. Workspaces and credentials are preserved, and the startup menu reopens. Never install a branch build into a shared installation; use a merged release.

On a non-interactive host, GitHub sign-in needs the `user:email` scope. Add it once in a terminal with `gh auth refresh -h github.com -s user:email`.
