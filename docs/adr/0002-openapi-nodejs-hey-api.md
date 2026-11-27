# ADR 0002: OpenAPI → nodejs via @hey-api/openapi-ts (SDK flat functions)

Status: Accepted — approved by David Châu 2026-11-27 (GH issue #10 / #12).

Supersedes: ADR 0001, **OpenAPI → nodejs** cell only (`openapi-typescript` + `openapi-fetch`).

## Context

Consumers (notably **xq-platform** → **xq-mcp**) need less boilerplate than the ADR 0001 client:

```ts
const { data, error } = await client.GET("/api/v1/routines/{routineId}", {
  params: { path: { routineId } },
  headers: { Authorization: `Bearer ${token}` },
});
```

Named operation functions and centralized auth config reduce noise:

```ts
client.setConfig({ baseUrl, auth: () => token });
const { data } = await getRoutine({ path: { routineId } });
```

Immutable published dirs `v1.0.0` and `v1.1.0` keep the legacy generator; **contract versions ≥ 1.2.0** use this ADR.

## Decision

| Item | Choice |
|------|--------|
| Generator | `@hey-api/openapi-ts` **0.99.0** (CLI in `pipeline/nodejs`) |
| SDK shape | `@hey-api/sdk` plugin, `operations.strategy: 'flat'`, `paramsStructure: 'flat'` |
| HTTP client | `@hey-api/client-fetch` (generated Fetch client; runtime pin **0.13.1** recorded in generated `package.json` when a separate runtime package is required; output is self-contained under `src/client/`) |
| TypeScript | **5.9.3** (same pin as legacy pipeline) |
| Version cutoff | Semver **≥ 1.2.0** → hey-api; **&lt; 1.2.0** → ADR 0001 toolchain (unchanged committed output) |
| Published artifact | `tsc` emit to `dist/` (`*.js` + `*.d.ts`); `package.json` `main`/`types`/`exports` point at `dist/` |
| Package names | Unchanged: `@experiencequality/<service>-client` on GitHub Packages |

Tool pins live in `pipeline/nodejs/package.json` + `package-lock.json`.

## Consequences

**Positive**

- Flat `operationId` functions align with MCP tool wrappers.
- Compiled `dist/` fits Node ≥24 consumers without compiling raw `.ts`.
- Older immutable version dirs stay on the legacy generator; validation gate unchanged for `v1.0.0` / `v1.1.0`.

**Negative**

- Two nodejs output layouts coexist until old dirs are deprecated.
- hey-api output is multi-file under `src/`; regen diffs are larger than `schema.ts` + `index.ts`.
- Cutoff `1.2.0` is fixed here; issue #12 may refine the first hey-api contract minor — never regenerate published dirs with the new toolchain.

## Alternatives considered

- **Amend ADR 0001 in place** — rejected (issue #10); supersession via this ADR only.
- **Regenerate `v1.1.0` nodejs with hey-api** — rejected; violates immutability and released clients.
- **openapi-typescript only (types) + hand SDK** — rejected; duplicates maintenance.