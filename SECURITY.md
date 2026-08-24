# Security Policy

## Public-repository rule

This repository is a curated public projection of a larger working architecture. Private runtime material must not be published merely because it is present in a local workspace.

## Never commit

- API keys, passwords, access tokens, session cookies, OAuth material, private keys, or recovery codes
- `.env` files or equivalent secret stores
- private account identifiers or personal data
- private conversation exports, personal memory stores, or unredacted user records
- runtime databases, machine-local state, generated execution logs, or cached receipts containing private data
- trading credentials, brokerage/account secrets, or private execution records
- browser profiles, login state, or automation credentials
- virtual environments, caches, backups, recovery archives, or machine-specific credential files

## Publication gate

Before importing implementation from a private/local lineage into this repository:

1. Source from a committed, identified revision rather than an arbitrary dirty working tree.
2. Use an explicit allowlist of files/directories to publish.
3. Review the staged diff for secrets and private data.
4. Run the relevant tests from a clean checkout.
5. Preserve provenance for imported implementation.
6. Do not promote staged or `PREPARED` artifacts to verified status without evidence.

## Release and deployment authority

Automated production deployment and package publishing are disabled unless the current release path has been explicitly revalidated. Historical workflow files do not inherit authority simply because they exist.

## Vulnerability reporting

Do not place credentials or exploitable secret material in a public issue. Use GitHub's private security-reporting mechanisms when available, or disclose only the minimum non-sensitive information necessary to establish contact.
