#!/bin/sh
# gen-openapi-java.sh — generate the committed Java client for an OpenAPI contract.
#
# Tooling (docs/adr/0001-codegen-tools.md): openapi-generator `java` generator with
# library=okhttp-gson (no Spring). Consumes openapi/<service>/openapi.yaml directly;
# no ephemeral database is involved.
#
# Resolved pins (recorded at pipeline-build time 2026-10; bump only via a
# deliberate upgrade PR):
#   Generator release : openapi-generator-cli 7.26.0 (latest stable at pin time)
#   Docker image      : ghcr.io/experiencequality/openapi-generator-cli
#                       @sha256:a304ddf1e2e5f24f68fa3153568d6174cea4959d09aa8e3db6d526fd0782326d
#                       (multi-arch manifest digest for tag v7.26.0, amd64+arm64;
#                       mirrored digest-for-digest from Docker Hub
#                       openapitools/openapi-generator-cli by
#                       .github/workflows/mirror-images.yml)
#   CLI jar (fallback): https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.26.0/openapi-generator-cli-7.26.0.jar
#                       sha256=1760050094997b9cc790cc1350be095f15da8c08a996b184d3eadc4ccda5e35e
#                       sha1  =b96b148fcf482808037f68fbad99cb4d7e65d40b (matches Maven Central)
#   JDK toolchain     : verified with OpenJDK 21
#
# Runner selection: the digest-pinned Docker image is preferred (most
# reproducible). If no working Docker daemon is reachable within 10s, the
# checksum-verified CLI jar under tools/ (gitignored) is used instead. No
# Maven-installed plugin is required.
#
# Output: openapi/<service>/<version>/java/ — a Maven-packageable client with
# groupId com.experiencequality, artifactId <service>-client, version <semver>
# (the --version argument minus the 'v' prefix) and distributionManagement
# pointing at GitHub Packages.
#
# Usage:
#   gen-openapi-java.sh --service NAME --version vX.Y.Z [--spec PATH]
#
#   --service NAME   kebab-case service name (e.g. example)
#   --version vX.Y.Z v-prefixed semver; must equal info.version + 'v' prefix
#   --spec PATH      optional spec override (default openapi/<service>/openapi.yaml);
#                    useful to preview output before a contract change lands.
set -eu

die() { echo "error: $*" >&2; exit 1; }
usage() { sed -n '2,/^set -eu/p' "$0" | sed 's/^# \{0,1\}//; s/^#$//' | head -n -1; exit "${1:-2}"; }

# --- pinned tool coordinates -------------------------------------------------
OGEN_VERSION="7.26.0"
OGEN_IMAGE="ghcr.io/experiencequality/openapi-generator-cli@sha256:a304ddf1e2e5f24f68fa3153568d6174cea4959d09aa8e3db6d526fd0782326d"
OGEN_JAR_URL="https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OGEN_VERSION}/openapi-generator-cli-${OGEN_VERSION}.jar"
OGEN_JAR_SHA256="1760050094997b9cc790cc1350be095f15da8c08a996b184d3eadc4ccda5e35e"
GH_PACKAGES_URL="https://maven.pkg.github.com/ExperienceQuality/xq-luthor"

# --- args --------------------------------------------------------------------
SERVICE=""
VERSION=""
SPEC_OVERRIDE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --service) [ $# -ge 2 ] || die "--service requires a value"; SERVICE=$2; shift 2 ;;
    --version) [ $# -ge 2 ] || die "--version requires a value"; VERSION=$2; shift 2 ;;
    --spec)    [ $# -ge 2 ] || die "--spec requires a value";    SPEC_OVERRIDE=$2; shift 2 ;;
    -h|--help) usage 0 ;;
    *) die "unknown argument: $1" ;;
  esac
done

[ -n "$SERVICE" ] || die "--service is required"
[ -n "$VERSION" ] || die "--version is required"
echo "$SERVICE" | grep -qE '^[a-z0-9]+(-[a-z0-9]+)*$' \
  || die "service name '$SERVICE' is not lowercase kebab-case (docs/contracts-conventions.md)"
echo "$VERSION" | grep -qE '^v[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$' \
  || die "version '$VERSION' is not v-prefixed semver vX.Y.Z"
ARTIFACT_VERSION="${VERSION#v}"

# --- paths -------------------------------------------------------------------
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(dirname "$SCRIPT_DIR")
cd "$ROOT"

SERVICE_REL="openapi/$SERVICE"
OUT_REL="$SERVICE_REL/$VERSION/java"
OUT_ABS="$ROOT/$OUT_REL"

if [ -n "$SPEC_OVERRIDE" ]; then
  case "$SPEC_OVERRIDE" in
    /*) SPEC_ABS=$SPEC_OVERRIDE ;;
    *)  SPEC_ABS="$PWD/$SPEC_OVERRIDE" ;;
  esac
else
  SPEC_ABS="$ROOT/$SERVICE_REL/openapi.yaml"
fi
[ -f "$SPEC_ABS" ] || die "spec not found: $SPEC_ABS"
[ -d "$ROOT/$SERVICE_REL" ] || die "service directory not found: $SERVICE_REL"

# contracts-conventions: <version> must equal info.version + 'v' prefix
SPEC_VERSION=$(awk '
  /^info:/ { in_info=1; next }
  in_info && /^[^[:space:]]/ { in_info=0 }
  in_info && /^[[:space:]]+version:[[:space:]]*/ { sub(/^[[:space:]]*version:[[:space:]]*/, ""); gsub(/["'"'"'[:space:]]/, ""); print; exit }
