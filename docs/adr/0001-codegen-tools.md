# ADR 0001: Codegen tool selection for contract pipelines

Status: Accepted — pending human review at the Foundation checkpoint (tasks/plan.md). Not binding until approved.

## Context

`xq-luthor` commits generated clients alongside hand-authored contracts so consumers
need no codegen toolchain (README.md, tasks/plan.md). Two artifact types feed six
generation cells:

- `openapi/<service>/openapi.yaml` → nodejs, python, java clients (published via npm /
  Maven on GitHub Packages, and `uv` git install respectively).
- `database_schema/schema.sql` → nodejs, python, java database access code.

Hard constraints:

1. **Deterministic regeneration** (docs/contracts-conventions.md): same contract +
   same pinned tool = byte-identical output. The Task 8 gate diffs a fresh regen
   against committed output, so tool versions must be pinned exactly, and any tool
   that introspects a database must introspect a *pinned-version* ephemeral
   PostgreSQL instance.
2. **The DDL input is a bare `.sql` file, not a live database.** Most mature
   schema-codegen tools introspect a running Postgres. Where a tool requires that,
   the pipeline gains a standard preamble: start an ephemeral PostgreSQL container
   (pinned image tag/digest), apply `schema.sql`, then run the introspecting
   generator. This is preferable to DDL-simulation modes, which silently mishandle
   PostgreSQL-specific syntax (extensions, `gen_random_uuid()`, `TIMESTAMPTZ`,
   domains, partial indexes).
3. No version numbers are asserted in this ADR. At pipeline-build time, each tool is
   pinned to its **latest stable release**, the resolved version is recorded in a
   committed lockfile/manifest, and all regeneration uses that pin until a
   deliberate upgrade PR bumps it.

## Decision

| Artifact | Language | Selected tool | Input consumed | Version pin strategy |
|---|---|---|---|---|
| OpenAPI | nodejs | **openapi-typescript** (types) + **openapi-fetch** (runtime) | `openapi.yaml` directly | npm devDependency + committed `package-lock.json` in the pipeline workspace |
| OpenAPI | python | **openapi-python-client** | `openapi.yaml` directly | `uv` pinned run (`uv tool run` with `==` pin or locked via `uv.lock`); pin recorded in pipeline manifest |
| OpenAPI | java | **openapi-generator** `java` generator, `library=okhttp-gson` | `openapi.yaml` directly | Pin generator release (Maven plugin version or CLI jar/container image digest) + JDK toolchain version |
| SQL DDL | nodejs | **kysely-codegen** → Kysely type definitions | Ephemeral Postgres (apply `schema.sql`, then introspect) | npm pin + lockfile; pin `postgres:<tag>` image digest |
| SQL DDL | python | **sqlacodegen** → SQLAlchemy models (declarative; `--generator sqlmodel`/`dataclasses` variants available) | Ephemeral Postgres | uv/pip `==` pin + `uv.lock`; pin postgres image digest |
| SQL DDL | java | **jOOQ codegen** (`jooq-codegen-maven`) | Ephemeral Postgres via Testcontainers/Docker — **not** `DDLDatabase` | Maven plugin version pin; pin postgres image digest; pin JDK |

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
  distribution model (Task 11) with minimal packaging glue.
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

### SQL DDL → nodejs: kysely-codegen (with ephemeral Postgres)

- Produces Kysely `Database` interfaces — types only, no runtime lock-in; consumers
  bring Kysely (permissively licensed, MIT) themselves. Smallest possible committed
  artifact, clean diffs.
- **Honest flag:** kysely-codegen introspects a **live database**; it cannot parse a
  `.sql` file. Required workaround: pipeline spins a pinned `postgres` container,
  applies `schema.sql`, runs codegen against it. No mature pure-DDL parser
  alternative exists for Kysely types, so the ephemeral-DB step is the honest cost.
- Rejected: **pgtyped** — also needs a live DB, and it types *queries written in
  `.sql`/`.ts` files*, not the schema itself. Wrong input shape for this repo (we
  have DDL, not an authored query corpus). Revisit if a query file convention
  emerges.
- Rejected: **Drizzle introspection (`drizzle-kit pull`)** — needs a live DB too, and
  commits consumers to the Drizzle ORM rather than emitting neutral types. Heavier
  opinion than a contract hub should impose.

### SQL DDL → python: sqlacodegen (with ephemeral Postgres)

