# Setup & everyday use

[← Incept Course Builder](../README.md) · [About](https://joshuadurey-del.github.io/incept-course-builder/about.html) · [Agent runbook (team access)](https://github.com/InceptTrilogy/ap-four-course-dashboard/blob/main/course-runbook/START.md)

## Before you start

- A Mac and an internet connection for the first install.
- A GitHub account with a **verified `@alpha.school` email** and access to the [private InceptTrilogy package](https://github.com/InceptTrilogy/ap-four-course-dashboard).
- Your preferred agent and its model access. Setup can also produce a portable prompt for another host.

## Install

Paste this into Terminal:

```bash
curl -fsSL https://joshuadurey-del.github.io/incept-course-builder/install.sh | bash
```

The installer checks your machine, reuses installed tools, and downloads missing runtime components into the app directory. It requires no administrator password or shell-profile edit. Onboarding happens in Terminal: GitHub sign-in, course name, agent choice, then dashboard or agent launch.

**Watch progress in your customized dashboard.** It updates as your agent saves coverage, completed work and its next action. The dashboard runs independently through macOS: closing Terminal or navigating away does not stop it. Reopen the same local address to see saved progress. Run `incept-course-builder build` to resume the agent; the dashboard itself stays available after that session ends.

The public Courses page is a shared reference, not your installed workspace. Local dashboard refreshes read saved progress only; they do not launch work or call paid services.

## When something is needed from you

Your agent resolves ordinary setup, retries and workflow choices. It reuses existing access and authorization. A missing-input request must give you one concrete action, such as a hidden-input Terminal command or the existing service's browser sign-in. If you do not have access, it provides the verified retrieval steps, access owner or request channel, and a prepared message. Never paste secrets into chat or the dashboard.

The request gate checks agent reports and what appears in the local dashboard. Local agent hosts must follow the bundled instruction to run it before speaking; the builder cannot intercept every host's conversation. Native spending limits, access checks and required release approvals still apply.

## Everyday commands

```bash
~/.local/bin/incept-course-builder          # Open your local dashboard
~/.local/bin/incept-course-builder build    # Start your selected agent
~/.local/bin/incept-course-builder onboard  # Change your course or agent
~/.local/bin/incept-course-builder scan     # Inspect tools offline
~/.local/bin/incept-course-builder connect  # Check native connections; no course work
~/.local/bin/incept-course-builder stop     # Stop only the dashboard; preserve course work
```

Choose **Claude Code**, **Codex**, **Hermes**, a custom local command, or a portable prompt during onboarding. Automated execution needs an agent with filesystem and terminal tools. Keep using your existing model credentials and subscription; the builder does not provide model access.

## Connect the native stack

Run `incept-course-builder connect` for read-only connection checks, or `incept-course-builder build` to check and continue with your agent. The agent resolves existing course repository, AWS profile, S3 prefix and native publish configuration; only references go in `workspace/connections.config.json`. Credentials stay with their existing providers. `CONNECTIONS.json` supplies a dated connection report to the local dashboard and agent. Source coverage and learner acceptance still require their native verifiers.

## From zero to a complete course

The builder walks four steps in a fixed order, for a new course and for an existing one alike. A script chooses the step from receipts on disk; your agent does the work the step card names and closes it with a receipt. Skipping is refused.

1. **Standards, essential knowledge, assessments.** Reconcile or author the blueprint on its nine dimensions, build the coverage matrix (every essential knowledge statement has a lesson, a practice item and an assessment item), and write the media rule.
2. **Course map.** Fill the course profile, emit the unit and topic tree, price lessons by type, and give every unit an assessment milestone.
3. **Lessons with checks.** Prove one lesson end to end (article, five checks, judge, render). Then author the rest in complete forms with one owner each: free prescreens before every paid judge call, bank gates on one candidate SHA.
4. **Host and present.** Publish dark with three receipts per native write, run cold course QC and sort failures by class, walk the course once on a test account, then the designated reviewer decides and enrollment is read back.

An existing course starts at step 0 too. At steps 1 to 3 the agent sorts what already exists into keep, modify, replace or discard, using the factory's own checks; only the replace and missing rows get new work. Templates for the mission, intake rows, articles, five-check sets, forms and titles ship in the package, so a small model fills and checks instead of designing.

Non-interactive hosts: the GitHub sign-in must already carry the `user:email` scope (`gh auth refresh -h github.com -s user:email`, once, in a terminal). Then run the install command with `--no-onboard`, fill `templates/mission.json`, then `incept-course-builder onboard --mission-file <path> --agent <codex|claude|hermes|prompt>`. The same loop reaches Codex through `AGENTS.md`, Claude Code through `CLAUDE.md`, and any other host through the exported prompt.

The complete course is the target. Setup grants no course, spend or publication authority; the owner walk and the designated reviewer decision remain human steps. Read the [spec sheet](https://joshuadurey-del.github.io/incept-course-builder/spec.html) for each step's factory shape, tooling and closing receipt.

## Skills & factory tooling

The private release bundles the official [Content Factory skillpack](https://content-factory.inceptstore.com/#download) and workflow skills with their scripts and references. After download, bundled skill setup works offline: missing skills are copied, custom files are preserved, and version differences are reported.

Native repositories, service credentials and course configuration are resolved from current factory instructions. Installing the builder alone does not configure every course service.

## GitHub sign-in

The installer uses GitHub CLI’s browser OAuth flow. It requests `user:email` to check your verified work email; existing logins request this scope only when needed. Tokens and email lists are not saved in installer logs or settings.

If your work email is missing, add and verify it in [GitHub email settings](https://github.com/settings/emails), then rerun the installer. It does not need to be your primary email. A verified email and access to the private repository are separate requirements.

An environment token must already provide email-read and repository access. Browser consent cannot expand an externally supplied token. If GitHub sign-in succeeds but package download fails, check that the same account can open the private repository.

## Update or remove

**For maintainers:** skill changes ship in the private builder repository with their scripts, affected runtime consumers and rebuilt installation package. Validate both bundled resources and the installed code path; a dashboard-only edit is not a builder update. Public documentation follows the actual installable release.

**Update:** the installer reuses your saved course and agent settings, preserves course work and existing skills, and reopens the dashboard. Onboarding is only repeated when you explicitly request it. Changed managed release files are left for review rather than silently overwritten.

**Remove:** back up any course work, then run `incept-course-builder stop` to unregister its macOS dashboard service. Then remove the app directory at `~/.local/share/incept-course-builder` and the launcher at `~/.local/bin/incept-course-builder`. Runtime dependencies installed by this app are contained in its directory.

## Privacy

The public repository serves the dashboard, published observations, product documentation and install entry point. The private repository contains the builder package and agent resources. Course content, credentials and local checkpoints are not served by the public site. Agent and factory calls use the services configured for your authorized workflow.
