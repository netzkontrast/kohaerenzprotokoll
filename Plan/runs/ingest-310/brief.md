# Brief — readings from document 309 (step 6)

1 document, one reader, one batch: `ingest-310`. Files go to `Plan/runs/ingest-310/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 309 | `angereichertes-plotkonzept-kapitelthemen-detailliert-kohaere` | 2025-04-26 | „the enriched plot concept“ (an unsigned German plot outline) | a premise — AEGIS, an autopoietic AI in the Potentialmeer, fragments Kael, an avatar of the entity M, into 20 Kernwelten, four in focus (Co₁, McL, B, Ly), held as faulty caches — with conflict, setting, genre and themes, and a 39-chapter theme draft in three parts (Kapitel 1–10, 11–25, 26–39), each chapter keyed to a borrowed concept; no claim about its own standing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (81 lines for `angereichertes-plotkonzept-kap`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plot outline: write „the enriched plot concept has / plans …“ in its present tense, and name the chapter where a point comes from the draft. Its chapter entries are numbered 1–N anew in each part; Kapitel N follows from the part's range and the entry's order (Teil 1 L36–L45 = Kap 1–10, Teil 2 L49–L63 = Kap 11–25, Teil 3 L67–L80 = Kap 26–39). The bracketed concept numbers „(67)“ are references, not chapters — never quote them. The borrowed concepts are lens.

## Pages — document 309, `angereichertes-plotkonzept-kapitelthemen-detailliert-kohaere`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L22, L24, L26, L36, L37, … (20 lines). central (3–6): the autopoietic AI fighting for its existence in the Potentialmeer, defending its borders (L15); a faulty „Kohärenz-Controller“ that enforces and analyses incoherence (L22); its system with visible „Rissen“ (L26); the cascading data corruption from the K-J anomaly (L54, Kap 16); its alignment dilemma (L73, Kap 32); its collapse by Gödelian self-contradiction (L78, Kap 37).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L22, L42, L52, L60, L72. minor (1–3): the Kernwelten as faulty „Caches“, each holding an inconsistent copy of Kael's identity (L22); the cache chapters — conflict (L52, Kap 14), faulty updates (L60, Kap 22), active synchronisation (L72, Kap 31).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L22, L39. minor (1–3): DID as the process of fragmentation, Kael's time jumps and memory gaps (L39, Kap 4).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L24, L30, L65, L69. minor (1–3): Kael seeding simple rules into the Ly-Welt that grow into complex structures (L69, Kap 28); Teil 3's title (L65).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L80. minor (1–3): the resolution's new, more stable „niedrig-entropische?“ existence form in the Potentialmeer (L80, Kap 39) — keep the question mark.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L22, L24, L44, L55, L71, L79. minor (1–3): supporting Kael's striving for integration (L24); a moment of shared perception with Kael (L55, Kap 17); mediating Kael's intuitive insight (L71, Kap 30).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L22, L24, L36, L37, L38, … (36 lines). central (3–6): an avatar of the entity M, fragmented by AEGIS into 20 Kernwelten (L15); the fragmentation as DID (L39, Kap 4); arrival in Co₁ under a social error-correction code (L40, Kap 5); confronting his manifest shadow (L58, Kap 20); the sensory fusion of all 20 fragments (L74, Kap 33); integration as Kael/M (L77, L79, Kap 36, Kap 38).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L15, L22, L26, L40, L70. minor (1–3): 20 Kernwelten, four in focus — Co₁, McL, B, Ly with their rules (L15–L20); the other 16 worlds glimpsed (L74, Kap 33); leaks between the worlds (L70, Kap 29).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the novel's title.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L22. minor (1–3): the K-J link as `Moonshine-Link` in the premise (L22), only where the line is about the link; its culmination as a stable conscious channel (L76, Kap 35).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L15, L26, L36, L70, L79, L80. minor (1–3): an unstable meta-space of pure potentiality with ontological friction (L15); shown in Kap 1 (L36); the changed Potentialmeer after integration (L79, L80).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L22, L26, L47, L54. minor (1–3): AEGIS's system „mit sichtbaren „Rissen““ (L26); the cascading corruption visualised as Risse (L54, Kap 16); Teil 2's title (L47).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L30. not read: occurrence — `Simulation` (L30) is a theme word in the Kernthemen line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: `Gödel` is the borrowed incompleteness theorems (L43, L78), lens.
- `kohaerenz`: `Kohärenz-Controller` (near `koharenz`), `Identitäts-Kohärenz` (near `koharenz`), `alternatives Kohärenzprotokoll` (near `koharenz`), `Kohärenzfehler` (near `koharenz`), `temporale Kohärenzverletzung` (near `koharenz`), `Kohärenzwelle` (near `koharenz`), … (7). occurrence: the plan's coherence labels (`Kohärenz-Controller`, `Identitäts-Kohärenz`, `Kohärenzwelle` …), read with the cache-kohaerenz and aegis readings, not promoted.
- `personas`: `Transpersonale Psychologie` (near `persona`). occurrence: `Transpersonale Psychologie` a borrowed school, lens.
- `verschraenkungs-insel`: `Verschränkung` (near `verschrankungsinsel`). occurrence: `Verschränkung` the borrowed quantum concept (L45), lens.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: 20 Kernwelten, four in focus, named after sporadic groups — Co₁, McL, B, Ly (L15–L20) — and „Die anderen 16 Welten“ (L74); quote around the digits and subscripts.

**Not promoted:** the entity M, the four named worlds and their rules, the Kohärenz-Controller, the ontological friction, the chapter concept labels, and the borrowed lens (Gödel, Theseus, Moonshine, IFS, NET, cellular automata, quantum foam, transpersonal psychology).

**One reader**: every page above, the record entry and the chapter readings below.

**Chapter readings** (the same reader, one file per chapter, into `Plan/runs/ingest-310-kap/readings/kap-NN--angereichertes-plotkonzept-kapitelthemen-detailliert-kohaere.md`, Kap 1 to Kap 39): each chapter's entry in the theme draft — its concept label (backticks, no bracketed number) and what it has happen, one bullet with one or two quotations from its own line: Kap 1–10 from L36–L45, Kap 11–25 from L49–L63, Kap 26–39 from L67–L80, in order. Say in each that the number follows from the part's range and the entry's order, since the export restarts the numbering. A plan, not the chapter.
