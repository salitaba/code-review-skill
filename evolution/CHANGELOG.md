# Changelog

## 0.6.0 — 2026-09-12

Focused improvement: make configuration-, feature-flag-, role-, tenant-, version-, and deployment-dependent behavior explicit during review.

Added:
- a mode-and-configuration matrix step before deep reading
- pairwise/risk-based guidance instead of blind Cartesian-product testing
- checks for missing, invalid, stale, or default configuration values
- explicit review of semantic changes that appear only in non-default modes
- rollout-risk checks for flags/configuration that change backend behavior without telemetry, rollback, or migration handling
- test guidance for high-risk matrix cells rather than default-only coverage

Why:
- Previous versions were strong on invariants, deleted safeguards, rollout safety, and decision quality, but could still miss bugs that occur only for a non-default flag, role, tenant, API version, or mixed deployment.
- This is a common source of authorization, compatibility, pricing/entitlement, routing, and data-interpretation defects.
- The new step improves coverage of interaction risks without requiring exhaustive testing of every possible configuration combination.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.5.1 — 2026-09-11

Focused improvement: close an integration gap in the previous evolution and make the final review decision part of the mandatory agent workflow.

Fixed:
- synchronized the `SKILL.md` version with the latest documented evolution
- connected `references/review-decision-record.md` to the main review workflow instead of leaving it as an optional standalone reference
- required explicit decision, residual-risk, and review-limit output when concluding a review

Why:
- Version 0.5.0 documented a decision-record framework, but the agent-facing skill still declared version 0.4.0 and did not explicitly require using the new reference.
- This created a real maintenance and behavior gap: the repository could claim stronger approval discipline than the skill would consistently apply.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

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
- self-critique and stopping rule
