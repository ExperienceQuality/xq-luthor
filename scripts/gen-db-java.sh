#!/bin/sh
# gen-db-java.sh -- regenerate the committed jOOQ database client into
# database_schema/java/src/main/java/com/experiencequality/db.
#
# Tooling (docs/adr/0001-codegen-tools.md): jOOQ codegen (jooq-codegen-maven,
# PostgresDatabase) against an ephemeral REAL Postgres started by the shared
# preamble scripts/pg-ephemeral.sh -- never jOOQ's DDLDatabase, which only
# simulates PostgreSQL DDL and silently mishandles pgcrypto/gen_random_uuid()/
# TIMESTAMPTZ.
#
# Runner: the pinned Maven plugin inside database_schema/java/pom.xml is more
# reproducible than a standalone codegen jar (jOOQ ships no single fat jar;
# Maven resolves the exact pinned dependency graph with Central checksums).
# Codegen lives in a Maven profile activated by -Ddb.url, so a plain
# `mvn compile` for consumers just compiles the committed sources.
#
# Resolved pins (recorded at pipeline-build time 2026-10; bump only via a
# deliberate upgrade PR -- the regen-diff gate depends on them):
#   Generator     : org.jooq:jooq-codegen-maven:3.21.9 (latest stable at pin
#                   time; plugin + org.jooq:jooq runtime dep pinned in pom.xml)
#   JDBC driver   : org.postgresql:postgresql:42.7.14 (plugin dependency)
#   JDK toolchain : OpenJDK 21 (JAVA_HOME or PATH)
#   Maven         : mvn on PATH, else tools/apache-maven-3.9.16/bin/mvn
#                   (downloaded, checksum-verified, gitignored)
#   Postgres image: pinned inside scripts/pg-ephemeral.sh (shared; not editable
#                   from this task)
#
# Usage: gen-db-java.sh
set -eu

die() { echo "error: $*" >&2; exit 1; }

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(dirname "$SCRIPT_DIR")
cd "$ROOT"

POM="database_schema/java/pom.xml"
GEN_DIR="database_schema/java/src/main/java/com/experiencequality/db"

[ -f "$POM" ] || die "missing $POM"

# --- toolchain selection -----------------------------------------------------
if command -v mvn >/dev/null 2>&1; then
    MVN="mvn"
elif [ -x "$ROOT/tools/apache-maven-3.9.16/bin/mvn" ]; then
    MVN="$ROOT/tools/apache-maven-3.9.16/bin/mvn"
else
    die "mvn not on PATH and tools/apache-maven-3.9.16/bin/mvn is missing"
fi
command -v java >/dev/null 2>&1 || [ -n "${JAVA_HOME:-}" ] \
    || die "java (JDK 21) is required"
echo "maven: $MVN" >&2

# Bounded check not needed when using embedded Postgres via pg-ephemeral.sh

# --- shared ephemeral Postgres preamble (ADR 0001; do not edit pg-ephemeral.sh)
# start prints the DSN on stdout and "container: NAME" on stderr; the caller is
# responsible for `stop` -- done via trap so the container dies on every exit.
CONTAINER=""
cleanup() {
    if [ -n "$CONTAINER" ]; then
        "$SCRIPT_DIR/pg-ephemeral.sh" stop "$CONTAINER" || true
    fi
}
trap cleanup EXIT
trap 'exit 1' INT TERM

ERR_FILE=$(mktemp "${TMPDIR:-/tmp}/gen-db-java.XXXXXX")
if ! DSN=$("$SCRIPT_DIR/pg-ephemeral.sh" start 2>"$ERR_FILE"); then
    cat "$ERR_FILE" >&2 || true
    rm -f "$ERR_FILE"
    exit 1
fi
CONTAINER=$(sed -n 's/^container: //p' "$ERR_FILE" | head -n 1)
rm -f "$ERR_FILE"
[ -n "$CONTAINER" ] || die "pg-ephemeral.sh did not report a container name"
echo "ephemeral postgres: $CONTAINER" >&2

# postgresql://user:pass@host:port/db -> jdbc:postgresql://host:port/db + creds
DSN_REST=${DSN#*://}
DB_USER=${DSN_REST%%:*}
DSN_REST2=${DSN_REST#*:}
DB_PASS=${DSN_REST2%%@*}
HOST_DB=${DSN_REST#*@}
[ -n "$DB_USER" ] && [ -n "$HOST_DB" ] || die "could not parse DSN: $DSN"
JDBC_URL="jdbc:postgresql://$HOST_DB"
echo "jdbc: $JDBC_URL" >&2

# --- generate ----------------------------------------------------------------
# Remove previously generated sources so dropped objects cannot go stale
# (generated dirs are never hand-edited -- docs/contracts-conventions.md).
rm -rf "$GEN_DIR"

"$MVN" -q -f "$POM" \
    -Ddb.url="$JDBC_URL" \
    -Ddb.user="$DB_USER" \
    -Ddb.password="$DB_PASS" \
    generate-sources

[ -d "$GEN_DIR" ] || die "codegen produced no output at $GEN_DIR"
echo "generated: $GEN_DIR" >&2
