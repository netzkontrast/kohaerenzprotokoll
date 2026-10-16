# Brief — readings from document 528 (step 6)

1 document, one reader, one batch: `ingest-528`. Files go to `Plan/runs/ingest-528/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 528 | `cyberpunk-roman-kohaerenz-protokoll-ubersetzung` | 2026-04-26 | „the interface translation“ (an unsigned German specification essay) | translates an earlier figure-and-image concept into an interface design language for the novel: Slow and Fast Kernel, a roster of thirteen numbered parts, colour and glitch rules, an escalation module; it calls its architecture „radikal isomorph“ (L17), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (162 lines for `cyberpunk-roman-kohaerenz-prot`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design translation: write „the interface translation maps … to …“; each part's entry is its proposed visual identity, never canon. **The source concept and several parts are named by earlier names and by other first names (L11, L31, L81, L88, L89, L91, L98, L99, L102): quote only spans that contain no name other than a current one (Kael, Lex, Alex, Isabelle, Selene, Argus, Nyx, Moros, Oblivion, Kiko, Lia, Rhys, Silas), and never write any other name.** The yellow palette (L71–L75) is never quoted or described. No gendered pronoun for any figure in our own prose; quotations stay verbatim.

## Pages — document 528, `cyberpunk-roman-kohaerenz-protokoll-ubersetzung`

- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L81, L88, L89. minor (1–4): number 03, „das Intrusion Detection System an der Grenze zwischen den Kernen“, caught in permanent hypervigilance (L89 — quote from „operiert als“; the line opens on another name).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L92. minor (1–4): number 11, the meta-cognition: fleeing emotional experience into pattern recognition, a bird's-eye view of reality's code (L92).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L90. minor (1–4): number 09, the elitist façade: masking, inverting powerlessness through elitist, toxic dominance (L90).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L11. not read: the hit is an earlier name in the title (L11); Juna is not named.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L87, L121, L129. minor (1–4): number 01, the primary executive protocol (L87 — quote from „Als *Kael*“); a dominant instance from the Slow Kernel in the master-terminal principle (L121).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L100. minor (1–4): number 07, the freeze state in which space contracts (L100).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L81. not read: an occurrence (L81).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L88, L121, L140. minor (1–4): number 02, „das Mikroskop der reinen Logik“, eliminating every organic curve (L88 — quote from „in *Lex*“; the line opens on another name).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L73, L81, L101. minor (1–4): number 08, „dem flackernden Paradoxon aus Sehnsucht und panischer Flucht“ (L101); L73 is the yellow palette — not read.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L99. minor (1–4): number 10, „dem existenziellen Gravitationskollaps“ (L99 — quote only that span; the line names an earlier name).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L111. not read: an occurrence (L111).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L98, L121, L140. minor (1–4): number 06, „das destruktive Fehlerprotokoll“ (L98 — quote only that span; the line names an earlier name).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L99. minor (1–4): number 13, split off with Moros (L99 heading — quote only a name-free span, or describe without quotation).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L102. minor (1–4): number 04, „die thermale Überlastung“ (L102 — quote only that span; the line names an earlier name).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L31. not read: an occurrence — the bunker's cracks in the source concept (L31), a line that names an earlier name.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L91, L121. minor (1–4): number 05, „stabilisierendes Puffer-Protokoll“ neutralising hostile signals through distance (L91 — quote from „Selene fungiert“; the line opens on another name); a dominant Slow Kernel instance (L121).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L102. minor (1–4): number 12, split off with Rhys (L102 heading — quote only a name-free span, or describe without quotation).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17. minor (1–4): the interface structure mirrors the TSDP trauma model exactly (L17 — cut before any person's name).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L56. not read: an occurrence — `Simulation` in a table cell (L56), not the page's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Maschine` (near `koharenz`). an occurrence: `Kohärenz-Protokoll` the title's subject; `Kohärenz-Maschine` the Slow Kernel's other name (L23).


**Record entries:** none.

**No chapter readings**: no chapter is named.

**Not promoted:** Slow Kernel, Fast Kernel, Kohärenz-Maschine, Kollaps-Maschine, the colour palette, the line grammar, the escalation tiers, the master-terminal principle, NovelOS and the writing tools, Interface Brutalismus, and the source concept.

**One reader**: every page above.
