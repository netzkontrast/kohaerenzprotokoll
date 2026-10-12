# Brief — readings from document 320 (step 6)

1 document, one reader, one batch: `ingest-321`. Files go to `Plan/runs/ingest-321/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 320 | `entwicklungsstrategie-fuer-kohaerenz-protokoll` | 2025-04-28 | „the development-strategy guide“ (an unsigned German how-to guide with a web reference list) | a guide in the imperative for using a novel-writing software on the novel: it maps figures, core worlds, the Juna/Verbindung pair, Paradoxon X, Cache Kohärenz and the three-part structure onto the software's features (L84–L94), with sample prompts, a workflow and recommendations; tool guidance, light pass, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (286 lines for `entwicklungsstrategie-fuer-koh`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is tool guidance: it tells a user how to enter the novel's figures, worlds and concepts into a writing software, and its sample prompts are prompts. It states nothing about the novel's world that a page needs. The census and note stand as the record that it was read.

## Pages — document 320, `entwicklungsstrategie-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L51, L53, L87, L90, L91, L108, … (13 lines). not read: named only as material to enter into the software.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L51, L52, L88, L144. not read: named only as material to enter into the software.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L144. not read: named only as material to enter into the software.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L90, L139. not read: named only as material to enter into the software.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L51, L52, L53, L88, L90, L91, … (16 lines). not read: named only as material to enter into the software.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L51, L52, L89, L131, L173, L209; `Kernwelt` L51, L52, L89, L108, L131, L133, … (13 lines). not read: named only as material to enter into the software.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: named only as material to enter into the software.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L90. not read: named only as material to enter into the software.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L53. not read: named only as material to enter into the software.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Fragmentierung` (near `psychischefragmentierung`). occurrence: an item of the tool mapping or a sample prompt; not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Systemkohärenz` (near `koharenz`). occurrence: an item of the tool mapping or a sample prompt; not read.


**Record entries:** none.

**Not promoted:** everything — the software's features, the mapping table, the sample prompts, the workflow.

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter of the novel.
