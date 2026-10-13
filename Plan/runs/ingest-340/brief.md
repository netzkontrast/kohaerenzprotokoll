# Brief — readings from document 339 (step 6)

1 document, one reader, one batch: `ingest-340`. Files go to `Plan/runs/ingest-340/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 339 | `aegis-singularitaet-jenseits-entropiegleichung-docx` | 2025-08-05 | „the Singularität album review“ (an unsigned German review, „Eine Expertenrezension“, docx export) | a review of an AI-made concept album about AEGIS and the „Kael-Juna-Phänomen“ in six parts — opening prose, concepts, lyrics, sound, a song-by-song table and a closing judgement — with 77 cited works; a review of a companion work, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (223 lines for `aegis-singularitaet-jenseits-e`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document reviews a concept album, a companion work to the novel; it names AEGIS, the Kael-Juna phenomenon, entropy and the borrowed concepts as the album's subjects and judges the album's songs, lyrics and sound, stating nothing about the novel's world that a page needs. The census and note stand as the record that it was read.

## Pages — document 339, `aegis-singularitaet-jenseits-entropiegleichung-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L17, L19, L21, L27, L29, … (46 lines). not read: named only as a subject of the concept album the review judges.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L47. not read: named only as a subject of the concept album the review judges.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L27, L35, L41, L49, L112, L115, … (9 lines). not read: named only as a subject of the concept album the review judges.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L118. not read: named only as a subject of the concept album the review judges.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L89. not read: named only as a subject of the concept album the review judges.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L27, L35, L115. not read: named only as a subject of the concept album the review judges.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L37, L85, L118. not read: named only as a subject of the concept album the review judges.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L79. not read: named only as a subject of the concept album the review judges.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L39. not read: named only as a subject of the concept album the review judges.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Kael-Juna-Phänomen` (near `juna`), `Kael-Juna-Anomalie` (near `juna`), `Kael-Juna` (near `juna`). occurrence: a song title, an album phrase or the album's subject; not read.
- `kael`: `Kael-Juna-Phänomen` (near `kael`), `Kael-Juna-Anomalie` (near `kael`), `Kael-Juna` (near `kael`). occurrence: a song title, an album phrase or the album's subject; not read.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: a song title, an album phrase or the album's subject; not read.


**Record entries:** none.

**Not promoted:** everything — the album, its songs and phrases (`Dystopian-Clear Twist`, `Logik-Gott`), the Kael-Juna-Phänomen as the album names it, and the borrowed concepts.

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
