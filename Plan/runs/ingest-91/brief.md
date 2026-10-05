# Brief — readings from document 91 (step 6)

1 document, one reader, one batch: `ingest-91`. Files go to `Plan/runs/ingest-91/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 91 | `leserzentrierte-roman-outline-generierung-kohaeren` | 2025-05-03 | „the reader-centred outline“ (titled `Leserzentriertes Roman-Outline (Prolog + 39 Kapitel)`) | a German chapter outline of 2025-05-03, a prologue and 39 chapters in three acts, which names itself „Leserzentriertes Roman-Outline“ (L11); each chapter a hedged `Handlung` paragraph plus labelled lines (`Core Theme`, `Reader Psychology Note`, …); ends with „Quellenangaben“, a list of 39 web references (L521). It is a third generated version of the plan of documents 88 and 89 (3 matching lines each), so a **light pass**: readings only on the pages where it adds or changes something; no chapter readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (524 lines for `leserzentrierte-roman-outline-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan with its own question marks: write „the reader-centred outline plans …“; keep its hedges (`?`, `oder`) in the quotation. **Light pass:** documents 88 (`kontext-outline`) and 89 (`outline-2`) hold the same plan; write a reading only where this document says something that page lacks, and name the document-88 reading it adds to or differs from in a sentence. `read.py` drops digits glued to words (`KW1`): quote around them; a backslash-escaped `\!` cannot be cited (quote around it). Bracketed chapter titles are escaped in the export (`\[`).

## Pages — document 91, `leserzentrierte-roman-outline-generierung-kohaeren`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L20, L21, L24, … (140 lines). reading (3–5): the prologue (L15): out of noise a catastrophic event forces the rigid collective AEGIS; AEGIS suppresses Komponente 734 and activates the Kohärenz Protokoll as its „ultimative Abwehrmaßnahme“; Chapter 20 and 24 on the Kernparadoxon (L267, L271, L317).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L56, L58, L59, L60, L61, L64, … (20 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L154, L157, L167, L170, L193, L196, … (20 lines). reading (1–2): „der neu auftauchende Meta-Beobachter Argus“ (L154).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L128, L130, L132, L133, L134, L136, … (17 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L209. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L15. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L258. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L15. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L128. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L49, L88, L99, L134, L193, L225, … (16 lines). reading (2–3): the guardian by world — LogOS, Mnemosyne, Cerberus (L43, L93, L304) and the two of KW4 (L230).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L15. reading (2): „(implizit Juna/V)“ in the prologue (L15) and the open nature in Chapter 19 and 25 (L254, L330); L511 among the mysteries the end may leave open.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L18, L21, L24, L30, L33, … (175 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L230, L234, L235, L236. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L82, L85, L93, L96, L106, L128, … (14 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L15, L267, L425, L434, L460. reading (2–3): L15 — a pre-conscious entity wrestling for emergence, suppressed by the new collective and fragmented by the protocol, „die traumatische Geburtsstunde des Protagonistensystems Kael“.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L30, L33, L43, L45, L46, L49, … (37 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L93, L96, L106, L233, L374, L397. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L43, L45, L47, L48, L49, L51, … (17 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L82, L86, L87, L88, L91, L93, … (25 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L82, L85, L93, L96, L106, L397. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L513. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L15, L20, L421, L447. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L128, L131, L304, L408, L411. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L523. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L254. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L69, L71, L72, L73, L78, L82, … (25 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L30, L34, L36, L43, L82, L154, … (7 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L18, L141, L144, L278, L281, L291, … (19 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L230, L234, L236. not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L106, L108. reading (1): the panicked defence of the ANPs against the EPs as „eine Kernmechanik von TSDP“ (L106).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L20, L154, L185, L193, L197, L198, … (30 lines). not read: light pass — this document restates document 88's outline on this page and adds no line the page lacks.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.
- `residual-echos`: `Echo` (near `residualechos`). occurrence (J9, J12, J49, J69 as in record 88): a compound, a title or a folded match, no new reading.


**Record entries** (one file each; light pass):

- **`q7-what-734-names`**: Komponente 734 as a pre-conscious entity in the prologue (L15).
- **`c16-kael-origin`**: the prologue as Kael's origin — „die traumatische Geburtsstunde des Protagonistensystems Kael“ (L15).
- **`q3-how-many-kern-welten-and-alters`**: four Konstrukt-Welten; the ANP and EP groups of Chapter 7 (L106).

**One reader**: write only the pages above that carry a reading, plus the two records.
