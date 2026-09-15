#!/usr/bin/env bash
# Install the pinned lit-critic upstream into a gitignored working directory.
#
#     scripts/setup_lit_critic.sh [--pin <sha>] [--force]
#
# The manuscript repository stays prose-only: the upstream source tree and the
# virtualenv both live under .lit-critic-src/, which .gitignore excludes. The
# pin below is what makes a checkout reproducible — bump it deliberately and
# re-run the projection tests afterwards.
set -euo pipefail

REPO_URL="https://github.com/lit-pack/lit-critic"
PIN="29adcb8a06bbb43aa9ff22d5eae37b89440ed9ec"   # v5.1.1, 2026-05-02
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/.lit-critic-src"
VENV="$SRC/.venv"
FORCE=0

while [ $# -gt 0 ]; do
    case "$1" in
        --pin) PIN="$2"; shift 2 ;;
        --force) FORCE=1; shift ;;
        -h|--help) sed -n '2,12p' "${BASH_SOURCE[0]}"; exit 0 ;;
        *) echo "unknown argument: $1" >&2; exit 2 ;;
    esac
done

if [ "$FORCE" = "1" ] && [ -d "$SRC" ]; then
    echo "==> removing existing $SRC"
    rm -rf "$SRC"
fi

if [ ! -d "$SRC/.git" ]; then
    echo "==> fetching lit-critic @ ${PIN:0:12} into $SRC"
    mkdir -p "$SRC"
    git -C "$SRC" init -q
    git -C "$SRC" remote add origin "$REPO_URL" 2>/dev/null || true
    # Fetch the pinned commit directly; fall back to a full fetch for servers
    # that refuse a by-SHA want.
    if ! GIT_LFS_SKIP_SMUDGE=1 git -C "$SRC" fetch -q --depth 1 origin "$PIN" 2>/dev/null; then
        echo "    by-SHA fetch refused, falling back to a full fetch"
        GIT_LFS_SKIP_SMUDGE=1 git -C "$SRC" fetch -q origin
    fi
    git -C "$SRC" checkout -q "$PIN"
else
    CURRENT="$(git -C "$SRC" rev-parse HEAD)"
    if [ "$CURRENT" != "$PIN" ]; then
        echo "==> moving existing checkout from ${CURRENT:0:12} to ${PIN:0:12}"
        if ! GIT_LFS_SKIP_SMUDGE=1 git -C "$SRC" fetch -q --depth 1 origin "$PIN" 2>/dev/null; then
            GIT_LFS_SKIP_SMUDGE=1 git -C "$SRC" fetch -q origin
        fi
        git -C "$SRC" checkout -q "$PIN"
    fi
fi

echo "==> checkout is at $(git -C "$SRC" rev-parse --short HEAD)"

if [ ! -x "$VENV/bin/python" ]; then
    echo "==> creating virtualenv at $VENV"
    python3 -m venv "$VENV"
fi

echo "==> installing lit-critic dependencies"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r "$SRC/requirements.txt"
# lit-critic v5.1.1 imports httpx directly but does not declare it: it used to
# arrive with the anthropic SDK, which now ships httpx2 instead. Without this
# the engine fails at import time.
"$VENV/bin/pip" install -q "httpx>=0.27,<1.0"

echo "==> verifying the import surface the gate depends on"
cd "$SRC" && "$VENV/bin/python" - <<'PY'
import sys
from api.analysis_engine import AnalysisEngine           # noqa: F401
from orchestrator.persistence.database import get_connection  # noqa: F401
from orchestrator.persistence.snapshot_store import SnapshotStore  # noqa: F401
print(f"    ok — python {sys.version.split()[0]}")
PY

cat <<'DONE'

lit-critic is installed.

Next:
  1. export ANTHROPIC_API_KEY=...        (or OPENAI_API_KEY)
  2. python3 scripts/lit_critic_project.py        # project chapters into scenes
  3. python3 scripts/lit_critic_gate.py --chapter 4

The gate runs with .lit-critic-src/.venv automatically; you do not need to
activate it yourself.
DONE
