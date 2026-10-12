# Brief — readings from document 279 (step 6)

1 document, one reader, one batch: `ingest-280`. Files go to `Plan/runs/ingest-280/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 279 | `kohaerenz-protokoll-synthese` | 2026-04-28 | „the final validation brief“ (an unsigned English synthesis with German summaries) | a final architecture validation in four parts — eight axes with verdicts, appendices A–H, audit logs with gate reports, and a plot-outline-ready handoff: the truth-rotation exposing AEGIS as the Kollaps-Kern, two Dramatica storyforms, Juna as composite and Witness Function, the Wahrheits-Vortex at the climax, the reader as substrate; it calls its resolution „a singular, canonical resolution“ (L19) and marks its gates `PASS`, its claims |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (356 lines for `kohaerenz-protokoll-synthese`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A validation brief: write „the final validation brief judges / places / calls …“; „canonical“, the verdicts and `PASS` are its own labels, never applied. **Do not read or cite L101–L104 or L181–L222** (excluded for privacy). Kernel symbols are lost (empty parentheses); straight and curly apostrophes are mixed — match the line.

## Pages — document 279, `kohaerenz-protokoll-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L43, L67, L87, L99, L107, L111, … (29 lines). central (3–6): the canonical mapping previously assigned it Coherence; the inversion exposes its claimed coherence as the true Kollaps-Kern (L43); Storyform B tracks its rigid, functional tragedy (L67); at the Wahrheits-Vortex it isolates Kael's fragments and its operational closure is revealed as the engine of entropy (L159–L161); its exclusionary suppression generates Landauer heat (L277).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L87, L107, L341. minor (1–3): the state after the vortex (L87, L341).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Chaitin-Konstante` alone on L173. minor (1–3): Juna's status as an amalgam of Gödel-Satz, Chaitin-Konstante and external observer (L173), the German summary.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L25, L117, L119, L121, L193, L270. minor (1–3): the DKT positioning information erasure as the primary thermodynamic engine of narrative reality (L117); the first axis, trauma and erasure as engines of progression (L25).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L117. not read: occurrence — `Entropie` at L117 is read on dkt.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L31, L89, L91, L109, L145, L151, … (18 lines). central (3–6): operating through an orbifold construction to access erased data (L31); „verified as a controlled composite“, a fifth position outside the Dramatica quad, the Zeuge-Funktion at the climax, not solving the plot by intervention (L91); IC in Storyform A, outside Storyform B (L177, L282); candidate (e) rejected (L175).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L43, L47, L87, L91, L99, L109, … (28 lines). central (3–6): Storyform A tracks his journey toward Funktionale Multiplizität (L47); at the vortex his fragments isolated (L159); in the silence „He embodies the dialetheia“ (L339); the gardener of the sea after the inversion (L99).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L169. minor (1–3): among the unreliable narrators representing the alters (L169).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: occurrence — the title (L13).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L169. minor (1–3): among the unreliable narrators representing the alters (L169).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L169. minor (1–3): among the unreliable narrators representing the alters (L169).
- **`moonshine-link`** (central, 3–12 quotations): the census's surfaces — `Moonshine-Link` L19, L31, L91, L109, L129, L145, … (10 lines). central (3–6): Juna's Moonshine-Link to Kael „not a mere literary metaphor for quantum entanglement“ (L145); the fourth axis (L31); the Witness Function's layers (L151) only as they concern the link.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L141. minor (1–3): the Monster Group and VOA as the rigid foundation of the Witness Function and the Mosaik-Herz (L141).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L47. minor (1–3): Storyform A's goal, Funktionale Multiplizität (L47).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L95, L99, L339. minor (1–3): only if L95, L99 or L339 characterise the Nichts-Rauschen; else not read.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L169. minor (1–3): among the unreliable narrators representing the alters (L169).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L33, L137, L169, L245. minor (1–3): the narrative Risse modelled by paraconsistent logic (L245); L33, L137 only if they name the Risse.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L41, L205, L209, L210. minor (1–3): „the primary structural and thematic pivot of the narrative“ (L43); the audit row (L277) and L205–L210 only outside L181–L222 — L205, L209, L210 are excluded.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L27, L39, L193, L194, L271, L299. minor (1–3): identity fractured into ANPs and EPs (L27); TSDP at L39 only if it adds; never L193–L194.
- **`vortex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vortex` alone on L23. minor (1–3): the Story-Mind Vortex and its eight axes (L23); the Wahrheits-Vortex at the climax (L87); the driver flipping from Action to Decision (L129).

- **`kollaps-kernel`** (minor, 1): AEGIS's claimed coherence „exposed as the true“ Kollaps-Kern (L43).
- **`kohaerenz-kernel`** (minor, 1): only if L43 gives the Kohärenz-Kern to Kael; else not read.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `chaitin-konstante`: `Chaitin` (near `chaitinkonstante`). reading: `Chaitin` in Juna's candidates, read with L173.
- `genesis`: `Genesis-Krise` (near `genesis`). occurrence unless the line characterises the Genesis-Krise; read on genesis only then.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Kern` (near `koharenz`). occurrence: the title; `Kohärenz-Kern` read on kohaerenz-kernel.
- `kohaerenz-kernel`: `Kohärenz-Kern` (near `koharenzkernel`), `Kohärenz-Kern` (near `koharenzkernelk1`). reading: `Kohärenz-Kern`, Kael's after the rotation (L43), if the line says so.
- `kollaps-kernel`: `Kollaps-Kern` (near `kollapskernel`), `Kollaps-Kern` (near `kollapskernelk0`). reading: `Kollaps-Kern`, AEGIS's claimed coherence exposed as it (L43).
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `Mnemosyne-Archipel` a world's name, the vortex's setting (J49).
- `vortex`: `Story-Mind Vortex` (near `vortex`), `Wahrheits-Vortex` (near `vortex`), `Vortex Inversion` (near `vortex`). reading: `Wahrheits-Vortex` (L87), `Story-Mind Vortex` (L23), `Vortex Inversion`.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: Algorithmische Melancholie after the Wahrheits-Vortex (L87, L341).
- **`q9-moonshine-link-boundary`**: the link not a mere metaphor for quantum entanglement (L145); Juna accesses erased data through an orbifold construction (L31).

**Not promoted:** the eight axes and verdicts, the Story-Mind Vortex as a label, the Witness Function's three layers, the gate reports, Phönix-Mode, the Foundation as Monster Group bedrock.

**One reader**: every page above and the two records. Never L101–L104 or L181–L222.

**Chapter readings**: none — „39 fragmented chapters“ (L169) is a total.
