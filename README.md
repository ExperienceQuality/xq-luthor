# xq-luthor

Contract-first hub repository. OpenAPI documents and the database schema are hand-authored here as the source of truth, and generated client code for `nodejs`, `python`, and `java` is committed alongside them so consumers do not need codegen toolchains.

## Contract layout

```text
openapi/<service_name>/openapi.yaml
openapi/<service_name>/<version>/{nodejs,python,java}/
database_schema/schema.sql
database_schema/{nodejs,python,java}/
```

Layout rules:

- OpenAPI documents live at `openapi/<service_name>/openapi.yaml`, one document per service. `<service_name>` is the service identifier (for example, `openapi/example/openapi.yaml`).
- Generated API clients live under `openapi/<service_name>/<version>/<lang>/`, where `<version>` is the contract version (for example, `v1.0.0`) and `<lang>` is one of `nodejs`, `python`, or `java`.
- The canonical database schema is PostgreSQL DDL and lives in `database_schema/` (for example, `database_schema/schema.sql`).
- Generated database clients live under `database_schema/<lang>/`.
- Directories that hold generated code are never hand-edited. Generated output is refreshed by rerunning the codegen pipeline, not by editing files in place.
- Contracts themselves (`openapi.yaml`, `schema.sql`) are hand-authored and reviewed; only the generated client directories are machine-produced.
- AsyncAPI support is explicitly deferred; do not add an `asyncapi/` directory yet.
