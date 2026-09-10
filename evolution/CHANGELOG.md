# Changelog

## 0.5.0 — 2026-09-10

Focused improvement: make review conclusions explicit, falsifiable, and proportional to the evidence and scope actually covered.

Added:
- `references/review-decision-record.md`
- explicit decision states: approve, request changes, needs context, and limited review
- changed-behavior summary requirements for the final decision
- verification status for high-risk assumptions: verified, inferred, or unknown
- residual-risk and review-limit recording for approvals and no-material-issue conclusions
- approval-quality checks covering scope, negative paths, deleted safeguards, regression-test strength, and unresolved assumptions

Why:
- Previous versions were strong at candidate-finding and falsification, but could still produce an overconfident “LGTM” when the review scope or assumptions were incomplete.
- The new framework improves decision quality without adding another broad checklist to the main skill.

Kept:
- risk-based review depth
- invariant-ledger reasoning
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.4.0 — 2026-09-09

Focused improvement: make review depth proportional to blast radius and make removed safeguards visible during diff review.

Added:
- a pre-review risk map using reach and failure cost to prioritize deep analysis
- explicit guidance that small changes in high-reach surfaces can outrank large local refactors
- a negative-space pass for deleted validation, authorization, tests, telemetry, limits, cleanup, retries, and rollback hooks
- stronger review of safeguard equivalence when protections move rather than disappear

Kept:
- invariant-ledger reasoning
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.3.0 — 2026-09-08

Focused improvement: make reviewers reason from explicit invariants and prove that tests would catch the suspected regression.

Added:
- an invariant-ledger pass covering preconditions, postconditions, ownership, uniqueness, authorization, and state transitions
- boundary-focused counterexamples instead of happy-path-only reasoning
- explicit producer-and-consumer contract checks at integration boundaries
- a regression-test validity check requiring the new test to fail on the old behavior
- restart/recovery and observability-error-collapsing checks for distributed systems

Kept:
- high signal over exhaustive comment count
- changed behavior over changed lines
- evidence and confidence requirements
- abstraction-leak checks
- rollout/migration/rollback heuristics
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.2.0 — 2026-09-08

Focused improvement: make reviews more sensitive to behavior changes that are easy to miss in diffs and to operational failures during rollout.

Added:
- explicit old-versus-new differential behavior pass
- first-class treatment of deletions, default changes, reordered operations, and narrowed conditions
- rollout, mixed-version, migration, rollback, feature-flag, and recovery heuristics
- evidence ladder prioritizing reproductions and complete code-path proofs
- regression-test expectations for rollout and migration risks

Kept:
- high signal over exhaustive comment count
- changed behavior over changed lines
- evidence and confidence requirements
- abstraction-leak checks
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.1.0 — 2026-09-06

Initialized the repository as the canonical home for the Code Review agent skill.

Initial principles:
- high signal over exhaustive comment count
- review changed behavior, not only changed lines
- evidence and confidence required for substantive findings
- explicit abstraction-leak checks
- correctness, concurrency, contracts, security, performance, testing, architecture, and domain risk
- counterexample/falsification before reporting major findings
- regression-test guidance for findings
