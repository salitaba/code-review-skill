# Code Review Agent Skill

[![skills.sh](https://skills.sh/b/salitaba/code-review-skill)](https://skills.sh/salitaba/code-review-skill)

A living, evidence-driven skill for high-signal code review.

## Install

Install with the skills CLI:

```bash
npx skills add salitaba/code-review-skill
```

`owner/repo` is the form the skills.sh documentation uses. This repository publishes one skill, `code-review`, at the repository root. The explicit equivalent, which selects that skill by name, is:

```bash
npx skills add https://github.com/salitaba/code-review-skill --skill code-review
```

After installation the skill is available to supported coding agents through the standard Agent Skills workflow.

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

The badge above uses the format skills.sh serves —
`https://skills.sh/b/owner/repo`, linking to `https://skills.sh/owner/repo`.
It renders the number of skills skills.sh has indexed for the repository, not an
install count: an indexed repository renders `Skills: 1`, an unindexed one
renders `resource not found`. There is no per-skill badge; `/b/owner/repo/skill`
renders `invalid`.

This repository has no skills.sh index entry yet, so the badge renders
`resource not found` and the link 404s. The repository layout is not the cause —
a skill defined by a root `SKILL.md` is indexed once an entry exists. skills.sh
creates the entry from the anonymous telemetry its CLI reports, so the entry
appears after the skill is first installed through that CLI. Until then, treat
the badge as a placeholder and this GitHub repository as the canonical source.
