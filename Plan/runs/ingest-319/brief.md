# Brief — readings from document 318 (step 6)

1 document, one reader, one batch: `ingest-319`. Files go to `Plan/runs/ingest-319/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 318 | `rechercheauftrag-die-genesis-von-aegis` | 2025-04-27 | „the Genesis-of-AEGIS research order“ (an unsigned German research brief) | a `Rechercheauftrag` for a short story on AEGIS's origin: three research areas — the Potentialmeer, AEGIS's emergence from the „Reste“ of failed predecessors, the Überwelt and the Kernwelten-Methodik — set out mostly as questions, then the story's requirements and expected result; a prompt, light pass, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (115 lines for `rechercheauftrag-die-genesis-v`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a research order — a prompt that asks questions and sets requirements for a story still to be written; it states nothing of the world that the narrative it commissions (document 313, `genesis-der-leere`) does not tell. Light pass: the census and note stand as the record that it was read.

## Pages — document 318, `rechercheauftrag-die-genesis-von-aegis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L19, L47, L49, L64, … (23 lines). not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L35. not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L24. not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L15, L77, L79, L94, L100, L104. not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L17, L19, L30, L45, L60, … (15 lines). not read: a research order of questions and requirements, a prompt; it changes nothing on this page.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L15, L77, L79, L84, L90, L100, … (8 lines). not read: a research order of questions and requirements, a prompt; it changes nothing on this page.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis der Überwelt` (near `genesis`). occurrence: a term inside the order's questions; not read in this light pass.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: a term inside the order's questions; not read in this light pass.
- `thermodynamischer-phaenomenalismus`: `Dynamis` (near `thermodynamischerphaenomenalismus`), `Dynamis` (near `thermodynamischerphanomenalismus`). occurrence: a term inside the order's questions; not read in this light pass.


**Record entries:** none.

**Not promoted:** everything — the research areas, the Reste, the Kernwelten-Methodik, Entität M, and the lens (autopoiesis, autocatalysis, Chora, Kolmogorov complexity …).

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
