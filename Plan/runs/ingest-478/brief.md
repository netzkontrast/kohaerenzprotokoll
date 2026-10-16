# Brief — readings from document 478 (step 6)

1 document, one reader, one batch: `ingest-478`. Files go to `Plan/runs/ingest-478/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 478 | `from-monolith-to-mosaic-a-strategic-proposal-for-restructuri` | 2025-11-03 | „the mosaic proposal“ (an unsigned English strategic report, „From Monolith to Mosaic“) | proposes recasting the novel as a narrative mosaic of 39 short stories: alters' perspective stories, a cyclical second act with costs, AEGIS's origin as a first-person Genesis Log of the Ursprungs-Ich, and a table of story ideas for four Kernwelten; it calls this the optimal strategy (L76), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (79 lines for `from-monolith-to-mosaic-a-stra`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal: write „the mosaic proposal proposes …“; its story sketches are in future and conditional tense. L31 names a logician — never quote that line's name or the class named after it. Quote the English as written; cut before bold, escaped asterisks, straight quotes and inner quotes. No gendered pronoun for Kael, Juna, AEGIS, Nyx, Kiko, Lex or LogOS — use the names (quotations verbatim, including the document's „his“).

## Pages — document 478, `from-monolith-to-mosaic-a-strategic-proposal-for-restructuri`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L15, L31, L35, L57, L70. minor (1–4): AEGIS risks becoming an abstract threat; shown instead as a tragic entity born from its own foundational trauma (L57); the Genesis-Krise narrated in first person by the Ursprungs-Ich (L57 — describe around the bold).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L57. not read: an occurrence — the Genesis-Krise and the Genesis Log are the proposal's story forms, read on aegis.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L47. minor (1–4): Juna/V the external entity of the Moonshine-Link, whose link fades in the cyclical act (L47).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L23, L31, L35, L45, … (10 lines). central (4–8): Kael clinically defined by the structural-dissociation theory, with ANPs managing daily life and EPs holding unprocessed trauma (L21); the 39-story format deep-dives into the perspectives of Kael's alters (L35); in the cyclical second act Kael's system grows more brittle with each failed loop (L45); the Moonshine-Link to Juna/V grows fainter, increasing Kael's isolation (L47); the Kernwelten as externalisations of Kael's inner landscape (L61).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L46, L61; `Kernwelt` L46, L61, L66. minor (1–4): the Kernwelten as simulated realities that directly externalise Kael's inner landscape (L61); a table of story ideas for KW1 Logos-Prime, KW2 Mnemosyne-Archipel, KW3 Cerberus-Labyrinth, KW4 Kairos-Potentialis (L66–L70 — describe the cells).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L38. minor (1–4): a story from the perspective of Kiko, the Freeze EP, immersing the reader in paralysing fear (L38 — describe).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L39. minor (1–4): a story from the perspective of Lex, the rationalist ANP, staging a phobic rejection of emotion (L39 — describe).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L67. minor (1–4): in KW1 LogOS, the Guardian, systematically acts against an inhabitant's perceived imperfection (L67 — describe the table cell).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L47. minor (1–4): the Moonshine-Link to the external entity Juna/V growing fainter and noisier in each failed loop (L47 — describe around the bold and quotes).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L57. minor (1–4): in the proposed Genesis Log, the Nichts Rauschen as auditory pressure without sound (L57 — describe).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L37. minor (1–4): a story from the perspective of Nyx, the Fight EP, framing the aggression as a protector's high-cost strategy (L37 — describe around the bold and inner quotes).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L57. minor (1–4): the Ursprungs-Ich's origin in the Potentialmeer in the proposed Genesis Log (L57 — describe).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L21. minor (1–4): Kael clinically defined by the structural-dissociation theory, TSDP (L21).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` titles, not the subfunction.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). an occurrence: `Cerberus-Labyrinth` names KW3 — recorded on Q5.
- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis Log` (near `genesis`). an occurrence: read on aegis.
- `guardians`: `Guardian` (near `guardians`). a reading: Guardians in KW1 and KW3 — recorded on Q1.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna.
- `kairos`: `Kairos-Potentialis` (near `kairos`). an occurrence: `Kairos-Potentialis` names KW4 — recorded on Q5.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). an occurrence: `Mnemosyne-Archipel` names KW2 — recorded on Q5.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). an occurrence: the borrowed theory's name.


**Record entries** (one file each, formatted as earlier entries):
- **`q3-how-many-kern-welten-and-alters`**: the mosaic proposal lists four Kernwelten, KW1–KW4 (L66–L70); recorded.
- **`q5-guardians-and-kern-welten`**: the proposal names the four worlds Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth and Kairos-Potentialis, with LogOS as the Guardian of KW1 (L67) and a Guardian of the bunker-fortress in KW3 (L69); recorded, not resolved.

**No chapter readings**: the proposal plans 39 stories, none named or numbered.

**Not promoted:** narrative mosaic, psycho-structural resonance, the story labels, Cyclical Structure and its costs, Genesis Log, Echo der Einsamkeit, Guardian Analyst, and the borrowed concepts (one carries a person's name).

**One reader**: every page above and the two record entries.
