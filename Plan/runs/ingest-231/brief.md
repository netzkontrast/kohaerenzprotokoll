# Brief — readings from document 231 (step 6)

1 document, one reader, one batch: `ingest-231`. Files go to `Plan/runs/ingest-231/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 231 | `kohaerenz-protokoll-comprehensive-project-state-narrative-au` | 2026-03-26 | „the project-state audit“ (an unsigned English audit) | an English audit in five parts — „HARD CANON“ pillars (each citing another text), a Version A / Version B contradictions table with recommendations, narrative gaps, an inventory of fragments marked READY or NEEDS REVISION, and a roadmap; its „HARD CANON“ is its own label, its recommendations decide nothing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (77 lines for `kohaerenz-protokoll-comprehens`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An audit: its pillars report other texts („Source: Plot-Exploration“, „Source: Existenzforschung“) — write „the project-state audit reports, citing …“; its Version A / B rows are positions it sets side by side, its recommendations are recommendations („the audit recommends …“), never applied. Its „HARD CANON“ is its own label. The contradictions table is one long line (L30) — `--find` a short phrase in it. Bold digits (`11`, `13`) are dropped — quote around them.

## Pages — document 231, `kohaerenz-protokoll-comprehensive-project-state-narrative-au`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L18, L19, L21, L23, L30, L36, … (7 lines). minor (1–3): AEGIS as „a sophisticated, autopoietic system“ dedicated to control and closure, reported citing Plot-Exploration (L19); framed as the environment itself (L20); the AEGIS endpoint set out as Version A, total implosion, against Version B, the „Big Bounce“ (L30), and the recommendation for B (L36).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L30. minor (1–3): the alter count set out as two versions, 11 or 13 (L30), with the recommendation to standardize at 11 (L35, L73) — quote around the bold digits.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L63, L65. occurrence: `Cerberus` stands in `KW3-Cerberus`, a world label, and „Cerberus’s barriers“ at the Grenzfeste (L65); read on grenzfeste.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel Gambit` L15, L21, L30. minor (1–3): the Gödel Gambit as „The chosen narrative engine“, the Kael–Juna connection as the „unprovable truth“, reported citing Plot-Exploration (L21).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L65. minor (1–3): „Übergangsschleuse (Grenzfeste)“: „Cerberus’s barriers“ in KW3, marked READY (L65).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L21, L30, L34, L44, L61. minor (1–3): Juna's ontology set out as Version A, „An "Anomaly"“ — quote around the inner quotes — against Version B, „Relational Essence“ (L30); the recommendation for B, Juna as the „true but unprovable“ sentence (L34); a place of a specific Juna memory in KW2 (L61).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L17, L18, L21, L36, L42, L44, … (8 lines). minor (1–3): Kael's origin „traced directly to the Coherence Island“, reported citing Plot-Exploration (L17); Kael as an anomaly AEGIS cannot delete without its own collapse (L18); his origin trauma, the „Betrayal“, named as undefined, the „Zero-Bit“ of his fragmentation (L42).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L25, L30, L43, L75. minor (1–3): the Coherence Protocol as „the literal operating system of the Kernwelten“, reported citing Existenzforschung (L25); trigger objects bridging Kernwelten as sensory anchors (L43, L75).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L30, L73. minor (1–3): Silas and Oblivion as the primary names against a Silas/Rhys overlap (L30); the roadmap confirming „the retention of Silas and Oblivion“ (L73).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L30. minor (1–3): „Silas vs. Rhys overlap“ as the naming problem of Version A (L30).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L25, L26, L28, L76; `Glitch` L26. minor (1–3): the Coherence Protocol suppressing „Risse“ (entropy) in the simulation, reported citing Existenzforschung (L25); every Glitch or Riss as a narrative event of reality's code failing (L26); the first Riss at Datenknotenpunkt Gamma-7 (L54).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L30, L73. minor (1–3): Silas and Oblivion as primary, against a Silas/Rhys overlap (L30); the retention of Silas and Oblivion (L73).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L76. occurrence: `Simulation` names the novel itself in the roadmap's close (L76).
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — `Vergessener Schrein` L60. minor (1–3): „Vergessener Schrein“, the site of the Kern-Trauma-Lokus in KW2, marked NEEDS REVISION until the Betrayal is defined (L60).

- **`kaels-wohneinheit`** (minor, 1): „Kaels Initiale Wohneinheit“, the minimalist starting point in KW1, marked READY (L52).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kairos`: `KW4-Kairos` (near `kairos`). occurrence: `KW4-Kairos` is a world label (L63, L66); its bearing on the pairing goes to Q5.
- `logos`: `KW1-LogOS` (near `logos`). occurrence: `KW1-LogOS` is a world label (L50, L52–L55); its bearing on the pairing goes to Q5.
- `mnemosyne`: `KW2-Mnemosyne` (near `mnemosyne`). occurrence: `KW2-Mnemosyne` is a world label (L57–L61); its bearing on the pairing goes to Q5.


**Record entries** (one file each):

- **`c16-kael-origin`**: Kael's origin traced to the Coherence Island, reported citing Plot-Exploration (L17).
- **`q3-how-many-kern-welten-and-alters`**: 11 or 13 alters set side by side, the recommendation for 11 as aligning „with the 4 Kernwelten“ (L30, L35, L73).
- **`q8-aegis-after-the-vortex`**: AEGIS's endpoint as implosion (Version A) or „Big Bounce“, evolution into a new logic (Version B), with the recommendation for B (L30, L36).
- **`q5-guardians-and-kern-welten`**: the worlds labelled with Guardian names — KW1-LogOS, KW2-Mnemosyne, KW3-Cerberus, KW4-Kairos (L50, L57, L63).

**Not promoted:** Coherence Island, Potential Sea, Monster Group, Big Bounce, Betrayal, Zero-Bit, Transfer Protocol, the fragment places, READY / NEEDS REVISION.

**One reader**: kael, juna, aegis, alters, goedel-gambit, grenzfeste, kern-welten, oblivion, rhys, silas, risse, vergessener-schrein, kaels-wohneinheit and the records c16, q3, q8, q5.

**Chapter readings**: none — the audit names acts and locations, not chapters.
