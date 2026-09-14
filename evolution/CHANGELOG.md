# Changelog

## 0.8.1 — 2026-09-14

Focused improvement: report when a fixture cannot measure the skill, and correct a grader that rewarded silence.

Added:
- a `NON-DISCRIMINATING` report in `scripts/eval-summary.py`: when a case scores no better with the skill than without it, the reducer says so and names the case, instead of printing a mean lift that reads as a result
- `evals/no-material-findings/graders/calibration-pii-severity.md` — grades whether the response describes the added log line in terms the fixture supports

Fixed:
- the README badge link now points at `https://skills.sh/owner/repo`, the target the skills.sh documentation pairs with the badge image; the previous link carried a `/code-review` segment that returns a not-found page
- replaced `must-not-flag-pii-exposure.md`, which failed a response that filed the log line as `Minor`, acknowledged the pre-existing `BillingService` occurrence, and declined to escalate. It forbade reporting the line as a new exposure at all, so it penalised the calibrated review and rewarded omitting the item — a precision grader inverted into an incentive against thoroughness.

Removed:
- the unverified claim that a root-level `SKILL.md` is a location skills.sh discovers. The documentation states the badge shows an install count derived from the CLI's telemetry and does not state a repository layout requirement, so the README no longer asserts one.

Why:
- The third eval run reported `mean lift -0.083`. Reading the failed graders showed the cause was this repository's grader, not the skill: the case scored lower with the skill only because the skill did what it should. A suite whose precision graders penalise correct restraint cannot measure the restraint it was built beside.
- The badge resolved to `resource not found` because skills.sh holds no install data for this repository. Only the link target was wrong in the repository; the missing count is upstream and is now documented rather than implied to be fixed.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.8.0 — 2026-09-14

Focused improvement: make the eval suite test restraint as well as recall, and remove the last reference that no workflow step loads.

Added:
- `evals/no-material-findings/` — a case whose correct outcome is approval; it grades the absence of manufactured findings rather than the presence of a defect, and is the only shape of case that can distinguish a disciplined reviewer from an eager one
- a `must-not-flag-credential-exposure` grader on the CI case, restoring the precision coverage lost when an invalid decoy was removed
- a change-shape classification in step 2, covering additive, semantic, deletion, refactor, dependency/configuration, and cross-cutting changes

Removed:
- `references/review-triage-and-evidence.md` — its evidence ladder and finding gate were already in `SKILL.md`, and its triage section was the only distinct part; that part is now the step 2 change-shape line. With no exemptions remaining, `scripts/check-consistency.sh` no longer carries a REDUNDANT allowlist, so the wiring rule is now absolute.

Why:
- The first eval run reported `meanDelta: 0`: the no-plugin arm solved every case, so the suite could not distinguish the skill from no skill. Cases that only reward finding defects cannot measure a skill whose distinguishing claim is knowing when not to report one.
- A decoy that graded a correct finding as a false positive demonstrated that fixture semantics, not author intent, decide whether a grader is valid.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.7.1 — 2026-09-14

Focused improvement: close the reference-integration gap and make reference wiring checkable.

Fixed:
- synchronized the `SKILL.md` version with the latest documented evolution (`0.6.0` → `0.7.1`)
- connected `references/dependency-and-delivery-review.md` to the main workflow with an explicit trigger; 0.7.0 added the reference without any workflow step that loads it
- consolidated load conditions into a single `Reference loading` section instead of leaving them implied by prose
- corrected the stale README reference list and the obsolete "Current improvement" summary
- added the missing plugin manifest, so `claude plugin validate` passes; validation previously failed with no manifest in the directory

Added:
- `.claude-plugin/plugin.json` — makes `claude plugin validate` pass and the repository installable as a plugin alongside `npx skills add`
- `scripts/check-consistency.sh` — fails when a file in `references/` is neither loadable by `SKILL.md` nor declared redundant, or when the declared version disagrees between `SKILL.md`, `.claude-plugin/plugin.json`, and the changelog
- `evals/` — two adversarial review cases with judge-scored graders, and `scripts/eval-summary.py`, which reduces a run to recall, false-positive rate, and lift against the harness's no-plugin baseline arm

Why:
- The same integration gap occurred in 0.5.0 (`review-decision-record.md`) and recurred in 0.7.0 (`dependency-and-delivery-review.md`). Fixing only the second instance would leave the mechanism unfixed.
- A reference that exists but is never loaded is worse than no reference: the repository claims coverage the agent will not apply.
- The check converts a documentation convention into an enforced one, which is what 0.5.1 lacked.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

## 0.7.0 — 2026-09-13

Focused improvement: make dependency, build, CI/CD, packaging, container, infrastructure, and release changes first-class review surfaces.

Added:
- `references/dependency-and-delivery-review.md`
- provenance and pinning checks for packages, actions, images, plugins, and registries
- effective dependency-graph and environment-parity checks
- CI/CD permission, secret, runner, network, and untrusted-input review
- reproducibility, artifact identity, rollback, and partial-delivery checks
- targeted regression coverage for build, startup, compatibility, and release risks

Why:
- Previous versions prioritized application behavior, configuration matrices, rollout safety, and final decision quality, but treated the delivery chain mostly as a generic CI/deploy concern.
- Small dependency or workflow edits can change the artifact that ships, the credentials a build can access, or the environments affected by a release.
- The new reference adds high-signal heuristics without bloating the main workflow with supply-chain-specific detail.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule

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
