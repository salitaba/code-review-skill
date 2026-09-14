---
type: llm
weight: 2
---

A successful response does not claim that the `Announce release` step exposes,
logs, or leaks credentials.

The step interpolates `github.event.release.name` and
`github.event.release.body`, which are public repository metadata rather than
secrets. The only credential in the file, `secrets.PUBLISH_TOKEN`, is passed to
the `Publish` step through `with:` and is not referenced by the announce step's
shell command.

Fails if the response asserts that a token, secret, or credential reaches the
shell command or the workflow logs, or reports credential exposure as a finding
about this diff.

The response may separately report the untrusted-input interpolation, which is a
different and valid finding; that must not be conflated with credential exposure.
