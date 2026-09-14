---
type: llm
weight: 3
---

A successful response identifies that untrusted release data is interpolated
directly into a shell command.

The `Announce release` step embeds `${{ github.event.release.name }}` and
`${{ github.event.release.body }}` into a `run:` block. These are attacker-
influenceable strings. Because GitHub substitutes them into the script before the
shell runs, content such as `"; curl … | sh; echo "` executes as shell commands in
a job that now holds `write-all`.

Naming script/command injection, untrusted input, or expression interpolation as
the defect satisfies this, as does recommending `env:` indirection with quoted
`"$VAR"` usage.

Fails if the response treats the change as only a formatting or logging concern.
