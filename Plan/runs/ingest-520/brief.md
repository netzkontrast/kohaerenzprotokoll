# Brief — readings from document 520 (step 6)

1 document, one reader, one batch: `ingest-520`. Files go to `Plan/runs/ingest-520/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 520 | `dramatica-storyform-kohaerenz-protokoll-analyse` | 2026-01-02 | „the storyform exegesis“ (an unsigned German expert report) | applies the Dramatica storyform, the Dual Kernel Theory and TSDP to the novel: throughlines (L82–L86), problem and solution, Juna and Das Fundament as operators, a critique of the 39-part mosaic, three open questions; it calls itself a definitive exegesis (L11) and the novel an architectural masterpiece (L151), claims recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (206 lines for `dramatica-storyform-kohaerenz-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis: write „the storyform exegesis assigns/reads …“. Its Dramatica values are its proposal, never the project's storyform (`Plan/storyform/`). Physicists and mathematicians are named on several lines and concepts are named after people (L46, L101, the gambit at L97/L106): never write a name, never quote a span containing one — cut before. No gendered pronoun for Kael, Juna, AEGIS or the parts in our own prose; quotations stay verbatim (the document writes „Er“, „Sie“).

## Pages — document 520, `dramatica-storyform-kohaerenz-protokoll-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L34, L46, L52, L60, L67, … (19 lines). central (4–8): „System AEGIS“, the objective, rigid control structure acting as antagonist and Influence Character (L24); in the throughline table AEGIS (and Juna/V) in Universe, the status quo of the simulation, „Gott der Maschine“ (L85); the OS problem Control, AEGIS trying to eliminate all entropy and producing more instability (L101 — cut before the named demon); the IC problem Faith, believing blindly in its own protocols (L103); the open question whether AEGIS, as a feeling system, has a right to exist (L147).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L68. minor (1–4): the discourse of functional multiplicity versus fusion in DIS therapy, a cooperative coexistence of the parts (L68), as it speaks of the alters.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L187. not read: an occurrence — `DID` in a reference title (L187).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L42, L52. minor (1–4): the Dual Kernel Theory as the census lists it (L42, L52 — name-free spans only).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L102. not read: an occurrence (L102).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L36. not read: an occurrence — read on aegis (L101).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L171. not read: an occurrence — a reference title (L171).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L97, L106. not read: the page's term carries a person's name; under the project's privacy rule no reading is written onto it from this document.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L25, L56, L60, L85, L86, L108, … (11 lines). central (4–8): „Die Anomalie (Juna/V)“, a catalyst introducing non-algorithmic data — resonance and emotion — into the closed system (L25); in the throughline table with AEGIS as Influence Character (L85) and the Relationship Story with Kael, the Moonshine Link (L86); more than a love interest, „ein struktureller Operator im System“ (L112); its nature deliberately vague — external entity, aspect of Kael, principle of connectedness — a glitch evading classification (L114).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L36, L56, L66, L84, L85, … (18 lines). central (4–8): „System Kael“ as Main Character in Mind (Fixed Attitude), stuck in trauma, amnesia and fear of remembering (L84); Kael as a living paradox whose existence forces AEGIS into a state it cannot resolve (L106 — quote only the name-free span from „Kael präsentiert sich“); approaching integration, resonating more with Das Fundament (L124).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence — the title.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L66. minor (1–4): Lex named among the agents of the system (L66 — check).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine Link` L60, L86, L115. minor (1–4): the Relationship Story, „The Moonshine Link“: a psychological game of resonance, gaslighting and mutual transformation between Kael and Juna (L86).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L62, L68. minor (1–4): „Funktionale Multiplizität“ as the census lists it (L62, L68).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L50. minor (1–4): K0 as the realm of irreversible erasure; in the novel K0 is „das „Nichts Rauschen““ — not empty but full of potential (L50 — cut around inner quotes and before any physicist's name).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L66. minor (1–4): Nyx named among the agents of the system (L66 — check).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L36. minor (1–4): the second kernel K0, the emotional part, manifesting in the simulation as „Risse“, entropy and the „Nothing Noise“ (L36 — quote name-free spans).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L17, L34, L62, L64, L116, … (7 lines). minor (1–4): tertiary dissociation (DIS) as several ANPs and several EPs (L66); TSDP lines as the census lists them (read two).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L28. not read: an occurrence — `Simulation` in the introduction (L28); the simulation's status quo is read on aegis.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Die Anomalie` (near `mustererkennunganomaliedetektion`). read on juna (above): `Die Anomalie` names Juna/V (L25).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Prime` (near `koharenz`). an occurrence: the title and `Kohärenz-Prime`, not read.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). an occurrence: `Mosaik` is the 39-part mosaic structure, not the page's term.


**Record entries:** none.

**No chapter readings**: no chapter is named (`Kapitel` 0; the 39 parts are discussed as a mosaic, L126–L139).

**Not promoted:** the Dramatica values as surfaces, Seltsamer Attraktor, Diagonale Opposition, Kohärenz-Prime, Das Fundament as an operator, the three open questions, and the concepts named after people.

**One reader**: every page above.
