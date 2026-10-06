# Brief — readings from document 149 (step 6)

1 document, one reader, one batch: `ingest-149`. Files go to `Plan/runs/ingest-149/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 149 | `kohaerenz-protokoll-plotideen-generierung` | 2025-04-26 | „the plot-idea synthesis“ (titled `Kohärenz Protokoll: Konzeptanalyse und Plot-Ideen-Synthese`, L11) | a German concept analysis of 2025-04-26 (Teil I: the Potentialmeer, AEGIS and its five protocols, the Guardians and Kernwelten, Kael with DID and ten Alters, the Kael-Julia link, the central conflict) and a synthesis of plot seeds and arcs from it (Teil II, L288–L337); it hedges with „möglicherweise“ and marks its guardian table „Hypothetisch“ (L147); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (428 lines for `kohaerenz-protokoll-plotideen-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis and its plot seeds: write „the plot-idea synthesis analyses / proposes …“; keep its hedges and its „Hypothetisch“; Juna is Julia here — write `Julia` as the document does and say it is read on juna; borrowed theory (Aristoteles, Bateson, IFS) is the document's application, attributed. German — quote as written; cut before inner straight quotes and before reference digits glued to a word.

## Pages — document 149, `kohaerenz-protokoll-plotideen-generierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L24, L25, L28, L30, L40, … (103 lines). central (2–4): „AEGIS entsteht durch Selbstorganisation (Autopoiesis) aus dem Potentialmeer“ (L49); five protocols OBP, RIVE, PMAS, SARM, CCPP (L55, L63); the conflict between CAS and control (L65); a first-order observer (L109); misreads the K-J link as maximal threat (L192); the double bind (L253).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L174, L306, L307. minor (1–2): ten Alters named in one parenthesis — Der Architekt, Das Echo, Der Wächter, Der Sucher, Der Funke, Limina, Nox, Praetor, Index, Silas — read through IFS (L174); none described.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L129, L133, L154. minor (1–2): „Überwacht das Schattenlabyrinth“ (L133).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L93, L109, L111, L170, L172, L307, … (8 lines). minor (1–2): Kael's DID „durch AEGIS' Analyseversuche induziert“ (L172).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L23. minor (1–2): the conditions for „Emergenz aus dem Meer“ (L23); AEGIS arising from the Potentialmeer by autopoiesis (L49).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. minor (1–2): the Potentialmeer of „maximale Entropie – hier im Sinne maximaler Möglichkeit“ (L19) — entropy as possibility.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L292. minor (1–2): plot seed „9.1 Genesis von AEGIS“ — AEGIS's emergence from the sea (L292).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L125, L129, L141, L143, L145, L164, … (13 lines). central (2–4): „spezialisierte Subsysteme, die Guardians“, each for one Kernwelt (L129); the five (L131–L135); the hypothetical table of functions and blind spots (L147); their potential for doubt (L143, L145).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Julia` L43, L73, L87, L119, L141, L153, … (15 lines). central (2–4): as `Julia`: the Kael-Julia link, „sub-protokollare und nicht-lokale Verbindung“ to a deeper Realitätsebene „(repräsentiert durch Julia“ (L188); outside AEGIS's rules (L190); misread by AEGIS (L192); the Monstergruppe as its analogy (L196).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L25, L28, L43, L73, L87, … (55 lines). central (2–4): „ein Avatar einer Struktur, die von der Monstergruppe (M) inspiriert ist“, a Kohärenz-Insel from the Potentialmeer (L172); DID induced by AEGIS (L172); journey from induced fragmentation to integration (L180); the plot seed where he recognises it (L308).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L129, L134, L155. minor (1–2): „Überwacht den Möglichkeitsstrom“ (L134).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L43, L101, L109, L127, L147, L160, … (18 lines). central (2–4): „von AEGIS geschaffene Simulationsumgebungen“ (L164), „keine statischen Kulissen“ (L166); the guardian list names them Konstrukt-Stadt, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom (L131–L134).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); Kohärenz-Inseln belong to the Potentialmeer — said there.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L131, L152, L164. minor (1–2): LogOS „Überwacht die Konstrukt-Stadt“ (L131).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L129, L131, L152. minor (1–2): LogOS over the Konstrukt-Stadt, logic and control (L131).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L129, L132, L145, L153, L299. minor (1–2): „Überwacht den Resonanz-Nebel“ (L132).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L182. minor (1–2): Kael's healing as „die Annahme seiner Multiplizität“ (L182), against AEGIS's methods.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L156. minor (1–2): Sophia's cell „Übergeordnet/Nexus“ in the hypothetical table (L156) — stands once, undefined.
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L188. minor (1–2): Julia as „eine“ Partnerin — cut before the inner quotes (L188).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L17, L19, L23, L24, L25, … (24 lines). central (2–4): „Das Fundament der dargestellten Realität bildet das Potentialmeer“ (L19), pure informational potentiality, with Kohärenz-Inseln as the origin of Kael's essence (L19); Aristoteles' Dunamis (L23); AEGIS's source, against which it fights (L30, L49).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L103. minor (1–2): „der von AEGIS aufrechterhaltenen Realitätsebene“ (L103); the deeper Realitätsebene the K-J link reaches (L188).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L57, L65, L93, L103, L166, L243, … (9 lines). minor (1–2): Risse described as system instabilities (L166) — cut before the inner quotes; thermodynamic costs feeding them (L103).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L174. minor (1–2): an Alter here, in the list of ten (L174), not a Guardian.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L129, L135, L156, L299. minor (1–2): „Überwacht potenziell eine übergeordnete oder integrierende Funktion“, „Funktion im Konzept weniger klar definiert“ (L135).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L43, L101, L273, L301, L313. minor (1–2): „AEGIS' Domäne (die Überwelt)“ (L43).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-signatur`: `Signatur` (near `entropiesignatur`). occurrence: `Signatur` in the document's sense, not the Entropie-Signatur.
- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`). occurrence: Kohärenz-Inseln, on potentialmeer.
- `landauer-signatur`: `Signatur` (near `landauersignatur`). occurrence: as for entropie-signatur.
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). occurrence: Der Architekt is an Alter (L174).
- `residual-echos`: `Das Echo` (near `residualechos`). occurrence: Das Echo is an Alter (L174).


