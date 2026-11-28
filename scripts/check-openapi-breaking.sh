#!/bin/sh
# check-openapi-breaking.sh — fail when the current contract introduces breaking
# deltas vs the previously published version, or when a published version dir
# receives a generator/call-shape change in place.
#
# Baseline (per service):
#   For openapi/<service>/openapi.yaml at info.version V, find the largest
#   openapi/<service>/vX.Y.Z/ with X.Y.Z < V. Use that dir's committed
#   java/api/openapi.yaml (openapi-generator snapshot of the published contract)
#   as the prior YAML. Services with no prior version are skipped.
#
# Breaking HTTP/OpenAPI deltas (align with docs/contracts-conventions.md
# Versioning — read-only reference): path/method removal, operationId rename,
# required request field/param added, auth added/tightened, success status
# removed, response property removal, pagination-shaped property churn.
# Allowed only when the current MAJOR is greater than the prior MAJOR.
# Note: component schema *name* diffs are ignored — openapi-generator snapshots
# invent nested names (e.g. Problem_violations_inner) absent from hand-authored
# YAML; consumer-facing renames still surface via operationId / properties.
#
# Generator/call-shape gate:
#   Published nodejs trees with semver < 1.2.0 must stay on the ADR 0001
#   (openapi-fetch) shape; semver >= 1.2.0 must use ADR 0002 (@hey-api/openapi-ts).
#   Applying hey-api under v1.0.0/v1.1.0 (or legacy under >=1.2.0) fails.
#
# Usage: scripts/check-openapi-breaking.sh
# Deps: node (semver sort), uv + PyYAML 6.0.2 (via `uv run --no-project --with`).
set -eu

PYYAML_VERSION="6.0.2"
HEY_API_MIN="1.2.0"

die() { echo "error: $*" >&2; exit 1; }
say() { echo "==> $*" >&2; }

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(dirname "$SCRIPT_DIR")
cd "$ROOT"

command -v node >/dev/null 2>&1 || die "node not found on PATH"
command -v uv >/dev/null 2>&1 || die "uv not found on PATH"

# Read info.version from a hand-authored or generated OpenAPI YAML.
read_info_version() {
    awk '
        /^info:/ { in_info=1; next }
        in_info && /^[^[:space:]]/ { in_info=0 }
        in_info && /^[[:space:]]+version:[[:space:]]*/ {
            sub(/^[[:space:]]+version:[[:space:]]*/, "")
            gsub(/["'"'"'[:space:]]/, "")
            print
            exit
        }
    ' "$1"
}

# Semver compare: exit 0 if $1 < $2, else 1. Args are bare X.Y.Z (no v).
semver_lt() {
    node -e '
const a = process.argv[1].split(/[.+]/).slice(0, 3).map(Number);
const b = process.argv[2].split(/[.+]/).slice(0, 3).map(Number);
const lt = a[0] < b[0] || (a[0] === b[0] && (a[1] < b[1] || (a[1] === b[1] && a[2] < b[2])));
process.exit(lt ? 0 : 1);
' "$1" "$2"
}

semver_gte() {
    node -e '
const a = process.argv[1].split(/[.+]/).slice(0, 3).map(Number);
const b = process.argv[2].split(/[.+]/).slice(0, 3).map(Number);
const gte = a[0] > b[0] || (a[0] === b[0] && (a[1] > b[1] || (a[1] === b[1] && a[2] >= b[2])));
process.exit(gte ? 0 : 1);
' "$1" "$2"
}

# Largest published vX.Y.Z under $1 strictly less than bare version $2; prints vX.Y.Z or empty.
find_previous_version_dir() {
    SERVICE_DIR=$1
    CURRENT=$2
    BEST=
    BEST_BARE=
    for D in "$SERVICE_DIR"/v*/; do
        [ -d "$D" ] || continue
        BASE=$(basename "$D")
        case "$BASE" in
            v[0-9]*.[0-9]*.[0-9]*) ;;
            *) continue ;;
        esac
        BARE=${BASE#v}
        if semver_lt "$BARE" "$CURRENT"; then
            if [ -z "$BEST_BARE" ] || semver_lt "$BEST_BARE" "$BARE"; then
                BEST=$BASE
                BEST_BARE=$BARE
            fi
        fi
    done
    printf '%s' "$BEST"
}

# --- Check A: generator/call-shape on published version dirs -------------------
say "checking published client call-shapes (generator immutability)"

