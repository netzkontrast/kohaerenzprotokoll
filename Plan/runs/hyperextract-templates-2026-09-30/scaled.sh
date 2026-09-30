#!/bin/sh
# The second pass: the three contracts whose records a reader marked right most often on theory text
# (TermDefinitions, TermContrasts, CausalLinks) over the twelve documents that hold the most of the bench's
# gold lines. One HyperExtract pass per (document, contract), Haiku through claude -p (decision 011), one at a
# time. Each run stages Plan/runs/<document>/hyperextract/<template>-haiku-2026-09-30/ and records its cost.
cd "$(dirname "$0")/../../.." || exit 1
run() {
  t="$1"; shift
  lower=$(echo "$t" | tr 'A-Z' 'a-z')
  for doc in "$@"; do
    echo "== $doc $t $(date +%H:%M:%S)"
    python3 scripts/he_claude.py run "$doc" "Plan/hyperextract/$t.yaml" --run "$lower-haiku-2026-09-30" --model haiku 2>&1 | grep -E '^\{"source_sha256|^\{"document"|Traceback|Error|error' | cut -c1-420
  done
}
DOCS="kohaerenz-protokoll-philosophischer-bericht-md worldbuilding-konzept-kohaerenzprotokoll-md systemic-architecture-specification-the-coherence-protocol-w systems-narrative-analysis-the-coherence-protocol-kanon-2026 koharenz-protokoll-konzept-konsolidiert-2026-05-08-md kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md kohaerenz-protokoll-konzept-master-md kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md dramatica-storyform-synthese-aegis-analyse-2 hard-sf-roman-outline-dkt-physik-cosmic-horror mining-report-kohaerenz-protokoll-narrative-building-blocks the-architecture-of-fracture-a-compendium-of-the-kael-system"
run TermDefinitions $DOCS
run TermContrasts $DOCS
run CausalLinks $DOCS
echo "== done $(date +%H:%M:%S)"
