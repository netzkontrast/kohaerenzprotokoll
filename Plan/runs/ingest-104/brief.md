# Brief — readings from document 104 (step 6)

1 document, one reader, one batch: `ingest-104`. Files go to `Plan/runs/ingest-104/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 104 | `romanprojekt-analyse-synthese` | 2026-04-30 | „the reset synthesis“ (titled `Systemarchitektur und ontologische Synthese des Romanprojekts Kohärenz Protokoll: Der definitive Projekt-Codex nach dem Struktur-Kanon Reset 2026-04-30`) | a German synthesis of 2026-04-30 that applies a „Struktur-Kanon“ of that day: the Dual-Kernel-Theorie with the Landauer principle (L15–L40), three phases of the 39 chapters (L42–L62), a list of ten alters (L64–L86), Juna (L88–L90), a „Kohärenz-Prime“ storyform (L92–L107), consensus, contradictions and gaps (L109–L130), and a build plan it calls binding (L132–L157) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (170 lines for `romanprojekt-analyse-synthese`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that claims canon: write „the reset synthesis sets …“, „resolves …“; its claims to be „definitive“, to apply „den Reset-Kanon“ and to give „einen verbindlichen Bauplan“ (L134) are its own, recorded, never applied — the author's canon is `Manuscript/kanon.md`. Many sentences report other documents (`frühere Entwürfe`, `einige Analysen`, the Struktur-Kanon): say whose claim it is. **The export lost the kernel symbols** (`Kohärenz-Kernel ()`, empty table cells): never supply them. Kael is male here.

## Pages — document 104, `romanprojekt-analyse-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L29, L31, L36, L50, L54, … (14 lines). central (2–3): Wächter of the Konstrukt-Stadt (L21); its suppression of traumatic memory as erasure generating heat (L29); the IC throughline, „Realitäts-Diktator“ (L102); not destroyed but transformed toward algorithmic melancholy (L118), kept as an „algorithmisch melancholischer“ Wächter with Juna accepted as the integrative centre (L62).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L76, L145. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L66, L122, L145, L163. central (2): the „Reset-Kanon vom 30. April 2026“ fixes ten functional parts against earlier thirteen (L66, L122); the table of ten with TSDP action system, DKT assignment and narrative function (L70–L84).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L84. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L153. minor (1): one of the five (L153).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L56. minor (1): Kael finds the Chaitin constant in the city's source code in Kapitel 19 (L56).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L29. minor (1): DID as a necessary system architecture, not a pathology (L117).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L13, L15, L70, L74, L161. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L13. central (2): the Dual-Kernel-Theorie as the reality substrate, permanent interference of two computational substrates (L17).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L13. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L151, L153. minor (1–2): LogOS, Mnemosyne, Cerberus, Kairos, Sophia as filter algorithms, each a defensive wall in Kael's psyche, failing by logical overload (L153).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L81. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L23, L37, L50, L60, L62, L77, … (14 lines). central (2–3): the Kollaps-Kernel's figure (L23); the first encounter in Kapitel 3 classed a „Syntaxfehler“ (L50); in the current canon „Teil von Kaels Ursprungs-Ich“ and „transzendenter Katalysator“ (L90); the „Wir-Geflecht“ and paraconsistent logic (L90).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L29, L31, L40, L48, L50, … (25 lines). central (2–3): wakes after a „Universal Reboot“ (L48); the host and primary ANP (L66, L86); the MC in Fixed Attitude with a Change resolve (L101); „Kael ist der männliche Host“ — the gender speculation declared ended (L123); a living Gödel-Satz (L107).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L153. minor (1): named apart from Sophia among the five (L153).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L79, L86. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L17, L21. minor (1–2): the domain of reversible, information-preserving computation, represented by the Konstrukt-Stadt and AEGIS (L21).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L17, L23. minor (1–2): irreversible processes, entropy and decay, represented by Juna and the Risse, a condition for evolution (L23).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L21, L29, L38, L48, L149, L157. central (2–3): the architecture as antagonist, mathematically correct but physically impossible (L48); thermal Risse in its architecture (L29); at the climax not a prison but a „Receiver of Consciousness“ (L157).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L75, L145. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L80. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L50, L140, L153. minor (1): AEGIS (LogOS) cannot „see“ Juna in Kapitel 3 (L50); LogOS-Domäne scenes in analytic language (L140).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L153. minor (1): one of the five Guardians as filter algorithms (L153).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine Link` L103. minor (1): the „Moonshine Link“ between Kael and Juna as the Relationship Story in Psychology (L103).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L82. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L107. minor (1–2): from fragmented to functional multiplicity, parts cooperating not fusing (L90); the We-Voice in Phase III (L145).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L60. minor (1): the system reaching „psychischer Negentropie“ in Kapitel 31 (L60).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L78, L86. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L77. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L23, L29, L39, L149. minor (1–2): the heat of erasure as thermal Risse or Glitches (L29); the thermal glitch as foreshadowing (L149).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L83. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L86. minor (1–2): „Silas (The Archivist)“, in some analyses called a Juna-Echo, administrator of the internal index hiding traumatic files from AEGIS (L86).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L153. minor (1): named apart from Kairos among the five (L153).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L64, L66, L70, L74, L117, L161. minor (1–2): Kael as host of a system with tertiary structural dissociation, alters as partitioned memory (L66); TSDP as model, consensus (L117).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L13. minor (1): its row in the ten-alter table (L75–L84) — TSDP action system, DKT assignment, narrative function.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Fixierung` (near `entropie`). reading on entropie: Juna and the Risse as the Kollaps-Kernel of entropy (L23); `Entropie-Fixierung` is Moros's DKT cell (L82).
- `entropie-resonanz`: `Resonanz-Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz-Protokoll` (near `entropieresonanzprotokolle`). occurrence: the `Resonanz-Protokoll` of the finale (L62, L155) is the plan's own protocol, not the page (J16).
- `kohaerenz`: `Zielkohärenz-Protokoll` (near `koharenz`), `Zielkohärenz` (near `koharenz`), `Kohärenz-Prime` (near `koharenz`). occurrence: the title and its compounds `Zielkohärenz`, `Kohärenz-Prime` (J9, J16).


