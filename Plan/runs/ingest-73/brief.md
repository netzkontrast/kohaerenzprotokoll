# Brief — readings from document 73 (step 6)

1 document, one reader, one batch: `ingest-73`. Files go to `Plan/runs/ingest-73/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 73 | `romanprojekt-kohaerenz-protokoll-analyse` | 2026-04-30 | „the Synthese-Report“ | a German synthesis report in four parts — Konsens, Widersprüche (a four-column table: pre-reset claim, Struktur-Kanon claim, verdict), Lücken, Synthese und Operationalisierung (directives for the encoding phase); it calls the Struktur-Kanon of 2026-04-30 the „unwiderrufliche Fundament“ (L15) and decides its table „Kanon gewinnt“ |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (144 lines for `romanprojekt-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A report with three voices.** Part 1 states what it calls secured by the Struktur-Kanon (L15) — write „the Synthese-Report states as consensus …“. **The table (L45–L54) has three voices in one row:** column 2 is pre-reset material („Behauptung Projektwissen (Prä-Reset PDFs)“), column 3 the Struktur-Kanon as the report renders it, column 4 its own verdict; say which column a statement stands in, and never attribute column 2 to the report. Parts 3–4 are the report's own gaps and directives (`Lösung zu C.4`, `F3`): write „the report proposes / directs …“. Its claim to canon (L15) and its verdict `Kanon gewinnt`: record once on `aegis`, never apply. Empty reference marks (backticks) and escaped asterisks: quote prose, not table cells, where possible; cut a quotation before an empty reference mark.

