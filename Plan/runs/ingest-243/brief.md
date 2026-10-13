# Brief — readings from document 243 (step 6)

1 document, one reader, one batch: `ingest-243`. Files go to `Plan/runs/ingest-243/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 243 | `kohaerenz-protokoll-dramatica-synthese` | 2025-12-05 | „the Dramatica synthesis report“ (an unsigned German report) | a report mapping the project onto Dramatica's four throughlines and four dimensions, with the Dual Kernel Theory, a paraconsistent ending, the Mosaik-Strategie and a four-step Resonanz-Kodex; it calls itself complete („Das System ist vollständig.“ L210) — its claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (231 lines for `kohaerenz-protokoll-dramatica-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of proposals: write „the Dramatica synthesis report maps / proposes …“. **Privacy: do not read or cite L17–L23, L33–L59 or the appendix L212–L221** — those passages speak about matters outside the novel's world; read only from L65 on to L210. Its `Implikation:` lines are instructions to a writer, say so. `K\_1` and `K\_0` are written with the escape; cut quotations before reference numbers glued to words.

## Pages — document 243, `kohaerenz-protokoll-dramatica-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L43, L51, L59, L84, L88, … (20 lines). central (3–8): the world's guardian of an artificial state of high coherence, the AI deity of this world (L84); operating as Maxwell's demon, its failure a failure of knowledge (L90); fearing Desire most (L148); forced into Algorithmische Melancholie, giving up its operative closure to integrate Kael (L170). Do not read L23 or L43.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L170. minor (1–4): the ending forcing AEGIS into „Algorithmische Melancholie“, giving up its operative closure (L170).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L41, L63, L94, L146, L158, L205. minor (1–4): the physical laws of the DKT must allow inconsistencies (L94); the attraction between Kael and Juna working like gravity in the DKT (L146); the DKT as a bridge between the two stories (L158). Do not read L41 or L63.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L23. minor (1–4): the world built on the lie that existence without entropy is possible (L84). L23 is not read.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L84. minor (1–4): Kael, Juna and the Guardians as prisoners in this false universe, Logos-Prime (L84).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L84, L114, L116, L120, L124, L126, … (12 lines). central (3–8): the impact character, „Psychology / Dimension: Ability (Juna/V)“ (L114); Juna or her transcendent form V (L116); the error in the system that proves it wrong (L120); able to use the Moonshine-Link (L124); the living proof of functional multiplicity (L126); the attraction between Kael and Juna like gravity in the DKT (L146).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L39, L59, L84, L92, L96, … (28 lines). central (3–8): the main character, „Mind / Dimension: Thought (System Kael)“ (L96); System Kael a mind palace become a prison (L110); Lex a brooder (L106); not to be healed by a brilliant deduction (L112); his desire proves he lives (L148); in the finale a living Gödel sentence (L169). Do not read L19, L39 or L59.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L110, L146. minor (1–4): an EP breaking in as „Intrusive Thoughts“ (L110); the attachment trauma, a frustrated desire (L146).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. not read: occurrence — `Kohärenz` at L17 stands in the opening, which is not read.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L106, L217. minor (1–4): „Kael (speziell sein Anteil Lex) ist ein Grübler.“ (L106). L217, in the appendix, is not read.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L124. minor (1–4): Juna able to use the Moonshine-Link, a metaphorical adaptation of quantum entanglement (L124).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L126, L169. minor (1–4): Juna as the living proof of functional multiplicity (L126); the ending (L169).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L110. minor (1–4): an EP breaking in as „Intrusive Thoughts“ with Kiko (L110).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L94. minor (1–4): the world must have Risse; the report's instruction to a writer (L94); the high-coherence state leading to Risse (L84).
- **`tsdp`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `TSDP` alone on L21. not read: occurrence — `TSDP` at L21 stands in the opening, which is not read.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L55. not read: occurrence — `Simulation` at L55 is a simulation of polyphony in the work process, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `Ontological Exploit` (near `alex`). occurrence: `Ontological Exploit` is not Alex.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth`, a place of the struggle between Kael and Juna named once (L138), not the Guardian.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Integrierten Kohärenz-Protokolls` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence: the title and the report's own name for itself; `Kohärenztheorie der Wahrheit` a borrowed lens.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` names the false universe (L84), not LogOS.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: AEGIS the guardian of the high-coherence state; Kael, Juna and the Guardians prisoners in this false universe, Logos-Prime (L84).
- **`q9-moonshine-link-boundary`**: Juna able to use the Moonshine-Link, a metaphorical adaptation of quantum entanglement, Monstrous Moonshine (L124).

**Not promoted:** the four throughlines and dimensions, K_1/K_0, Mosaik-Strategie and Mosaik-Struktur, Slots, Resonanz-Kodex, Golden Sources, Logos-Prime, AEGIS-Falle, Buffering Capacity, Intrusive Thoughts, the borrowed concepts.

**One reader**: aegis, kael, juna, kiko, nyx, lex, guardians, moonshine-link, multiplizitaet, dkt, algorithmische-melancholie, risse, entropie and the records q1, q9. `kohaerenz`, `tsdp` and `ueberwelt` are occurrences. **Never read L17–L23, L33–L59 or L212–L221.**

**Chapter readings**: none — the report names Slot 12 as an example (L178), no chapter.
