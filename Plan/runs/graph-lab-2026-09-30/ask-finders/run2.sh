#!/bin/sh
# E3b: how many co-mention paragraphs, and how many lines of the contracts' readings, a pack can hold. Sequential.
cd "$(dirname "$0")/../../../.." || exit 1
PY=.venv-graphqlite/bin/python
out=Plan/runs/graph-lab-2026-09-30/ask-finders
run() { name="$1"; shift; echo "== $name $(date -u +%H:%M:%S)" >> $out/log2.txt; $PY scripts/ask.py bench "$@" > $out/$name.txt 2>&1; tail -1 $out/$name.txt >> $out/log2.txt; }
run comention-20 --comention 20
run comention-10 --comention 10
run comention-5 --comention 5
run without-co-mention-with-he-lines-10 --without co-mention --with he-lines --he-lines 10
run with-he-lines-10 --with he-lines --he-lines 10
echo "== done $(date -u +%H:%M:%S)" >> $out/log2.txt
