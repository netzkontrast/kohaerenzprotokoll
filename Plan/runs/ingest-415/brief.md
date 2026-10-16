# Brief — readings from document 414 (step 6)

1 document, one reader, one batch: `ingest-415`. Files go to `Plan/runs/ingest-415/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 414 | `spec-entwicklung-fuer-agentic-dramatica-roman` | 2026-04-26 | „the agentic-Dramatica spec“ (an unsigned German specification) | specifies a multi-agent system that writes novels through the four Dramatica phases, with schema, constraints, invariants, failure catalogue and decision records; it names no figure, place or term of the novel; no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (593 lines for `spec-entwicklung-fuer-agentic-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a general software specification for writing novels with agents; it names nothing of this novel. The census and note stand as the record that it was read.

## Pages — document 414, `spec-entwicklung-fuer-agentic-dramatica-roman`

- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L26. not read: the specification's general sense.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Record entries:** none.

**Not promoted:** everything — the specification's parts, identifiers and the Dramatica vocabulary.

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
