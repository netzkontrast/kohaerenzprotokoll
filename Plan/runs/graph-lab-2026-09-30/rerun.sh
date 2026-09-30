#!/bin/sh
# The decisive experiments again, on the wiki as it stands after the scaled contract pass and the four reader-lab documents
# (58 documents with a census). The first run — the diagnosis and E1 before the readings of documents 52–54 were merged at
# 13:53, E2–E5 after them — is kept in first-run/; these overwrite the top-level files, so every table in the folder is of one
# wiki and the note says which.
cd "$(dirname "$0")/../../.." || exit 1
F=Plan/runs/graph-lab-2026-09-30
PY=.venv-graphqlite/bin/python
mkdir -p $F/first-run
for f in diagnose e1-core e2-enrich e2b-comention e4-hub e5-he; do cp $F/$f.md $F/$f.json $F/first-run/ 2>/dev/null; done
for c in diagnose core enrich comention hub he; do
  echo "== $c $(date -u +%H:%M:%S)" >> $F/rerun-log.txt
  $PY scripts/graphlab.py $c > $F/rerun-$c.txt 2>&1
  tail -1 $F/rerun-$c.txt >> $F/rerun-log.txt
done
sh $F/ask-finders/run4.sh
echo "== done $(date -u +%H:%M:%S)" >> $F/rerun-log.txt
