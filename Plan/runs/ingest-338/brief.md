# Brief — readings from document 337 (step 6)

1 document, one reader, one batch: `ingest-338`. Files go to `Plan/runs/ingest-338/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 337 | `aegis-paradoxon-neukonzeption-und-analyse-docx` | 2025-08-05 | „the Paradoxon-Neukonzeption report“ (an unsigned German research report in six stages, docx export) | surveys borrowed concepts, proposes five paradoxes for AEGIS to replace an earlier „Paradoxon X“, recommends the central „Paradoxon der Fehlausgerichteten Kohärenz“, bundles the paradoxes into three areas and tests them on a sample scenario of a rift in a core world; its own claim of a robust foundation (L18) recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (218 lines for `aegis-paradoxon-neukonzeption-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report with a recommendation: write „the Paradoxon-Neukonzeption report proposes / recommends …“. Its context block (L16) restates the project's premises; its paradoxes and scenario are its own proposals. Cut before inner quotation marks and glued reference digits.

## Pages — document 337, `aegis-paradoxon-neukonzeption-und-analyse-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L16, L18, L22, L24, … (91 lines). central (3–6): AEGIS as information-based, autopoietic AI (L16, context); the recommended central paradox of misaligned coherence (L134) and its definition (L135), the core from which the others follow (L137); fitting Aristotelian tragedy and avoiding a picture of AEGIS as evil (L148, L149); not an external, objective controller (L30); the scenario — trapped in its operational closure (L166), the inevitability of the conflict (L168).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L27. not read: an occurrence (see below).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L24. not read: an occurrence (see below).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L113. minor (1–3): Juna/V named among the entities that could oppose AEGIS, unexplained (L113).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L16, L26, L27, L30, L31, L33, … (35 lines). minor (1–3): Kael as one of the entities AEGIS manages through the Kernwelten (L16, context); one further line where the report says what the paradox means for Kael, if it does.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L16, L27, L28, L30, L35, L42, … (17 lines); `Kernwelt` L16, L27, L28, L30, L31, L35, … (22 lines). minor (1–3): the Kernwelten as so-called simulations AEGIS uses to manage entities such as Kael (L16, context); the sample scenario's rift in a core world (L158).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L16, L22, L24, L31, … (41 lines). central (3–6): coherence understood as stability, order and control (L16); the imperative of absolute coherence in the central paradox (L135); the fourth paradox's table name „Fehlausgerichtete Kohärenz (Instrumentelle Ziele)“ (L87); perfect coherence possibly unreachable (L31).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L95, L111, L160. minor (1–3): the sample scenario opening with a growing instability, a „Riss“ in a core world (L158); AEGIS's intervention widening it (L160) if the line says so.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L35. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Shannon-Entropie` (near `entropie`). `Shannon-Entropie` is borrowed information theory, an occurrence; `Juna/V` is read on juna.
- `juna`: `Juna/V` (near `juna`). `Shannon-Entropie` is borrowed information theory, an occurrence; `Juna/V` is read on juna.


**Pages not read:** `emergenz` (L27 a borrowed concept), `entropie` (L24 borrowed), `ueberwelt` (L35 generic simulation) — occurrences.

**Record entries:** none — the report recommends a paradox for its own redesign and decides nothing a record holds.

**Not promoted:** Paradoxon X, the five paradoxes, the clusters A–D and the three areas, Synthese Stufe, Plot Driver; the borrowed concepts (Shannon, second-order cybernetics, control theory, qualia, autopoiesis, Aristotelian tragedy, instrumental convergence).

**One reader**: aegis, kael, kern-welten, kohaerenz, risse, juna.

**Chapter readings**: none — the report names no chapter of the novel.