' "$SPEC_ABS")
[ -n "$SPEC_VERSION" ] || die "could not read info.version from $SPEC_ABS"
[ "$SPEC_VERSION" = "$ARTIFACT_VERSION" ] \
  || die "version mismatch: --version $VERSION implies $ARTIFACT_VERSION but spec info.version is $SPEC_VERSION"

if grep -qE '^paths:[[:space:]]*\{[[:space:]]*\}[[:space:]]*$' "$SPEC_ABS"; then
  echo "warning: spec has 'paths: {}' — generated client will contain no API classes" >&2
fi

# java package base: kebab-case service -> alnum segment under com.experiencequality
PKG_SEGMENT=$(echo "$SERVICE" | tr -d '-')
PKG_BASE="com.experiencequality.$PKG_SEGMENT"

# --- runner selection --------------------------------------------------------
docker_usable() {
  command -v docker >/dev/null 2>&1 || return 1
  ( docker info >/dev/null 2>&1 ) &
  pid=$!
  n=0
  while kill -0 "$pid" 2>/dev/null; do
    n=$((n + 1))
    if [ "$n" -ge 10 ]; then
      kill "$pid" 2>/dev/null
      wait "$pid" 2>/dev/null
      return 1
    fi
    sleep 1
  done
  wait "$pid" 2>/dev/null
}

sha256_of() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    shasum -a 256 "$1" | awk '{print $1}'
  fi
}

JAR=""
ensure_jar() {
  command -v java >/dev/null 2>&1 || die "java (JDK) required for jar mode"
  mkdir -p "$ROOT/tools"
  JAR="$ROOT/tools/openapi-generator-cli-$OGEN_VERSION.jar"
  if [ ! -f "$JAR" ]; then
    command -v curl >/dev/null 2>&1 || die "curl required to fetch the CLI jar"
    echo "downloading $OGEN_JAR_URL" >&2
    curl -fsSL -o "$JAR" "$OGEN_JAR_URL" || die "jar download failed"
  fi
  actual=$(sha256_of "$JAR")
  [ "$actual" = "$OGEN_JAR_SHA256" ] \
    || die "sha256 mismatch for $JAR (expected $OGEN_JAR_SHA256, got $actual)"
}

if docker_usable; then
  MODE="docker"
  GEN_INPUT="/input-openapi.yaml"
  GEN_OUTPUT="/local/$OUT_REL"
else
  MODE="jar"
  ensure_jar
  GEN_INPUT="$SPEC_ABS"
  GEN_OUTPUT="$OUT_ABS"
fi
echo "generator: openapi-generator-cli $OGEN_VERSION via $MODE" >&2

ogen() {
  if [ "$MODE" = "docker" ]; then
    docker run --rm --user "$(id -u):$(id -g)" \
      -v "$ROOT:/local" \
      -v "$SPEC_ABS:/input-openapi.yaml:ro" \
      -w /local \
      "$OGEN_IMAGE" "$@"
  else
    java -jar "$JAR" "$@"
  fi
}

# --- generate ----------------------------------------------------------------
mkdir -p "$OUT_ABS"
ogen generate \
  -i "$GEN_INPUT" \
  -g java \
  --library okhttp-gson \
  -o "$GEN_OUTPUT" \
  --api-package "$PKG_BASE.api" \
  --model-package "$PKG_BASE.model" \
  --invoker-package "$PKG_BASE.invoker" \
  --group-id com.experiencequality \
  --artifact-id "$SERVICE-client" \
  --artifact-version "$ARTIFACT_VERSION" \
  --additional-properties "hideGenerationTimestamp=true,dateLibrary=java8,artifactUrl=https://github.com/ExperienceQuality/xq-luthor,artifactDescription=Generated client for $SERVICE (contract $VERSION),developerOrganization=ExperienceQuality,developerOrganizationUrl=https://github.com/ExperienceQuality,scmUrl=https://github.com/ExperienceQuality/xq-luthor,scmConnection=scm:git:git://github.com/ExperienceQuality/xq-luthor.git,scmDeveloperConnection=scm:git:ssh://github.com/ExperienceQuality/xq-luthor.git,licenseName=Apache-2.0,licenseUrl=https://www.apache.org/licenses/LICENSE-2.0.txt"

# --- minimal pom patch: distributionManagement -> GitHub Packages ------------
# The okhttp-gson pom template has no distributionManagement option; inserting
# this block is the sanctioned post-gen patch. Generated Java sources are never
# edited.
POM="$OUT_ABS/pom.xml"
[ -f "$POM" ] || die "expected $POM was not generated"
if ! grep -q 'distributionManagement' "$POM"; then
  POM_TMP="$POM.tmp"
  awk -v url="$GH_PACKAGES_URL" '
    /^<\/project>/ && !done {
      print "  <distributionManagement>"
      print "    <repository>"
      print "      <id>github</id>"
      print "      <name>GitHub Packages</name>"
      print "      <url>" url "</url>"
      print "    </repository>"
      print "  </distributionManagement>"
      done=1
    }
    { print }
  ' "$POM" > "$POM_TMP" && mv "$POM_TMP" "$POM"
fi

echo "generated: $OUT_REL" >&2
