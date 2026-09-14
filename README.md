# Code Review Agent Skill

[![skills.sh](https://skills.sh/b/salitaba/code-review-skill)](https://skills.sh/salitaba/code-review-skill)

A living, evidence-driven skill for high-signal code review.

## Install

Install directly with the skills CLI:

```bash
npx skills add https://github.com/salitaba/code-review-skill --skill code-review
```

The `--skill code-review` selector is supported by the skills CLI. After installation the skill is available to supported coding agents through the standard Agent Skills workflow.

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

The latest iteration makes the eval suite refuse to overstate itself. The reducer now reports when a case scores no better with the skill than without it, rather than averaging that away into a lift figure, and the restraint case no longer carries a grader that penalised a well-calibrated `Minor` finding for being reported at all.

## skills.sh

The badge above uses the format skills.sh documents —
`https://skills.sh/b/owner/repo`, linking to `https://skills.sh/owner/repo`.
It renders an install count, which skills.sh derives from anonymous telemetry
collected by its own CLI.

That count is empty for this repository, so the badge currently resolves to
`resource not found`. Nothing in the repository can change this: the badge
reports data skills.sh has, and it acquires data by being installed through the
skills CLI. Until this repository is installed that way, treat the badge as a
placeholder and the GitHub repository as the canonical source.
