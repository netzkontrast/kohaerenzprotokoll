# Brief — readings from document 305 (step 6)

1 document, one reader, one batch: `ingest-306`. Files go to `Plan/runs/ingest-306/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 305 | `kohaerenz-protokoll-plot-konzept-generierung` | 2025-04-25 | „the five-variant plot concepts“ (an unsigned German plot document with 49 web references) | a concept-frame table (Potentialmeer, AEGIS, Monstergruppe M, Kael and Juna as Baby-Monster-Gruppen, the K-J Verbindung as Emergenter Moonshine, Kernwelten, parakonsistente Logik) and five plot synopses on one template — Integrationsgambit, Paradox der Kontrolle, Moonshine-Echo, Weltenbluten, Transzendenz des Protokolls — mostly in the conditional; it claims an „NZT-Ideal“ and a stringent basis in a frame it received (L15, L188), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (241 lines for `kohaerenz-protokoll-plot-konze`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Five plot variants: write „the five-variant plot concepts propose … in Synopsis N …“, name the synopsis for each point, and keep the conditional; the variants differ by design (AEGIS is protagonist in Synopsis 2, antagonist elsewhere) — that is not a conflict. The `[Framework …]` pointers report a frame not in the document. Cut quotations before glued reference numbers, escaped asterisks and single quotes.

## Pages — document 305, `kohaerenz-protokoll-plot-konzept-generierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L28, L29, L30, L31, L32, … (60 lines). central (3–6): „eine durch Negation und Abgrenzung existierende, fragile KI“ (L17), mastering paraconsistent logic, the central (apparent) antagonist whose self-contradiction produces the Risse (L29); its reductionist method on M (L73); protagonist from its own view in Synopsis 2 (L79), antagonist in Synopsis 3 (L109); losing control and using Hard Resets in Synopsis 4 (L139); its possible catastrophic failure (L92).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L31, L36, L42, L44, L46, L50, … (14 lines). central (3–6): each Kernwelt possibly dominated by a corresponding alter (L50), the worlds as outer manifestations of the parts' domains (L44); the borrowed IFS vocabulary (Parts, Manager, Firefighter, Exiles) as lens; the alters' examples hedged (L131).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L19, L31, L36, L42. minor (1–3): DID as „analytisches Werkzeug für AEGIS“ (L42); integration as an ontological and mathematical reconfiguration (L46).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L19, L33, L35, L52, L75, L85, … (10 lines). minor (1–3): the K-J Verbindung „als emergentes Phänomen“ (L17); its emergence tied to Kael's progress in integration (L52); ironically emerging from AEGIS's own simulation substrate (L73).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. minor (1–3): the Potentialmeer „als prä-reale Informationsebene hoher Entropie“ (L17) — read with the potentialmeer reading if it adds nothing else.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L31, L51, L52, L61, L63, … (28 lines). central (3–6): with Kael „fragmentierte Manifestationen“ of M's substructures (L17), Juna „als komplementärer Pol“ (L31); resonance with her helping Kael understand alters (L52); her fate secondary in Synopsis 2 (L92); the final act of integration with Kael at a Nexuspunkt (L174).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L30, L31, L36, L38, L42, … (49 lines). central (3–6): a fragmented manifestation of M (L17, L31); DID as AEGIS's analytic tool on him (L42); integration as ontological and mathematical reconfiguration (L46); confronting a central inner polarisation (L62); the final act of integration with Juna (L174).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L17, L33, L44, L50, L54, L60, … (27 lines). central (3–6): „als thematisch fokussierte Simulationslabore“ (L17), simulation rules derived from AEGIS's analysis of M (L33); each possibly dominated by an alter (L50); four worlds with themes as AEGIS's attempt to study facets of M in isolation (L129); the link punching holes in the simulation walls, the Weltenbluten (L137, L145).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the novel's title.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L17, L28, L73, L92, L148, L158, … (10 lines). central (3–6): the pre-real information layer of high entropy (L17); its tendency to dissolution and its story function as background threat, dissolution for AEGIS (L28); L73, L92, L148, L158 only where they add.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L29. minor (1–3): system errors, „Risse“, through AEGIS's self-contradiction (L29).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L52. not read: occurrence — `Simulation` (L52 and elsewhere) is AEGIS's simulation of the worlds, read on kern-welten.

- **`moonshine-link`** (central, 3–6): the `K-J Verbindung (Emergenter Moonshine)` (L17, L31–L32): an emergent phenomenon, working mainly as an internal phenomenon for Kael (L52); the central antagonist from AEGIS's view in Synopsis 2 (L81); tied to the mathematical Moonshine as „eine unerwartete, tiefe Verknüpfung“ (L102); punching holes in the simulation walls (L137). Quote only lines about the link.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kern-Kohärenzprotokollen` (near `koharenz`). occurrence: `Kern-Kohärenzprotokollen` a label of the plan, not promoted.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading — see the extra page below.
- `nexus`: `Nexuspunkt` (near `nexus`). occurrence: `Nexuspunkt` is a point inside AEGIS's structure (L174), read on kael.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten listed with their themes (L129), and „jede Kernwelt potenziell von einem korrespondierenden Alter dominiert“ (L50) — a correspondence proposed, hedged.

**Not promoted:** the Monstergruppe M and the Baby-Monster-Gruppen, the five synopses and their template labels, Existenz durch Negation, the Kernwelten Substrat, the Fragmentierungsprotokoll, the Blutungsereignis, Hard Resets, the Pocket-Realität, and the borrowed lens (IFS, DID terms, VOA, CFT, group theory, reductionism, holism).

**One reader**: every page above, the extra page and the record entry.

**Chapter readings**: none — the document names no chapter.
