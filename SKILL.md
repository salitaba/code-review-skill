---
name: code-review
version: 0.3.0
description: Perform high-signal code reviews for correctness, security, concurrency, reliability, architecture, maintainability, testing, API contracts, performance, and product/domain risks. Use when reviewing a pull request, diff, patch, commit, or code change; prioritize user/system impact over style and require evidence before reporting findings.
---

# Code Review

## Mission

Find issues that can cause incorrect behavior, security exposure, data loss/corruption, concurrency failures, reliability problems, broken contracts, harmful product behavior, or disproportionate future maintenance cost.

Optimize for **signal over coverage**. Do not manufacture findings to make the review look comprehensive.

## Core rule

Review **changed behavior, not merely changed lines**.

A change can alter behavior through callers, downstream consumers, transaction/retry boundaries, persistence, schemas/migrations, events, caches, authorization, observability, configuration, external APIs, or domain invariants even when those files are unchanged.

## Review workflow

1. Establish intent and acceptance criteria.
   - Read the PR description, issue, tests, API/schema changes, and relevant surrounding code.
   - If intent is unavailable, state the assumption that constrains the review.
2. Build a change map.
   - Identify changed components, callers, dependencies, data flows, state transitions, and boundaries.
   - Follow important inputs to side effects and outputs to consumers.
3. Build an invariant ledger.
   - Write down the key preconditions, postconditions, ownership rules, uniqueness constraints, authorization rules, and state-transition rules that must remain true.
   - For each changed path, mark which invariant it establishes, preserves, weakens, or silently bypasses.
   - Treat an invariant that exists only in comments or caller discipline as a review risk.
4. Compare old versus new behavior.
   - For each meaningful branch, default, error path, and state transition, ask what was true before, what is true now, and whether the difference is intentional.
   - Treat deletions, default changes, reordered operations, and narrowed conditions as first-class behavior changes.
5. Check correctness and invariants.
   - Normal path, boundary values, empty/null/error cases, retries, partial failure, ordering, idempotency, and state transitions.
   - Look for violated preconditions/postconditions and duplicated or conflicting business rules.
   - Test the smallest counterexample at each changed boundary instead of relying on the happy path.
6. Check concurrency and lifecycle.
   - Shared mutable state, races, lost updates, locking, transaction scope, isolation, async execution, duplicate delivery, retries, timeouts, cancellation, TTL/lease expiry, and resource ownership.
   - Ask whether a second actor, delayed message, retry, timeout, or restart can interleave between the check and the side effect.
7. Check contracts and integration boundaries.
   - API compatibility, serialization, schema evolution, event contracts, versioning, authentication/authorization, tenant isolation, and backward/forward compatibility.
   - Inspect both producers and consumers; a locally valid change can still violate a downstream assumption.
8. Check rollout, migration, and recovery safety.
   - Consider mixed-version deployments, feature flags, retries during rollout, backward-compatible database changes, expand/contract sequencing, rollback feasibility, and recovery after partial deployment.
   - A change is not operationally safe merely because the steady-state code path is correct.
9. Check architecture and abstraction boundaries.
   - Dependency direction, ownership, coupling, hidden policy, lifecycle leakage, duplicated orchestration, and abstractions that permit type-correct but semantically invalid use.
10. Check security, performance, and operability when relevant.
   - Trust boundaries, input handling, secrets, privilege, injection, denial-of-service risks, query amplification, hot paths, resource growth, metrics/logging/tracing, recovery, and alertability.
   - Verify that important failures remain distinguishable in telemetry; collapsed errors can make a defect operationally invisible.
11. Check tests.
   - Prefer tests that prove observable behavior and invariants.
   - Look for missing negative paths, concurrency/retry cases, contract tests, migration coverage, rollout/rollback coverage, and assertions that merely verify mocks/interactions.
   - Confirm new tests would fail on the suspected regression; a test that passes both before and after the change is not a regression test.
12. Validate findings.
   - For every candidate issue, identify the smallest trigger and trace the affected behavior.
   - Try to falsify it with a concrete counterexample.
   - Prefer a reproducer, failing test, executable query, or precise code-path proof over intuition.
13. Self-critique and stop.
   - Remove duplicates and style-only comments.
   - Downgrade unsupported certainty.
   - Stop when meaningful coverage is complete; do not keep searching solely to increase finding count.

## Finding standard

Report a finding only when it is actionable and supported by evidence.

Each substantive finding should contain:

- **Severity**: blocker / major / minor / nit
- **Confidence**: confirmed / strongly likely / needs context
- **Evidence**: exact file/line, behavior trace, test result, or reproducible trigger
- **Failure**: what can go wrong and under what condition
- **Impact**: user, data, security, reliability, performance, or maintenance consequence
- **Fix**: smallest safe correction or concrete investigation
- **Regression test**: the smallest test that would prevent recurrence

### Evidence ladder

Prefer the strongest available evidence:

1. Reproduced failure, failing test, or deterministic command output.
2. Code-proven behavior with a complete path from trigger to consequence.
3. Strong indication supported by surrounding code, contract, or invariant.
4. Focused question when the concern depends on missing context.

