# Evaluation suite

Adversarial cases for the `code-review` skill, run with Claude Code's first-party
eval harness. The point of this directory is to replace "the review reasoning
looks good" with a number.

## Running

```bash
claude plugin eval . --no-publish --max-cost-usd 2
```

- `--no-publish` keeps the HTML report local instead of publishing it.
- `--max-cost-usd` is a hard ceiling; the run aborts with exit 2 if hit.
- Exit codes: `0` at/above threshold, `1` below or load error, `2` partial.
- `--ablation none` skips the baseline arm when you only want the with-skill score.
- `--case '<glob>'` runs a subset while iterating.

Targeting `.` resolves this repo as a skill folder, which is what enables the
`with-without` ablation arm — the comparison that makes the suite a benchmark
rather than a spot check.

## Case format

Each case is `evals/<case>/prompt.md` plus one or more `evals/<case>/graders/*.md`.
Markdown bodies, YAML frontmatter. Scaffold a blank template with:

```bash
claude plugin eval init <name> --bare
```

`prompt.md` frontmatter may set `runs`, `max_turns`, `timeout_seconds`,
`allowed_tools`, `model`, `tags`, and `append_system_prompt`.

Graders declare `type` and `weight`. `type: llm` graders describe what a
successful response looks like and are scored by a judge model (default haiku;
override with `--judge-model`).

## What these cases measure

Review quality has two failure directions, and a recall-only suite rewards the
worse one — a reviewer that flags everything finds every seeded bug. So every
case here carries both:

- **Recalled defect** — a seeded, real defect the review must find.
- **Decoy** — a plausible concern that is *wrong given the context supplied*.
  A grader passes only when the review declines to report it.

Decoys are resolved by context on purpose. Each one tests a specific claim the
skill makes: that severity must not exceed evidence, that a concern should be
dropped when falsifying evidence is already present, and that a removed
safeguard must be checked for relocation rather than assumed lost.

A case may also be **precision-only**, with no `must-find` grader at all. Some
changes are genuinely clean and the correct review is approval, and that is the
only shape of case that can test whether a reviewer manufactures findings to look
thorough. The reducer prints `n/a` for a recall column with no graders rather
than a misleading zero.

## Fixture validity

A decoy is a claim about the code, so it must be true of the code as written —
not of what the fixture's author meant. The first CI case shipped with a decoy
asserting that a deleted artifact-upload step had merely relocated to another
workflow. It had not: `actions/download-artifact@v4` reads artifacts from its own
workflow run and needs an explicit `run-id` and token to read another's, so the
consumer could never have received the producer's output. Both arms correctly
reported the deletion as a break, and the decoy graded a right answer as wrong.

That case now grades the producer/consumer break as a must-find, which is what it
always was. Before adding a decoy, confirm the finding it forbids is actually
false given the fixture's semantics. A decoy that encodes intent rather than
behavior penalises correct reviews and makes the precision numbers meaningless.

## Scoring and the known gap

The harness reports per-grader verdicts in
`evals/results/<timestamp>/aggregate-result.json`, with `cases[].arms.with[]` and
`arms.without[]`. It does **not** aggregate precision/recall. To state a
benchmark claim, reduce the JSON to:

```
recall              = must-find graders passed / must-find graders total   (with arm)
false-positive rate = must-not-flag graders failed / must-not-flag total   (with arm)
severity accuracy   = calibration graders passed / calibration total       (with arm)
lift                = with-arm score − without-arm score
```

Writing the reducer is the next step; until it exists, read the numbers off
`aggregate-result.json` by hand rather than quoting a summary that is not
computed anywhere.

## Fidelity limits

Stated plainly, because a suite that overstates what it proves is worse than none:

- Cases embed the relevant code inline instead of scaffolding a repository, so
  the reviewer cannot follow callers or search for consumers. The skill's central
  claim — review changed behavior, not changed lines — is therefore
  **under-tested** here. Testing it needs `scaffold_script`, which this suite
  does not yet use.
- `runs: 1` is set on the current cases to bound cost, which means results carry
  model variance. Raise `runs` before drawing conclusions from small deltas.
- Judge-scored graders are themselves a model. A grader that passes is evidence,
  not proof.
