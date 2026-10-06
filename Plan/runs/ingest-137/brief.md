# Brief — readings from document 137 (step 6)

1 document, one reader, one batch: `ingest-137`. Files go to `Plan/runs/ingest-137/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 137 | `kohaerenz-protokoll-plot-blueprint-erstellung` | 2025-04-20 | „the plot blueprint“ (titled `Kohärenz Protokoll: Finaler Plot-Blueprint (V2)`, L11) | a German blueprint of 2025-04-20: a methods introduction (L13–L24), answers to eleven core questions (L26–L134), then chapter steps 1.1–1.13 (Teil 1, after a reboot under AEGIS v1.4) and 2.1–2.9 (Teil 2, AEGIS v1.5), each in seven lettered fields (a) Kapitel-Titel … (g); it breaks off in step 2.10 before 87 references; it calls itself „Finaler“ and „direkte Vorlage für die Ausformulierung des Romans“ (L24) — recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (557 lines for `kohaerenz-protokoll-plot-bluep`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A blueprint plans: write „the plot blueprint plans / answers …“; it names Juna also „Julia“ — write „Julia (Juna)“ as it does, never merge silently; „(Integriert in: …)“ pointers are its own bookkeeping; borrowed theories carry footnote digits — cut quotations before glued digits and before inner straight quotes. Kael is male. Chapter pages Kap 1–13 are done by the session from steps 1.1–1.13.

## Pages — document 137, `kohaerenz-protokoll-plot-blueprint-erstellung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L21, L34, L42, L46, L50, … (80 lines). central (2–4): Teil 1 after a reboot under „AEGIS v1.4“ (L138); Teil 2 „AEGIS implementiert Version 1.5“ (L319); the Kohärenz-Inseln enforced by AEGIS's protocols (L34); the AEGIS version table (L387).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L101, L147, L158, L159, L171, L182, … (40 lines). central (2–4): the alters' defence mechanisms hiding the core wound (L101); step 2.3 „Interne Dialoge: Die Anteile formieren sich“ (L347); find the alter names per step (L159, L182, L201).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L116, L286, L287, L288, L289, L298, … (21 lines). central (2–4): L116; step 1.11 „Der Wächter der Schwelle“ (L283) and 2.4 Cerberus' Protokoll (L359); KW3 Grenzfeste (L289).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L20, L146, L158, L182, L263, L351, … (7 lines). minor (1–2): „Dissoziativen Identitätsstörung (DID)“ researched for its fiction (L20).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L21. occurrence unless L21 says more than `Shannon-Entropie` (borrowed).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L101, L452. minor (1–2): Sophia's synthesis and the Externe Ebene (L452); L101.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L196, L197, L202, L286, L289, L301, … (7 lines). minor (1–2): KW3 (Grenzfeste) (L289); step 1.12 „Im Labyrinth der Angst“ (L295).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L22, L58, L71, L105, L109, L129, … (39 lines). central (2–4): each Guardian's possible insight (L113–L117); introduced as agents of AEGIS (L170); Sophia „dem fünften Guardian“ operating above the others (L452).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L34, L42, L50, L86, L91, L101, … (67 lines); `Julia` L38, L42, L215. central (2–4): „Julia (Juna) ist keine aktive Agentin“ inside the simulation (L42); her influence the passive consequence of her ontological connection to Kael (L42); step 1.5 „Die Juna-Spur“ (L211); AEGIS 1.5 tries to eliminate the Juna-Anomalie (L319).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L20, L22, L30, L34, L42, … (134 lines). central (2–4): „Kael (Host): Amnesistisch, verwirrt, funktional im Alltag“ (L147); his loneliness after integration as the core wound, the separation from Juna (L101); from passive sufferer to active investigator (L171).
- **`kairos`** (central, 3–12 quotations): the census's surfaces — `Kairos` L117, L391, L406, L418, L421, L425, … (13 lines). central (2–4): L117; step 2.7 „Kairos' Angebot: Die verführerische Zukunft“ (L425); KW4 Möglichkeits-Garten (L416, L419).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L19, L58, L72, L160, L207, L217, … (13 lines). central (2–4): what L19, L58, L72, L160 say; KW1–KW4 with their Guardians in the steps (L148, L201, L289, L416).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9); the Kohärenz-Inseln are their own term.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L145, L148, L195, L203, L403. minor (1–2): „KW1 - Konstrukt-Stadt (LogOS)“ (L148) — cut before the digit if --find refuses.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L114, L147, L148, L159, L169, L170, … (30 lines). minor (1–2): „Könnte durch ein unlösbares Paradoxon“ (L114); KW1 - Konstrukt-Stadt (LogOS) (L148); step 2.5 LogOS' Dilemma (L371).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L115, L240, L252, L264, L274, L275, … (21 lines). central (2–4): L115; step 2.2 „Mnemosynes Einflüsterungen“ (L335); what L240, L252 say.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L199, L200, L204, L416, L419. minor (1–2): step 2.6 „Der Garten der Möglichkeiten“ (L413); KW4 (L416).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L101. minor (1–2): „funktionale Multiplizität“ after significant integration (L101).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L201, L240, L250, L252, L276, L340, … (7 lines). minor (1–2): find Oblivion's lines (L201, L240, L250) — briefly.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L34, L440. minor (1–2): the K-J-Essenz „potenziell im Potentialmeer angesiedelt, jenseits der linearen Logik von AEGIS“ (L34); L440.
- **`protokoll-v14`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Protokoll v1.4` alone on L147. minor (1–2): „Protokoll v1.4“ (L147) and the reboot under AEGIS v1.4 (L138) — what it says.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L146. occurrence unless L146 says what the levels are — then minor.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L198, L201, L238, L241, L253. minor (1–2): step 1.7 „Flucht in die Resonanz“ (L235); KW2 (L238, L241).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L42, L138, L145, L146, L148, L150, … (22 lines). central (2–4): the Risse as symptoms of the fundamental instability (L138); step 1.4 „Der erste Riss im Selbst“ (L178); L145–L150.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L204, L216, L350, L352, L430. minor (1–2): find Silas's lines (L204, L216) — briefly.
- **`sophia`** (central, 3–12 quotations): the census's surfaces — `Sophia` L113, L392, L407, L449, L451, L452, … (11 lines). central (2–4): L113; step 2.9 „Sophias Synthese und der blinde Fleck“ (L449); „Sophia, dem fünften Guardian, der für Weisheit und Synthese zuständig ist“ (L452).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L20, L149, L161, L194, L207. minor (1–2): „Struktureller Dissoziation (TSDP)“ (L20); Kael as ANP (L147).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L205, L377, L407, L437, L439, L440, … (11 lines). central (2–4): step 2.8 „Die Überwelt: AEGIS' Netzwerk“ (L437); what L439–L440 say.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the role word.
- `entropie`: `Shannon-Entropie` (near `entropie`). `Shannon-Entropie` borrowed — occurrence.
- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`). occurrence: `Kohärenz-Inseln` its own term, read on aegis if at all (L34).
- `personas`: `Apparently Normal Personality` (near `persona`). occurrence: ANP's expansion, on tsdp.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` in step 1.2's title (L154), not the page.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: five Guardians, each with an insight (L113–L117), Sophia „dem fünften Guardian“ above the others (L452); Kairos alone in KW4 (L416–L425) — dated 2025-04-20.
- **`q5-guardians-and-kern-welten`**: LogOS with KW1 (L148), Cerberus with KW3 (L289), Kairos with KW4 (L416–L425), Sophia possibly in the Überwelt (L452).
- **`c13-externe-ebene-beyond-the-simulation`**: Julia (Juna) not an agent inside the simulation, her influence from her ontological connection (L42); the K-J-Essenz in the Potentialmeer beyond AEGIS's logic (L34).

**Not promoted:** Kohärenz-Inseln, K-J-Essenz, Bond-Verlust, the „Welle“, the AEGIS version table, the eleven core questions, Environmental Storytelling, IFS.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, juna, guardians, logos, mnemosyne, cerberus, kairos, sophia, ueberwelt, externe-ebene, potentialmeer, protokoll-v14, risse, and the entries c6, q5, c13.
- Reader 2: kael, alters, oblivion, silas, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, did, tsdp, multiplizitaet, realitaetsebenen (if read), entropie (if read).
