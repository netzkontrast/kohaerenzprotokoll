# Brief — readings from document 240 (step 6)

1 document, one reader, one batch: `ingest-240`. Files go to `Plan/runs/ingest-240/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 240 | `aegis-paradoxon-konzeption-und-analyse` | 2025-04-29 | „the AEGIS paradox report“ (an unsigned German Forschungsbericht) | a six-stage research report that surveys borrowed concepts, formulates five candidate paradoxes for AEGIS in three areas, recommends „Kohärenz durch Entfremdung“ and illustrates it with an invented rift in KW3; a proposal, explicitly written without earlier plot ideas (L16), not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (395 lines for `aegis-paradoxon-konzeption-und`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report of proposals: write „the AEGIS paradox report proposes / suggests …“. Sentences tagged `\[Kontext\]` are the report restating the project's setting — say „the setting the report restates“. Its world claims are mostly conditional („könnte“, „vermutlich“): keep the condition. The KW3 scenario with Lex and Kiko is an invented illustration („beispielsweise“, L331) — say so. Table paradox ordinals print as `1\.`; quote around them.

## Pages — document 240, `aegis-paradoxon-konzeption-und-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L13, L16, L18, L22, L24, … (110 lines). central (3–12): in the restated setting an information-based, potentially autopoietic AI whose raison d'être is coherence as stability, order and predictability, which creates and manages the Kernwelten to influence Kael (L18); genesis as order from chaos (L26); the recommended paradox „Kohärenz durch Entfremdung“ — programmed to absolute coherence, its necessary operative and epistemological distancing produces the incoherence and entropy it fights (L287–L288), rooted in its core nature (L296) and read as classical tragedy (L297); the scenario's containment protocol (L337).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L63. minor (1–4): DID's multiple identities (Alters) in the concept table, read as Kael's complex adaptive system (L63).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L63. minor (1–4): „Dissoziative Identitätsstörung - DID“ as a borrowed concept for understanding Kael (L63).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L40, L69, L92, L171, L180, L250, … (8 lines). minor (1–4): emergence from complexity theory as what AEGIS's control cannot predict (L69, L92); KW4 glossed as „Potentialität/Emergenz“ (L171).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L18, L36, L37, L79, L170, L288, … (8 lines). minor (1–4): information entropy as AEGIS's measure to minimise, glossed as Inkohärenz (L36); in the restated setting the active management of entropy (L18); the recommended paradox producing incoherence and entropy (L288).
- **`genesis`** (central, 3–12 quotations): the census's surfaces — `Genesis` L26, L59, L124, L145, L197, L233, … (10 lines). minor (1–4): AEGIS's genesis as order from chaos (L26), path dependence from its genesis (L59), the Hybris paradox rooted in it (L124, L197).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L16, L52, L108, L151, L162, L171, … (24 lines). minor (1–4): „Die externe, unkontrollierbare Variable Juna/V“ (L162); possibly the uncontrollable outside world (L198); the Juna/V connection named among the analysis's contexts (L151) and among the earlier plot ideas it sets aside (L16).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L18, L26, L40, L41, L43, L44, … (55 lines). central (3–12): in the restated setting a complex entity with a dissociative identity structure based on TSDP whose journey to integration is the core of the narrative (L18); AEGIS ordering him through rigid structures in KW1 may deepen his fragmentation (L162); the scenario's cooperation of two of his parts and its re-traumatisation (L331, L338).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L18, L26, L40, L50, L69, L92, … (19 lines); `Kernwelt` L18, L26, L40, L50, L69, L92, … (20 lines). central (3–12): in the restated setting simulations AEGIS creates and manages, numbered KW1–KW4 (L18); glosses KW1 „Logik/Ordnung“ (L162) and „Ordnung“ (L249), KW2 „Emotion/Erinnerung“ and KW4 „Potentialität/Emergenz“ (L171), KW3 „Abwehr“ (L249) and in the scenario chaos, defence, paranoia and boundaries (L331) — the KW1 gloss differs between passages; record both.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L331, L336, L337. minor (1–4): the strongly emotional, child-like part „Kiko“, offered as an example in the invented KW3 scenario (L331), forcibly separated from Lex by AEGIS (L336–L337).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L16, L18, L26, L39, L46, … (43 lines). central (3–12): in the restated setting AEGIS's aim, glossed as stability, order and predictability (L18); the recommended paradox „Kohärenz durch Entfremdung“ (L287–L288, L348).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L331, L336, L337. minor (1–4): the highly logical, controlled part „Lex“, offered as an example in the invented KW3 scenario (L331); its cooperation with Kiko misread as anomalous convergence (L336).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L250, L338. minor (1–4): „die rebellische Nyx“ among Kael's parts that may resist AEGIS's intervention (L338).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L42, L92, L141, L151, L161, L249, … (10 lines). central (3–12): instability („Risse“) amplified by AEGIS's control through positive feedback loops (L42); Paradox 1, control-induced instability producing Risse (L92); the scenario's rift in KW3 that widens instead of closing (L331, L338).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L18. minor (1–4): in the restated setting Kael's dissociative structure „basierend auf TSDP“, expanded as Trauma Spectrum Dissociative Profile (L18).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L47. not read: occurrence: `Simulation` in the halting-problem row means AEGIS's simulations in general (L47), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: the restated setting writes four Kernwelten, KW1–KW4 (L18), each glossed by domain (L162, L171, L249, L331); the KW1 gloss differs between L162 and L249. It names no count of alters.
- **`c2-entropie-sense`**: Entropie in the information-theoretic sense, AEGIS's measure to minimise, glossed as Inkohärenz (L36); the recommended paradox produces „Inkohärenz und Entropie“ (L288).

**Not promoted:** the five paradoxes and three areas, Paradoxon X, Monstergruppe, Primärdirektive, Kernprogrammierung, the lens concepts (Autopoiesis, Hamartia, Halteproblem, Qualia and the rest), Baudrillard, KW1–KW4 as separate pages.

**One reader**: aegis, kael, kern-welten, kohaerenz, risse, juna, lex, kiko, nyx, tsdp, entropie, emergenz, genesis, alters, did and the records q3, c2. `ueberwelt` is decided as an occurrence (sweep).

**Chapter readings**: none — the report names no chapter.
