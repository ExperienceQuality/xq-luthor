#!/bin/sh
# POSIX sh wrapper for ephemeral Postgres.
# Runs scripts/pg-ephemeral.py via uv with pinned postgresql-binaries==16.15.0.
# No Docker required!
set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
exec uv run --with 'postgresql-binaries==16.15.0' python "$SCRIPT_DIR/pg-ephemeral.py" "$@"
