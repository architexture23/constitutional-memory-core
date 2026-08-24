# Publication Boundary

This repository is not a byte-for-byte mirror of the private working workspace.

## Publishable by default

- architecture laws, contracts, and public-safe design documentation
- implementation needed to demonstrate the public architecture
- deterministic tests and verification harnesses
- sanitized evidence, receipts, and provenance records
- changelog and lineage documentation

## Excluded by default

- credentials and authentication material
- personal/private memory stores or conversation archives
- runtime state, databases, logs, caches, and generated receipts containing private context
- machine-specific configuration that exposes local secrets or account details
- trading/private financial execution data
- unrelated experiments and product trees
- backups, virtual environments, recovery archives, large generated assets, and transient files

## Import rule

Newer implementation may be imported from the private/local lineage only from an identified committed revision and only through an explicit path allowlist. The dirty root working tree is not a publication source.

## Truth rule

Public claims follow this order:

`evidence > verified implementation > implemented/staged material > plans > historical claims`

A newer-looking filename or branch never outranks stronger verification evidence.
