# Brief — readings from document 253 (step 6)

1 document, one reader, one batch: `ingest-253`. Files go to `Plan/runs/ingest-253/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 253 | `romanentwurf-kapitel-1-ausformulierung` | 2025-04-19 | „the chapter-1 draft“ (unsigned German prose) | „Kohärenz Protokoll – Teil 1, Kapitel 1“: the same chapter-1 text as document 245's Kapitel 1 (L353–L413 there) — every body line from L18 on stands verbatim in 245, and L17 differs in two words — plus 33 web references; a near version, light pass |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (112 lines for `romanentwurf-kapitel-1-ausform`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: a near version of document 245's Kapitel 1, read onto the pages there. No readings are written; the census and note stand as the record that it was read. The two-word difference at L17 (`Depersonalisation` … `pilotiert` against 245's wording) changes no page's reading.

## Pages — document 253, `romanentwurf-kapitel-1-ausformulierung`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L31. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L63, L90. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L39, L51. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L90. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L21, L27, L29, L43, L53. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L25, L29, L31, L33, … (13 lines). not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L41, L69. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L35, L61, L71, L73. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L27, L31, L39. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L41; `Risse` L37, L51, L57. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L57, L59. not read: a near version of document 245's Kapitel 1, already read onto this page from 245.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: a near version of 245's Kapitel 1; not read.
- `did`: `Fragmentierung` (near `psychischefragmentierung`). occurrence: a near version of 245's Kapitel 1; not read.
- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence: a near version of 245's Kapitel 1; not read.
- `kaels-wohneinheit`: `Wohneinheit` (near `kaelswohneinheit`), `Wohneinheit` (near `kaelswohneinheit10`). occurrence: a near version of 245's Kapitel 1; not read.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: a near version of 245's Kapitel 1; not read.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence: a near version of 245's Kapitel 1; not read.
- `personas`: `Depersonalisation` (near `persona`). occurrence: a near version of 245's Kapitel 1; not read.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence: a near version of 245's Kapitel 1; not read.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: a near version of 245's Kapitel 1; not read.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). occurrence: a near version of 245's Kapitel 1; not read.


**Record entries:** none — 245's entries (Q3, Q4, C9) cover this text.

**Not promoted:** nothing new.

**No reader**: no readings are written.

**Chapter readings**: none — Kap 1 already carries 245's reading of the same text.