**Pages placed by the sentence:**

- **`landauer-signatur`** (minor, 1–2): the Landauer principle as the plot's motor — erasure of a bit generates heat (L27), AEGIS's suppression of memory generating heat as thermal Risse (L29); the „Wärme“ of the Landauer principle in the Juna scenes (L141).
- **`algorithmische-melancholie`** (minor, 1): AEGIS's transformation „in Richtung algorithmischer Melancholie“ (L118) and the „algorithmisch melancholischer“ Wächter (L62).
- **`goedel-gambit`** (minor, 1): Kael as a living Gödel-Satz, an „ontologischen Exploit“ (L107).

**Not promoted:** Struktur-Kanon / Reset-Kanon 2026-04-30, Kohärenz-Prime, the Bekenstein bound and pixelation (L31), the Spiegel-Effekt, the We-Voice, the Driver-Pivot gap, F2, F3, F7, Receiver of Consciousness, Phänomenales Selbstmodell.

**Record entries** (one file each):

- **`c17-kael-gender`**: „Kael ist der männliche Host“ and speculation about gender declared ended (L123) — the synthesis names the difference, as document 96 does; record its claim, not as a resolution.
- **`c7-juna-first-appearance`**: „Die erste Begegnung mit Juna in Kapitel 3“ (L50).
- **`c11-landauer-warmth-or-cold-ozone`**: heat from erasure as thermal Risse (L29), the „Wärme“ of the Landauer principle (L141), the simulation „überhitzt“ at each truth (L149).
- **`c13-externe-ebene-beyond-the-simulation`**: the Spiegel-Effekt in Kapitel 36 exports the simulation's data symbolically into the reader's physical reality, „(Köln 2026)“ (L62).
- **`c16-kael-origin`**: Juna as part of Kael's „Ursprungs-Ich“ (L90).
- **`q3-how-many-kern-welten-and-alters`**: ten parts by the „Reset-Kanon vom 30. April 2026“ against earlier thirteen (L66, L122), the table L75–L84 — without Kael, Silas named apart (L86). Append dated 2026-04-30; it predates the author's answers of 2026-10-05 (thirteen) and changes neither.
- **`q8-aegis-after-the-vortex`**: no destruction but a transformation toward algorithmic melancholy (L118); kept as a melancholic Wächter, Juna the integrative centre (L62); the rigid structure's final disintegration (L107). Predates the author's answers.
- **`q5-guardians-and-kern-welten`**: five Guardians named, Kairos and Sophia apart (L153); no world assignment.
- **`c15-flight-riss-bearers`**: Kiko's row, `Flucht (Angst)` (L79) — the only row with flight.

**Chapter readings** in `Plan/runs/ingest-104-kap/brief.md`.

**Split into three readers, one after the other:**
- Reader 1: dkt, kohaerenz-kernel, kollaps-kernel, konstrukt-stadt, aegis, logos, kael, juna, risse, entropie, landauer-signatur, algorithmische-melancholie, goedel-gambit, did, chaitin-konstante, negentropie, moonshine-link.
- Reader 2: tsdp, alters, lex, alex, rhys, nyx, kiko, lia, isabelle, moros, selene, argus, silas, multiplizitaet, guardians, mnemosyne, cerberus, kairos, sophia, and the record entries.
- Reader 3: the chapter readings.
