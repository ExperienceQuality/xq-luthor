#!/bin/sh
# gen-db-nodejs.sh — generate the nodejs (Kysely) database types for
# database_schema/schema.sql, per ADR 0001: kysely-codegen introspects a live
# Postgres, so this uses the shared ephemeral-Postgres preamble
# (scripts/pg-ephemeral.sh): start container, apply schema.sql, introspect.
#
# Usage: scripts/gen-db-nodejs.sh   (no args; schema.sql is the single
#                                   canonical input, docs/contracts-conventions.md)
#
# Input : database_schema/schema.sql (hand-authored source of truth)
# Output: database_schema/nodejs/
#           schema-types.ts  — kysely-codegen output (Kysely Database interface)
#           package.json     — @experiencequality/db-client
#           tsconfig.json    — `npm run typecheck` (tsc --noEmit)
#           .gitignore       — node_modules/, package-lock.json (install-time only)
#
# Tool versions come from pipeline/nodejs/package.json (installed via the
# committed package-lock.json) so regeneration is deterministic.
set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
ROOT_DIR=$(CDPATH='' cd -- "$SCRIPT_DIR/.." && pwd)
cd "$ROOT_DIR"

PIPELINE_DIR="$ROOT_DIR/pipeline/nodejs"
GEN_BIN="$PIPELINE_DIR/node_modules/.bin/kysely-codegen"
OUT_DIR="$ROOT_DIR/database_schema/nodejs"

if [ ! -x "$GEN_BIN" ]; then
  echo "installing pinned pipeline toolchain (npm ci) ..." >&2
  npm --prefix "$PIPELINE_DIR" ci --no-audit --no-fund
fi

# --- Shared preamble: ephemeral Postgres (scripts/pg-ephemeral.sh) -----------
# `start` prints the DSN on stdout and `container: NAME` on stderr, so stderr is
# captured to a file (not /dev/null) to recover the container name; on failure
# the captured stderr is replayed for diagnostics.
START_LOG=$(mktemp "${TMPDIR:-/tmp}/pgcodegen-start.XXXXXX")
CONTAINER=
cleanup() {
  if [ -n "$CONTAINER" ]; then
    ./scripts/pg-ephemeral.sh stop "$CONTAINER" >/dev/null 2>&1 || true
  fi
  rm -f "$START_LOG"
}
trap cleanup EXIT

if ! DSN=$(./scripts/pg-ephemeral.sh start 2>"$START_LOG"); then
  cat "$START_LOG" >&2
  echo "error: failed to start ephemeral postgres" >&2
  exit 1
fi

CONTAINER=$(sed -n 's/^container: //p' "$START_LOG" | head -n 1)
if [ -z "$CONTAINER" ]; then
  # pg-ephemeral.sh names containers xq-luthor-pgcodegen-<pid>; without the name
  # we cannot clean up reliably, so fail loudly rather than leak a container.
  echo "error: could not determine ephemeral container name from pg-ephemeral.sh stderr" >&2
  cat "$START_LOG" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
rm -f "$OUT_DIR/.gitkeep"

"$GEN_BIN" \
  --dialect postgres \
  --url "$DSN" \
  --out-file "$OUT_DIR/schema-types.ts"

# The generated package depends on kysely only (types are `import type`, so the
# dependency exists to satisfy consumers' type resolution). Versions are read
# from the pipeline pin so they live in exactly one place.
KYSELY_VERSION=$(node -p "require('$PIPELINE_DIR/package.json').devDependencies['kysely']")
TYPESCRIPT_VERSION=$(node -p "require('$PIPELINE_DIR/package.json').devDependencies['typescript']")

cat > "$OUT_DIR/package.json" <<EOF
{
  "name": "@experiencequality/db-client",
  "version": "0.1.0",
  "description": "Generated Kysely Database types for database_schema/schema.sql. Do not edit by hand.",
  "type": "module",
  "main": "./schema-types.ts",
  "types": "./schema-types.ts",
  "exports": {
    ".": "./schema-types.ts"
  },
  "files": [
    "schema-types.ts"
  ],
  "scripts": {
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "kysely": "$KYSELY_VERSION"
  },
  "devDependencies": {
    "typescript": "$TYPESCRIPT_VERSION"
  },
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  }
}
EOF

cat > "$OUT_DIR/tsconfig.json" <<'EOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022"],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noEmit": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "verbatimModuleSyntax": true
  },
  "include": ["schema-types.ts"]
}
EOF

cat > "$OUT_DIR/.gitignore" <<'EOF'
# Install-time artifacts only; the committed artifact is the .ts output itself.
node_modules/
package-lock.json
EOF

echo "generated $OUT_DIR"
