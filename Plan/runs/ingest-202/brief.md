# Brief — readings from document 202 (step 6)

1 document, one reader, one batch: `ingest-202`. Files go to `Plan/runs/ingest-202/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 202 | `romanplot-kohaerenz-protokoll-entwickeln` | 2025-04-23 | „the detailed plot blueprint“ (an unsigned plot outline) | a German plot blueprint that follows Kael's arc through the Heldenreise and three acts, AEGIS's escalating interventions, the four Kernwelten KW1–KW4 with their Wächter, a table of two kinds of coherence and „Was wäre wenn“ questions, with a 70-entry web reference list (L193–L264) — written in the modal mood throughout; it calls itself a reliable foundation (L189, L191); its proposals recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (265 lines for `romanplot-kohaerenz-protokoll-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal in the modal mood: write „the detailed plot blueprint proposes / describes …“ and keep its `möglicherweise`, `könnte`, `vielleicht`; its questions (L169–L182) are asked, not answered — record them as questions. German — quote as written; the export glued footnote numbers to words and punctuation (`Umgebung.22`, `Mentor 3`) — cut every quotation before a glued digit; cut before inner straight quotes and the `\[Query\]` markers; the table L126–L131 has escaped bold.

## Pages — document 202, `romanplot-kohaerenz-protokoll-entwickeln`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L29, L30, L31, L32, L33, … (54 lines). central (3–8): AEGIS as „einer gewaltigen, nicht-menschlichen Entität“ on pure logic and information processing (L17); its role as antagonist not from malice (L64); it can understand connection only as dissolution of order (L66); the Kerndirektive „Kohärenz durch Exklusion“ (L68) against „Kohärenz durch Abgrenzung“ (L31) — record both; the three phases of escalating intervention, diagnosis, correction, escalation (L70–L72); the ending need not destroy AEGIS (L59).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L29, L31, L118, L159. minor (1–3): the dominant controlling parts — „Alters oder IFS-Manager“ — resisting the confrontation (L31); the integration of a split-off part, „Alter/Part“, as the reward (L57).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L45, L71, L74, L98. minor (1–3): the Wächter Cerberus possibly deployed to restrict Kael's movement or access to KW4 (L71); in KW3 Cerberus „könnte hier als bedrohlicher Hüter“ or the embodiment of Kael's fears appear (L98).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L21, L46, L105, L107, L108, L128, … (7 lines). minor (1–3): KW4 as a place of change and emergence (L46, L105); integration as „eine relationale, emergente Logik“ (L145).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L66, L129, L247. minor (1–3): read L66 and L129 — the reduction of complexity/entropy as AEGIS's goal in the table; decide reading or occurrence and say which.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L30, L32, L68, L118, L145, … (10 lines). central (3–8): the „rätselhafte Kael-Juna (K-J) Verbindung“ (L17); the connection as an inner mentor (L32); AEGIS reacting to „die Anomalie Kael/Juna“ (L68); „Was oder wer ist Juna genau?“ (L169) and the three options — separate entity, aspect of the Kohärenz-Insel, or Kael's own integrated potential (L180) — asked, not answered.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L25, L29, L30, L31, … (56 lines). central (3–8): Kael as „einem Menschen mit Dissoziativer Identitätsstörung (DIS)“ (L17); his arc from fragmentation to integration through the Heldenreise (L25, L29–L33); he sees the Risse are not his fault (L52); integration as an ongoing process at the end (L60); his practical identity of cooperating parts (L138).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L46, L105. minor (1–3): the presence of Kairos „könnte sich als Gefühl für den“ right moment show in KW4 (L105) — cut where the line breaks off.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L29, L30, L31, L33, L39, L48, … (18 lines); `Kernwelt` L29, L30, L31, L33, L39, L48, … (18 lines). central (3–8): four Kernwelten that are „nicht nur Schauplätze“ (L80): KW1 Konstrukt-Stadt — Logik, Ordnung, Kontrolle (L43); KW2 Resonanz-Nebel (L44); KW3 Schattenlabyrinth (L45); KW4 Möglichkeitsstrom (L46); the environment as an actor in Kael's healing (L48).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–3): the comparison table of two kinds of coherence — AEGIS's „Exkludierende Kohärenz“ against the Kohärenz-Insel's „Integrative Kohärenz“ (L126), by mechanism and goal (L128, L129); L11 is the title, an occurrence.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L33, L43, L48, L82. minor (1–3): KW1, the Konstrukt-Stadt — a highly structured, geometric, perhaps sterile world mirroring AEGIS's principle of order, where AEGIS and LogOS intervene most (L43); its growing rigidity under AEGIS's pressure (L48).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L30, L43, L70, L84, L179. minor (1–3): LogOS as a „Wächter-Subsystem“ for logical consistency (L30); AEGIS and „sein Wächter LogOS“ in KW1 (L43); whether LogOS might simulate integration and fail on Gödel (L179) — a question.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L30, L44, L70, L74, L91, L179. minor (1–3): Mnemosyne as a Wächter for memory (L30, L70); a Wächter like Mnemosyne possibly developing rudimentary empathy (L179) — a question.
- **`personas`** (minor, 1–4): the census's surfaces — `Persona` L29, L43, L86, L87. minor (1–3): read L29 and L86 — decide reading or occurrence; a `Persona` as Kael's mask is an occurrence unless the line speaks of the page's Personas.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L17, L119, L127, L138, L145, L169, … (9 lines). minor (1–3): the Potentialmeer as origin of both kinds of coherence in the table (L127); asked whether there is a prehistory of the Potentialmeer (L169); whether the connection lets Kael perceive it (L180).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L119. minor (1–3): read L119; decide reading or occurrence and say which.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L52, L53, L57, L60, L72, L159, … (7 lines). minor (1–3): the Risse as „paradoxe Konsequenzen von AEGIS' eigenen Kontrollversuchen“ (L52); in phase 3 AEGIS creates more chaos, the Risse arise and widen (L72).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L139. occurrence: `Simulation` is the philosophical question of simulation and reality (L139), nothing of the Überwelt.

