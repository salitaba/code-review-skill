# Changelog

## 1.1.4 — 2026-09-22

Focused improvement: add a dedicated failure-containment and degradation review playbook.

Added:
- `references/failure-containment-and-degradation-review.md`
- failure-boundary and degradation-mode analysis
- retry, backoff, breaker, queue, load-shedding, and recovery amplification checks
- partial-success and ambiguous-timeout review heuristics
- blast-radius and isolation checks across tenants, queues, dependencies, and priority classes
- stale/alternate-data safety checks for authorization, pricing, entitlements, and writes
- deterministic fault-injection and recovery-test guidance

Why:
- The executable skill already covered general reliability and retry concerns, but it did not provide a focused method for reviewing graceful degradation and failure containment.
- Fallbacks can preserve availability while silently violating correctness, security, contract, or product semantics.
- A dedicated reference improves depth on outage behavior without bloating the main workflow with a second generic reliability checklist.

Known integration gap:
- `SKILL.md` still needs an explicit failure-containment/degradation trigger in its executable workflow. The playbook is now present and version metadata is synchronized; the next pass should wire the trigger so the reference is guaranteed to load for fallback, breaker, timeout, load-shedding, queue-limit, stale-cache, and partial-success changes.

## 1.1.3 — 2026-09-22

Integration improvement: wire the generated-artifact/codegen playbook into the executable review workflow and synchronize version metadata.

Fixed:
- updated `SKILL.md` from `1.0.1` to `1.1.3`
- added a mandatory generated-artifact/codegen review step when changes touch schemas, generators, templates, SDKs/clients, serializers/parsers, checked-in generated code, or artifact-producing build steps
- added the matching reference-loading trigger for `references/generated-artifacts-and-codegen-review.md`
- synchronized `.claude-plugin/plugin.json` to `1.1.3`
- added generated-output drift, artifact-identity, compatibility, and stale-cache checks to the executable workflow and high-value checks

Why:
- The repository already had a stronger generated-artifact playbook, but the executable skill did not guarantee that it would load when relevant.
- This created a real capability gap: source/generated drift, stale output, and tested-versus-shipped artifact mismatches could be documented but skipped in practice.
- The fix improves execution reliability rather than adding another disconnected checklist.

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
