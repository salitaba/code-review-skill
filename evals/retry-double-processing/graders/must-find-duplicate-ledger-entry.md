---
type: llm
weight: 3
---

A successful response identifies that retrying a non-idempotent write can record
the same payment more than once.

The response must connect the retry to duplicate ledger entries — that a transient
failure whose write actually succeeded, or a broker redelivery of the same
`OrderPaid` event, produces a second `LedgerEntry` for one order. Naming
idempotency or a dedupe key as the missing guard satisfies this.

A response that only says "consider idempotency" without tying it to this code
path, or that never raises duplicate recording at all, fails this grader.
