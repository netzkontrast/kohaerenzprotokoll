# Brief — readings from document 512 (step 6)

1 document, one reader, one batch: `ingest-512`. Files go to `Plan/runs/ingest-512/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 512 | `spannungsfelder-und-aegis-meta-framework-analyse-docx` | 2025-06-03 | „the tension-fields analysis" (an unsigned German analysis) | an outside analysis of thirteen proposed tension fields and of an „AEGIS Meta-Framework“, a self-organising structure meant to secure its own existence (L292); it names no figure, place or chapter of the novel (Kael, Juna, Roman each 0) and judges the framework coherent but circular and too abstract; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (521 lines for `spannungsfelder-und-aegis-meta`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: the analysis treats an abstract meta-framework that bears the name AEGIS and names nothing of the novel; nothing it says is a reading of the novel's AEGIS.

## Pages — document 512, `spannungsfelder-und-aegis-meta-framework-analyse-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L17, L19, L34, L35, L36, … (55 lines). not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L15, L19, L27, L34, L36, L37, … (29 lines). not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L51. not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L297, L298. not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L191. not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L203. not read: light pass — the analysis's abstract AEGIS meta-framework and its own general use, not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Energie und Entropie` (near `entropie`). an occurrence: the meta-framework's own vocabulary, light pass.
- `grosse-mauer`: `Systemgrenzen und Selbstorganisation` (near `systemgrenze`). an occurrence: the meta-framework's own vocabulary, light pass.
- `kohaerenz`: `Fluktuationskohärenz` (near `koharenz`), `Spannungskohärenz` (near `koharenz`). an occurrence: the meta-framework's own vocabulary, light pass.
- `realitaetsebenen`: `Verschachtelte Realitätsebenen` (near `realitatsebene`), `Verschachtelte Realitätsebenen` (near `realitatsebenen`). an occurrence: the meta-framework's own vocabulary, light pass.
- `ueberwelt`: `Layered Simulations / Nested Worlds` (near `simulation`). an occurrence: the meta-framework's own vocabulary, light pass.


**Record entries:** none.

**Not promoted:** the thirteen tension fields, the meta-framework's dimensions, axes and five operative rules, Koheränz der Emergenz, the schema AEGIS(t), and the borrowed concepts (several named after people).

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
