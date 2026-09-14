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
- `references/` — deeper review heuristics, loaded by `SKILL.md` when a trigger applies
- `references/dependency-and-delivery-review.md` — dependency, build, CI/CD, container, infrastructure, and release review
- `references/review-decision-record.md` — decision boundary, assumptions, evidence, residual risk, and review limits
- `evolution/` — change history and decisions
- `evals/` — adversarial review cases; run with `claude plugin eval .`, validated with `claude plugin validate .`
- `.claude-plugin/plugin.json` — plugin manifest, enabling plugin install and first-party eval
- `scripts/check-consistency.sh` — fails when a reference is not loadable by `SKILL.md`, when the version disagrees between `SKILL.md`, `.claude-plugin/plugin.json`, and the changelog, or when a grader name breaks the prefix contract

## Current improvement

The latest iteration wires the dependency and delivery reference into the review workflow and makes reference wiring checkable, so a reference that `SKILL.md` never loads fails the check instead of silently claiming review coverage the agent will not apply.

## skills.sh

The public skill page is:

`https://www.skills.sh/salitaba/code-review-skill/code-review`

The page becomes available after skills.sh indexes the repository; the GitHub repository itself remains the canonical source.
