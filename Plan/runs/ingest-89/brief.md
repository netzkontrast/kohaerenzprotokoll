# Brief — readings from document 89 (step 6)

1 document, one reader, one batch: `ingest-89`. Files go to `Plan/runs/ingest-89/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 89 | `outline-2` | 2025-05-03 | „the new-format outline“ (titled `Outline`) | a German chapter outline of 2025-05-03, a prologue and 39 chapters in three acts, which calls itself „Zusammenstellung der Outline-Informationen (Neues Format)“ (L15); each chapter one hedged paragraph plus the fields `Core Theme`, `Kael Internal`, `AEGIS Focus`, `Setting`, `Subplots`, `Philosophy`, `Genre/Trope`; the same outline as document 88 in another format (55 of its lines match), so a **light pass**: readings only on the pages where it adds or changes something; no chapter readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (586 lines for `outline-2`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan with its own question marks: write „the new-format outline plans …“; keep its hedges (`?`, `oder`) in the quotation. **Light pass:** document 88 (`kontext-outline`) holds the same outline; write a reading only where this document says something that page lacks, and name the document-88 reading it adds to or differs from in a sentence. `read.py` drops digits glued to words (`KW1`): quote around them; a backslash-escaped `\!` cannot be cited (quote around it). Bracketed chapter titles are escaped in the export (`\[`).

## Pages — document 89, `outline-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L25, L27, L28, L29, L43, … (110 lines). reading (3–5): the prologue (L23): „die Entität AEGIS oder ihr Vorläufer-Ich (Komponente 734)“, the emergence from the Nichts-Rauschen, the Resonanz with an external anomaly that triggers the crisis (`Juna/V?`) and the violent fragmentation of Komponente 734 as „der Geburtsstunde von System Kael“; chapter 20 and 24 on the paradox (L307, L363); chapter 33 (L491).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L67, L69, L70, L72, L75, L81, … (13 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L179, L182, L196, L223, L226, L240, … (12 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L151, L153, L155, L156, L157, L349, … (13 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L23. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L382, L567. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L21, L449. reading (1–2): the prologue's bracketed title `Genesis` (L21) and its being named again as the possible core trauma (L449).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L149. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L59, L101, L115, L157, L257, L265, … (13 lines). reading (2–3): the guardian by world — chapters 2, 5, 9 (L53, L95, L151) and the dual guardians Kairos (Potenzial/Chaos) and Sophia (Weisheit/Struktur) of chapter 17 (L263 on).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L23. reading (2–3): Juna/V as the external anomaly in the prologue (L23, with its question mark); chapter 19's guess list on her nature (L293) and chapter 25's (L377).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L26, L29, L39, L42, L45, … (120 lines). reading (2–3): Kael as host in chapter 1 with „Keine bewusste Wahrnehmung anderer Anteile“ (L39); the end state in chapter 38 (L565) and chapter 39's open end (L576).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L265, L269, L270, L271. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L95, L98, L109, L112, L151, L154, … (10 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L23. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L23, L491. reading (2–3): L23, the prologue — AEGIS's precursor and its violent fragmentation; chapter 33's question whether Kael can address its echo.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Konstrukt-Stadt` alone on L51. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L39, L42, L53, L55, L56, L67, … (23 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L109, L112. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L53, L55, L57, L58, L59, L95, … (12 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L95, L99, L100, L101, L109, L111, … (19 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L95, L98, L109, L112. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L397, L579; `Multiplizität` L210, L397, L563, L565, L576, L578, … (7 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L23, L28. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L151, L154, L349, L463. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L505. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Resonanz-Landschaft` alone on L93. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L81, L83, L84, L98, L165, L168, … (11 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L39, L179. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L26, L168, L321, L324, L391, L394, … (11 lines). reading (2): Selene offered as a guess — „Selene als Koordinatorin?“ (L394), „Kael (integriertes System, Selene?)“ (L548).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L265, L269, L271. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L125. reading (1): `TSDP` stands only inside „Interne Barrieren und die Angst voreinander (TSDP-Dynamiken)“ (L125) and is never expanded.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L28, L184, L212, L221, L223, L227, … (25 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.
- `juna`: `Juna/V` (near `juna`), `Juna/V Focus` (near `juna`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.
- `residual-echos`: `Echo` (near `residualechos`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.


**Record entries** (one file each; light pass):

- **`q7-what-734-names`**: AEGIS's „Vorläufer-Ich (Komponente 734)“ (L23) — and the fragmentation of 734 as the birth of System Kael.
- **`c16-kael-origin`**: the same prologue as Kael's origin.

**One reader**: write only the pages above that carry a reading, plus the two records.
