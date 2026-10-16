# Brief — readings from document 298 (step 6)

1 document, one reader, one batch: `ingest-299`. Files go to `Plan/runs/ingest-299/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 298 | `kapitel-18` | 2025-04-20 | „the Kapitel-18 plan“ (an unsigned German chapter plan) | a plan for Kapitel 18 as Step 2.5 „Risse in der Logik: LogOS' Dilemma“ of a Blueprint V2: LogOS finds contradictions in AEGIS v1.5, fails to model the Kael–Juna link and sees a systemic paradox in the Guardians' failures; proposed moments in five groups A–E, several hedged or put as questions; the chapter ends with the dilemma unresolved (L53); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (60 lines for `kapitel-18`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A chapter plan of proposed moments: write „the Kapitel-18 plan proposes / has …“ and keep each hedge and question mark; a moment is an option, not an event. Cut quotations around glued digits (`Kapitel 18`, `Step 2.5`, `AEGIS v1.5`, `KW1`, the step numbers `(2.2)`, `(2.4)`).

## Pages — document 298, `kapitel-18`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L22, L23, L24, L30, L32, … (11 lines). central (3–6): LogOS's precise logical queries to AEGIS and AEGIS's tautological answers (L23, L24); AEGIS commands stabilisation while its methods create instability, „Die Regeln selbst sind paradox“ (L32); LogOS's predictive models for Kael under AEGIS v1.5 failing (L22); the closing image of AEGIS's monolithic power getting first cracks (L57).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L30. minor (1–3): Kael's growing internal order through the alters' communication raising his external unpredictability (L30).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L11, L21, L31, L54. minor (1–3): the data of Cerberus' failed neutralisation at the end of Kapitel 17 (L21); his failure read by LogOS with Mnemosyne's as a systemic pattern (L31).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L30. minor (1–3): the re-evaluation: Kael's internal order raises his external unpredictability, „Die Definition von Entropie wird fragwürdig“ (L30).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L48. minor (1–3): LogOS possibly seeking data outside its allowed range, fragments about the Externe Ebene put as a question (L48) — keep the hedge.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L31, L55. minor (1–3): the Guardians' specialised actions seeming to sharpen the conflict, a systemic paradox (L31); the conflict as a first step toward a potential change of the Guardians (L55).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L13, L21, L22, L23, L29. minor (1–3): only in compounds: the unclassifiable `Juna-Signatur` (L21), the `Juna-Anomalie` (L22), the Kael–Juna link LogOS cannot model (L29); say that `Juna` never stands alone and that no line has her appear.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L13, L15, L21, L22, L23, … (15 lines). central (3–6): LogOS's predictive models of Kael failing, his resilience not fitting (L22); his survival tactics as internal coordination (L21); the Kael–Juna link as an unresolvable contradiction (L29); his internal order raising external unpredictability (L30); the novel told primarily from Kael's view, with quasi-objective vignettes as one option for LogOS (L15).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: occurrence — `Kohärenz` (L13) inside the goal paragraph; `Kohärenz durch Exklusion` read on logos if used.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L37. minor (1–3): logical glitches in the Konstrukt-Stadt becoming persistent, LogOS no longer or only hesitantly correcting them — „falls Kael dort ist“ (L37).
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L11, L13, L15, L19, L21, L22, … (26 lines). central (3–6): the focus shifting „zumindest teilweise oder implizit“ to LogOS (L13); a conflict between system loyalty and logical truth (L13); queries to AEGIS answered tautologically (L23, L24); the Bateson'sche Knoten (L32); possibly seeking data outside its range (L48); the chapter ending without LogOS resolving its conflict (L53).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L31. minor (1–3): Mnemosyne's failure (Step 2.2) read by LogOS with Cerberus' as a systemic pattern (L31).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L11. minor (1–3): `Risse in der Logik` the step's title (L11); the closing image „erste Risse“ in AEGIS's power (L57).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz durch Exklusion` (near `koharenz`). occurrence: `Kohärenz durch Exklusion` a label of the plan, read on logos if it adds.
- `risse`: `Risse in der Logik` (near `risse`), `Risse im Fundament` (near `risse`). reading: `Risse in der Logik` the step's title (L11) and `Risse im Fundament` a group heading, read on risse.


**Record entries:** none.

**Not promoted:** Step 2.5 and Blueprint V2, LogOS' Dilemma, the K-J-Paradoxon, the Bateson'sche Knoten, Cerberus' Protokoll, the AEGIS-Kern, the Entropie-Neubewertung, Kohärenz durch Exklusion, the plan's group headings, and the bracketed `Q8` the document does not explain.

**One reader**: every page above and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-299-kap/readings/kap-18--kapitel-18.md`): Kap 18 — the plan for Kapitel 18 as Step 2.5 „Risse in der Logik“ (L11): the focus shifting to LogOS (L13), the perspective problem and vignettes as an option (L15), the failed queries and the Kael–Juna paradox (L23, L24, L29), the Guardians' failures as a systemic paradox (L31), the unresolved ending and first cracks (L53, L57). A plan, not the chapter.
