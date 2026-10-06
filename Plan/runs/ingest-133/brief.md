# Brief — readings from document 133 (step 6)

1 document, one reader, one batch: `ingest-133`. Files go to `Plan/runs/ingest-133/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 133 | `roman-lokalitaeten-konzept-und-ausarbeitung-2` | 2025-04-18 | „the locations concept (second version)“ (titled `Umfassendes Lokalitäten-Konzept für den Roman "Kohärenz Protokoll"`, L11) | a German concept of 2025-04-18 on the novel's places — another rendering of the locations concept read as document 129, same date, different wording: worldbuilding principles (Teil 1), the six Realitätsebenen with a table (L112–L124) and seven key places (Teil 2), research results (Teil 3), and a Teil 4 that describes the „finale, integrierte Dokument“ instead of writing it (L347–L361); conditional throughout, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (389 lines for `roman-lokalitaeten-konzept-und`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept proposes: write „the second locations concept assigns / describes …“; it is a sibling of document 129 — read only what it says, and where it says the same as 129 keep the reading short. Inner straight quotes ("Rissen", "Innere Bunker", "Nexus-Knoten") — cut quotations before them. `Insight N` and „Kontext Punkt 6“ point to text not in the file. Kael is male; Juna is called „Co-Protagonistin“ (L183).

## Pages — document 133, `roman-lokalitaeten-konzept-und-ausarbeitung-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L27, L29, L37, L43, … (63 lines); `Entropic Gatekeeper` L331. central (2–4): the Überwelt as „Betriebssystem und Kontrollzentrum für die gesamte Simulation“ — find the line (L172); a localisable AEGIS-Kern „unwahrscheinlich“ (L177); its protocols and Zero-Trust (L175).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L43, L62, L150, L153, L175, L177. minor (1–2): Zero-Trust in the Überwelt's rules (L175) and L43.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L128, L139, L146, L150, L155, L157, … (10 lines). central (2–4): the Grenzfeste's inner bunker as seat of the „Limina“-Alter — cut before the quotes (L155); what L128, L139, L150 say of alters per world.
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L121, L148, L150, L153, L155, L157, … (10 lines). minor (1–2): KW3 „Grenzfeste (Cerberus)“ (L148); the Innerer Bunker as Cerberus' control centre (L230–L232).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L15. occurrence unless L15 says more than DID in passing.
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L29, L43, L47, L51, L59, L62, … (29 lines). central (2–4): each level's `Manifestation von Rissen/Entropie` field (L134, L145, L156, L167, L178); in the Überwelt entropy „in ihrer reinsten Form“ (L178); not applicable to the Externe Ebene (L209).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L27, L60, L77, L124, L181, L322, … (7 lines). minor (1–2): „Eine Realität, die vollständig außerhalb des AEGIS-Kontrollsystems existiert“ (L183); its laws unknown (L206).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L35, L121, L148, L232, L267. minor (1–2): KW3 (L121, L148), defensive, labyrinthine (L121).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L87, L89, L106, L123, L128, L170, … (14 lines). central (2–4): one per level in the table (L119–L123): LogOS, Mnemosyne, Cerberus, Kairos/Sophia; AEGIS and Guardians in the Überwelt (L123).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L124, L135, L146, L155, L157, … (23 lines). central (2–4): the Externe Ebene „mit der Co-Protagonistin Juna verbunden“ (L183); „Dies ist Junas Herkunftsort“ (L210); Juna's intervention letting Kael see the Überwelt (L179).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L27, L29, L33, L35, … (67 lines). central (2–4): each world as a side of Kael (L128, L139, L150, L161); „Kael erwacht hier ohne Erinnerung an den Reboot“ (L221).
- **`kaels-wohneinheit`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kaels Wohneinheit` alone on L341. minor (1–2): „Kaels Initiale Wohneinheit (KW1)“ (L216): a perfect cube (L219), where Kael wakes after the reboot (L221).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L122, L159, L161, L164, L168, L242. minor (1–2): KW4 „Möglichkeits-Garten (Kairos/Sophia)“ (L159); L122.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L15, L27, L29, L33, L35, L43, … (23 lines). central (2–4): the table of six levels, four Kern-Welten with their Guardians (L119–L124); each world a side of Kael (L128, L139, L150, L161).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L35, L119, L126, L218, L266. minor (1–2): KW1 (L119, L126).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L106, L119, L126, L128, L131, L133, … (9 lines). minor (1–2): KW1's Guardian (L119, L126); LogOS' Kern-Präsenz (L133).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L120, L137, L139, L142, L144, L146, … (10 lines). central (2–4): KW2's Guardian (L120, L137); what L146 says of Mnemosyne.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L35, L91, L122, L159, L239, L265. minor (1–2): KW4 (L122, L159): potential, creativity (L161).
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L242. minor (1–2): the `Nexus-Knoten` in KW4 as „Interface zur Überwelt oder anderen Ebenen“ (L166) — cut before the straight quotes.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L139, L145, L150, L228. minor (1–2): an alter of KW2 and KW3 (L139, L150) — briefly.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L27, L110, L112, L114, L355, L365. minor (1–2): „A. Die 6 Realitätsebenen (Generelle Konzepte)“ (L112): KW1–4, Überwelt, Externe Ebene (L27, L355).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L35, L91, L120, L137, L226, L251. minor (1–2): KW2 (L120, L137), emotions and memories, physics dictated by emotion (L142).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L29, L37, L45, L87, L91, L104, … (19 lines). central (2–4): each level's Riss manifestation (L134, L145, L156, L167, L178); not applicable on the Externe Ebene (L209).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L139, L146, L161. minor (1–2): an alter named in KW2 and KW4 (L139, L161) — briefly.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L122, L159, L161, L164, L166, L168, … (7 lines). minor (1–2): the same: KW4 shared with Kairos (L122, L159).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L15, L27, L43, L47, L59, L62, … (29 lines). central (2–4): „5. Die Überwelt (AEGIS/Guardians)“ (L170): purely digital, informational (L172); Kael entering it, perhaps through a Riss or Juna's intervention (L179).
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vergessener Schrein` alone on L355. minor (1–2): „Ort des Kern-Traumas (KW2)“ (L223); a distorted version of a real place bound to the trauma (L226).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `junas-ankerpunkt`: `Ankerpunkt` (near `junasankerpunkt`). occurrence unless the reader finds `Ankerpunkt` said of Juna — then minor on junas-ankerpunkt.
- `nexus`: `Nexus-Knoten` (near `nexus`). `Nexus-Knoten` — on nexus above.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` in passing.
- `verschraenkungs-insel`: `Verschränkung` (near `verschrankungsinsel`). occurrence: `Verschränkung` the borrowed concept.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: five Guardians on four worlds, Kairos/Sophia sharing KW4 (L119–L122) — dated 2025-04-18.
- **`q5-guardians-and-kern-welten`**: the same table (L119–L123).
- **`c9-konstrukt-stadt-scale`**: „KW1: Konstrukt-Stadt“ (L119) — KW1 only.
- **`c13-externe-ebene-beyond-the-simulation`**: „vollständig außerhalb des AEGIS-Kontrollsystems“ (L183).
- **`q6-nexus-ueberraum-ueberwelt`**: the Nexus-Knoten in KW4 as an interface to the Überwelt (L166).

**Not promoted:** Innerer Bunker, AEGIS-Kern, the Insight references, Bachelard's Poetik des Raumes and the six comparison works, Teil 4's description of the final document.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, aegis-teilfunktionen, ueberwelt, guardians, logos, mnemosyne, cerberus, kairos, sophia, externe-ebene, juna, entropie, risse, nexus, and the entries c6, q5, q6, c13.
- Reader 2: kael, kaels-wohneinheit, alters, oblivion, silas, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, realitaetsebenen, vergessener-schrein, junas-ankerpunkt (if read), did (if read), and the entry c9.
