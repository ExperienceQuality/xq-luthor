# Contract Conventions

Rules for everything under `openapi/`. Contracts are the source of truth; generated code is disposable output.

Database schema and DB clients are **not** owned by this repo. Canonical DDL and DB access code live in [xq-db](https://github.com/ExperienceQuality/xq-db).

## Service naming

- One directory per service: `openapi/<service_name>/`.
- `<service_name>` is lowercase kebab-case (`a-z`, `0-9`, `-`) and must match the consumer-facing service name exactly (e.g., `openapi/routine-service/`).
- Exactly one `openapi.yaml` per service directory.
- `openapi/example/` is a **template only** (illustrates layout and codegen). It is not a production service; do not depend on it for new work (GH #17).

## Versioning

### Layout and immutability

- Generated OpenAPI clients live under `openapi/<service_name>/<version>/`, where `<version>` is semantic versioning with a mandatory `v` prefix: `vX.Y.Z` (e.g., `v1.2.0`).
- `<version>` must equal `info.version` in that service's `openapi.yaml`, plus the `v` prefix. The hand-authored YAML always describes the **current target** version; older targets remain only as frozen dirs under `vX.Y.Z/`.
- **Published version directories are immutable.** Once a `<version>` dir is generated and shipped (merged and/or published as npm/Maven/Python assets), never edit, regenerate, or delete anything under it — including generator upgrades or call-shape changes. Any change that needs new clients is a **new** `<version>` directory.

### Current target

| Service | Current target | Superseded (immutable) |
|---------|----------------|------------------------|
| `routine-service` | **`1.2.0`** | `1.0.0`, `1.1.0` |
| `exercise-service` | **`1.2.0`** | `1.0.0`, `1.1.0` |
| `example` | *(none — template only)* | `1.0.0` (history only; not a target) |

Supersession chain for routine/exercise: **`1.0.0` → `1.1.0` → `1.2.0` (current)**. `1.2.0` is the multi-user JWT target (snapshots, cursor pagination, `exerciseNames`, required fields) plus exercise `POST /api/v1/exercise-logs` **409**. Node clients for ≥ 1.2.0 use [ADR 0002](./adr/0002-openapi-nodejs-hey-api.md). New work depends on **1.2.0**, not `1.0.0`, `1.1.0`, or `example`.

### Semver bumps (when to cut a new dir)

Bump `info.version` and create `vX.Y.Z/` as follows. Always cut a new dir; never patch an existing published dir in place.

| Bump | Use when |
|------|----------|
| **MAJOR** (`X`) | Breaking HTTP or **client** change for consumers of this contract (see below). Example: requiring JWT on paths that were public, removing `/api/v1/routines/{routineId}`, renaming `operationId` `getRoutine` → `fetchRoutine`. |
| **MINOR** (`Y`) | Backward-compatible additive HTTP change, or a **non-breaking** client/tooling change that still needs a new immutable dir. Example: exercise-service `1.1.0` → `1.2.0` documenting create **409** while keeping the 1.1.0 surface; adding an optional query param. |
| **PATCH** (`Z`) | Documentation-only or non-behavioral contract clarifications that still require regenerated clients for determinism (rare). Prefer MINOR if consumers could notice. Never use PATCH to sneak in breaking changes. |

If unsure whether a change is breaking, bump **MAJOR**.

### What counts as breaking

Treat any of the following as **breaking** for that service’s consumers (→ **MAJOR**, new `vX.Y.Z`):

**HTTP / OpenAPI contract**

- Auth: adding required security (e.g. `bearerAuth`) where none existed; tightening scopes.
- Paths / methods: removing or renaming a path; removing an HTTP method.
- Request: adding a **required** field or parameter; tightening types/enums/patterns in a way that rejects previously valid input.
- Response: removing a field consumers rely on; changing pagination shape (e.g. offset → cursor); changing success status codes; renaming schema or property names that appear in payloads.
- Errors: removing a documented status that clients handle; changing problem `code` semantics without a new version.
- Identifiers: renaming `operationId` or component schema names that generators bind to (affects typed clients even if wire JSON is unchanged).

**Client / generator (language-specific)**

- A **generator or call-shape change** is a **client breaking change for that language**, even when the HTTP contract is unchanged. Example: switching TypeScript from openapi-fetch `client.GET("/path")` to `@hey-api/openapi-ts` flat `getRoutine(...)` ([ADR 0002](./adr/0002-openapi-nodejs-hey-api.md) / issue #10).
- **Do not** apply a new generator or call shape in place to a published version dir (`v1.0.0`, `v1.1.0`, …). Ship the new shape only under a new version dir (for TypeScript, contract semver ≥ **1.2.0**).
- Python and Java keep their existing generators unless a separate ADR changes them; the same immutability rule applies.

### Deprecation

**Version deprecation**

1. Mark the version superseded in this doc’s [Current target](#current-target) table (and README).
2. Keep the `vX.Y.Z/` tree and published packages/tags; do **not** delete them in the deprecation PR.
3. Point consumers at the current target (e.g. routine-service / exercise-service **1.2.0**).
4. Optionally note the superseded version under [Deprecated releases](#deprecated-releases).

**Operation deprecation**

1. Prefer OpenAPI `deprecated: true` on the operation in a **new** minor/major contract version; do not edit an already-published version dir.
2. Keep the operation until a later MAJOR removes it.
3. Document migration in the PR / release notes (which service, which `operationId`, which replacement).

Example: do not strip `listRoutines` from `openapi/routine-service/v1.1.0/`; introduce replacement or mark deprecated only in a newer target YAML and its new `vX.Y.Z/` clients.

## Authorship

- `openapi/<service_name>/openapi.yaml` is hand-written. It is the source of truth.
- Contract changes go through the same PR review as code. Reviewers check downstream impact on already-published versions.
- AsyncAPI is deferred. Do not add `asyncapi/` directories.

## Generated code

- Everything under `openapi/<service_name>/<version>/{nodejs,python,java}/` is machine-generated. Never hand-edit it; fix the contract or the generator instead.
- Regeneration procedure:
  1. Change the contract (`openapi.yaml`).
  2. Create a new `<version>` directory when immutability requires it (per above).
  3. Rerun the OpenAPI codegen pipeline for every affected language (`scripts/gen-openapi-*.sh`).
  4. Commit the contract change and its regenerated output together in one PR — never one without the other.
- Regeneration must be deterministic: same contract + same pinned tool version = byte-identical output. The validation gate will diff committed output against a fresh regen.

## Distribution

- `nodejs` clients publish as npm packages to GitHub Packages (`npm.pkg.github.com`).
- `java` clients publish as Maven artifacts to GitHub Packages (`maven.pkg.github.com`).
- Published package versions match the contract version dir.
- `python` clients distribute as built `wheel` + `sdist` assets on a GitHub Release — no registry involved (GitHub Packages has no PyPI endpoint):
  `uv pip install 'https://github.com/ExperienceQuality/xq-luthor/releases/download/<tag>/<package>-<semver>-py3-none-any.whl'`
- Tag/release scheme: `py/<package-name>/<semver>` (e.g. `py/xq-example-client/1.0.0`), where `<package-name>` is the package's `pyproject.toml` `name` and `<semver>` its `version`. For OpenAPI clients, `<semver>` is the contract version dir minus the `v` prefix. One tag per package release lets one repo host multiple packages at independent versions.
- Python release procedure (run after the contract+clients PR merges and the `py/` tag is pushed):
  1. `uv build --out-dir <dist-dir> <package-dir>` — emits `<pkg>-<semver>.tar.gz` and `<pkg>-<semver>-py3-none-any.whl`.
  2. `gh release create <tag> <dist-dir>/* --title "<package-name> <semver>" --generate-notes` — attaches both assets to the tag's release.
  3. Verify: `uv pip install '<release-asset-wheel-url>'` in a scratch venv.
- Example:
  - `uv pip install 'https://github.com/ExperienceQuality/xq-luthor/releases/download/py/xq-example-client/1.0.0/xq_example_client-1.0.0-py3-none-any.whl'`
  - Fallback (no release needed, builds from source): `uv pip install 'git+https://github.com/ExperienceQuality/xq-luthor@<tag>#subdirectory=<package-dir>'`

## Deprecated releases

Tags and release files below stay for history; do **not** delete them when deprecating (including this issue’s retention of `py/xq-example-client/1.0.0`, `py/xq-routine-service-client/1.0.0`, and `py/xq-exercise-service-client/1.0.0`). Prefer the [current target](#current-target).

| Tag / version | Package or contract | Notes |
|---------------|---------------------|-------|
| `py/xq-db-client/0.1.0` | `xq-db-client` | Deprecated (issue #11). Use DB clients from **xq-db**. |
| `py/xq-example-client/1.0.0` / `openapi/example` | `example` template | **Template only** (GH #17). Not a production target; keep tree and tag; do not treat as current. |
| routine-service / exercise-service **1.0.0** | API contracts + clients | Superseded first by **1.1.0**, then by **1.2.0** (current). Dirs/tags immutable. |
| routine-service / exercise-service **1.1.0** | API contracts + clients | Superseded by **1.2.0**. Dirs/tags immutable. |
| Node under `v1.0.0/` and `v1.1.0/` | TypeScript clients | Stay on the pre–ADR 0002 (openapi-fetch) generator; do **not** regenerate with the ADR 0002 toolchain. |

## Consuming clients

GitHub Packages requires a token to install npm and Maven packages, even public ones. Use:

- locally: a classic personal access token with `read:packages`;
- in a consumer repo's GitHub Actions: the built-in `GITHUB_TOKEN` with `permissions: packages: read`. If a package is private, also grant the consumer repo access under the package's *Package settings → Manage Actions access*.

Python clients need no token (public repo release assets and git tags; see [Distribution](#distribution)). If the repo ever goes private, release-asset URLs and git installs both require repo access — prefer the git+ssh form then.

### Java (Maven)

Coordinates: `com.experiencequality:<service>-client:<semver>` (e.g. current target `routine-service-client:1.2.0`). Do not use `example-client` or superseded `1.0.0` / `1.1.0` for new work.

`pom.xml`:

```xml
<repositories>
  <repository>
    <id>github-xq-luthor</id>
    <url>https://maven.pkg.github.com/ExperienceQuality/xq-luthor</url>
  </repository>
</repositories>

<dependencies>
  <dependency>
    <groupId>com.experiencequality</groupId>
    <artifactId>routine-service-client</artifactId>
    <version>1.2.0</version>
  </dependency>
</dependencies>
```

`~/.m2/settings.xml` (the `<id>` must match the repository id above):

```xml
<settings>
  <servers>
    <server>
      <id>github-xq-luthor</id>
      <username>${env.GITHUB_ACTOR}</username>
      <password>${env.GITHUB_TOKEN}</password>
    </server>
  </servers>
</settings>
```

### Java (Gradle, Kotlin DSL)

```kotlin
repositories {
    maven {
        url = uri("https://maven.pkg.github.com/ExperienceQuality/xq-luthor")
        credentials {
            username = System.getenv("GITHUB_ACTOR")
            password = System.getenv("GITHUB_TOKEN")
        }
    }
}

dependencies {
    implementation("com.experiencequality:routine-service-client:1.2.0")
}
```

### Node.js (npm)

Packages: `@experiencequality/<service>-client` (e.g. current target `@experiencequality/routine-service-client@1.2.0`). Do not depend on `example-client` or superseded `1.0.0` / `1.1.0` for new work.

**Legacy clients** (`openapi/*/v1.0.0/nodejs`, `v1.1.0/nodejs`) expose `createClient(baseUrl)` and path-literal `client.GET(...)` via openapi-fetch ([ADR 0001](./adr/0001-codegen-tools.md)). Those dirs stay on that generator; do not regenerate them with ADR 0002.

**Current target clients** (contract semver ≥ **1.2.0**, [ADR 0002](./adr/0002-openapi-nodejs-hey-api.md)) compile to `dist/` and export flat `operationId` functions (e.g. `getRoutine`, `createRoutine`) plus a shared `client` with `setConfig`:

```ts
import { client, getRoutine, listRoutines } from "@experiencequality/routine-service-client";

client.setConfig({
  baseUrl: process.env.XQ_ROUTINE_BASE_URL!,
  auth: () => process.env.XQ_JWT!,
});

const { data: routine } = await getRoutine({ path: { routineId } });
const { data: page } = await listRoutines({ query: { limit: 20 } });
```

`.npmrc` in the consumer project:

```ini
@experiencequality:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
```

Then `npm install @experiencequality/routine-service-client@1.2.0`.

### GitHub Actions example

```yaml
permissions:
  contents: read
  packages: read

steps:
  - uses: actions/checkout@v4
  # Maven only: writes ~/.m2/settings.xml with the <server> entry above.
  - uses: actions/setup-java@v4
    with:
      distribution: temurin
      java-version: "21"
      server-id: github-xq-luthor
      server-username: GITHUB_ACTOR
      server-password: GITHUB_TOKEN
  - run: mvn -B verify          # or: ./gradlew build / npm ci
    env:
      GITHUB_ACTOR: ${{ github.actor }}
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```