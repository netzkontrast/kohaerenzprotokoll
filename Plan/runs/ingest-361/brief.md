# Brief — readings from document 360 (step 6)

1 document, one reader, one batch: `ingest-361`. Files go to `Plan/runs/ingest-361/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 360 | `exploring-the-coherence-protocol` | 2025-11-03 | „the cross-domain coherence essay“ (an unsigned English essay) | coherence in general from quantum decoherence and cache coherence through self-organisation to two speculative theories — the Dual Kernel Theory and the Λ-Canon Synthesis, each with its own critical analysis — and fine-tuning, ending in a five-scale synthesis and a reference list; it names no figure of the novel |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (356 lines for `exploring-the-coherence-protoc`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A general essay: write „the cross-domain coherence essay reports / judges …“. Only its section on the Dual Kernel Theory touches a page; say when it reports the theory and when it judges it (`Critical Analysis`). Quote the English as written.

## Pages — document 360, `exploring-the-coherence-protocol`

- **`coheron`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Coheron` alone on L298. minor (1–3): Coherons as the minimal, self-correcting units of mutual information, as the essay reports the Dual Kernel Theory (L171); the synthesis table's row (L298) if it adds.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L166, L175. minor (1–3): the theory reported as a compelling metaphysical synthesis with two kernels (L166), K₁ the domain of reversible computation (L168), K₀ of irreversible computation and entropy (L169); the essay's own verdict, a metaphysical and explanatory architecture rather than a conventional scientific theory (L175).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). `Coherons` is read on coheron.


**Record entries:** none.

**Not promoted:** the Λ-Canon Synthesis, Corrective Wavelets, the five-scale synthesis, and the borrowed concepts (decoherence, cache coherence protocols, self-organisation, fine-tuning).

**One reader**: dkt, coheron.

**Chapter readings**: none.
