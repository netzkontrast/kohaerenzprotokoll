#!/bin/sh
# Commit what the backfill has finished, in one commit, and push it. The runs are hidden from `git status` between batches
# (.git/info/exclude and assume-unchanged on the log — local to the container), so that the end of a turn does not force a commit
# and a CI run for each of 137 runs; this makes them visible, stages the finished ones (a run writes usage.json and calls.jsonl
# last, so a directory without them is one in progress), commits with the message given as $1, pushes, and hides the log again.
# Usage: commit_batch.sh "what this batch holds"
cd "$(dirname "$0")/../../.." || exit 1
LOG=Plan/runs/hyperextract-backfill-2026-09-30/log.txt
OUT=Plan/runs/hyperextract-backfill-2026-09-30/stdout.txt
git update-index --no-assume-unchanged $LOG $OUT
n=0
for d in Plan/runs/*/hyperextract/*-haiku-2026-09-30 Plan/runs/*/hyperextract/*-haiku-2026-09-30-failed*; do
  [ -d "$d" ] || continue
  git ls-files --error-unmatch "$d/usage.json" >/dev/null 2>&1 && continue          # already committed
  if [ -f "$d/usage.json" ] && [ -f "$d/calls.jsonl" ]; then git add -f "$d"; n=$((n+1)); fi
done
git add $LOG $OUT
echo "staged $n run directories"
if ! git diff --cached --quiet; then
  git commit -q -F - <<MSG
${1:-HyperExtract backfill: finished runs}

$(python3 Plan/runs/hyperextract-backfill-2026-09-30/backfill.py status | head -1)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017rz7eM9k5RrKTBXaD9N6FY
MSG
  git fetch -q origin claude/elegant-ramanujan-onfl2w
  git push origin claude/elegant-ramanujan-onfl2w 2>&1 | tail -1
else
  echo "nothing to commit"
fi
git update-index --assume-unchanged $LOG $OUT
