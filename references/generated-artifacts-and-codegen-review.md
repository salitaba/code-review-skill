# Generated Artifacts and Code Generation Review

Use this playbook when a change touches code generators, schemas, OpenAPI/GraphQL/protobuf/Avro definitions, migrations that emit artifacts, checked-in generated code, SDKs, clients, serializers, parsers, templates, or build steps that produce source/binaries/configuration.

## Why this surface is risky

A small source change can alter many generated files, consumers, wire formats, or shipped artifacts. The inverse is also dangerous: generated output can change without the source-of-truth changing, or stale generated output can make local tests pass while CI or production uses something else.

## Review procedure

1. Identify the source of truth.
   - Determine whether the authoritative input is a schema, template, generator, handwritten source, or external specification.
   - Verify that the changed file is the intended source of truth rather than a derived copy.
2. Trace the generation boundary.
   - Identify when generation runs: local development, CI, packaging, release, startup, or runtime.
   - Check which versions of generators, plugins, runtimes, and templates are actually used.
3. Compare source and generated output.
   - Confirm generated files are reproducible from the committed source and pinned toolchain.
   - Inspect whether the diff contains accidental formatting churn, omitted outputs, or stale files that should have changed.
   - If generated output is checked in, verify the repository policy for regeneration and review both source and output when semantics changed.
4. Check compatibility impact.
   - For schemas and public interfaces, inspect old readers/new writers and new readers/old writers.
   - Check field numbering, enum evolution, defaults, nullability, optionality, unknown-field handling, naming, and serialization precision.
   - Verify that generated clients and servers agree on the same contract and error semantics.
5. Check generated-code safety.
   - Look for unsafe defaults, missing validation, weak auth hooks, insecure deserialization, broad exception handling, or resource-heavy generated paths.
   - Treat generated code as production code: generation does not reduce its security or correctness obligations.
6. Check build and release identity.
   - Ensure CI and release jobs regenerate or validate artifacts consistently.
   - Check that the artifact tested is the artifact packaged and deployed.
   - Look for local-only generation, ignored generated files, cache reuse, or environment-dependent output.
7. Check drift and partial updates.
   - Ask whether a source edit can land without regenerated outputs, or generated outputs can land without the source change.
   - Inspect migration ordering, compatibility windows, and mixed-version rollout behavior.
8. Check tests.
   - Prefer a deterministic generate-and-diff check for checked-in artifacts.
   - Add contract tests across representative old/new versions when wire compatibility matters.
   - Test unknown fields, missing fields, enum additions, malformed input, and large or pathological payloads when relevant.
   - Ensure a regression test fails when generated output is stale or generation is nondeterministic.

## Artifact identity proof

Do not stop at “generation succeeded.” Establish that the artifact under test is the artifact that will ship.

For each generated or packaged output, identify:

- the exact source-of-truth revision
- the generator/plugin/runtime versions
- the relevant configuration and environment inputs
- the output path or artifact digest
- the validation step that compares or signs the result

High-signal evidence includes a deterministic generate-and-diff command, a content digest recorded in CI, or a build step that fails when the workspace is dirty after generation. Treat an artifact as unproven when any of these inputs are implicit, mutable, or supplied only by a developer workstation.

Pay special attention to:

- build caches that can reuse output from a different source revision or toolchain
- generated files copied from a previous workspace rather than regenerated
- release jobs that package a directory different from the one tested
- “best effort” generation that logs a warning and continues with stale output
- environment variables, locale, timezone, filesystem order, or timestamps that make output nondeterministic
- signing or publishing a digest before the final generation/packaging step completes

## Semantic diff triage

When generated output changes, separate noise from behavior:

1. Group changes by semantic effect: wire format, defaults, validation, error mapping, auth, resource use, or naming only.
2. Trace one representative generated change back to the source/template/toolchain input.
3. Confirm that every affected consumer is either regenerated or intentionally compatible with the new output.
4. Reject “regenerate everything” as evidence by itself; large output diffs can hide one incompatible field or unsafe default.
5. If generated output does not change after a source edit, prove that the source is non-semantic or treat the missing output change as drift.

## High-signal heuristics

- A generated diff is not safe merely because it is machine-produced.
- If the generator version changed, review the semantic output changes, not only the toolchain edit.
- If only generated files changed, verify the source-of-truth change exists and can reproduce them.
- If only the source-of-truth changed, verify every required consumer/output was regenerated.
- Treat nondeterministic generation as a correctness and supply-chain risk.
- Treat generated clients as contract consumers; compile success does not prove runtime compatibility.
- A checked-in generated file that is not validated in CI is a drift risk.
- A build that silently falls back to stale generated output is a release risk.
- A cache hit is not proof of correctness unless the cache key includes every semantic input.
- A passing compile does not prove that defaults, validation, error mapping, or authorization semantics are compatible.
- A source/template diff with no corresponding artifact diff needs an explanation, not automatic approval.

## Evidence to prefer

Prefer a reproducible command, generated diff, compatibility test, artifact digest, or exact toolchain/configuration trace. If generation cannot be reproduced, report the limitation explicitly instead of assuming the output is correct.

## Example review questions

- What exact input and toolchain produced this generated file, and can CI reproduce it from a clean checkout?
- Could a stale cache or ignored file make tests exercise different generated code than the release artifact?
- If a schema field became optional, what do old readers, generated clients, validators, and persistence adapters do with omission versus explicit null?
- If only generated output changed, where is the source-of-truth change and how do we know it is not hand-edited drift?
- If the generated diff is large, which small semantic changes alter wire compatibility, defaults, auth, or resource consumption?
