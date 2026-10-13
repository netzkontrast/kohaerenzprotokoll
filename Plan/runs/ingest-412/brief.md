# Brief — readings from document 411 (step 6)

1 document, one reader, one batch: `ingest-412`. Files go to `Plan/runs/ingest-412/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 411 | `narrative-context-protocol-ncp-spezifikation` | 2025-07-03 | „the NCP white paper“ (an unsigned German specification proposal) | proposes Dramatica values for four story subsystems — Kael, AEGIS, Juna/V, Das Fundament (Table 1, L51–L61) — a JSON schema for the Narrative Context Protocol, a prompt cascade, an oversight component and a roadmap; a proposal that calls its table „die entscheidende kreative und logische Grundlage“ (L63); predates decision 025 |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (224 lines for `narrative-context-protocol-ncp`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A specification proposal: write „the NCP white paper proposes …“; its table assigns each subsystem one value set — Kael's, AEGIS's, Juna/V's — which are not storyforms A and B of decision 025; never apply them. Its JSON schema and prompt cascade are software, not the novel: read only Part I (L13–L75). Quote the German as written; cut before straight and nested quotes, bold markers and glued footnote digits. No gendered pronoun for Kael or Juna — use the names. Never write a real person's name.

## Pages — document 411, `narrative-context-protocol-ncp-spezifikation`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L30, L51, L71, L126, L165, L166, … (7 lines). minor (1–3): one of the four subsystems (L30); in Table 1 „AEGIS (Logisch-Systemische Ebene)“ (L51), Domain Physics, Concern Obtaining, Issue Self-Interest vs. Morality, Problem Control, Solution Uncontrolled, Goal Learning, Consequence Doing (L53–L61).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L75. not read: an occurrence — emergence in the white paper's general sense (L75).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L30. minor (1–3): the subsystem „Juna/V“ (L30); in Table 1 „Juna/V (Ontologische Ebene)“ (L51), Domain Universe, Concern Future, Issue Faith vs. Disbelief, Problem Inequity, Solution Equity, Goal The Past, Consequence Progress (L53–L61).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L30, L51, L71, L115, L117, L166, … (8 lines). minor (1–3): one of the four story subsystems (L30); in Table 1 „Kael (Psychologische Ebene)“ (L51), Domain Mind, Concern Conscious, Issue Appraisal vs. Re-appraisal, Problem Doubt, Solution Certainty, Goal Understanding, Consequence Memories (L53–L61).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L45. not read: an occurrence — simulation in the software sense (L45).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). decided with the pages above: `Juna/V` read on juna; `Das Fundament`/`DasFundament` one subsystem, no page; the schema's field names the white paper's own; `Kohärenz Protokoll` the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). decided with the pages above: `Juna/V` read on juna; `Das Fundament`/`DasFundament` one subsystem, no page; the schema's field names the white paper's own; `Kohärenz Protokoll` the title.


**Record entries:** none.

**Pages not read:** emergenz, kohaerenz, ueberwelt — occurrences.

**Not promoted:** Narrative Context Protocol, Das Fundament, Dramaturgischer Aufseher, activeFocalSystem and the other schema fields, the prompt cascade, and the Dramatica vocabulary.

**One reader**: kael, aegis, juna.

**Chapter readings**: none — the document names no chapter.
