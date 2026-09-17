# Changelog

## 1.0.1 — 2026-09-18

Focused improvement: wire the data-lifecycle and privacy playbook into the executable review workflow.

Fixed:
- synchronized `SKILL.md` to version `1.0.1`
- added an explicit data-lifecycle/privacy review step
- added the new reference trigger to `Reference loading`
- added data-copy, deletion, redaction, replay, restore, and derived-data checks to the high-value review guidance

Why:
- Version 1.0.0 added `references/data-lifecycle-and-privacy-review.md`, but `SKILL.md` remained at 0.9.1 and did not require the agent to load the reference.
- The repository therefore documented a useful privacy/data-lifecycle capability that the executable workflow could silently skip.
- This change fixes the integration mechanism rather than adding another disconnected checklist.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- temporal-correctness review
- data-lifecycle and privacy review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 1.0.0 — 2026-09-17

Focused improvement: add a dedicated data-lifecycle and privacy review surface.

Added:
- `references/data-lifecycle-and-privacy-review.md`
- data-flow and trust-boundary tracing for collected, copied, derived, logged, cached, indexed, exported, and deleted data
- purpose limitation and minimization checks
- tenant/user/role/region isolation checks across joins, caches, indexes, replays, and batch jobs
- retention, TTL, deletion propagation, restore, replay, and backfill heuristics
- inference and re-identification checks for joined or derived data
- tests for redaction, unauthorized access, deletion propagation, and resurrection through retry/restore paths

Why:
- Previous versions covered security, contracts, rollout, observability, and temporal behavior, but data lifecycle risks were still scattered across those categories.
- Privacy and confidentiality failures often come from secondary copies and derived paths—logs, traces, caches, search indexes, dead-letter queues, exports, backups, and replays—rather than the primary request path.
- A focused reference improves review depth without turning the core skill into another exhaustive checklist.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- temporal-correctness review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.9.1 — 2026-09-16

Focused improvement: close the temporal-reference integration gap and synchronize the executable skill and plugin metadata.

Fixed:
- connected `references/temporal-correctness-review.md` to the mandatory review workflow with an explicit trigger
- synchronized `SKILL.md` and `.claude-plugin/plugin.json` to version `0.9.1`
- added temporal correctness to the high-value review checks for correctness, contracts, concurrency, reliability, and testing

Why:
- Version 0.9.0 added a valuable temporal-correctness reference, but the main skill did not require loading it. The repository therefore documented coverage that an agent could silently skip.
- The version metadata also lagged behind the documented evolution, creating an install/runtime inconsistency.
- This change fixes the mechanism rather than merely adding more heuristics: triggered references are now wired into the executable workflow and metadata is consistent.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- temporal-correctness review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.9.0 — 2026-09-15

Focused improvement: make temporal correctness a first-class review surface.

Added:
- `references/temporal-correctness-review.md`
- clock-source and timestamp-semantics checks
- expiry, TTL, lease, scheduling, restart, retry, late-event, and out-of-order delivery heuristics
- deterministic-clock and exact-boundary testing guidance

Why:
- Previous versions mentioned TTLs, leases, retries, and delayed work, but those checks were scattered across concurrency and reliability guidance.
- Temporal defects often appear only at exact boundaries, after restart, under clock adjustment, or when delayed work arrives.
