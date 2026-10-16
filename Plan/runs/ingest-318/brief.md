# Brief — readings from document 317 (step 6)

1 document, one reader, one batch: `ingest-318`. Files go to `Plan/runs/ingest-318/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 317 | `kohaerenz-protokoll-umfassendes-konzept-mit-prin` | 2025-04-27 | „the comprehensive concept with 13 principles“ (an unsigned German concept outline) | a revised concept re-reading the world, plot, cast, setting and a chapter overview through thirteen named principles (`Emergenz aus der Leere` … `Autonome Grenzbildung`, L17–L29), assigning principles to the Potentialmeer, AEGIS, M/Kael, Juna and the K-J connection, the Kernwelten, the Guardians and the Überwelt, and giving focus lines for seven chapters (L76–L82); it calls itself an updated comprehensive concept (L11, L84) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (85 lines for `kohaerenz-protokoll-umfassende`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept outline: write „the 13-principle concept frames / assigns …“; its principle numbers („Prinzip 13“) carry glued digits — never quote across them; name the principle by its title in backticks instead. Hedges (`möglicherweise`) stay. The borrowed equations (Autopoiesis = Prinzip 13 …) are its mapping, lens.

## Pages — document 317, `kohaerenz-protokoll-umfassendes-konzept-mit-prin`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L35, L36, L37, L38, L42, … (15 lines). central (3–6): a highly complex AI whose existence manifests autonomous boundary-formation (autopoiesis) (L35); emerged from „Resten“ of earlier systems (L35); embodying a rigid application of the principles focused on self-preservation by order and isolation (L49); the core conflict, its self-preservation against M/Kael's dynamic, integrated striving (L38); its Überwelt aiming at maximal order (L58).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L65. minor (1–3): cache coherence as the lived consequence of identity and perception disturbed by AEGIS's fragmentation (L65).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L68. minor (1–3): IFS/DID as the psychological manifestation of the fragmentation on the levels of reflection, identity and will (L68).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L17. minor (1–3): the first principle, `Emergenz aus der Leere`: existence as a fragile coherence emerging from fluctuations in the unstable null space of non-existence (L17).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L25. minor (1–3): the ninth principle, `Kreative Spannung`: complex structures between energy flow and entropy (L25); the Potentialmeer's high entropy (L34).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L52. minor (1–3): „Verkörpern die überbetonten oder verzerrten Prinzipien ihrer jeweiligen Kernwelt“ (L52).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L37, L50. minor (1–3): the K-J connection challenging AEGIS's understanding of communication/isolation and possibly time/causality (L37); Juna possibly another entity or principle outside AEGIS's understanding (L50) — keep `möglicherweise`.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L35, L38, L40, L42, L43, L44, … (7 lines). central (3–6): M/Kael a more stable form of coherence based on inner order and integration (L36); his journey from a passive object of AEGIS's manipulations to a being navigating the thirteen principles (L48); the three parts as his learning, cycle and action (L42–L44).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L36, L57. minor (1–3): nested reality levels created by AEGIS as controlled environments to analyse M by minimal coupling (L36); artificial reality layers isolating or manipulating specific principles (L57).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the novel's title.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L48. not read: occurrence — `Multiplizität` (L48) inside Kael's journey line; read on kael if it adds.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L15, L33, L34, L56. minor (1–3): the fundamental state of unstable non-existence, high chaos, informational noise and high entropy (L34); the ground defined by those principles (L56).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L27. not read: occurrence — `Realitätsebenen` (L27) is the eleventh principle's title, read on kern-welten.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L58. minor (1–3): „AEGIS' Überwelt“, a space created by boundary-formation trying to establish maximal order (L58).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Emergenz aus der Leere` (near `emergenz`), `Relationale Emergenz` (near `emergenz`), `Multikausale Emergenzzeit` (near `emergenz`). occurrence: the principles' titles (`Emergenz aus der Leere`, `Relationale Emergenz`, `Multikausale Emergenzzeit`, `Verschachtelte Realitätsebenen`), `Moonshine` and `Gödel` in the concept mapping, `Kohärenz Protokoll` the title — read with the page's reading where they add, not promoted.
- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: the principles' titles (`Emergenz aus der Leere`, `Relationale Emergenz`, `Multikausale Emergenzzeit`, `Verschachtelte Realitätsebenen`), `Moonshine` and `Gödel` in the concept mapping, `Kohärenz Protokoll` the title — read with the page's reading where they add, not promoted.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the principles' titles (`Emergenz aus der Leere`, `Relationale Emergenz`, `Multikausale Emergenzzeit`, `Verschachtelte Realitätsebenen`), `Moonshine` and `Gödel` in the concept mapping, `Kohärenz Protokoll` the title — read with the page's reading where they add, not promoted.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). occurrence: the principles' titles (`Emergenz aus der Leere`, `Relationale Emergenz`, `Multikausale Emergenzzeit`, `Verschachtelte Realitätsebenen`), `Moonshine` and `Gödel` in the concept mapping, `Kohärenz Protokoll` the title — read with the page's reading where they add, not promoted.
- `realitaetsebenen`: `Verschachtelte Realitätsebenen` (near `realitatsebene`), `Verschachtelte Realitätsebenen` (near `realitatsebenen`). occurrence: the principles' titles (`Emergenz aus der Leere`, `Relationale Emergenz`, `Multikausale Emergenzzeit`, `Verschachtelte Realitätsebenen`), `Moonshine` and `Gödel` in the concept mapping, `Kohärenz Protokoll` the title — read with the page's reading where they add, not promoted.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: the Guardians embodying the over-stressed or distorted principles of „ihrer jeweiligen Kernwelt“ (L52) — one Guardian per world implied, no count; say so.

**Not promoted:** the thirteen principles and their formulas, the entity M, the parts' journeys, the concept mapping (Autopoiesis, Monstergruppe, Moonshine, Gödel, Holismus vs. Reduktionismus as principles).

**One reader**: every page above, the record entry and the chapter readings below.

**Chapter readings** (the same reader, one file per chapter, into `Plan/runs/ingest-318-kap/readings/kap-NN--kohaerenz-protokoll-umfassendes-konzept-mit-prin.md`): Kap 1 (L76), Kap 2 (L77), Kap 6 (L78), Kap 7 (L79), Kap 14 (L80), Kap 28 (L81), Kap 39 (L82) — each chapter's focus line from the chapter overview, naming the principles by title in prose (the numbers carry glued digits). Say the overview keeps the chapter assignment and only colours its interpretation (L74). A concept's focus, not the chapter.
