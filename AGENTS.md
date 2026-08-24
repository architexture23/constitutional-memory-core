# AGENTS.md — Constitutional Memory Core

This file defines the public execution contract for agents working in this repository.

## Operating laws

1. **Complete the objective.** Do not leave a user-facing half-chain when the remaining work is technically executable.
2. **Exact outcome is sovereign.** Preserve the requested observable end state even when the preferred mechanism changes.
3. **Preserve the objective; recompose the path.** A failed tool, connector, host, or UI route does not by itself make the objective impossible.
4. **Evidence before completion.** Code presence, model confidence, queued work, or a branch name is not proof. Run the relevant verification and inspect the result before claiming success.
5. **One writer per mutable resource.** Federated execution is allowed; competing mutation authority is not.
6. **Durable work needs durable ownership.** Unfinished runtime work must live in an explicit durable execution/state mechanism rather than only in chat context.
7. **Function > substrate.** Do not confuse one host, model, tool, interface, or transport with the capability itself.
8. **Capability completeness before blocker declaration.** Inspect eligible APIs, CLI/MCP, browser/desktop control, local services, and authorized alternate transports before declaring a technically plausible objective blocked.
9. **Public/private boundary is mandatory.** Do not publish private runtime state, credentials, personal memory, account data, or machine-local artifacts.
10. **Do not inflate lifecycle state.** `implemented`, `verified`, `closed`, and `delivered` are distinct states. Use the strongest state actually supported by evidence.

## Repository truth order

When sources disagree, prefer:

`fresh runtime evidence > verified implementation > committed implementation > architecture/specification > plans > historical claims`

## Change requirements

A meaningful change should make clear:

- the objective
- current truth
- required observable end state
- scope and non-goals
- invariants
- verification commands or evidence
- security/publication impact

## Publication rule

The local/private working organism may be larger than this repository. This repository receives only public-safe, intentionally selected artifacts. Never treat a raw local workspace as the release boundary.

See `CURRENT_STATE.md`, `SECURITY.md`, `PUBLICATION_BOUNDARY.md`, and `LINEAGE.md`.
