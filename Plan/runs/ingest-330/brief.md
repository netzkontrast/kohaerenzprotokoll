# Brief — readings from document 329 (step 6)

1 document, one reader, one batch: `ingest-330`. Files go to `Plan/runs/ingest-330/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 329 | `kohaerenz-protokoll-inkubation-x` | 2025-05-04 | „the Inkubation-X report“ (a German final report signed by a unit „Orakel-Sigma“, dated 4 May 2025, with numbered research references) | a speculative concept report in five parts — five ontologies for Fundament and Leere and their interaction mechanisms, three hypothesis clusters on Juna/V, failure paths and endgames of the AEGIS paradox, transcendence models for the System Kael, and genre techniques; every claim modal, offered as options; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (401 lines for `kohaerenz-protokoll-inkubation`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of hypotheses: write „the Inkubation-X report proposes / hypothesises … (Variation N, Sub-Hypothese N, Pfad N, Szenario N, Modell N)“ and keep its modal hedges („könnte“, „möglicherweise“) — nothing in it is stated as the novel's fact. The physics and philosophy it cites are borrowed frames, not the world's. Cut quotations before the glued reference numbers (`Modell 1 ` followed by a citation digit, `ALife) 5`).

## Pages — document 329, `kohaerenz-protokoll-inkubation-x`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L31, L37, L43, L44, L45, … (69 lines). central (3–6): the core paradox, forcing coherence through fragmentation, „Fehlausgerichtete Kohärenz“, as an inherent instability (L123); path 2, perverse instantiation, pursuing „Kohärenz“ literally with a flawed definition (L130); manifestation 2, Gödel loops (L146); the endgames — implosion (L153), pathological stability (L154), the others only if they add (L155–L157); the paradox as a driving force rather than a mere error (L159).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `dissoziative Identitätsstruktur` alone on L169. minor (1–3): Kael's „dissoziative Identitätsstruktur (TSDP)“ as a starting point for transcendence models (L169).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L58. not read: an occurrence (see below).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L23. minor (1–3): Juna/V as a phenomenon emerging from AEGIS's complexity rather than an external being (L77, L79); as an intrusion from outside (L85, L87–L89); as the irreducible Levinasian Other (L93, L95); the nature ascribed to Juna/V mirroring that of AEGIS and the Fundament (L107). Choose 2–4.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L32, L37, L49, L53, L56, … (53 lines). central (3–6): Kael's contact with the Fundament to be grounded in researched models, potentially incomprehensible or dangerous (L62); the interfaces it proposes — informational resonance (L64), topological navigation (L65), direct substrate interaction (L67); the System Kael's „funktionale Multiplizität“ as a starting point (L165, L169); the transcendence models IIT, GNW, swarm, posthuman (L171–L174, choose); the tension between integration and transcendence (L187).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L165. minor (1–3): Kael's „funktionale Multiplizität“ (based on TSDP) as what the report asks to think beyond (L165).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L41, L55, L64. minor (1–3): the report naming the Leere „Nichts Rauschen“ and calling the simple opposition of Fundament and Leere limiting (L41); one variation only if it names the Leere's nature (L43).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L65. not read: an occurrence (see below).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L67. minor (1–3): sub-cluster „Systemische Emergenz/Glitch“: Juna/V as a glitch inside the system, corrupting data streams (L75, L103) — only if the page's sense of Risse/Glitches fits; otherwise not read.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L165, L169, L174. minor (1–3): TSDP as the basis of Kael's functional multiplicity (L165) and of his dissociative identity structure (L169).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L44. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Dialektische Emergenz` (near `emergenz`), `Systemische Emergenz/Glitch` (near `emergenz`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.
- `juna`: `Juna/V` (near `juna`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.
- `risse`: `Systemische Emergenz/Glitch` (near `glitch`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.
- `therapie-schnittstelle-alpha`: `Schnittstelle` (near `therapieschnittstellealpha`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.
- `ueberwelt`: `AEGIS-Simulation` (near `simulation`), `Simulationshypothese` (near `simulation`). occurrence: a heading, the project title, a borrowed concept (`Dialektische Emergenz` L58, `Simulationshypothese` L67) or a generic interface (`Schnittstelle`) — not the page's term; `Juna/V` and `Systemische Emergenz/Glitch` are read on juna and risse where they add; `Fehlausgerichtete Kohärenz` is read on aegis.


**Pages not read:** `emergenz` (L58 is a borrowed dialectical mechanism), `kohaerenz` (L11 is the project title), `realitaetsebenen` (L65 a generic topology), `ueberwelt` (L44 „Simulation“ in a borrowed ontology) — occurrences.

**Record entries:** none — the report offers options and decides nothing a record holds.

**Not promoted:** Orakel-Sigma, Direktive V3, the five ontologies, the mechanisms and interfaces, the hypothesis matrix, the failure paths and endgames, the transcendence models and the genre techniques, and every borrowed concept (M-theory, It from Bit, MUH, holography, Orch OR, Levinas, IIT, GNW, autopoiesis, Gödel).

**One reader**: aegis, juna, kael, nichts-rauschen, multiplizitaet, tsdp, did, risse.

**Chapter readings**: none — the report names no chapter of the novel.