- Emits SQLAlchemy declarative models from introspection; newer releases also offer
  `dataclasses` and `sqlmodel` generators, leaving the model style flexible without
  changing the pipeline.
- **Honest flag:** sqlacodegen introspects a **live database** — same ephemeral-
  Postgres preamble as the nodejs cell.
- Rejected: **SQLAlchemy `automap`/runtime reflection** — reflects at runtime against
  a live DB; produces no committed artifact, violating the committed-generated-code
  and determinism requirements.
- Rejected: **hand-written models** — violates docs/contracts-conventions.md
  (generated dirs never hand-edited) and guarantees drift from `schema.sql`.
- Alternative noted: a custom DDL parser (e.g., sqlglot-based) could skip the
  ephemeral DB, but writing/maintaining our own parser contradicts "pick boring,
  maintained tools" (tasks/plan.md).

### SQL DDL → java: jOOQ codegen (with ephemeral Postgres / Testcontainers)

- Industry-standard for typed SQL in Java; generates table/record/POJO classes and a
  catalog/dsl API. Maven-native (`jooq-codegen-maven`), matching the Maven/GitHub
  Packages distribution path.
- **Honest flag:** jOOQ codegen normally introspects a live database. Workarounds,
  in preference order:
  1. **Ephemeral real Postgres (chosen):** Testcontainers or a CI service container
     running a pinned `postgres` image; apply `schema.sql`; run jOOQ codegen with
     `PostgresDatabase`. Most faithful — a real Postgres parses real Postgres DDL.
  2. **jOOQ `DDLDatabase` (rejected as primary):** parses DDL via an H2-backed
     simulation. Fast and container-free, but it is a *simulation* — PostgreSQL
     specifics (`CREATE EXTENSION pgcrypto`, `gen_random_uuid()`,
     `TIMESTAMPTZ`, domains, exclusion constraints) are partially or silently
     unsupported, risking wrong output rather than a clean failure. May be kept as a
     fast-path experiment only if the schema stays within its supported subset.
  3. Flyway-database mode: still resolves to a JDBC/H2 path — same caveats.
- License sanity: jOOQ Community Edition is Apache-2.0 and covers standard
  PostgreSQL; verify at pin time that required features don't pull in commercial
  editions (jOOQ Professional/Enterprise gate some dialect/version combinations).
- Rejected: **Hibernate Tools / JPA metamodel generation, MyBatis Generator,
  QueryDSL** — all need a live DB anyway, and each produces ORM-coupled or
  heavier-weight output; jOOQ's typed-SQL model best matches "contract-first" usage.

## Consequences

**Positive**

- One pipeline shape per artifact type; the DDL cells share a single reusable
  "ephemeral Postgres → apply schema → introspect" preamble (Task 7).
- All OpenAPI cells consume `openapi.yaml` directly — no preprocessing.
- Small, diffable artifacts (openapi-typescript, kysely-codegen) make the Task 8
  regen-diff gate precise rather than noisy.

**Negative**

- The DDL pipelines require Docker (or a Postgres service container) in every
  environment that regenerates, including CI — documented requirement for Task 7.
- Two toolchain ecosystems must be versioned and locked: npm and Python/uv; the Java
  cell additionally requires a JDK and pinned generator release. Regen output is
  only deterministic when *all* of {tool version, DB image tag, JDK/Node/Python
  version} are pinned — the pipeline manifest must record them together.
- `schema.sql` must remain applicable to a *fresh, empty* Postgres for the ephemeral
  step to work (no dependency on pre-existing extensions beyond what the script
  itself creates). `CREATE EXTENSION pgcrypto` in schema.sql already assumes the
  contrib package is present in the chosen postgres image.
- openapi-python-client imposes its runtime deps (httpx, attrs/pydantic per version)
  on generated packages — acceptable, but a locked input to each client's
  pyproject.

## Alternatives (whole-approach)

- **openapi-generator for all three OpenAPI languages:** single tool/JVM, uniform
  config — rejected because output quality and idiom are worse for nodejs/python,
  and it forces a JVM into every pipeline.
- **Types-only contracts (no runtime clients):** rejected; consumers explicitly
  consume packaged clients (tasks/plan.md).
- **Parse DDL directly instead of ephemeral DB:** rejected; no boring maintained
  tool parses raw Postgres DDL into these targets — introspection against a real,
  pinned Postgres is more correct.
