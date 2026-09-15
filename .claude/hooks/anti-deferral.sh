#!/bin/bash
# anti-deferral.sh — PreToolUse hook (Write, Edit, MultiEdit)
# Scans content being written for deferral language and warns Claude.
# Deferred worldbuilding ("wird später ergänzt") creates permanent canon gaps.
# Adapted for Kohärenz Protokoll: German patterns added; the canon provenance
# marker `[L]` (Lücke) is a legitimate, tracked gap and is NOT flagged; the
# diegetic word "Platzhalter" (used in chapter prose) is NOT flagged either.
# Warn-only: always exits 0.

input=$(cat)

read -r filepath content < <(echo "$input" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    tool = data.get('tool_name', '')
    params = data.get('tool_input', {})
    path = params.get('file_path', params.get('filePath', params.get('path', '')))
    if tool == 'Write':
        text = params.get('content', params.get('file_text', ''))
    elif tool == 'Edit':
        text = params.get('new_string', params.get('new_str', ''))
    elif tool == 'MultiEdit':
        text = '\n'.join(e.get('new_string', e.get('new_str', '')) for e in params.get('edits', []))
    else:
        text = ''
    # one line: path, then the content with newlines folded
    print(path, ' '.join(text.split()))
except Exception:
    print('', '')
" 2>/dev/null)

[ -z "$content" ] && exit 0
# Graph, generated views and JSON manifests are not prose.
case "$filepath" in
    *.agency/*|*Codex/*|*.json|*.db) exit 0 ;;
esac

patterns=(
    "TODO"
    "FIXME"
    "XXX"
    "TBD"
    "placeholder"
    "will flesh out"
    "flesh out later"
    "add later"
    "expand later"
    "detail later"
    "to be determined"
    "needs more work"
    "draft only"
    "coming soon"
    "später ausarbeiten"
    "später ergänz"
    "wird ergänzt"
    "wird später"
    "noch zu schreiben"
    "noch auszuarbeiten"
    "noch zu füllen"
    "kommt später"
)

found=()
for pattern in "${patterns[@]}"; do
    if echo "$content" | grep -qi -- "$pattern"; then
        found+=("$pattern")
    fi
done

if [ ${#found[@]} -gt 0 ]; then
    cat << WARN

⚠  ANTI-DEFERRAL WARNING (${filepath}): ${found[*]}

Deferred canon creates permanent gaps. Before continuing:
1. Can this be written now? If yes, write it.
2. If deferral is genuinely correct, mark it as a tracked gap — \`[L]\` in canon
   documents, an entry in Plan/drafting/decision-log*.md for drafting choices —
   and get explicit user approval.
3. Do not declare the task done while deferral language remains.

WARN
fi

exit 0
