# Brief — readings from document 151 (step 6)

1 document, one reader, one batch: `ingest-151`. Files go to `Plan/runs/ingest-151/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 151 | `romanstruktur-duale-erzaehlung-und-kishotenketsu` | 2025-08-15 | „the dual structure“ (titled `Kohärenz Protokoll: Eine narrative Architektur der dualen Strukturdynamik`, L13) | a German outline of 2025-08-15 of four acts and 40 chapters: AEGIS's plot as Western conflict dramaturgy beside Kael's as Kishōtenketsu (L22), each full chapter block with perspective, AEGIS-Plot, Kael's stage and a Ki/Shō/Ten/Ketsu pass, and a table following each Anteil through the acts (L305–L311); it „entwirft“ the structure (L22) — a design, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (316 lines for `romanstruktur-duale-erzaehlung`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline that designs: write „the dual structure plans …“ and name the chapter („in Kapitel 3“); a planned chapter is not a chapter as written. Chapter readings are the session's own (ingest-151-kap) — term readings may name a chapter but write no chapter page. German — quote as written; cut before inner quotes („…“ or straight) and before reference digits glued to a word.

## Pages — document 151, `romanstruktur-duale-erzaehlung-und-kishotenketsu`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L26, L35, L41, L49, L58, … (43 lines). central (2–4): AEGIS's „Streben nach Kontrolle folgt einer westlichen Konfliktdramaturgie“ (L22); its mission, „dem tragischen Versuch eines fehlerhaften Schöpfers“ (L26); Paradoxon X, „AEGIS initiiert sein finales Protokoll“ (L204), a „logische Bombe in Kaels Psyche“ (L212); afterwards „Es kontrolliert nicht mehr; es unterstützt“ (L275); its last log entry (L284).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L76. minor (1–2): the Wächter-Konstrukte work „unter dem strikten Zero-Trust Execution Model (ZTEM)“ (L76).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L265, L309. minor (1–2): Alex in the inner council (L265) and the Anteil table (L309).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L275. minor (1–2): the end sequence (L275) — read what it says of Emergenz, else not read.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L89, L94, L100, L102, L113, L158, … (11 lines). central (2–4): Kapitel 3 is „Juna“ (L89); AEGIS classifies her as „einer externen menschlichen Person“ (L94); the planned meeting (L100) and her unexpected authentic gesture (L102); Kael's relationship to her in Act IV (L275).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L26, L27, L35, L41, L49, … (63 lines). central (2–4): Kael's „Heilungsreise auf der transformativen Kishōtenketsu-Struktur“ (L22); coherence „zwischen seinen elf Persönlichkeitsanteilen“ (L27); the host ANP (L59); the birth of co-consciousness (L231); the end state, parts still distinct (L285), „Er hat wahre Kohärenz erreicht“ (L293).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L140. minor (1–2): „Kairos, der Wächter des Potenzials“ (L140).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L58, L83, L132, L139, L185; `Kernwelten` L185. minor (1–2): Kael's „Kernwelt“ Co₁ (L58, L139) — backticks for the subscript; „die chaotische Welt McL“ (L185).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L66, L185, L212, L309. minor (1–2): Kiko the EP-Kind (Angst) (L309); in the white room (L212).
- **`kishotenketsu`** (central, 3–12 quotations): the census's surfaces — `Kishōtenketsu` L22, L35, L60, L78, L96, L134, … (12 lines). central (2–4): Kael's line on Kishōtenketsu against AEGIS's Western dramaturgy (L22); „Die Form des Romans wird so zu einem Meta-Kommentar“ (L41); the four acts Ki, Shō, Ten, Ketsu (L45, L119, L191, L245) and the Kapitel-Kishōtenketsu pass in each chapter block.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. minor (1–2): AEGIS's „Paradoxon der Fehlausgerichteten Kohärenz“ (L26) — cut before the quotes; the two coherences, imposed (L26) and negotiated (L27); the epilogue „Kohärenz“ (L279).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L65, L101, L132, L156, L158, L174, … (14 lines). central (2–4): „Lex (der rationale ANP)“ warns (L101); the Anteil table: dominant internal critic, AEGIS-strengthened tyrant (L307); his logic offered to the council (L265).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L102. minor (1–2): „einem kindlichen Anteil (Lia)“ moved by Juna's gesture (L102).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L76, L83, L84, L132, L140. minor (1–2): „Die nicht-anthropomorphen Wächter-Konstrukte wie LogOS“ (L76); LogOS in Kapitel 10 (L132).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L76, L84. minor (1–2): named with LogOS among the constructs (L76, L84), undefined.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L113, L212, L230, L275. minor (1–2): „Moros (die Verkörperung des Zusammenbruchs)“ (L230).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L113, L167, L174, L176, L177, L212, … (9 lines). minor (1–2): Nyx the EP-Kampf (L308); Kapitel 12 with focus on Nyx's co-consciousness (L167).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L101, L185, L241, L265, L309, L310. minor (1–2): „Rhys (der fürsorgliche ANP)“ longs for connection (L101); a mediator after the collapse (L241, L310).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L185, L241, L264, L311. minor (1–2): the inner council under Selene's mediation (L264); ANP-Regulator, buffer and gatekeeper (L311).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L305. minor (1–2): the table's column „Rolle (TSDP)“ (L305), undefined.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Überwelt` alone on L75. minor (1–2): Kapitel 2's perspective „AEGIS / Die Digitale Überwelt“ (L75) — the world run by the Wächter-Konstrukte (L76).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust Execution Model (ZTEM)` (near `zerotrust`), `Zero-Trust Execution Model` (near `zerotrust`). a reading — on aegis-teilfunktionen above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence: the title; the Paradoxon is read on kohaerenz above.
- `ueberwelt`: `Digitale Überwelt` (near `uberwelt`), `Digitalen Überwelt` (near `uberwelt`). a reading — on ueberwelt above.


**Record entries** (one file each):

- **`c14-aegis-first-person-chapter`**: AEGIS's perspective in Kapitel 2 (L75), 10 (L131) and 22 (L203), and a dual perspective in Kapitel 40 (L283); no grammatical person stated; dated 2025-08-15.
- **`c7-juna-first-appearance`**: Kapitel 3 „Juna“ (L89): a planned meeting with Juna, an external human person (L94, L100).
- **`q3-how-many-kern-welten-and-alters`**: „elf Persönlichkeitsanteilen“ (L27), nine named; Kael's Kernwelt Co₁ and „McL“ (L139, L185).
- **`q8-aegis-after-the-vortex`**: after Paradoxon X „Es kontrolliert nicht mehr; es unterstützt“ (L275); its last log entry (L284).

**Not promoted:** Paradoxon X, Paradoxon der Fehlausgerichteten Kohärenz (on kohaerenz), Co₁, McL, Consensus Enforcer, Ko-Bewusstsein, the act and stage labels, the Heldenreise and Heldinnenreise frames.

**Chapters:** the session writes the ten chapter readings with headings of their own (Kap 1, 2, 3, 10, 11, 12, 22, 23, 32, 40) as `ingest-151-kap`; ranges are not read.

**Two readers**, disjoint: (1) kael, juna, lex, rhys, nyx, kiko, lia, moros, selene, alex, tsdp and the records c7, q3; (2) aegis, kishotenketsu, kohaerenz, aegis-teilfunktionen, ueberwelt, logos, mnemosyne, kairos, kern-welten, emergenz and the records c14, q8.
