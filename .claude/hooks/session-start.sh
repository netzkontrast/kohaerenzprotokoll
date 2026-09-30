#!/bin/bash
# SessionStart hook — install what a fresh cloud container lacks.
# Runs the coordinator initializer before any reading, locally and remotely.
# Synchronous: the session starts once this finishes, so no step races an
# install. A failed component is logged and never blocks the session.
set -uo pipefail

ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
LOG="$ROOT/.install.log"

# uv tools land in ~/.local/bin; make sure the session sees them.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
fi
export PATH="$HOME/.local/bin:$PATH"

echo "session-start: knowledge init --profile research (log: .install.log)"
cd "$ROOT"
if python3 scripts/knowledge.py init --profile research >"$LOG" 2>&1; then
  cat "$LOG"
else
  cat "$LOG"
  echo "session-start: initialization incomplete — inspect capability failures before reading; rerun knowledge.py init"
fi
exit 0
