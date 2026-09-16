#!/usr/bin/env bash
# Create the DSPy virtualenv for tools/kpwiki and run the offline smoke test.
#
#   scripts/setup_dspy.sh            # create .venv-dspy, install, smoke-test
#   scripts/setup_dspy.sh --check    # only run the smoke test + kpwiki tests
#   scripts/setup_dspy.sh --deno     # also install Deno, which dspy.RLM needs
#
# Needs `uv` (preferred) or python3 -m venv. No API key is needed for the
# smoke test; live runs read ANTHROPIC_API_KEY or, without it, run through the
# `claude` CLI (KP_LM_BACKEND=auto; see docs/dspy-base.md "Local runtime").
#
# `dspy.RLM` runs its sandbox on Pyodide under Deno, so without Deno on PATH
# it raises at construction. Every other program here works without it, which
# is why the install is opt-in and its absence is a warning rather than an
# error. Re-run with --deno in a fresh container: the install lands in
# $HOME/.deno and does not survive one.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv-dspy"
PY="$VENV/bin/python"

DENO_HOME="${DENO_INSTALL:-$HOME/.deno}"

# Prints deno's path, or nothing. Never fails: callers run under `set -e`, so
# a non-zero return here would abort the setup on exactly the containers that
# have no Deno — the case this is meant to report.
deno_path() {
    command -v deno 2>/dev/null && return 0
    [[ -x "$DENO_HOME/bin/deno" ]] && echo "$DENO_HOME/bin/deno"
    return 0
}

if [[ "${1:-}" == "--deno" ]]; then
    if [[ -n "$(deno_path)" ]]; then
        echo "deno already present: $(deno_path)"
    else
        echo "installing Deno into $DENO_HOME (dspy.RLM needs it)"
        DENO_INSTALL="$DENO_HOME" bash -c \
            'curl -fsSL https://deno.land/install.sh | sh -s -- -y' >/dev/null
    fi
    export PATH="$DENO_HOME/bin:$PATH"
fi

if [[ "${1:-}" != "--check" && "${1:-}" != "--deno" ]]; then
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

DENO="$(deno_path)"
if [[ -n "$DENO" ]]; then
    echo "deno $("$DENO" --version | head -1 | cut -d" " -f2) — dspy.RLM is available"
else
    echo "deno missing — dspy.RLM is unavailable; everything else runs. Add it with --deno"
fi
"$PY" -m tools.kpwiki.smoke --dry-run
"$PY" -m pytest tests/test_kpwiki.py tests/test_kpwiki_lm_backend.py tests/test_kpwiki_clarify.py tests/test_kpwiki_tetraframe.py -q
