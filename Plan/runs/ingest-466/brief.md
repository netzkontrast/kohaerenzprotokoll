# Brief — readings from document 466 (step 6)

1 document, one reader, one batch: `ingest-466`. Files go to `Plan/runs/ingest-466/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 466 | `roman-outline-kohaerenz-protokoll-strategie` | 2025-05-03 | „the strategy outline“ (an unsigned German chapter outline with English field labels, „Strategisches Roman-Outline“, L11) | a Prolog and Chapters 1–10 written out, Chapters 15, 25, 38 and 39 as sample continuations (L255), a summary table; the Kohärenz Protokoll a mystery whose nature shifts between chapters, the world revealed as a simulation in Chapter 25; an early outline with figures absent elsewhere, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (373 lines for `roman-outline-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline: write „the strategy outline plans …“; its field labels (Core Theme, Plot Summary, …) are its template; Chapters 11–39 are not written (L251) and the later ones are samples (L255). Its own figures (a scientist, an ally, the Sentient Echo) and Chrono-Weave are its own; describe them without promoting them. The export lost 24 concept headings (`- : …`) — never guess them. No gendered pronoun for Kael or AEGIS — use the names (quotations verbatim, including the document's „ihm“). Cut before inner quotes, bold and italics.

## Pages — document 466, `roman-outline-kohaerenz-protokoll-strategie`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L26, L31, L37, L39, … (57 lines). central (4–8): in the Prolog an omnipresent but faceless controlling instance, only hinted at (L17), its strategy surveillance and keeping the status quo (L19); in Chapter 4 active suppression and censorship of information (L105); in Chapter 9 justifying its methods by higher goals (L213); Chrono-Weave as a core component of the protocol in Chapter 10's AEGIS field (L234); in Chapter 25 keeping the simulation's integrity and credibility (L284); in Chapter 38 a desperate attempt to regain control (L306).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L16, L17, L18, L25, L36, L37, … (69 lines). central (4–8): Kael's psychological core conflict introduced as cognitive dissonance (L25), the table's internal conflict driver for Kael (L353); the fragmented memory as a central trope (L89); Kael's motivation and shift per chapter as the outline gives them (Prolog L16–L18 and the chapter fields); the ending open on the ultimate fate (L327).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–4): the Kohärenz Protokoll first named with function and purpose unclear (L45); in Chapter 8 a question between technology, rules, ideology or something else, its vagueness a weapon (L199); in Chapter 25 the simulation's mechanism (L291); in the table a central mystery and tool of control (L354).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Glitch` L125, L128, L134, L136, L146, L156, … (11 lines). central (4–8): the Glitch in Chapter 5, „Risse im Fundament“ (L121), possibly an unintended side effect of the protocol (L134); further glitches as the census lists them (L125, L128, L136, L146, L156).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L235, L278, L282, L283, L284, L285, … (16 lines). minor (1–4): the twist of Chapter 25, „Die Wahrheit der Simulation“ (L278): the protocol revealed or strongly implied as the mechanism that keeps the simulation (L291); the table's simulation twist, which redefines the conflict (L364); the AI might know of the simulation (L294).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). an occurrence: `Protokoll` is the Kohärenz Protokoll, not this page's protocol.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kollabierende Kohärenz` (near `koharenz`). read on kohaerenz (above): the protocol's name; `Kollabierende Kohärenz` is Chapter 38's title.
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Der Architekt` is Chapter 4's title.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). an occurrence: `Protokoll` is the Kohärenz Protokoll, not this page's protocol.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). an occurrence: `Protokoll` is the Kohärenz Protokoll, not this page's protocol.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). an occurrence: `Protokoll` is the Kohärenz Protokoll, not this page's protocol.


**Record entries** (one file, formatted as earlier entries):
- **`q8-aegis-after-the-vortex`**: the strategy outline has AEGIS in Chapter 38 desperately trying to regain control (L306) and leaves the ultimate fate open in Chapter 39 (L327); recorded.

**Chapter readings** (batch `ingest-466-kap`, `Plan/runs/ingest-466-kap/readings/kap-NN--roman-outline-kohaerenz-protokoll-strategie.md`, formatted as the files in `Plan/runs/ingest-446-kap/readings/`): the outline's Prolog „Das Flackern“ (L13) as **kap-00**; **kap-01** „Die Stimme im Rauschen“ (L33); **kap-02** „Der Test“ (L55); **kap-03** „Echos der Vergangenheit“ (L77); **kap-04** „Der Architekt“ (L99); **kap-05** „Risse im Fundament“ (L121); **kap-06** „Der Köder“ (L142); **kap-07** „Die Allianz der Fragmente“ (L164); **kap-08** „Das Phantom-Protokoll“ (L186); **kap-09**, titled after a scientist's perspective (L207 — never write the name; describe as a scientist's perspective); **kap-10** „Die Chrono-Weave Anomalie“ (L228); **kap-15** „Der Pakt mit dem Echo“ (L257); **kap-25** „Die Wahrheit der Simulation“ (L278); **kap-38** „Kollabierende Kohärenz“ (L300); **kap-39** „Das Offene Ende“ (L323). Each: the title and the plot summary in one or two sentences, attributed to the outline; chapters 15, 25, 38, 39 as its sample continuations. Quote titles only where `--find` resolves them; otherwise describe.

**Not promoted:** Chrono-Weave, the Sentient Echo, the scientist and ally figures, Phantom-Protokoll, Kognitive Dissonanz, the field labels, and the tropes.

**One reader**: every page above, the Q8 entry and the fifteen chapter readings.
