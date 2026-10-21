# xq-db-client

<!-- HAND-WRITTEN packaging glue (not generated). The xq_db_client/ package itself
     is machine-generated from database_schema/schema.sql — do not edit it by hand;
     regenerate with scripts/gen-db-python.sh. Keep this file in sync with
     docs/contracts-conventions.md. -->

SQLAlchemy declarative models generated from `database_schema/schema.sql`.

## Install

Install directly from the `xq-luthor` repo via `uv`:

```bash
uv pip install 'git+https://github.com/ExperienceQuality/xq-luthor@py/xq-db-client/0.1.0#subdirectory=database_schema/python'
```

See `docs/contracts-conventions.md` (Distribution) for the `py/<package>/<semver>` tag scheme.
