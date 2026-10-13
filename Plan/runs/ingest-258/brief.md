# Brief — readings from document 258 (step 6)

1 document, one reader, one batch: `ingest-258`. Files go to `Plan/runs/ingest-258/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 258 | `fundament-konzept-fuer-kohaerenz-protokoll` | 2025-04-28 | „the Fundament analysis“ (an unsigned German report) | an analysis of the proposed entity „Das Fundament“, an ontological ground meant to integrate the Paraiyas and resolve Paradoxon X in AEGIS: mapping, philosophical, physical, psychological and gnostic analogies, five integration strategies, alternatives, and a conditional recommendation (L437); an analysis of a proposal, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (595 lines for `fundament-konzept-fuer-kohaere`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of a proposal: write „the Fundament analysis reports the proposal as … / judges …“. The entity is proposed, not settled; its six Paraiyas are never listed. Its gnostic, physical and logical analogies are borrowed lenses. Cut quotations before inner quotes, emphasis marks and reference numbers glued to words.

## Pages — document 258, `fundament-konzept-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L31, L42, L45, L53, L54, L64, … (28 lines). central (3–6): a powerful, information-processing, possibly reality-shaping entity with inherent paradoxes and a limited, possibly faulty view of reality (L42); rejecting certain aspects of reality, the Paraiyas, as errors (L42); Paradoxon X as a narrative symptom of its inadequacy (L45), arising because AEGIS fails to see the deeper symmetry (L67); structurally like the gnostic Demiurge (L81).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L31. minor (1–4): the conflict Kontrolle/Emergenz between centralised control (AEGIS) and self-organising phenomena, central to the novel (L31).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L54, L64, L74, L330, L335, L450. minor (1–4): the Juna/V connection possibly an alternative mode of being, needing more work (L54); L330, L335, L450 only if they add.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L30, L43, L53, L64, L65, L73, … (33 lines). central (3–6): the TSDP model as the basis of Kael's character architecture, his psyche fragmented (L43); his struggle for inner coherence mirroring the structure of ultimate reality (L82); the recommended resolution through the characters (L437–L444, only if a line names Kael).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L32, L44, L66, L177. minor (1–4): the Kernwelten and the Potentialmeer pointing to a layered reality (L44); multiple levels of reality, the Kernwelten (L32).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L44, L66, L74. minor (1–4): with the Kernwelten, a layered reality (L44); a possible weakness in the exact nature of AEGIS and the Potentialmeer (L74).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L32. not read: occurrence — `Realitätsebenen` at L32 glosses the Kernwelten, read on kern-welten.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L148, L459. not read: occurrence — `Sophia` at L148 is the gnostic Sophia of the analogy, not the Guardian.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L43, L53, L65, L73, L82, L268, … (7 lines). minor (1–4): the TSDP model as the basis of Kael's character architecture (L43).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L32. not read: occurrence — `Simulation` at L32 is the theme Realität/Simulation, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Kontrolle/Emergenz` (near `emergenz`), `Schwache Emergenz` (near `emergenz`), `Starke Emergenz` (near `emergenz`). `Kontrolle/Emergenz` read on emergenz; `Schwache Emergenz` and `Starke Emergenz` a borrowed lens.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `ueberwelt`: `Realität/Simulation` (near `simulation`). occurrence: `Realität/Simulation` a theme.
- `verschraenkungs-insel`: `Verschränkung` (near `verschrankungsinsel`). occurrence: `Verschränkung` the physical concept, not the Verschränkungs-Insel.


**Record entries:** none — no open record's question is answered.

**Not promoted:** Das Fundament (a proposed entity, the analysis's subject), the Paraiyas, Paradoxon X, Übermonstergruppe, the integration strategies and their table, the gnostic, physical and logical analogies, the Deus-ex-Machina risk.

**One reader**: aegis, kael, juna, tsdp, kern-welten, potentialmeer, emergenz. `kohaerenz`, `realitaetsebenen`, `sophia` and `ueberwelt` are occurrences.

**Chapter readings**: none.