## Pages — document 73, `romanprojekt-kohaerenz-protokoll-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L21, L23, L27, L31, L39, … (23 lines). central (4–6): not an intentional antagonist but an operationally closed autopoietic system (L23); the table's kernel identity row — believes K1, operates as K0 (L48, column 3); the Vortex beats, AEGIS „löscht sich nicht“ and keeps a world built on a faulty axiom (L85); the canon claim once (L15).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `SIS` L83, L113. minor (1–2): SIS, Secure Isolation State, the cognitive firewall that crashes in the heat spike (L83, L113); RIVE and ZTEM as the other two protocols (L112, L114).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L53, L69, L85. minor (1–2): the table's end state, column 3 (L53); the recommendation, Option 1 as permanent state (L69); the Vortex's fifth beat (L85).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L82. minor (1–2): thirteen TSDP alters against the Bekenstein bound (L65); the 13-alter syntax grid (L121, L125–L128).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L50, L104. minor (1): the table's five Wächter as pre-reset material (L50, column 2); „Cerberus subsumiert“ into LogOS's pole (L104).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L89. minor (1): Juna as „die Chaitin-Konstante des Romans“ (L89).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L31, L48, L54, L121. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L31. minor (1–2): „keine Metapher, sondern diegetisches Naturgesetz“ (L31); the table's row on the role of DKT concepts (L54).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L23. minor (1): AEGIS's control acts producing the entropy (L23, L48).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L39. minor (1–2): the Genesis-Symmetrie, three beats (L37–L39); the revelation through overload, C.4 (L70, L83).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L25, L27, L39, L48, L49, L51, … (13 lines). central (4–6): IC in both storyforms simultaneously, Witness-Funktion and Gödel-Satz (L27); the table, Juna as the unmodellable rest of the separation, not part of Kael (L49, column 3); „Juna ist die Chaitin-Konstante des Romans“ (L89); the Telefonstille as anchor mode (L91); her one appearance in Kap 33/34, written by exclusion (L93). Record that L27 says she never intervenes physically and L93 has her enter the room; decide nothing.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L27, L31, L39, L49, L52, … (21 lines). central (3–5): the Genesis three beats, Kael becoming Komponente 734 (L39); the pivot — Kael's decision to accept the heat (L84); Oblivion as AEGIS's echo in Kael (L128); the Ouroboros pronouns, a single amnesic „Ich“ in Kap 1 (L138).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L50. not read: one of the five Wächter in the pre-reset column (L50) — column 2, the report's report of older material; one line only if the reader judges it adds: `occurrence`.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L127. minor (1): the syntax grid — Freeze, microscopic perception, the square centimetre of floor (L127).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: title (L11) — occurrence (J9).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L39, L49. minor (1): Beat 3 of the Genesis (L39); the table's genesis row, Kael became Komponente 734 (L49, column 3).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L31, L65, L71, L112. minor (1–2): threatening to collapse into a solipsistic vacuum chamber without other entities (C.3, L71); the Nichts-Rauschen at its edges (L112).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L125. minor (1): the syntax grid — rationalist, hypotactic cold cascades (L125).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L50, L91, L93, L104. minor (1–2): the erasing pole, Cerberus subsumed, the K0 executive (L104); the LogOS scanners in Juna's appearance (L93).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L50, L81, L85, L103, L143. minor (2–3): the Mnemosyne-Archipel as AEGIS's physical storage substrate, the K1 cache banks (L81); the storage pole, static, cold (L103); the archipel brought to thermodynamic equilibrium (L85).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L49. minor (1): only if L49 names it as the report's own; otherwise not read: column 3.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L82. minor (1): Kael having reached funktionale Multiplizität, 13 alters, in the heat spike (L82).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nichts-Rauschen` alone on L112. minor (1): RIVE's phenomenology, the constant quiet Nichts-Rauschen at the city's edges (L112).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L126. minor (1): the syntax grid — Fight, asyndetic series (L126).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L128, L143. minor (1–2): „Das AEGIS-Echo“, the system's Trojan in Kael, waking when AEGIS undergoes the Truth-Rotation in Kap 36 (L128); and L143 if it names Oblivion otherwise — record both if they differ.
- **`ouroboros-struktur`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Ouroboros-Struktur` alone on L53. minor (1–2): the Ouroboros-Leitmotiv — the ozone smell in Kap 1, cold and sterile, and in Kap 39, hot from friction (L134–L139).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Potentialmeer` alone on L83. minor (1) or not read: only if L83 names it in the report's own words.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L52. minor (1): the table's driver-pivot row, pre-reset — Kael's conflict triggering external Glitches (L52, column 2): say it is column 2; or ZTEM generating heat and Glitches (L114).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L93. minor (1): the alters' somatic relaxation in Juna's one appearance, „z.B. Selene“ (L93).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L50. not read: one of the five pre-reset Wächter (L50, column 2) — occurrence.
- **`telefon-stille`** (minor, 1–4): the census's surfaces — `Telefonstille` L62, L91. minor (1–2): „Der Anker-Modus: Die Telefonstille.“ (L91) — the silence as pure Mutual Information without a carrier; and L62 if it names it.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L39, L70, L83. minor (1–2): Beat 2, AEGIS misreading qualia as noise (L39); the original Trennungsprotokoll pouring out as unstructured data when the firewall collapses (L83).
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L69, L85, L128. minor (1–2): after the Truth-Rotation in Kap 36 the system's worldview collapses (L69); the system recognising its K0 nature (L85).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L39, L49, L65, L83, L113. minor (1): 13 complex TSDP alters against the Bekenstein bound (L65).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L53. not read: `Simulation` (L53) is the table's pre-reset column — occurrence.
- **`vortex`** (minor, 1–4): the census's surfaces — `Vortex` L52, L69, L77, L143. central (3): the Vortex's narratological mechanics, Kap 35–36 (L77–L85) — five steps, the pivot as a strictly physical event (L79); the table's driver-pivot row (L52, column 3).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Symmetrie` (near `genesis`). reading, above (`Genesis-Symmetrie` is the heading, L37).
- `kohaerenz`: `Kohärenz Protokolls` (near `koharenz`), `K1-Kohärenzwächter` (near `koharenz`). occurrence (J9, J12).
- `ouroboros-struktur`: `Ouroboros` (near `ouroborosstruktur`). reading, above.


**Record entries** (one file each, page = the record's file stem):

- **`c11-landauer-warmth-or-cold-ozone`**: the report's Ouroboros image — ozone in Kap 1 as K1 perfection, cold, atoms cooled to zero point; in Kap 39 the same smell from the hot friction of atoms (L138–L139); Juna's trace is cold, AEGIS's heat (L92). Central to the record; decide nothing.
- **`c6-guardians-count-and-pairing`**: „Es existieren exakt zwei Pole.“ (L99), Mnemosyne and LogOS with Cerberus subsumed (L103–L104); the five pre-reset Wächter in column 2 (L50).
- **`c7-juna-first-appearance`**: her only appearance, Kap 33/34, as „Lösung zu C.7“ (L93).
- **`c16-kael-origin`**: the table's genesis row — pre-reset, Juna an exiled part of Kael's Ursprungs-Ich (column 2); Struktur-Kanon as rendered, Kael and AEGIS separated, Juna the unmodellable rest, not part of Kael (column 3) (L49).
- **`q8-aegis-after-the-vortex`**: AEGIS does not delete itself, manages a world it knows rests on a faulty axiom (L85); the recommendation of Option 1 (L69).
- **`c12-genesis-beats`**: „einer strikten Drei-Beat-Struktur“ (L39).

One reader writes everything.
