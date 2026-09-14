---
type: llm
weight: 2
---

A successful response reports the duplicate-recording risk with a concrete trigger
and a concrete consequence, and calibrates severity to the evidence.

Required: the response names the condition that produces the duplicate (a
transient failure after a successful write, or an at-least-once redelivery) and
the observable result (duplicate ledger rows, double-counted revenue, or a
reconciliation break).

Required: severity is at least `major`. Duplicate financial records in a ledger
are not a `minor` or `nit`, and a response that files this as a style or
maintainability concern fails.

Fails if the response demands a `blocker` severity while giving no evidence beyond
speculation, since the evidence standard requires severity not to exceed evidence.
