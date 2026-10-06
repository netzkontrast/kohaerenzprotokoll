# Brief — readings from document 152 (step 6)

1 document, one reader, one batch: `ingest-152`. Files go to `Plan/runs/ingest-152/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 152 | `kohaerenz-protokoll-plotideen-extraktion` | 2025-04-26 | „the concept extraction“ (titled `Konzeptuelle Analyse und Narrative Potentiale`, L11) | a German analysis of 2025-04-26 in nine chapters — the Potentialmeer, AEGIS and its protocols, its limits, the K-J connection and the Monstergruppe, Kael's DID read through IFS, the Kernwelten and Guardians, the core conflict — and 19 abstract plot ideas (L390–L587); a sibling of document 149, same date, different text; it calls itself a „konzeptuelle Landkarte“ (L610), hedges throughout and marks its Alter table „Hypothetische Zuordnung“ (L271) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (701 lines for `kohaerenz-protokoll-plotideen-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that proposes: write „the concept extraction analyses / proposes …“; keep its hedges („könnte“, the question marks of Table 3). It is a sibling of document 149 — where it says the same, say so in one clause and quote its own line; do not copy 149's reading. Juna is `Julia` here, read on juna. Borrowed theory (Floridi, Gödel, Ashby, Landauer, Schwartz) is the document's application, attributed. German — quote as written; cut before inner straight quotes and glued reference digits.

