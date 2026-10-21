# pipeline/nodejs

Pinned npm toolchain for the OpenAPI -> nodejs client pipeline (ADR 0001).

- `openapi-typescript` generates `schema.ts` types from `openapi/<service>/openapi.yaml`.
- `openapi-fetch` is the runtime dependency baked into each generated client's
  `package.json`; its version is read from this workspace's `package.json` so the
  pin lives in exactly one place.
- `typescript` satisfies openapi-typescript's `typescript: ^5.x` peer range and
  type-checks generated output.

Install/update the toolchain with `npm ci` (uses the committed `package-lock.json`).
Bump pins only via a deliberate upgrade PR — regeneration must be deterministic.
