# Brief — readings from document 454 (step 6)

1 document, one reader, one batch: `ingest-454`. Files go to `Plan/runs/ingest-454/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 454 | `monstergruppe-kohaerenz-protokoll-fundament` | 2025-04-23 | „the Monster-group foundation report“ (an unsigned German research report with English headings, „Forschungsbericht: Die Monstergruppe als Inspirationsquelle“) | reports the group's mathematics and physics from its references, then reads the Kael-Juna connection as a Kohärenz-Insel (KJ/KI) modelled on the group, set against AEGIS's coherence by demarcation, and closes with conditional narrative proposals; it calls the group „ein tragender konzeptioneller Pfeiler“ (L266), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (303 lines for `monstergruppe-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report: write „the Monster-group foundation report proposes …“; its mathematics (L23–L155) is reported from references and stays off the pages; its Section VII proposals are conditionals („Szenen könnten zeigen“). No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim). Never write a real person's name nor quote a span containing one; cut before glued reference numbers and inner „…“.

## Pages — document 454, `monstergruppe-kohaerenz-protokoll-fundament`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L21, L43, L51, … (46 lines). central (4–8): AEGIS as an entity or system whose existence and order rest on demarcation, classification, control and exclusion (L17); order by defining borders and excluding incoherence (L194); its methods presumably modelling, simulation and reduction (L51 — hedged); AEGIS must read the KJ/KI as maximal disorder, noise or entropy (L218); an unresolvable paradox (L224), neither containable nor predictable (L225), the maximal threat (L226); a fundamental ontological blindness (L235).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. minor (1–4): AEGIS must interpret the KJ/KI as maximal disorder, noise or information-theoretic entropy (L218).
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L250. minor (1–4): Section VII proposes scenes in which AEGIS sets specialised Analyse-Guardians on the KJ/KI and they fail (L250 — conditional).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L119, L121, L159, L169, L171, … (13 lines). central (4–8): the same connection from Juna's side: KJ/KI as the integrative structure (L15, L159); acausal from AEGIS's view (L119); Moonshine as the connection's metaphor (L171).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L119, L121, L159, L169, L171, … (13 lines). central (4–8): the Kael-Juna connection / Kohärenz-Insel as a central, integrative structure in the novel's universe (L15, L159); from AEGIS's side the connection seems acausal, inexplicable or protocol-violating (L119); Moonshine as the primary metaphor of the Kael-Juna connection (L171); the resonance appears to AEGIS as noise (L175).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title and the document's own Kohärenz-Insel.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L250. minor (1–4): LogOS named once, as one such analysis Guardian („wie LogOS oder ähnliche Instanzen“, L250), with no definition.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L21, L163, L177, L179, L181, L183, … (9 lines). minor (1–4): the KJ/KI no generic fluctuation in the Potentialmeer (L163) but a rare, stable island of order; within the novel's concept of the Leere or Potentialmeer it could be an emergent configuration (L179); a third possibility against chaos and AEGIS (L181).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L51. not read: an occurrence — `Simulation` on L51 is an analysis method.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `guardians`: `Analyse-Guardians` (near `guardians`). `Analyse-Guardians` read on guardians (L250).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kael-Juna-Verbindung / Kohärenz-Insel` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`), `Kohärenz durch Abgrenzung` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). an occurrence: the protocol's name and the document's own Kohärenz-Insel.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading: Moonshine as the metaphor of the Kael-Juna connection — read on moonshine-link (below).


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–3): Monstrous Moonshine as the primary metaphor of the Kael-Juna connection (L171); its sub-protocol resonance appears to AEGIS as acausal noise (L175).

**Record entries** (one file, formatted as earlier entries):
- **`q1-guardians-and-aegis`**: the foundation report proposes specialised Analyse-Guardians, such as LogOS, that AEGIS sets on the KJ/KI and that report to higher AEGIS instances (L250 — conditional); recorded.

**No chapter readings**: the report names no chapter.

**Not promoted:** Kohärenz-Insel, KJ/KI, Sein / Kohärenz durch Abgrenzung, Kohärenz durch Integration, Happy Family, Classification / Reductionism Failure, Protocol Violation, EST, and the mathematical and physical concepts (several carry people's names).

**One reader**: every page above and the record entry.
