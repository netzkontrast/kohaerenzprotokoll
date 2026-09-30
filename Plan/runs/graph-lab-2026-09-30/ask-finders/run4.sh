#!/bin/sh
# E3d: the finders on the store after the scaled contract pass and the four reader-lab documents. The gold grew with the
# records (Q3, Q8 and C2 gained entries from documents 56 and 57), so the default is measured again, on the same store as
# every other row here; nothing is compared with an earlier default.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log4.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log4.txt; cp "$(ls -t Plan/runs/ask/bench-*.json | head -1)" $out/$name.json; }
run default-scaled
run he-lines-10-scaled --with he-lines --he-lines 10
run he-lines-40-scaled --with he-lines --he-lines 40
run without-co-mention-scaled --without co-mention
echo "== done $(date -u +%H:%M:%S)" >> $out/log4.txt
