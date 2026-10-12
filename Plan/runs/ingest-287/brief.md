# Brief — readings from document 286 (step 6)

1 document, one reader, one batch: `ingest-287`. Files go to `Plan/runs/ingest-287/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 286 | `entwickle-einen-neuen-plot-der-sich-ueber-13-kurz` | 2025-04-17 | „the Seelen-Kohärenz blueprint“ (an unsigned German reply) | a reply reviewing a request for a new three-part plot and giving a „Neuer Plot-Blueprint“ titled „Das Seelen-Kohärenz-Protokoll“: thirteen persona episodes with growing cracks, the Hüter intervening from the Überraum, and a hunt for an outside solution that worsens the cracks until the solution turns inward; it calls itself an attempt (L267), an early stage of the project |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (268 lines for `entwickle-einen-neuen-plot-der`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A blueprint from an early stage: write „the Seelen-Kohärenz blueprint proposes …“; its personas (Der Architekt, Das Echo, Der Wächter …) and Hüter are its own figures, not the later alters. Quotations avoid digits (`Plotpunkt 1.1` → `Plotpunkt.1`).

## Pages — document 286, `entwickle-einen-neuen-plot-der-sich-ueber-13-kurz`

- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L24. not read: occurrence — `Kohärenz` (L24) in the review's general sentence.
- **`kohaerenz-programm`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz-Programm` alone on L17. minor (1–3): the higher program that fails, the `Seelen-Kohärenz-Programm`, the fragmentation of a simulated consciousness causing its errors and cracks (L17, L38).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L261. minor (1–3): the final state „funktionaler Multiplizität“, an open end regarding the simulation (L261).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L137, L195. minor (1–3): the control room „Schaltzentrale/Kontrollraum/Nexus“ of the Hüter in the Überraum (L137).
- **`personas`** (minor, 1–4): the census's surfaces — `Personas` L26, L28, L113, L151, L164, L183, … (9 lines). central (3–6): each plot point of part 1 giving a persona its reality (L42–L57); the personas as passive receivers or active participants, a question (L26); the Hüter giving them integration tools (L164).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L38. not read: occurrence — `Realitätsebene` (L38) in the premise sentence, read on kohaerenz-programm.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L17, L24, L38, L113, L129, L137, … (16 lines); `Glitches` L46, L113. central (3–6): cracks in the simulated reality from the fragmentation (L38); a creative act unintentionally causing a larger rift (L107); growing more frequent and stronger (L113); „Die Risse sind nicht nur Fehler im Raum-Zeit-Gefüge“ (L209); the hunt causing or worsening them (L248).
- **`ueberraum`** (minor, 1–4): the census's surfaces — `Überraum` L11, L17, L25, L127, L136, L150, … (9 lines). central (3–6): part 2, „Intervention aus dem Überraum“ (L127); the Hüter der Realitäten there (L136); the control room (L137).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L17, L113, L121, L129, L149, L150, … (12 lines). minor (1–3): the simulation and its premise (L38); the solution beyond the simulation (L222); an open end regarding the simulation (L261) — read here only as far as the lines speak of the simulation as a whole.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis`: `Der Wächter` (near `wachterdersystemischenstabilitat`). occurrence: `Der Wächter` is a persona of this blueprint, not AEGIS.
- `kohaerenz`: `Seelen-Kohärenz-Programm` (near `koharenz`), `Das Seelen-Kohärenz-Protokoll` (near `koharenz`). occurrence: the program's and the blueprint's names.
- `kohaerenz-programm`: `Seelen-Kohärenz-Programm` (near `koharenzprogramm`). reading: `Seelen-Kohärenz-Programm` (L17, L38).
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Der Architekt` a persona.
- `multiplizitaet`: `funktionaler Multiplizität` (near `multiplizitat`). reading: `funktionaler Multiplizität` (L261).
- `residual-echos`: `Das Echo` (near `residualechos`). occurrence: `Das Echo` a persona.


**Record entries:** none.

**Not promoted:** the personas (Der Architekt, Das Echo, Der Wächter, Der Funke …), the Hüter der Realitäten, the Seelen-Kohärenz-Protokoll as a title, NZT-Modus, the M/R/P-Modi, the plot-point fields.

**One reader**: every page above.

**Chapter readings**: none — the document numbers plot points, not chapters.
