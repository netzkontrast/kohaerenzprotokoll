# Brief — readings from document 516 (step 6)

1 document, one reader, one batch: `ingest-516`. Files go to `Plan/runs/ingest-516/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 516 | `existenzforschung-fuer-roman-kohaerenz-protokoll` | 2025-10-15 | „the existence research compendium" (an unsigned German compendium) | a five-part compendium of philosophy, cosmology, quantum physics, abiogenesis, consciousness and simulation theory (L11) that reads the title „Kohärenz Protokoll“ as a rule set in conditional sentences (L107, L268, L341, L349); it names no figure, place or event of the novel (AEGIS, Kael, Juna each 0); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (386 lines for `existenzforschung-fuer-roman-k`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: a general research compendium that names nothing of the novel; its readings of the title as a rule set are general and conditional.

## Pages — document 516, `existenzforschung-fuer-roman-kohaerenz-protokoll`

- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L190. not read: light pass — the compendium's general use; it names nothing of the novel.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L152. not read: light pass — the compendium's general use; it names nothing of the novel.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L71, L73, L75, L79, … (39 lines). not read: light pass — the compendium's general use; it names nothing of the novel.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L109, L336, L356; `Glitches` L336. not read: light pass — the compendium's general use; it names nothing of the novel.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L69, L107, L318, L320, L322, L324, … (19 lines). not read: light pass — the compendium's general use; it names nothing of the novel.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). an occurrence: the compendium's general vocabulary, light pass.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). an occurrence: the compendium's general vocabulary, light pass.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). an occurrence: the compendium's general vocabulary, light pass.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). an occurrence: the compendium's general vocabulary, light pass.


**Record entries:** none.

**Not promoted:** the compendium's philosophy, cosmology, physics, abiogenesis, consciousness and simulation vocabulary, its four-level definition of the title as a rule set, and the borrowed concepts (several named after people).

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
