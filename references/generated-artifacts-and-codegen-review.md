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

## High-signal heuristics

- A generated diff is not safe merely because it is machine-produced.
- If the generator version changed, review the semantic output changes, not only the toolchain edit.
- If only generated files changed, verify the source-of-truth change exists and can reproduce them.
- If only the source-of-truth changed, verify every required consumer/output was regenerated.
- Treat nondeterministic generation as a correctness and supply-chain risk.
- Treat generated clients as contract consumers; compile success does not prove runtime compatibility.
- A checked-in generated file that is not validated in CI is a drift risk.
- A build that silently falls back to stale generated output is a release risk.

## Evidence to prefer

Prefer a reproducible command, generated diff, compatibility test, or exact toolchain/configuration trace. If generation cannot be reproduced, report the limitation explicitly instead of assuming the output is correct.
