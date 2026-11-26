# pipeline/nodejs

Pinned npm toolchain for the OpenAPI → nodejs client pipeline.

| Contract semver | ADR | Tools |
|-----------------|-----|-------|
| `< 1.2.0` | [ADR 0001](../../docs/adr/0001-codegen-tools.md) | `openapi-typescript` + `openapi-fetch` → `schema.ts` + `createClient()` |
| `≥ 1.2.0` | [ADR 0002](../../docs/adr/0002-openapi-nodejs-hey-api.md) | `@hey-api/openapi-ts` (SDK flat + Fetch client) → `src/` + compiled `dist/` |

Install with `npm ci` (committed `package-lock.json`). Bump pins only in a deliberate upgrade PR so regeneration stays deterministic.