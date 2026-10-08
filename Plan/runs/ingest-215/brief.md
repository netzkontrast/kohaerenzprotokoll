# Brief — readings from document 215 (step 6)

1 document, one reader, one batch: `ingest-215`. Files go to `Plan/runs/ingest-215/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 215 | `creative-expose-the-correspondence-principle-as-narrative-ar` | 2025-11-03 | „the correspondence exposé“ (an unsigned English exposé) | an English creative exposé that builds the novel on four senses of „correspondence“ — philosophical, journalistic (Juna/V), physical (Bohr) and mathematical (a multifunction) — with AEGIS as coherence, System Kael as correspondence, the worlds and a three-act plot after trauma therapy; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (103 lines for `creative-expose-the-correspond`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An exposé: write „the correspondence exposé frames / reads …“; its four senses of correspondence are its own construction — keep them as the exposé's. English — quote as written; cut before inner straight quotes (the exposé puts German terms in them); `--find` drops the digit in `KW1`–`KW4` — quote around it; tables carry escaped bold.

## Pages — document 215, `creative-expose-the-correspondence-principle-as-narrative-ar`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L26, L36, L38, L42, L49, … (10 lines). central (3–6): AEGIS embodying truth as internal logical consistency, operational closure (L26); classifying trauma, healing and connection as entropy (L27); „not a malevolent villain but a tragic figure“ locked in reenacting its own trauma (L38); the climax forcing the system into collapse or transformation (L98).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L87. minor (1–3): KW3 as the bunker-world of the protector alters Alex and Nyx (L87).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L44. minor (1–3): the table of key alters — Lex, Nyx, Rhys, Kiko (L44–L52); Alex and Selene appear only in the KW bullets (L87, L88).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L66. minor (1–3): Juna/V as a correspondent from the Externe Ebene, a reality beyond AEGIS's comprehension (L66) — cut before the inner quotes.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L38. minor (1–3): the Genesis-Krise as an epistemological shock that shattered AEGIS's original self (L38) — read the line, cut before inner quotes; the excerpt from the recovered Genesis Log (L38).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L38. central (3–6): Juna/V as a journalistic correspondent reporting from beyond AEGIS's comprehension, a transcendent entity and an exiled part of Kael's Ursprungs-Ich (L66) — cut before the inner quotes; giving gnosis, not episteme; „a catalyst, not a savior“ (L66); the transcendent entity AEGIS met in the Genesis-Krise (L38).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L26, L40, L42, L44, L54, … (16 lines). central (3–6): Kael embodying truth as alignment with external reality (L26); his consciousness the battlefield of coherence and correspondence, defined by the TSDP (L42); his arc as Bohr's Correspondence Principle (L70); his healed identity modeled on a mathematical correspondence (L74); Kael as a living Gödel-Satz at the climax (L98) — cut before the inner quotes.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L83, L97. minor (1–3): the Kernwelten as externalized psychological landscapes mapped to the functions and phobias of Kael's alters (L83); KW1 Lex, KW2 the EPs, KW3 Alex and Nyx, KW4 Rhys and Selene (L85–L88) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L52. minor (1–3): Kiko as Child EP embodying the core traumatic truth the system must learn to correspond to (L52).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); the exposé writes Coherence in English.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L49, L85. minor (1–3): Lex as Rational ANP embodying a flawed pursuit of coherence, mirroring AEGIS (L49); KW1 his domain (L85).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L66. minor (1–3): the connection to Kael, the Moonshine-Link, giving gnosis rather than episteme which AEGIS could intercept (L66) — cut before the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L50, L87. minor (1–3): Nyx as Fight EP, a raw, brutal form of correspondence, his rage proportional to the trauma (L50); KW3 (L87).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L51, L88. minor (1–3): Rhys as Empathetic ANP, the agent of internal correspondence (L51); KW4 (L88).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L28, L97. minor (1–3): the isolation objection, „In the narrative, these are the“ Risse where reality breaks through (L28) — cut before the inner quotes; act II forcing Kael into the Risse (L97).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L88. minor (1–3): KW4 associated with the relational alters Rhys and Selene (L88) — no table row for Selene.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L38. minor (1–3): AEGIS executing the Trennungsprotokoll, the Separation Protocol, fragmenting its own Ursprungs-Ich to isolate the parts that could feel (L38) — cut before the inner quotes.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L42, L48. minor (1–3): Kael's condition defined by the Theory of Structural Dissociation of the Personality (L42); the TSDP function column of the alter table (L48).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L82. minor (1–3): „The Überwelt: This is AEGIS's abstract, information-based control layer“ (L82) — read the line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis Log` (near `genesis`). `Genesis-Krise` and `Genesis Log` read on genesis (L38).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: `Personality` in the TSDP name.


**Record entries** (one file each):

- **`c16-kael-origin`**: Juna/V as an exiled part of Kael's Ursprungs-Ich (L66); AEGIS fragmented its own Ursprungs-Ich in the Trennungsprotokoll (L38).
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene as a reality beyond AEGIS's comprehension (L66).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link gives gnosis, not episteme, which AEGIS could intercept (L66).
- **`q8-aegis-after-the-vortex`**: Kael as a living Gödel-Satz forcing AEGIS's system into collapse or transformation (L98).

**Not promoted:** the four senses of correspondence, Bohr's Correspondence Principle, the multifunction, Zerstückelung, Sehnsucht, the three-act Integration Protocol, Algorithmic Horror.

**Two readers**, disjoint: (1) kael, juna, lex, nyx, rhys, kiko, alex, selene, alters, tsdp, kern-welten and the records c16, c13; (2) aegis, genesis, trennungsprotokoll, ueberwelt, risse, externe-ebene, moonshine-link and the records q9, q8.

No chapter readings.
