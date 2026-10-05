#!/bin/bash
# pre-pr-app.sh — PreToolUse hook (mcp__github__create_pull_request, Bash)
# Before a pull request is opened, the project app must have been rebuilt and
# checked for the commit it carries (the author, 2026-10-05: „keep the ui updated").
# It does not build — a build takes about two minutes — it asks scripts/appstamp.py
# whether `ui.py --check` passed for HEAD's tree, and refuses the call (exit 2,
# the reason on stderr, which Claude reads) when it did not. The skill
# `app-refresh` (.agents/skills/app-refresh/SKILL.md) is what makes it pass.
# A Bash call is let through unless it opens a pull request (`gh pr create`).

input=$(cat)
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

opens_pr=$(printf '%s' "$input" | python3 -c '
import json, re, sys
try:
    d = json.load(sys.stdin)
except Exception:
    print("no"); raise SystemExit
tool = d.get("tool_name", "")
if tool == "mcp__github__create_pull_request":
    print("yes")
elif tool == "Bash" and re.search(r"\bgh\s+pr\s+create\b", d.get("tool_input", {}).get("command", "")):
    print("yes")
else:
    print("no")
' 2>/dev/null)

[ "$opens_pr" = "yes" ] || exit 0

cd "$ROOT" || exit 0
if why=$(python3 scripts/appstamp.py verify 2>&1); then
  echo "$why"
  exit 0
fi

cat >&2 <<MSG
pre-pr-app: no pull request until the project app is rebuilt for this commit.
$why

Run the skill app-refresh (.agents/skills/app-refresh/SKILL.md): it rebuilds the app with
\`python3 scripts/ui.py --check\` (which writes the stamp this hook reads), looks at what changed,
and publishes. Then open the pull request again.
If the app genuinely cannot be built here, record why — \`python3 scripts/appstamp.py waive "<reason>"\` —
and say so in the pull request's description.
MSG
exit 2
