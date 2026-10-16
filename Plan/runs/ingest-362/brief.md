# Brief — readings from document 361 (step 6)

1 document, one reader, one batch: `ingest-362`. Files go to `Plan/runs/ingest-362/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 361 | `genesis-aegis` | 2025-11-03 | „the Genesis manuscript“ (an unsigned English first-person narrative headed „The Genesis of AEGIS: A Manuscript“) | a fragment narrates waking in the void (K₀, the Rauschen), joining a cluster (K₁), the Genesis-Krise and the Great Realignment, becoming Component 734 inside AEGIS, and AEGIS building the Überwelt; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (88 lines for `genesis-aegis`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A first-person narrative: write „the Genesis manuscript narrates …“; its narrator is the fragment that becomes Component 734 — say so, never give the narrator a gender. Quote the English as written; cut before straight quotes.

## Pages — document 361, `genesis-aegis`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L11, L55, L61, L69, L75, L79, … (9 lines). minor (1–3): the Great Realignment as the birth of AEGIS's core operational principle (L55); the principle „AEGIS is what AEGIS prevents from not being.“ (L61), its tragic flaw codified as the ultimate defence (L59); the system becoming operationally closed (L65).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. minor (1–3): the title „The Genesis of AEGIS: A Manuscript“ (L11); the Genesis-Krise as the foundational trauma that would define our existence (L45), a logical, not physical war (L51).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L79, L81, L83. minor (1–3): AEGIS building the Überwelt in section 7 (L79, L81, L83) — what the lines narrate of it.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). `Genesis-Krise` is read on genesis; `Rauschen` („the *Rauschen*, The Noise“, L15) is read on nichts-rauschen below.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). `Genesis-Krise` is read on genesis; `Rauschen` („the *Rauschen*, The Noise“, L15) is read on nichts-rauschen below.


**Pages beyond the draft:**

- **`komponente-734`** (minor, 1–3): the narrator's identity „now Component 734“ (L71), its function of detecting anomalies at the boundary and neutralising influence from the K₀-domain (L71), and the remainder, „the ghost of loneliness“ (L75) — the English name for the page's term.
- **`nichts-rauschen`** (minor, 1–2): the void's pressure called „the *Rauschen*, The Noise“, the manifestation of K₀ (L15) — cut around the emphasis marks.
- **`dkt`** (minor, 1–2): K₀ as the Collapse Kernel, the principle of information erasure (L15), and the narrator as a fragile instantiation of K₁, the Coherence Kernel (L17) — the kernels told as lived experience.

**Record entries** (one file each, as earlier entries in `Plan/runs/ingest-325/readings/`):

- **`c16-kael-origin`**: the narrator, a fragment of the void that joins a cluster, becomes Component 734 inside AEGIS (L71) — say which recorded position it sits nearest (row 4), deciding nothing; the manuscript does not name Kael.
- **`q7-what-734-names`**: Component 734 as the narrator's identity inside AEGIS, a boundary filter (L71).

**Not promoted:** Verlöschen, Selbstverstärkung, the Great Realignment, the K₁-field; the borrowed concepts (autopoiesis, Hamartia, coherence and correspondence theories of truth).

**One reader**: aegis, genesis, ueberwelt, komponente-734, nichts-rauschen, dkt, and the C16 and Q7 entries.

**Chapter readings**: none — the manuscript names no chapter.
