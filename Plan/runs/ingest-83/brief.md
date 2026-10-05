# Brief — readings from document 83 (step 6)

1 document, one reader, one batch: `ingest-83`. Files go to `Plan/runs/ingest-83/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 83 | `romanprojekt-analyse-kohaerenz-protokoll` | 2026-03-31 | „the contradiction report and idea registry“ | a German export of 2026-03-31 holding two generated reports: a `Contradiction Report` (L11–L51) with conflicts C-001 to C-008, each setting a quotation from „Doc NN“ against another, and a source index; and an `Idea Registry` (L55–L123) with 27 concepts in five tables (Figuren, Weltbau, Physik / DKT, Themen, Struktur), each with sources, a star rating and a core statement, and four open questions „vom Archivist identifiziert“ |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (124 lines for `romanprojekt-analyse-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A report about other documents, which it names only by number.** Two voices: (1) the `Quelle A` / `Quelle B` cells quote other texts — write „the report quotes Doc NN as …“, never as the report's claim, and never as the named document's (we cannot tell which landed document Doc NN is); (2) the `Kern-Konflikt` column and the registry's `Kernaussage` column are the report's own summary — write „the registry sums up …“. The star ratings are its weighting. Its open questions are questions. Quote prose cells; cut before inner „…“ or "…".

## Pages — document 83, `romanprojekt-analyse-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L32, L33, L67, L70, L82, … (15 lines). central (2–3): F-02, an autopoietic AI suffering from misaligned coherence (L67); C-005, AEGIS's fate — the two quoted hypotheses and the report's Kern-Konflikt (L32); T-03 the paradox of control (L104).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L82. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L69. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L32, L93. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L23. minor (2): F-04, `Die 10 Kern-Alters` and its list (L69); F-06, decanonised alters — Silas, Oblivion, Eos, Nox, Praetor — as narrative redundancies (L71); C-002, 11 against 13+ (L23); record the 10 against the „11er-Kanon“.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L24, L69. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L70, L80. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`dkt`** (minor, 1–4): the census's surfaces — `Dual-Kernel-Theorie (DKT)` L91; `DKT` L49, L86, L91, L121. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L84. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Externe Ebene` alone on L83. minor (1): W-06, `Externe Ebene (Köln)`, the base reality where Kael lives with KPTBS, ADHS and DIS, cared for by Juna (L83); open question 3 (L122).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L33, L93. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L70, L82, L116. minor (1–2): F-05, LogOS, Mnemosyne, Cerberus, Kairos and Sophia over the 4 Kernwelten (L70); S-04, the Wächter-Zwiespalt (L116).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L69. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L22, L41, L68, L83, L94, L115, … (7 lines); `Julia` L41, L122. minor (2): F-03, a transcendent anomaly and/or Kael's exiled origin self (L68); C-001's Kern-Konflikt, Juna paradoxical (L22); C-008, the names Juna, V, Julia (L41).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L25, L33, L66, L68, L69, … (15 lines). central (2–3): F-01, the host of a dissociated identity in amnesia (L66); C-004, Kael's origin trauma left unclear (L25); open question 1, his real trauma in Köln (L120).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L70. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L70. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L69, L121. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: title — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Konstrukt-Stadt` alone on L78. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L69, L123. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L69, L121, L123. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L70, L78. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L70, L79. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Möglichkeits-Garten` alone on L81. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L68, L94, L115. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L69. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L105. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L82. minor (1): W-05 (L82).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts-Rauschen` L84. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L69, L121. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L71. minor (1): F-06, among the decanonised alters (L71).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L84. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L33. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Resonanz-Landschaft` alone on L79. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L24, L34, L69, L123. minor (1): C-007, the role of Rhys (L34).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L92. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L69, L81. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L23, L24, L71. minor (1–2): C-003, the identity of Silas — the two quoted positions and the Kern-Konflikt (L24); F-06 (L71).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L70. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L25, L49, L66. minor (1): read by the census's surfaces: what the registry's `Kernaussage` or the report's `Kern-Konflikt` says of it — 1–2 quotations.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L82. minor (1): W-05, `Die Überwelt (Nexus)`, the guardians' meta-cognitive data level (L82).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust Execution Model` (near `zerotrust`). occurrence (J12): the Zero-Trust Execution Model is W-05's basis, read on ueberwelt.
- `alters`: `Die 10 Kern-Alters` (near `alters`), `Dekanonisierte Alters` (near `alters`). reading, above.
- `externe-ebene`: `Externe Ebene (Köln)` (near `externeebene`). reading, above.
- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis-Event` (near `genesis`). reading (1) on `genesis`: open question 1, the Genesis-Event of Kael (L120).
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). occurrence (J24): `Kaels` is a genitive.
- `kohaerenz`: `Fehlausgerichteter Kohärenz` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`). occurrence (J12).
- `konstrukt-stadt`: `Konstrukt-Stadt (KW1)` (near `konstruktstadt`). reading (1): W-01 (L78).
- `moeglichkeits-garten`: `Möglichkeits-Garten (KW4)` (near `moglichkeitsgarten`). reading (1): W-04 (L81).
- `resonanz-landschaft`: `Resonanz-Landschaft (KW2)` (near `resonanzlandschaft`). reading (1): W-02 (L79).
- `risse`: `Landauer-Prinzip / Risse` (near `risse`). reading (1): P-02, `Landauer-Prinzip / Risse` (L92).


**Record entries** (each from the report's own columns; the quoted Doc NN cells as quotations of unnamed sources):

- **`c16-kael-origin`**: C-001, Juna's nature — Doc 33's „exiled part of Kael's own Ursprungs-Ich“ against Doc 36's catalyst outside the system (L22).
- **`q3-how-many-kern-welten-and-alters`**: C-002 (L23), F-04's ten (L69), the „11er-Kanon“ (L71), F-05's 4 Kernwelten (L70).
- **`q8-aegis-after-the-vortex`**: C-005 (L32).
- **`c13-externe-ebene-beyond-the-simulation`**: W-06 (L83); C-006, the climax strategies — transcendence and flight against confrontation (L33).
- **`c6-guardians-count-and-pairing`**: F-05, five guardians over four worlds (L70).
- **`q6-nexus-ueberraum-ueberwelt`**: W-05 (L82).
- **`c11-landauer-warmth-or-cold-ozone`**: P-02, information erasure generating waste heat that burns Risse (L92).

One reader writes everything.
