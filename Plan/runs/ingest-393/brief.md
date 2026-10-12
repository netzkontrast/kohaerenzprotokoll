# Brief — readings from document 392 (step 6)

1 document, one reader, one batch: `ingest-393`. Files go to `Plan/runs/ingest-393/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 392 | `ki-architektur-fuer-kohaerenz-und-skalierbarkeit` | 2026-01-02 | „the NeSy architecture report“ (an unsigned German proposal report) | proposes a neuro-symbolic architecture for consistent long generated stories — ontology and SHACL, a temporal knowledge graph, an agent hierarchy and a „Vortex“ cycle; it names no figure of the novel; no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (349 lines for `ki-architektur-fuer-kohaerenz-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a general proposal for an AI writing architecture; its examples are generic, it names no figure, place or object of the novel, and its `Vortex` is a cycle of its own architecture, not the novel's Vortex. The census and note stand as the record that it was read.

## Pages — document 392, `ki-architektur-fuer-kohaerenz-und-skalierbarkeit`

- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L11. not read: the report's own or general sense (its architecture's Vortex cycle, coherence and entropy in general), not the novel's term.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: the report's own or general sense (its architecture's Vortex cycle, coherence and entropy in general), not the novel's term.
- **`vortex`** (minor, 1–4): the census's surfaces — `Vortex` L17, L55, L287. not read: the report's own or general sense (its architecture's Vortex cycle, coherence and entropy in general), not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenztheorie` (near `koharenz`). occurrence in the general sense; not read.


**Record entries:** none.

**Not promoted:** everything — the architecture, its components and the borrowed concepts.

**No reader**: no readings are written.

**Chapter readings**: none.
