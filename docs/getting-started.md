# Setup and everyday use

[← Incept Course Builder](../README.md) · [How the build works](../course-runbook/START.md) · [The rules file](../course-runbook/course.rules)

## What you need

- A Mac. The installer reuses an installed GitHub CLI and Python 3.11 or newer, and otherwise downloads its own copies into the app directory.
- A GitHub account with a verified alpha.school email and access to the private package.
- TimeBack credentials: client id, client secret and organization id. AWS uses your existing profile or SSO sign-in.

## The one line

```
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash
```

Four screens: your Mac is checked, GitHub is connected, the pinned release is installed, and the build starts. The build shows a numbered menu of course ids read live from ap-one and asks for the three TimeBack strings with hidden input. Then it runs. With `--course <id>` on the install line and the TimeBack names in the environment there are no prompts at all:

```
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash -s -- --course ap-world-history-fall-2026-v1
```

Typing the line is the owner word. The build records a standing authorization with the account, time, course and scope until the course is live. Every paid call, landing and native write cites it. No gate is skipped because of it.

## What the build does

`make.py` reads `course.rules`, a build file in the 1995 shape: every step is a target file, a check and a recipe. A target is rebuilt when it is missing, older than a prerequisite, or failing its check. Run the command again any time; only what is missing or stale rebuilds. The progress lines read like a build log:

```
  profile.json .................................. fetched
  course-map.json ............................... derived
  lessons/004/article.md ........................ open

  STOP 3  work orders open (50)   fetched 18   derived 806   answered 2   authored 0   person 0
```

Every value follows one order of resort, and a model is next to last: factory bytes fetched at live main and pinned; derivation from those bytes; the answer file; you, asked once and saved; a model called on a work order and checked by a script; a person. The last line counts targets by provenance. `authored 0` is the normal case when the factory's bytes are complete.

## The screen

After every build you see one screen: the course, the steps with a detail each, WHAT IS MISSING in plain words, and WHAT YOU CAN DO as a numbered list of only what this Mac can run now. Type the number and it runs.

```
  AP WORLD HISTORY: MODERN
  ✓ Course map                    9 units · 176 lessons · 6576 XP
  ! Lessons with checks           126 of 176 articles · 176 of 176 checks judged · 782 of 884 pieces
  · Bank gates                    0 of 8 pieces

  WHAT IS MISSING
    50 lessons have no accepted article. The factory's own quality check rejected the ones it had.

  WHAT YOU CAN DO
    1  Write them with a local model
    2  Write the 50 missing pieces with Claude (small model)   paid · about 50 drafting calls
    3  Show me which lessons
    4  Open the course page in the browser
    5  Stop for now
  >
```

No step starts until the previous step's receipt exists. While it builds, one counter line rewrites itself.

## Stops

| Exit | Meaning | What prints |
|---|---|---|
| 0 | the course is live | the readback and the time |
| 1 | a check failed | target, check, observed, expected |
| 2 | network or sign-in | the exact command to run |
| 3 | work orders open | file, what, shape, last finding |
| 4 | an answer is needed | the one line to add to the answer file |

Nothing else is printed to you.

## Work orders

What the factory has not committed becomes `workspace/workorders/<target>.json`: every fact the artifact needs and its exact shape, sized for a local 30B model. If a local OpenAI-style server answers on port 1234 or 11434 the build uses it as the author seat and records `AUTHOR_CMD` in the answer file; any `{prompt_file}` command works too. The author's output is checked by the free prescreen, then judged by the factory's paid judge, three tries. What it cannot fill waits for a person. An operator the course profile marks not implemented is a factory pull request, never authored here.

## Everyday commands

```
~/.local/bin/incept-course-builder                 # build (the default); run again to continue
~/.local/bin/incept-course-builder --course <id>   # choose or change the course without the menu
~/.local/bin/incept-course-builder open            # open the local page
~/.local/bin/incept-course-builder status          # the build as JSON
~/.local/bin/incept-course-builder credentials     # enter the TimeBack strings again (hidden)
~/.local/bin/incept-course-builder stop            # stop the local page; files stay
```

## The local page

It shows where the course is: a progress bar, the four steps, the next target, the provenance counts and open work orders. Click a step for its targets and receipts; the course map shows units, topics and lessons with each part labeled. It runs locally through macOS after Terminal closes and never launches work or calls paid services.

## Files

Everything lives under `~/.local/share/incept-course-builder/`: `workspace/` (the build), `credentials.env` (owner-only), `releases/<commit>/` (the pinned package), `current` (a link to it). The workspace files are the state; there is no other memory.

**Update:** re-run the install command. Course work and credentials are preserved; the next build continues where it left off.

**Non-interactive hosts:** the GitHub sign-in must carry the `user:email` scope (`gh auth refresh -h github.com -s user:email`, once).
