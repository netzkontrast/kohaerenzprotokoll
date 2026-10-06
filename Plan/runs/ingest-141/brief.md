# Brief — readings from document 141 (step 6)

1 document, one reader, one batch: `ingest-141`. Files go to `Plan/runs/ingest-141/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 141 | `briefing-core-concepts-of-the-kohaerenz-protokoll-project` | 2025-10-15 | „the briefing“ (titled `Briefing: Core Concepts of the "Kohärenz Protokoll" Project`, L11) | an English briefing of 2025-10-15 summarising the project: the central dialectic of two coherences with a comparison table (L23–L48), the core entities — AEGIS with its protocols, Kael with an alter table, Juna/V and the Moonshine-Link, Das Fundament, the Void (L52–L109), scientific and philosophical concepts with a Core-World table (L113–L138), and the narrative architecture with a Dramatica table (L142–L170); third person, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (174 lines for `briefing-core-concepts-of-the-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A briefing summarises: write „the briefing describes / maps …“; English — quote as written, never translate; German terms in quotation marks are the briefing's — cut quotations before inner straight quotes. Kael is male; Juna/V „she“.

## Pages — document 141, `briefing-core-concepts-of-the-kohaerenz-protokoll-project`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L27, L29, L31, L33, … (25 lines). central (2–4): „AEGIS (Autonomous Entropic Gatekeeper for Integrity Systems) is the central antagonist“ (L56); its motto quoted in German (L31) — cite the line; a three-tiered cognitive architecture, LFI, D2, reinforcement learning (L60–L64); its protocols table (L69–L75).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Cognitive Firewall` L74. minor (1–2): the protocols ZTEM, RTSV, BPoF, EIC, Cognitive Firewall, RIVE (L70–L75) — the briefing's list.
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L37, L63, L124, L135, L162. minor (1–2): the alter table (L83–L91); D2 treating his alters as separate speakers (L63).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L90. minor (1–2): „ANP: Meta-Observer“ (L90).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L135. minor (1–2): KW3 Cerberus-Labyrinth (L135).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L17, L117. minor (1–2): the narrative climax structured around Gödel's first incompleteness theorem (L117).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L93. minor (1–2): „a mysterious external entity or anomaly“ (L95); her origin deliberately ambiguous (L97).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L35, L37, L39, L43, … (23 lines). central (2–4): „Kael's psyche is a complex adaptive system modeled on“ Tertiary Structural Dissociation (L79); „Kael (Host)“ ANP (L84); his integrated state a dialetheic mind (L39).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L136. minor (1–2): KW4 Kairos-Potentialis, „Generative Synthesis / Kairos/Sophia“ (L136).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L87. minor (1–2): EP: Child/Fear (L87).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L156. minor (1–2): the four-act East Asian structure also used (L156).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9); the paradox on aegis.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L85. minor (1–2): „Rationalist, embodies cold, emotion-avoiding logic“ (L85).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L133. minor (1–2): KW1 Logos-Prime, Classical Consistency / LogOS (L133).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L134. minor (1–2): KW2 Mnemosyne-Archipel (L134).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L93, L98. minor (1–2): „a non-local“ sub-protocol connection, an architectural backdoor (L98) — cut before the quotes; invisible to AEGIS's sensors (L101).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L91. minor (1–2): „EP: The Frozen“ (L91).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L29, L107. minor (1–2): „This is the primordial state of pure, high-entropy potentiality from which AEGIS emerged“ (L109).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L86. minor (1–2): EP: Fighter/Protector, an internal persecutor (L86).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L29, L97. minor (1–2): the high-entropy void, „Potentialmeer“ or Nichts Rauschen (L29); Juna as a possible manifestation of it (L97).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L88. minor (1–2): „ANP: Caregiver“ (L88) — an ANP.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L138. minor (1–2): the Risse as manifestations of systemic instability, the Landauer paradox (L138) — cut before the quotes.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L89. minor (1–2): „ISH (Internal Self Helper): Guardian and mediator“ (L89).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L136. minor (1–2): the same line (L136).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L83, L123. minor (1–2): „This clinical theory provides the rigorous architectural blueprint for Kael's psyche“ (L123).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L126. occurrence: `Simulation` in a heading (L126), nothing said of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `ontological exploit` (near `alex`). occurrence: `ontological exploit` is not Alex.
- `juna`: `Juna/V` (near `juna`). `Juna/V` (J34) — on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`), `Kairos/Sophia` (near `kairos`). on kairos above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence (J9).
- `personas`: `Theory of Structural Dissociation of Personality` (near `persona`). occurrence: TSDP's full name, on tsdp.
- `sophia`: `Kairos/Sophia` (near `sophia`). on sophia above.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: „Autonomous Entropic Gatekeeper for Integrity Systems“ (L56) — position 1 again.
- **`q3-how-many-kern-welten-and-alters`**: four Core Worlds (L128–L136); eight alters in the table (L84–L91), Rhys and Argus ANPs, Selene an ISH.
- **`c6-guardians-count-and-pairing`**: LogOS KW1, Mnemosyne KW2, Cerberus KW3, Kairos/Sophia KW4 (L133–L136) — dated 2025-10-15.
- **`q9-moonshine-link-boundary`**: non-local, acausal, invisible to AEGIS's sensors (L98, L101).
- **`c11-landauer-warmth-or-cold-ozone`**: the Risse in „a key paradox based on Landauer's principle“ (L138) — only what the line says.

**Not promoted:** ARCHON, NCP, LFI, D2, IIT/Φ, the protocol acronyms (on aegis-teilfunktionen), Das Fundament, perpetrator introject, polyphonic prose.

**One reader**, all pages and entries.
