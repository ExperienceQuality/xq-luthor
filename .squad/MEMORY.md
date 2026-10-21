# Squad Memory

This file holds canonical, human-readable knowledge for the repository. Update it during memory maintenance when durable conventions, architecture, or decisions are discovered.

## Repository map

`xq-luthor` is a contract-first hub. Hand-authored contracts are the source of truth; generated clients for `nodejs`, `python`, and `java` are committed alongside them so consumers need no codegen toolchain.

- `openapi/<service_name>/openapi.yaml` — hand-authored OpenAPI contract per service (e.g. `openapi/example/openapi.yaml`).
- `openapi/<service_name>/<vX.Y.Z>/{nodejs,python,java}/` — generated clients, versioned per contract version.
- `database_schema/schema.sql` — canonical PostgreSQL DDL, single evolving file (not version-dir'd).
- `database_schema/{nodejs,python,java}/` — generated DB access code.
- `docs/contracts-conventions.md` — contract naming/versioning/authorship rules.
- `docs/adr/0001-codegen-tools.md` — codegen tool selection ADR.
- `tasks/plan.md`, `tasks/todo.md` — 11-task implementation plan and checklist (T1–T7 done; Foundation and Pipelines checkpoints complete).
- `.squad/` — squad config, agent profiles, workflows, memory.

## Conventions

From `docs/contracts-conventions.md`:

- Service names: lowercase kebab-case, matching the consumer-facing service name; exactly one `openapi.yaml` per service dir.
- Version dirs: `vX.Y.Z` (mandatory `v` prefix) equal to `info.version`; immutable once published — any contract change gets a new version dir.
- `database_schema/schema.sql` evolves in place; generated code under `database_schema/<lang>/`.
- Everything under generated dirs is machine-generated — never hand-edit; fix the contract or generator.
- Contract change + regenerated output are committed together in one PR — never one without the other.
- Regeneration must be deterministic: same contract + same pinned tool version = byte-identical output (Task 8 gate diffs fresh regen vs committed output).
- AsyncAPI is deferred — do not create `asyncapi/` dirs.

Squad rules:

- Lead never commits/pushes/PRs without explicit authorization (`.squad/agents/lead.md`, `AGENTS.md`).
- `analyst` profile is read-only — it returns findings; the Lead writes the docs.

## Architecture

- Contracts authored and versioned in this repo — not synced from elsewhere.
- One codegen pipeline per artifact type (openapi, database_schema), parameterized by language.
- Codegen tool picks (ADR 0001, accepted pending human review at Foundation checkpoint):
  - OpenAPI → nodejs: `openapi-typescript` (types) + `openapi-fetch` (runtime), consumes `openapi.yaml` directly.
  - OpenAPI → python: `openapi-python-client`, direct.
  - OpenAPI → java: `openapi-generator` `java` generator with `library=okhttp-gson` (no Spring dependency), direct.
  - SQL DDL → nodejs: `kysely-codegen` (Kysely types only).
  - SQL DDL → python: `sqlacodegen` (SQLAlchemy declarative models).
  - SQL DDL → java: `jOOQ` codegen (`jooq-codegen-maven`), `PostgresDatabase` — not `DDLDatabase`.
- All three SQL DDL tools introspect a **live database**, so the pipeline has a shared preamble: start ephemeral **embedded** PostgreSQL via `scripts/pg-ephemeral.sh` (`uv run --with postgresql-binaries==16.15.0` → `pg-ephemeral.py`) → apply `schema.sql` → introspect. No Docker daemon required. `DDLDatabase`/H2 simulation rejected (silently mishandles Postgres-specific syntax).
- Determinism requires pinning all of: tool version (recorded in a committed lockfile/manifest), `postgresql-binaries` version (16.15.0, pinned in `pg-ephemeral.sh`), JDK/Node/Python versions.
- Distribution: nodejs → npm on GitHub Packages (`npm.pkg.github.com`); java → Maven on GitHub Packages (`maven.pkg.github.com`); python → `uv` git install from repo tags (GitHub Packages lacks python support). Git tag naming convention TBD in Task 11.

## Testing strategy

- Task 8 (planned): contract validation gate — lint contracts on change and diff a fresh regeneration against committed output to catch drift.
- Generated nodejs clients verified by compile (`npm`/`tsc`); python by clean import; java by `javac`/`mvn` (per `tasks/todo.md`).

## Lessons

- Prefer boring, maintained codegen tools; when a mature tool needs a live DB, an ephemeral embedded Postgres (`postgresql-binaries` via `uv`, no Docker) beats DDL-simulation modes that fail silently on Postgres-specific syntax (extensions, `gen_random_uuid()`, `TIMESTAMPTZ`, domains).
- `schema.sql` must apply cleanly to a fresh empty Postgres (it may create its own extensions, e.g. `CREATE EXTENSION pgcrypto`).
- All 6 codegen pipelines (OpenAPI + database_schema × nodejs/python/java) run end-to-end deterministically with zero Docker dependency (Tasks 4–7 verified).
- Detailed structured records live in `.squad/memory/*.ndjson`.
