# Reconciliation Contract

**Started:** 2026-08-24

The public repository was materially behind the working architecture. Reconciliation is being performed as a controlled public projection rather than a wholesale merge of the private/local workspace.

## Completed in this reconciliation

- replaced the stale v1.4-only README framing with the current lifecycle boundary
- corrected the repository clone URL
- removed unverified npm/PyPI quick-start claims from the README
- established `CURRENT_STATE.md`
- established `SECURITY.md`
- established `PUBLICATION_BOUNDARY.md`
- established `LINEAGE.md`
- disabled inherited automatic production deployment and package publishing pending revalidation

## Implementation import contract

Verified implementation is imported only when all of the following hold:

1. the source is an identified committed revision;
2. the public file set is explicitly allowlisted;
3. secrets/private-state review is clean;
4. relevant tests pass from a clean checkout;
5. the imported artifact does not overstate its lifecycle status;
6. provenance is recorded.

## Explicitly rejected shortcuts

- force-merging unrelated public/local histories
- publishing the dirty local working tree
- `git add .` from the private workspace
- treating branch names or staged artifacts as verification
- preserving effectful 2025 deployment/release workflows merely because they existed

The goal is not to make GitHub look newer. The goal is to make GitHub tell the truth.
