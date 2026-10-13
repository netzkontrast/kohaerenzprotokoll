# Brief — readings from document 312 (step 6)

1 document, one reader, one batch: `ingest-313`. Files go to `Plan/runs/ingest-313/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 312 | `emergenz-aegis-und-selbststrukturierung` | 2025-04-27 | „the emergent self-structuring research“ (an unsigned German research report with a web reference list) | a study for „Projekt: AEGIS“ of thirteen tension fields in clusters, a synthesis, models, philosophy, eight principles and a seven-aspect architecture, with AEGIS „Ein postuliertes theoretisches Modell“ (L26) of a system that generates „Kohärenz aus Entropie“; hedged throughout and calling the model a „vielversprechende theoretische Konstruktion“ (L417), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (424 lines for `emergenz-aegis-und-selbststruk`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report on a postulated model: write „the self-structuring research postulates / asks …“, keep its conditional and its questions, and say AEGIS is a postulated theoretical model here. The borrowed theories (Prigogine, Luhmann, Haken, constructivism) are lens. Cut quotations before glued reference numbers and inner quotes.

## Pages — document 312, `emergenz-aegis-und-selbststrukturierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L26, L30, L34, L50, … (31 lines). central (3–6): „Ein postuliertes theoretisches Modell“, a frame for a system creating itself by emergent self-structuring and generating „Kohärenz aus Entropie“ (L26); its boundary not necessarily spatial (L338); possibly a simulation machine for its own existence (L290); the question whether it could develop consciousness (L122); a new form of being, asked (L375); the architecture „kein fester Bauplan“ (L409).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L21. minor (1–3): emergent self-structuring defined as the spontaneous rise of complex patterns without external steering (L21); the constitutive principle of emergence from nothing or the void (L38, L50).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L15, L26, L50, L66, L74, L158, … (26 lines). central (3–6): coherence generated from entropy as „das Kernversprechen von AEGIS“ (L74) and its core concept, which „klingt paradox“ and must be read through non-equilibrium thermodynamics (L242); dissipative structures as key (L74); L158 only if it adds.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L15, L26, L50, L74, L98, L122, … (22 lines). central (3–6): coherence from entropy as AEGIS's core concept (L26, L242); the question how AEGIS defines its identity while generating coherence (L266); only lines where coherence is AEGIS's, not general.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L162, L235. minor (1–3): negentropy in the energy and entropy cluster (L162, L235) — only where tied to AEGIS.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L120. not read: occurrence — `Simulation` (L120) is internal simulation of scenarios, a capacity in the consciousness cluster.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: the document's labels (`AEGIS-Protokoll`, `AEGIS-Bezug`, `Energie und Entropie`, `Systemgrenzen und Selbstorganisation`, `Simulationsmaschine`, `Agentenbasierte Simulation`, `Simulationstheorie`, `Gödel`) — cluster headings, model names or lens, read with the page's reading where it adds, not promoted.
- `grosse-mauer`: `Systemgrenzen und Selbstorganisation` (near `systemgrenze`). occurrence: the document's labels (`AEGIS-Protokoll`, `AEGIS-Bezug`, `Energie und Entropie`, `Systemgrenzen und Selbstorganisation`, `Simulationsmaschine`, `Agentenbasierte Simulation`, `Simulationstheorie`, `Gödel`) — cluster headings, model names or lens, read with the page's reading where it adds, not promoted.
- `ueberwelt`: `Simulationsmaschine` (near `simulation`), `Agentenbasierte Simulation` (near `simulation`), `Simulationstheorie` (near `simulation`). occurrence: the document's labels (`AEGIS-Protokoll`, `AEGIS-Bezug`, `Energie und Entropie`, `Systemgrenzen und Selbstorganisation`, `Simulationsmaschine`, `Agentenbasierte Simulation`, `Simulationstheorie`, `Gödel`) — cluster headings, model names or lens, read with the page's reading where it adds, not promoted.


**Record entries** (one file each):

- **`c2-entropie-sense`**: entropy as what AEGIS generates coherence from (L26, L74, L242) — the source, not only the thing to be resisted; say which position it sits nearer, deciding nothing.
- **`c3-emergenz-origin`**: AEGIS's emergence from low organisation, nothing or the void as „das konstitutive Prinzip der Emergenz“ (L38, L50) — a postulated model; say which position it sits nearer, deciding nothing.

**Not promoted:** the thirteen clusters and their five labels, the eight principles, the seven-aspect architecture, Emergente Selbststrukturierung, Realitätsgenerierung, operative Schließung, and the borrowed theories.

**One reader**: every page above and the two record entries.

**Chapter readings**: none — the document names no chapter.
