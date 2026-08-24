# Constitutional Memory Core

Constitutional Memory Core is an evolving architecture for durable AI-agent memory, governed execution, recovery, verification, and continuity across sessions and tools.

> **Public status (2026-08-24): `VERIFYING` — not `DELIVERED`.**

This repository began as the public **Constitutional Memory v1.4** snapshot in November 2025. The working architecture has since expanded substantially. The public repository is now reconciled to that newer reality with an evidence-first rule: **published claims must be bounded by actual verification, and private runtime state is never dumped into GitHub just to make the repository look current.**

## What changed

The original v1.4 README described a fixed package around 13 Drops, 7 patterns, and 8 MCP tools. Those artifacts remain part of the project's lineage, but they are no longer an accurate description of the whole system.

The current architecture includes layers for:

- durable memory and constitutional rules
- objective preservation and recovery
- `ACTIVE_WORK`-backed persistent execution
- execution routing across available tools and transports
- explicit authority and ownership boundaries
- verification, receipts, and operative-truth gates
- failure recovery without silently converting a blocked mechanism into a failed objective
- multi-machine / specialist-node coordination

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the current public architecture map and [`AGENTS.md`](AGENTS.md) for the repository execution contract.

## Current verified state

The public truth model distinguishes **verified subsystem closure** from **whole-system delivery**.

- **Quota Failover Supervisor v0.1:** closed and verified.
- **Task 5 runtime work:** closed and verified.
- **Task 6 `ACTIVE_WORK` integration:** closed and verified.
- **Overall organism lifecycle:** `VERIFYING`.
- **Task 7:** not part of the verified public state.
- **Delivery status:** not declared.

These status claims describe the verified working architecture. They do **not** imply that every newer private/local implementation file has already been published here. Implementation publication is selective and must pass the public boundary before import.

See [`CURRENT_STATE.md`](CURRENT_STATE.md) for the public status contract.

## Core operating laws

### Preserve the objective; recompose the path

A preferred route failing does not make the objective impossible. The system should inspect eligible alternatives, substitute when necessary, and preserve the requested observable outcome.

### Function > substrate

Capabilities are defined by the function and evidence they provide, not by one specific host, UI, model, or connector.

### Evidence before completion

A prompt, queued artifact, model confidence, or implementation claim is not completion evidence. Completion requires observable verification appropriate to the work.

### One owner per mutable resource

Execution may be federated, but mutation authority must stay explicit to avoid competing writers and false state.

## Repository boundary

This repository is a **public projection**, not a raw mirror of the private runtime workspace.

Public material may include:

- architecture contracts and laws
- sanitized implementation code
- tests and deterministic verification harnesses
- public-safe evidence and provenance
- changelog / lineage records

Public material must not include:

- credentials, tokens, passwords, or private account data
- private conversation exports or personal memory stores
- runtime databases, machine-local state, or generated logs
- trading credentials or private execution data
- local virtual environments, caches, backups, or recovery archives
- private artifacts merely because they exist in the working repository

See [`SECURITY.md`](SECURITY.md) and [`PUBLICATION_BOUNDARY.md`](PUBLICATION_BOUNDARY.md).

## Clone

```bash
git clone https://github.com/architexture23/constitutional-memory-core.git
cd constitutional-memory-core
```

The previous README advertised npm and PyPI installation commands that are not currently treated as verified release paths. They have been removed from the public quick start until reproducible release validation exists.

## Lineage

The November 2025 public repository and the later local implementation lineage were initialized independently. They do not share one clean Git ancestry. The public history is therefore preserved while newer artifacts are imported selectively with provenance rather than force-merging unrelated histories.

See [`LINEAGE.md`](LINEAGE.md) and [`RECONCILIATION.md`](RECONCILIATION.md).

## License

The repository is licensed under the [MIT License](LICENSE). MIT is permissive open-source licensing; it is not the same thing as public-domain dedication.

---

**Repository role:** public architecture, status, and selectively published verified implementation  
**Lifecycle:** `VERIFYING`  
**Last reconciled:** 2026-08-24
