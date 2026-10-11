# Brief — readings from document 254 (step 6)

1 document, one reader, one batch: `ingest-254`. Files go to `Plan/runs/ingest-254/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 254 | `tropenanalyse-fuer-kohaerenz-protokoll` | 2025-05-01 | „the trope analysis“ (an unsigned German report) | a catalogue of tropes at the crossing of hard SF, cosmic horror and psychological thriller, each with a relevance note for the novel, five clusters, a mapping table and advice in the imperative; its world facts come from a brief it tags `[User Query]`; proposals, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (306 lines for `tropenanalyse-fuer-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of proposals: write „the trope analysis proposes / advises …“. Its recap (L124) restates a brief it tags `\[User Query\]`: say „the brief it recaps“. The mapping of Kern-Welten onto ANP/EP (L100, L161) is its own proposal. `Simulation` mostly names the simulated-reality trope in general: read only lines that speak of the novel's simulation. Cut quotations before reference numbers glued to words and before escaped brackets.

## Pages — document 254, `tropenanalyse-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L29, L30, L32, L44, L45, … (29 lines). central (3–6): „Autonomous Entropic Gatekeeper“ (L91); the controlling AI aiming at entropy minimisation, in the brief it recaps (L124); its core programming (Entropieminimierung) as primary drive, and whether it is conscious or an automaton left open (L169); beyond Skynet or HAL (L153, L202); its methods raising ethical questions (L91).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L159. minor (1–4): the alters within the TSDP frame (L159); only if a line names them of Kael.
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L17, L18, L46, L48, L51, L60, … (30 lines). central (3–6): the premise of a protagonist with DID inside a simulation controlled by AEGIS (L17); DID to be shown as a complex post-traumatic disorder, not as malice or a source of violence (L165); avoiding harmful tropes, consulting the literature (L187, L189); highest care (L218).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L17. minor (1–4): among the novel's themes, „Kontrolle vs. Emergenz“ (L17); the Risse as manifestations of entropy or emergence in the recapped brief (L124).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. minor (1–4): among the novel's themes, „Ordnung vs. Entropie“ (L17); AEGIS's entropy minimisation (L124, L169).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L44, L46, L47, L61, L66, L68, … (14 lines). central (3–6): „eine mysteriöse Verbindung oder Entität“ in the recapped brief (L124); her nature at first unclear — AI fragment, system error, external entity (L171); possibly helper or guide (L171), a mysterious counterweight to AEGIS (L216); her connection to Kael central (L171).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L29, L33, L34, L45, L46, … (40 lines). central (3–6): the protagonist with DID inside the simulation (L17); his parts mappable onto the Kern-Welten (L100); the ANP probably his initial state (L159).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L100, L124, L151, L161. minor (1–4): the Kern-Welten as direct manifestations of the ANP/EP structure: KW1 (Logik) ANP, KW2 (Emotion/Trauma) EPs, KW3 (Abwehr) EP defences, KW4 (Potential) integration (L161, L100); in the recapped brief mirroring Kael's psyche (L124).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L44, L47, L109, L124, L144, L171, … (8 lines). minor (1–4): „als mögliche tiefere Realitätsebene“ in the recapped brief (L124); L109, L144, L171 only if they add.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L124. not read: occurrence — `Realitätsebene` at L124 glosses the Potentialmeer, read on potentialmeer.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L48, L49, L82, L124, L143, L151, … (9 lines). minor (1–4): in the recapped brief system errors or manifestations of entropy or emergence (L124); the trope of glitches in the simulation (L143); narrative and thematic breaking points (L151); feeding both psychological and cosmic horror (L155); where genre borders blur (L175).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L17, L100, L118, L124, L140, L151, … (15 lines). central (3–6): the theory behind the novel's themes (L17); a robust, non-sensational frame for DID (L159); ANP and EP (L100, L159).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L16, L17, L29, L32, L33, L34, … (32 lines). minor (1–4): only the novel's simulation: the simulation controlled by AEGIS (L17); in the recapped brief the simulation consisting of Kern-Welten (KW1-4) mirroring Kael's psyche (L124). The trope lines are not read.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropieminimierung` (near `entropie`). `Entropieminimierung` AEGIS's drive, read on aegis and entropie.
- `nichts-rauschen`: `Nichts` (near `nichtsrauschen`). occurrence: `Nichts` is the existential threat, not the Nichts-Rauschen.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten mapped onto the ANP/EP structure — KW1 ANP, KW2 EPs, KW3 EP defences, KW4 integration (L100, L161); a proposal.

**Not promoted:** the trope catalogue and its clusters, the mapping table, Sensitivity Reader, the advice list, Das Nichts as a page.

**One reader**: kael, aegis, juna, did, tsdp, kern-welten, risse, potentialmeer, ueberwelt, entropie, emergenz, alters and the record q3. `kohaerenz` and `realitaetsebenen` are occurrences.

**Chapter readings**: none — the analysis names no chapter.
