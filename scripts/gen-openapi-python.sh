#!/bin/sh
# gen-openapi-python.sh -- regenerate the Python client for one OpenAPI
# service/version into openapi/<service>/<version>/python/.
#
# Tool (docs/adr/0001-codegen-tools.md): openapi-python-client
#   Emits a complete httpx-based package with its own pyproject.toml
#   (`--meta uv` selects the uv_build backend), matching the `uv` git-install
#   distribution model in docs/contracts-conventions.md.
#
# Pinned tool version: openapi-python-client==0.29.1
#   Resolved 2026-10-20 as the latest stable release on PyPI
#   (0.29.1 released 2026-08-30). Bump only via a deliberate upgrade PR;
#   the Task 8 regen-diff gate depends on this exact pin.
#
# Usage: gen-openapi-python.sh --service NAME --version vX.Y.Z [--force]
#
#   --service NAME   service directory under openapi/ (lowercase kebab-case)
#   --version vX.Y.Z target version dir; must equal info.version in
#                    openapi/<service>/openapi.yaml plus the `v` prefix
#   --force          allow overwriting an existing generated client
#                    (version dirs are immutable once published; only use
#                    for pre-release regeneration)
set -eu

TOOL_VERSION="0.29.1"

usage() {
    sed -n '2,/^set -eu/p' "$0" | sed 's/^# \{0,1\}//; /^set -eu/d' >&2
    exit 2
}

SERVICE=""
VERSION=""
FORCE=0

while [ $# -gt 0 ]; do
    case "$1" in
        --service)
            [ $# -ge 2 ] || usage
            SERVICE=$2
            shift 2
            ;;
        --version)
            [ $# -ge 2 ] || usage
            VERSION=$2
            shift 2
            ;;
        --force)
            FORCE=1
            shift
            ;;
        *)
            usage
            ;;
    esac
done

[ -n "$SERVICE" ] && [ -n "$VERSION" ] || usage

# Resolve repo root so the script works from any cwd.
SCRIPT_DIR=$(CDPATH='' cd -P "$(dirname "$0")" && pwd)
REPO_ROOT=$(dirname "$SCRIPT_DIR")
cd "$REPO_ROOT"

# --- validation -------------------------------------------------------------

printf '%s' "$SERVICE" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' || {
    echo "error: --service '$SERVICE' must be lowercase kebab-case" >&2
    exit 1
}

printf '%s' "$VERSION" | grep -Eq '^v[0-9]+\.[0-9]+\.[0-9]+$' || {
    echo "error: --version '$VERSION' must be semver with a v prefix (vX.Y.Z)" >&2
    exit 1
}

SPEC="openapi/$SERVICE/openapi.yaml"
[ -f "$SPEC" ] || {
    echo "error: contract not found: $SPEC" >&2
    exit 1
}

command -v uv >/dev/null 2>&1 || {
    echo "error: uv not found on PATH" >&2
    exit 1
}

# docs/contracts-conventions.md: <version> must equal info.version plus `v`.
SPEC_VERSION=$(sed -n '/^info:/,/^[a-z]/p' "$SPEC" \
    | sed -n 's/^  *version:[[:space:]]*//p' \
    | head -n 1 | tr -d "\"'")
if [ -z "$SPEC_VERSION" ]; then
    echo "warning: could not parse info.version from $SPEC; skipping version check" >&2
elif [ "v$SPEC_VERSION" != "$VERSION" ]; then
    echo "error: --version $VERSION does not match info.version $SPEC_VERSION (+v) in $SPEC" >&2
    exit 1
fi

# --- generate ---------------------------------------------------------------

OUT_DIR="openapi/$SERVICE/$VERSION/python"
PKG_MODULE=$(printf '%s' "$SERVICE" | tr '-' '_')

if [ -f "$OUT_DIR/pyproject.toml" ] && [ "$FORCE" -ne 1 ]; then
    echo "error: $OUT_DIR already contains a generated client." >&2
    echo "       Version dirs are immutable once published; pass --force only for pre-release regen." >&2
    exit 1
fi

TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT INT TERM

# Tool-supported naming overrides (not a hand-edit of generated source):
#   distribution name: xq-<service>-client   import package: xq_<service>_client
cat > "$TMP_DIR/config.yaml" <<EOF
project_name_override: xq-$SERVICE-client
package_name_override: xq_${PKG_MODULE}_client
EOF

uv tool run --from "openapi-python-client==$TOOL_VERSION" \
    openapi-python-client generate \
    --path "$SPEC" \
    --meta uv \
    --config "$TMP_DIR/config.yaml" \
    --output-path "$TMP_DIR/gen"

# The generator runs ruff post-gen and leaves its cache inside the output;
# drop it so committed output stays clean and deterministic.
rm -rf "$TMP_DIR/gen/.ruff_cache"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"
cp -R "$TMP_DIR/gen/." "$OUT_DIR/"

echo "generated xq-$SERVICE-client ($VERSION) -> $OUT_DIR"
