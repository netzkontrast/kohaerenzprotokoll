# Brief — readings from document 345 (step 6)

1 document, one reader, one batch: `ingest-346`. Files go to `Plan/runs/ingest-346/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 345 | `a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll` | 2025-10-15 | „the learner's glossary“ (an unsigned English glossary in four sections) | a conceptual framework for readers explaining AEGIS, Kael and the alters, the Foundation, the Void, the four Core Worlds, Juna/V and the Moonshine-Link, with outside concepts as lenses and German names glossed in brackets; it separates „real-world“ science from „in-world“ terms and makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (132 lines for `a-learner-s-glossary-for-the-w`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A glossary: write „the learner's glossary explains / defines …“; its definitions are its own account for readers, not decisions. Quote the English as written; the German names it brackets are its glosses. The Core World names are worlds, not the Guardians of the same stems.

## Pages — document 345, `a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L21, L22, L23, L27, … (23 lines). central (3–6): the story's primary antagonist (L19); its identity by negation (L21); its guiding principle „Kohärenz statt Wahrheit“ (L22); its central flaw, the Paradox of Misaligned Coherence (L23); the Void as the state from which AEGIS emerged (L43); the Core Worlds as its controlled environments (L47).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L29, L72, L99. minor (1–3): the alters as Kael's parts (L29, L72, L99) — say what the lines state.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L119, L121, L128, L130, L131. minor (1–3): Juna/V as not a traditional character (L121), an „ontological exploit“ (L124).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L23, L25, L27, L29, L30, … (22 lines). central (3–6): the protagonist whose goal is co-awareness, communication and cooperation between all identities (L30); his structure grounded in a real-world psychological model, TSDP (L103); the alters as his parts (L29) if the line says so; his link to Juna/V (L128).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Die Kernwelten` L45. minor (1–3): the Core Worlds as distinct simulated realities AEGIS creates as controlled environments (L45, L47) and their table of purposes (L52, L53).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L106. minor (1–3): Kiko placed among the Emotional Parts as the frightened child (L106).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L52. minor (1–3): the table row naming the Konstrukt-Stadt (L52) — what the line says of it.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L105. minor (1–3): Lex among the Apparently Normal Parts as the analytical and logical alter (L105).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L126. minor (1–3): the name for the mysterious, non-local connection between Kael and Juna/V (L128); the entanglement concept used as a metaphor (L130).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L106. minor (1–3): Nyx among the Emotional Parts as the protector/fighter (L106).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L41. minor (1–3): „Das Potentialmeer“ as a heading of the world section (L41), what the lines under it say.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L43. minor (1–3): „Risse“ glossed as cracks (L43) — what the line says of them.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L29, L101. minor (1–3): the real-world psychological model, the Theory of Structural Dissociation of the Personality (L101, L103); Kael's structure grounded in it (L29).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `ontological exploit` (near `alex`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `kohaerenz`: `Kohärenz statt Wahrheit` (near `koharenz`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.
- `personas`: `Theory of Structural Dissociation of the Personality (TSDP)` (near `persona`). occurrence: `ontological exploit` is read on juna, not alex; the Core World names are worlds, not the Guardians; `Kohärenz statt Wahrheit` is read on aegis; TSDP's full name is read on tsdp, not personas.


**Pages not read:** `kohaerenz` (L11 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** the glossary's English headwords as terms (The Foundation, The Void, Nothingness Noise, Core Worlds), ontological exploit, and the lens concepts (IIT and Phi, Gödel, paraconsistent logic, autopoiesis, entropy, emergence, entanglement).

**One reader**: aegis, kael, alters, juna, kern-welten, kiko, konstrukt-stadt, lex, moonshine-link, nyx, potentialmeer, risse, tsdp.

**Chapter readings**: none — the glossary names no chapter.
