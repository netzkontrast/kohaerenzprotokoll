# Brief — readings from document 456 (step 6)

1 document, one reader, one batch: `ingest-456`. Files go to `Plan/runs/ingest-456/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 456 | `kosmischer-horror-in-kohaerenz-protokoll` | 2025-04-25 | „the cosmic-horror analysis“ (an unsigned German analysis brief carrying out an NZT directive it does not reproduce) | reports eight principles of cosmic horror from its sources, maps them onto the novel's concepts in a table, then gives imperative strategies (`Verstärkung`) and guidelines; proposals and instructions, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (197 lines for `kosmischer-horror-in-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that instructs: write „the cosmic-horror analysis proposes …“; its `Verstärkung` lines are imperatives to the writer, never canon; the genre principles (L15–L60) are reported from its sources and stay off the pages. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „Seine“). Never write a real person's name nor a genre named after one, nor quote a span containing one; cut before straight or single quotes.

## Pages — document 456, `kosmischer-horror-in-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L73, L74, L79, L88, L93, L97, … (24 lines). central (4–8): AEGIS as a vast, non-human AI existing by negation (L97); its existence by negation can be shown as deeply uncanny (L98); its fragility heightens cosmic fear (L74); a possible realisation that AEGIS's logic is flawed (L177).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L76, L111, L115. minor (1–4): Kael/Juna joined in the table row and heading (L76, L111); the K-J connection as a source of disturbance (L116) and of resilience (L171) — the document gives both and does not reconcile them.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L76, L107, L111, L115, L116, L137, … (15 lines). central (4–8): what the analysis takes for Kael: fragmented psyche, avatar status, integration process (L115); use the K-J connection to bring in disturbing, inexplicable phenomena (L116); the connection as anchor or source of resilience amid cosmic fear (L171); Kael must make meaningful decisions (L171).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L78, L88, L133, L134, L176; `Kernwelt` L78, L88, L133, L134, L150, L176. minor (1–4): the core worlds read as simulations, inherently fragile realities (L78); a plot strategy asks for a direct but incomprehensible manifestation of M in a Kernwelt (L150).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title and the document's tonal coherence.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L73, L78, L80, L84, L98, L124, … (15 lines). central (4–8): the Potentialmeer as a pre-real space of unstructured potentiality embodying the genre's unknown (L88); the table's „Verkörperung der unbegreiflichen Prä-Realität“ (L73); describe it as a seething, paradoxical void (L89); leave key aspects of M and the Potentialmeer undefined (L166); knowledge limits as the inability to understand M/Potentialmeer (L80).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L177. not read: an occurrence — `Simulation` on L177 is the simulated reality, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Tonale Kohärenz` (near `koharenz`). an occurrence: the title and `Tonale Kohärenz`, the document's own term.
- `personas`: `Depersonalisation` (near `persona`). an occurrence: `Depersonalisation` is a symptom word.
- `ueberwelt`: `Simulations-Horror` (near `simulation`). an occurrence: `Simulations-Horror` is a genre label.


**Record entries:** none.

**No chapter readings**: the analysis names no chapter.

**Not promoted:** Kernkonflikt, Wissensgrenzen, Verstärkung, NZT-Direktive, Nutzeranfrage, Tonale Kohärenz, Simulations-Horror, the genre principles and the borrowed concepts (several carry people's names).

**One reader**: every page above.