for NODE_PKG in openapi/*/v*/nodejs/package.json; do
    [ -f "$NODE_PKG" ] || continue
    NODE_DIR=$(dirname "$NODE_PKG")
    VERSION_DIR=$(dirname "$NODE_DIR")
    SERVICE_DIR=$(dirname "$VERSION_DIR")
    SERVICE=${SERVICE_DIR#openapi/}
    VER_BASE=$(basename "$VERSION_DIR")
    BARE=${VER_BASE#v}

    HAS_HEY=0
    HAS_LEGACY=0
    if grep -q '@hey-api/openapi-ts' "$NODE_PKG" 2>/dev/null \
        || [ -f "$NODE_DIR/openapi-ts.config.ts" ] \
        || [ -f "$NODE_DIR/src/sdk.gen.ts" ]; then
        HAS_HEY=1
    fi
    if grep -q 'openapi-fetch' "$NODE_PKG" 2>/dev/null \
        || [ -f "$NODE_DIR/schema.ts" ]; then
        HAS_LEGACY=1
    fi

    if semver_gte "$BARE" "$HEY_API_MIN"; then
        if [ "$HAS_HEY" -ne 1 ]; then
            die "$SERVICE $VER_BASE/nodejs: expected ADR 0002 (@hey-api/openapi-ts) call shape for semver >= $HEY_API_MIN"
        fi
        if [ "$HAS_LEGACY" -eq 1 ] && [ "$HAS_HEY" -ne 1 ]; then
            die "$SERVICE $VER_BASE/nodejs: legacy openapi-fetch markers without hey-api for semver >= $HEY_API_MIN"
        fi
    else
        if [ "$HAS_HEY" -eq 1 ]; then
            die "$SERVICE $VER_BASE/nodejs: hey-api/call-shape change applied to published version < $HEY_API_MIN (cut a new version dir instead; see docs/contracts-conventions.md Versioning)"
        fi
        if [ "$HAS_LEGACY" -ne 1 ]; then
            die "$SERVICE $VER_BASE/nodejs: expected ADR 0001 (openapi-fetch) call shape for semver < $HEY_API_MIN"
        fi
    fi
done

# --- Check B: OpenAPI breaking deltas vs previous published YAML --------------
say "checking OpenAPI breaking changes vs previous published versions"

BREAK_HELPER=$(mktemp "${TMPDIR:-/tmp}/xq-openapi-breaking.XXXXXX.py")
trap 'rm -f "$BREAK_HELPER"' EXIT
trap 'exit 1' INT TERM

cat > "$BREAK_HELPER" <<'PY'
"""Semantic OpenAPI breaking-delta checker (pragmatic, no network)."""
from __future__ import annotations

import sys
from typing import Any

import yaml

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
PAGINATION_KEYS = {
    "offset",
    "limit",
    "cursor",
    "next",
    "nextcursor",
    "next_cursor",
    "page",
    "pagesize",
    "page_size",
    "total",
    "totalcount",
    "total_count",
    "items",
    "results",
    "data",
}


def load(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    if not isinstance(doc, dict):
        raise SystemExit(f"error: not a mapping: {path}")
    return doc


def resolve_ref(doc: dict[str, Any], node: Any) -> Any:
    if not isinstance(node, dict) or "$ref" not in node:
        return node
    ref = node["$ref"]
    if not isinstance(ref, str) or not ref.startswith("#/"):
        return node
    cur: Any = doc
    for part in ref[2:].split("/"):
        if not isinstance(cur, dict) or part not in cur:
            return node
        cur = cur[part]
    return cur


def schema_required(doc: dict[str, Any], schema: Any) -> set[str]:
    resolved = resolve_ref(doc, schema)
    if not isinstance(resolved, dict):
        return set()
    req = resolved.get("required") or []
    if not isinstance(req, list):
        return set()
    return {str(x) for x in req}


def schema_props(doc: dict[str, Any], schema: Any) -> set[str]:
    resolved = resolve_ref(doc, schema)
    if not isinstance(resolved, dict):
        return set()
    props = resolved.get("properties") or {}
    if not isinstance(props, dict):
        return set()
    return set(props.keys())


def pagination_props(doc: dict[str, Any], schema: Any) -> set[str]:
    return {p.lower() for p in schema_props(doc, schema) if p.lower() in PAGINATION_KEYS}


def security_names(sec: Any) -> set[str]:
    """Flatten OpenAPI security requirements to scheme names."""
    if not sec:
        return set()
    if not isinstance(sec, list):
        return set()
    names: set[str] = set()
    for req in sec:
        if isinstance(req, dict):
            names.update(str(k) for k in req.keys())
    return names


def op_map(path_item: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(path_item, dict):
        return {}
    out: dict[str, dict[str, Any]] = {}
    for method, op in path_item.items():
        if method.lower() in HTTP_METHODS and isinstance(op, dict):
            out[method.lower()] = op
    return out


def json_schema(doc: dict[str, Any], op: dict[str, Any], which: str) -> Any:
    """which: 'request' | response status code string."""
    if which == "request":
        rb = op.get("requestBody")
        if not isinstance(rb, dict):
            return None
        content = rb.get("content") or {}
        if not isinstance(content, dict):
            return None
        for ctype in ("application/json", "application/yaml", "*/*"):
            if ctype in content and isinstance(content[ctype], dict):
                return content[ctype].get("schema")
        # first content schema
        for body in content.values():
            if isinstance(body, dict) and "schema" in body:
                return body.get("schema")
        return None
    responses = op.get("responses") or {}
    if not isinstance(responses, dict):
        return None
    resp = responses.get(which)
    if not isinstance(resp, dict):
        # try $ref response
        resp = resolve_ref(doc, resp) if resp is not None else None
        if not isinstance(resp, dict):
            return None
    content = resp.get("content") or {}
    if not isinstance(content, dict):
        return None
    for ctype in ("application/json", "application/yaml", "*/*"):
        if ctype in content and isinstance(content[ctype], dict):
            return content[ctype].get("schema")
    for body in content.values():
        if isinstance(body, dict) and "schema" in body:
            return body.get("schema")
    return None


def param_key(p: dict[str, Any]) -> str:
    return f"{p.get('in', '')}:{p.get('name', '')}"


def collect_params(doc: dict[str, Any], path_item: dict[str, Any], op: dict[str, Any]) -> dict[str, dict[str, Any]]:
    params: dict[str, dict[str, Any]] = {}
    for src in (path_item.get("parameters") or [], op.get("parameters") or []):
        if not isinstance(src, list):
            continue
        for raw in src:
            p = resolve_ref(doc, raw)
            if isinstance(p, dict) and "name" in p:
                params[param_key(p)] = p
    return params


def success_statuses(op: dict[str, Any]) -> set[str]:
    responses = op.get("responses") or {}
    if not isinstance(responses, dict):
        return set()
    out: set[str] = set()
    for code in responses.keys():
        s = str(code)
        if s.startswith("2") or s == "default":
            out.add(s)
    return out


def compare(old: dict[str, Any], new: dict[str, Any]) -> list[str]:
    findings: list[str] = []

    old_paths = old.get("paths") or {}
    new_paths = new.get("paths") or {}
    if not isinstance(old_paths, dict):
        old_paths = {}
    if not isinstance(new_paths, dict):
        new_paths = {}

    for path in sorted(set(old_paths) - set(new_paths)):
        findings.append(f"path removed: {path}")

    # Global auth added / tightened
    old_sec = security_names(old.get("security"))
    new_sec = security_names(new.get("security"))
    if not old_sec and new_sec:
        findings.append(f"global auth added: {sorted(new_sec)}")
    elif old_sec and new_sec - old_sec:
        findings.append(f"global auth schemes added: {sorted(new_sec - old_sec)}")

    for path in sorted(set(old_paths) & set(new_paths)):
        old_item = old_paths[path] if isinstance(old_paths[path], dict) else {}
        new_item = new_paths[path] if isinstance(new_paths[path], dict) else {}
        old_ops = op_map(old_item)
        new_ops = op_map(new_item)

        for method in sorted(set(old_ops) - set(new_ops)):
            findings.append(f"method removed: {method.upper()} {path}")

        for method in sorted(set(old_ops) & set(new_ops)):
            o = old_ops[method]
            n = new_ops[method]
            loc = f"{method.upper()} {path}"

            oid_o = o.get("operationId")
            oid_n = n.get("operationId")
            if oid_o and oid_n and oid_o != oid_n:
                findings.append(f"operationId renamed: {loc} {oid_o!r} -> {oid_n!r}")
            elif oid_o and not oid_n:
                findings.append(f"operationId removed: {loc} {oid_o!r}")

            # Operation-level auth: empty list means optional; absent inherits global.
            if "security" in o or "security" in n:
                o_sec = security_names(o.get("security")) if "security" in o else None
                n_sec = security_names(n.get("security")) if "security" in n else None
                # Newly required auth on an operation that was explicitly public
                if o_sec == set() and n_sec:
                    findings.append(f"auth added on operation: {loc} schemes={sorted(n_sec)}")
                elif o_sec is not None and n_sec is not None and n_sec - o_sec:
                    findings.append(f"auth schemes added on operation: {loc} {sorted(n_sec - o_sec)}")
                elif o_sec is None and n_sec and not old_sec:
                    # inherited no global auth before; now operation requires auth
                    findings.append(f"auth added on operation: {loc} schemes={sorted(n_sec)}")

            old_params = collect_params(old, old_item, o)
            new_params = collect_params(new, new_item, n)
            for key, p in sorted(new_params.items()):
                if key not in old_params and p.get("required") is True:
                    findings.append(f"required parameter added: {loc} {key}")
            for key, p in sorted(old_params.items()):
                if key not in new_params:
                    findings.append(f"parameter removed: {loc} {key}")
                else:
                    # newly required
                    if p.get("required") is not True and new_params[key].get("required") is True:
                        findings.append(f"parameter became required: {loc} {key}")

            old_req_schema = json_schema(old, o, "request")
            new_req_schema = json_schema(new, n, "request")
            if old_req_schema is not None or new_req_schema is not None:
                old_req = schema_required(old, old_req_schema) if old_req_schema is not None else set()
                new_req = schema_required(new, new_req_schema) if new_req_schema is not None else set()
                for field in sorted(new_req - old_req):
                    findings.append(f"required request field added: {loc} {field}")

            old_success = success_statuses(o)
            new_success = success_statuses(n)
            for code in sorted(old_success - new_success):
                findings.append(f"success status removed: {loc} {code}")

            # Compare response bodies for shared success codes
            for code in sorted(old_success & new_success):
                if code == "default":
                    continue
                old_s = json_schema(old, o, code)
                new_s = json_schema(new, n, code)
                if old_s is None:
                    continue
                old_props = schema_props(old, old_s)
                new_props = schema_props(new, new_s) if new_s is not None else set()
                for prop in sorted(old_props - new_props):
                    findings.append(f"response property removed: {loc} {code} {prop}")
                old_page = pagination_props(old, old_s)
                new_page = pagination_props(new, new_s) if new_s is not None else set()
                if old_page and new_page and old_page != new_page:
                    findings.append(
                        f"pagination shape changed: {loc} {code} {sorted(old_page)} -> {sorted(new_page)}"
                    )

            # Documented error status removal
            old_resp = set(str(c) for c in (o.get("responses") or {}).keys())
            new_resp = set(str(c) for c in (n.get("responses") or {}).keys())
            for code in sorted(old_resp - new_resp):
                if code.startswith("4") or code.startswith("5"):
                    findings.append(f"error status removed: {loc} {code}")

    return findings


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: check_breaking.py <old.yaml> <new.yaml>")
    old = load(sys.argv[1])
    new = load(sys.argv[2])
    findings = compare(old, new)
    if findings:
        for line in findings:
            print(f"BREAKING: {line}")
        raise SystemExit(2)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
PY

BREAKING_FAILED=0

for SPEC in openapi/*/openapi.yaml; do
    [ -f "$SPEC" ] || die "no contracts found matching openapi/*/openapi.yaml"
    SERVICE_DIR=$(dirname "$SPEC")
    SERVICE=${SERVICE_DIR#openapi/}

    INFO_VERSION=$(read_info_version "$SPEC")
    [ -n "$INFO_VERSION" ] || die "could not read info.version from $SPEC"

    PREV_DIR_NAME=$(find_previous_version_dir "$SERVICE_DIR" "$INFO_VERSION")
    if [ -z "$PREV_DIR_NAME" ]; then
        say "$SERVICE@$INFO_VERSION: no previous published version; skipping breaking YAML diff"
        continue
    fi

    BASELINE="$SERVICE_DIR/$PREV_DIR_NAME/java/api/openapi.yaml"
    [ -f "$BASELINE" ] \
        || die "$SERVICE: previous version $PREV_DIR_NAME has no java/api/openapi.yaml baseline"

    PREV_BARE=${PREV_DIR_NAME#v}
    say "$SERVICE: comparing $PREV_DIR_NAME -> $INFO_VERSION"

    set +e
    OUT=$(uv run --no-project --with "pyyaml==$PYYAML_VERSION" python "$BREAK_HELPER" "$BASELINE" "$SPEC" 2>&1)
    STATUS=$?
    set -e

    if [ "$STATUS" -eq 0 ]; then
        say "$SERVICE: no breaking deltas vs $PREV_DIR_NAME"
        continue
    fi
    if [ "$STATUS" -ne 2 ]; then
        printf '%s\n' "$OUT" >&2
        die "$SERVICE: breaking-change checker failed (exit $STATUS)"
    fi

    # Breaking deltas found — allow only across a MAJOR bump.
    CUR_MAJOR=${INFO_VERSION%%.*}
    PREV_MAJOR=${PREV_BARE%%.*}
    printf '%s\n' "$OUT" >&2
    if [ "$CUR_MAJOR" -gt "$PREV_MAJOR" ]; then
        say "$SERVICE: breaking deltas allowed (MAJOR $PREV_MAJOR -> $CUR_MAJOR)"
        continue
    fi

    echo "error: $SERVICE@$INFO_VERSION has breaking changes vs published $PREV_DIR_NAME; bump MAJOR (see docs/contracts-conventions.md Versioning)" >&2
    BREAKING_FAILED=1
done

rm -f "$BREAK_HELPER"

[ "$BREAKING_FAILED" -eq 0 ] || exit 1
say "openapi breaking-change check passed"
