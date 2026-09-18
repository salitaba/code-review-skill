# Changelog

## 1.1.0 — 2026-09-18

Focused improvement: add a dedicated generated-artifact and code-generation review playbook.

Added:
- `references/generated-artifacts-and-codegen-review.md`
- source-of-truth and generation-boundary tracing
- checked-in generated-code drift and reproducibility checks
- schema/wire compatibility checks for old/new readers and writers
- generator/toolchain/version and build-artifact identity checks
- generated-code security and resource-safety heuristics
- deterministic generate-and-diff and contract-test guidance

Why:
- The existing skill covered APIs, schemas, delivery chains, and compatibility, but it did not make generator drift and source/generated mismatch a first-class review surface.
- Small generator or template changes can affect many consumers and shipped artifacts, while stale generated output can make local and CI behavior disagree.
- A focused reference improves review depth without adding another broad checklist to the core workflow.

Integration note:
- The new playbook should be loaded when a change touches generators, schemas, checked-in generated code, SDKs, serializers, templates, or build steps that produce artifacts. The next maintenance pass should wire this trigger into `SKILL.md` so the executable workflow and the reference catalog remain synchronized.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- temporal-correctness review
- data-lifecycle and privacy review
- dependency-and-delivery review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

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
