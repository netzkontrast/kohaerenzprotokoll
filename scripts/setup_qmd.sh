#!/usr/bin/env bash
# Rebuild the qmd setup from nothing. Idempotent.
#
#   scripts/setup_qmd.sh            # install, models, index, embeddings, skill, shim
#   scripts/setup_qmd.sh --check    # report what is missing, change nothing
#
# THE CONFIGURATION IS COMMITTED, at `.qmd/index.yml`, and this script does not
# write it. qmd's own trust.ts says a project-local config "arrives with a `git
# clone`, and `findLocalConfigPath` adopts it automatically for any command run
# inside the tree" — so collections, their contexts and the three model URIs
# travel with the repository.
#
# This script used to rebuild the collections from `collection add` arguments.
# That was one configuration in two places: the shell argument and the YAML qmd
# wrote from it, free to drift, and the YAML was git-ignored so a fresh clone
# got whichever the script happened to say that week. Now there is one file,
# and this script installs what a clone cannot carry: the package (~50 MB), the
# three GGUF models (~2.1 GB), the SQLite index (~100 MB) and the embeddings.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QMD="$ROOT/.tools-node/node_modules/.bin/qmd"
CONFIG="$ROOT/.qmd/index.yml"
SHIM=/usr/local/bin/qmd
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

say() { printf '  %-44s %s\n' "$1" "$2"; }

# Collections qmd reports, against collections the committed config declares.
# Derived from the file on both sides: a check that carries a constant about its
# own subject goes stale exactly when the subject changes.
config_collections() {
    python3 -c "import yaml,sys; print(' '.join(sorted(yaml.safe_load(open(sys.argv[1]))['collections'])))" "$CONFIG"
}
index_collections() {
    "$QMD" collection list 2>/dev/null | grep -oE "^[a-z_-]+ \(qmd://" | cut -d' ' -f1 | sort | tr '\n' ' ' | sed 's/ $//'
}

if [[ $CHECK -eq 1 ]]; then
    [[ -x "$QMD" ]] && say "package" "ok" || say "package" "MISSING"
    [[ -f "$CONFIG" ]] && say "config (committed)" "ok" || say "config (committed)" "MISSING — .qmd/index.yml is tracked; restore it"
    [[ -x "$SHIM" ]] && say "PATH shim" "ok" || say "PATH shim" "MISSING — the skill's Bash(qmd:*) will fail"
    [[ -f "$ROOT/.claude/skills/qmd/SKILL.md" ]] && say "agent skill" "ok" || say "agent skill" "MISSING"
    if [[ -x "$QMD" && -f "$CONFIG" ]]; then
        want="$(config_collections)"; have="$(index_collections)"
        [[ "$want" == "$have" ]] && say "collections" "$(wc -w <<<"$want") of $(wc -w <<<"$want")" \
                                 || say "collections" "INDEX DISAGREES WITH CONFIG — run qmd update
      config: $want
      index:  $have"
        pending=$("$QMD" status 2>/dev/null | grep -oE "Pending:[[:space:]]+[0-9]+" | grep -oE "[0-9]+" || echo "?")
        [[ "$pending" == "0" ]] && say "embeddings" "complete" \
                                || say "embeddings" "$pending pending — vsearch and query's vector leg return nothing until 'qmd embed'"
    fi
    python3 "$ROOT/scripts/qmd_coverage.py" >/dev/null 2>&1 \
        && say "coverage" "every file in a collection" \
        || say "coverage" "A DIRECTORY IS UNCOVERED — scripts/qmd_coverage.py"
    exit 0
fi

cd "$ROOT"

[[ -f "$CONFIG" ]] || {
    echo "No $CONFIG. It is tracked in git — this is a restore, not a setup:" >&2
    echo "  git checkout .qmd/index.yml" >&2
    echo "Never run 'qmd init' here: it overwrites the committed configuration." >&2
    exit 1
}

[[ -x "$QMD" ]] || npm install --prefix .tools-node @tobilu/qmd >/dev/null

# The models are ~2.1 GB and live in ~/.cache/qmd, outside the repository, so a
# fresh container has none. Without the embedding one, `qmd embed` cannot run
# and every vector search returns nothing while looking like it worked.
"$QMD" pull >/dev/null 2>&1 || echo "  ! qmd pull failed — vsearch will return nothing" >&2

"$QMD" update >/dev/null
"$QMD" embed --timeout 0 >/dev/null 2>&1 || echo "  ! qmd embed did not finish — rerun it" >&2

# NOT `qmd skill install`: that writes the package's bootstrap over this
# project's own .claude/skills/qmd, which documents the corpus rather than the
# tool. `qmd skill show` prints the package's text when it is wanted.

# The skill declares Bash(qmd:*) and the package is not on PATH.
if [[ ! -x "$SHIM" ]] && [[ -w /usr/local/bin ]]; then
    cat > "$SHIM" <<'SHIMEOF'
#!/usr/bin/env bash
set -euo pipefail
for root in "${QMD_PROJECT:-}" "$PWD" /home/user/kohaerenzprotokoll; do
  [[ -n "$root" && -x "$root/.tools-node/node_modules/.bin/qmd" ]] && exec "$root/.tools-node/node_modules/.bin/qmd" "$@"
done
echo "qmd is not installed for this project. From the repository root:" >&2
echo "  scripts/setup_qmd.sh" >&2
exit 127
SHIMEOF
    chmod +x "$SHIM"
    echo "  + PATH shim at $SHIM"
fi

echo
"$0" --check
