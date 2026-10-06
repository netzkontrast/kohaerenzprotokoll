# Brief — readings from document 145 (step 6)

1 document, one reader, one batch: `ingest-145`. Files go to `Plan/runs/ingest-145/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 145 | `charakterkonzepte-fuer-kohaerenz-protokoll` | 2025-04-18 | „the character concepts“ (titled `Charakterkonzepte für Kohärenz Protokoll`) | a German character-concept paper addressed to the author: Kael as host and whole system (Teil I), Juna, AEGIS and the five Guardians each with a „Blinder Fleck“, ten alters with a table of worlds (Teil II, L211–L511), eleven proposed minor figures (Teil III), a research synthesis on depicting DID (Teil IV); it calls itself a practical tool, hedges Juna as „Rein spekulativ“ (L92), and breaks off mid-word at L700 — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (769 lines for `charakterkonzepte-fuer-kohaere`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept paper proposes: write „the character concepts propose / describe …“; its question marks in the tables (L501–L511) and its „möglicherweise“ are part of what it says — keep them. Lines tagged „Kontext Pt N“ report a context the file does not hold: say „citing a supplied context“. „Kernaussagen der Recherche“ (L658) reports web sources — attribute as the document's report of research. German — quote as written; cut quotations before inner straight quotes and before reference digits glued to a word.

## Pages — document 145, `charakterkonzepte-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L27, L30, L46, L50, L58, … (76 lines). central (2–4): „Autonomous Entropic Gatekeeper for Integrity Systems“ (L118), the law of the Überwelt and the worlds, antagonism „jedoch nicht aus Bosheit“ (L118); binary logic, Seele=Info (L127); its blind spot by Ashby's Law (L128); not anthropomorphic (L143); the reboot as its act (L146).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L29, L30, L49, L60, L65, L77, … (62 lines). central (2–4): the review of „10 Kern-Anteilen“ (L218) by DID research — Limina, Nox, Eos, Index (L222–L224); the overview table with a primary Kern-Welt per alter, many with a question mark (L499–L511); depiction: switches the exception (L231).
- **`blinder-fleck`** (central, 3–12 quotations): the census's surfaces — `Blinder Fleck` L50, L97, L128, L160, L170, L180, … (18 lines). central (2–4): the profile field „Blinder Fleck“ for Kael (L50), Juna (L97), AEGIS (L128) and each Guardian (L160, L170, L180, L190, L200); the Guardians' acts rest on their blind spots (L209). Name C4 if the reading shows both bearers in one document.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L148, L175, L207, L578, L580. minor (1–2): Guardian „Cerberus (Zugeordnet: Grenzfeste)“ (L175), security and border control (L179), paranoia as blind spot (L180).
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L18, L19, L26, L27, L29, L30, … (36 lines). central (2–4): the paper's framing: Kael as the whole system (L29), fragmentation from early repeated trauma (L49, L217); the research synthesis (L658) — attributed as reported research.
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L67, L86, L106, L116, L118, L123, … (24 lines). minor (1–2): AEGIS's binary order vs. chaos in entropy terms (L127); Juna as source of „unkontrollierbarer Entropie“ (L86).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L94, L112. minor (1–2): Juna's „primäre Verankerung die Externe Ebene“ (L112); the „postulierten Externen Ebene“ (L58); a realm beyond AEGIS's control (L86).
- **`grenzfeste`** (central, 3–12 quotations): the census's surfaces — `Grenzfeste` L30, L66, L111, L175, L283, L309, … (18 lines). central (2–4): KW3 (L66); Cerberus's world (L175); the primary world of Nox, Praetor and, with a question mark, Limina (L501–L509); Limina's two worlds (L283).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L59, L77, L111, L126, L136, L138, … (21 lines). central (2–4): „Die fünf Guardians sind spezialisierte, funktionale Agenten von AEGIS“ (L150); one per world, Sophia on the Überwelt (L207); limited awareness of each other (L205); antagonists of Teil 1 (L209).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L40, L45, L46, L47, L58, L67, … (49 lines). central (2–4): Kael's „zentraler emotionaler und möglicherweise ontologischer Ankerpunkt“ (L86); AEGIS's view of her as an anomaly (L86); „Rein spekulativ“ (L92) and „Ihre genauen Ziele sind unbekannt“ (L91); arc tied to Kael's (L114); Junas Fragment, Echo / Lichtfunke as a proposed name.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L25, L26, L27, L28, … (125 lines). central (2–4): the primary point of view after the „universal reboot“ (L26); host and whole system (L29); his amnesia as function (L27); the hero's journey (L68–L79); his arc a change of worldview (L688).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L148, L185, L207, L588, L590. minor (1–2): Guardian „Kairos (Zugeordnet: Möglichkeiten-Garten)“ (L185); growth and simulated futures within AEGIS's limits (L189).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L30, L48, L65, L66, L111, L112, … (18 lines). central (2–4): „ökologischen Manifestationen spezifischer Cluster von Alters“ (L30); the four named (L30, L66); „buchstäbliche Landschaften des Geistes“ (L671).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: L11 is the title.
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L26, L30, L39, L48, L66, L72, … (28 lines). central (2–4): KW1, Kael's start after the reboot (L66, L72); LogOS's world (L155, L159); the Therapeut-Konstrukt as its figure (L525–L528).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L148, L155, L207, L530. minor (1–2): Guardian „LogOS (Zugeordnet: Konstrukt-Stadt)“ (L155), logic and rule conformity (L159), blind to trauma's illogic (L160).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L148, L165, L207, L560, L568, L570. minor (1–2): Guardian „Mnemosyne (Zugeordnet: Resonanz-Landschaft)“ (L165), memories as data points (L170).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L658. minor (1–2): „funktionale Multiplizität ist ebenfalls ein valider Therapieerfolg“ (L658) — the document's report of research.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L225, L393, L394, L411, L418, L508, … (7 lines). central (2–4): here an alter, not a Guardian: „Oblivion (Der Gefrorene)“ (L393), Trauma-Halter, Freeze Response (L395); table KW2 (isoliert)/KW3 (L508).
- **`resonanz-landschaft`** (central, 3–12 quotations): the census's surfaces — `Resonanz-Landschaft` L30, L66, L76, L111, L165, L335, … (18 lines). central (2–4): KW2 (L66), Mnemosyne's world (L165, L169); the primary world of Echo and, with a question mark, Silas (L504, L511).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L27, L59, L73, L125, L136, L143, … (29 lines). central (2–4): the Guardians' acts provoke or worsen the „Risse“ (L209) — cut before the quotes; the Risse as visible manifestations of breaking-through parts (L671).
- **`silas`** (central, 3–12 quotations): the census's surfaces — `Silas` L225, L328, L354, L432, L471, L472, … (10 lines). central (2–4): here an alter, not a Guardian: „Silas (Der Pflegende)“ (L471), Caretaker for Echo and Flicker (L473); table Resonanz-Landschaft (KW2)? (L511).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L148, L195, L207. minor (1–2): „Sophia (Zugeordnet: Überwelt / Integration?)“ (L195) — the question mark is the paper's; system-defined wisdom (L199).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L118, L143, L144, L150, L195, L201, … (11 lines). minor (1–2): AEGIS's „primäre Domäne ist die rein informationsbasierte Überwelt“ (L144), citing a supplied context; Sophia's station (L195, L201).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Protokolle` (near `zerotrust`). occurrence: `Zero-Trust-Protokolle` (L205) is the reason the Guardians may know little of each other — say it on guardians, not here.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the novel's title.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: Echo is an alter (child, trauma-holding, L225, L504) and a proposed name for Juna's fragment, not the residual echoes.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: five Guardians LogOS, Mnemosyne, Cerberus, Kairos, Sophia, one per world and Sophia on the Überwelt (L148–L207); Oblivion and Silas are alters here (L393, L471); dated 2025-04-18.
- **`q5-guardians-and-kern-welten`**: the pairing LogOS–Konstrukt-Stadt, Mnemosyne–Resonanz-Landschaft, Cerberus–Grenzfeste, Kairos–Möglichkeiten-Garten, Sophia–Überwelt with a question mark (L155–L207).
- **`q3-how-many-kern-welten-and-alters`**: ten alters with a primary world each, several with a question mark, and clusters of alters per world (L30, L499–L511).
- **`q1-guardians-and-aegis`**: „spezialisierte, funktionale Agenten von AEGIS“ (L150), „funktionale Ausführungsorgane“ (L138).
- **`c4-guardians-and-aegis`**: one document holding both bearers — AEGIS's blind spot (L128) and each Guardian's (L160–L200).

**Not promoted:** the ten alters without a page (Limina, Nox, Echo, Flicker, Eos, Praetor, Index), the eleven minor figures (Aris Thorne, Herr Jansen, Der Archivar, Chronos, Sibyl, Cassian …), Möglichkeiten-Garten (no page; on kern-welten), the DID vocabulary (ANP, Persecutor, Internal Self-Helper, Switching …), Heldenreise, Ashby, Homöostase, John Locke.

**Two readers**, disjoint: (1) kael, juna, aegis, ueberwelt, externe-ebene, entropie, did, multiplizitaet, alters, oblivion, silas and the record q3; (2) guardians, logos, mnemosyne, cerberus, kairos, sophia, blinder-fleck, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, risse and the records c6, q5, q1, c4.
