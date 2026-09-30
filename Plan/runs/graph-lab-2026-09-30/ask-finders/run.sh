#!/bin/sh
# E3: which finder earns its place in an ask pack. Sequential; one bench is about 90 s.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log.txt; }
run default
run with-he-lines --with he-lines
run without-graph-evidence --without graph-evidence
run without-bm25-lines --without bm25-lines
run without-entity-unread --without entity-unread
run without-co-mention --without co-mention
run without-parallel --without parallel
echo "== done $(date -u +%H:%M:%S)" >> $out/log.txt
