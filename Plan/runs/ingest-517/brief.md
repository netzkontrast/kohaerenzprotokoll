# Brief — readings from document 517 (step 6)

1 document, one reader, one batch: `ingest-517`. Files go to `Plan/runs/ingest-517/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 517 | `roman-plot-kohaerenz-protokoll-glitch` | 2025-10-15 | „the Glitch plot outline" (an unsigned German plot outline) | an alternative plot outline in three acts with its own cast (Aris Thorne, Elara Vance, Silus, the company Aethelred) in a simulated world (L71); it names no figure of the novel (AEGIS, Kael, Juna each 0); a draft, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (188 lines for `roman-plot-kohaerenz-protokoll`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: an outline with its own figures and world; a reading would put another plot under the novel's terms (precedent: 471, 486).

## Pages — document 517, `roman-plot-kohaerenz-protokoll-glitch`

- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L109. not read: light pass — the outline's own plot and figures, not the novel's term.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Julia` alone on L33. not read: light pass — the outline's own plot and figures, not the novel's term.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: light pass — the outline's own plot and figures, not the novel's term.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L25, L35, L37, L49, L71, L113, … (8 lines); `Glitches` L25, L49, L71, L113, L131, L148. not read: light pass — the outline's own plot and figures, not the novel's term.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L71. not read: light pass — the outline's own plot and figures, not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `neuronalen Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`), `Quanten-Dekohärenz` (near `koharenz`). an occurrence: the outline's own world, light pass.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). an occurrence: the outline's own world, light pass.


**Record entries:** none.

**Not promoted:** the outline's cast (Aris Thorne, Elara Vance, Silus, Aethelred), its acts and sections, the Glitches as its own device, and the borrowed concepts (several named after people).

**No reader**: no readings are written.

**Chapter readings**: none — the document names no chapter.
