# Brief — readings from document 85 (step 6)

1 document, one reader, one batch: `ingest-85`. Files go to `Plan/runs/ingest-85/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 85 | `outline` | 2025-07-30 | „the outline“ (titled `Outline`) | a German plot outline of 2025-07-30 in the voice of a „Narrativer Architekt“ who distils „einen klaren Bauplan“ from unnamed drafts (L11, L13): Teil 1 lists Kap 1–13 (L17–L91) and Teil 3 Kap 27–39 (L154–L266) under repeated field labels (Inhalt/Plot, Fokus, Erzählperspektive, Thematische Kernfrage, Subplot-Integration, Reisestufe); Teil 2 (Kap 14–26, L93–L152) has no chapter list, only six Roman-numbered thematic sections; no canon claim, no lock |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (276 lines for `outline`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the outline plans …“, never as what the novel is. Its hedges stay (`möglicherweise`, `z.B.`, `oder`): Argus at L71 is an example („z.B. Argus“), keep the example as an example. Teil 3's chapters carry joined alternative titles separated by „/“ (L158 on) — quote them as joined, decide nothing between them. Recorded by the reader, not to be repaired: a gap at L174 („in abweicht“), one sentence repeated in Kap 29 and Kap 31 (L178, L196), Argus a Wächter at L71 and an EP at L116. `read.py --find` drops digits glued to words (`KW1` compares as `KW`): quote around them. Chapter content goes on the chapter pages (a later batch): on a term page, at most one or two beats by chapter number.

## Pages — document 85, `outline`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L24, L36, L46, L47, L61, … (51 lines). central (4–6): AEGIS as the outline plans it across the three Teile — its control in KW1 (Kap 1–2), the Gaslighting of Kap 8 (L59), the „Paradoxon der Fehlausgerichteten Kohärenz“ where the outline names it, its defences and end in Teil 3 (Kap 27–37, „Das Erbe von AEGIS“).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L116. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L37, L57, L99. minor (1–3): the alters as the outline lists them; the ANP/EP division at L116.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L71, L116. minor (1–2): the Wächter example at Kap 10 (L71) and the EP list (L116) — record both, decide nothing.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L51, L132, L167, L170. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L37, L57, L82. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L89. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L105. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L164, L200, L209, L236, L263, L272. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L132. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L67, L128, L134, L173. minor (1–3): the Wächter as „personalisierte konzeptionelle Herausforderungen“ (Kap 10, L71), Kairos/Sophia as Guardians (L67), and „Die Wächter als Agenten & Charaktere“ in Teil 3.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L116. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L66, L67, L76, L77, L133, L142, … (22 lines). central (3–5): Juna and `Juna/V` — the Hilferuf aus der Leere (Kap 11, L74), the „Mysterium Juna/V & die Externe Ebene“ subplot, „Junas Hand: Die externe Intervention“ (Kap 31), „Die Wende der Partnerin“ (Kap 35).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L13, L19, L23, L24, L25, … (82 lines). central (4–6): his path from the awakening in KW1 (Kap 1, L21 on) to „funktionale Multiplizität“ (Kap 39); the Reisestufe labels (Heldinnenreise in Teil 1, Heldenreise stages in Teil 3) as the outline gives them.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L66, L67, L133. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L71, L105, L106, L126, L128, L205, … (7 lines). minor (1–3): the worlds as the outline names them — KW1 LogOS-Prime, KW4 Kairos-Potentialis (L66), section IV „Die Konfrontation mit AEGIS und den Kernwelten“ (L126 on).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L42, L116, L121. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the novel's title (L11) and „Kohärenz“ inside labels — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Konstrukt-Stadt` alone on L21. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L29, L30, L35, L36, L56, L77, … (18 lines). central (3–5): Lex as the logical part and analyst — Kap 2–3, the stylistic signature (L119), „Lex' Systemanalyse & AEGIS' Paradoxon“ as a subplot, its climax in Kap 28.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L116. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L23, L130, L203, L205. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L35, L131. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Möglichkeits-Garten` alone on L133. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L116. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L56. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L158, L160. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L223. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L116, L122. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L230. minor (1): `Die Wende der Partnerin` (Kap 35, L230) — what the chapter's lines say of her.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Resonanz-Landschaft` alone on L131. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L42, L72, L82, L116, L187. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L25, L30, L36, L95; `Glitches` L23. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L142, L203, L206. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L67, L133. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L19, L23, L57. minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L71, L84, L86, L87, L134, L158, … (7 lines). minor (1–2): what the outline says of it — 1–3 quotations, with the chapter or section it sits in.
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Trauma-Lokus` alone on L187. minor (1) only if the `Trauma-Lokus` line (L187) is the forgotten shrine the page means; else not read — occurrence, and say why.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Management` (near `entropie`). `Entropie-Management` is a compound of its own (J12): occurrence, unless the line says what entropy is — then a reading on `entropie`.
- `kohaerenz`: `Paradoxons der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenzprotokollen` (near `koharenz`). occurrences: the title and compounds (J9, J12).
- `multiplizitaet`: `funktionaler Multiplizität` (near `multiplizitat`), `Funktionalen Multiplizität` (near `multiplizitat`), `Kaels Weg zur Funktionalen Multiplizität` (near `multiplizitat`). readings: `funktionale Multiplizität` is the outline's goal for Kael — 2–3 quotations on `multiplizitaet` (L114, Kap 29, Kap 39).
- `residual-echos`: `Echo` (near `residualechos`). `Echo` alone is the outline's general word (Teil 1's title, `Echo-Lokus`): occurrence, unless a line names residual echoes.


**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, guardians, kern-welten, logos, mnemosyne, cerberus, kairos, sophia, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, ueberwelt, externe-ebene, nexus, nichts-rauschen, entropie, emergenz, risse, kohaerenz, partnerin, vergessener-schrein, and residual-echos only if it is a reading.
- Reader 2: the alters' pages (lex, alex, argus, isabelle, kiko, lia, moros, nyx, rhys, selene, alters), multiplizitaet, tsdp, did.

No conflict or question record is assigned. If a reader finds the outline answering an open record (`Wiki/conflicts/`, `Wiki/questions/`) directly, say so in the report; do not write a record entry.
