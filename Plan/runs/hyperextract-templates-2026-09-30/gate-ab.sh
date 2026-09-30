#!/bin/sh
# Does the cue gate lose what an ungated run finds? `CausalLinks`, whose cue keeps a little over a third of a German
# document (§4.6 of the note), on three German documents of the twelve: once more ungated (the run-to-run difference, which
# a model's repeat always has) and once gated (`he_claude.py run --gate`). Haiku through claude -p (decision 011), one run at a
# time. Each run is moved out of Plan/runs/<document>/hyperextract/ into gate-ab/, because the store loads every run that
# stands there and would count a line twice; gate-ab.py compares them with the first ungated run of the scaled pass.
cd "$(dirname "$0")/../../.." || exit 1
OUT=Plan/runs/hyperextract-templates-2026-09-30/gate-ab
mkdir -p $OUT
DOCS="kohaerenz-protokoll-philosophischer-bericht-md worldbuilding-konzept-kohaerenzprotokoll-md kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md"
for doc in $DOCS; do
  for mode in repeat gated; do
    flag=""; [ $mode = gated ] && flag="--gate"
    echo "== $doc $mode $(date +%H:%M:%S)"
    python3 scripts/he_claude.py run "$doc" Plan/hyperextract/CausalLinks.yaml --run "causallinks-$mode-2026-09-30" --model haiku $flag 2>&1 | grep -E '^\{"source_sha256|^\{"document"|Traceback|Error|error' | cut -c1-420
    mkdir -p $OUT/$doc
    mv Plan/runs/$doc/hyperextract/causallinks-$mode-2026-09-30 $OUT/$doc/$mode
  done
done
echo "== done $(date +%H:%M:%S)"
