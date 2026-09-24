#!/bin/bash
# SessionStart hook — install what a fresh cloud container lacks.
# Runs scripts/install.sh, the same list a person runs by hand. Cloud only:
# on a local machine this exits at once and changes nothing.
# Synchronous: the session starts once this finishes, so no step races an
# install. A failed component is logged and never blocks the session.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
LOG="$ROOT/.install.log"

# uv tools land in ~/.local/bin; make sure the session sees them.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
fi
export PATH="$HOME/.local/bin:$PATH"

echo "session-start: scripts/install.sh (log: .install.log)"
if "$ROOT/scripts/install.sh" >"$LOG" 2>&1; then
  cat "$LOG"
else
  cat "$LOG"
  echo "session-start: some components failed — see above; rerun scripts/install.sh <name>"
fi
exit 0
