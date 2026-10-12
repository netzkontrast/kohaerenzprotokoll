# Brief — readings from document 389 (step 6)

1 document, one reader, one batch: `ingest-390`. Files go to `Plan/runs/ingest-390/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 389 | `dramatica-storyform-kohaerenz-protokoll` | 2026-01-02 | „the January storyform“ (an unsigned English Dramatica storyform, 2026-01-02) | sets the novel as one Grand Argument Story: OS Universe (AEGIS's system), MC Mind (Kael), IC Psychology (Juna/V), SS Physics (the Moonshine-Link), with Concerns, Issues and Problems, and maps KW1–KW4 onto the four throughlines; it calls itself „the definitive architectural blueprint“ — recorded, not applied; it predates decision 025 and its domains differ from storyform A |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (70 lines for `dramatica-storyform-kohaerenz-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A storyform draft: write „the January storyform sets / assigns …“; its values are its own and decide nothing — decision 025's storyforms A and B stand, and where the readings name a value they attribute it to this document. Quote the English as written; cut before escaped emphasis and straight quotes. No gendered pronoun for Kael or Juna/V — use the names (quotations stay verbatim).

## Pages — document 389, `dramatica-storyform-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L23, L34, L35, L36, L37, … (13 lines). central (3–5): the Overall Story in the domain Universe, the simulated reality governed by AEGIS's paradoxical logic (L34); its Progress devolving toward collapse (L35); Control vs. Uncontrolled, AEGIS's obsession with algorithmic control (L36); the Problem Uncontrolled, a phobia symbolised by the Nichts Rauschen (L37); AEGIS's attempts to sever the link (L58).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L53. minor (1–3): AEGIS's „Zero-Trust“ principles, which Juna/V's trust bypasses and refutes (L53).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L44, L45, L50. minor (1–3): the contradictory information from Kael's internal alters (L44); Kael's disbelief in the validity of the voices of the alters (L45).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L36, L47, L50, L51, L52, … (11 lines). central (3–5): Juna/V as the Impact Character in the domain Psychology, a way of thinking rooted in connection and resonance (L50); Concern Becoming, a catalyst for transformation (L51); Commitment vs. Responsibility (L52); the Problem Trust (L53).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L35, L36, L39, L42, … (15 lines). central (3–5): Main Character Resolve Change, toward functional multiplicity (L23); the MC throughline in the domain Mind, fixed in trauma-induced fragmentation (L42); Concern The Conscious (L43); Issue Truth vs. Falsehood (L44); Problem Disbelief, whose overcoming is called the novel's true Kohärenz Protokoll (L45).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L23, L63, L65; `Kernwelt` L23, L63, L65. minor (1–3): the Kernwelten as externalized psychological landscapes resonating with the throughlines: KW1 Logos-Prime with the Overall Story, KW2 Mnemosyne-Archipel with the Main Character, and the others as the line sets them (L65).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L53, L55, L58, L65. minor (1–3): the Moonshine-Link based on a non-local, intuitive trust that refutes AEGIS's Zero-Trust (L53); the Subjective Story of Kael and Juna/V in the domain Physics, the activity of building the link (L58); Obtaining a stable channel (L59); the Problem Control (L61).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L37. minor (1–3): the Nichts Rauschen from which AEGIS emerged, symbol of its phobia of the uncontrolled (L37).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L36. minor (1–3): the chaotic Potentialmeer that AEGIS seeks to hold at bay, part of the Uncontrolled (L36).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L23, L65. minor (1–3): glitches or Risse in KW1's geometry as a visual measure of the failing Progress of AEGIS's system (L65).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L42. minor (1–3): Kael's fixed mind modelled on the Theory of Structural Dissociation of the Personality (TSDP) (L42).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `kairos`: `Kairos-Potentialis` (near `kairos`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `logos`: `Logos-Prime` (near `logos`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `truth-rotation`: `Truth` (near `truthrotation`). `Juna/V` on juna; `Zero-Trust` on aegis-teilfunktionen, `Trust` the IC Problem; the Kernwelt names on kern-welten, worlds not Guardians; `Truth` a Dramatica Issue, not the Truth-Rotation; `Story Mind`, `Main Character` and `Control`/`Uncontrolled` Dramatica terms; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.


**Pages not read:** `kohaerenz` (the title) — an occurrence.

**Record entries:** none. The storyform's values differ from storyform A of decision 025 (here OS Universe and IC Psychology, MC Concern The Conscious and Problem Disbelief; A has IC Universe, OS Psychology, MC Memory and Inertia). The document predates the decision; this is recorded in the reconciliation record, not raised as a question.

**Not promoted:** Story Mind, Grand Argument Story and every Dramatica value; the borrowed concepts.

**One reader**: aegis, kael, juna, moonshine-link, aegis-teilfunktionen, potentialmeer, nichts-rauschen, risse, kern-welten, alters, tsdp.

**Chapter readings**: none — the storyform names no chapters.