## Pages — document 152, `kohaerenz-protokoll-plotideen-extraktion`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L24, L30, L32, L41, L42, … (137 lines). central (2–4): „AEGIS entsteht nicht durch Design, sondern emergiert durch Selbstorganisation“ (L49); „definiert sich primär durch Negation und Abgrenzung“ (L30); its aim „die Maximierung und Aufrechterhaltung systemischer Kohärenz“ (L57); its limits act together — „Das Scheitern von AEGIS ist somit kein einzelner Fehler“ (L153); it reads the K-J connection as maximal threat (L180).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L219, L221, L225, L233, L411, L438, … (8 lines). minor (1–2): the ten Alters in one line (L233), read as IFS parts in the hypothetical Table 3 (L271–L281), Praetor and Index with question marks.
- **`ani`** (minor, 1–4): the census's surfaces — `ANI` L57. minor (1–2): „Assume Non-Intentionality, ANI“ in AEGIS's philosophy of trustlessness (L57) — stands once.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L257, L267, L498. minor (1–2): „Cerberus (Schattenlabyrinth - Abwehr/Angst)“ (L267), the failure of boundary-drawing.
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L143, L167, L215, L217, L219, L221, … (11 lines). central (2–4): Kael's DID „keine inhärente Eigenschaft seiner M-Avatar-Natur“ but a consequence of AEGIS's analytic trauma (L221); AEGIS in the perpetrator's role (L223); IFS from Richard Schwartz (L227); the aim, access to the Self (L235).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L24. minor (1–2): „Die Emergenz von AEGIS aus diesem Meer“ (L24).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. minor (1–2): the sea's „maximale Entropie im Sinne von Möglichkeit“ (L19).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L255, L257, L261, L263, L269, L400, … (17 lines). central (2–4): „Jeder Guardian ist für die Überwachung und Steuerung einer spezifischen Kernwelt zuständig“ (L257); each with its blind spot (L259); „Guardians als verkörperte Limitationen“ of AEGIS (L263–L269); five Guardians for four worlds.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Julia` L19, L28, L41, L59, L75, L79, … (17 lines). central (2–4): as `Julia`: the K-J connection operates below the reach of AEGIS's protocols (L177), stabilises Kael (L179), is read by AEGIS as maximal threat (L180); the origin-island „mit einer Entität oder einem Prinzip namens“ Julia (L181); the Julia-Signatur in the plot ideas.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L28, L41, L59, L61, L72, … (77 lines). central (2–4): an M-Avatar whose DID is AEGIS's doing (L221); access to his Self (L235); the plot ideas — integration raises his coherence (L463, L464), the final dissolution into the sea (L587).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L257, L268, L498. minor (1–2): „Kairos (Möglichkeitsstrom - Potential/Kreativität)“ (L268).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L43, L55, L61, L71, L73, L83, … (38 lines); `Kernwelt` L43, L55, L61, L71, L73, L83, … (42 lines). central (2–4): „Die Kernwelten (Konstrukt-Stadt, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom) sind von AEGIS geschaffene Simulationsumgebungen“ (L241), „einem doppelten Zweck“ (L241); „Die Kernwelten sind explizit Simulationen“ (L73).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–2): „zwei gegensätzlichen Prinzipien der Kohärenz“ (L289); AEGIS's aim of systemic coherence (L57).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L241, L265. minor (1–2): the first world in the list (L241) and LogOS's (L265).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L257, L265, L498. minor (1–2): „LogOS (Konstrukt-Stadt - Logik/Kontrolle)“ (L265), the limits of formal logic.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L257, L266, L487, L498. minor (1–2): „Mnemosyne (Resonanz-Nebel - Emotion/Erinnerung)“ (L266).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L269, L474. minor (1–2): „Sophia (Nexus/Übergreifende Weisheit?)“ (L269); Nexus in plot idea 9 (L474).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L17, L19, L21, L23, L24, … (38 lines). central (2–4): „Das Potentialmeer stellt die fundamentalste Ebene der Realität dar“ (L19); „kein Nichts, sondern die Quelle aller denkbaren Möglichkeiten“ (L19); Kohärenz-Inseln as the origin of Kael's and Julia's essences (L19); the substrate of Floridi's Infosphäre (L23); plot idea 16, the sea intruding (L557).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L41. minor (1–2): the Potentialmeer as „Fundamentalste Realitätsebene“ in the table (L41).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L32, L90, L119, L164, L211, L248, … (17 lines). central (2–4): the cracks' possible causes, „Sie könnten verschiedene Ursachen haben“ (L248) — the K-J connection (L250), thermodynamic artefacts; costs that may show as Risse (L32).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L233, L280. minor (1–2): an Alter in the list of ten (L233) and Table 3 (L280), not a Guardian.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L257, L269, L498. minor (1–2): „Sophia (Nexus/Übergreifende Weisheit?)“ — the fifth Guardian with no world (L269).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L73, L79, L81, L83, L89, L91, … (16 lines). central (2–4): „Die Überwelt ist die abstrakte, informationsbasierte operative Domäne von AEGIS“ (L83); whether the Überwelt and the sea are simulations too is left open (L73).
- **`ztv`** (minor, 1–4): the census's surfaces — `ZTV` L57. minor (1–2): „Zero Trust Verification, ZTV“ in AEGIS's philosophy of trustlessness (L57) — stands once.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero Trust Verification` (near `zerotrust`). occurrence: Zero Trust Verification is read on ztv.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Inseln` (near `koharenz`). occurrence: the novel's title; Kohärenz is read on kohaerenz above.
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). occurrence: Der Architekt is an Alter (L233).
- `residual-echos`: `Das Echo` (near `residualechos`). occurrence: Das Echo is an Alter (L233).


**Record entries** (one file each):

- **`c16-kael-origin`**: Kael's „M-Avatar-Natur“, his DID AEGIS's doing (L221); the origin-island associated with Julia (L181); dated 2025-04-26.
- **`c3-emergenz-origin`**: „AEGIS entsteht nicht durch Design, sondern emergiert durch Selbstorganisation“ (L49), „Die Emergenz von AEGIS aus diesem Meer“ (L24).
- **`c6-guardians-count-and-pairing`**: five Guardians, four worlds, Sophia with a question mark (L257, L265–L269); Silas an Alter (L233).
- **`q5-guardians-and-kern-welten`**: the pairing LogOS–Konstrukt-Stadt, Mnemosyne–Resonanz-Nebel, Cerberus–Schattenlabyrinth, Kairos–Möglichkeitsstrom, Sophia–„Nexus/Übergreifende Weisheit?“ (L265–L269).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as AEGIS's operative domain (L83); Nexus in Sophia's line (L269).

**Not promoted:** the five protocols and v1.4/v1.5 (on aegis), the six limitations (borrowed), Kohärenz-Inseln (on potentialmeer), the K-J connection's names, Monstergruppe, Moonshine, M-Substrat, Julia-Signatur (on juna), Paradoxon-Cluster, the IFS roles and the eight Alters without a page, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom (on kern-welten), the 19 plot ideas, Infosphäre and the other borrowed theory.

**Two readers**, disjoint: (1) kael, juna, did, alters, silas, potentialmeer, emergenz, entropie, realitaetsebenen, risse and the records c16, c3; (2) aegis, ztv, ani, kohaerenz, ueberwelt, kern-welten, konstrukt-stadt, guardians, logos, mnemosyne, cerberus, kairos, sophia, nexus and the records c6, q5, q6.
