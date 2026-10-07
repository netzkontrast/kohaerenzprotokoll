# Brief — readings from document 201 (step 6)

1 document, one reader, one batch: `ingest-201`. Files go to `Plan/runs/ingest-201/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 201 | `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1` | 2025-04-18 | „the part-1 plot concept“ (an unsigned revision plan) | a German „Finale Plot-Konzeption“ for part 1 that critiques an earlier plot draft (strengths L19–L23, weaknesses L27–L44), sets revision principles for characters, places, the Risse and the DID (L50–L92), then gives revised chapters 1–13 scene by scene — its proposals recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (870 lines for `romanplot-uberarbeitung-kohaer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A revision plan: write „the part-1 plot concept proposes / plans / criticises …“; its hedges (`könnte`, `möglicherweise`, `z.B.`) stay; the chapters are its proposal, not the novel. German — quote as written; the export kept escaped bracket line ranges (`\[1207-1540\]`, `\[565-1183\]`, `\[1-542\]`) — cut every quotation before a `\[`; cut before inner straight quotes and glued digits.

## Pages — document 201, `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L27, L43, L56, L57, L60, … (86 lines); `Entropic Gatekeeper` L43, L484, L559. central (2–5): the Guardian interventions of AEGIS „noch potenziell generisch“ — naming units like Einheit 734 would sharpen AEGIS as Entropic Gatekeeper (L43); in Kap 1 no direct AEGIS intervention, the sterile perfection hints at control (L118); the systemwide wave where AEGIS „reagiert sofort und brutal“ with barriers, drones and Einheit 734 and pursues Kael (L481, L484).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L27, L50, L59, L280, L508, L532, … (31 lines). central (2–5): the plan names further alters of Kael left unused — Limina, Nox, Chronos, Schattenkind (L27); every scene must say which alter is dominant, with inner dialogue between alters (L59); read L280 or L508 for one alter at work.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L27, L50, L56, L82, L242, L266, … (23 lines). central (2–5): „Argus tritt an Übergangspunkten zwischen Simulationsebenen oder Kern-Welten auf“ as personified gatekeeper whose state mirrors the boundary's stability (L56); level transitions with border entities like Argus (L82); read L242 or L266 for his chapter.
- **`did`** (central, 3–12 quotations): the census's surfaces — `Dissoziative Identitätsstruktur` L39; `DID` L39, L44, L91, L132, L134, L308, … (23 lines). central (2–5): the places should externalise Kael's „Dissoziative Identitätsstruktur, DID“ and the decay (L39); the link between dominant alter and perception of the place must be written into the scenes (L44); read L132 or L134.
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L39, L81, L118, L133, L156, L180, … (30 lines). minor (1–2): the Risse and entropy shown through the places — glitches, physical anomalies, escalating (L81); AEGIS trying to contain entropy by brutal means (L484).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L21, L481. minor (1–2): the earlier draft introduces the interventions of the „Guardians“ (AEGIS) (L21) — the Guardians as AEGIS's agents, cut before the bracket; Einheit 734 „und andere Guardians“ in the systemwide wave (L481).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L27, L50, L60, L90, L92, L104, … (31 lines). central (2–5): Juna from the external reality, her role nuanced and unused in the draft (L27); her interaction points and communication paths from the external reality to be defined, possibly bypassing AEGIS protocols (L60); in Kap 1 possibly a failed attempt of Juna's to communicate, as static (L118); read L90 for her interventions in the therapy subplot.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L23, L27, L31, L39, L44, … (216 lines). central (2–5): Kael waking after the universal reboot, estranged, the first Risse in his perception, a mirror confrontation triggering a dissociative episode (L104); his journey of awareness after the reboot in the earlier draft (L21); the stakes — integration of his parts, sanity, survival, truth (L92); pursued by AEGIS as disturbance (L481).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L56, L82. minor (1–2): Argus at transitions between simulation levels or Kern-Welten (L56); the transitions between the Kern-Welten as significant events (L82).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title's name of the Protokoll (L11).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L22, L142, L152, L153, L154, L156, … (31 lines). central (2–5): Lex/Archivar as one of four integrated side characters (L22); Kael meets Lex in Kap 2 — „pflichtbewusst, leicht distanziert“ (L152); Lex's warning that deviations are logged (L154) — cut before the inner straight quote, or quote inside it only.
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L58. minor (1–2): Sibyl placed at an atmospheric place, „z.B. im 'Nexus of Whispers'“ (L58) — a place name of the example; decide reading or occurrence by the page's sense, and say which.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L35. minor (1–2): „die detailliert ausgearbeiteten Lokalitäten der sechs Realitätsebenen“ used as passive scenery in the draft (L35).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L21, L39, L43, L58, L81, L91, … (47 lines); `Glitches` L70, L81, L117, L138, L142, L154, … (18 lines). central (2–5): the Risse introduced in the earlier draft (L21); their manifestation through the places as glitches, gravity shifts, non-Euclidean geometry, escalating (L81); the first obvious Risse on Kael's way through the city in Kap 2 — visual glitches, audio loops (L142, L153); the massive wave of Risse over the simulation (L481).
- **`silas`** (central, 3–12 quotations): the census's surfaces — `Silas` L22, L89, L317, L330, L340, L341, … (21 lines). central (2–5): Silas/Skeptiker among the four side characters (L22); the Glitching Market in Sektor Beta where Kael meets him (L317); the market's chaos mirrors the doubt Silas embodies (L330); „zynisch, scharfsinnig, undurchschaubar“ (L341).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L23. occurrence: `Simulation` is the setting's general word (L23), nothing of the Überwelt.

- **`komponente-734`** (minor, 1–3): „Diese spezifische AEGIS-Einheit wird als wiederkehrender, konkreter Antagonist eingeführt“ (L57) — Einheit 734 as an AEGIS unit; read L43 and L481.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `mnemosyne`: `Mnemosyne-Archive` (near `mnemosyne`), `Mnemosyne-Archiven` (near `mnemosyne`). occurrence: the place name `Mnemosyne-Archive` among the locations, the world's name only.
- `nexus`: `Nexus of Whispers` (near `nexus`). see the page entry above: the place `Nexus of Whispers` (L58).
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is the clinical symptom, not the Personas.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is the alter (Verlorenes Kind/Echo, L22, L50), not the Residual-Echos.


**Record entries** (one file each):

- **`q7-what-734-names`**: Einheit 734 as a specific AEGIS unit, a recurring concrete antagonist (L57), pursuing Kael in the systemwide wave (L481).
- **`c4-guardians-and-aegis`**: the earlier draft's interventions of the „Guardians“ (AEGIS) (L21) and Einheit 734 „und andere Guardians“ (L481) — the Guardians as AEGIS's units.
- **`c7-juna-first-appearance`**: Juna possibly as a failed communication attempt in Kap 1, as static (L118) — a proposal hedged by `Möglicherweise`.

**Not promoted:** Sibyl, Dr. Thorne, Anya, Limina, Nox, Chronos, Schattenkind (no pages), the 38 places, Environmental Storytelling, the Glitching Market, Sektor Beta.

**Two readers**, disjoint: (1) kael, juna, alters, did, lex, silas, argus, kern-welten, realitaetsebenen, nexus; (2) aegis, risse, entropie, guardians, komponente-734 and the records q7, c4, c7.
