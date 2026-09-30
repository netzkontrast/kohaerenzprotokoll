#!/bin/sh
# E3c: the counted co-mention relation in the walk that ranks pages (`--pr-comention W`), the finders as they now stand.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log3.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log3.txt; }
run default-comention10
run pr-comention-10 --pr-comention 10
run pr-comention-30 --pr-comention 30
echo "== done $(date -u +%H:%M:%S)" >> $out/log3.txt
