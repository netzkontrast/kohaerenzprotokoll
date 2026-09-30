#!/bin/sh
# The rest of scaled.sh, after it was paused for the readings batch (one model run at a time): every
# (contract, document) pair that has no run yet. Same contracts, same documents, same model.
cd "$(dirname "$0")/../../.." || exit 1
DOCS="kohaerenz-protokoll-philosophischer-bericht-md worldbuilding-konzept-kohaerenzprotokoll-md systemic-architecture-specification-the-coherence-protocol-w systems-narrative-analysis-the-coherence-protocol-kanon-2026 koharenz-protokoll-konzept-konsolidiert-2026-05-08-md kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md kohaerenz-protokoll-konzept-master-md kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md dramatica-storyform-synthese-aegis-analyse-2 hard-sf-roman-outline-dkt-physik-cosmic-horror mining-report-kohaerenz-protokoll-narrative-building-blocks the-architecture-of-fracture-a-compendium-of-the-kael-system"
for t in TermDefinitions TermContrasts CausalLinks; do
  lower=$(echo "$t" | tr 'A-Z' 'a-z')
  for doc in $DOCS; do
    [ -d "Plan/runs/$doc/hyperextract/$lower-haiku-2026-09-30" ] && continue
    echo "== $doc $t $(date +%H:%M:%S)"
    python3 scripts/he_claude.py run "$doc" "Plan/hyperextract/$t.yaml" --run "$lower-haiku-2026-09-30" --model haiku 2>&1 | grep -E '^\{"source_sha256|^\{"document"|Traceback|Error|error' | cut -c1-420
  done
done
echo "== done $(date +%H:%M:%S)"
