# Brief — readings from document 86 (step 6)

1 document, one reader, one batch: `ingest-86`. Files go to `Plan/runs/ingest-86/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 86 | `kohaerenz-protokoll-kapitel-outline-generierung-2` | 2026-04-30 | „the dual-storyform outline of Kap 1–39“ (titled `39-Kapitel-Outline mit Dual-Storyform-Encoding`) | a German chapter outline of 2026-04-30 in three acts (L59, L171, L281): essay sections on the physics, the two Dramatica storyforms (A „Heuristics of Integration“, B „Phoenix Collapse“, L13, L25) and a ten-row alter table (L41–L55), then every chapter with a summary, a `Storyform B` and a `Storyform A` line, a `Szenen-Keim` and a `Pacing` label; it says it „operationalisiert den Struktur-Kanon-Reset vom“ 30 April 2026 (L13) and cites numbered references; not the same text as document 78 (no shared line) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (415 lines for `kohaerenz-protokoll-kapitel-ou`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the dual-storyform outline plans …“, never as what the novel is. Its claim to implement a Struktur-Kanon-Reset (L13) is recorded once, on `kael` or `aegis`, never applied. The trailing reference digits glued to sentences (`…Entropie verschwimmen.1`) are footnote marks, not numbers: quote around them. The export lost every formula and kernel symbol (empty `()` at L17, L37; cells starting `\-` at L46, L49, L55): quote around the gap, never fill it. The storyform lines name Dramatica positions (`IC: Mind/Memory`): quote them as the outline's encoding. Chapter content goes on the chapter pages (a later batch): on a term page, at most one or two beats by chapter number.

## Pages — document 86, `kohaerenz-protokoll-kapitel-outline-generierung-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L21, L25, L37, L41, L61, … (43 lines). central (4–6): AEGIS in the essay sections (the kernels L17, the storyforms L25) and its arc through the acts — traumatised by the loss of its makers (Kap 31, L319), the Vortex (Kap 27–35, L285 on), the Vortex-Mechanik section (L389 on).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L47. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L37, L256. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L41, L148, L158, L237, L274, L298, … (8 lines). minor (2): the ten-row alter table (L44–L55) with its columns TSDP-Aktionssystem, Funktionale Rolle and DKT-Korrelat; the alters as the chapters use them.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L55. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L183. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`dkt`** (minor, 1–4): the census's surfaces — `Dual-Kernel-Theorie (DKT)` L17. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L13, L17, L53, L57, L173, L283, … (9 lines). minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L135. minor (1): Kael's „wahre Genesis“ (L135) — a reading on `genesis` only if the page's sense is Kael's origin; else an occurrence, say why.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L52. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L31, L37, L48, L81, L83, … (31 lines). central (3–5): Juna in the essays (L17, L31, L37) and the chapters — `Die Juna-Anomalie` (Kap 3), Silas as „Juna-induzierte Korruption“ (L132), Juna-Resonanz as Rhys's DKT correlate (L48).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L25, L30, L39, L41, L65, … (75 lines). central (4–6): Kael as a TSDP system (L41), the goal `Funktionale Multiplizität` (L57), „Komponente 734“ as his true genesis (Kap 9, L135); the Struktur-Kanon-Reset claim once (L13).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L50, L94, L234. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the novel's title (L11, L13) — occurrence (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L17. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L17. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L135. minor (1): „Komponente 734“ as Kael's true genesis, hinted (Kap 9, L135).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17, L61, L168, L225, L370. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L46, L107, L110, L193, L195. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L51. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L154, L156, L250. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L122, L199, L201, L303, L325, L357. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine Link` L33. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L53, L143. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L57. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L367. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L124, L175. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L49, L146, L148, L234. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L41, L317, L319. minor (2): Kap 31 — „Der systemische Trojaner Oblivion erwacht“ (L319); L41.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L48. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L17, L109, L227, L234, L295. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L54. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L130, L132, L134, L148. minor (2): Kap 9, `Das Echo von Silas` — Silas „den Archivar“ and „eine Juna-induzierte Korruption“ (L132), and L148.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L266. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L349. minor (1): Kap 35, `Der Vortex-Pivot — Die Truth-Rotation` (L349).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L41, L45, L173. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L17. not read unless a line uses `Simulation` for the Überwelt itself: the sweep's hit at L17 is the outline's „duale Simulationsarchitektur“ sense — occurrence, say why.
- **`vortex`** (minor, 1–4): the census's surfaces — `Vortex` L285, L333, L335, L341, L349, L389, … (7 lines). minor (2–3): the Vortex chapters (Kap 27 L285, Kap 35 L349) and the section `Die Mechanik des Vortex und das Ouroboros-Leitmotiv` (L389 on).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence (J69): `Guardian` is not the Integrity Guardian.
- `guardians`: `Guardian` (near `guardians`). a reading on `guardians` only if a line says what the guardians are or do; else occurrence.
- `hitze-polaritaetsregel`: `Hitze` (near `hitzepolaritaetsregel`), `Hitze` (near `hitzepolaritatsregel`). occurrence: `Hitze` alone is the word, not the rule (J12).
- `kohaerenz`: `Zielkohärenz` (near `koharenz`). occurrence: `Zielkohärenz` is a compound of its own (J12).
- `personas`: `Bewusstsein` (near `bewusstseinsinstanzen`). occurrence (J69): `Bewusstsein` is not Bewusstseinsinstanzen.
- `sektor-04`: `Sektor 0` (near `sektor04`). occurrence unless the line names Sektor 04: `--find` drops the digit; check the line with `read.py --from/--to`.


**Record entries** (find the lines; one file each; write one only where the outline says something on the record's question):

- **`q3-how-many-kern-welten-and-alters`**: the ten-row alter table (L44–L55).
- **`q7-what-734-names`**: „Komponente 734“ (L135).
- **`c16-kael-origin`**: Kael's „wahre Genesis“ as Komponente 734 (L135).
- **`q8-aegis-after-the-vortex`**: what the Vortex chapters (Kap 27–39) plan for AEGIS.
- **`c7-juna-first-appearance`**: where the outline first puts Juna in a chapter (Kap 3 `Die Juna-Anomalie`, L81 on).

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, entropie, negentropie, dkt, kohaerenz-kernel, kollaps-kernel, chaitin-konstante, konstrukt-stadt, logos, mnemosyne, nexus, moonshine-link, risse, vortex, truth-rotation, trennungsprotokoll, algorithmische-melancholie, genesis, komponente-734, ueberwelt, guardians, sektor-04, and the five records.
- Reader 2: the alters' pages (alters, alex, argus, isabelle, kiko, lex, lia, moros, nyx, rhys, selene), silas, oblivion, multiplizitaet, tsdp.
