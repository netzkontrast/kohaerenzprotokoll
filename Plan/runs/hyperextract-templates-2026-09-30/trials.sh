#!/bin/sh
# One HyperExtract pass per (document, contract), Haiku through claude -p (decision 011), one at a time.
# Each run stages Plan/runs/<document>/hyperextract/<template>-haiku-2026-09-30/ and records its cost in usage.json.
cd "$(dirname "$0")/../../.." || exit 1
run() {
  doc="$1"; shift
  for t in "$@"; do
    lower=$(echo "$t" | tr 'A-Z' 'a-z')
    echo "== $doc $t $(date +%H:%M:%S)"
    python3 scripts/he_claude.py run "$doc" "Plan/hyperextract/$t.yaml" --run "$lower-haiku-2026-09-30" --model haiku 2>&1 | grep -E '^\{"source_sha256|^\{"document"|Traceback|Error|error' | cut -c1-420
  done
}
run kohaerenz-protokoll-meta-foreshadowing-beobachter-logik Anchors Knowledge ThemeMotifs Analogies Attributions OpenPoints CausalLinks TermTaxonomy Rules StandingClaims
run detaillierte-kapiteluebersicht ChapterCards StructureBeats ChapterBeats Precedence CastRoles Anchors
run koharenz-protokoll-sprach-dna-2026-05-13-md CardFields ProseRules DiegeticTerms Utterances EntityFacts
run the-coherence-protocol-the-hidden-rules-that-hold-reality-to Rules Locks Quantities Analogies
run dual-storyform-hintergruende-md Storypoints
run kp-kap25-2026-09-14-md Utterances
run briefing-core-concepts-of-the-kohaerenz-protokoll-project Pitch StandingClaims
echo "== done $(date +%H:%M:%S)"
