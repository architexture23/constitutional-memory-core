# Changelog

## 2026-08-24 — Public truth reconciliation

### Changed

- Replaced the v1.4-only README with an evidence-bounded description of the current architecture.
- Corrected the clone URL to `architexture23/constitutional-memory-core`.
- Removed unverified npm and PyPI installation claims from the quick start.
- Changed whole-system status from an implied operational/completed state to the supported lifecycle state: `VERIFYING`, not `DELIVERED`.
- Clarified the distinction between implemented, verified, closed, and delivered.
- Added public/private publication boundaries and repository security rules.
- Documented the independent public/local Git lineages and the selective-import reconciliation rule.
- Hardened `.gitignore` against credentials, runtime state, private memory, databases, logs, and local worktrees.

### Safety

- Disabled automatic npm/PyPI publishing inherited from the 2025 snapshot.
- Disabled automatic Railway/Vercel production deployment inherited from the 2025 snapshot.
- Both effectful workflows are now manual inert placeholders until their release/deployment authority is explicitly revalidated.

### Historical note

Constitutional Memory v1.4 remains preserved in Git history as the original public snapshot. It is no longer treated as a complete description of the current architecture.
