# Review Decision Record

Use this after candidate findings have been validated and before producing the final review.

The goal is not to create bureaucracy. The goal is to make an approval or “no material issue found” conclusion falsifiable and tied to the changed behavior.

## 1. State the decision boundary

Record one of:

- **approve**: no material issue found within the reviewed scope and evidence is sufficient
- **request changes**: one or more actionable findings must be fixed before merge
- **needs context**: a material decision depends on missing contract, rollout, ownership, or domain information
- **limited review**: important surfaces could not be verified; do not imply broad safety

Do not use “approve” when the review was only a syntax/style pass.

## 2. Summarize the changed behavior

In one or two sentences, state:

- what behavior changed
- which users, systems, data, or operators can observe it
- which boundaries were crossed (API, persistence, event, queue, cache, auth, deployment, or domain policy)

This prevents the final conclusion from drifting back to changed-line inspection.

## 3. Record the highest-risk assumptions

List only assumptions that materially affect safety, such as:

- a downstream consumer accepts a new field or status
- a migration runs before new code depends on it
- retries are idempotent at the source of truth
- a feature flag isolates backend behavior, not only UI exposure
- a domain rule is intentionally changed rather than accidentally bypassed

For each assumption, mark it as:

- **verified**: supported by code, tests, configuration, contract, or runtime evidence
- **inferred**: strongly suggested but not directly verified
- **unknown**: requires owner confirmation or environment evidence

If an unknown assumption can cause material harm, use **needs context** or report it as a finding.

## 4. Record the strongest evidence

Prefer evidence in this order:

1. reproduced behavior or failing/passing regression test
2. complete trigger-to-consequence code path
3. producer/consumer or schema contract evidence
4. deployment, migration, or runtime configuration evidence
5. focused owner clarification

Do not treat “tests passed” as proof when the relevant invariant, boundary, or failure mode is not exercised.

## 5. Record residual risk

If approving, state the most important remaining risk in concrete terms:

- what is still unverified
- what would trigger it
- how it would be detected or recovered
- whether it is acceptable for this change

Residual risk should be specific enough that another reviewer could challenge it.

## 6. Approval quality checks

Before finalizing an approval or “no material issue found” conclusion, verify:

- the conclusion matches the actual review scope
- high-reach surfaces received deeper analysis than local mechanical changes
- at least one negative path, boundary case, or failure interleaving was considered where relevant
- important deleted or moved safeguards were checked
- tests are capable of failing on the suspected regression
- unknown assumptions are either resolved, surfaced, or explicitly excluded from the decision

## Suggested final format

```text
Decision: approve | request changes | needs context | limited review

Changed behavior:
- ...

Highest-risk assumptions:
- [verified|inferred|unknown] ...

Evidence:
- ...

Residual risk / review limits:
- ...

Required actions:
- ...
```