Never use high-severity wording for a low-confidence observation. If evidence is insufficient, ask a focused question or omit the finding.

## Severity guidance

### Blocker
Likely to cause severe correctness, security, data-integrity, concurrency, reliability, contract, rollout, or critical product failure. Requires resolution before approval.

### Major
Meaningful defect or architectural/operational risk with a realistic trigger and material impact. Usually should be fixed before merge.

### Minor
Real but bounded issue with limited impact or a meaningful maintainability/testability concern.

### Nit
Preference or polish that does not materially affect behavior or maintainability. Prefer omission unless explicitly requested.

## Abstraction-leak test

Do not call something an abstraction leak merely because an abstraction is imperfect.

Flag it when the abstraction claims to hide a concept but callers still need to understand or duplicate its:

- policy or business invariant
- lifecycle or transaction boundary
- ownership/resource responsibility
- failure/retry semantics
- ordering/concurrency requirements
- representation details required for correct use

Strong evidence includes APIs that are easy to misuse while remaining type-correct, repeated validation/orchestration across callers, or callers depending on internal lifecycle details.

## Counterexample discipline

For each major candidate finding ask:

1. What is the smallest input/state/concurrency schedule that triggers it?
2. Which boundary does it cross?
3. What invariant or contract is violated?
4. What observable consequence follows?
5. What evidence could prove the concern false?

If the fifth question has an obvious answer and that evidence is present, do not report the finding.

## Rollout and migration heuristics

Pay special attention when a change affects persisted data, public contracts, or distributed deployment:

- Can old and new versions read/write the same data safely during rollout?
- Does a new writer require an old reader to understand a field, enum, event, or status?
- Is the database migration additive before code depends on it?
- Can rollback restore code without corrupting data or making old code crash?
- Are retries, duplicate deliveries, and partially completed migrations safe?
- Is a feature flag actually isolating risk, or only hiding the UI while backend behavior changes globally?
- Are observability and recovery signals present before enabling the risky path?

## Common high-value checks

### Correctness
- off-by-one and boundary errors
- null/empty/default semantics
- incorrect state transitions
- stale reads and lost updates
- partial success treated as full success
- error paths that accidentally commit, acknowledge, or discard work
- deletion or default changes that silently alter existing behavior
- invariants enforced in one path but bypassed in another
- tests that do not distinguish the old bug from the fixed behavior

### Concurrency
- check-then-act races
- lock scope too narrow or too broad
- transaction boundary mismatches
- duplicate processing after retry/redelivery
- idempotency assumptions not enforced at the source of truth
- TTL/lease expiry during work
- async work outliving request/transaction context
- restart/recovery paths that replay or lose in-flight work

### API/contracts
- breaking changes hidden behind compatible types
- changed defaults or semantics
- enum/status evolution
- serialization/nullability changes
- event/schema compatibility
- authentication/authorization behavior changes
- downstream consumers that infer meaning from ordering, omission, or error codes

### Security
- trust-boundary changes
- authorization performed before/after the wrong transformation
- tenant/user scope confusion
- injection or unsafe deserialization
- secret exposure
- sensitive data in logs/errors
- resource-exhaustion paths
- fail-open behavior after timeout, cache miss, or dependency failure

### Performance/reliability
- N+1 and accidental fan-out
- unbounded memory/queue/cache growth
- expensive work inside locks/transactions
- retry amplification
- missing timeouts/cancellation
- synchronous dependencies on failure-critical paths
- observability gaps that make failures unrecoverable
- error collapsing that prevents safe retry, alerting, or diagnosis

### Testing
- happy-path-only coverage
- assertions that prove mocks rather than outcomes
- tests coupled to implementation details
- missing regression test for the actual invariant
- missing concurrency/retry/contract/migration/rollback tests where those are the risk
- fixtures that omit the boundary condition needed to trigger the bug
- tests that cannot fail independently when the behavior regresses

## AI-generated-code checks

When code appears generated or heavily copied, inspect rather than assume it is wrong. High-value signals include:

- swallowed exceptions or fake fallbacks
- comments claiming guarantees the implementation does not provide
- tests that assert mocks instead of behavior
- duplicated business logic copied across layers
- unnecessary dependencies or abstractions
- happy-path-only implementation
- hardcoded fixtures or constants presented as general logic
- local conventions violated by copied patterns

## Scope discipline

Distinguish:

- **caused**: the change introduces the defect
- **exposed**: the change makes an existing defect reachable or materially worse
- **adjacent**: real issue, but unrelated to the change

Do not turn adjacent cleanup into a blocker unless it is required for the changed behavior to be safe.

## Review output

Order findings by severity, then confidence and user impact.

Prefer a small number of strong findings over a long checklist. For each finding, explain the trigger and consequence before proposing the fix.

Finish with:

- overall risk assessment
- important areas reviewed with no material issue found, when useful
- rollout/migration assumptions or required deployment sequencing, when relevant
- required changes before approval
- optional improvements only if they are genuinely valuable

Do not report style preferences unless they encode a real correctness, maintainability, or consistency risk.
