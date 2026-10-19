# Brief — readings from document 557 (step 6)

1 document, one reader, one batch: `ingest-557`. Files go to `Plan/runs/ingest-557/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 557 | `p-vs-np-und-kohaerenz` | 2025-04-21 | „the complexity report“ | a report that applies P vs NP to AEGIS and the four core worlds and recommends how to use it in the plot, all in the conditional; its self-praise recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (530 lines for `p-vs-np-und-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report: write „the complexity report proposes …“; its conditionals stay conditionals; never canon. Sentences ending in a bracketed input marker restate a request, not the report. **Never cite L212 or L220** (earlier names). Quote no gendered pronoun.

## Pages — document 557, `p-vs-np-und-kohaerenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L19, L21, L25, L29, L148, … (50 lines). central: an advanced system keeping order (L21); a P-machine in an NP-world (L230); a degraded mode (L205); a fight against complexity itself (L328).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L276, L286, L344, L380, L390. minor: the Wächter guardian of KW3 (L276), relying on fast but inexact heuristics (L286).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L21, L29, L181, L183, L185, L186, … (8 lines). minor: predicting entropy as a hard task (L186).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L236, L358, L389, L390. minor: each guardian mirrors its world's computational limits (L390).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L212, L220, L236, L243, L260, L285, … (19 lines). central: Kael as a non-deterministic solver, headed as a question (L402); intuitive solutions AEGIS cannot compute (L389); Kael's experience per world, all conditional (L243).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L11, L19, L21, L25, L185, L234, … (17 lines). central: four core worlds (L21, L236); KW1–KW4 mapped to complexity classes (L238, L246, L263, L288).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L13, L19, L21, L25, L29, … (26 lines). central: producing global coherence as an NP-hard goal (L189, L214).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L152, L204. minor: cracks as the consequence of heuristics (L204).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L21, L185. minor: global coherence over the Überwelt and all core worlds (L185).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names the worlds' guardians, not the integrity guardian.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Architekt` is KW1's guardian.
- `potentialmeer`: `Potential` (near `potentialmeer`). an occurrence: `Potential` is KW4's label.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` is KW2's guardian.


**Record entries:** none.

**Not promoted:** KW1–KW4 as complexity worlds, the P-machine, degraded mode, RIVE, SARM, EST, Reboot, the K-J connection, the hybrid approach, every complexity-theory term.

**One reader**: every page above.
