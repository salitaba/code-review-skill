# Code Review Agent Skill

[![skills.sh](https://skills.sh/b/salitaba/code-review-skill)](https://skills.sh/salitaba/code-review-skill/code-review)

A living, evidence-driven skill for high-signal code review.

## Install

Install directly with the skills CLI:

```bash
npx skills add https://github.com/salitaba/code-review-skill --skill code-review
```

The `--skill code-review` selector is supported by the skills CLI. The repository contains a root-level `SKILL.md`, which is a supported discovery location.

After installation, the skill is available to supported coding agents through the standard Agent Skills workflow. skills.sh indexes GitHub-hosted skills automatically when they are discovered/installed.

## Goal

Find defects and design risks that matter to users and systems—not merely changed lines or style preferences.

## Evolution

The skill is evolved iteratively. Improvements must be justified by a concrete blind spot, regression/evaluation evidence, or a materially better review heuristic. Changes that only add verbosity are rejected.

## Canonical artifact

- `SKILL.md` — agent-facing skill
- `references/` — deeper review heuristics
- `references/review-triage-and-evidence.md` — risk-based review depth and evidence calibration
- `evolution/` — change history and decisions

## Current improvement

The latest iteration adds rollout/migration safety, before-versus-after behavior comparison, and a stronger evidence ladder so the reviewer spends deep effort on trust, state, ownership, compatibility, and failure boundaries, while downgrading weakly evidenced concerns to focused questions instead of overstated blockers.

## skills.sh

The public skill page is:

`https://www.skills.sh/salitaba/code-review-skill/code-review`

The page becomes available after skills.sh indexes the repository; the GitHub repository itself remains the canonical source.
