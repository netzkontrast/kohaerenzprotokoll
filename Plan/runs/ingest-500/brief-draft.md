# Brief — readings from document 500 (step 6)

1 document, one reader, one batch: `ingest-500`. Files go to `Plan/runs/ingest-500/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 500 | `roman-kapitel-1-erstellung-analyse` | 2025-12-28 | <brief: the name the reading calls it> | <brief: what it is, in one clause, and how it stands>|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (275 lines for `roman-kapitel-1-erstellung-ana`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** <brief: how each document's readings must be worded: a plan says what it wants, a review what it reports, a proposal what it proposes; a name inside an example is the example's>

## Pages — document 500, `roman-kapitel-1-erstellung-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L27, L59, L65, L75, … (13 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L29, L203, L251. <brief: what the document says about it, with its lines, or „not read: why“>
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache-Kohärenz` L189, L203. <brief: what the document says about it, with its lines, or „not read: why“>
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L246, L261. <brief: what the document says about it, with its lines, or „not read: why“>
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L255. <brief: what the document says about it, with its lines, or „not read: why“>
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L65. <brief: what the document says about it, with its lines, or „not read: why“>
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L21. <brief: what the document says about it, with its lines, or „not read: why“>
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L241, L243, L270. <brief: what the document says about it, with its lines, or „not read: why“>
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L33, L73, L75, L83, L93, L99, … (11 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L27, L29, L33, L39, … (40 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L153, L205, L247. <brief: what the document says about it, with its lines, or „not read: why“>
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. <brief: what the document says about it, with its lines, or „not read: why“>
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L23, L33, L109, L119, L153, L175, … (9 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L23, L83, L85, L107, L151, L165, … (10 lines). <brief: what the document says about it, with its lines, or „not read: why“>
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L109, L245. <brief: what the document says about it, with its lines, or „not read: why“>
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L260. <brief: what the document says about it, with its lines, or „not read: why“>
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L19, L21. <brief: what the document says about it, with its lines, or „not read: why“>
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L75. <brief: what the document says about it, with its lines, or „not read: why“>
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L245. <brief: what the document says about it, with its lines, or „not read: why“>
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L219, L263; `Glitch` L29, L107, L163, L238. <brief: what the document says about it, with its lines, or „not read: why“>
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L89. <brief: what the document says about it, with its lines, or „not read: why“>

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Architektur` (near `zerotrust`). <brief: an occurrence, and why — or a reading, and its lines>
- `entropie`: `Niedrigen Entropie` (near `entropie`), `Niedrige Entropie` (near `entropie`), `Hohe Entropie` (near `entropie`). <brief: an occurrence, and why — or a reading, and its lines>
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). <brief: an occurrence, and why — or a reading, and its lines>
- `genesis`: `Post-Genesis` (near `genesis`), `Genesis der Existenz` (near `genesis`). <brief: an occurrence, and why — or a reading, and its lines>
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 4` (near `kernwelt`). <brief: an occurrence, and why — or a reading, and its lines>
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`). <brief: an occurrence, and why — or a reading, and its lines>
- `personas`: `Depersonalisation` (near `persona`). <brief: an occurrence, and why — or a reading, and its lines>
- `residual-echos`: `Echo` (near `residualechos`). <brief: an occurrence, and why — or a reading, and its lines>

