# Brief — readings from document 142 (step 6)

1 document, one reader, one batch: `ingest-142`. Files go to `Plan/runs/ingest-142/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 142 | `project-coherence-protocol-a-canon-of-core-identity-and-anta` | 2025-11-03 | „the canon decree“ (titled `Project Coherence Protocol: A Canon of Core Identity and Antagonist Fate`, L11) | an English document of 2025-11-03 that „formally canonizes“ (L13) Kael as the male host with an eleven-part roster (L29–L44), AEGIS's Genesis-Krise and its fate, algorithmic melancholy (L52–L66), and the Guardians' Wächter-Zwiespalt with a Core-World table (L70–L90); it names no author — its canon claims are recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (97 lines for `project-coherence-protocol-a-c`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A decree claims canon: write „the canon decree declares / canonizes …“ — always as its claim, never as the wiki's fact; English — quote as written, never translate; cut quotations before inner straight quotes. Kael is male here too.

## Pages — document 142, `project-coherence-protocol-a-canon-of-core-identity-and-anta`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L52, L54, L58, L62, L66, … (10 lines). central (2–4): „a tragic and philosophically complex figure rather than a simplistic, malicious villain“ (L54); its prime directive „Aegis is what Aegis prevents itself from not being“ — cut before the quotes if needed (L62); its fate, algorithmic melancholy (L64–L66).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L36. minor (1–2): „ANP (Protector)“ (L36).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L44. minor (1–2): „ANP/EP-Mix“ (L44).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L85. minor (1–2): KW3 Cerberus-Labyrinth (L85).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L72, L76, L90. minor (1–2): not monolithic enforcers (L72); „specialized agents who administer AEGIS's simulated“ Kernwelten (L76); the Wächter-Zwiespalt (L90).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L41. minor (1–2): „EP (Sexualized)“ (L41).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L58. occurrence unless L58 says something of Juna/V — then minor, by the reader.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L17, L19, L23, L27, L29, … (13 lines). central (2–4): „It is hereby canonized that the central protagonist of“ the story „is the male host known as“ Kael (L23) — cut at the straight quotes; the TSDP architecture (L27); the arc toward functional multiplicity, not erasure of parts (L48).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L86. minor (1–2): KW4 Kairos-Potentialis, Kairos/Sophia (L86).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L74, L76; `Kernwelt` L74, L76, L82. minor (1–2): each world „an externalized psychological landscape“ (L76); the table KW1–KW4 (L83–L86).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L39. minor (1–2): „EP (Child)“ (L39).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L35. minor (1–2): „ANP (Rationalist)“ (L35).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L40. minor (1–2): „EP (Child)“, ambivalent attachment (L40).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L83. minor (1–2): KW1 Logos-Prime, „Designated Guardian“ LogOS (L83).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L84. minor (1–2): KW2 Mnemosyne-Archipel (L84).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L42. minor (1–2): „EP (Collapse)“ (L42).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L38. minor (1–2): „EP (Fight)“ (L38).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L37. minor (1–2): „ANP (Caretaker)“ (L37).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L43. minor (1–2): „ANP (Integrator?)“ (L43) — the question mark is the decree's.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L86. minor (1–2): the same line (L86).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L25, L27, L33. minor (1–2): „Kael's internal world is canonically defined by the“ TSDP (L27).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading, minor (1–2): the Genesis-Krise as AEGIS's canonical origin, an epistemological trauma of the Ursprungs-Ich (L56–L58).
- `juna`: `Juna/V` (near `juna`). `Juna/V` (J34) — on juna above if read.
- `personas`: `Theory of Tertiary Structural Dissociation of the Personality` (near `persona`). occurrence: TSDP's full name, on tsdp.


**Record entries** (one file each):

- **`c17-kael-gender`**: „the male host known as“ Kael (L23), „anchored in the male host, Kael“ (L19) — dated 2025-11-03.
- **`q3-how-many-kern-welten-and-alters`**: eleven parts in the roster (L34–L44) with ANP/EP types; four Kernwelten (L83–L86).
- **`c6-guardians-count-and-pairing`**: LogOS KW1, Mnemosyne KW2, Cerberus KW3, Kairos/Sophia KW4 (L83–L86).
- **`q8-aegis-after-the-vortex`**: AEGIS's „definitive fate“ is algorithmic melancholy (L64–L66).

**Not promoted:** Wächter-Zwiespalt (on guardians), Coherence Imperative, autopoietic (borrowed), the canon claims themselves.

**One reader**, all pages and entries.
