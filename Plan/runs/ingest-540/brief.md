# Brief — readings from document 540 (step 6)

1 document, one reader, one batch: `ingest-540`. Files go to `Plan/runs/ingest-540/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 540 | `romanentwurf-ruf-des-abenteuers` | 2025-04-18 | „the chapter-2 draft“ | a narrative draft for „Teil 1, Kapitel 2 (Ruf des Abenteuers)“ of an earlier outline (L11): context, craft research, twenty scene blocks, a prose sketch and conclusions; the protagonist and the partner appear only under earlier names; it also holds craft research on a real diagnosis (not harvested) and is themed by an album song (not harvested)|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (483 lines for `romanentwurf-ruf-des-abenteuer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A draft of an earlier outline: write „the chapter-2 draft proposes …“; never canon. Read only the settings and their Guardians. **Never cite these lines: 15,16,22,23,34,35,36,45,47,48,53,66,67,71,73,74,75,84,85,88,98,99,107,112,113,114,115,116,126,127,139,140,141,144,154,155,167,168,169,181,182,196,197,199,210,211,224,225,228,233,238,239,240,241,242,243,251,252,253,256,266,267,270,279,280,281,282,284,294,295,308,309,322,323,326,335,336,337,340,349,350,351,354,365,367,369,393,397,403,405,417,437,441,443,445.** Never cite L17 (the song and a personal theme) or any line of the craft research on a diagnosis; never cite L447–L482 (references). Never put Kael's or Juna's name on what the draft says of its protagonist or partner.

## Pages — document 540, `romanentwurf-ruf-des-abenteuers`

- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L74. not read: on a barred line, in the craft research (L74).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L74. not read: on a barred line, in the craft research (L74).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L443. not read: on a barred line (L443).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L15. not read: the partner appears only under an earlier name.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L15. not read: the protagonist appears only under an earlier name; the draft does not make the identity plain.
- **`kern-welten`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kern-Welt` alone on L27. minor: „Kern-Welt 2 – Die Resonanz-Landschaft“ as the chapter's setting (L27).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title (L11) (J9).
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L15, L22, L31, L35, L46, L53, … (17 lines). minor: the logic of the Konstrukt-Stadt as fundamental contrast (L31); the comparison table: logic, order, efficiency, linear physics, suppressed emotion, LogOS (L58–L64); the landscape „fundamental *falsch* nach den Gesetzen der Konstrukt-Stadt“ (L87).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L64. minor: the Konstrukt-Stadt's Guardian „LogOS (Logik, Ordnung)“ in the table (L64).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L36, L64. minor: the Resonanz-Landschaft's Guardian „Mnemosyne (Erinnerung, Emotion)“ in the table (L64).
- **`resonanz-landschaft`** (central, 3–12 quotations): the census's surfaces — `Resonanz-Landschaft` L22, L23, L27, L46, L53, L58, … (18 lines). minor: Kern-Welt 2 (L27); a reality shaped by emotions and memories, a store of the unconscious (L31); non-linear, associative physics (L32); dreamlike, foggy, aquatic aesthetics (L33); the emotional counterpole of the Konstrukt-Stadt (L46); the comparison table (L58–L65).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L35, L443; `Glitches` L15, L35. not read: `Risse` and `Glitches` stand only on barred lines; the table's „Glitch-Manifestation“ row (L65) is read on resonanz-landschaft.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L22. not read: on a barred line (L22).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kern-welten`: `Kern-Welt 2` (near `kernwelt`). a reading: `Kern-Welt 2` — read on kern-welten above.
- `mnemosyne-server-architektur`: `Mnemosynes` (near `mnemosyneserverarchitektur`), `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Architekt` and `Mnemosynes`, read on mnemosyne where safe.


**Chapter readings:** none — the chapter is Kapitel 2 of an earlier outline, and every line about its action names the protagonist or the partner by an earlier name.

**Record entries:** none.

**Not promoted:** Kern-Trauma, Betrayal, Stimme in der Leere, Kind/Echo, Host, Meta-Ebene, Zeitschleife, Ruf des Abenteuers, the craft lenses.

**One reader**: every page above.
