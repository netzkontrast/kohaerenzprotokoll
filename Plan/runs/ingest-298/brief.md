# Brief — readings from document 297 (step 6)

1 document, one reader, one batch: `ingest-298`. Files go to `Plan/runs/ingest-298/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 297 | `kapitel-17` | 2025-04-20 | „the Kapitel-17 plan“ (an unsigned German chapter plan) | a plan for Kapitel 17 as Step 2.4 of a blueprint: AEGIS v1.5 rates Kael's inner organisation as a threat and gives Cerberus wider powers; proposed moments in six groups A–F, hedged (`möglicherweise`, `vielleicht`, `könnte`); Kapitel 16 as Step 2.3 and LogOS hesitating in Step 2.5 (L11, L62); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (65 lines for `kapitel-17`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A chapter plan of proposed moments: write „the Kapitel-17 plan proposes / has … possibly …“ and keep each hedge; a moment is an option, not an event. Cut quotations around glued digits (`Kapitel 17`, `Step 2.4`, `AEGIS v1.5`, `KW3`).

## Pages — document 297, `kapitel-17`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L13, L47. minor (1–3): AEGIS (v1.5) rates Kael's growing inner organisation as a raised threat (L13); the brutality shows how far AEGIS will go to enforce its definition of coherence, even destroying parts of the system or Kael (L47).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L36, L54. minor (1–3): Kael (Host) consciously calls on specific alters (L36); the vulnerable traumatised or childlike parts (L38); the plan's named alters — Index, Praetor, Limina, Silas, Echo, Flicker, Nox — in their proposed roles (L37–L40).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L11, L13, L20, L22, L23, L28, … (15 lines). central (3–6): the warden of the Schattenlabyrinth with extended powers (L13); returning changed, possibly with defence drones or shadow constructs (L22); possibly a new directive (L23); escalated yet still a defence protocol (L46); his influence possibly beyond KW3, or Kael forced back there (L20, L21).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L13, L32. minor (1–3): only in the compounds `Juna-Fokussierung` (L13) and `Juna-Spur-Ort` (L32): say what each line plans and that `Juna` never stands alone.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L13, L19, L20, L21, L23, … (24 lines). central (3–6): the target of the escalated hunt (L13); falling back on his newly established inner coordination (L13); calling as host on specific alters (L36); Index analysing a trap, a manager alter protecting (L37, L38).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L47. not read: occurrence — `Kohärenz` (L47) is AEGIS's definition it enforces, read on aegis.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L62. minor (1–3): LogOS hesitating, pointing to Step 2.5 (L62).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L38, L53. minor (1–3): Silas named with Limina, set as a question, as a possible protector (L38); L53 only if it adds.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L45. not read: occurrence — `Simulation` (L45) is the possible damage laying bare deeper layers of the simulation; a hedged option, read on the chapter page.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` names a vulnerable part (L38), read on alters.


**Record entries:** none.

**Not promoted:** the Steps 2.3–2.5 and Blueprint V2, the Schattenlabyrinth, KW3, System-Alarmstufe Rot, the Abwehrdrohnen and Schattenkonstrukte, Cerberus 2.0, the Manager-Alter, Praetor, Index, Limina, Flicker, Nox, and the plan's group headings.

**One reader**: every page above and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-298-kap/readings/kap-17--kapitel-17.md`): Kap 17 — the plan for Kapitel 17 as Step 2.4 after Kapitel 16 as Step 2.3 (L11): Cerberus' escalation against Kael under AEGIS v1.5 (L13); the six groups of proposed moments (L17–L58), the open place of the hunt (L20, L21), the visible destruction (L45), the open ending and LogOS's hesitation pointing to Step 2.5 (L62). A plan, not the chapter.
