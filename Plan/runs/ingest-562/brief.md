# Brief — readings from document 562 (step 6)

1 document, one reader, one batch: `ingest-562`. Files go to `Plan/runs/ingest-562/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 562 | `coherence-critique-and-question-generation` | 2025-11-13 | „the coherence critique“ | a developmental-edit critique of an earlier manuscript (the Genesis and Krise arcs) with revision questions; it reports and asks, never canon|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (311 lines for `coherence-critique-and-questio`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A critique of a manuscript: write „the coherence critique reads the manuscript as …“ or „asks …“; its hypotheses stay hypotheses. **Never cite** the lines on the manuscript's creator and tooling (L22, L50, L56–L60, L300) nor lines with a real person's name (L38, L42, L109). Quote no gendered pronoun.

## Pages — document 562, `coherence-critique-and-question-generation`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L36, L38, L40, L42, L72, … (27 lines). central: AEGIS as antagonist, coherence theory of truth (L72); epistemological blindness to qualia (L36); creating the Überwelt as an immune system to test signatures (L174).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L133. not read: `Emergenz` in its general sense (L133).
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L54, L87, L91, L113, L148, L172, … (9 lines). minor: the Genesis arc as a prologue of the whole (L54).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L50, L73, L75, L86, L109, L118, … (16 lines). central: protagonist, correspondence theory of truth (L73); the 'Ich' later Kael (L75); asks whether Kael is a simulation (L179); recommends Kael be one of the shards (L272).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: L13 is a heading.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L168, L172, L174, L180, L211, L241. minor: the 'Ich' replaced by a function (L172); asks whether it starts the simulation (L180).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L180. not read: `Persona` in passing (L180).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L52, L54, L134, L174, L246. minor: the separation protocol fragments the 'Ich' at the arc's end (L52).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L172, L173, L174, L179, L181, L227, … (7 lines). minor: a simulation created by AEGIS (L172–L174); asks whether the rest of the novel is set inside it (L179).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokoll 1.0` (near `koharenz`), `Kohärenz Protokoll 2.0` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). an occurrence: titles and named paradoxes.
- `nichts-rauschen`: `Nichts` (near `nichtsrauschen`). an occurrence: `Nichts` as a word.
- `residual-echos`: `Echos` (near `residualechos`). an occurrence: `Echos` as felt states.


**Record entries:** none.

**Not promoted:** the Dramatica table, Kohärenz Protokoll 1.0/2.0, the Paradoxon der Fehlausgerichteten Kohärenz, the fremde Entität, Scherben, Dazwischen, the revision questions.

**One reader**: every page above.
