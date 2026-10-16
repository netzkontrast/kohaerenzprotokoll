# Brief — readings from document 280 (step 6)

1 document, one reader, one batch: `ingest-281`. Files go to `Plan/runs/ingest-281/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 280 | `integriertes-kohaerenz-protokoll-erstellung` | 2025-12-05 | „the protocol report“ (an unsigned German analytic report) | an inventory of twenty project files with a status and an analysis each (L35–L192), then applications of physics, systems theory and narratology to the novel's world, and a three-phase „Integrierte Kohärenz-Protokoll“ (L304–L353); it calls the files an „unveränderlichen Kern“ (L17) and confirms itself at the end (L369), its claims |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (420 lines for `integriertes-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report: in the inventory (L35–L192) every analysis is the document's report of another file — write „the protocol report reports of the file … that …“; in its own applications (L196 onward) write „the protocol report applies / describes …“. **Do not read or cite L15, L17 (beyond the phrase „unveränderlichen Kern“), L82, L90 or L170–L180.** Cut quotations before bold markers, inner quotes and `$K\_1$`-notation.

## Pages — document 280, `integriertes-kohaerenz-protokoll-erstellung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L43, L49, L51, L122, L130, L132, … (31 lines). central (3–6): reported of a file: its fate fixed, a tragic figure (L49), its Genesis-Krise and the excision of its emotional parts (L51); in the document's own application „AEGIS ist ein Maxwellscher Dämon“ (L208, L212), „ein hyper-autopoietisches System“ (L250) whose pathology is endless repetition (L252); failing because it cannot process paraconsistent states (L302).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L132, L252. minor (1–3): reported of a file: the plot forces AEGIS to accept a true contradiction, leading to its transformation (L132).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L290, L339. minor (1–3): „Die Alters (Lex, Nyx, Kiko) sind“ … — Funktionale Multiplizität as internalised polyphony (L290); the chorus of the Alters interrupting AEGIS's monologue (L339).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L39, L88, L104. minor (1–3): reported of a file: it defines the Dual Kernel Theory splitting reality into two antagonistic principles (L39); the workflow tagging elements by the DKT principle (L88).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L39. not read: occurrence — `Entropie` at L39 is read on dkt.
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L78. not read: occurrence — `Systemgrenze` (L78) is the system's boundary in general, not the Große Mauer.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L122, L138, L172, L176, L287, L338, … (9 lines). minor (1–3): reported of a file: four autonomous subsystems including Juna/V (L122); the Moonshine-Link as ontological exploit (L138); in Phase II an outside oscillator synchronising the separated parts (L338). Never L170–L180.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L33, L43, L49, L51, L106, … (34 lines). central (3–6): reported of a file: Kael's journey mapped on three phases, not fusion (L146–L148); in the document's own application healing as the move to second-order observation (L263); in Phase III a system true yet unprovable within AEGIS's axioms (L345); the Bekenstein limit of Kael in Phase I (L329).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L290. minor (1–3): among the Alters (L290).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L234. minor (1–3): the simulated world of AEGIS, the Konstrukt-Stadt, as the Bulk (L234).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L290, L331. minor (1–3): among the Alters (L290); „Die ANP-Barrieren (Lex)“ as protective in Phase I (L331).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L138, L338. minor (1–3): reported of a file: the Moonshine-Link as quantum entanglement and ontological exploit beyond AEGIS's surveillance (L138); Juna/V as oscillator (L338).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L148, L290, L347. minor (1–3): reported of a file: not fusion (L148); in the document's application „ist nichts anderes als internalisierte Polyphonie“ (L290); the synthesis output (L347).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L290. minor (1–3): among the Alters (L290).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L252. minor (1–3): AEGIS's openness to the environment („Potentialmeer“) closed off after the Genesis-Krise (L252).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L41, L78, L210, L212, L236, L277, … (8 lines). minor (1–3): reported of a file: „Pixelierungsfehler oder Informationsüberläufe an der Systemgrenze“ (L78); in the document's application the world's instability as the physical consequence of AEGIS's deletion (L212); the simulation a faulty projection of Boundary data (L236).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L98, L104, L146, L325, L364, … (7 lines). minor (1–3): TSDP at L98, L104 or L146 where the line reports a file's use of it; never L17.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L198. not read: occurrence — `Simulation` (L198) in a general sentence.

- **`genesis`** (minor, 1–2): reported of a file, AEGIS's origin trauma, the „Genesis-Krise“ (L51); AEGIS closing off its openness after it (L252).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). reading: `Genesis-Krise` as AEGIS's origin trauma (L51, L252), on genesis.
- `goedel-gambit`: `Gödel-Gambits` (near `godelgambit`). occurrence unless the line describes the Gambit; `Gödel-Gambits` read on goedel-gambit only then.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Integrierte Kohärenz-Protokoll` (near `koharenz`), `Integrierten Kohärenz-Protokolls` (near `koharenz`), `Statische Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence: the title and the Protocol's own name; `Kohärenztheorie der Wahrheit` read on aegis.
- `kohaerenz-kernel`: `Kernel` (near `kohaerenzkernel`), `Kernel` (near `koharenzkernel`), `Kernel` (near `koharenzkernelk1`). occurrence: `Kernel` alone is not the Kohärenz-Kernel.
- `kollaps-kernel`: `Kernel` (near `kollapskernel`), `Kernel` (near `kollapskernelk0`). occurrence: `Kernel` alone is not the Kollaps-Kernel.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: `Mosaik` the narrative approach, not the Mosaik-Herz.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: reported of a file, the plot forces AEGIS to accept a true contradiction, leading to Algorithmische Melancholie (L132).

**Not promoted:** the inventory's status ranks, the three-phase Integrierte Kohärenz-Protokoll and its formula, Bulk and Boundary, the Bekenstein limit, Beobachtung zweiter Ordnung, the Agentive Narrative, the System-Dirigent.

**One reader**: every page above and the record. Never L15, L17 (beyond its one phrase), L82, L90, L170–L180.

**Chapter readings**: none — 39 chapters (L57, L277, L365) is a total.
