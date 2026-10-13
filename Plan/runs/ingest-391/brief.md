# Brief — readings from document 390 (step 6)

1 document, one reader, one batch: `ingest-391`. Files go to `Plan/runs/ingest-391/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 390 | `dramatica-storyform-kohaerenz-protokoll-2` | 2026-01-02 | „the four-subsystem storyform“ (an unsigned English Dramatica storyform, 2026-01-02) | assigns storyforms to four subsystems — Kael (Mind, Memories), AEGIS (Physics, Understanding), Juna/V (Universe, Future), the Fundament (Psychology, Becoming) — and maps them onto OS, MC, IC and SS; it calls its storyforms „immutable“ and the model „complete and consistent“ — recorded, not applied; it predates decision 025 |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (78 lines for `dramatica-storyform-kohaerenz-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A storyform draft: write „the four-subsystem storyform assigns / maps …“; its values are its own and decide nothing — decision 025's storyforms stand; attribute every value to this document. Quote the English as written; cut before escaped emphasis, table pipes and straight quotes. No gendered pronoun for Kael, Juna/V or the parts — use the names (quotations stay verbatim).

## Pages — document 390, `dramatica-storyform-kohaerenz-protokoll-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L23, L27, L43, L45, L49, … (10 lines). minor (1–3): the Logical-Systemic Subsystem (AEGIS) in the domain Physics with the Concern Understanding (L45); AEGIS focusing on the Symptom of inconsistent data — the alters, the Risse, Juna/V's influence (L61).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L15, L47, L49, L61, L67, L69, … (8 lines). minor (1–3): the Ontological Subsystem (Juna/V) in the domain Universe with the Concern Future (L49); the IC throughline, Juna/V as catalyst challenging Kael's Faith (L69).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L27, L39, L41, L45, … (13 lines). central (3–5): Main Character Resolve Change, from TSDP to Functional Multiplicity, and Approach Do-er, traversing the Kernwelten (L23); the Psychological Subsystem (System Kael) in the domain Mind with the Concern Memories (L41); the MC throughline, Kael's Symptom Pursuit of an illusion of normalcy (L65).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L23. minor (1–3): Kael actively traversing the Kernwelten and confronting AEGIS's constructs (L23).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L23. minor (1–3): Kiko among the traumatized Exiles Kael must witness in the IFS process (L23).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L71, L73. minor (1–3): the SS throughline as the Moonshine-Link, the non-local, resonant connection of Kael and Juna, in Physics, driven by Desire, performing „physikalische Arbeit“ against AEGIS's resistance (L73).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L23. minor (1–3): Nyx among the Protectors Kael must witness in the IFS process (L23).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L27, L61. minor (1–3): the Risse (Rifts) caused by the Isolation Objection, Kael's externalized trauma, driving the plot (L27); the Risse among the inconsistent data AEGIS mistakes for the source of instability (L61).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L23. minor (1–3): Kael's journey from Tertiary Structural Dissociation (TSDP) to Functional Multiplicity (L23).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). `System Kael` on kael; `Juna/V` on juna; `Kohärenz Protokoll` the title; `Kohärenztheorie der Wahrheit` a borrowed concept.


**Pages not read:** `kohaerenz` (L11, the title) — an occurrence.

**Record entries:** none. Unlike ingest 390's storyform, this one's domains agree with storyform A of decision 025 (MC Mind / Memories, IC Universe, OS Psychology, SS Physics) while adding a fourth subsystem, the Fundament; recorded in the reconciliation record.

**Not promoted:** the four subsystems as labels, Story Engine Settings, Isolation Objection, Functional Multiplicity, the Fundament, every Dramatica value; the borrowed concepts (IFS, TSDP, theories of truth).

**One reader**: kael, aegis, juna, kiko, nyx, risse, kern-welten, moonshine-link, tsdp.

**Chapter readings**: none — the storyform names no chapters.
