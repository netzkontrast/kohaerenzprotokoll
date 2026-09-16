#!/bin/bash
# post-tool-use.sh — PostToolUse hook (Write, Edit, MultiEdit)
# Deterministic post-write lint for Kohärenz Protokoll. Warn-only (exit 0).
#
#   chapters/NN-*.md  → scripts/lint_chapter.py --hook (R-rules, Act-I fences,
#                       frontmatter/status enum, voice labels, heat polarity)
#   Codex/**/*.md     → generated views: warn, point at the render script
#   Canon/*.md        → normative imports: warn, remind of decision-log discipline
#   ncp*.json         → storyform state: warn, remind of ncp-author + coherence check
#   other *.md under Manuscript/ → frontmatter presence

input=$(cat)
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"

filepath=$(echo "$input" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if data.get('tool_name', '') in ('Write', 'Edit', 'MultiEdit'):
        p = data.get('tool_input', {})
        print(p.get('file_path', p.get('filePath', p.get('path', ''))))
except Exception:
    pass
" 2>/dev/null)

[ -z "$filepath" ] && exit 0
[ ! -f "$filepath" ] && exit 0

case "$filepath" in
    */Wiki/index.md|*/Wiki/concept-table.md|*/Wiki/graph/*|Wiki/index.md|Wiki/concept-table.md|Wiki/graph/*)
        echo ""
        echo "⚠  RENDERED WIKI VIEW EDITED: $filepath"
        echo "  index.md, concept-table.md and graph/ are tools-only (Wiki/schema/conventions.yaml)."
        echo "  Edit the pages, then run: python3 scripts/render_wiki_views.py"
        echo ""
        ;;
    */Wiki/*.md|Wiki/*.md)
        if [ -f "$root/scripts/wiki_lint.py" ]; then
            out=$(python3 "$root/scripts/wiki_lint.py" --hook "$filepath" 2>&1)
            if [ -n "$out" ]; then
                echo ""
                echo "⚠  WIKI LINT (scripts/wiki_lint.py, warn-only; the gate before /wiki-promote is strict):"
                echo "$out"
                echo ""
            fi
        fi
        ;;
    */chapters/[0-9][0-9]-*.md)
        out=$(python3 "$root/scripts/lint_chapter.py" --hook "$filepath" 2>&1)
        if [ -n "$out" ]; then
            echo ""
            echo "⚠  CHAPTER LINT (scripts/lint_chapter.py):"
            echo "$out"
            echo "Semantic rules (R-1, R-2, R-6, R-7, register) still need the scene-bridge-auditor."
            echo ""
        fi
        ;;
    */Codex/*.md|*/Codex/*/*.md|*/Codex/*/*/*.md|Codex/*.md|Codex/*/*.md|Codex/*/*/*.md)
        echo ""
        echo "⚠  GENERATED VIEW EDITED: $filepath"
        echo "  Codex/ is rendered from .agency/session.db. Hand edits are overwritten."
        echo "  Change the graph (create/update_codex_entry, record_story_event,"
        echo "  create_world_axiom) and run: python3 scripts/render_codex_views.py"
        echo ""
        ;;
    */Canon/*.md|Canon/*.md)
        echo ""
        echo "⚠  CANON EDITED: $filepath"
        echo "  Canon/ is the imported normative corpus (storyform-und-outline wins on conflict)."
        echo "  Record the decision in Plan/drafting/decision-log*.md, keep [K]/[V]/[L] markers,"
        echo "  and re-run scripts/ingest_canon.py if terms/axioms changed. Author approval required."
        echo ""
        ;;
    */ncp.json|*/ncp-b.json)
        echo ""
        echo "⚠  NCP EDITED: $filepath — structural mutations go through the ncp-author skill;"
        echo "  run novel_coherence_check(ncp) + validate_appreciations before committing."
        echo ""
        ;;
    */Manuscript/*.md)
        if ! head -1 "$filepath" | grep -q '^---$'; then
            echo ""
            echo "⚠  FRONTMATTER: $filepath lacks YAML frontmatter (Manuscript files start with ---)"
            echo ""
        fi
        ;;
esac

exit 0
