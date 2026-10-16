# Brief — readings from document 440 (step 6)

1 document, one reader, one batch: `ingest-441`. Files go to `Plan/runs/ingest-441/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 440 | `tsdp-analyse-kaels-innere-welt` | 2025-04-28 | „the TSDP analysis of Kael's inner world“ (an unsigned German report, „TSDP-Basierte Analyse der Spannungspunkte und Charakterprofile für Kaels Anteile“) | reads Kael's five named parts through structural dissociation as hypotheses, with tension points per part against the four Kernwelten, the system, the other parts and AEGIS/Juna/V/Paradoxon X, profiles and narrative advice; calls itself a grounded basis (L404), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (471 lines for `tsdp-analyse-kaels-innere-welt`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Hypotheses about a figure of the novel: write „the TSDP analysis hypothesises …“ — fiction about Kael, never anyone's real condition; its role assignments are „Hypothesen“ (L56, L66) hedged with „wahrscheinlich“, „möglicherweise“, and its quoted first-person sentences are beliefs it attributes to the parts. Its theory sections (L34–L52) report cited research. The four worlds are named by code with a gloss (L87–L90); never write the second world's expansion — call it „the second world“. Quote the German as written; cut before straight quotes, bold markers, escaped table markup and glued footnote digits. No gendered pronoun for Kael, Juna, AEGIS or any part — use the names (quotations stay verbatim). Never write a real person's name.

## Pages — document 440, `tsdp-analyse-kaels-innere-welt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L47, L60, L62, L110, L114, L118, … (25 lines). minor (1–4): AEGIS's control mechanisms could exploit or strengthen the parts' phobies to keep the fragmentation (L47); suppression „durch ANPs oder AEGIS“ (L60); each part's tension points with AEGIS, Juna/V and Paradoxon X (L114).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L467. not read: an occurrence — a reference-list title (L467).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L398, L421. minor (1–4): advice: use the „Cache Kohärenz“-problem for plot complications — an ability unavailable because the wrong part is in front, amnesia, contradictions (L421 — quote around the straight quotes).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L467. not read: an occurrence — a reference-list title (L467).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L47. minor (1–4): the connection to Juna/V possibly challenges phobias of attachment and intimacy (L47); each part's interaction with Juna/V (L114).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L17, L19, L21, L23, L30, … (30 lines). central (4–8): Kael's inner landscape understood as structural dissociation, five named, distinct parts (L23); the analysis reads Kael's „Personas“ as dissociated parts (L19 — quote around the nested quote); the conflicts between the ANPs block inner coherence (L398); the „Cache Kohärenz“ problem as plot complication (L421).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L79, L83, L124, L165, L206, L247, … (10 lines). minor (1–4): the four worlds by code and gloss as the setting of each part's tension points (L87–L90 — the second world described, never expanded).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L17, L23, L30, L38, L58, L59, … (44 lines). minor (1–4): the table: Kiko an EP holding trauma affects — fear, grief, pain — and attachment need, with a phobia of abandonment (L72).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L87. minor (1–4): the first world „(Konstrukt-Stadt)“: clear rules and rational order could strengthen Lex's ANP function, tension when unpredictability intrudes (L87).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L17, L23, L30, L37, L52, L58, … (44 lines). minor (1–4): the table: Lex an ANP — rationality, logic, control — with a phobia of the EPs Kiko and Nyx (L71); Lex in the logical world: needs for logic and structure find resonance (L87); in the chaotic fourth world Lex is most vulnerable (L90).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L17, L23, L30, L38, L51, L58, … (48 lines). minor (1–4): the table: Nyx an EP holding anger and aggression, defence by fight, with a phobia of re-traumatisation and of control (L73).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L19. minor (1–4): the analysis reads Kael's inner „Personas“ as manifestations of dissociated parts (L19).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L17, L23, L30, L37, L51, L52, … (39 lines). minor (1–4): the table: Rhys an ANP of social harmony and empathy, with a phobia of conflict and of EP intrusions, especially Nyx (L74).
- **`selene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Selene` alone on L94. minor (1–4): „Wächterin/Selene“ within the self and the whole system Kael (L94).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L11, L17, L19, L21, L25, L32, … (27 lines). central (4–8): TSDP applied to Kael's system as stated in research (L19); principles relevant for Kael (L34); provisional classification as hypotheses (L56); the table of roles, functions and core phobias (L66, L70–L75); the parts' phobias producing an inner stalemate (L47).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `selene`: `Wächterin/Selene` (near `selene`). `Wächterin/Selene` read on selene.


**Record entries:** none.

**Not promoted:** Kai (no page exists), ANP, EP, Aktionssysteme, Kernphobien, Schlüsselphobien, Attachment Cry, Bindungsruf, Paradoxon X, Juna/V, the world glosses, Kernwelt-Regeln, and the borrowed concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
