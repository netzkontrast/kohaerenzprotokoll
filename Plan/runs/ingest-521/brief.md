# Brief — readings from document 521 (step 6)

1 document, one reader, one batch: `ingest-521`. Files go to `Plan/runs/ingest-521/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 521 | `codex-optimierung-fuer-kohaerenz-protokoll` | 2025-04-29 | „the Codex optimisation report" (an unsigned German research report) | a report on configuring an AI-assisted writing tool for the novel — template assessment, Codex field names, a master prompt, a context strategy — demonstrated on two scenes it labels hypothetical (L316, L333, L407); the novel's figures and world appear only as sample material; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (583 lines for `codex-optimierung-fuer-kohaere`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: a tooling report whose figures and world values are sample data for a writing tool, never statements about the story.

## Pages — document 521, `codex-optimierung-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L38, L50, L62, L63, L96, … (26 lines). not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L50. not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L38, L112, L139. not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L38, L94, L111, L133, L150, … (13 lines). not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelt` L43, L44, L63, L95, L101, L113, … (16 lines); `Kernwelten` L550. not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L46, L113, L142, L147, L297, L353, … (8 lines). not read: light pass — the tooling report's sample data, not a statement about the novel.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L43. not read: light pass — the tooling report's sample data, not a statement about the novel.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `tsdp`: `TSDP-System` (near `tsdp`), `TSDP-Dynamiken` (near `tsdp`), `TSDP-basiert` (near `tsdp`), `TSDP-Rolle` (near `tsdp`). an occurrence: sample data, light pass.


**Record entries:** none.

**Not promoted:** the tool's templates, the Codex field names, the master prompt, the three-tier context strategy, the hypothetical scenes, and the sample world and part values.

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
