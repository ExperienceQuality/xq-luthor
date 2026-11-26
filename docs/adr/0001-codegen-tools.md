# ADR 0001: Codegen tool selection for OpenAPI client pipelines

Status: Accepted — approved at Foundation checkpoint.

> **Amendment (2026-11-25, GH issue #11):** Database schema and DB client codegen were removed from `xq-luthor`. Canonical PostgreSQL DDL and DB clients belong to **xq-db** (ADR-001 there). This ADR now covers **OpenAPI → client** pipelines only.

## Context

`xq-luthor` commits generated clients alongside hand-authored OpenAPI contracts so consumers
need no codegen toolchain (README.md). One artifact type feeds three generation cells per
service version:

- `openapi/<service>/openapi.yaml` → nodejs, python, java clients (published via npm /
  Maven on GitHub Packages, and GitHub Release wheel/sdist assets respectively;
  `uv` git-tag install retained as source fallback).

Hard constraints:

1. **Deterministic regeneration** (docs/contracts-conventions.md): same contract +
   same pinned tool = byte-identical output. The Task 8 gate diffs a fresh regen
   against committed output, so tool versions must be pinned exactly.
2. No version numbers are asserted in this ADR. At pipeline-build time, each tool is
   pinned to its **latest stable release**, the resolved version is recorded in a
   committed lockfile/manifest, and all regeneration uses that pin until a
   deliberate upgrade PR bumps it.

## Decision

| Artifact | Language | Selected tool | Input consumed | Version pin strategy |
|---|---|---|---|---|
| OpenAPI | nodejs | **openapi-typescript** (types) + **openapi-fetch** (runtime) — **superseded for ≥ 1.2.0** by [ADR 0002](./0002-openapi-nodejs-hey-api.md) | `openapi.yaml` directly | npm devDependency + committed `package-lock.json` in the pipeline workspace |
| OpenAPI | python | **openapi-python-client** | `openapi.yaml` directly | `uv` pinned run (`uv tool run` with `==` pin or locked via `uv.lock`); pin recorded in pipeline manifest |
| OpenAPI | java | **openapi-generator** `java` generator, `library=okhttp-gson` | `openapi.yaml` directly | Pin generator release (Maven plugin version or CLI jar/container image digest) + JDK toolchain version |

### OpenAPI → nodejs: openapi-typescript + openapi-fetch

- Emit strict TypeScript types for every schema/operation; `openapi-fetch` provides a
  minimal typed `fetch` wrapper. Output is a small, deterministic `.d.ts`-style file —
  trivially diffable by the validation gate.
- No framework or HTTP-client lock-in beyond `fetch` (universal on modern Node 18+);
  consumers compose their own retry/auth transport.
- Both packages live in the same maintained ecosystem (openapi-ts), MIT-licensed,
  pure Node — no JVM needed in the nodejs pipeline.
- Rejected: **openapi-generator `typescript-fetch`** — produces a complete runtime
  client (per-endpoint classes, config objects), which is heavier to publish and
  requires a JVM in an otherwise-Node pipeline; output is more verbose and churns
  more across generator versions, enlarging regen diffs. Kept as fallback if
  consumers later demand a batteries-included client.
- Rejected: **orval** — excellent but feature-rich (axios/fetch variants, msw mocks,
  mutator hooks); more config surface and more release churn than this hub needs.
  Revisit if mock generation becomes a requirement.

### OpenAPI → python: openapi-python-client

- Generates a complete, self-contained Python package (httpx-based client + typed
  models) with its own `pyproject.toml` — aligns directly with the `uv` git-install
  distribution model with minimal packaging glue.
- MIT-licensed, actively maintained, purpose-built for client generation rather than
  models only.
- Rejected: **openapi-generator `python`** — generated code is verbose and
  stylistically dated; same JVM dependency concern; larger regen diffs.
- Rejected: **datamodel-code-generator** — emits Pydantic/dataclass **models only,
  no client methods**. Would require hand-written transport per service, which
  contradicts the generated-only convention. A reasonable supplement if consumers
  want standalone models, but insufficient alone.

### OpenAPI → java: openapi-generator, `library=okhttp-gson`

- OkHttp + Gson client with **no Spring dependency** — correct default for a hub
  repo whose consumers' frameworks are unknown. Mature, widely used, Apache-2.0.
- Rejected: **`resttemplate`** and **`webclient`** — couple every consumer to
  Spring (MVC and WebFlux respectively). Wrong default for a shared contract hub;
  individual services can generate their own Spring-flavored client if needed.
- Considered: **`native`** (Java 11 `HttpClient` + Jackson) — attractive zero-HTTP-dep
  option; kept as fallback if OkHttp/Gson versions conflict for consumers, but
  okhttp-gson is the more battle-tested path.
- Determinism note: openapi-generator output varies *between generator releases*
  (templates change). Pin the exact release and the JDK; the regen-diff gate will
  flag any unplanned bump.

## Consequences

**Positive**

- All OpenAPI cells consume `openapi.yaml` directly — no preprocessing.
- Small, diffable artifacts (openapi-typescript types) make the Task 8 regen-diff gate
  precise rather than noisy.

**Negative**

- Three toolchain ecosystems must be versioned and locked: npm and Python/uv; the Java
  cell additionally requires a JDK and pinned generator release. Regen output is only
  deterministic when *all* of {tool version, JDK/Node/Python version} are pinned — the
  pipeline manifest must record them together.
- openapi-python-client imposes its runtime deps (httpx, attrs/pydantic per version)
  on generated packages — acceptable, but a locked input to each client's
  `pyproject`.

## Alternatives (whole-approach)

- **openapi-generator for all three OpenAPI languages:** single tool/JVM, uniform
  config — rejected because output quality and idiom are worse for nodejs/python,
  and it forces a JVM into every pipeline.
- **Types-only contracts (no runtime clients):** rejected; consumers explicitly
  consume packaged clients (tasks/plan.md).

## Historical note: SQL DDL codegen (removed)

Prior versions of this ADR selected kysely-codegen, sqlacodegen, and jOOQ for
`database_schema/schema.sql` with an ephemeral Postgres preamble. That scope was
retired in favor of **xq-db** owning schema and DB clients. The old release
`py/xq-db-client/0.1.0` is deprecated (see `docs/contracts-conventions.md`).