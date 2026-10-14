# Brief — readings from document 508 (step 6)

1 document, one reader, one batch: `ingest-508`. Files go to `Plan/runs/ingest-508/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 508 | `narrative-vertiefung-kohaerenz-protokoll` | 2025-04-27 | „the deepening research report“ (an unsigned German research report) | surveys borrowed theories in eight sections against a plot concept and proposes, mostly in the subjunctive, how each could enrich the novel; sentences marked with a restated-concept label (32 times) restate the plot concept; the body breaks off at L722; a research report, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (972 lines for `narrative-vertiefung-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Two voices: a line that ends with the restated-concept label (`[User Query]` in the export) restates the plot concept — write „the deepening report restates from the plot concept …“; the `Narrative Relevanz` lines are the report's own proposals — write „the deepening report proposes …“. Never write „user“ in our prose: call the label „the restated-concept label“. Theory names after people stand on most lines (philosophers, psychologists, scientists): never write a name, never quote a span containing one or an adjective formed from one (e.g. „Jung'scher“); world codes (Co1, McL, Ly, B, M) are never expanded to mathematicians' names. No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim.

## Pages — document 508, `narrative-vertiefung-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L30, L38, L46, L54, … (79 lines). central (4–8): restated: AEGIS fighting for existence and stability in the Potentialmeer, analysing the entity M actualised as Kael (L25); AEGIS observing M by creating Kernwelten as subsystems in which fragments of M exist (L71); the faulty „Kohärenz-Controller“ that creates and analyses inconsistencies it cannot synchronise (L83, L348); the report's own: AEGIS as the observer within its own analytic system (L71), AEGIS's action structurally gaslighting (L505), and the question weak or strong AI kept open (L358).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L206. minor (1–4): the report's general description of alters as distinguishable personality states taking control (L206).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L202. minor (1–4): restated: DID as the model for Kael's extreme fragmentation and loss of identity (L206).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L264. not read: an occurrence — emergence in the report's survey of theories and a world's focus (L264, L268, L284).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L38, L79, L96, L129, L137, … (35 lines). central (4–8): the Kael–Juna connection, the „Moonshine-Link“, as an alternative coherence protocol or backchannel (L565, L569 restated); the report's proposals: Juna's influence possibly resting on principles like hypercomputation (L137); Juna possibly embodying the Anima that leads Kael to integration (L240 — quote name-free spans only); section VII grades seven alternative mechanisms (L581–L629) — summarise, quote at most two.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L25, L38, L46, L54, L71, … (84 lines). central (4–8): restated: M actualised as Kael (L25); the Kernwelten as faulty caches holding inconsistent copies of Kael's identity, Kael's journey the fight to restore identity coherence (L83); DID as the model of Kael's extreme fragmentation (L206); the report's own: Kael's integration possibly an NP-hard problem AEGIS can verify but not produce (L129); Kael as the pole of integration and wholeness (L274–L276).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L30, L38, L46, L54, L63, L71, … (47 lines); `Kernwelt` L30, L38, L46, L54, L63, L71, … (52 lines). central (4–8): restated: the 20 Kernwelten based metaphorically on the 20 sporadic subquotients of M, the symmetry of each group defining each world's rules (L145); faulty caches of Kael's identity (L83); the report's proposals for single worlds by their letter codes — B tied to chaos and shadow (L190, L208), Co1, McL and Ly (L240, L264); never expand the codes.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L96, L129, L166, L465, L565, L569. minor (1–4): the link's name restated from the plot concept, referring to the Monstrous Moonshine theory (L569), an alternative coherence protocol or backchannel (L569); the section examining alternative explanations (L565).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L236. not read: an occurrence — `Persona` in a named psychologist's archetype list (L236).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L21, L25, L38, L46, L54, L58, … (23 lines). central (4–8): restated: the Potentialmeer as a realm of pure potentiality where AEGIS fights for existence and stability (L25); the report's own: the quantum vacuum as a metaphor for it, no nothing but a plenum of latent possibilities (L46); a process of becoming that AEGIS's forced stability could fail against (L38 — cut before the philosopher's name).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L46, L71, L190, L348, L394, L402, … (8 lines). minor (1–4): restated: AEGIS suffering system instabilities, „Risse“ (L348); the report's proposals: the Risse as a consequence of AEGIS's self-reference (L71), as chaotic dynamics (L190), as the failure of a global workspace (L394).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L240. minor (1–4): the report proposes Juna might embody the Anima, the Great Mother or Sophia (wisdom) (L240 — quote name-free span).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L358. not read: an occurrence — `Simulation` in the weak-or-strong-AI question (L358), read on aegis.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cache-kohaerenz`: `Cache-Kohärenz-Metapher` (near `cachekoharenz`). read on kern-welten (above): the cache metaphor (L83).
- `emergenz`: `Emergenztheorie` (near `emergenz`), `Schwache Emergenz` (near `emergenz`), `Starke Emergenz` (near `emergenz`). an occurrence: theory names in the survey.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Cache-Kohärenz-Metapher` (near `koharenz`), `Kohärenz-Controller` (near `koharenz`), `Identitäts-Kohärenz` (near `koharenz`). an occurrence: the project name and `Kohärenz-Controller`, read on aegis.
- `personas`: `Transpersonale Psychologie` (near `persona`). an occurrence: a school of psychology.


**Record entries** (one file, formatted as earlier entries):
- **`q3-how-many-kern-welten-and-alters`**: the deepening report restates from the plot concept twenty Kernwelten, based metaphorically on the twenty sporadic subquotients of M (L145); recorded, not applied.

**No chapter readings**: no chapter is named (`Kapitel` 0; `Kapitelentwurf` once, L15).

**Not promoted:** Kohärenz-Controller, the theory names (most named after people), Hypercomputation, the BPM labels, the seven graded mechanisms, the label pair Kernkonzept/Narrative Relevanz.

**One reader**: every page above and the Q3 entry.
