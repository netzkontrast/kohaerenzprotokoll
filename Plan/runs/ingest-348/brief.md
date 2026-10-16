# Brief — readings from document 347 (step 6)

1 document, one reader, one batch: `ingest-348`. Files go to `Plan/runs/ingest-348/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 347 | `archon-ai-narrative-coherence-framework` | 2025-10-15 | „the ARCHON report“ (an unsigned English analytic report) | an analysis of ARCHON, a proposed AI framework for narrative coherence (the Narrative Context Protocol, a four-layer knowledge hypergraph, a self-critiquing director agent), compared with existing writing tools; the novel enters only in section V (L184–L216) as a proposed case study; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (337 lines for `archon-ai-narrative-coherence-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analytic report on an AI tool: write „the ARCHON report proposes, as a case study, …“; everything about the novel sits in the proposed case study of section V and is a proposal for a test, not an account of the novel. It never names Kael: write „the case study's protagonist“.

## Pages — document 347, `archon-ai-narrative-coherence-framework`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L202, L204. minor (1–3): the case study's antagonist as an AI, AEGIS (L202), whose motivation the NCP would encode as a formal process (L204).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L194. minor (1–3): modelling the alters under TSDP as a proposed test of the framework (L194).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L192, L323. minor (1–3): the case study's protagonist characterised by Dissociative Identity Disorder (L192); the reference-list hit (L323) is a host name, not read.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L184. not read: an occurrence (see below).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L188, L192, L194, L216. minor (1–3): the protagonist modelled on TSDP (L188, L192); successfully modelling TSDP would demonstrate the framework (L194).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the novel's title as the case study's subject.


**Pages not read:** `kohaerenz` (L184 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** ARCHON, the Narrative Context Protocol as applied here, the Knowledge Hypergraph and its layers, the Narrative Director, Project Coherence, the compared tools, and the borrowed concepts (Dramatica, ReAct, complexity classes).

**One reader**: aegis, alters, did, tsdp.

**Chapter readings**: none.
