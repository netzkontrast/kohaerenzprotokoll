#!/bin/sh
# Stage what the backfill has finished: every untracked run directory under Plan/runs/*/hyperextract/ that holds its
# usage.json and calls.jsonl (a run writes those last, so a directory without them is one in progress), and the log.
# Prints what it staged; the commit is the session's, with the message naming the count and the cost.
cd "$(dirname "$0")/../../.." || exit 1
n=0
for d in $(git ls-files --others --exclude-standard --directory Plan/runs/*/hyperextract/ 2>/dev/null); do
  d=${d%/}
  if [ -f "$d/usage.json" ] && [ -f "$d/calls.jsonl" ]; then git add "$d"; n=$((n+1)); fi
done
git add Plan/runs/hyperextract-backfill-2026-09-30/log.txt 2>/dev/null
echo "staged $n run directories"
