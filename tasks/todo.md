# Task List: Contract Hub Scaffold

## Task 1: Scaffold directory skeleton + layout docs

**Description:** Create `openapi/`, `database_schema/` with a placeholder example service so the layout is concrete, plus a root README section documenting the layout.

**Acceptance criteria:**
- [x] `openapi/<service_name>/` path exists with an `openapi.yaml` placeholder
- [x] `database_schema/` exists with a placeholder schema file
- [x] `{nodejs,python,java}` generated-client slots present under the example
- [x] README documents layout rules

**Verification:**
- [x] `find openapi database_schema -type f` shows expected skeleton

**Assignee:** `implementer`
**Dependencies:** None
**Estimated scope:** S (2-3 files)

## Task 2: Contract conventions doc

**Description:** `docs/contracts-conventions.md` covering: service naming, version directory semantics (semver, immutability), authorship rules (hand-written, reviewed), generated-code rules (never hand-edit, regeneration procedure).

**Acceptance criteria:**
- [x] Naming rules documented
- [x] Versioning rules documented
- [x] Generated-code rules documented

**Verification:**
- [x] Doc exists and covers all three rule sets

**Assignee:** `analyst`
**Dependencies:** Task 1
**Estimated scope:** S

## Task 3: Codegen tool decisions (ADR)

**Description:** `docs/adr/0001-codegen-tools.md` selecting tools: openapi -> nodejs (`openapi-typescript` or openapi-generator), python (`openapi-python-client`), java (`openapi-generator`); SQL DDL -> per-language DB clients. Inputs decided: PostgreSQL, canonical SQL DDL, publish to GitHub Packages (npm + Maven), python via `uv` git install.

**Acceptance criteria:**
- [x] One tool chosen per language per artifact type
- [x] Rationale recorded; alternatives listed

**Verification:**
- [x] ADR reviewed with human

**Assignee:** `analyst`
**Dependencies:** Task 2
**Estimated scope:** S

## Checkpoint: Foundation
- [x] Human approves layout, conventions, tool choices

## Task 4: OpenAPI -> nodejs client pipeline

**Description:** Script (`scripts/gen-openapi-client.sh` or Makefile target) that takes service + version and generates `openapi/<svc>/<ver>/nodejs/`.

**Acceptance criteria:**
- [x] Runs against sample openapi.yaml, produces committed output
- [x] Re-runnable, deterministic output

**Verification:**
- [x] Generated client compiles (`npm`/`tsc` where applicable)

**Assignee:** `implementer`
**Dependencies:** Task 3
**Estimated scope:** M

## Task 5: OpenAPI -> python client pipeline

**Acceptance criteria:**
- [x] Same contract as Task 4 for `python/` output
- [x] Generated client imports cleanly

**Verification:** `python -c "import <client>"`
**Assignee:** `implementer`
**Dependencies:** Task 3
**Estimated scope:** M

## Task 6: OpenAPI -> java client pipeline

**Acceptance criteria:**
- [x] Same contract for `java/` output
- [x] Generated client compiles (`javac`/`mvn`)

**Verification:** compile of generated module
**Assignee:** `implementer`
**Dependencies:** Task 3
**Estimated scope:** M

## Task 7: database_schema -> client pipeline (3 languages)

**Description:** Generate DB access code per language from schema files. Shape depends on Task 3 decision.

**Acceptance criteria:**
- [x] `database_schema/{nodejs,python,java}/` populated from schema
- [x] Regeneration is one command

**Verification:** generated code typechecks/compiles
**Assignee:** `implementer`
**Dependencies:** Task 3, Task 4-6 (shared script conventions)
**Estimated scope:** M

## Checkpoint: Pipelines
- [x] All four pipelines run end-to-end on sample artifacts

## Task 9: nodejs client publish -> GitHub Packages

**Description:** Package generated nodejs clients as scoped npm packages (`@experiencequality/...`) and publish to GitHub Packages. Needs `NPM_TOKEN`/GitHub auth, `package.json` registry config, publish script in codegen pipeline.

**Acceptance criteria:**
- [x] `npm publish` to `npm.pkg.github.com` succeeds for a sample client
- [x] Version matches contract version dir
- [x] Consumers can `npm install` with a `.npmrc` token

**Verification:** install the published package in a scratch dir
**Assignee:** `implementer`
**Dependencies:** Task 4
**Estimated scope:** M

## Task 10: java client publish -> GitHub Packages

**Description:** Package generated java clients as Maven artifacts and publish to `maven.pkg.github.com`. Needs `settings.xml`/pom distribution config.

**Acceptance criteria:**
- [x] `mvn deploy` to GitHub Packages succeeds
- [x] Version matches contract version dir

**Verification:** `mvn dependency:get` resolves the artifact
**Assignee:** `implementer`
**Dependencies:** Task 6
**Estimated scope:** M

## Task 11: python client packaging for `uv` git install

**Description:** Give generated python clients a `pyproject.toml` so consumers run `uv pip install git+https://github.com/ExperienceQuality/xq-luthor@vX.Y.Z#subdirectory=...` or equivalent. Tags/versioning strategy documented.

**Acceptance criteria:**
- [x] `uv pip install` from the repo installs a generated client
- [x] Tag/subdir convention documented in conventions doc

**Verification:** `uv pip install` from clean venv succeeds
**Assignee:** `implementer`
**Dependencies:** Task 5
**Estimated scope:** S

## Checkpoint: Distribution
- [x] One client per language consumed from its distribution channel

## Task 8: Contract validation gate

**Description:** Lint openapi yaml + schema on change; regeneration-diff check to catch drift. Pre-commit or CI.

**Acceptance criteria:**
- [ ] Invalid contract fails the gate
- [ ] Uncommitted generated drift fails the gate

**Verification:** introduce deliberate break, gate catches it
**Assignee:** `implementer`
**Dependencies:** Tasks 4-7
**Estimated scope:** M
