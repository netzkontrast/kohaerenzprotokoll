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

echo "session-start: read NOW.md first; follow its next-session mandate and linked briefing before selecting work."
echo "session-start: knowledge init --profile research (log: .install.log)"
cd "$ROOT"
if python3 scripts/knowledge.py init --profile research >"$LOG" 2>&1; then
  cat "$LOG"
else
  cat "$LOG"
  echo "session-start: initialization incomplete — inspect capability failures before reading; rerun knowledge.py init"
fi
# The session board: NOW.md's plan against GitHub — which session a pull request has claimed, which branches are
# being pushed to. Read it before choosing work; claim yours with a pull request holding `Session: <id>`.
# Never blocks: offline, it says the live state is unknown.
echo
timeout 25 python3 scripts/sessions.py board 2>&1 || echo "session-start: the session board could not run — check https://kohaerenzprotokoll.vercel.app/#/now by hand before taking a session"
exit 0
