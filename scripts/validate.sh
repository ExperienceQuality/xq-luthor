#!/bin/sh
# validate.sh -- contract validation gate (Task 8). Single entrypoint for CI
# and local runs; exits non-zero on any failure.
#
# Check 1 -- contract lint:
#   * every openapi/<service>/openapi.yaml is a valid OpenAPI 3.x spec
#     (pinned validator: openapi-spec-validator==0.7.2 via `uv tool run`;
#     pin also recorded in pipeline/python/requirements-pins.txt)
#   * <service> dir name is lowercase kebab-case
#   * info.version has a matching v<info.version>/ dir containing
#     {nodejs,python,java}/ subdirectories
#
# Check 2 -- regeneration-diff:
#   * re-run all gen-openapi-*.sh pipelines against the current contracts
#     (the v<info.version> dir of each service)
#   * `git diff --exit-code -- openapi/` must be empty and
#     `git status --porcelain` must show no untracked files under openapi/.
#     Any diff or untracked file = committed output drifted from the contract.
#
# Usage: scripts/validate.sh
set -eu

SPEC_VALIDATOR_VERSION="0.7.2"

die() { echo "error: $*" >&2; exit 1; }
say() { echo "==> $*" >&2; }

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(dirname "$SCRIPT_DIR")
cd "$ROOT"

command -v uv >/dev/null 2>&1 || die "uv not found on PATH"
command -v git >/dev/null 2>&1 || die "git not found on PATH"

# --- Check 1: OpenAPI contract lint ------------------------------------------
say "linting OpenAPI contracts"

# service<tab>version pairs to regenerate in check 2.
PAIRS_FILE=$(mktemp "${TMPDIR:-/tmp}/xq-validate.XXXXXX")
trap 'rm -f "$PAIRS_FILE"' EXIT
trap 'exit 1' INT TERM

for SPEC in openapi/*/openapi.yaml; do
    [ -f "$SPEC" ] || die "no contracts found matching openapi/*/openapi.yaml"
    SERVICE_DIR=$(dirname "$SPEC")
    SERVICE=${SERVICE_DIR#openapi/}

    case "$SERVICE" in
        *[!a-z0-9-]*|*--*|''|-*|*-)
            die "service directory '$SERVICE' is not lowercase kebab-case (docs/contracts-conventions.md)" ;;
    esac

    say "validating $SPEC"
    uv tool run --from "openapi-spec-validator==$SPEC_VALIDATOR_VERSION" \
        openapi-spec-validator --schema detect "$SPEC" \
        || die "OpenAPI validation failed: $SPEC"

    INFO_VERSION=$(awk '
        /^info:/ { in_info=1; next }
        in_info && /^[^[:space:]]/ { in_info=0 }
        in_info && /^[[:space:]]+version:[[:space:]]*/ { sub(/^[[:space:]]*version:[[:space:]]*/, ""); gsub(/["'"'"'[:space:]]/, ""); print; exit }
    ' "$SPEC")
    [ -n "$INFO_VERSION" ] || die "could not read info.version from $SPEC"

    VERSION_DIR="$SERVICE_DIR/v$INFO_VERSION"
    [ -d "$VERSION_DIR" ] \
        || die "info.version $INFO_VERSION in $SPEC has no matching dir $VERSION_DIR"
    for lang in nodejs python java; do
        [ -d "$VERSION_DIR/$lang" ] \
            || die "missing generated dir $VERSION_DIR/$lang"
    done

    printf '%s\t%s\n' "$SERVICE" "v$INFO_VERSION" >> "$PAIRS_FILE"
done

# --- Check 2: regeneration-diff ----------------------------------------------
say "regenerating clients (regen-diff check)"

while IFS="$(printf '\t')" read -r SERVICE VERSION; do
    [ -n "$SERVICE" ] || continue
    ./scripts/gen-openapi-nodejs.sh --service "$SERVICE" --version "$VERSION"
    ./scripts/gen-openapi-python.sh --service "$SERVICE" --version "$VERSION" --force
    ./scripts/gen-openapi-java.sh --service "$SERVICE" --version "$VERSION"
done < "$PAIRS_FILE"
rm -f "$PAIRS_FILE"

say "checking for committed/generated drift"
DIFF_FILE=$(mktemp "${TMPDIR:-/tmp}/xq-validate-diff.XXXXXX")
STATUS=0
git diff --exit-code -- openapi/ > "$DIFF_FILE" || STATUS=$?
if [ "$STATUS" -ne 0 ]; then
    cat "$DIFF_FILE" >&2
    rm -f "$DIFF_FILE"
    die "generated output drifted from contracts; re-run the gen-openapi-*.sh pipelines and commit the result (diff above)"
fi
rm -f "$DIFF_FILE"

UNTRACKED=$(git status --porcelain -- openapi/ | grep '^??' || true)
if [ -n "$UNTRACKED" ]; then
    printf '%s\n' "$UNTRACKED" >&2
    die "untracked files under openapi/; commit regenerated output or remove strays"
fi

say "contract validation passed"