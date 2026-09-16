# Data Lifecycle and Privacy Review

Load this reference when a change collects, stores, derives, shares, logs, caches, exports, indexes, deletes, or re-identifies personal, confidential, financial, health, tenant, or security-sensitive data.

## Review objective

Verify that the change preserves the intended data lifecycle and does not create hidden copies, ambiguous ownership, excessive retention, unauthorized inference, or unsafe deletion behavior.

## Data-flow questions

- What data enters the system, from which trust boundary, and with what consent or authorization?
- Which fields are copied, transformed, joined, derived, embedded, indexed, cached, logged, exported, or sent to third parties?
- Which downstream systems, jobs, analytics pipelines, backups, replicas, search indexes, and dead-letter queues receive the data?
- Is the data classification still accurate after the transformation? Derived or joined data can be more sensitive than either input alone.

## Purpose and minimization

- Does the change collect or retain fields that are not required for the stated behavior?
- Are identifiers, payloads, and logs scoped to the minimum audience and duration?
- Does a new metric, trace attribute, debug log, or event accidentally carry raw secrets or personal data?
- Does a fallback, replay, or retry path duplicate data beyond the intended purpose?

## Access and isolation

- Is authorization enforced at every new read, export, replay, search, or administrative path?
- Can tenant, user, role, region, or environment boundaries be crossed through joins, caches, shared indexes, or batch jobs?
- Does a service trust a caller-provided subject, tenant, or classification instead of deriving it from an authoritative context?
- Are redaction and masking applied before data reaches less-trusted systems or operators?

## Retention and deletion

- Does the new storage path have an explicit retention owner, TTL, archival policy, and deletion mechanism?
- Does deletion propagate to replicas, caches, search indexes, materialized views, exports, backups, and derived records where required?
- Can a deleted record reappear through replay, eventual consistency, restore, or backfill?
- Does the change preserve legal hold, audit, or recovery requirements without keeping unrelated sensitive payloads indefinitely?

## Security and inference

- Can the new combination of fields enable re-identification, privilege inference, fraud detection bypass, or sensitive classification leakage?
- Are encryption, key scope, secret rotation, and access logging appropriate for the new storage or transport boundary?
- Are error messages, analytics, and model features exposing more than the primary response?
- Is sensitive data copied into client-visible metadata, URLs, filenames, labels, or cache keys?

## Tests and evidence

Prefer tests that prove observable lifecycle properties:

- unauthorized tenant/user access is rejected
- sensitive fields are absent from logs/events/metrics
- retention and TTL boundaries behave as intended
- deletion removes or invalidates all supported copies
- replay, retry, restore, and backfill do not resurrect deleted or over-retained data
- derived outputs preserve the intended classification and access scope

When evidence is missing, report the exact unknown ownership, retention, deletion, or access assumption instead of asserting compliance or non-compliance from naming alone.
