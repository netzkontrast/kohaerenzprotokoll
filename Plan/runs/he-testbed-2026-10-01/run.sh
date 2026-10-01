#!/usr/bin/env bash
# The testbed: every HyperExtract contract on two small, already-read documents, Sonnet through claude -p
# (decision 011), ONE RUN AT A TIME (the author's „starte diese nicht parallel", 2026-09-30).
# On the author's instruction of 2026-10-01: „Erstelle für jedes hyperextract Template eine Datei mit allen
# Ergebnissen aus zwei kleinen Test-sources - nutze sonnet agents für diese Tests".
# Resumable: a run whose directory exists is skipped. `touch STOP` beside this file stops it after the current run.
# Then: python3 Plan/runs/he-testbed-2026-10-01/results.py writes one file per contract.
set -u
cd "$(dirname "$0")/../../.."
HERE=Plan/runs/he-testbed-2026-10-01
DOCS=(kohaerenz-protokoll-meta-foreshadowing-beobachter-logik 2026-09-14-kap25-vertiefung-md)
APPROVAL="decision 011 (Claude, first party); the author's instruction of 2026-10-01 to run every HyperExtract template on two small test sources with Sonnet"
for doc in "${DOCS[@]}"; do
  for path in Plan/hyperextract/*.yaml; do
    [[ -f "$HERE/STOP" ]] && { echo "STOP file: stopped before $doc $path"; exit 0; }
    t=$(basename "$path" .yaml); lower=$(echo "$t" | tr '[:upper:]' '[:lower:]')
    run="$lower-sonnet-2026-10-01"
    [[ -d "Plan/runs/$doc/hyperextract/$run" ]] && continue
    echo "$(date -u +%H:%M:%S) $doc $t"
    python3 scripts/he_claude.py run "$doc" "$path" --run "$run" --model sonnet --approval "$APPROVAL" 2>&1 \
      | grep -E '^\{"document"|Traceback|Error' | cut -c1-300
  done
done
echo "$(date -u +%H:%M:%S) done"
