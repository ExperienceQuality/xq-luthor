# Implementation Plan: Contract Hub Scaffold

## Overview

`xq-luthor` is a contract-first hub repository. Database schema files and OpenAPI documents are hand-authored here as source of truth, and generated client code for `nodejs`, `python`, and `java` is committed alongside them. Squad agents read these contracts during delivery; other `xq-*` repositories consume the generated clients.

## Architecture Decisions

- Contracts are authored and versioned in this repo — not synced from other repos.
- AsyncAPI is explicitly on hold; do not create `asyncapi/` scaffolding yet.
- Generated client code is committed (not produced on demand by consumers) so consumers do not need codegen toolchains.
- One codegen pipeline per artifact type (openapi, database_schema), parameterized by language.

## Target Layout

```text
openapi/<service_name>/openapi.yaml
openapi/<service_name>/<version>/{nodejs,python,java}/
database_schema/<schema files>
database_schema/{nodejs,python,java}/
```

## Task List

### Phase 1: Foundation
- [x] Task 1: Scaffold directory skeleton + layout docs
- [x] Task 2: Contract conventions doc (naming, versioning, authorship rules)
- [x] Task 3: Pin codegen tool decisions (ADR)

### Checkpoint: Foundation
- [x] Layout reviewed with human; conventions approved; tools chosen

### Phase 2: Codegen pipelines
- [x] Task 4: OpenAPI -> nodejs client pipeline
- [x] Task 5: OpenAPI -> python client pipeline
- [x] Task 6: OpenAPI -> java client pipeline
- [x] Task 7: database_schema -> {nodejs,python,java} client pipeline

### Checkpoint: Pipelines
- [x] Each generator runs against a sample contract and produces committed output

### Phase 3: Distribution
- [x] Task 9: nodejs client publish -> GitHub Packages (npm)
- [x] Task 10: java client publish -> GitHub Packages (Maven)
- [x] Task 11: python client packaging for `uv` git install (pyproject + tags)

### Phase 4: Validation
- [x] Task 8: Lint/validate contracts on change (CI or pre-commit)

### Checkpoint: Complete
- [x] All acceptance criteria met; memory updated; ready for review

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Codegen tool choice locks in early | Med | Task 3 ADR before any pipeline work; pick boring, maintained tools |
| Generated code drift from committed contracts | Med | Task 8 validation regenerates and diffs |
| database_schema format undecided (SQL DDL vs Prisma vs migration files) | High | Resolve in Task 3; pipeline shape depends on it |
| Empty repo — no existing conventions to match | Low | Conventions doc (Task 2) defines them now |

## Open Questions (answered)

- Database engine: **PostgreSQL**.
- Schema format: **canonical SQL DDL** in `database_schema/`; Prisma or ORM artifacts generated for consumers as needed.
- Consumers pull clients as **published packages**.
- Registry: **GitHub Packages** (npm + Maven). Python unsupported there — Python clients ship as **wheel/sdist assets on GitHub Releases** (`py/<pkg>/<semver>` tags); `uv` git-tag install remains as source fallback.
