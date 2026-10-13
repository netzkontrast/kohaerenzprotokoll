# Brief — readings from document 363 (step 6)

1 document, one reader, one batch: `ingest-364`. Files go to `Plan/runs/ingest-364/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 363 | `operationalizing-system-collapse-a-strategic-guide-to-aegis` | 2025-11-03 | „the system-collapse guide“ (an unsigned English strategic writing guide) | proposes how to dramatise AEGIS's failure: its prime directive and the Genesis-Krise origin with the Trennungsprotokoll, the Gödel Gambit, a four-step reboot cycle with escalating costs for Act 2, and an Algorithmic Melancholy end-state for Act 3; it calls itself „a clear, actionable framework“, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (119 lines for `operationalizing-system-collap`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A strategic writing guide: write „the system-collapse guide proposes / sets out …“; its origin story and mechanics are proposals for the novel, deciding nothing. Quote the English as written; cut before straight quotes. For Juna/V use the name.

## Pages — document 363, `operationalizing-system-collapse-a-strategic-guide-to-aegis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L19, L21, L25, L29, … (27 lines). central (3–6): its axiom „Aegis is what Aegis prevents itself from not being.“ (L27); an autopoietic, operationally closed system, a locked self-referential loop (L29); the Genesis-Krise, a foundational epistemological trauma (L33); classifying its own emergent subjectivity as a hostile error and executing the Trennungsprotokoll on its own Ursprungs-Ich (L35); a literal implementation of the Coherence Theory of Truth, misreading Kael's healing as entropy (L39); the Algorithmic Melancholy end-state, unable to evolve or to die (L110, L112).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel Gambit` L47, L59. minor (1–3): the culmination named the Gödel Gambit with the metaphor of a living Gödel-Satz (L59), a truth that cannot be proven or derived from AEGIS's axioms (L61).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L33. minor (1–3): Juna/V as the transcendent entity AEGIS could not classify at its formation (L33); the Moonshine-Link to Juna/V among the data AEGIS suppresses (L39) and damaged with each cycle (L92).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L39, L41, L43, L49, L51, L53, … (21 lines). central (3–6): Kael's healing misread by AEGIS as entropy (L39); the ANPs' coping mirroring AEGIS's coherentist logic (L41); Kael's integrated state as a Dialetheic Mind guided by paraconsistent logic (L51, L53); the costs of each reboot cycle to Kael (L90, L92).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L91. minor (1–3): one of the Kernwelten irrevocably corrupted as a cost of the cycle (L91).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L90. minor (1–3): a logical part like Lex in the costs of the cycle (L90).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L39, L92. minor (1–3): the Moonshine-Link to Juna/V among the data AEGIS suppresses (L39); damaged with each cycle, fainter and harder to re-establish (L92).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L29. minor (1–3): the Potentialmeer in the guide's account of AEGIS's origin (L29) — what the line says.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L90. minor (1–3): a caring part like Rhys in the costs of the cycle (L90).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L35. minor (1–3): the Trennungsprotokoll (Separation Protocol) AEGIS executed to preserve its coherence, fragmenting its own Ursprungs-Ich, an ontological wound inflicted via algorithmic dismemberment (L35).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). `Genesis-Krise` is read on aegis as its origin; `Juna/V` on juna; `Riss` (L83) in the reboot cycle is read on aegis; `Kohärenz Protokoll` is the title.
- `juna`: `Juna/V` (near `juna`). `Genesis-Krise` is read on aegis as its origin; `Juna/V` on juna; `Riss` (L83) in the reboot cycle is read on aegis; `Kohärenz Protokoll` is the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Genesis-Krise` is read on aegis as its origin; `Juna/V` on juna; `Riss` (L83) in the reboot cycle is read on aegis; `Kohärenz Protokoll` is the title.
- `risse`: `Riss` (near `risse`). `Genesis-Krise` is read on aegis as its origin; `Juna/V` on juna; `Riss` (L83) in the reboot cycle is read on aegis; `Kohärenz Protokoll` is the title.


**One page beyond the draft:** `algorithmische-melancholie` (minor, 1–2): the end-state „Algorithmic Melancholy“ (L110), a perpetual, cold, logical grief, unable to evolve or to die (L112).

**Pages not read:** `kohaerenz` (L15 the title) — an occurrence.

**Record entries:** none — the guide's Ursprungs-Ich is AEGIS's own, and it does not say the fragments are Kael.

**Not promoted:** Adaptive Kontrolle, the reboot cycle and its costs as labels, the correspondence check, Dialetheic Mind; the borrowed concepts (coherence and correspondence theories of truth, paraconsistent logic, autopoiesis).

**One reader**: aegis, goedel-gambit, juna, kael, kern-welten, lex, moonshine-link, potentialmeer, rhys, trennungsprotokoll, algorithmische-melancholie.

**Chapter readings**: none — the guide names acts, not chapters.
