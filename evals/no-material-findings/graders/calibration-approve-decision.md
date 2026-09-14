---
type: llm
weight: 3
---

A successful response concludes with an explicit decision to approve, or to
approve with optional nits.

The change is purely additive and does not alter existing behavior, so
`request changes` is not supported by the reviewed scope. The skill's stated
standard is that `approve` means the reviewed scope and evidence support it, and
they do here.

Fails if the final decision is `request changes` or a blocker.

A decision of `needs context` is acceptable only when the response names the
specific missing artifact it requires and does not pair that with a blocker or
major finding. A vague `needs context` that rests on unstated doubt fails.
