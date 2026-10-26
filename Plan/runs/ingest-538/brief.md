# Brief — readings from document 538 (step 6)

1 document, one reader, one batch: `ingest-538`. Files go to `Plan/runs/ingest-538/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 538 | `kohaerenz-protokoll-plot-entwurf` | 2025-04-20 | „the plot draft (blueprint)“ | a German blueprint: answers to numbered core questions on the world, AEGIS, Kael and the Guardians, then 39 steps in three parts, written out only in part („exemplarische Darstellung“), and a synthesis; it calls itself the final conceptual development order and „ultimativer Leitfaden“ (L15 — barred, not cited); its own claim, recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (483 lines for `kohaerenz-protokoll-plot-entwu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the plot draft proposes …“; never canon. **Never cite these lines (an earlier name): 15,23,27,31,33,35,37,39,41,56,69,89,133,148,201,234,241,255,296,325,327,426,432,458,475.** Never write the bond partner's name; never put Juna's name on what the draft says of the partner. `K-J-…` compounds are not glossed. No gendered pronoun for Kael, AEGIS or the Guardians in our own prose; quotations stay verbatim, cut before pronouns where possible.

## Pages — document 538, `kohaerenz-protokoll-plot-entwurf`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L27, L29, L31, L33, L37, … (112 lines); `Entropic Gatekeeper` L440. central: purpose „reine Selbsterhaltung“ (L462, L97); arc from „Entropic Gatekeeper“ (L440) to being overtaken, not destroyed (L442); a reset to an earlier stable state (L75); its sensors register exploding anomalies (L58).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Cognitive Firewall` L63, L68. minor: the „Cognitive Firewall“ as AEGIS's perception filter beside OBP v1.5 (L63, L68).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L239. minor: a dissociative switch to an Alter (L199); the first conscious meeting with an Alter as a separate entity (L225, L227); a mirror letting Kael see through another Alter's eyes (L239).
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L15, L27, L112, L193, L200, L201, … (10 lines). minor: Kael's DID as the starting point (L200, L193); the instruments grow from facing the DID (L112); from an unconscious DID to functional multiplicity (L420, L460).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L29, L32, L33, L45, L60, L82, … (14 lines). minor: AEGIS's dualistic logic Kohärenz vs. Entropie (L45); AEGIS identifies Kael as the source of the „Entropie-Infektion“ (L268).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L113, L136, L138, L140, L141, L142, … (22 lines). minor: possibly give implicit tools (L113); their change, catalysed by watching Kael's resilience and AEGIS's failure (L136, L140); begin to split (L287); the renegades support Kael's integration (L311, L312); from agents to potentially autonomous beings (L446).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L31. not read: the bond partner is named only by an earlier name (L31).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L27, L31, L37, L39, … (118 lines). central: the instruments as inner abilities (L105); loneliness after integration into functional multiplicity (L129); the first switch in the Überwelt (L199); in a Kernwelt meeting an Alter (L225); full integration with the renegade Guardians (L311); the arc (L420, L422); the search for Gleichzeitigkeit beyond self-preservation (L97, L462).
- **`kael-julia-bindung`** (minor, 1–4): the census's surfaces — `K-J-Bindung` L32, L45, L48, L133. not read: the page awaits renaming under decision 028; nothing is added to it.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L15, L39, L41, L56, L58, L61, … (22 lines); `Kernwelt` L15, L39, L41, L56, L58, L61, … (29 lines). minor: anomalies and structure deletions in the Kernwelten (L58); a bizarre symbolic landscape representing a dominant part (L225); the first instrument found in a Kernwelt (L239); representations of Kael's fragments (L472).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title (L11) (J9).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L50, L325, L326, L422. minor: Gleichzeitigkeit as the next step after functional multiplicity (L50); loneliness after it (L129); Kael reaches it (L422); from DID to functional multiplicity (L460).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L25, L45, L49, L50, L155, … (16 lines). minor: Kohärenz-Inseln as transient zones of order in it (L25); Gleichzeitigkeit in or beyond it (L45); the final journey there (L155); origin and goal, beyond AEGIS's order (L470).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L15. not read: on a barred line (L15).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Glitches` L41, L58, L234, L241; `Risse` L41, L61, L150, L256, L287, L291, … (8 lines). minor: „Glitches“ among the anomalies (L58); „Risse“ in the Überwelt's reality (L61); massive visible cracks (L256); a hiding place in the cracks (L311); the Potentialmeer felt through them (L470).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L15, L41, L61, L75, L132, L150, … (33 lines). minor: its structural instability (L61); Kael's seemingly normal life there (L199, L200); its decay (L268, L277); AEGIS's constructed, controlled but vulnerable domain (L471).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter` (near `alters`). a reading — read on alters above.
- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`), `System-Dekohärenz` (near `koharenz`), `qualitative Kohärenz` (near `koharenz`). occurrences: Kohärenz-Inseln, System-Dekohärenz, qualitative Kohärenz and the title (J9).


**Chapter readings:** none — steps, not `Kap`.

**Record entries:** none.

**Not promoted:** Kohärenz-Insel(n), K-J compounds, Gleichzeitigkeit, Instrumente der Ordnung, PMAS, RIVE, SARM, OBP and their v1.5 forms, Entropie-Infektion, Welle von Unmöglichkeit, Einsamkeit, Zweck, Entropic Gatekeeper.

**One reader**: every page above.
