# Brief — readings from document 84 (step 6)

1 document, one reader, one batch: `ingest-84`. Files go to `Plan/runs/ingest-84/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 84 | `ai-assisted-narrative-coherence` | 2025-10-15 | „the English compilation“ — name the part: „the ARCHON proposal“, „the AEGIS analysis“, „the blueprint“, „the concept document“, „the critique“, „the methodology report“, „the three-act blueprint“, „the Kael biography“, „the strategy paper“, „the scene outline“, „the architecture analysis“ | an English compilation of 2025-10-15: fourteen separately headed texts (L11 ARCHON proposal, L124 AEGIS analysis, L219 simple guide, L279 distillation, L339 „Definitive Narrative & Conceptual Blueprint“, L525 concept document, L652 critical review, L732 methodology report, L831 three-act blueprint, L931 critique — written out twice, L1001–L1069, L1073 Kael biography, L1157 strategy paper, L1273 scene-by-scene outline of Kap 1–39, L1671 architecture analysis with a lexicon); the blueprint calls itself „the canonical architectural blueprint for the project“ (L343) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1836 lines for `ai-assisted-narrative-coherenc`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **Fourteen texts, one file — name the part you read.** Every reading names its part (see the table) and its line; parts disagree with each other, and that is recorded, not resolved. The blueprint's claim to canon (L343): record once on `aegis`, never apply. The ARCHON proposal (L11–L122) is about an AI tool; it uses the novel as a case study — read from it only what it says of the novel. The critique at L931 is doubled at L1001: cite the first copy. Quote the English as written; the German terms in it are the document's. Chapter content goes on the chapter pages (a later batch): on a term page, at most one or two beats by chapter number.

## Pages — document 84, `ai-assisted-narrative-coherence`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L97, L124, L128, L134, L136, L137, … (297 lines). central (5–7): the AEGIS analysis (L124–L217) — its tragic architecture; the blueprint's canon claim once (L343); its fate as the parts give it; name each part.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L1312, L1313, L1357, L1359, L1363, L1366, … (7 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L1227. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L96, L242, L249, L433, L439, L585, … (12 lines). minor (2): „eleven identified alters“ (L431) against tables of six (L435), five (L1101) and eleven rows (L1751) — record each with its part.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L1383, L1449, L1458, L1470, L1598, L1764, … (7 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L477, L570, L874, L949, L1019, L1203, … (16 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L96. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L1175. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L1724, L1725, L1726, L1727, L1728. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L601, L1730, L1732. minor (1–2): section 3.2 of the architecture analysis, „The Überwelt and the Externe Ebene“ (L1730–L1732 and on).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L136. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`goedel-gambit`** (central, 3–12 quotations): the census's surfaces — `Gödel-Gambit` L259, L317, L321, L335, L352, L410, … (13 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L1727. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L791, L793, L795, L797, L800, L904, … (11 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L1542, L1546, L1549, L1551, L1552, L1563, … (8 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L158. central (3–5): the concept document (L525–L650) on Juna/V; her names and forms across parts (Juna Echo, Juna-Resonanz).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L157, L176, L177, L181, L183, L187, … (357 lines). central (4–6): the Kael biography (L1073–L1155) — and Einheit K-1123 (L1079), which only it writes; his journey as the blueprint and the scene outline give it.
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L950. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L351, L465, L467, L561, L563, L710, … (17 lines); `Kernwelt` L351, L465, L467, L561, L563, L567, … (32 lines). minor (1–2): the worlds as the parts name them; KW4 as `Kairos/Sophia` (L950) and `Kairos-Potentialis`; the KW1 guardian as „Guardian of KW1 (Logik)“ (L801) and LogOS (L1322).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L247, L287, L309, L440, L441, L442, … (34 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L1814. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L94. not read: title — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L812, L1725. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L246, L299, L309, L440, L441, L442, … (44 lines). minor (1–2): what the parts say of Lex; record that the three-act blueprint gives „Dr. Aris Thorne“ as a protagonist who goes by Lex (L835) while the scene outline makes Dr. Aris Thorne an AEGIS therapy construct (L1373–L1376).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L1516, L1521, L1523, L1524, L1525, L1542, … (8 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L847, L947, L1017, L1322, L1327, L1725. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L473, L569, L873, L948, L1018, L1202, … (25 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L1728. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L265, L353, L372, L374, L603, L605, … (9 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L1553, L1555, L1563, L1567, L1760. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L1174, L1184, L1681. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`nichts-rauschen`** (central, 3–12 quotations): the census's surfaces — `Nichts Rauschen` L136, L229, L368, L391, L531, L533, … (10 lines). minor (1): its three English glosses — „Nothingness Noise“ (L136), „Nothingness Roaring“ (L229), „Nothing Noise“ (L533).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L247, L287, L299, L309, L440, L441, … (40 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L531, L533. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L1726. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L299, L441, L443, L444, L695, L970, … (25 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L287, L351, L463, L471, L475, L664, … (15 lines); `Glitches` L843, L1083; `Glitch` L843, L849, L851, L943, L1013, L1083, … (7 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L440, L445, L695, L1106, L1107, L1110, … (24 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L950. minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L96, L244, L285, L422, L424, L426, … (30 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L461, L463, L557, L559, L898, L1419, … (11 lines). minor (1–2): read by the census's surfaces: what the parts say of it — 2–4 quotations, each naming its part.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence (J69).
- `emergenz`: `Emergenz durch Negation` (near `emergenz`). reading (1) on `emergenz` if `Emergenz durch Negation` is explained in its line; else occurrence.
- `genesis`: `Genesis Crisis` (near `genesis`). reading (1) on `genesis`: the Genesis Crisis as the parts give it.
- `juna`: `Juna/V` (near `juna`), `Juna Echo` (near `juna`), `Juna-Resonanz` (near `juna`), `Juna-construct` (near `juna`). reading, above.
- `kairos`: `KW4: Kairos-Potentialis` (near `kairos`), `Kairos-Potentialis` (near `kairos`), `Kairos/Sophia` (near `kairos`). reading (1) on `kairos`: KW4, Kairos-Potentialis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz statt Wahrheit` (near `koharenz`), `Kohärenz-Verifikator` (near `koharenz`), `Kohärenz-Validierung` (near `koharenz`), `Kohärenz wiederhergestellt` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence (J12).
- `negentropie`: `Negentropie-Fehlinterpretation` (near `negentropie`). reading (1) on `negentropie` if the line says what the misinterpretation is; else occurrence.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`), `Tertiary Structural Dissociation of the Personality` (near `persona`), `Emotional Personality parts` (near `persona`). occurrence (J69): the full name of TSDP.
- `sophia`: `Kairos/Sophia` (near `sophia`). reading (1) on `sophia`: KW4 as Kairos/Sophia (L950).


**Record entries** (find the lines; one file each, naming the part):

- **`c6-guardians-count-and-pairing`**: the guardians the parts name and pair with the worlds.
- **`q5-guardians-and-kern-welten`**: the pairing of guardians and Kernwelten, and the KW1 guardian's two names (L801, L1322).
- **`c13-externe-ebene-beyond-the-simulation`**: section 3.2 (L1730 on).
- **`q3-how-many-kern-welten-and-alters`**: the alter counts (L431, L435, L1101, L1751).
- **`q8-aegis-after-the-vortex`**: AEGIS's end as the parts give it.
- **`c16-kael-origin`**: the concept document's origin of the simulation and Juna/V (L525 on), if it speaks to Kael's origin.

**Split into two readers, one after the other:**
- Reader 1: aegis, juna, kael, the guardians' and worlds' pages (guardians, logos, mnemosyne, cerberus, kairos, sophia, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten), externe-ebene, ueberwelt, potentialmeer, nichts-rauschen, entropie, negentropie, emergenz, genesis, risse, moonshine-link, goedel-gambit, algorithmische-melancholie, kishotenketsu, and all six records.
- Reader 2: the alters' pages (alex, argus, isabelle, kiko, lex, lia, moros, nyx, rhys, selene, alters), multiplizitaet, tsdp, did.
