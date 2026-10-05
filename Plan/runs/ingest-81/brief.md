# Brief — readings from document 81 (step 6)

1 document, one reader, one batch: `ingest-81`. Files go to `Plan/runs/ingest-81/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 81 | `kohaerenz-protokoll-39-kapitel-matrix` | 2026-02-25 | „the 39-chapter matrix“ (its title: `DIE 39-KAPITEL-MATRIX`) | a German plot outline of 2026-02-25, an „Operativer Bauplan der narrativen Faktoren“ (L13): 39 chapters in three parts, each a block of nine fields — Titel, Überschrift, Perspektive & Stimme, Charaktere, Ort, Fragestellung, Plot-Beat, Narrative Funktion, Sensorisches Leitmotiv — beats in the present tense; it names no source and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (494 lines for `kohaerenz-protokoll-39-kapitel`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A plan in a fixed grid.** Write „the matrix plans …“. Its chapter content goes on the chapter pages, a later batch: on a term page give at most one or two chapter beats, by chapter number — what the matrix makes of the term across chapters. Its hedges in parentheses (`oder …`) stay. Escaped arrows (`-\>`) and the logic symbol in Kap 34's title: quote around them.

## Pages — document 81, `kohaerenz-protokoll-39-kapitel-matrix`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L40, L59, L64, L100, L135, … (38 lines). central (3–4): AEGIS across the matrix — its Genesis-Log (Kap 21), the Consensus Enforcer (Kap 16), its end in Algorithmische Melancholie (Kap 35).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L83, L84, L155, L159, L195, L196, … (13 lines). central (2): what Alex does in the matrix.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Algorithmische Melancholie` alone on L437. minor (1): Kap 35, `Algorithmische Melancholie`.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L279, L280, L283. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L193, L196, L208, L392. minor (1): Kap 15, `Das Cerberus-Labyrinth`.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L467. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L187, L271, L283, L342. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L477. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L337, L377. minor (1): Kap 30, `Das Gödel-Gambit`.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L232, L389, L395. minor (1): Kap 31, `Die Auflösung der Guardians`.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L46, L48, L51, L144, L147, L148, … (14 lines). central (2–3): where the matrix places Juna — the bridge to her in Kap 38, and her first trace.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L24, L27, L35, L36, L39, … (100 lines). central (2–3): Kael's arc, from the Erwachen-Zyklus (Kap 1) to the Mosaik-Herz (Kap 39).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L229, L232. minor (1): Kap 18, `Kairos Potentialis`.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L393. minor (1–2): `Kern-Welt 1` (L25), then `KW1`–`KW4`; Kap 18 `Kairos Potentialis`.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L71, L72, L75. minor (1–2): Kiko „(intern)“ (L72) and „(EP)“ (L75) — record both.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L28. not read: title (L11) — occurrence (J9); the in-world system `Kohärenz Protokoll` (L63) is a name.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L25. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L35, L59, L60, L95, L96, L99, … (15 lines). central (2): what Lex does in the matrix.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L219, L220, L223. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L36, L96, L97, L392. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L106, L117, L120, L132, L135. minor (1): Kap 9, `Mnemosynes Archipel`.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L431, L485. minor (1): Kap 39, `Das Mosaik-Herz`.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L419. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L317, L319, L329, L345, L381, L417, … (7 lines). minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L75. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L119, L120, L123, L131, L132, L291, … (8 lines). minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L271. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L108, L155, L159. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L74. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`sektor-04`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sektor 04` alone on L25. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L353, L355, L356, L359, L367, L379. minor (1–2): Kap 28, `Die Geburt von Selene` — the integrated Kern-Selbst (L355) „oder der geheilte Host-Zustand“ (L359); record both.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L232, L242, L244, L247, L256. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L76, L160. minor (1–2): read by the census's surfaces: what the matrix plans for it — 1–3 quotations, chapter numbers in prose.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L177, L181, L185. minor (1): Kap 14, `Eintritt in die Überwelt`.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the guardians' label (J69).
- `genesis`: `Genesis-Log` (near `genesis`). reading (1) on `genesis`: Kap 21, `AEGIS' Genesis-Log`.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).
- `risse`: `Riss` (near `risse`), `Zeit-Glitch` (near `glitch`). reading, above.


**Record entries:**

- **`c7-juna-first-appearance`**: the first chapter in which the matrix lets Juna be present, and Kap 38 `Die Brücke zu Juna` — give numbers and one quotation each.
- **`c6-guardians-count-and-pairing`**: the guardians the matrix names, and Kap 31's dissolution of the Guardians.
- **`q8-aegis-after-the-vortex`**: Kap 34–35, AEGIS's protocol negated and Algorithmische Melancholie.

One reader writes all term pages and records.
