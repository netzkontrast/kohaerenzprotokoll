#!/bin/sh
# E3f: the ablations of run.sh again, on the store after the scaled contract pass, so that every row of the finder table is of
# one store and one gold (the default is default-scaled: co-mention limited to 10, the contracts' lines off). Waits for run5.sh.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
until grep -q '== done' $out/log5.txt 2>/dev/null; do sleep 5; done
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log6.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log6.txt; cp "$(ls -t Plan/runs/ask/bench-*.json | head -1)" $out/$name.json; }
run without-graph-evidence-scaled --without graph-evidence
run without-bm25-lines-scaled --without bm25-lines
run without-parallel-scaled --without parallel
run without-entity-unread-scaled --without entity-unread
echo "== done $(date -u +%H:%M:%S)" >> $out/log6.txt
