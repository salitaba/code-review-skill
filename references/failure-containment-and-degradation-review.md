# Failure Containment and Degradation Review

Use this reference when a change adds or modifies fallbacks, retries, circuit breakers, timeouts, bulkheads, load shedding, queue limits, stale-cache behavior, partial success, dependency failure handling, or user-visible degraded modes.

The goal is to verify that failure handling limits blast radius without silently violating correctness, security, contracts, or product expectations.

## 1. Map the failure boundary

Identify:

- the dependency or resource that can fail
- the caller's timeout and cancellation behavior
- whether the operation is read-only, mutating, or externally visible
- which work may already have completed when the failure is observed
- which callers, tenants, queues, or products share the same resource

A fallback is safe only relative to the operation's semantics. A cached read and a money movement cannot share the same degradation rule.

## 2. Classify the degradation mode

For each failure path, state whether the system:

- fails closed
- fails open
- serves stale data
- returns partial results
- queues for later
- drops work
- retries synchronously or asynchronously
- switches to an alternate dependency

Check that the chosen mode preserves the most important invariant. In particular, do not use availability-oriented fallback for authorization, financial state, uniqueness, or irreversible side effects unless the contract explicitly permits it.

## 3. Check failure amplification

Look for:

- retries multiplied across layers
- synchronized backoff or retry storms
- circuit breakers that open too late, too early, or never recover
- unbounded queues or stale work accumulation
- fallback paths that are more expensive than the primary path
- load shedding that preferentially harms a tenant, role, or critical workflow
- timeout values that exceed upstream deadlines and keep work alive after the caller is gone
- recovery causing a catch-up storm or duplicate execution

Trace the worst-case request rate and resource consumption during both outage and recovery.

## 4. Check partial-success semantics

For multi-step work, determine what happens when some steps succeed and later steps fail:

- Is the result reported as success, failure, partial, or pending?
- Can the caller safely retry?
- Is compensation required?
- Can a timeout hide a committed side effect?
- Is an acknowledgement, event, or status update emitted too early?
- Do downstream consumers understand the new intermediate state?

A response that says "failed" after a side effect committed is a contract defect unless the API explicitly models that uncertainty.

## 5. Check isolation and blast radius

Verify that protection mechanisms isolate failures by the right boundary:

- tenant, user, region, queue, endpoint, dependency, or resource pool
- read versus write traffic
- interactive versus background work
- high-priority versus bulk work

A global breaker or shared thread pool can turn one unhealthy dependency or tenant into a system-wide outage. Conversely, over-isolation can starve recovery or create inconsistent state.

## 6. Check stale and alternate data

When serving cached, replicated, or alternate data, verify:

- maximum staleness and expiry semantics
- whether sensitive or authorization-dependent data can be served from the wrong scope
- whether the result is clearly marked as stale or degraded where users/operators need to know
- whether stale data can trigger writes, entitlements, pricing, or irreversible actions
- whether cache refresh failure causes permanent staleness

Do not treat a cache hit as safe merely because the value has the right type.

## 7. Check observability and recovery

The system should make the degradation visible and actionable:

- distinguish primary success, fallback success, partial success, and uncertain outcome
- expose breaker, queue, drop, timeout, and retry metrics
- preserve the root cause without leaking sensitive details
- alert on sustained degradation and recovery backlog
- define how operators or automated jobs restore normal behavior
- ensure the recovery path is idempotent and does not replay unsafe work

If all degraded outcomes collapse into the same success or error signal, the defect may be operationally invisible.

## 8. Check tests and evidence

Prefer tests that prove:

- dependency timeout and cancellation behavior
- retry count and backoff bounds
- breaker open/half-open/close transitions
- queue saturation and load shedding
- partial success and ambiguous timeout outcomes
- stale-data limits and scope isolation
- recovery after dependency restoration or process restart
- no fail-open authorization or data-integrity bypass

Use deterministic fault injection and controllable time rather than long sleeps or flaky network simulations.

## Review questions

- What is the exact user-visible and system-visible behavior when the dependency fails?
- Which invariant must never be weakened by the fallback?
- Can a timeout race with a committed side effect?
- Can retries or recovery multiply work across layers?
- Is the blast radius bounded to the intended tenant, resource, or workflow?
- Can stale or alternate data influence a write, permission, price, or entitlement?
- How will operators distinguish degraded success from normal success?
- What evidence proves the recovery path is safe?
