# Brief — readings from document 399 (step 6)

1 document, one reader, one batch: `ingest-400`. Files go to `Plan/runs/ingest-400/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 399 | `kohaerenz-protokoll-architektur-implementierung` | 2026-02-27 | „the implementation plan“ (an unsigned German technical report) | evaluates three software ecosystems and lays out a four-phase plan for a single-user writing tool; real-system material — its statements on the novel's figures are taken from a character document it cites and serve the tool's design; no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (196 lines for `kohaerenz-protokoll-architektu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a technical plan for a real software system, a writing tool for a single user; where it names Kael's parts (L49, L59, L69, L119) it repeats a character document it cites as its source and maps them onto software objects, and it names real people (L53, L71, L86). The census and note stand as the record that it was read.

## Pages — document 399, `kohaerenz-protokoll-architektur-implementierung`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L13, L36, L41, L71, L108, L143. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L27. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L13, L93. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L13, L45, L49, L51, L116, L119, … (7 lines). not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L49, L59. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L13. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L13, L38, L93. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L49, L51, L69, L71, L119. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L49. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L133. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L49, L51, L119. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L119. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L13, L47, L49, L104, L143. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L13. not read: real-system material — a technical plan for a writing tool, whose naming of the novel's figures and terms repeats a cited character document and maps it onto software objects.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Dual Kernel Theorie` (near `dualkerneltheoriedkt`). occurrence: the plan's own or a borrowed sense; not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence: the plan's own or a borrowed sense; not read.
- `konstrukt-stadt`: `Konstrukts` (near `konstruktstadt`). occurrence: the plan's own or a borrowed sense; not read.
- `thermodynamischer-phaenomenalismus`: `Phaenomena` (near `thermodynamischerphaenomenalismus`). occurrence: the plan's own or a borrowed sense; not read.


**Record entries:** none.

**Not promoted:** everything — the software components, the plan's phases and the borrowed concepts.

**No reader**: no readings are written.

**Chapter readings**: none — `Kapitel 12` (L100) and `Akt III` (L133) are named only as analogies for the software.
