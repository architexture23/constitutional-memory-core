# Lineage

## Public origin

The public repository began with the November 4, 2025 Constitutional Memory v1.4 snapshot.

## Later implementation lineage

The later local implementation history was initialized independently rather than as a normal descendant of the public `main` branch. Inspection on 2026-08-24 confirmed that the public and local histories do not share a usable common Git ancestor.

That means this project must not pretend a normal fast-forward or cherry-pick lineage exists where it does not.

## Reconciliation rule

The public `main` history is preserved. Newer implementation is imported selectively from identified committed local revisions through explicit path allowlists, with tests and provenance. The private/local history is not force-merged wholesale and the dirty working tree is not used as a release source.

## Historical v1.4

The original v1.4 material remains valid as historical lineage. It is no longer treated as a complete description of the current architecture.

## Provenance expectation

For imported implementation, the repository should record at minimum:

- source revision identity
- imported paths
- verification performed
- public destination revision
- any intentional exclusions or redactions

This preserves continuity without manufacturing Git ancestry that never existed.
