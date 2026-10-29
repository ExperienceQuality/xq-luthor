# Contract Conventions

Rules for everything under `openapi/` and `database_schema/`. Contracts are the source of truth; generated code is disposable output.

## Service naming

- One directory per service: `openapi/<service_name>/`.
- `<service_name>` is lowercase kebab-case (`a-z`, `0-9`, `-`) and must match the consumer-facing service name exactly (e.g., `openapi/example/`).
- Exactly one `openapi.yaml` per service directory.

## Versioning

- Generated OpenAPI clients live under `openapi/<service_name>/<version>/`, where `<version>` is semantic versioning with a mandatory `v` prefix: `vX.Y.Z` (e.g., `v1.0.0`).
- `<version>` must equal `info.version` in that service's `openapi.yaml`, plus the `v` prefix.
- Version directories are immutable. Once a `<version>` is generated and published, never edit, regenerate, or delete anything under it.
- Any contract change requiring new clients is a new `<version>` directory — including fixes. Never mutate a released version dir.
- `database_schema/` is not versioned by directory: `schema.sql` is a single canonical file that evolves in place, with generated clients under `database_schema/<lang>/`.

## Authorship

- `openapi/<service_name>/openapi.yaml` and `database_schema/schema.sql` are hand-written. They are the source of truth.
- Contract changes go through the same PR review as code. Reviewers check downstream impact on already-published versions.
- AsyncAPI is deferred. Do not add `asyncapi/` directories.

## Generated code

- Everything under `openapi/<service_name>/<version>/{nodejs,python,java}/` and `database_schema/{nodejs,python,java}/` is machine-generated. Never hand-edit it; fix the contract or the generator instead.
- Regeneration procedure:
  1. Change the contract (`openapi.yaml` or `schema.sql`).
  2. For OpenAPI: create a new `<version>` directory (per immutability above).
  3. Rerun the codegen pipeline for every affected language.
  4. Commit the contract change and its regenerated output together in one PR — never one without the other.
- Regeneration must be deterministic: same contract + same pinned tool version = byte-identical output. The validation gate will diff committed output against a fresh regen.

## Distribution

- `nodejs` clients publish as npm packages to GitHub Packages (`npm.pkg.github.com`).
- `java` clients publish as Maven artifacts to GitHub Packages (`maven.pkg.github.com`).
- Published package versions match the contract version dir.
- `python` clients install directly from this repo's git tags via `uv` — no registry involved:
  `uv pip install 'git+https://github.com/ExperienceQuality/xq-luthor@<tag>#subdirectory=<package-dir>'`
- Tag scheme: `py/<package-name>/<semver>` (e.g. `py/xq-example-client/1.0.0`), where `<package-name>` is the package's `pyproject.toml` `name` and `<semver>` its `version`. For OpenAPI clients, `<semver>` is the contract version dir minus the `v` prefix. `database_schema` clients version independently of OpenAPI versions. One tag per package release lets one repo host multiple packages at independent versions.
- Examples:
  - `uv pip install 'git+https://github.com/ExperienceQuality/xq-luthor@py/xq-example-client/1.0.0#subdirectory=openapi/example/v1.0.0/python'`
  - `uv pip install 'git+https://github.com/ExperienceQuality/xq-luthor@py/xq-db-client/0.1.0#subdirectory=database_schema/python'`

## Consuming clients

GitHub Packages requires a token to install npm and Maven packages, even public ones. Use:

- locally: a classic personal access token with `read:packages`;
- in a consumer repo's GitHub Actions: the built-in `GITHUB_TOKEN` with `permissions: packages: read`. If a package is private, also grant the consumer repo access under the package's *Package settings → Manage Actions access*.

Python clients need no token (git install from this public repo; see [Distribution](#distribution)).

### Java (Maven)

Coordinates: `com.experiencequality:<service>-client:<semver>` (e.g. `example-client:1.0.0`) and `com.experiencequality:db-client:<semver>`.

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
    <artifactId>example-client</artifactId>
    <version>1.0.0</version>
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
    implementation("com.experiencequality:example-client:1.0.0")
}
```

### Node.js (npm)

Packages: `@experiencequality/<service>-client` (e.g. `example-client@1.0.0`) and `@experiencequality/db-client`.

`.npmrc` in the consumer project:

```ini
@experiencequality:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
```

Then `npm install @experiencequality/example-client@1.0.0`.

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
