# Brief — readings from document 191 (step 6)

1 document, one reader, one batch: `ingest-191`. Files go to `Plan/runs/ingest-191/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 191 | `the-psychological-mechanics-from-tertiary-structural-dissoci` | 2025-11-03 | „the TSDP mechanics report“ (titled `The Psychological Mechanics: From Tertiary Structural Dissociation to Organic Alter-Dynamics`) | an English analysis report in six sections: AEGIS as the engine of Kael's fragmentation, a table of six alters with functions, phobias and integrated roles, the four Core Worlds as proving grounds, and functional multiplicity rather than fusion as the goal; its sources are bracketed `[cite: …]` markers — it says it „has demonstrated“ its case (L82), recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (85 lines for `the-psychological-mechanics-fr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that cites: write „the TSDP mechanics report reads / defines …“; a sentence ending in `[cite: …]` reports that source — name it where it matters. English with German titles — quote as written; cut before inner straight quotes and before `\[cite:`; the table at L43–L49 has escaped bold and `<br>` — quote the plain words; KW digits drop in `--find` — quote around them.

## Pages — document 191, `the-psychological-mechanics-from-tertiary-structural-dissoci`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L25, L27, L29, L30, … (12 lines). central (2–4): Kael's condition „is actively maintained and exacerbated by the story's primary antagonist“ (L25); the Paradox of Misaligned Coherence as specification gaming (L29); AEGIS „as an Externalized Perpetrator Introject“ (L30); trauma by analysis, a category error of its hybrid LFI/D2 architecture (L31); the Core Worlds designed by AEGIS to test the system (L55).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L35. minor (1–2): each alter emerged with a specific function to help the system survive (L37).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L59. minor (1–2): „KW3: The Fortress (Cerberus)“, Kael's defence mechanisms and a Traveling-Salesperson puzzle (L59) — quote around the digit.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L48. minor (1–2): Rhys is „central to the connection with Juna/V“ (L48).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L21, L23, L25, L27, … (23 lines). central (2–4): Kael with TSDP and a complex inner system (L17); „Primary ANP/Host“, carrying amnesia and unreality (L44) — quote the plain words; unaware of his alters at first, glitches and voices (L70); „functional multiplicity“, co-consciousness not fusion (L74); the goal „integration and coordination“, not fusion (L84).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L60. minor (1–2): „KW4: The Garden of Possibility (Kairos/Sophia)“, NP-search (L60) — quote around the digit.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L47, L57, L76. minor (1–2): „EP - Child/Freeze“: the core vulnerability, fear and shame of early trauma (L47) — quote the plain words.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L29. occurrence: „Maximize Coherence“ is AEGIS's directive in the specification-gaming sentence (L29), read on aegis.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L45, L57, L76. minor (1–2): „Primary ANP“: logic, analysis and control, fear of emotion and chaos (L45); KW1 tests him (L57).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L58. minor (1–2): „KW2: The Resonance Landscape (Mnemosyne)“, a fluid world of Dialetheic Koexistenz (L58) — quote around the digit.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L46, L57, L59, L76. minor (1–2): „EP - Fight/Persecutor“: the fight response, aggression turned inward (L46); in KW1 and KW3 (L57, L59).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L48, L58. minor (1–2): „Secondary ANP“: a caregiver for harmony and connection, central to the connection with Juna/V (L48); in KW2 (L58).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L49, L60. minor (1–2): „Modified ANP/EP“: the potential for healing, an inner helper and regulator (L49); in KW4 (L60).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L60. minor (1–2): joined with Kairos in „KW4: The Garden of Possibility (Kairos/Sophia)“ (L60).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L43. central (2–4): „Tertiary Structural Dissociation of the Personality (TSDP)“ (L17); defined as a fundamental split into ANPs and EPs (L19); the table's „Alter & TSDP Type“ column (L43); translated into a narrative mechanic (L82).

**Pages the census reaches by another surface** (read them too):

- **`multiplizitaet`**: central (2–4): „functional multiplicity“ defined as co-consciousness and cooperation, not fusion (L74); performed by polyphonic or choric prose, a collective We (L76); the goal of integration over fusion (L84).
- **`kern-welten`**: central (2–4): the Core Worlds as „epistemological landscapes“ of Kael's psyche, designed by AEGIS (L55); KW1 Construct City (Logos-Prime) to KW4 Garden of Possibility (Kairos/Sophia), each a computational class (L57–L60).
- **`konstrukt-stadt`**: minor (1–2): „KW1: The Construct City (Logos-Prime)“, the class P, hyper-logic and sterility (L57) — quote around the digit.
- **`resonanz-landschaft`**: minor (1–2): „KW2: The Resonance Landscape (Mnemosyne)“, Dialetheic Koexistenz (L58).
- **`moeglichkeits-garten`**: minor (1–2): „KW4: The Garden of Possibility (Kairos/Sophia)“, NP-search (L60).
- **`grenzfeste`**: minor (1–2): „KW3: The Fortress (Cerberus)“, Kael's defence mechanisms (L59).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). a reading — on juna above (`Juna/V`, L48).
- `kairos`: `Kairos/Sophia` (near `kairos`). a reading — on kairos above.
- `kohaerenz`: `Wahre Kohärenz` (near `koharenz`). occurrence: „Wahre Kohärenz“ is a phrase in the report's conclusion, read on multiplizitaet if it bears on it.
- `logos`: `Logos-Prime` (near `logos`). occurrence: Logos-Prime is KW1's world, J49 — on konstrukt-stadt.
- `personas`: `Apparently Normal Personality parts` (near `persona`), `Emotional Personality parts` (near `persona`). occurrence: the ANP and EP expansions are the TSDP's types, read on tsdp — not the Personas.
- `sophia`: `Kairos/Sophia` (near `sophia`). a reading — on sophia above.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: six alters in the table — Kael, Lex, Nyx, Kiko, Rhys, Selene (L44–L49); four Core Worlds (L57–L60).
- **`q5-guardians-and-kern-welten`**: the Core Worlds named with Logos-Prime, Mnemosyne, Cerberus and Kairos/Sophia in brackets (L57–L60) — say the report names no Guardians.

**Not promoted:** Specification Gaming, the externalized perpetrator introject, trauma by analysis, LFI and D2, the computational classes P, NP and TSP, Dialetheic Koexistenz, the unconscious switch, polyphonic prose.

**Two readers**, disjoint: (1) kael, alters, lex, nyx, kiko, rhys, selene, juna, tsdp, multiplizitaet and the record q3; (2) aegis, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, mnemosyne, cerberus, kairos, sophia and the record q5.
