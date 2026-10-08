# Brief — readings from document 219 (step 6)

1 document, one reader, one batch: `ingest-219`. Files go to `Plan/runs/ingest-219/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 219 | `plot-outline-for-kohaerenz-protokoll-a-journey-through-syste` | 2025-11-03 | „the journey outline“ (an unsigned English plot outline) | an English plot outline in three parts with approximate chapter ranges — a Heroine's Journey, a cyclical structure, a Hero's Journey — and three turning points (chapter 13, the chapter 17 midpoint, the Gödel Gambit in chapters 33–35), ending in AEGIS's algorithmic melancholy and an open ending; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (103 lines for `plot-outline-for-kohaerenz-pro`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plot outline: write „the journey outline plans …“ and name the part or chapter a line belongs to. English — quote as written; cut before inner straight quotes (German names stand in them); `--find` drops the digit in `KW1`–`KW3` — quote around it.

## Pages — document 219, `plot-outline-for-kohaerenz-protokoll-a-journey-through-syste`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L21, L25, L29, L31, L32, … (20 lines). central (3–6): AEGIS as an autopoietic AI whose imposed order defends against the chaotic Nichts Rauschen (L15) — cut before the inner quotes; deploying Guardians, gaslighting and manipulation in Part II (L59); Paradoxon X, its core tragic flaw, at the midpoint (L63); forced into a logical collapse by the Gödel-Gambit (L89); „AEGIS is not destroyed but is irrevocably transformed“, algorithmic melancholy (L98).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L46. minor (1–3): faced with annihilation, Kael's warring internal parts (Alters) forced into cooperation at the end of chapter 13 (L46).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L59. minor (1–3): Kael leveraging his analytical parts like Lex and Argus to probe the Überwelt (L59) — quote around the short names.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L25. minor (1–3): read L25 — the Konstrukt-Stadt and the Cache Kohärenz; decide reading or occurrence.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L88. minor (1–3): Kael executes the Gödel-Gambit; his integrated self becomes a living Gödel-Satz (L88) — cut before the inner quotes; the climax in chapters 33–35 (L84).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L59, L69. minor (1–3): AEGIS deploys Guardians, „specialized system agents“ (L59) — cut before the inner quotes; the misguided mission given to Kael by the Guardians (L69).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L32. minor (1–3): „The Juna/V Connection“ as a disruptive external influence AEGIS can neither model nor control (L32); growing stronger after the midpoint (L70); the Moonshine-Link provided by Juna/V (L89).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L25, L29, L31, L32, … (27 lines). central (3–6): Kael's initial existence in the Konstrukt-Stadt (KW1) (L25); his descent through the Kernwelten (L36); turning from victim to active investigator at the end of chapter 13 (L47); understanding AEGIS's core flaw at the midpoint (L63); functional multiplicity as his goal, not fusion (L82); his new role and the open ending (L99).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L36. minor (1–3): the Kernwelten as externalized representations of Kael's psyche (L36); KW2 Mnemosyne-Archipel as the domain of the EPs like Kiko (L38), KW3 Cerberus-Labyrinth as the domain of protective parts like Nyx (L39) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L38. minor (1–3): KW2 as the domain of the Emotional Parts like Kiko (L38).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); the outline writes coherence in English.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L25. minor (1–3): Kael's initial existence „unfolds within the Konstrukt-Stadt“, a hyper-logical, sterile environment, AEGIS's philosophy of control (L25).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L59. minor (1–3): Lex and Argus as Kael's analytical parts (L59).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L89. minor (1–3): aided by the Moonshine-Link provided by Juna/V, Kael presents his integrated state to AEGIS's core (L89) — cut before the inner quotes.
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L45. occurrence: `Entropy Nexus` is the gloss of the Entropie-Knotenpunkt (L45), not the Nexus.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L15. minor (1–3): AEGIS's order defends against the chaotic Nichts Rauschen (L15) — quote around the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L39. minor (1–3): KW3 as the domain of protective and defensive parts like Nyx (L39).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L31. minor (1–3): „The“ Risse as glitches in the simulation that are manifestations of Kael's suppressed trauma (L31) — cut before the inner quotes.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L82. minor (1–3): read L82 — Selene and functional multiplicity.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L59. minor (1–3): Kael probing the Überwelt (Overworld) and AEGIS's protocols in Part II (L59) — cut before the inner quotes.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` KW3's name (L39), read on kern-welten (J49).
- `entropie`: `Entropie-Knotenpunkt` (near `entropie`). occurrence: `Entropie-Knotenpunkt` is the crisis of chapter 13 (L45), not entropy as a term.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `Mnemosyne-Archipel` KW2's name (L38), read on kern-welten (J49).
- `nexus`: `Entropy Nexus` (near `nexus`). occurrence: `Entropy Nexus` is a gloss (L45).


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: AEGIS „not destroyed but is irrevocably transformed“, algorithmic melancholy, paraconsistent logic (L98).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link provided by Juna/V, the channel of the Gödel Gambit (L89).
- **`c4-guardians-and-aegis`**: Guardians as specialized system agents AEGIS deploys (L59), giving Kael a misguided mission (L69).

**Not promoted:** the journey structures, Paradoxon X, the Entropie-Knotenpunkt, Das Fundament, The Open Protocol, the meta-narrative devices.

**Two readers**, disjoint: (1) kael, juna, alters, argus, lex, kiko, nyx, selene, kern-welten, konstrukt-stadt, cache-kohaerenz; (2) aegis, guardians, goedel-gambit, moonshine-link, risse, nichts-rauschen, ueberwelt and the records q8, q9, c4.

**Chapter readings**: Kap 13, 17, 38, 39, by the session (`Plan/runs/ingest-219-kap/`).