**Record entries** (one file each):

- **`c16-kael-origin`**: Kael „ein Avatar einer Struktur, die von der Monstergruppe (M) inspiriert ist“ and a Kohärenz-Insel from the Potentialmeer (L172); dated 2025-04-26.
- **`c3-emergenz-origin`**: AEGIS emerges by autopoiesis from the Potentialmeer (L49), with Aristoteles' Dunamis (L23).
- **`c2-entropie-sense`**: entropy in the sea „im Sinne maximaler Möglichkeit“ (L19).
- **`c6-guardians-count-and-pairing`**: five Guardians, one per world, Sophia over an integrating function (L129–L135); Silas an Alter (L174).
- **`q5-guardians-and-kern-welten`**: the pairing with other world names — Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom (L131–L134).
- **`q6-nexus-ueberraum-ueberwelt`**: Nexus once in Sophia's cell (L156); the Überwelt as AEGIS's domain (L43).

**Not promoted:** the five protocols (OBP, RIVE, PMAS, SARM, CCPP), Kohärenz-Inseln (on potentialmeer), the Kael-Julia link's names (on juna and kael), Monstergruppe and Moonshine metaphors, the eight Alters without a page, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom (on kern-welten), the plot seeds, borrowed theory.

**Two readers**, disjoint: (1) kael, juna, partnerin, did, alters, silas, multiplizitaet, potentialmeer, emergenz, entropie, genesis, realitaetsebenen and the records c16, c3, c2; (2) aegis, guardians, logos, mnemosyne, cerberus, kairos, sophia, nexus, kern-welten, konstrukt-stadt, ueberwelt, risse and the records c6, q5, q6.
