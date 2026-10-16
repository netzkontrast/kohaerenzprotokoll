# Brief — readings from document 426 (step 6)

1 document, one reader, one batch: `ingest-427`. Files go to `Plan/runs/ingest-427/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 426 | `binnenerzaehlungen-kohaerenz-protokoll-heldinnenreise-strukt` | 2025-04-26 | „the inner-stories outline“ (an unsigned German „Binnenerzählungen für Kohärenz Protokoll (39 Kapitel - mit Heldinnenreise)“) | three parts of numbered inner stories — 13 steps of a Heldinnenreise (Kapitel 1-13), 12 cycle steps (Kapitel 14-26) and 14 steps of a Heldenreise (Kapitel 27-39) — each with a place and characters; Parts 2 and 3 said to stay as in an earlier draft (L33, L50); a plan, no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (66 lines for `binnenerzaehlungen-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the inner-stories outline plans …“ or „the inner-stories outline's Part 2 …“; it gives steps, not chapters — Part 1's 13 steps, Part 2's 12 and Part 3's 14 do not map one to one onto the chapter ranges in its headings (L13, L31, L48), so never number a step as a chapter. Its worlds are named after real mathematicians (L17, L21, L42): never write those world names nor their abbreviations — write „the logical world“, „the network world“, „the world of focused intention“, and `B-Welt`/„the Baby-Monster world“ only as the document writes it. The recurring nightmare motif (L45, L54) is the document's Kernwunde for Kael: name it as that, without detail. Quote the German as written; cut before straight quotes, bold and italics markers. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim).

## Pages — document 426, `binnenerzaehlungen-kohaerenz-protokoll-heldinnenreise-strukt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L18, L19, L21, L35, L41, … (17 lines). minor (1–4): AEGIS presents the logical world as the ideal (L17) and forces Kael to split off a part (L18); AEGIS manipulates the channels between the Kernwelten (L41); AEGIS's defences use logical paradoxes and personalised fear simulations (L53); at the climax AEGIS collapses under its own contradictions or is absorbed by Kael/M (L59).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L23, L24, L38, L52, L61, L65. minor (1–4): Part 1: in the crisis the K-J connection intensifies and Juna appears perhaps as a vision showing the way to integration (L23); Part 2: an unexpected hint from Juna (L38); Part 3: Juna as navigator (L52), Kael/M meets Juna in the Potentialmeer (L61), and the closing image of both exploring it (L65).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L18, L19, L20, L21, L22, … (39 lines). central (4–8): Part 1: Kael lives in a strictly logical world presented by AEGIS as ideal and suppresses the intuitive side (L17); Kael splits off a part to stay (L18); in the crisis Kael recognises the need for the suppressed side (L22) and resolves the conflict by using both (L25); Part 2: AEGIS challenges Kael's new balance (L35), Kael glimpses the raw Potentialmeer (L43); Part 3: Kael reaches AEGIS's core and confronts it with M's irreducible nature (L54), becomes „Kael/M“ (L58), and steps out into the Potentialmeer free of AEGIS's simulations (L60).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L41. minor (1–4): AEGIS manipulates the communication channels between the Kernwelten, corrupting data (L41); the outline's worlds — the logical one, the network one, the Baby-Monster world, the world of focused intention — are not called Kernwelten except there (describe, never name them).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11), and „Innere Kohärenz“, the name of Part 1's twelfth step, Kael's inner calm (L28), not the page's term.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L43, L57, L59, L60, L61, L62, … (9 lines). minor (1–4): the simulation breaks down and Kael glimpses „das rohe Potentialmeer außerhalb von AEGIS' Kontrolle“ (L43); Part 3's ending is set in it: Kael/M steps out into it (L60), meets Juna there (L61), and begins to shape new structures in it (L63).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L43. minor (1–4): during an experiment the simulation briefly collapses (L43); Kael/M free „von AEGIS' Simulationen“ (L60); the decision to escape the cycle of the simulations (L46).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `garten-der-stillen-praesenz`: `Garten` (near `gartenderstillenpraesenz`), `Garten` (near `gartenderstillenprasenz`). an occurrence: Kael's inner „Garten“ (L27, L29), not Juna's place.
- `kohaerenz`: `Innere Kohärenz` (near `koharenz`). an occurrence: „Innere Kohärenz“ a step's name.
- `moeglichkeits-garten`: `Garten` (near `moeglichkeitsgarten`), `Garten` (near `moglichkeitsgarten`). an occurrence: Kael's inner „Garten“ (L27, L29), not the Kern-Welt.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). an occurrence: the „Mosaik“ of Kael's abilities (L27), not the Mosaik-Herz.


**Record entries:** none.

**Pages not read:** kohaerenz — occurrences.

**Not promoted:** the four worlds named after mathematicians and their abbreviations, B-Welt, Cache-Konflikt, Wächterin, Wächterin-Anteil, Wächterin-Analogon, Kael/M, Kernwunde, Kissen, Trojaner, the outline's rooms, the steps' names, and the two journey structures.

**One reader**: every page above.

**Chapter readings**: none — the document names only chapter ranges in its part headings (L13, L31, L48), and its steps do not map onto chapters.
