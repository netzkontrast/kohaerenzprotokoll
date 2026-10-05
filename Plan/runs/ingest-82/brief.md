# Brief — readings from document 82 (step 6)

1 document, one reader, one batch: `ingest-82`. Files go to `Plan/runs/ingest-82/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 82 | `romanprojekt-kohaerenz-protokoll-leitfragen` | 2026-02-26 | „the research report“ (its parts: plot, `MAP-Synthese`, `Leitfragen`, `Kohärenz-Check`) | a German research report of 2026-02-26 in an assistant's first person: a provisional plot in three acts (L23–L29), a four-axis synthesis with a table of the Kernwelten and the Externe Ebene (L31–L60), ten guiding questions for the chapters it finds unoutlined (L62–L104), a consistency check with correction proposals (L106–L130), a question back to the author (L132–L136); reference 7 pastes another text (L146–L154) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (155 lines for `romanprojekt-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A report that asks more than it decides.** Write „the research report gives / proposes / asks …“. Its `Leitfragen` are questions with a scene logic: quote the scene logic as what it proposes, never as the plot. Its `Korrektur-Vorschlag` lines are proposals. Its claim that the DKT is the valid in-world metaphysics (L126) is its own; record, don't apply. **Reference 7's pasted English text (L146–L154) is another document's**: never read onto a page from it. Glued reference digits after a word: cut before them. The empty `Wertvollste Quellen:` fields name nothing.

## Pages — document 82, `romanprojekt-kohaerenz-protokoll-leitfragen`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L27, L28, L29, L33, L41, … (18 lines). central (3): not a malicious antagonist but a tragic autopoietic system suffering from operational closure (L41); its genesis in a traumatic origin event, the „Genesis-Krise“ (L41); its probabilistic manipulations in Teil I (L27).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L54. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L27, L28, L84, L92, L130. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L54. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L126. minor (1): the DKT (K1 vs. K0) as „die gültige, in-world wahre Metaphysik“ (L126), against the Λ-Canon as pseudoscientific — the report's claim.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L29. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L92. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L56, L96. central (2): the table's `Externe Ebene` row — „Köln, Februar 2026“, chaotic, escaping AEGIS's control, the real world (L56); Leitfrage 8, Kael breaking the rendering limits and waking in Köln (L96).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L29, L60, L90, L118. minor (1–2): Teil III culminating in the Gödel-Gambit (L29); Leitfrage 7, Kap 33 (L92); the warning about over-abstraction (L118).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L27, L28, L29, L41, L76, L78, … (10 lines). central (2–3): Juna/V as the personified correspondence-truth principle AEGIS had to split off in the Genesis-Krise (L80); the Moonshine-Link based on entanglement and Gnosis (L76).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L27, L28, L29, L33, L41, … (20 lines). central (2–3): Kael waking after a Universal Reboot (L27); from passive victim to active investigator (L28); the Gödel-Gambit (L29); waking in Köln (L96).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L55, L100. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L51, L80. central (2): the table — KW1 LogOS, KW2 Mnemosyne, KW3 Cerberus, KW4 Kairos/Sophia, each with its TSDP part (L52–L55).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L37, L53, L88, L122. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L21. not read: title — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L27, L68, L72. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L28, L37, L52, L72, L84. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L55. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L52, L68, L80. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L27, L53, L80, L88. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L28, L74, L76. minor (1): Leitfrage 3, Kap 19 (L76).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L88. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L17, L29, L88, L110. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L28. minor (1): Kael ascending into the Nexus „(die Überwelt)“ in Teil II (L28).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L28, L37, L53, L54, L72, L84, … (7 lines). minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L96. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L29, L104. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L53, L88. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L72, L100, L154. minor (1): Leitfrage 2, the Cache-Inkohärenz as Riss (L70–L72).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L37, L55, L88, L110, L114. minor (1): Selene (Integrator) in KW4 (L55); the check's proposal for her task (L114).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L55, L110, L114. minor (1–2): the consistency check — Sophia striving for integration by eliminating differences, against Selene (L110); the proposal to read it as AEGIS's corruption (L114).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L41. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L28, L37, L51, L72, L126. minor (1–2): read by the census's surfaces: what the report gives for it — 1–3 quotations.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L28. minor (1): L28, the Nexus as the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). reading (1) on `genesis`: AEGIS's Genesis-Krise (L41, L80).
- `kohaerenz`: `Cache-Inkohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Check` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence (J12).


**Record entries:**

- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene as Köln, Februar 2026, the real world (L56), and Kael waking there in Kap 27/35 (L94–L96) — the report's position, decided nothing.
- **`q6-nexus-ueberraum-ueberwelt`**: the Nexus as the Überwelt (L28).
- **`q5-guardians-and-kern-welten`**: the table's pairing (L52–L55).

One reader writes everything.
