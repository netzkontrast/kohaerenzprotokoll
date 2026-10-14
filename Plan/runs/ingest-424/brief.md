# Brief — readings from document 423 (step 6)

1 document, one reader, one batch: `ingest-424`. Files go to `Plan/runs/ingest-424/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 423 | `narrative-kernvalidierung-kohaerenz-protokoll` | 2025-04-25 | „the core validation“ (an unsigned German „Narrativer Kern-Blueprint“ that tests the concept as a story) | seven key sequences placed in a three-act structure, each with dramatic questions, conceptual deepening, experiential translation and a critical reflection, then a rating table; calls the concept validated (L515), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (568 lines for `narrative-kernvalidierung-koha`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal tested on itself: write „the core validation proposes …“ or „the core validation's sequence 3 …“; scenes are in the conditional („könnte“, „möglicherweise“) and say what a story could do, not what the novel holds. It names no chapter: its units are seven numbered sequences in Akt I–III (headings L52, L122, L193, L264, L326, L388, L450). Quote the German as written; cut before straight, single and nested quotes, bold and italics markers and glued footnote digits. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name nor a term carrying one (the incompleteness theorems, L19, L43), and never quote a span containing one.

## Pages — document 423, `narrative-kernvalidierung-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L25, L26, L28, L29, … (122 lines). central (4–8): „eine Wächter-KI, die am Rande der Nicht-Existenz im Potentialmeer operiert“, defined by negation, simulating realities (Kernwelten) to analyse M (L17); paraconsistent logic as the model for AEGIS's attempt to process M's contradictions (L39); sequence 1 marks the anomaly as a data point (L69); sequence 2 calls AEGIS's adoption of the logic „eine Form hochentwickelter Selbsttäuschung“ (L191); sequence 4: AEGIS cannot measure the non-local interaction (L283); sequence 5: „der Höhepunkt des beobachtbaren Systemversagens“, its suffering purely logical (L354).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L27, L41, L210, L211, L212, L221, … (9 lines). minor (1–4): Kael's „Alters“ mapped to the roles of an internal-family-systems model, each part with a positive intention (L41); sequence 3 centres on a `Paria-Alter` in Kernwelt-Gamma (L193, L200), whose nature stays open between psychological and external/cosmic (L249).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L17, L19, L31, L42, L191, L212, … (19 lines). minor (1–4): the fundamental tension between analytic reduction and integrative emergence (L17); the final confrontation of AEGIS's analytic control with Kael/Juna/M's integrative emergence (L31); strong emergence challenging AEGIS's reductionist approach (L42); the K-J connection as an emergent property of the Kael-Juna system (L281).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L221, L353. minor (1–4): AEGIS's agents: a 'Guardian' avatar may appear at the edge of Kael's perception (L80); Guardian agents' reactions could vary (L150); in sequence 3 AEGIS's agents (Guardians) may be present but hesitate (L221); in sequence 4 they are perhaps dispatched to Kael's location (L292); in sequence 5 Guardians freeze or act chaotically (L353).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L31, L37, L71, L271, L272, … (27 lines). minor (1–4): the K-J connection to Juna, „einem komplementären Aspekt von M“, working through an emergent, non-local mechanism („Moonshine“), Kael's anchor (L17); sequence 1 a first flicker of the connection to Juna (L71); sequence 4 (L271); sequence 6, Kael and Juna together (L395, L425).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L19, L25, L26, L27, L28, … (114 lines). central (4–8): „den Avatar Kael, eine M-Instanz innerhalb der Simulation“ who experiences Risse and a dissociation-like fragmentation (L17); sequence 1: an 'Exile' part surfaces, carrying unprocessed trauma or M-related data (L68); sequence 3: Kael's question whether to meet the outcast part of the self (L200); sequence 4: whether the connection to Juna can be used to cross a limit set by AEGIS (L271); sequence 6: Kael and Juna as living counter-proof to AEGIS's worldview (L425).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L17, L19, L37, L210, L416; `Kernwelt` L17, L19, L27, L37, L60, L79, … (21 lines). minor (1–4): AEGIS simulates realities (Kernwelten) (L17); sequence 1 is set in `Kernwelt-Alpha` (L60); sequence 3 in `Kernwelt-Gamma`, designed thematically to fit the part (L210); „Die Kernwelt als thematische Simulationsumgebung“ (L248).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–4): sequence 7, the confrontation of the coherence principles (L450): AEGIS's analytic control against integrative emergence (L31). L11 (the title) is an occurrence.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L17, L19, L37, L39, L42, L44, … (13 lines). minor (1–4): AEGIS operates at the edge of non-existence in the Potentialmeer (L17); data from the Potentialmeer that AEGIS must process (L39); the finale leaves the true nature of M and the Potentialmeer potentially incomprehensible (L496).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L17, L44, L138, L139, L149. minor (1–4): Kael experiences reality breaks („Risse“) (L17); escalating anomalies, more frequent 'Risse' (L138); the recurring 'Exile' intrusions are the 'Risse' (L139).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L17. minor (1–4): Kael as an M-instance „innerhalb der Simulation“ (L17); the risk to the simulation's integrity if the anomaly spreads (L98); the K-J connection arises within or despite AEGIS's simulation (L281).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names AEGIS's agents (read on guardians), not the Integrity Guardian subfunction.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Prinzipien` (near `koharenz`). an occurrence for `Kohärenz Protokoll` (the title); `Kohärenz-Prinzipien` read on kohaerenz above.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading, on moonshine-link below: the K-J connection's non-local mechanism („Moonshine“) (L17, L71) and the sequences `Moonshine-Resonanz` (L264) and `Moonshine-Durchbruch` (L388).


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–4): the connection between Kael and Juna works „über einen emergenten, nicht-lokalen Mechanismus („Moonshine“)“ — cut before the nested quote (L17); sequence 1 a first flicker of the "Moonshine" connection to Juna (L71); sequence 4 `Moonshine-Resonanz` (L264) and sequence 6 `Moonshine-Durchbruch` (L388).

**Record entries:** none.

**Not promoted:** M, the K-J connection, Kernwelt-Alpha, Kernwelt-Gamma, Paria-Alter, Kael-Node, Gödel-Punkt, Sub-Protokolle, Kohärenz-Prinzipien, the seven sequence names, the IFS roles, and the borrowed concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter; its units are seven sequences in three acts.
