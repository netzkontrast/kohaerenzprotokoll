#!/bin/bash
# Post-Compact Restore — reads saved session state on session start.
# Also reports whether the generated Codex/ views are stale relative to the
# graph, so a resumed session doesn't reason from an outdated glossary.
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"

if [ -f "$root/.claude/CURRENT_TASK.md" ]; then
    echo ""
    echo "## Resumed Task State (from previous session)"
    echo ""
    cat "$root/.claude/CURRENT_TASK.md"
    echo ""
    echo "Continue from the 'Next concrete step' above."
fi

if [ -f "$root/scripts/render_codex_views.py" ] && [ -d "$root/Graph" ]; then
    if ! python3 "$root/scripts/render_codex_views.py" --check >/dev/null 2>&1; then
        echo ""
        echo "⚠  Codex/ views are stale vs Graph/ — run: python3 scripts/render_codex_views.py"
    fi
fi
exit 0
