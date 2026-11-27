# Squad Memory

This file holds canonical, human-readable knowledge for the repository. Update it during memory maintenance when durable conventions, architecture, or decisions are discovered.

## Repository map

`xq-luthor` is a contract-first hub for **OpenAPI only**. Hand-authored contracts are the source of truth; generated API clients for `nodejs`, `python`, and `java` are committed alongside them so consumers need no codegen toolchain. Database schema and DB clients live in **xq-db** (decision 2026-11-25, GH issue #11).

- `openapi/<service_name>/openapi.yaml` — hand-authored OpenAPI contract per service (e.g. `openapi/example/openapi.yaml`).
- `openapi/<service_name>/<vX.Y.Z>/{nodejs,python,java}/` — generated clients, versioned per contract version.
- `docs/contracts-conventions.md` — contract naming/versioning/authorship rules.
- `docs/adr/0001-codegen-tools.md` — OpenAPI codegen tool selection ADR.
- `tasks/plan.md`, `tasks/todo.md` — historical implementation plan (includes retired DB pipeline tasks).
- `.squad/` — squad config, agent profiles, workflows, memory.

## Conventions

From `docs/contracts-conventions.md`:

- Service names: lowercase kebab-case, matching the consumer-facing service name; exactly one `openapi.yaml` per service dir.
- Version dirs: `vX.Y.Z` (mandatory `v` prefix) equal to `info.version`; immutable once published — any contract change gets a new version dir.
- Everything under generated dirs is machine-generated — never hand-edit; fix the contract or generator.
- Contract change + regenerated output are committed together in one PR — never one without the other.
- Regeneration must be deterministic: same contract + same pinned tool version = byte-identical output (Task 8 gate diffs fresh regen vs committed output).
- AsyncAPI is deferred — do not create `asyncapi/` dirs.
- Deprecated: `py/xq-db-client/0.1.0` — use **xq-db** for DB clients.

Squad rules:

- Lead never commits/pushes/PRs without explicit authorization (`.squad/agents/lead.md`, `AGENTS.md`).
- `analyst` profile is read-only — it returns findings; the Lead writes the docs.

## Architecture

- OpenAPI contracts authored and versioned in this repo — not synced from elsewhere.
- One OpenAPI codegen pipeline per language (nodejs, python, java), parameterized by service and version dir.
- Codegen tool picks:
  - OpenAPI → nodejs **&lt; 1.2.0**: ADR 0001 — `openapi-typescript` + `openapi-fetch`, `createClient()`.
  - OpenAPI → nodejs **≥ 1.2.0**: ADR 0002 (accepted) — `@hey-api/openapi-ts` flat SDK + compiled `dist/`.
- Current target contracts: **routine-service / exercise-service `1.2.0`** (GH #12). `v1.0.0` / `v1.1.0` dirs immutable. fitness-bff left alone for now (#18).
  - OpenAPI → python: `openapi-python-client`, direct.
  - OpenAPI → java: `openapi-generator` `java` generator with `library=okhttp-gson` (no Spring dependency), direct.
- Determinism requires pinning all of: tool version (recorded in a committed lockfile/manifest), JDK/Node/Python versions.
- Distribution: nodejs → npm on GitHub Packages; java → Maven on GitHub Packages; python → GitHub Release wheels (tags `py/<package>/<semver>`).

## Testing strategy

- Task 8: contract validation gate — lint OpenAPI contracts on change and diff a fresh regeneration against committed output (`scripts/validate.sh`, CI `validate.yml`).
- Generated nodejs clients verified by compile (`npm`/`tsc`); python by clean import; java by `javac`/`mvn` (per `tasks/todo.md`).

## Lessons

- Prefer boring, maintained codegen tools for OpenAPI → client generation.
- Detailed structured records live in `.squad/memory/*.ndjson`; supersede stale DB-pipeline records when updating memory.