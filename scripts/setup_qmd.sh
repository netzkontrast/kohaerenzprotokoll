#!/usr/bin/env bash
# Rebuild the whole qmd setup from nothing. Idempotent.
#
# The container is ephemeral and `.tools-node/` and `.qmd/` are git-ignored, so
# everything here is lost on a fresh clone: the package, the index, every
# collection, their contexts, the agent skill and the PATH shim. Before this
# script that was six commands nobody had written down.
#
#   scripts/setup_qmd.sh            # install, index, collections, skill, shim
#   scripts/setup_qmd.sh --check    # report what is missing, change nothing
#
# Collections are named for PURPOSE, not for folder. `all` covers every markdown
# file outside the Legacy shelf — the flag is --mask, not --pattern, and a
# collection rooted at `.` without one indexes Legacy and the vendored clones
# (1,382 files, tried and removed). It is excluded from default queries because
# it overlaps the others.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QMD="$ROOT/.tools-node/node_modules/.bin/qmd"
SHIM=/usr/local/bin/qmd
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

say() { printf '  %-44s %s\n' "$1" "$2"; }

if [[ $CHECK -eq 1 ]]; then
    [[ -x "$QMD" ]] && say "package" "ok" || say "package" "MISSING"
    [[ -d "$ROOT/.qmd" ]] && say "index" "ok" || say "index" "MISSING"
    [[ -x "$SHIM" ]] && say "PATH shim" "ok" || say "PATH shim" "MISSING — the skill's Bash(qmd:*) will fail"
    [[ -f "$ROOT/.claude/skills/qmd/SKILL.md" ]] && say "agent skill" "ok" || say "agent skill" "MISSING"
    if [[ -x "$QMD" ]]; then
        # Derived, not hardcoded: this said "of 6" and reported "7 of 6" the
        # first time a collection was added. A check that carries a constant
        # about its own subject goes stale exactly when the subject changes.
        want=$(grep -c '^add ' "$ROOT/scripts/setup_qmd.sh")
        n=$("$QMD" collection list 2>/dev/null | grep -c " (qmd://" || true)
        [[ "$n" -eq "$want" ]] && say "collections" "$n of $want" \
                               || say "collections" "$n of $want — run scripts/setup_qmd.sh"
    fi
    python3 "$ROOT/scripts/qmd_coverage.py" >/dev/null 2>&1 \
        && say "coverage" "every file in a collection" \
        || say "coverage" "A DIRECTORY IS UNCOVERED — scripts/qmd_coverage.py"
    exit 0
fi

cd "$ROOT"

[[ -x "$QMD" ]] || npm install --prefix .tools-node @tobilu/qmd >/dev/null
[[ -d .qmd ]] || "$QMD" init >/dev/null

# name:path:context — purpose first, folder second.
add() {
    "$QMD" collection show "$1" >/dev/null 2>&1 && return 0
    if [[ -n "${4:-}" ]]; then
        "$QMD" collection add "$2" --name "$1" --mask "$4" >/dev/null
    else
        "$QMD" collection add "$2" --name "$1" >/dev/null
    fi
    "$QMD" context add "qmd://$1/" "$3" >/dev/null
    echo "  + $1"
}

add sources Sources/drive \
    "Immutable German research documents fetched from Google Drive, one per file, named by slug. The corpus the wiki is derived from. Never edited."
add wiki Wiki \
    "Derived term pages (candidates/), conflict records (conflicts/), question pages (questions/) and per-document reconciliation records (compare/). Each page collects every source's reading of one term, attributed and unmerged."
add census Sources/terms \
    "Term censuses: one per source document, listing every candidate term in that document exhaustively. Describes one document and nothing else."
add notes Sources/notes \
    "Reading notes: what one document says about the terms that matter, quoted with line numbers."
add plan Plan \
    "Process artifacts: concept notes, decisions, learnings, per-document run artifacts, the judgement ledger and the derived state."
add decisions . \
    "Everything already decided, and why: per-document reconciliation records, conflict records, open question pages, decision files, and the judgement ledger rendered from JSONL. Ask this by name before re-reading a whole record — a hit gives the file and the line. Excluded from default queries because it overlaps wiki and plan." \
    'Wiki/compare/**/*.md,Wiki/conflicts/**/*.md,Wiki/questions/**/*.md,Plan/decisions/**/*.md,Plan/runs/judgements.md'
"$QMD" collection exclude decisions >/dev/null 2>&1 || true

add all . \
    "Every markdown file in the project except the Legacy shelf and vendored clones. Excluded from default queries because it overlaps the purpose collections — ask for it by name when a question could be answered by any layer." \
    'Sources/**/*.md,Wiki/**/*.md,Plan/**/*.md,*.md'
"$QMD" collection exclude all >/dev/null 2>&1 || true

"$QMD" update >/dev/null
"$QMD" skill install --yes --force >/dev/null 2>&1 || "$QMD" skill install --yes >/dev/null 2>&1 || true

# The skill declares Bash(qmd:*) and the package is not on PATH.
if [[ ! -x "$SHIM" ]] && [[ -w /usr/local/bin ]]; then
    cat > "$SHIM" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
for root in "${QMD_PROJECT:-}" "$PWD" /home/user/kohaerenzprotokoll; do
  [[ -n "$root" && -x "$root/.tools-node/node_modules/.bin/qmd" ]] && exec "$root/.tools-node/node_modules/.bin/qmd" "$@"
done
echo "qmd is not installed for this project. From the repository root:" >&2
echo "  scripts/setup_qmd.sh" >&2
exit 127
SH
    chmod +x "$SHIM"
    echo "  + PATH shim at $SHIM"
fi

echo
"$0" --check
