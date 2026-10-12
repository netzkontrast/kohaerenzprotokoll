# Brief — readings from document 393 (step 6)

1 document, one reader, one batch: `ingest-394`. Files go to `Plan/runs/ingest-394/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 393 | `the-coherence-protocol-an-architectural-blueprint-for-agenti` | 2026-01-02 | „the NovelOS white paper“ (an unsigned English white paper) | presents a narrative-generation architecture (NovelOS, ARCHON, the Narrative Context Protocol) and uses the novel as its case study, saying the novel was „the stress test that forged“ it; it calls itself a „manifesto“ — recorded, not applied; a light pass |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (98 lines for `the-coherence-protocol-an-arch`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A light pass: readings only where the case study speaks to the novel (section 5). Write „the NovelOS white paper describes the novel's conflict as …“; it reports the novel from outside, deciding nothing. Quote the English as written; cut before LaTeX ($K\_1$) and escaped emphasis. No gendered pronoun for Kael — use the name (quotations stay verbatim).

## Pages — document 393, `the-coherence-protocol-an-architectural-blueprint-for-agenti`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L26, L48, L69, L89, L93. minor (1–2): the case study's AEGIS, „an AI that embodies coherence through the exclusion of paradox“, on classical logic and the K₁ kernel; the AEGIS agent keeping its own beliefs and rules in the architecture (L89).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L48. not read: an occurrence (see below).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L26, L32, L48, L69, L89, L93. minor (1–2): System Kael, „a human consciousness that achieves coherence through the integration of paradox“, on paraconsistent logic and the K₀ kernel (L89); Kael's climax as functional multiplicity, a living Gödel-Satz (L93).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L26. not read: an occurrence (see below).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L68. not read: an occurrence (see below).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L34, L35. not read: a light pass — the architecture's borrowed clinical model, not the novel's.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Kernel` (near `dualkerneltheoriedkt`). `System Kael` on kael; `Juna/V` (L48) a table column head; `Kohärenz Protokoll` the title (L26); `Persona` (L68) an agent persona of the architecture; `Kernel` the architecture's own word.
- `juna`: `Juna/V` (near `juna`). `System Kael` on kael; `Juna/V` (L48) a table column head; `Kohärenz Protokoll` the title (L26); `Persona` (L68) an agent persona of the architecture; `Kernel` the architecture's own word.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `System Kael` on kael; `Juna/V` (L48) a table column head; `Kohärenz Protokoll` the title (L26); `Persona` (L68) an agent persona of the architecture; `Kernel` the architecture's own word.
- `kohaerenz-kernel`: `Kernel` (near `kohaerenzkernel`), `Kernel` (near `koharenzkernel`), `Kernel` (near `koharenzkernelk1`). `System Kael` on kael; `Juna/V` (L48) a table column head; `Kohärenz Protokoll` the title (L26); `Persona` (L68) an agent persona of the architecture; `Kernel` the architecture's own word.
- `kollaps-kernel`: `Kernel` (near `kollapskernel`), `Kernel` (near `kollapskernelk0`). `System Kael` on kael; `Juna/V` (L48) a table column head; `Kohärenz Protokoll` the title (L26); `Persona` (L68) an agent persona of the architecture; `Kernel` the architecture's own word.


**Pages beyond the draft:**
- `goedel-gambit` (minor, 1): Kael becoming „a living Gödel-Satz“, true within the system's world but unprovable by its axioms (L93).

**Pages not read:** `tsdp`, `juna`, `kohaerenz`, `personas` — a light pass, occurrences.

**Record entries:** none.

**Not promoted:** everything else — NovelOS, ARCHON, the Narrative Context Protocol, BDI-OCC, and the borrowed frameworks.

**One reader**: aegis, kael, goedel-gambit.

**Chapter readings**: none — the paper names no chapters.
