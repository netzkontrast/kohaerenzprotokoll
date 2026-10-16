# Brief — readings from document 513 (step 6)

1 document, one reader, one batch: `ingest-513`. Files go to `Plan/runs/ingest-513/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 513 | `kohaerenz-protokoll-agentive-narrative` | 2025-07-03 | „the agentive-narrative architecture report“ (an unsigned German report) | an architecture for an interactive, agent-driven version of the story: four layers (Kael, AEGIS, Juna/V, Das Fundament) mapped to Dramatica storyforms (L55–L62), a JSON schema, a prompt cascade, a symbolic overseer, storage, a UI and a build plan; it answers an earlier brief and calls its schema the single source of truth for its system (L132); a design proposal, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (671 lines for `kohaerenz-protokoll-agentive-n`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design proposal for software: write „the agentive-narrative report models/proposes …“. Its state variables and UI modes are its own design, never the novel's facts; its quotations of „the brief“ are the earlier brief's phrases as the report reports them. Theory names after real people stand on several lines (L82, L84, L104, L115): never write or quote them. No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim (the document writes „ihren“ for AEGIS).

## Pages — document 513, `kohaerenz-protokoll-agentive-narrative`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L57, L88, L92, L94, L104, L178, … (12 lines). central (4–8): AEGIS as the „Logisch-Systemische Ebene“ of four layers (L57); the brief's „traumatisierten Wächter-KI“ modelled as deep systemic and logical damage, since a non-biological entity cannot have trauma in the human sense (L92); the Dramatica table's solution for AEGIS, giving up belief in its faulty directives (L62); the state variable `AEGIS.protocolAdherence`, how rigidly AEGIS holds to its faulty core protocols (L302).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L62. not read: an occurrence — a cell of the Dramatica table (L62).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L57, L98, L102, L104, L105, L179, … (9 lines). minor (1–4): Juna/V as the „Ontologische Ebene“ (L57); the brief's „transzendente, resonanzbasierte Kraft“, an intervention not by direct physical causality (L102 — cut before the theory names); `JunaV.resonanceFrequency`, the narrative theme Juna/V amplifies (L303); the table's solution for Juna/V, delay as a valid option (L62).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L57, L76, L80, L82, L94, L104, … (16 lines). central (4–8): Kael as the „Psychologische Ebene“ (L57); Kael's story as the brief's „Heilungsreise eines fragmentierten Bewusstseins“, mapped onto therapeutic models (L80); the table's solution for Kael, accepting one's worth as inherent (L62); the state variable `Kael.integrationProgress`, 0.0 total fragmentation to 1.0 full healing (L299).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L525. minor (1–4): the four layers as the report's „vier Realitätsebenen“, each given its own UI (L525).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L435. not read: an occurrence — `Simulation` of automated play-throughs (L435).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the project name.


**Record entries:** none.

**No chapter readings**: `Kap` 0, `Kapitel` 0.

**Not promoted:** NCP, the state variables, interferenceRules, the prompt cascade, the dramaturgic overseer (Aufseher), Das Fundament as a layer, the UI modes, the build phases, and the borrowed concepts (several named after people).

**One reader**: aegis, kael, juna, realitaetsebenen.
