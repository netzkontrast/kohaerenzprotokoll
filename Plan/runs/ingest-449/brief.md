# Brief — readings from document 449 (step 6)

1 document, one reader, one batch: `ingest-449`. Files go to `Plan/runs/ingest-449/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 449 | `kohaerenz-direktive-narratives-protokoll` | 2026-02-25 | „the narrative directive“ (an unsigned German writing directive, „Narratives Kohärenz-Protokoll“) | sets three physics-based plot mechanics and three narrative levels, each with a „Fixe Regel“ or language rules, and a four-item scene checklist; instructions to the writer, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (94 lines for `kohaerenz-direktive-narratives`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A directive: write „the narrative directive prescribes …“ — its „Fixe Regel“ lines are its own rules, never canon. Quote the German as written; cut before bold markers and inner „…“. No gendered pronoun for Kael, Juna, AEGIS or LogOS — use the names (quotations verbatim, including the document's „sie“ and „er“). Never write a real person's name nor a term carrying one (L17, L22, L28, L36, L91 carry names: describe, never quote those spans).

## Pages — document 449, `kohaerenz-direktive-narratives-protokoll`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L25, L42, L90. minor (1–4): deleting Kael's traumatic memories (Juna) is a physical act for AEGIS (L25); Ebene 1, the Konstrukt-Stadt, stands for order / AEGIS (L42); the checklist asks how AEGIS reacts (L90).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L17, L32, L56. minor (1–4): the levels: Ebene 2, the Grenz-Zonen, stands for entropy / dissociation (L56); LogOS can measure only Juna's effects, entropy (L32).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L31. minor (1–4): the Wächter (Guardians) cannot see Juna because Juna lies outside their axiomatic base; for them a „Syntaxfehler“ (L31 — quote around the inner quotes).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L25, L31, L32, L70. minor (1–4): the memories AEGIS tries to delete are named Juna (L25); the Guardians cannot see Juna (L31); LogOS may never understand Juna directly (L32); Ebene 3, the Resonanz-Kontinuum, stands for transcendence / Juna (L70).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L25, L26, L37, L64, L89. minor (1–4): scenes in which Kael forgets or parts split off must be described by heat, melting or thermal flicker (L26 — describe around the bold); Kael's deepest trauma as the event horizon of the mind, nothing lost (L37); synaesthesia when Kael's system is partitioned (L64); the checklist asks from which Alter Kael writes (L89).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — L11 is the title.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L42. minor (1–4): Ebene 1: the Konstrukt-Stadt as order / AEGIS (L42), atmosphere sterile, cold, overexposed (L44), no metaphors (L45), the horror of absolute predictability (L54).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L32. minor (1–4): the rule that LogOS may never understand Juna directly and can only measure the effects (L32).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L17. not read: an occurrence — `Simulation` on L17 is the simulation the story is set in, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter` (near `alters`). a reading: `Alter` on L89 — read on alters (see below).
- `dkt`: `Theorie` (near `dualkerneltheoriedkt`). an occurrence: `Theorie` is the label of each mechanic.
- `kohaerenz`: `Narratives Kohärenz-Protokoll` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Checkliste` (near `koharenz`), `Stilistische Kohärenz` (near `koharenz`), `Inhaltliche Kohärenz` (near `koharenz`). an occurrence: the directive's title and its section labels.
- `residual-echos`: `Echos` (near `residualechos`). an occurrence: `Echos` on L38 is a kind of radiation at the edge of reality, not the residual echoes.


**Pages beyond the draft:**
- **`alters`** (minor, 1–2): the checklist asks from which identity (Alter) Kael writes: the manager uses technical terms, the child emotional fragments, the gatekeeper barrier metaphors (L89).

**Record entries:** none.

**No chapter readings**: the directive names no chapter.

**Not promoted:** Thermodynamik der Verdrängung, the incompleteness prison and the black-hole trauma (their names carry real names), Grenz-Zonen, Resonanz-Kontinuum, Fixe Regel, Kohärenz-Checkliste, Manager, Kind, Gatekeeper, and the borrowed concepts.

**One reader**: every page above.
