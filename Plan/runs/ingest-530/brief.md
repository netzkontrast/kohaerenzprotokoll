# Brief — readings from document 530 (step 6)

1 document, one reader, one batch: `ingest-530`. Files go to `Plan/runs/ingest-530/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 530 | `roman-pitch-reduktion-auf-kern` | 2026-03-31 | „the pitch reduction“ (an unsigned German report) | inventories the project's documents, names the narrative core, compares it with published works and proposes a reduced pitch, a cut list and four recommendations; it calls the DKT the project's strongest worldbuilding element (L51), a judgement recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (158 lines for `roman-pitch-reduktion-auf-kern`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A critique that proposes: write „the pitch reduction proposes/judges …“; its reduced pitch (L81–L85) and cut list (L98–L102) are proposals, never canon. **Never cite L15, L28, L41, L118's „Methodischer Rat“ span or L124** (personal material about a person's work, and earlier names). Lines L38, L53, L59, L69, L71, L99 and L101 name real people or concepts named after them: quote only name-free spans, or none. Never write a figure's earlier name, a real person's name or a concept named after a person; write nothing for goedel-gambit. No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim but cut before „er“/„seiner“ where possible.

## Pages — document 530, `roman-pitch-reduktion-auf-kern`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L51, L53, L59, L69, L81, … (13 lines). central (3–8): the reduced pitch: the Konstrukt-Stadt controlled by AEGIS, an AI under one axiom, „Wahre Ordnung existiert nur dort, wo jeder Widerspruch und jedes Rauschen rigoros eliminiert werden.“ (L81); it should stay „eine kalte, unergründliche Naturgewalt der Logik“ (L69 — that span only); embodying the Kohärenz-Kernel (L51); every attempt by AEGIS to erase a traumatic memory releasing heat (L53 — name-free span only).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L33, L101. minor (1–4): listed in the corpus inventory for the plot-development document (L33) and in the cut list (L101 — name-free span only, or the L33 row alone).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L28. not read: L28 names earlier names.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L13, L29, L51. minor (1–4): the DKT not to be cut but strengthened as metaphor, „das stärkste Worldbuilding-Element des Projekts“ (L51); listed in the inventory (L29).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L39. minor (1–4): „Zielkohärenz durch Akzeptanz der Entropie“ as the resolution of the final chapter in the inventory (L39).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Gödel-Gambit` alone on L38. not read: the page's term carries a person's name; under the project's privacy rule no reading is written onto it from this document.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L28. not read: L28 names earlier names.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L28, L41, L43, L53, L57, … (11 lines). central (3–8): „das exilierte Ursprungs-Ich“, an anomaly in Kael that escapes AEGIS's algorithmic capture (L85 — quote spans before the pronouns); „das leidende, exilierte Zentrum von Kaels Menschlichkeit“ (L122); the bond with Kael to remain an undefinable blind spot for AEGIS (L98, name-free span), the cut list judging the mathematical explanation of the bond as destroying closeness (L57, L98). Never cite L28 or L41.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L28, L34, L43, L51, L53, … (22 lines). central (3–8): wakes without memory in the Konstrukt-Stadt (L81); Kael's ANPs as rational and EPs as emotional parts (L51); the body as a lie detector against the simulation (L53, name-free span); the cut list's „lebendes Paradoxon“ as the climax, not to be made to quote theorems (L101 — only „Kael als „lebendes Paradoxon“ zu inszenieren, ist der brillante Höhepunkt“); not an omniscient administrator (L118, before „Methodischer Rat“). Never cite L15, L28, L41.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L34, L71; `Kernwelt` L34, L71, L118. minor (1–4): „Kernwelten als Psycho-Architektur“ in the inventory (L34); L71 and L118 as the census lists them — name-free spans only.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L13, L51. minor (1–4): the Kohärenz-Kernel as the DKT's coherence side, embodied by AEGIS (L13, L51).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L13, L51. minor (1–4): the Kollaps-Kernel as the DKT's collapse side (L13, L51).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L81. minor (1–4): „einer sterilen, euklidischen Simulation, die von absoluter Stille und gleißendem Licht dominiert wird“, where Kael wakes, controlled by AEGIS (L81).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L34, L99. minor (1–4): listed in the inventory (L34); the cut list replaces the mathematical explanation of the bond (L99 — name-free span only, or L34 alone).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Das Mosaik-Herz` L39, L124, L136. minor (1–4): „Finale Kapitel 39 - Das Mosaik-Herz“ in the inventory: acceptance of entropy, physical fusion, waking in real reality (L39). Do not cite L124 or L136.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L51. minor (1–4): L51 as the census lists it — the DKT's metaphor.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L53, L59, L124. minor (1–4): Risse as heat damage to the simulated spacetime (L53, name-free span); a tangible consequence — heat, Risse, destruction (L59, name-free span).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L13, L31. minor (1–4): the implementation of TSDP, ANPs vs. EPs, in the inventory (L31); L13 as the census lists it.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L28. not read: L28 names earlier names.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). an occurrence: `Coherons` listed in the inventory (L29), not described.
- `goedel-gambit`: `Gödel-Gambits` (near `godelgambit`). an occurrence: the page's term carries a person's name; not read.
- `kohaerenz`: `Zielkohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Seelen-Kohärenz-Protokoll` (near `koharenz`), `Quantendekohärenz` (near `koharenz`). an occurrence: titles, `Zielkohärenz`, physics.
- `logos`: `Logos-Prime` (near `logos`). an occurrence: `Logos-Prime` is a Kernwelt, not the Guardian page.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). an occurrence: `Mnemosyne-Archipel` named, not described.


**Record entries:** none.

**No chapter readings**: only the final chapter's title row (L39), read on mosaik-herz; no chapter is outlined.

**Not promoted:** the corpus inventory as a list, the comparison with published works, the reduced pitch as a whole, the cut list's items, the Sensorisches Regelwerk and the Somatischer Filter, Seelen-Kohärenz-Protokoll, Blueprint V5, and the concepts named after people.

**One reader**: every page above.
