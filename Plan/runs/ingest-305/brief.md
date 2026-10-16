# Brief — readings from document 304 (step 6)

1 document, one reader, one batch: `ingest-305`. Files go to `Plan/runs/ingest-305/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 304 | `kohaerenz-protokoll-analyse-und-verstaendnis` | 2025-04-25 | „the cache-coherence report“ (an unsigned German technical report with 54 web references) | an explanation of cache coherence in computer systems — snooping and directory mechanisms, the MESI family, research protocols, consistency and synchronisation, and the physics and signal senses of the word — reading `Kohärenz Protokoll` as the computer-architecture term „Cache Coherence Protocol“ (L17, L236); it names no figure, place, event or chapter of the novel |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (302 lines for `kohaerenz-protokoll-analyse-un`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A technical report, not about the novel: write „the cache-coherence report explains …“, and say on the page that it is the computer-architecture sense of the term, with no figure, place or event of the novel. Cut quotations before glued reference numbers and the raw LaTeX of the table.

## Pages — document 304, `kohaerenz-protokoll-analyse-und-verstaendnis`

- **`cache-kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Cache-Kohärenz` L13, L17, L21, L25, L29, L47, … (32 lines). minor (1–3): the technical sense the novel's image borrows — „Kohärenz Protokoll“ read as the „Cache Coherence Protocol“ of computer architecture (L17, L236), what cache coherence guarantees (L21 or L25); a technical report, not the novel's image — say so.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: occurrence — `Kohärenz` (L13) is in a heading on the computer-architecture term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache-Kohärenzprotokolle` (near `koharenz`), `Kohärenzprotokolle` (near `koharenz`), `Kohärenz-Invarianten` (near `koharenz`), `Approximative Kohärenz` (near `koharenz`), `Kohärenz für disaggregierten Speicher` (near `koharenz`), … (8). occurrence: the technical and physical senses of the word, not the novel's; read on cache-kohaerenz only for the computer-architecture definition.


**Record entries:** none.

**Not promoted:** everything new to the index — the snooping and directory mechanisms, MESI and its family, the research protocols, Kohärenz-Invarianten, approximate coherence, consistency and synchronisation, Dekohärenz and Kohärenzfunktion.

**One reader**: cache-kohaerenz.

**Chapter readings**: none — the document names no chapter.
