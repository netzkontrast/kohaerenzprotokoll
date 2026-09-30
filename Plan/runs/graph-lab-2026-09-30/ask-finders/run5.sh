#!/bin/sh
# E3e: how many contract lines the `he-lines` finder should add. run4.sh measured 10 and 40 on the store after the scaled
# contract pass (+0.009 and +0.029 document recall); this adds 20 and 80 so that the limit is read off a curve of four points.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log5.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log5.txt; cp "$(ls -t Plan/runs/ask/bench-*.json | head -1)" $out/$name.json; }
run he-lines-20-scaled --with he-lines --he-lines 20
run he-lines-80-scaled --with he-lines --he-lines 80
echo "== done $(date -u +%H:%M:%S)" >> $out/log5.txt
