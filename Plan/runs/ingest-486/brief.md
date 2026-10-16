# Brief — readings from document 486 (step 6)

1 document, one reader, one batch: `ingest-486`. Files go to `Plan/runs/ingest-486/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 486 | `romanstruktur-3-teile-39-kapitel-1-anfang` | 2025-12-18 | „the Romanstruktur exegesis“ (an unsigned German essay, „Romanstruktur: 3 Teile, 39 Kapitel, 1 Anfang“, calling itself an Exegese, L11) | outlines a 39-chapter plot in three parts with a frame chapter 40/0 and borrowed models per chapter; its world — `Kael Voss`, a cyber-soldier of the `Aegis Coalition` in `New Zenith`, hunting the data runner `Nova Ardent` — is tied by reference 7 to a cited cyberpunk e-book (L175), so its chapters plan another story under the novel's title |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (215 lines for `romanstruktur-3-teile-39-kapit`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: the exegesis's plot, figures and places come from a cited cyberpunk e-book (reference 7, L175), not from the novel; its `Kael` is `Kael Voss` (L49, L165) and its `Aegis` the `Aegis Coalition`, a megacorporation (L49). No reading goes on a page or a chapter page — a reading would put another book's plot under the novel's figures. Names of real people, including the e-book's creator, are never written.

## Pages — document 486, `romanstruktur-3-teile-39-kapitel-1-anfang`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `Aegis` L21, L23, L49, L51, L55, L59, … (17 lines). not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cache-Kohärenz` alone on L183. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L177. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L21, L23, L25, L35, L49, … (38 lines). not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`kishotenketsu`** (central, 3–12 quotations): the census's surfaces — `Kishōtenketsu` L25, L34, L43, L45, L79, L111, … (10 lines). not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L21. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L25, L51, L140, L155. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L35, L51. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L25. not read: light pass — the exegesis's surface here belongs to the plot of a cited cyberpunk e-book (reference 7), not to the novel; recorded in the census and note only.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`). an occurrence (light pass): the e-book's plot, a reference title or the general sense, not the novel's term.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`), `Apparently Normal Personality` (near `persona`), `Personal Identity` (near `persona`). an occurrence (light pass): the e-book's plot, a reference title or the general sense, not the novel's term.
- `residual-echos`: `Echos` (near `residualechos`). an occurrence (light pass): the e-book's plot, a reference title or the general sense, not the novel's term.


**Record entries:** none.

**Not promoted:** the exegesis's vocabulary and the e-book's names — Kael Voss, Nova Ardent, Aegis Coalition, New Zenith, Neon Ashes, Forsaken, Quarantine Zones, the chapter-range labels, LeanRAG, Triple Helix and the borrowed concepts, several named after people

**No reader**: no readings are written.

**Chapter readings**: none — the exegesis names chapters 1–39 and 40/0, but they plan the e-book's story, not the novel's (precedent: 471).
