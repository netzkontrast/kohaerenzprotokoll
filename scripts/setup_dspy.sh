#!/usr/bin/env bash
# Create the DSPy virtualenv for tools/kpwiki and run the offline smoke test.
#
#   scripts/setup_dspy.sh            # create .venv-dspy, install, smoke-test
#   scripts/setup_dspy.sh --check    # only run the smoke test + kpwiki tests
#
# Needs `uv` (preferred) or python3 -m venv. No API key is needed for the
# smoke test; live runs read ANTHROPIC_API_KEY (see docs/dspy-base.md).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv-dspy"
PY="$VENV/bin/python"

if [[ "${1:-}" != "--check" ]]; then
    if command -v uv >/dev/null 2>&1; then
        # UV_EXCLUDE_NEWER can silently resolve an older DSPy (dspy-agent-skills docs/installation.md).
        env -u UV_EXCLUDE_NEWER uv venv -q "$VENV"
        env -u UV_EXCLUDE_NEWER uv pip install -q --python "$PY" -r "$ROOT/requirements-dspy.txt"
    else
        python3 -m venv "$VENV"
        "$PY" -m pip install -q -r "$ROOT/requirements-dspy.txt"
    fi
fi

cd "$ROOT"
"$PY" -c 'import dspy; print("dspy", dspy.__version__)'
"$PY" -m tools.kpwiki.smoke --dry-run
"$PY" -m pytest tests/test_kpwiki.py -q
