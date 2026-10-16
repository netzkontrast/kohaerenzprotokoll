# Brief — readings from document 413 (step 6)

1 document, one reader, one batch: `ingest-414`. Files go to `Plan/runs/ingest-414/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 413 | `dramatica-theorie-narrativem-kontext-storyentwicklung` | 2026-04-26 | „the Dramatica and NCP exposition“ (an unsigned German expository report) | explains the Dramatica story theory and the Narrative Context Protocol with an invented workflow and examples; it names no figure, place or term of the novel; no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (256 lines for `dramatica-theorie-narrativem-k`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a general exposition of a story theory and a protocol with invented examples; it names nothing of the novel. The census and note stand as the record that it was read.

## Pages — document 413, `dramatica-theorie-narrativem-kontext-storyentwicklung`

- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L197. not read: the exposition's general sense.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: the exposition's general sense.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`), `Trust` (near `zerotrust`). occurrence: the exposition's own or a general sense; not read.
- `guardians`: `Guardian` (near `guardians`). occurrence: the exposition's own or a general sense; not read.
- `potentialmeer`: `Potential` (near `potentialmeer`). occurrence: the exposition's own or a general sense; not read.


**Record entries:** none.

**Not promoted:** everything — the theory's and the protocol's terms.

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
