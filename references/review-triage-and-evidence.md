# Review Triage and Evidence

Use this reference when deciding how deeply to inspect a change and whether a concern is strong enough to report.

## Triage the change first

Classify:

- **Risk surface**: user-visible behavior, money/data movement, auth/tenant boundaries, public APIs/events, concurrency, migrations, or operational controls.
- **Change shape**: additive, semantic change, deletion, refactor, dependency/configuration change, or cross-cutting behavior change.
- **Review depth**: broad scan for local low-risk changes; full boundary/lifecycle analysis for high-risk or cross-cutting changes.

Spend the most effort where the change crosses a trust, state, ownership, compatibility, or failure boundary. A small diff can still require a deep review.

## Evidence ladder

Use the strongest available evidence and state which level supports the finding:

1. **Reproduced** — a test, command, trace, or deterministic scenario demonstrates the failure.
2. **Code-proven** — control/data flow and the violated invariant are directly derivable from code and context.
3. **Strongly indicated** — realistic trigger and material impact are clear, but one environmental or contract assumption remains.
4. **Question** — plausible concern that needs context.

Severity must not exceed evidence. A high-impact but weakly evidenced concern should be a focused question, not a blocker.

## Finding gate

Before reporting, answer all of these:

1. What is the smallest trigger?
2. Which boundary is crossed?
3. What invariant or contract is violated?
4. What observable consequence follows?
5. What evidence could prove the concern false?
6. What is the smallest regression test?

If the falsifying evidence is already present, omit the finding. Group multiple symptoms under one root cause.
