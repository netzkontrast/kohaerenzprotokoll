# Brief — readings from document 321 (step 6)

1 document, one reader, one batch: `ingest-322`. Files go to `Plan/runs/ingest-322/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 321 | `konzept-der-architektenraum-ein-behind-the-scenes-spiegel-zu` | 2025-04-28 | „the Architektenraum outline“ (an unsigned German concept outline) | an outline for a companion text, „Der Architektenraum“, a behind-the-scenes mirror meant to explain the theory behind the novel: four parts and ten chapters each listing topics to discuss (psyche, AEGIS, worlds and the Fundament, narrative choices), hedged with „könnte“, nothing defined or written out; a plan for another work, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (181 lines for `konzept-der-architektenraum-ei`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document outlines a companion work that would explain the theory behind the novel; it lists the novel's figures, worlds and theories only as topics that companion would discuss, and states nothing about them that a page needs. One appendix item (L164) was not read. The census and note stand as the record that it was read.

## Pages — document 321, `konzept-der-architektenraum-ein-behind-the-scenes-spiegel-zu`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L77, L86, L94, L95, L108. not read: listed only as a topic of the companion work the outline plans.
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L85. not read: listed only as a topic of the companion work the outline plans.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L116. not read: listed only as a topic of the companion work the outline plans.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L45, L54, L108. not read: listed only as a topic of the companion work the outline plans.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L108. not read: listed only as a topic of the companion work the outline plans.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: listed only as a topic of the companion work the outline plans.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L55. not read: listed only as a topic of the companion work the outline plans.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L55, L64. not read: listed only as a topic of the companion work the outline plans.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L64. not read: listed only as a topic of the companion work the outline plans.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L20, L49, L53, L54, L64, L72. not read: listed only as a topic of the companion work the outline plans.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L103. not read: listed only as a topic of the companion work the outline plans.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: the outline's topics; not read.
- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: the outline's topics; not read.
- `juna`: `Juna/V` (near `juna`). occurrence: the outline's topics; not read.
- `kiko`: `Kikos` (near `kiko`). occurrence: the outline's topics; not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the outline's topics; not read.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: the outline's topics; not read.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: the outline's topics; not read.


**Record entries:** none.

**Not promoted:** everything — Der Architektenraum, its parts and chapters, and the topics it lists.

**No reader**: no readings are written.

**Chapter readings**: none — its parts and chapters are the companion text's own, not the novel's.