- **`guardians`** (minor, 1–3): the Wächter as AEGIS's „spezialisierte Wächter-Subsysteme“ (L30) — LogOS, Mnemosyne, Cerberus — commissioned to collect data (L70); the Wächter as outer opponents in act 2 (L159); the evolution of the Wächter (L179) — a question.
- **`moonshine-link`** (minor, 1–2): read L119 — the Monstergruppe as metaphor for the Kohärenz-Insel, with the Happy Family and Monstrous Moonshine; quote before glued digits.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Insel` (near `koharenz`), `Exkludierende Kohärenz` (near `koharenz`), `Integrative Kohärenz` (near `koharenz`). `Exkludierende Kohärenz` and `Integrative Kohärenz` are read on kohaerenz (the table, L126); `Kohärenz-Insel` has no page — an occurrence (Kohärenz-Insel stays unpromoted).


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: four Kernwelten KW1–KW4 (L43–L46); AEGIS and „sein Wächter LogOS“ in KW1 (L43), Cerberus in KW3 (L98), Kairos in KW4 (L105), Mnemosyne as Wächter for memory (L70).
- **`c4-guardians-and-aegis`**: the Wächter as AEGIS's subsystems (L30, L70).
- **`c16-kael-origin`**: „Die Kohärenz-Insel, der Ursprung von Kaels Essenz und der K-J-Verbindung“ (L119).
- **`q9-moonshine-link-boundary`**: the Monstergruppe as a metaphor for the Kohärenz-Insel (L119) — a metaphor, not a link.

**Not promoted:** the Kohärenz-Insel (16+ documents, left for the author), the K-J-Verbindung (on juna and kael), Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom (on kern-welten), the IFS vocabulary, Bachelard, Vogler, the borrowed theories, the `\[Query\]` markers.

**Two readers**, disjoint: (1) kael, juna, alters, kern-welten, konstrukt-stadt, emergenz, kairos, personas, realitaetsebenen, potentialmeer, moonshine-link and the records c16, q9; (2) aegis, risse, entropie, kohaerenz, logos, mnemosyne, cerberus, guardians and the records q5, c4.
