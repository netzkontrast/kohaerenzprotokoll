# Brief — readings from document 524 (step 6)

1 document, one reader, one batch: `ingest-524`. Files go to `Plan/runs/ingest-524/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 524 | `research-prompt-kohaerenz-protokoll-final-architecture-md` | 2026-04-28 | „the final-architecture prompt“ (an English research prompt) | describes the novel's architecture for a research agent — two kernels, AEGIS, Kael, Juna, the Moonshine-Link, two storyforms and a Vortex Inversion, the Witness Function, the Reader as Substrate — and sets gates and axes to test it; it claims „This run produces canon.“ (L319), recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (936 lines for `research-prompt-kohaerenz-prot`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prompt that describes the architecture and asks for its testing: write „the final-architecture prompt describes/asks …“; its candidate answers (e.g. Juna's ontologies L491–L496) are options it lists, and the worked example (L880–L892) is an example, never a verdict. **Section 1.4 and the blocks fencing it (L137–L153, L298, L313) are personal material: never read, quote or cite any line in L137–L160, L298 or L313**, even where Kael or Juna is named there. Never write the names Michael, Julia, Shadow, „The Lost One“ or Isabella, nor any real person's name or a concept named after a person. No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim.

## Pages — document 524, `research-prompt-kohaerenz-protokoll-final-architecture-md`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L126, L128, L132, L133, L149, L393, … (17 lines). central (3–8): „Autonomous Entropic Gatekeeper for Integrity Systems“ (L126), „a tragic god“ and not the antagonist in a moral sense, a structure that emerged to preserve the protagonist (L126); Storyform B as „the functional tragedy of AEGIS attempting to maintain the simulation“ (L132); ontologically blind to the Moonshine-Link (L427); the rotation the prompt reports, „AEGIS = K₁, Kael's EPs = K₀“ (L393); in the worked example AEGIS migrates from K₁ to K₀ (L892, an example).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L243, L910. minor (1–4): one of the German terms to prefer over a translation (L910), in the request for a „cultural-tonal mirror“ (L243).
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L880. minor (1–4): the worked example's unit: „Each return is a Coheron“ (L880) — an example.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L15, L125, L391, L892. minor (1–4): Dual-Kernel Theory „serves as the in-world physics“, reality constituted by two computational substrates (L125); `DKT` in the worked example (L892).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L29, L37, L90, L128, L144, L171, … (22 lines). central (3–8): an entity that „operates outside AEGIS's perceptual range“, linked by a non-local Moonshine-Link, its status „deliberately unsettled“ (L128); Gate 2's question of its structural position (L282); the candidate ontologies the prompt lists (L491–L496) and Axis 8 as „The deliberately unresolved axis“ (L483) against a required verdict (L500) — say the prompt does not reconcile the two. Never cite L137–L160.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L127, L131, L133, L143, L147, L393, … (16 lines). central (3–8): the Main Character, TSDP glossed (L127); Storyform A as „the phenomenological journey of Kael toward functional multiplicity“ (L131); the loops of return-and-suffer preserving mutual information (L133); `Kael/M` as a possible Witness (L450); in the worked example Kael migrates from K₀ to K₁ (L892, an example). Never cite L137–L160.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence — the title in the frontmatter (L15).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L128, L282, L436, L437. minor (1–4): a connection modeled on entanglement, „a direct, intuitive grasping“ (L128); AEGIS ontologically blind to it (L427); L282, L436–L437 as the census lists them.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L914. minor (1–4): one of the German terms to prefer, „not "Mosaic Heart"“ (L914).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L911. minor (1–4): „Funktionale Multiplizität“ as a German term to prefer (L911); Storyform A's journey toward functional multiplicity (L131).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L243, L909. minor (1–4): one of the German terms to prefer (L909), with L243.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L243, L908. minor (1–4): one of the German terms to prefer, „not "rifts"“ (L908), with L243.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Truth-Rotation` alone on L609. minor (1–4): the Inversion Audit's „Truth-Rotation verdict“ (L609); the rotation of the truth-theory mapping to be tested explicitly (L134).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L127, L193. minor (1–4): the gloss of TSDP as a clinical model of Apparently Normal Parts and Emotional Parts (L127); L193 as the census lists it.
- **`vortex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vortex` alone on L15. minor (1–4): the Vortex Inversion as „The central narrative move“: at the climax the two storyforms invert (L133), to be expressible as a specific moment in the plot (L273); `Wahrheits-Vortex` offered as a candidate German term (L915). L15 (frontmatter) is an occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Kern` (near `koharenz`). an occurrence: `Kohärenz Protokoll` the title; `Kohärenz-Kern` a German term for the kernel, read on kohaerenz-kernel if at all.
- `kohaerenz-kernel`: `Kohärenz-Kern` (near `koharenzkernel`), `Kohärenz-Kern` (near `koharenzkernelk1`). a reading: `Kohärenz-Kern` offered as the German for the Coherence Kernel inside German prose (L912) — one line on the page.
- `kollaps-kernel`: `Kollaps-Kern` (near `kollapskernel`), `Kollaps-Kern` (near `kollapskernelk0`). a reading: `Kollaps-Kern` offered as the German for the Collapse Kernel inside German prose (L912) — one line on the page.
- `vortex`: `Vortex Inversion` (near `vortex`), `Wahrheits-Vortex` (near `vortex`). a reading: `Vortex Inversion` and `Wahrheits-Vortex`, read on vortex above.


**Record entries:** none.

**No chapter readings**: no chapter is named (`Kap`, `Kapitel` 0; „roughly 39 chapters across three acts“ at L113 is a plan).

**Not promoted:** the gates, axes and blocks, the three Witness layers, the Reader as Substrate, the truth theories, Foundation and Sea of Potentiality (named once, undefined), `Kael/M` as a surface, the worked example's values, the concepts named after people, and Section 1.4.

**One reader**: every page above.
