# Temporal Correctness Review

Use this reference when a change touches time, expiry, scheduling, retries, delayed work, leases, caches, event ordering, timestamps, or clock-dependent behavior.

## Why this deserves a dedicated pass

Many defects are not value errors; they are ordering errors. The code is correct for one instant, but wrong when clocks differ, work is delayed, retries arrive late, or a process restarts between two time-sensitive steps.

## Review heuristics

### Clock and timestamp semantics

- Identify the clock source: wall clock, monotonic clock, database time, event time, or client-supplied time.
- Check whether the chosen clock is appropriate for the comparison. Use monotonic time for elapsed-duration measurement; do not infer elapsed time from wall-clock timestamps when clock adjustments are possible.
- Check timezone, daylight-saving, calendar, and precision assumptions at every serialization boundary.
- Verify whether timestamps represent occurrence time, processing time, expiry time, or last-observed time. Similar names can hide different meanings.

### Expiry, TTL, and leases

- Ask what happens exactly at the boundary: before expiry, at expiry, after expiry, and when the stored expiry is missing or malformed.
- Check whether a lease can expire while work is still running and whether completion after expiry is rejected, ignored, or incorrectly committed.
- Inspect renewal, cancellation, and cleanup races. A late renewal must not resurrect already-invalid state unless that is explicitly intended.
- Verify that cache TTL, database expiry, token expiry, and business validity are not being conflated.

### Scheduling and delayed execution

- Check whether delayed work is durable across restart, deployment, failover, and clock changes.
- Verify that “run at” semantics define what happens when the scheduler is down, the target time is missed, or multiple workers claim the same item.
- Check for duplicate execution, skipped execution, and catch-up storms after an outage.
- Inspect boundary rounding and truncation: seconds versus milliseconds, local midnight versus UTC midnight, inclusive versus exclusive windows.

### Retries, ordering, and late events

- Model a late retry, duplicate delivery, out-of-order event, and response that arrives after a timeout.
- Check whether newer state can be overwritten by an older message because ordering is assumed rather than enforced.
- Verify idempotency keys, sequence numbers, version checks, or compare-and-set protections where temporal ordering matters.
- Ensure timeout handling does not turn an in-flight successful operation into a second conflicting operation.

### Tests and evidence

Prefer tests that use an injectable or controllable clock and explicitly cover:

- exact boundary instants
- clock skew or time adjustment
- restart between scheduling and execution
- lease expiry during work
- duplicate, late, and out-of-order delivery
- daylight-saving or timezone transitions when user-visible dates are involved

A test that sleeps for real time is weak evidence unless the timing itself is the behavior under test. Prefer deterministic time advancement and explicit event ordering.

## Finding standard

Report a temporal defect only when you can state:

1. the clock or ordering assumption,
2. the smallest trigger or interleaving,
3. the invariant or contract that fails,
4. the observable consequence, and
5. the smallest safe correction or focused question.
