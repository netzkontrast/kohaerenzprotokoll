#!/bin/sh
# The measurement that follows the backfill, as one command: rebuild the store, run `ask.py bench` with and without the
# `he-lines` finder (10, 20, 40 and 80 lines), repeat the graph laboratory's E5 on it, regenerate the contracts' yield and the
# note's two generated tables, and print what the runs cost. Every bench row is paired with the default of the same store.
#
#   sh Plan/runs/hyperextract-backfill-2026-09-30/measure.sh [tag]        # tag defaults to `backfilled`
#   FORCE=1 sh .../measure.sh interim                                     # while the backfill still runs: a snapshot, named so
#
# It refuses while the backfill is running, because each finished run changes the store's input hash and would make the rows
# of one measurement belong to different stores. No model is called: `kg.py index`, `ask.py bench` and `graphlab.py he` read
# files. The bench results land in `ask-finders/<config>-<tag>.{txt,json}`, the pairing in `ask-finders/paired-<tag>.json`,
# and the log in `ask-finders/log-<tag>.txt`. The laboratory's own `e5-he.{md,json}` is kept as `e5-he-before-<tag>.{md,json}`
# before it is rewritten.
cd "$(dirname "$0")/../../.." || exit 1
tag="${1:-backfilled}"
PY=.venv-graphqlite/bin/python
here=Plan/runs/hyperextract-backfill-2026-09-30
out=$here/ask-finders
lab=Plan/runs/graph-lab-2026-09-30
mkdir -p "$out"
log="$out/log-$tag.txt"
if ps -eo cmd | grep -q "[b]ackfill.py run"; then
  echo "the backfill is still running: its runs would change the store under this measurement."
  echo "stop it (touch $here/STOP, wait for the run in progress) or FORCE=1 for a snapshot"
  [ -z "$FORCE" ] && exit 1
fi
say() { echo "== $* $(date -u +%H:%M:%S)" | tee -a "$log"; }
say "start, tag $tag"
python3 $here/backfill.py status | tee -a "$log"
say "store"; $PY scripts/kg.py index >> "$log" 2>&1 || { echo "kg.py index failed, see $log"; exit 1; }
run() { name="$1"; shift; say "$name"; $PY scripts/ask.py bench "$@" > "$out/$name-$tag.txt" 2>&1; tail -1 "$out/$name-$tag.txt" | tee -a "$log"; cp "$(ls -t Plan/runs/ask/bench-*.json | head -1)" "$out/$name-$tag.json"; }
run default
run he-lines-10 --with he-lines --he-lines 10
run he-lines-20 --with he-lines --he-lines 20
run he-lines-40 --with he-lines --he-lines 40
run he-lines-80 --with he-lines --he-lines 80
say "paired"; python3 $here/paired.py "$tag" | tee -a "$log"
say "E5 (the laboratory's e5-he, kept as e5-he-before-$tag)"
cp $lab/e5-he.md "$lab/e5-he-before-$tag.md"; cp $lab/e5-he.json "$lab/e5-he-before-$tag.json"
$PY scripts/graphlab.py he >> "$log" 2>&1 || echo "graphlab he failed, see $log"
say "yield and the note's tables"
python3 scripts/hegraph.py report > /dev/null
python3 Plan/runs/hyperextract-templates-2026-09-30/fill_concept.py | tee -a "$log"
say "what it cost"
python3 $here/stats.py --documents | tee "$here/stats-$tag.txt" >> "$log"
say "done — the note's §6.5, NOW.md question 2, CLAUDE.md and the PR body are written from these files, by hand"
