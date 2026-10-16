# Brief — readings from document 307 (step 6)

1 document, one reader, one batch: `ingest-308`. Files go to `Plan/runs/ingest-308/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 307 | `kohaerenz-protokoll-plot-synthese` | 2025-04-25 | „the 39-beat plot synthesis“ (an unsigned German plot blueprint with 19 web references) | a three-act plan of 39 beats, each with `Handlung`, `M-Resonanz` and `Konzept/Funktion`, over AEGIS, M (the Monstergruppe), Kael and his alters, Juna and the K-J Verbindung, with three alternative resolutions (Beats 35–37), character vectors, a concept matrix and stress points; it calls itself a „Konzeptuell gesättigter Plot-Blueprint“ (L13) ready for execution (L390), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (413 lines for `kohaerenz-protokoll-plot-synth`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plot blueprint: write „the 39-beat plot synthesis plans … in Beat N (Akt N)“, name the beat, and keep the three resolution variants as variants — the choice is left open (L386). Cut quotations before glued reference numbers, bold markers and escaped asterisks.

## Pages — document 307, `kohaerenz-protokoll-plot-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L27, L28, L40, L41, L42, L43, … (92 lines). central (3–6): an entity in the Potentialmeer existing by negation and delimitation (L27); postulating M as a threat to its stability (L63); the significant system error and visible „Risse“ in Akt 2 (L177); its arc „die Tragödie einer Entität“ (L304); the three resolution variants — tragic end (L275), radical transformation (L279), a third (L283).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L42, L75, L77, L129, L130, L183, … (9 lines). minor (1–3): fragments of Kael's identity (L42); „Jeder Alter verkörpert eine spezifische Facette“ of M's internal structure (L310); L75, L129 only if they add.
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L40, L51, L69, L71, L131, L155, … (15 lines). central (3–6): Kael's DID induced by AEGIS and serving as its analytic tool (L40); the turn from passive to active perception of the DID structure at the end of Akt 1 (L131); L51, L69, L155 only where they add.
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L149, L173, L209, L257, L283, L286, … (13 lines). minor (1–3): only beats where emergence is applied to the plot (L149, L173, L283); else not read.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L306, L311, L381. minor (1–3): introduced only as minor figures, „Sie repräsentieren AEGIS' Willen und Methoden innerhalb der Kernwelten“ (L311); L306, L381 only if they add.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L41, L87, L237, L239, L291, L303, … (7 lines). minor (1–3): her connection to Kael embodying Moonshine (L41), „Die Verkörperung von Moonshine“ (L305); the K-J connection as AEGIS's primary blind spot (L41).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L40, L41, L42, L43, L51, L69, … (55 lines). central (3–6): „Menschlicher Avatar von M in AEGIS“ (L40); his conscious decision for full integration at the end of Akt 2 (L213); all of M's properties converging in him in Beat 34 (L268); integrated, existing beyond the simulation in a variant (L291).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L42, L51, L75, L76, L77, L111, … (17 lines). central (3–6): „Isolierte Simulationsumgebungen“ of AEGIS (L42); the four Kernwelten activated in Beat 4 (L75); collapsing or merging fully in Akt 3 (L255).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the novel's title.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L27, L28, L57. minor (1–3): AEGIS as an entity in the Potentialmeer (L27, L28); L57 only if it adds.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L131. minor (1–3): the false decomposition showing first „Risse“ at the end of Akt 1 (L131); visible „Risse“ in AEGIS's system in Akt 2 (L177).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L15. not read: occurrence — `Simulation` (L15) is the document's `NZT-48 Simulation` authorisation label.

- **`moonshine-link`** (minor, 1–3): the K-J Verbindung embodying Moonshine and being „AEGIS' primärer blinder Fleck“ (L41); Juna as „Die Verkörperung von Moonshine“ (L305). Quote only lines about the link.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading — see the extra page below.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: the Guardians as minor figures representing „AEGIS' Willen und Methoden innerhalb der Kernwelten“ (L311).
- **`q3-how-many-kern-welten-and-alters`**: „Die vier Kernwelten werden aktiviert“ (L75); each alter embodying a facet of M (L310) — no correspondence of worlds and alters stated; say so.
- **`q8-aegis-after-the-vortex`**: three resolution variants for AEGIS — tragic end (L275), radical transformation (L279), a third (L283) — left open, the choice said to carry considerable thematic implications (L386).

**Not promoted:** M and its five properties, the Parias, the Kernkonflikt, the Gödel-Punkt, NZT-48, the beats and acts, the Auflösungsvarianten, the concept matrix, and the borrowed lens (parakonsistente Logik, Dialetheismus, Nicht-lokalität, Quantenverschränkung).

**One reader**: every page above, the extra page and the three record entries.

**Chapter readings**: none — the document names no chapter; its units are acts and beats.
