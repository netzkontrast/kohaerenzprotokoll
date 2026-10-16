# Brief — readings from document 501 (step 6)

1 document, one reader, one batch: `ingest-501`. Files go to `Plan/runs/ingest-501/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 501 | `aieos-schema-fuer-ki-charaktere` | 2026-02-28 | <brief: the name the reading calls it> | <brief: what it is, in one clause, and how it stands>|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (641 lines for `aieos-schema-fuer-ki-charakter`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** <brief: how each document's readings must be worded: a plan says what it wants, a review what it reports, a proposal what it proposes; a name inside an example is the example's>

## Pages — document 501, `aieos-schema-fuer-ki-charaktere`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L31, L35, L41, L43, … (19 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L35. <brief: what the document says about it, with its lines, or „not read: why“>
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L43. <brief: what the document says about it, with its lines, or „not read: why“>
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L19, L31, L35, L41, L43, … (19 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. <brief: what the document says about it, with its lines, or „not read: why“>
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L51, L108. <brief: what the document says about it, with its lines, or „not read: why“>
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L307, L364, L600. <brief: what the document says about it, with its lines, or „not read: why“>
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L35. <brief: what the document says about it, with its lines, or „not read: why“>
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L45. <brief: what the document says about it, with its lines, or „not read: why“>
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L41. <brief: what the document says about it, with its lines, or „not read: why“>

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Kernel` (near `dualkerneltheoriedkt`), `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). <brief: an occurrence, and why — or a reading, and its lines>
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Digests` (near `koharenz`). <brief: an occurrence, and why — or a reading, and its lines>
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). <brief: an occurrence, and why — or a reading, and its lines>

