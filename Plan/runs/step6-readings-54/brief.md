# Brief — readings from document 54 (step 6)

One document, one reader, batch `step6-readings-54`. Files go to
`Plan/runs/step6-readings-54/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 54 | `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` | 2026-04-29 | „the Technical Audit" | an undated, unsigned English „Technical Audit & Research Mandate" of about 1,270 words: instructions to a writer and a „writer LLM" over a physics-of-information reading of the novel, in numbered sections, eight Axes and one table (L21); it ends by calling the framework „structurally verified" and „ready for publication" (L40) |

Read first: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` („What the extraction ran
into") and `Plan/runs/<slug>/05-verify.txt` section A; then the document with `python3 scripts/read.py <slug>`.
It is 40 lines, but five headings are glued into paragraph lines (L3, L9, L17, L29, L36), so one line
can hold two sections. The table is a single line of pipes (L21). For each page, read its digest:
`python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Things `read.py --find` cannot do, and what to do instead.**
- It drops fragments under four characters. Cite `Lex`, `Nyx`, `Lia` and `DKT` through a longer
  phrase: „The alters— Lex, Nyx, Kiko, and Lia —must be treated as discrete functional modules."
  (L12), „Dual-Kernel Theory (DKT)" (L3).
- A quotation cannot start with a one- or two-digit number. „resolving 39 fragmented chapters"
  resolves; „39 fragmented chapters" does not.
- The export escapes underscores: quote `$K\_1$` exactly as the line writes it, or quote around it.

**Stance: record, never apply.** It speaks in mandates („must", „Mandate", „Required") to a writer
and a writer LLM. Its standing claims are the document's own and are said as such: „definitive
structural requirements" (L3), the column „Alignment Status" (L21), „structurally verified" and „ready
for publication" (L40). Say „the audit requires" or „the audit mandates", never that the novel does.
It is English: quote it as written, never translate it, and never put the page's German term inside
a quotation.

## Pages

**Central (4–10 quotations each):**
- **`kael`**:
  - Janetian action systems, ANP and EP as informational buffers (L11);
  - the alters as modules (L12);
  - the Truth-Rotation's mandate (L13);
  - the storyform that tracks Kael (L19);
  - in the Vortex Inversion Mechanics, dropping the amnesic barriers and becoming
    mutual-information-dense, with the erasure of his structure overloading AEGIS's hardware (L38).
- **`aegis`**:
  - its „operational closure" (L7);
  - its „linear timeline" (L20);
  - its „deterministic clockwork" (L27);
  - the climax: its own hardware overloaded (L38);
  - „not destroyed but enters a state of permanent, broken paradox" under „Algorithmische
    Melancholie" (L39).
  - Two ends stand side by side, hardware overloaded (L38) and broken paradox (L39). The note's
    section 10 names this; state both.
- **`juna`**:
  - the Moonshine item: her ability to observe erased data is not „magic" but an involution on the
    VOA through an orbifold construction, outside AEGIS's linear timeline (L20);
  - „a living Gödel-sentence", her 5th position outside the Dramatica quad (L21);
  - the Witness Function (L32) and „Reader & Juna" (L30).
- **`moonshine-link`**: love „as a living dialetheia and a resonant Moonshine-Link" (L3); the
  Moonshine-Link item, the VOA over the Leech lattice (L20).

**Minor (1–4 quotations each):**
- **`alters`**: four named as modules, Lex, Nyx, Kiko and Lia (L12, L38). Four, where other sources
  count otherwise: Q3 (below).
- **`lex`**, **`nyx`**, **`kiko`**, **`lia`**: each named in the group of L12 and in the climax, L38.
  One reading each with that quotation. Write „not read" for a page only if the digest shows the
  page's lead is about something else entirely.
- **`tsdp`**: the Theory of Structural Dissociation of the Personality, its heading and its use for
  modularity (L9–L12).
- **`truth-rotation`**: „The Truth-Rotation: Architectural Mandate: Explicitly rotate the alignment."
  (L13). The text orders a rotation; it does not say one happens.
- **`dkt`**: „Dual-Kernel Theory (DKT)" heads Axis I (L3), with the kernels and Landauer's Principle.
  An English name for the page's term, placed by the sentence (J100). J106 does not apply: this
  expansion is the page's own.
- **`kohaerenz-kernel`** and **`kollaps-kernel`**: the Coherence Kernel (`$K\_1$`) and the Erasure
  Kernel (`$K\_0$`), „modeled through Landauer’s Principle" (L3); the „Kollaps-Kern" as the engine of
  history (L6); the K\_1 kernel the reader must synthesize (L36); the K\_1 substrate surviving at the
  end (L40). (J98, J99, J100)
- **`risse`**: „Treat "Risse" (cracks) in the Mnemosyne-Archipel as true contradictions—dialetheias."
  (L26), with its definition (L26).
- **`chaitin-konstante`**: „Chaitin’s Halting Probability ( $\\Omega$ )" as the „algorithmic
  randomness" novelty needs (L27).
- **`nichts-rauschen`**: the reader's effort counteracts the „Nichts-Rauschen" (nothingness static)
  (L31).
- **`algorithmische-melancholie`**: the label at L39 and what it heads.
- **`vortex`**: the „Vortex Inversion Mechanics" (L38); the climax as an „ontological rotation" in
  the server core of the Mnemosyne-Archipel (L36).
- **`resonanz-landschaft`** — the Mnemosyne-Archipel. Read sources gloss it as KW2's second name,
  „KW2 — Mnemosyne-Archipel (Resonanzlandschaft, Klimax-Setting)", and no read source separates the
  two, so its passages go on the paged world (J95). It is not the Guardian `mnemosyne` (J49).
  Passages: the server substrate (L6), the high-entropy environment (L9), where the Risse are (L26),
  the server core where the climax occurs (L36).
- **`mnemosyne-server-architektur`** — by the sentence: the climax „within the server core of the
  Mnemosyne-Archipel" (L36). Write a reading only if the digest's lead is that server as the
  climax's setting; otherwise „not read".
- **`telefon-stille`**: „The "Silence" of the foundational phone call must be treated as a
  high-density informational bedrock" (L40), what it is, and what survives in it. An English
  description of the page's referent, placed by the sentence (J100).
- **`overview/plot`** (page `plot`): the chapter count, „resolving 39 fragmented chapters" (L31) and
  „the 39-chapter mosaic" (L40). No chapter is named (`Kap` 0), so there are no chapter-page readings.

**Decided as occurrences — no file:**
- `ueberwelt`: „the simulation" (L23) is the simulated world in general (J30, J39).
- `landauer-signatur`: Landauer's Principle (L3, L6) is not the Landauer-Signatur (J53, J62, J81).
- `mosaik-herz`: the book's „mosaic structure" (L36) is not the Mosaik-Herz (J28).
- `goedel-gambit`: „a living Gödel-sentence" (L21) is not the gambit.
- `mnemosyne`: the Mnemosyne-Archipel is a world, not its Guardian (J49).
- `vergessener-schrein`: „trauma" (L9, L16) in general (J105).

## Records — one entry each, at most

- **`q8-aegis-after-the-vortex`**: what the audit makes of AEGIS after the climax. Its hardware is
  overloaded (L38), and it is „not destroyed but enters a state of permanent, broken paradox"
  (L39).
- **`q3-how-many-kern-welten-and-alters`**: four alters, named (L12, L38).
- **`q9-moonshine-link-boundary`**: only if a passage says where the link ends.

The heading is `## 2026-09-30 — \`technical-audit-research-mandate-the-kohaerenz-protokoll-fra\`,
2026-04-29, the Technical Audit`, then a bold one-line position, the quotations, and one closing line
in the record's own terms. For anything else that looks like a conflict, report it and write nothing.

## Before you finish

`python3 scripts/readings.py check step6-readings-54` shows no refusal. Report per page: the file
written or „not read" with why, and the lines cited.

Rules that apply: J28, J30, J39, J49, J53, J62, J81, J95, J98, J99, J100, J105, J106
(`Plan/runs/judgements.md`).
