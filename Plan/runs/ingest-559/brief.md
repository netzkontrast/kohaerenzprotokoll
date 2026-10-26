# Brief — readings from document 559 (step 6)

1 document, one reader, one batch: `ingest-559`. Files go to `Plan/runs/ingest-559/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 559 | `parakonsistente-logik-fuer-kohaerenz-protokoll` | 2025-04-21 | „the paraconsistency report“ | a report on paraconsistent logic for AEGIS and the four core worlds, with two scenarios and a recommendation; proposals, never canon|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (454 lines for `parakonsistente-logik-fuer-koh`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report: write „the paraconsistency report proposes …“; scenarios stay scenarios. Sentences ending in a bracketed input marker restate a request. **Never cite** L45, L153, L171, L188, L293, L383 (earlier names), nor a span with a person's name. Quote no gendered pronoun.

## Pages — document 559, `parakonsistente-logik-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L23, L147, L149, L151, L153, … (41 lines). central: scenario A, a possibly faulty paraconsistent system (L155); scenario B, classically bound (L167); the core directive reinterpreted (L165); A judged more plausible (L300).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L161, L261, L363, L402. minor: how Kael or the respective alter experiences the logics (L261).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L161, L175, L266, L292, L404. minor: the logics per world deepen the DID metaphor (L266).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L194, L204, L227, L245, L252, L262, … (10 lines). central: guardians presumably equipped with AEGIS's logic, facing foreign logics (L262); dialogue of confusion (L364).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L171. not read: the surface on L171 is an earlier name.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kael` alone on L23. minor: the Kael simulation held together by AEGIS as steward and Kael as connecting consciousness (L311); evolution to v1.5 learning from Kael (L181).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L11, L23, L147, L153, L161, L181, … (20 lines); `Kernwelt` L11, L23, L147, L153, L161, L181, … (25 lines). central: logic per core world (L194, L196, L214, L229, L247); the recommendation (L395–L398).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: L11 is the title.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L159, L169. minor: undefined states about the Potentialmeer receive the value N (L159); part of a reality that is not classical (L169).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L153, L159, L161, L173, L292. minor: cracks as regions of B or N states (L159); cracks as local ECQ events (L173).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L157. not read: `Simulation` in passing (L157).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names the worlds' guardians.
- `kael`: `Kaels` (near `kael`), `Kael-Simulation` (near `kael`). a reading: see `kael` above.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: the genitive, not the dwelling.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title phrase.
- `ueberwelt`: `Kael-Simulation` (near `simulation`). an occurrence: the simulation compound.


**Record entries:** none.

**Not promoted:** Szenario A/B, FDE, LFI, C-systems and every logic term, the logic table of the core worlds, EST, the log diction.

**One reader**: every page above.
