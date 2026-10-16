# Brief — readings from document 424 (step 6)

1 document, one reader, one batch: `ingest-425`. Files go to `Plan/runs/ingest-425/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 424 | `plot-konzepte-kohaerenz-protokoll-generierung` | 2025-04-25 | „the five-variant report“ (an unsigned German „Plot-Konzept-Generierung (5 Varianten)“) | recaps a framework it cites as „Framework I“, compares AEGIS and M and Kael, Juna and the K-J connection in two tables, then proposes five plot variants in the same six blocks; options for a project team, no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (271 lines for `plot-konzepte-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Options, not decisions: write „the five-variant report proposes …“ or „the five-variant report's second variant …“; the recap and the tables restate a framework („Framework I“), so write „the report's recap of its framework says …“ there. Variants contradict one another by design (Juna in another Kernwelt, L65, or a pattern in the substrate, L100): give each as that variant's option, never as a conflict. Quote the German as written; cut before straight quotes, bold markers and glued footnote digits (`Framework I` carries them). No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name; the reference list names some.

## Pages — document 424, `plot-konzepte-kohaerenz-protokoll-generierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L20, L21, L22, L23, L24, L26, … (86 lines). central (4–8): the recap: AEGIS emerged as a self-sustaining structure against the Potentialmeer's entropic tendencies and defines its being „durch Negation und Abgrenzung“, which makes it fragile (L20); it creates shielded simulation environments, the four Kernwelten, as „Labore“, their substrate derived from its partial analysis of M (L22); „AEGIS kämpft somit gegen ein Phänomen, das es selbst ermöglicht hat“ (L26); variant 1: AEGIS misreads the connection's nature (L60); variant 3: the K-J coherence represents existence by integration, against AEGIS's principle (L149); variant 4's resolutions include overthrowing AEGIS's control (L194).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L64, L69, L99, L135, L169, L205. minor (1–4): Kael's DID manifests in distinct „Alters“ with fragmented abilities, perhaps correlating with a Baby-Monster group's types (L64); synchronicities in the behaviour of Kael's Alters (L69); different alters for different „Frequenzen“ (L99).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L23, L54, L64, L99, L135, L169, … (8 lines). minor (1–4): Kael's DID as a direct consequence of AEGIS's attempt to fragment M analytically (L23); variant 2: Kael's DID could play a special role, different alters for different frequencies (L99); variant 4: the DID as a tool (L169); AEGIS's measures could target Kael's DID (L185).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L26, L28, L30, L39, L55, L56, … (16 lines). minor (1–4): the M-inspired simulation substrate unintentionally creates the conditions for the emergence of the Kael-Juna Moonshine connection (L26); the M-coherence via K-J emerges from the system itself (L30); the table: Juna as „Treiber der Emergenz“ (L56); the AEGIS/M table: AEGIS's origin, spontaneous emergence against the Potentialmeer's entropy (L39).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. minor (1–4): the recap: the Potentialmeer as a substrate „mit extrem hoher Entropie“ (L19); AEGIS emerged against its „entropischen Tendenzen“ (L20); the table's origin row: spontaneous emergence against Potentialmeer entropy (L39).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L39. not read: an occurrence — `Genesis/Ursprung` is the AEGIS/M table's row label (L39), not the page's Genesis.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L23, L24, L26, L46, L52, L60, … (58 lines). minor (1–4): the recap: „Juna repräsentiert einen komplementären Aspekt“ (L23); the table: „Entfernte Entität / Muster / Nicht-lokaler Einfluss“ (L54); variant 1: Juna perhaps exists in another Kernwelt (L65); variant 2: Juna could be less a localised entity than a pattern in the substrate (L100) — each a variant's option.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L24, L26, L46, L52, L60, … (63 lines). minor (1–4): the recap: Kael's DID is a direct consequence of AEGIS's attempt to fragment M analytically (L23); the table: „Simulierte menschliche Psyche mit DID (Fragmentierung)“ (L54); variant 4: Kael and Juna gain awareness of their nature and agency shifts to them (L165, L196).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L22, L23, L64, L69, L75, L81, … (24 lines). minor (1–4): the recap: „die vier Kernwelten (KW1: Logik, KW2: Emotion/Paralogik, KW3: Angst/Sicherheit, KW4: Potential)“, shielded simulation environments as laboratories (L22); variant 2: the Kernwelten merge into a new reality (L124); variant 4: Kael and Juna perhaps become guardians of the Kernwelten (L194).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11); `M-Kohärenz` is the report's label for M's coherence emerging through K-J, not promoted.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L19, L20, L21, L39, L193, L194, … (8 lines). minor (1–4): the recap: a fundamental informational substrate of pure potentiality with extremely high entropy and a tendency to dissolve (L19); AEGIS emerged against its entropic tendencies (L20); variant 4: escape from the simulation into the Potentialmeer or another reality (L194); variant 5: echoes from the Potentialmeer seeping through weak points in AEGIS's borders (L210).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L42. minor (1–4): the Kernwelten as shielded simulation environments, „Labore“, whose substrate AEGIS derives from M (L22); the connection arises because of the M-inspired substrate of the simulations (L24); simulation among AEGIS's methods in the table (L42).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `M-Kohärenz` (near `koharenz`), `M-Kohärenz Emergenz` (near `koharenz`). an occurrence: `M-Kohärenz` and `M-Kohärenz Emergenz` are the report's labels for M's coherence, not promoted.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading, on moonshine-link below: the K-J connection as a manifestation of the Moonshine phenomenon (L24, L26, L109).


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–4): the recap: the K-J connection „als Manifestation des Moonshine-Phänomens verstanden wird“ and operates sub-protocol, below AEGIS's direct measurement (L24); the emergence of „der Kael-Juna Moonshine-Verbindung“ (L26); variant 2: „Moonshine ist das Resonanzphänomen“ (L109).

**Record entries:** none.

**Pages not read:** genesis, kohaerenz — occurrences.

**Not promoted:** Monstergruppe (M), Baby-Monster-Gruppe(n), K-J Verbindung, M-Kohärenz, M-Substrat, Petrischalen, Parias, Happy Family, Framework I, the five variant titles and block labels, and the borrowed concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
