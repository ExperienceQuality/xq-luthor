#!/bin/sh
# gen-db-python.sh -- regenerate SQLAlchemy declarative models from
# database_schema/schema.sql into database_schema/python/xq_db_client/models.py.
#
# Tool (docs/adr/0001-codegen-tools.md): sqlacodegen introspects a *live*
# database, so this script uses the shared preamble scripts/pg-ephemeral.sh
# (pinned postgres image, applies schema.sql, prints a DSN) exactly as-is,
# then runs the pinned codegen toolchain against that DSN.
#
# Pinned toolchain (resolved 2026-10-20 as latest stable on PyPI; mirrored in
# pipeline/python/requirements-pins.txt):
#   sqlacodegen==4.0.4        (released 2026-06-19)
#   sqlalchemy==2.1.5         (released 2026-10-16)
#   psycopg[binary]==3.3.6    (released 2026-09-18; psycopg v3 driver)
# Bump only via a deliberate upgrade PR; the Task 8 regen-diff gate depends on
# these exact pins.
#
# Usage: gen-db-python.sh
set -eu

SQLACODEGEN_VERSION="4.0.4"
SQLALCHEMY_VERSION="2.1.5"
PSYCOPG_VERSION="3.3.6"

SCRIPT_DIR=$(CDPATH='' cd -P "$(dirname "$0")" && pwd)
REPO_ROOT=$(dirname "$SCRIPT_DIR")
cd "$REPO_ROOT"

command -v uv >/dev/null 2>&1 || {
    echo "error: uv not found on PATH" >&2
    exit 1
}

OUT_DIR="database_schema/python"
PKG_DIR="$OUT_DIR/xq_db_client"

# --- ephemeral postgres (shared preamble, do not modify pg-ephemeral.sh) -----

ERR_FILE=$(mktemp)
CONTAINER=""
cleanup() {
    rm -f "$ERR_FILE"
    if [ -n "$CONTAINER" ]; then
        "$SCRIPT_DIR/pg-ephemeral.sh" stop "$CONTAINER" >/dev/null 2>&1 || true
        CONTAINER=""
    fi
}
trap cleanup EXIT
trap 'exit 1' INT TERM

# `start` prints the DSN on stdout and "container: NAME" on stderr.
DSN=$("$SCRIPT_DIR/pg-ephemeral.sh" start 2>"$ERR_FILE")
CONTAINER=$(sed -n 's/^container: //p' "$ERR_FILE")
[ -n "$CONTAINER" ] || {
    echo "error: pg-ephemeral.sh did not report a container name" >&2
    exit 1
}

# --- generate ----------------------------------------------------------------

# Rewrite the scheme so SQLAlchemy uses the psycopg v3 dialect driver.
PSYCOPG_DSN=$(printf '%s' "$DSN" | sed 's|^postgresql://|postgresql+psycopg://|')

mkdir -p "$PKG_DIR"
rm -f "$OUT_DIR/.gitkeep"

uv tool run --from "sqlacodegen==$SQLACODEGEN_VERSION" \
    --with "sqlalchemy==$SQLALCHEMY_VERSION" \
    --with "psycopg[binary]==$PSYCOPG_VERSION" \
    sqlacodegen "$PSYCOPG_DSN" \
    --generator declarative \
    --outfile "$PKG_DIR/models.py"

echo "generated $PKG_DIR/models.py"
