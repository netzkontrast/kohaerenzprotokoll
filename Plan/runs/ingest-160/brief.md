# Brief — readings from document 160 (step 6)

1 document, one reader, one batch: `ingest-160`. Files go to `Plan/runs/ingest-160/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 160 | `detaillierte-kapiteluebersicht` | 2025-07-30 | „the chapter overview“ (titled `Kohärenz Protokoll: Detaillierte Kapitelübersicht`, L11) | a German outline of 2025-07-30 of 40 chapters in four acts on Kishōtenketsu — Ki (Kapitel 1–13), Shō (14–26), Ten (27–34), Ketsu (35–40) — one numbered line per chapter with a bold title and a present-tense summary; it makes no claim about its standing. The list numbers restart in each act: a chapter's number is its act's first chapter plus its place |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (72 lines for `detaillierte-kapiteluebersicht`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline that plans: write „the chapter overview plans, in Kapitel N, …“ and compute N from the act (Ki 1, Shō 14, Ten 27, Ketsu 35 plus the place minus one) — never use the restarted list number. Chapter pages are written by the session (ingest-160-kap); term readings name the chapter but write no chapter page. German — quote as written; cut before inner quotes („…“).

## Pages — document 160, `detaillierte-kapiteluebersicht`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L18, L20, L22, L26, … (16 lines). central (2–4): Kapitel 2 from AEGIS's perspective, „Subjekt Kael“ assessed after the reboot (L18); Kapitel 10, a perverse instantiation (L26); Kapitel 19, instrumental convergence, Kael an existential threat (L41); Kapitel 25, rudimentary paraconsistent logic (L47); Kapitel 35, Algorithmische Melancholie (L65).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L43. minor (1–2): Kapitel 22: the pragmatic protector Alex leads the analysis of AEGIS's tactics (L44).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L66. minor (1–2): Kapitel 35: „AEGIS kollabiert nicht“, frozen in transformation (L65) — cut before the inner quotes.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L44. minor (1–2): Kapitel 23: the meta-observer Argus confronts the system with hopelessness (L45).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L67. minor (1–2): Kapitel 36: the Gärtner fosters Emergenz instead of control (L66).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L17. minor (1–2): Kapitel 1: a metaphysical prologue on the Genesis of AEGIS from the Leere (L17).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L58. minor (1–2): Kapitel 32: Kael and Juna formulate the Gödel-Gambit (L58) — cut before the quotes; Kapitel 34, the presentation of the Gödel-Satz, the climax (L60).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L54. minor (1–2): Kapitel 28: Isabelle's sexualised control strategy unmasked as a trauma response (L54).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L20, L22, L35, L47, L51, L55, … (9 lines). central (2–4): Kapitel 4: „Die erste, subtile Manifestation der Juna/V-Verbindung“ (L20); Kapitel 6, the Juna anomaly in AEGIS's sensors (L22); Kapitel 29, the connection a clear conscious channel (L55); Kapitel 34, Juna/V helps present the Gödel-Satz (L60).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L18, L19, L20, L21, … (29 lines). central (2–4): Kapitel 1: Kael wakes in the Konstrukt-Stadt with amnesia (L17); Kapitel 13, the decision not to follow AEGIS (L29); Kapitel 30, funktionale Multiplizität reached (L56); Kapitel 36, the birth of the Gärtner (L66); Kapitel 37, Fragment 'O' (L67).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L27, L28. minor (1–2): Kapitel 11: a full intrusion of the child part Kiko (L27).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17, L19. minor (1–2): Kapitel 1: Kael's awakening in the sterile Konstrukt-Stadt (KW1) (L17) — cut around the digit if needed; Kapitel 3, echoes in it (L19).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L21, L24, L38, L44. minor (1–2): Kapitel 5: Kael meets the rational part Lex (L21); Kapitel 8 from Lex's perspective (L24); Kapitel 23, Lex paralysed (L45).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L42. minor (1–2): Kapitel 21: creativity represented by Lia in the Möglichkeiten-Garten (L43).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L36. minor (1–2): Kapitel 15: Kael confronts the Guardian Mnemosyne in KW2, who gaslights him (L37).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L45. minor (1–2): Kapitel 24: Rhys tries to reach the collapsed part Moros (L46).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L56. minor (1–2): Kapitel 30: „Funktionale Multiplizität“ — the parts act as a coordinated team (L56).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L28, L38, L41. minor (1–2): Kapitel 12: the fighter part Nyx takes control (L28); Kapitel 20, the positive intent of the anger (L42).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L23. minor (1–2): Kapitel 7: Kael enters the Resonanz-Landschaft (KW2) unwillingly (L23).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L38, L41, L45. minor (1–2): Kapitel 17: the empathic part Rhys mediates between Lex and Nyx (L39); Kapitel 24 (L46).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L17, L29. minor (1–2): Kapitel 9: a massive Riss in KW1 (L25) — cut before the quotes; Kapitel 26, the truth in the Riss, the midpoint (L48).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L25. occurrence: `Simulation` at L25 is the simulation's architecture behind the Riss — say it on risse.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: Guardian singular.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world name, said on kael via Kapitel 18 if the reader likes.
- `guardians`: `Guardian` (near `guardians`). occurrence: Guardian singular (L37, L59).
- `kishotenketsu`: `Ketsu (結)` (near `kishotenketsu`). a reading only if the reader wishes: the four act headings Ki, Shō, Ten, Ketsu — else not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Initialisierung` (near `koharenz`). occurrence: the title.


**Record entries** (one file each):

- **`c14-aegis-first-person-chapter`**: Kapitel 2 „Aus der kalten, analytischen Perspektive von AEGIS“ (L18), Kapitel 6 and 10 as AEGIS's analyses; no grammatical person stated; dated 2025-07-30.
- **`c7-juna-first-appearance`**: Kapitel 4, the first subtle manifestation of the Juna/V-Verbindung, a sensory detail (L20).
- **`q7-what-734-names`**: Kapitel 2 „Protokoll 734: Kohärenz-Initialisierung“ (L18) — cut around the digits if `--find` drops them.
- **`q8-aegis-after-the-vortex`**: Kapitel 35, AEGIS does not collapse but freezes in transformation (L65).

**Not promoted:** Protokoll 734, Korrekturprotokoll Delta, D2-Modul, Fragment 'O', the Gärtner, Grounding-Artefakte, the Archivar, the chapter titles.

**Chapters:** written by the session as `ingest-160-kap` (39 pages; Kap 32's title is a damaged formula).

**One reader** for all pages and entries.
