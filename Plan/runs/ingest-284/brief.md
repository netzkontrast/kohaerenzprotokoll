# Brief — readings from document 283 (step 6)

1 document, one reader, one batch: `ingest-284`. Files go to `Plan/runs/ingest-284/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 283 | `tropen-konzepte-fuer-kohaerenz-protokoll` | 2025-05-04 | „the trope analysis“ (an unsigned German analysis) | an analysis of the philosophical concepts and the narrative and genre tropes of a 39-chapter outline it calls „Outline V3“, each tied to chapters by bracketed `Ch` pointers and two summary tables, with Kael, AEGIS, Juna/V, Fundament/Leere and the Konstrukt-Welten as anchors; a „kritische Vorstufe“ (L17), hedged throughout, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (357 lines for `tropen-konzepte-fuer-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis: write „the trope analysis ties / reads / proposes …“; its concept definitions are its summaries of cited sources, not claims about the novel; keep its hedges (`implizit`, `wahrscheinlich`). The outline it analyses is not reproduced. Cut quotations before bold markers, glued reference digits and the escaped `\[Ch N\]` pointers.

## Pages — document 283, `tropen-konzepte-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L16, L29, L30, L31, L33, L42, … (50 lines). central (3–6): managing a simulated reality, maintained because of its core paradox, the `Fehlausgerichtete Kohärenz` (L29, L88); its faulty method causing the Glitches (L29); its origin as emergence (L31); manipulating Kael's perception by gaslighting (L42, L138); „AEGIS repräsentiert eine antagonistische KI“ with a potentially tragic aspect (L65); brought down by its own paradoxical logic (L143); whether it is conscious, a question (L60).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L52. minor (1–3): among Kael's parts named (L52).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L52. minor (1–3): among Kael's parts named (L52).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L31, L89, L105, L201, L202. minor (1–3): the origin of AEGIS and possibly Juna/V as emergence (L31); the table row (L105).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L90. not read: occurrence — `Entropie` (L90) as a concept of information theory.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L16. minor (1–3): „eine Entität, die fundamental extern und potenziell unerkennbar ist“ (L78); non-algorithmic intelligence (L126); the external entity in the summary (L202).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L16, L29, L31, L32, L41, L42, … (52 lines). central (3–6): the journey beginning in chapter 1 (L29); the parts based on TSDP, from fragmented dissociation to potential integration (L52); Lex his logical part (L43); amnesia and Mnemosyne's manipulation (L53); his journey through the KWs (L67).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L43, L52, L142. minor (1–3): „Kaels logischer Anteil“ trying to understand KW1 by reason (L43).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L44, L53. minor (1–3): „Mnemosynes potenzielle Manipulation von Erinnerungen“ (L44), challenging memory (L53).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L52. not read: occurrence — `Multiplizität` at L52 is read on kael.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L30. minor (1–3): the Leere glossed, the Fundament as deepest reality level, their relation not a simple dichotomy (L30), only as far as the line names the Nichts Rauschen.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L52. minor (1–3): among Kael's parts named (L52).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L29. not read: occurrence — `Realitätsebenen` (L29) in a general sentence.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L52. minor (1–3): among Kael's parts named (L52).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L29. minor (1–3): the Glitches Kael perceives, caused or worsened by AEGIS's faulty method or arising from his own consciousness (L29); the trope „Glitch in the Matrix“ (L42).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L52, L67. minor (1–3): named with the potential integration (L52); L67 only if it adds.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L52, L127, L139, L140. minor (1–3): the parts „basieren explizit auf der“ TSDP (L52); L127, L139–L140 only if they add.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: occurrence — `Simulation` (L29) the simulation in general.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` a general concept.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Fehlausgerichtete Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence: the title; `Fehlausgerichtete Kohärenz` read on aegis.
- `personas`: `Transpersonale Psychologie` (near `persona`). occurrence: `Transpersonale Psychologie` a field.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` not the world.
- `risse`: `Glitch in the Matrix` (near `glitch`), `Glitch Art` (near `glitch`). reading: `Glitch in the Matrix` as the trope of the Glitches (L42); `Glitch Art` an occurrence.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: `Simulationshypothese` a borrowed concept.


**Record entries:** none — the document counts no worlds or parts and takes no position on an open record beyond its readings.

**Not promoted:** the concepts and tropes as such (Simulationshypothese, Gaslighting, Perverse Instantiation, Hoist by His Own Petard, Philo Hint …), Outline V3, the Konstrukt-Welten as a label.

**One reader**: every page above, and the chapter readings below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-284-kap/readings/kap-NN--tropen-konzepte-fuer-kohaerenz-protokoll.md`, kap-00 for the Prolog): for each chapter the document ties a concept or trope to with a `Ch N` pointer or a table row, one bullet naming what it ties there, with the line — e.g. „Kapitel 29 stellt explizit ein ethisches Dilemma dar“ (L79). Read the pointers from the body (L27–L146) and the two tables (L100–L121, L177–L197). One bullet per chapter; combine several pointers to one chapter into it. Each ends „An analysis of an outline it does not reproduce.“
