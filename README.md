# Code Review Agent Skill

A living, evidence-driven skill for high-signal code review.

## Goal

Find defects and design risks that matter to users and systems—not merely changed lines or style preferences.

## Evolution

The skill is evolved iteratively. Improvements must be justified by a concrete blind spot, regression/evaluation evidence, or a materially better review heuristic. Changes that only add verbosity are rejected.

## Canonical artifact

- `SKILL.md` — agent-facing skill
- `references/` — deeper review heuristics
- `references/review-triage-and-evidence.md` — risk-based review depth and evidence calibration
- `evals/` — regression cases
- `evolution/` — change history and decisions

## Current improvement

The latest iteration adds risk-based triage and an evidence ladder so the reviewer spends deep effort on trust, state, ownership, compatibility, and failure boundaries, while downgrading weakly evidenced concerns to focused questions instead of overstated blockers.
