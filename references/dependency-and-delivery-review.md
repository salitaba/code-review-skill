# Dependency and Delivery Review

Use this reference when a change adds, removes, upgrades, configures, or executes dependencies, build tooling, CI/CD, packaging, containers, infrastructure, or release automation.

## Why this deserves a separate pass

Dependency and delivery changes often have small diffs but high reach. They can alter what code is built, what artifact is shipped, what credentials are trusted, or which environments receive the change. Review the supply chain and delivery behavior, not only application logic.

## Review sequence

1. Identify the effective change.
   - Which package, plugin, image, action, compiler, runtime, lockfile, base image, or deployment step changes?
   - Is the change direct, transitive, generated, or environment-specific?
2. Verify provenance and constraints.
   - Is the source pinned to an immutable version or digest where appropriate?
   - Are integrity checks, lockfiles, signature/provenance checks, and allowed registries still enforced?
   - Does the new dependency introduce a license, support, platform, or transitive-risk constraint?
3. Check build/runtime compatibility.
   - Can old and new artifacts coexist during rollout?
   - Are runtime, OS, architecture, ABI, database-driver, serialization, or protocol assumptions changed?
   - Do development, CI, staging, and production resolve the same effective dependency graph?
4. Check delivery permissions and trust boundaries.
   - Does the change expand workflow permissions, secret access, network egress, artifact publishing, or deployment authority?
   - Can untrusted input influence a build script, workflow command, container entrypoint, or release artifact?
   - Are pull requests from forks, tags, and manual runs handled safely?
5. Check failure and rollback behavior.
   - If the dependency is unavailable, compromised, incompatible, or partially rolled out, what fails?
   - Can the previous artifact be rebuilt and redeployed reproducibly?
   - Are caches, generated files, migrations, and release metadata safe to roll back?
6. Check observability and verification.
   - Is the effective version/digest visible in logs or artifact metadata?
   - Are smoke tests, compatibility tests, vulnerability scans, SBOM/provenance checks, and deployment gates appropriate to the risk?
   - Can operators distinguish dependency failure from application failure?

## High-signal triggers

Flag or investigate when you see:

- floating versions, mutable tags, or unpinned actions/images in a security-sensitive path
- lockfile changes that do not match the declared manifest change
- a package upgrade with changed defaults, transitive dependencies, native code, or serialization behavior
- a CI workflow gaining write permissions, secrets, privileged runners, or unrestricted network access
- build scripts executing repository-controlled data or shell fragments
- a new dependency used only in production but not exercised in CI or staging
- different dependency resolution between local, CI, and production environments
- a release step that is not reproducible or cannot identify the exact artifact deployed
- rollback that restores application code but leaves an incompatible schema, image, cache, or generated artifact

## Evidence standard

Prefer concrete evidence:

- resolved dependency graph or lockfile diff
- workflow permission diff
- image digest or artifact metadata
- reproducible build/deploy command
- compatibility test, smoke test, or failed rollback scenario

Do not report a generic “supply-chain risk” without identifying the changed trust boundary, trigger, and consequence.

## Minimal regression coverage

Choose tests that would fail if the risk returns:

- verify the resolved version/digest and integrity constraints
- run the affected build or workflow with least-privilege permissions
- exercise startup, serialization, protocol, or native-runtime compatibility
- deploy old/new artifacts against the same data and verify rollback/recovery
- verify the release metadata identifies exactly what was built and deployed
