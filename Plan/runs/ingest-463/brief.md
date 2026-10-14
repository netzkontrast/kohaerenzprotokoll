# Brief — readings from document 463 (step 6)

1 document, one reader, one batch: `ingest-463`. Files go to `Plan/runs/ingest-463/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 463 | `genesis-logik-krise-zerstueckelung` | 2025-04-29 | „the Genesis analysis“ (an unsigned German critical analysis of the text titled Genesis) | retells the analysed text scene by scene — the spark in the Nichts Rauschen, AEGIS's birth, Komponente 734, the anomaly, the Zerstückelung, Kael — then reads it by theme and through four lenses and evaluates it; an analysis that argues (L25), recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (204 lines for `genesis-logik-krise-zerstuecke`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of another text: write „the Genesis analysis retells …“ for its summaries and „the Genesis analysis reads …“ for its interpretations; keep apart what it reports of the analysed text and what it argues. Its lenses are hedged („kann als“). No gendered pronoun for Kael, AEGIS or 734 — use the names (quotations verbatim). Never write a real person's name; cut before inner „…“, glued scene numbers and italics.

## Pages — document 463, `genesis-logik-krise-zerstueckelung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L25, L41, L43, L47, L51, … (44 lines). central (4–8): the analysed text's course as the crystallisation of a rigid, logic-based system named AEGIS (L17); the birth scene retold, „AEGIS ist geboren.“ (L43); AEGIS the embodiment of pure logic (L95); AEGIS interprets the events only through its own logic (L143); the fragmentation no malicious act, elimination the only option within its logical frame (L151); a hedged lens: AEGIS as allegory of potentially oppressive systems (L165).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L13. not read: an occurrence — L13 names emergence in the analysis's opening in general terms.
- **`genesis`** (central, 3–12 quotations): the census's surfaces — `Genesis` L11, L13, L17, L21, L25, L37, … (15 lines). central (4–8): the analysed text titled Genesis, read as a critical allegory of systemic order (L25); it does without human characters and places (L21); the title points to no completed act of creation (L195); the open ending underlines the text's central thesis (L199).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L25, L55, L59, L69, L73, … (14 lines). central (4–8): in the final scene Kael is no coherent entity (L59); Kael stands for the potential of transformation through trauma (L111); Kael literally born from trauma, within the trauma lens (L169).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title, the spark of coherence and the protocol's name.
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L45, L47, L51, L65, L73, L77, … (13 lines). central (4–8): the original searching fragment exists from then on as Komponente 734 (L47); 734 symbolises the persistence of individual consciousness (L99); further retellings as the census lists them (L45, L51, L65, L73).
- **`nichts-rauschen`** (central, 3–12 quotations): the census's surfaces — `Nichts Rauschen` L17, L31, L69, L73, L85, L89, … (12 lines). central (4–8): the Rauschen described not as passive emptiness but as active, pressing potential (L31); not pure negation but a source of potentiality and dissolution at once (L69); further retellings (L17, L73, L85, L89).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L91. not read: an occurrence — L91 uses a level of reality in a general sense.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L53, L81, L101, L103, L115, L117, … (9 lines). minor (1–4): the Überwelt more than a simulation room (L117); AEGIS confuses its internal logical representation with the world itself (L129); the simulation of the anomaly crashes repeatedly (L125).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). an occurrence: `Anomalie` is the anomaly of the analysed text, not the metric.
- `did`: `Fragmentierung` (near `psychischefragmentierung`). an occurrence: `Fragmentierung` is the analysed text's fragmentation, not the diagnosis.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: the fragment's resonance.
- `kohaerenz`: `Funken Kohärenz` (near `koharenz`), `Funke Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). an occurrence: the spark of coherence (written two ways) and the protocol's name.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` is the fragment's echo.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). an occurrence: the fragment's resonance.


**Record entries** (one file each, formatted as earlier entries):
- **`q7-what-734-names`**: the Genesis analysis retells that the searching fragment exists as Komponente 734 (L47) and reads 734 as the persistence of individual consciousness (L99); recorded.
- **`c16-kael-origin`**: the analysis reads Kael as literally born from trauma, the result of the Zerstückelung of 734 (L59, L169); recorded, not applied.

**No chapter readings**: the analysis works with the scenes of Genesis, not chapters of the novel.

**Not promoted:** Funke / Funken Kohärenz, Zerstückelung, Anomalie, Echo, Resonanz, the scene titles, and the four lenses.

**One reader**: every page above and the two record entries.
