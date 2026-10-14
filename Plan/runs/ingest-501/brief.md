# Brief — readings from document 501 (step 6)

1 document, one reader, one batch: `ingest-501`. Files go to `Plan/runs/ingest-501/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 501 | `aieos-schema-fuer-ki-charaktere` | 2026-02-28 | „the AIEOS evaluation" (an unsigned German software report) | an evaluation of an AI-character JSON schema for the two kernels of a software architecture that names its kernels AEGIS and Juna and says it derives from the Kohärenz Protokoll (L15); it recommends dropping the schema (L606–L616); about software, not about the novel |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (641 lines for `aieos-schema-fuer-ki-charakter`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: the document is a software-architecture report that borrows the novel's names for its kernels; nothing it says is a reading of the novel's terms.

## Pages — document 501, `aieos-schema-fuer-ki-charaktere`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L31, L35, L41, L43, … (19 lines). not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L35. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L43. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L19, L31, L35, L41, L43, … (19 lines). not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L51, L108. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L307, L364, L600. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L35. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L45. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L41. not read: light pass — the software report uses the name for a kernel of its own architecture, not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Kernel` (near `dualkerneltheoriedkt`), `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). an occurrence: the software report's own use, light pass.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Digests` (near `koharenz`). an occurrence: the software report's own use, light pass.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). an occurrence: the software report's own use, light pass.


**Record entries:** none.

**Not promoted:** JANUS, the AIEOS schema and its fields, the kernel nicknames, the runtimes and protocols the report compares, and the borrowed theory concepts (some carry a person's name).

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
