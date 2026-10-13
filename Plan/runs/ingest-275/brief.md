# Brief — readings from document 274 (step 6)

1 document, one reader, one batch: `ingest-275`. Files go to `Plan/runs/ingest-275/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 274 | `blueprint` | 2025-07-29 | „the blueprint“ (an unsigned German plan, in an adviser's first person) | a plan in eight sections by a voice calling itself „Ihr Narrativer Architekt“: vision and principles, core concepts (AEGIS, Kael, Juna/V, Das Fundament, six Realitätsebenen with four Kernwelten), tension pairs, technique, tools and next steps; it reports a 39-chapter plot blueprint it does not contain, and calls itself „die ultimative Synthese“ (L11), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (97 lines for `blueprint`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the blueprint describes / proposes / lists …“; its next steps (L94) are open points, say so. Cut quotations before bold markers (`**AEGIS**` is bolded throughout) and inner quotes.

## Pages — document 274, `blueprint`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L30, L32, L38, L39, … (13 lines). central (3–6): „ein autopoietisches System“ from the Potentialmeer, radically closed (L38); the Paradoxon der Fehlausgerichteten Kohärenz, enforcing absolute coherence by control and fragmentation (L38); creator of the Kernwelten and Realitätsebenen (L42).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L79. minor (1–3): among the central metaphors (L79).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L29. minor (1–3): the respectful depiction of DID and trauma (L29).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L41. minor (1–3): only if L41 characterises emergence in the Fundament's integration; else not read.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L30. not read: occurrence — `Entropie` (L30) named as an abstract concept to embody, nothing said of it.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L46. minor (1–3): „Die mysteriöse Externe Ebene“, the unknown and connection, contrast to AEGIS's domain (L46); its nature still to be worked out (L94).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L40. minor (1–3): „Diese externe Entität oder Anomalie“ outside AEGIS's control, a non-local integrative force (L40); its nature still to be worked out (L94).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L30, L32, L39, L40, L41, … (12 lines). central (3–6): „ein System multiplen Bewusstseins“, aiming at functional multiplicity, not fusion, a dialetheic mind (L39); the thesis of true coherence by integration (L23).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L42, L44. minor (1–3): four psychological Kernwelten KW1-4, each with a function and aesthetic and watched by a Guardian (L44); simulated realities created by AEGIS (L42).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L83. minor (1–3): recommended as the central supporting frame of the novel (L83).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L44. minor (1–3): „KW1 (Konstrukt-Stadt) steril, logikbasiert“ (L44).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L39. minor (1–3): named with Nyx and Selene among Kael's parts (L39).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L40, L79. minor (1–3): Juna/V's link (L40); a central metaphor (L79).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L23. minor (1–3): „funktionalen Multiplizität“ as Kael's aim (L39); the thesis's acceptance of multiplicity (L23).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L39. minor (1–3): named with Lex and Selene (L39).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L38. minor (1–3): AEGIS arose from it (L38).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L32, L42. minor (1–3): „sechs distinkten Realitätsebenen“ (L42): four Kernwelten, the Überwelt, the Externe Ebene (L44–L46); the layered structure building tension (L32).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L47, L77. minor (1–3): „Risse“ as visual glitches, spatial distortions or logic errors marking the system's instability (L47); clues in environmental storytelling (L77).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L39. minor (1–3): named with Lex and Nyx (L39).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L39. minor (1–3): TSDP at L39 only if the line ties Kael's parts to it.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L45. minor (1–3): „Die digitale Überwelt von AEGIS“, a pure interface or operating system, sterile against the psychically rich Kernwelten (L45).

- **`guardians`** (minor, 1): each of the four Kernwelten „von einem Guardian überwacht“ (L44).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the Kernwelten's watcher, read on guardians.
- `emergenz`: `schwache Emergenz` (near `emergenz`). occurrence unless L41 reads it: `schwache Emergenz`.
- `guardians`: `Guardian` (near `guardians`). reading: one Guardian watching each Kernwelt (L44).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenz Protokoll 1.0` (near `koharenz`). occurrence: the title, `Kohärenz Protokoll 1.0` and the paradox, read on aegis.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). reading: `funktionalen Multiplizität` (L39).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: six Realitätsebenen, four psychological Kernwelten KW1-4 (L42–L44).
- **`q5-guardians-and-kern-welten`**: each Kernwelt watched by a Guardian (L44).
- **`c13-externe-ebene-beyond-the-simulation`**: the mysterious Externe Ebene as contrast to AEGIS's domain (L46), Juna/V outside AEGIS's control (L40).

**Not promoted:** the tension pairs, the Dramatica throughlines, Novelcrafter and the Single Source of Truth, the Meta-Erzähler, the AEGIS-Manifest, Kohärenz Protokoll 1.0.

**One reader**: every page above and the three records.

**Chapter readings**: none — it reports a 39-chapter blueprint it does not contain.
