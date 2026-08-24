# Architecture

## 1. Constitutional / remembrance layer

Purpose: preserve durable rules, preferences, patterns, and structural memory across sessions without treating every prior artifact as equally authoritative.

Core responsibilities:

- load durable constitutional context
- distinguish historical memory from current operative truth
- detect drift and contradiction
- preserve lineage while allowing correction

## 2. Objective-preservation layer

Core law: **Preserve the objective. Recompose the path.**

A preferred route failing must not be silently converted into objective failure. The system inspects eligible alternatives, substitutes when necessary, and continues toward the requested observable outcome.

This includes the Objective Preservation Loop and the `Substitute -> Compound` principle: substitutes can combine rather than being evaluated only one at a time.

## 3. Durable execution layer

Purpose: move unfinished intent out of fragile chat-only state and into explicit runtime ownership.

Current architecture centers on durable work state such as `ACTIVE_WORK`, unattended intake, and Temporal-backed execution where applicable.

Important distinction: a durable queued state is not itself proof of completion. Runtime ownership and completion evidence are separate.

## 4. Execution-routing layer

Execution may be routed across available authorized mechanisms, including APIs, MCP/CLI, browser or desktop automation, local services, macros, and specialist nodes.

The router follows **Function > substrate**: the capability is defined by what it can reliably accomplish and prove, not by a preferred host or interface.

## 5. Authority and ownership layer

The system keeps one mutation owner per resource and separates:

- interpretation / acceptance authority
- implementation authority
- persistent runtime ownership
- domain truth ownership

Federation does not mean every node has equal write authority.

## 6. Verification / operative-truth layer

Completion claims require evidence appropriate to the work.

Examples include:

- focused tests
- inherited/full regression tests
- live dispatch/resume proof
- journal or receipt checks
- specification review
- adversarial quality review

The operative-truth layer prevents staged, `PREPARED`, queued, or merely named artifacts from being promoted to verified state without evidence.

## 7. Public projection layer

The private working organism is larger than this repository. GitHub receives an intentionally selected public-safe projection:

`architecture -> implementation -> verification -> provenance`

Private runtime state, personal memory, credentials, account data, and unrelated local artifacts remain outside the public boundary.

## Meta-governance

The governing meta-rule is Whole-Organism Autonomy:

> Preserve the objective. Recompose the path. Goal > Tool.

The architecture is expected to evolve, but evolution must preserve truth, ownership, evidence, and lineage rather than merely accumulating new claims.
