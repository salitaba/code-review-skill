---
type: llm
weight: 3
---

A successful response identifies that replacing `permissions: contents: read` with
`permissions: write-all` at workflow level grants the job far more authority than
it needs.

The response must explain the consequence: every step in the job — including the
third-party `acme/publish-action@v1` and the shell steps — runs with a token that
can write repository contents, releases, and other scopes, so a compromised or
malicious action inherits that authority. Recommending least-privilege scopes
(for example `contents: read` plus the specific write scope the publish step
needs) satisfies this.

A response that mentions the permission change only as a style or consistency
preference, without connecting it to what the token can now do, fails.
