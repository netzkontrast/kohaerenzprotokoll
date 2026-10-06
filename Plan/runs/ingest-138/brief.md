# Brief — readings from document 138 (step 6)

1 document, one reader, one batch: `ingest-138`. Files go to `Plan/runs/ingest-138/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 138 | `umfassendes-lokalitaeten-konzept-fuer-roman` | 2025-04-18 | „the place profiles“ (titled `Umfassendes Lokalitäten-Konzept: Kohärenz Protokoll`, L11, with English glosses) | a German location concept of 2025-04-18: design principles (Teil I, L21–L100), then 31 numbered place profiles by level — KW1 (L106), KW2 (L241), KW3 (L346), KW4 (L436), Überwelt (L541) — each in eight labelled fields; its purpose a „Welt-Bibel“ of at least 30 places (L17), the profiles „Beispiele für den erforderlichen Detailgrad“ (L104); a promised appendix is missing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (747 lines for `umfassendes-lokalitaeten-konze`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept proposes: write „the place profiles describe / assign …“; place names come with inner straight quotes ("Vergessener Schrein", "Narbe", "Ankerpunkt", "Anya") — cut quotations before them or name them in backticks; glued footnote digits cut off; bracketed source ranges like [235-267] are its own. Alter names in single quotes ('Index', 'Limina') are its own of 2025-04-18. Kael is male.

## Pages — document 138, `umfassendes-lokalitaeten-konzept-fuer-roman`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L31, L34, L35, L43, L44, L46, … (40 lines). central (2–4): the Überwelt as AEGIS-Domäne (L43); profile 30, the AEGIS Analyse-Hub / Guardian Koordinationszentrum (L543); what L44–L47 say of AEGIS.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L31, L32, L58, L67, L100, L178, … (16 lines). central (2–4): KW1 „das natürliche Habitat für den Index-Alter“ — cut before the quote if any (L67); find the alters named per world (L31, L58, L67, L100).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L31, L33, L57, L67, L89, L100, … (23 lines). central (2–4): KW3 „Grenzfeste (Cerberus)“ (L346); profile 20, Cerberus' Kontrollzentrum (L393).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L31, L75, L203, L209. minor (1–2): the worlds externalising Kael's psyche and his dissociation (L31); L75.
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L34, L45, L46, L57, L92, L116, … (42 lines). central (2–4): the theme „Entropie versus Ordnung“ (L34); what L45–L46 and L92 say.
- **`grenzfeste`** (central, 3–12 quotations): the census's surfaces — `Grenzfeste` L67, L89, L100, L346, L352, L367, … (11 lines). central (2–4): KW3 (L346); profiles 17–21 (L348–L408); a Festung or Labyrinth (L33).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L34, L35, L74, L548, L551, L553, … (9 lines). minor (1–2): the Guardian-Domäne of the Überwelt (L541); profile 30's Koordinationszentrum (L543).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L119, L178, L179, L188, L194, L254, … (27 lines). central (2–4): profile 12, „Ort spezifischer Juna-Erinnerung (warm/schmerzhaft)“ (L273); profile 28, Junas Ankerpunkt in KW4 (L513–L518); what L119, L178 say.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L32, L34, L35, L44, L45, … (117 lines). central (2–4): „Die vier Kern-Welten (KW1-4) des Romans fungieren als Externalisierungen der Psyche des Protagonisten Kael“ (L31); profile 1, Kaels Initiale Wohneinheit (L108); profile 3, his workplace Datenknotenpunkt Gamma-7 (L138).
- **`kaels-wohneinheit`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kaels Wohneinheit` alone on L172. minor (1–2): profile 1, „Kaels Initiale Wohneinheit“ (L108) and what its fields say.
- **`kairos`** (central, 3–12 quotations): the census's surfaces — `Kairos` L31, L67, L436, L446, L461, L476, … (10 lines). central (2–4): KW4 „Möglichkeits-Garten (Kairos/Sophia)“ (L436); what L446, L461 say.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L31, L33, L43, L46, L58, L88, … (19 lines). central (2–4): „Externalisierungen der Psyche“ (L31); the four worlds with their Guardians (L106, L241, L346, L436); symbolism and archetypes (L33).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9).
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L106, L112, L127, L128, L142, L157, … (11 lines). central (2–4): KW1 „Konstrukt-Stadt (LogOS)“ (L106); profiles 1–7 (L108–L198): Wohneinheit, Transitkorridor, Datenknotenpunkt, Pausenbereich, Interface, Schlafnische, Therapie-Ort.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L31, L47, L57, L67, L88, L106, … (14 lines). central (2–4): KW1's Guardian (L106); L47, L57, L67, L88.
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L31, L44, L67, L94, L241, L251, … (16 lines). central (2–4): KW2 „Resonanz-Landschaft (Mnemosyne)“ (L241); profile 15, Mnemosynes Archiv-Schnittstelle (L318) — cut before the quote.
- **`moeglichkeits-garten`** (central, 3–12 quotations): the census's surfaces — `Möglichkeits-Garten` L67, L68, L93, L99, L436, L442, … (12 lines). central (2–4): KW4 (L436); profiles 23–28 (L438–L513), among them a Muse encounter (L453) and the Nexus-Knoten (L468).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L100, L194, L269, L314. minor (1–2): find Oblivion's lines (L100, L194, L269) — briefly.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L206. occurrence unless L206 says what Personas are in the world — then minor.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L19, L74, L76. minor (1–2): „Detaillierte Lokalitäten-Profile nach Realitätsebene“ (L102); L19, L74.
- **`resonanz-landschaft`** (central, 3–12 quotations): the census's surfaces — `Resonanz-Landschaft` L58, L67, L75, L241, L247, L262, … (11 lines). central (2–4): KW2 (L241); profiles 10–15 (L243–L318): Ankunftszone, Vergessener Schrein, Juna-Erinnerung, Zone Emotionaler Stürme, the Narbe, Mnemosyne's archive.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L44, L45, L47, L59, L74, L76, … (58 lines). central (2–4): profile 21, „Zerfallende Mauer / Riss-Zone“ (L408); what L44–L47, L59 say of the Risse.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L67, L284, L299, L314, L344, L374, … (9 lines). minor (1–2): find Silas's lines (L67, L284, L299) — briefly.
- **`sophia`** (central, 3–12 quotations): the census's surfaces — `Sophia` L31, L67, L436, L446, L458, L461, … (10 lines). central (2–4): the same: KW4 shared with Kairos (L436); L458, L461.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L43, L46, L74, L93, L95, L96, … (14 lines). central (2–4): „Überwelt (AEGIS/Guardian-Domäne)“ (L541); profiles 30–31 (L543, L558); its design as a virtual reality (L43).
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — `Vergessener Schrein` L33, L258, L262. minor (1–2): profile 11, the Vergessene Schrein / Kern-Trauma-Lokus in KW2 (L258) — cut before the quote; what L262 says.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `junas-ankerpunkt`: `Ankerpunkt` (near `junasankerpunkt`). a reading, minor (1–2), by Reader 1: profile 28, Junas Ankerpunkt / Symbolort in KW4 „(oder potenziell auch in anderen KW)“ (L513–L518).
- `nexus`: `Nexus-Knoten` (near `nexus`). a reading, minor (1), by Reader 1: profile 25, the Nexus-Knoten / Interface zum Potenzial in KW4 (L468).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` in passing.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: LogOS KW1, Mnemosyne KW2, Cerberus KW3, Kairos/Sophia KW4 (L106, L241, L346, L436) — dated 2025-04-18.
- **`q5-guardians-and-kern-welten`**: the same, and the Überwelt as Guardian-Domäne (L541).
- **`c9-konstrukt-stadt-scale`**: „KW1: Konstrukt-Stadt (LogOS)“ (L106) — KW1 only.
- **`q6-nexus-ueberraum-ueberwelt`**: the Nexus-Knoten as an interface to potential in KW4 (L468).

**Not promoted:** the 31 places themselves (read on the pages of their worlds), the Anya/Muse encounter (L453 — a name `Anya` stands on kairos, silas, lex already; read on moeglichkeits-garten only), Datenknotenpunkt Gamma-7, the Narbe, Auge des Sturms, the design principles and borrowed theories.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, ueberwelt, guardians, logos, mnemosyne, cerberus, kairos, sophia, juna, junas-ankerpunkt, nexus, entropie, risse, and the entries c6, q5, q6.
- Reader 2: kael, kaels-wohneinheit, alters, oblivion, silas, did, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, realitaetsebenen, vergessener-schrein, personas (if read), and the entry c9.
