# Changelog

## 1.1.2 — 2026-09-21

Focused improvement: strengthen generated-artifact review with artifact identity proof and semantic diff triage.

Added to `references/generated-artifacts-and-codegen-review.md`:
- exact source/toolchain/configuration/output identity checks
- cache reuse and stale-output failure modes
- proof that the tested artifact is the packaged/deployed artifact
- semantic grouping of generated diffs to expose hidden wire, default, validation, auth, and resource changes
- high-signal review questions and evidence requirements

Why:
- The existing playbook correctly identified source-of-truth drift and reproducibility risks, but it did not make artifact identity explicit enough.
- “Generation succeeded” and “the build passed” are weaker claims than proving that the exact generated artifact under test is the one that ships.
- Large generated diffs can hide one incompatible field, unsafe default, or authorization change; semantic triage improves review signal without expanding the core checklist.

Known integration gap:
- `SKILL.md` still needs an explicit generated-artifact/codegen trigger in its executable workflow. The playbook is stronger, but the next pass should wire the trigger and synchronize the skill version as well.

## 1.1.1 — 2026-09-20

Maintenance improvement: synchronize plugin metadata with the generated-artifact/codegen review playbook.

Fixed:
- updated `.claude-plugin/plugin.json` from `1.0.1` to `1.1.1`

Why:
- The repository already contains `references/generated-artifacts-and-codegen-review.md`, but version metadata lagged behind the documented `1.1.0` capability.
- Keeping plugin metadata synchronized prevents agents and tooling from reporting an older skill version than the repository content actually provides.

Known integration gap:
- `SKILL.md` still needs an explicit generated-artifact/codegen trigger in its executable workflow. The next pass should wire that trigger and then synchronize the skill version as well.

## 1.1.0 — 2026-09-18

Focused improvement: add a dedicated generated-artifact and code-generation review playbook.

Added:
- `references/generated-artifacts-and-codegen-review.md`
- source-of-truth and generation-boundary tracing
- checked-in generated-code drift and reproducibility checks
- schema/wire compatibility checks for old/new readers and writers
- generator/toolchain/version and build-artifact identity checks
- generated-code security and resource-safety heuristics
- deterministic generate-and-diff and contract-test guidance

Why:
- The existing skill covered APIs, schemas, delivery chains, and compatibility, but it did not make generator drift and source/generated mismatch a first-class review surface.
- Small generator or template changes can affect many consumers and shipped artifacts, while stale generated output can make local tests pass while CI or production uses something else.
- A focused reference improves review depth without adding another broad checklist to the core workflow.

Integration note:
- The new playbook should be loaded when a change touches generators, schemas, checked-in generated code, SDKs, serializers, templates, or build steps that produce artifacts. The next maintenance pass should wire this trigger into `SKILL.md` so the executable workflow and the reference catalog remain synchronized.

Kept:
- explicit review-decision states
- risk-based review depth
- invariant-ledger reasoning
- mode-and-configuration matrix review
- temporal-correctness review
- data-lifecycle and privacy review
- dependency-and-delivery review
- boundary-focused counterexamples
- producer-and-consumer contract checks
- regression-test validity checks
- rollout/migration/recovery heuristics
- evidence and confidence requirements
- abstraction-leak checks
- negative-space and deleted-safeguard review
- counterexample/falsification before major findings
- self-critique and stopping rule
