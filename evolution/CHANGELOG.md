# Changelog

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
