# Brief — readings from document 295 (step 6)

1 document, one reader, one batch: `ingest-296`. Files go to `Plan/runs/ingest-296/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 295 | `aegis-philosophie-und-systemtheorie` | 2025-04-19 | „the systems-theory analysis“ (an unsigned German analysis with a web reference list) | a study of AEGIS as „eines hypothetischen Systems“ (L15): borrowed frames (coherentism, autopoiesis, Gödel, the simulation argument …) in Part I, applied in Part II to AEGIS's slogans, Axiom 1 and 4, RCV, the formula `Existenz = Wirkung + Selbstbezug`, the Guardians as agents, EIC and BPoF, with five open questions in Part III; it calls AEGIS hypothetical and takes the `universal reboot` and EIC from outside itself (L96, L154) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (247 lines for `aegis-philosophie-und-systemth`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of a hypothetical system: write „the systems-theory analysis reads / interprets …“; what it says of AEGIS is its interpretation, often hedged (`möglicherweise`, `wahrscheinlich`) — keep the hedge. The borrowed frames of Part I are lens, not the novel. Glued reference digits end most sentences; `Axiom 1`, `Axiom 4` cannot be quoted across their digit — use backticks.

## Pages — document 295, `aegis-philosophie-und-systemtheorie`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L19, L21, L22, L23, … (61 lines). central (3–6): the expansion `Autonomous Epistemic Guardian for Integrity Systems` (L15); a radical turn from trust and external control (L15), trust replaced by verification (L117); existence as `Existenz = Wirkung + Selbstbezug`, not substance (L141); non-conscious (L59) and amoral, validity over goodness (L143); RCV and Axiom 1 — what is not verifiable does not exist inside (L23, L94); its boundary not physical (L95); the `universal reboot` interpreted as ultimate negation back to the Ursprungsmuster (L96); weaknesses: solipsism, incorrigibility (L22, L109, L110).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L40, L41, L80, L93. minor (1–3): weak or strong emergence held open for AEGIS (L41); `Emergenz durch Negation` as Axiom 4, order by filtering (L93).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L40. minor (1–3): only if L40 (or its neighbour) ties AEGIS's entropy management to self-organising physics; else not read.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L80, L147. minor (1–3): „wie die hypothetischen Guardians“ (L147) as agents interacting only with RCV-confirmed agents (L153); the EIC inference that agents might pursue private goals (L155). Keep `hypothetischen`.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. minor (1–3): the slogan `Kohärenz statt Wahrheit` and validity as the measure (L15, L93); cooperation where interactions reinforce coherence mutually (L159).
- **`negentropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Negentropie` alone on L51. not read: occurrence — `Negentropie` (L51) is an analogy for a resource supply, inside a borrowed frame.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L65. not read: occurrence — `Simulation` (L65) is Bostrom's simulation argument, a borrowed frame.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Management` (near `entropie`). occurrence: `Entropie-Management` as AEGIS's goal, read with the entropy reading if any.
- `kohaerenz`: `Kohärenz statt Wahrheit` (near `koharenz`), `Inkohärenz` (near `koharenz`). reading: `Kohärenz statt Wahrheit` the slogan (L15, L93); `Inkohärenz` read with it.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: `Simulationshypothese` a borrowed frame; L167's „Blaupause für eine Simulation“ read on aegis.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: the expansion `Autonomous Epistemic Guardian for Integrity Systems` (L15), with AEGIS as a hypothetical self-verifying system — add it as this document's position; quote around nothing the line does not hold.

**Not promoted:** RCV and its expansions, the slogans, Axiom 1 and 4, the Ursprungsmuster, `Existenz = Wirkung + Selbstbezug`, EIC, BPoF, Ontologische Autarkie, Epistemische Autonomie, Reaktive Transparenz, Das AEGIS-Wagnis, Solipsismusgefahr, Inkorrigierbarkeit, and the twenty borrowed frames.

**One reader**: every page above and the record entry.

**Chapter readings**: none — the document names no chapter.
