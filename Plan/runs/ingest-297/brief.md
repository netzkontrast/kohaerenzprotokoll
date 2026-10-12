# Brief — readings from document 296 (step 6)

1 document, one reader, one batch: `ingest-297`. Files go to `Plan/runs/ingest-297/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 296 | `kohaerenz-protokoll-konzeptionelle-ausarbeitung` | 2025-04-19 | „the conceptual report on the protocol“ (an unsigned German research report with a web reference list) | a report on a „Kohärenzprotokoll“ introduced as „ein abstraktes, hypothetisches Konstrukt“ (L32) that lets a system define and keep its coherence: a taxonomy of five forms of incoherence, a core directive, four derivation mechanisms, three groups of operative functions, a six-component model and a comparison with other disciplines; it names no figure, place, event or chapter, and calls its model „spekulativ und konzeptionell“ (L440) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (541 lines for `kohaerenz-protokoll-konzeption`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report on an abstract construct: write „the conceptual report defines / proposes …“; it describes a mechanism for any system, never the novel's world — say so on each page. Its imperative candidates are relayed from a commissioning text (L110): mark them as relayed. Glued reference numbers end most sentences; cut before them.

## Pages — document 296, `kohaerenz-protokoll-konzeptionelle-ausarbeitung`

- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L153, L157, L190, L192, L194, L244, … (10 lines). minor (1–3): emergence as one of four derivation mechanisms, defined (L157); combining with recursion (L190); its own open question whether the protocol is an emergent property (L445).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L32. minor (1–3): the protocol introduced against entropy in L32 only if the line says so; the thermodynamic entropy entry (L84, L85) as the tendency to decay — a borrowed frame, say so.
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L228. not read: occurrence — `Systemgrenze` (L228) is the abstract system's boundary in a report on any system.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L13, L17, L19, L21, L30, … (73 lines). central (3–6): coherence defined for the report's purpose as a system's internal structural integrity (L21), deliberately broad (L28); the Kohärenzprotokoll as a hypothetical construct letting a system define and keep its coherence (L32), derived from a very simple directive (L32, L106); incoherence not monolithic, five forms (L40, L94); the protocol constitutive, „Form aus Formlosigkeit“ (L102); the core directive as top optimisation goal (L383); the tension between delimiting and staying open (L230).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L124, L225, L230, L276. minor (1–3): extraction of order/negentropy from the environment as an operative function (L225); dissipative structures and negentropy as an analogy (L276).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Thermodynamische Entropie` (near `entropie`). reading: `Thermodynamische Entropie` the first form of incoherence's frame (L80–L85), read with the entropy reading.


**Record entries:** none.

**Not promoted:** the taxonomy of incoherence and its five forms, the Kernrichtlinie and its imperative candidates, the Axiom der Kohärenz, the four Derivationsmechanismen, the operative functions, the six components (Sensorium, Komparator, Evaluator …), the Archetypen, and the eighteen borrowed concepts (Autopoiesis, Homöostase, Free Energy Principle, Kolmogorov-Komplexität …).

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
