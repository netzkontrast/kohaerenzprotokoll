# Brief — readings from document 207 (step 6)

1 document, one reader, one batch: `ingest-207`. Files go to `Plan/runs/ingest-207/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 207 | `the-kohaerenz-protokoll-writer-s-bible-a-definitive-guide-to` | 2025-11-03 | „the writer's bible“ (an unsigned English writer's guide) | an English writer's guide in six parts with German names that derives world, entities and a three-act plot from one „Protocol Ontology“, which it calls „the single unifying source“ (L17), with a lexicon it calls „a definitive glossary“ (L54) — its standing claims recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (237 lines for `the-kohaerenz-protokoll-writer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A writer's guide that states its world as fact: write „the writer's bible states / defines …“ and keep its claims as its own. English — quote as written; cut before inner straight quotes (the guide quotes many terms in them); `--find` drops digits and subscripts (`KW1`, `K₁`, `Co₁`) — quote around them; tables have escaped bold.

## Pages — document 207, `the-kohaerenz-protokoll-writer-s-bible-a-definitive-guide-to`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L78, L80, L93, L97, L99, L100, … (26 lines). central (3–8): AEGIS as an autopoietic, operationally closed system whose identity is its prime directive (L145); its origin as a cluster of Ich-Fragmenten from the Potentialmeer (L146); its tragic flaw, the epistemological trauma of the Genesis-Krise, faced with Juna/V it could not classify (L147); its function as „Autonomous Entropic Gatekeeper“ classifying Kael's healing as entropy (L148) — cut before the inner quotes; at the end it must evolve or suffer total collapse (L204).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L88, L161. minor (1–3): Alex as ANP (Protector) — protection in crises, fear of helplessness (L161); a protector alter shaping KW3 (L88).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L84, L86, L88, L89, L123, L154, … (9 lines). minor (1–3): the Core Worlds embody the functions and phobias of the alters that inhabit them (L84); the table of key alters, the internal political landscape of System Kael (L154).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L169. minor (1–3): Argus as „ANP/EP-Mix“ — metacognitive observation and criticism, risk of analysis-paralysis (L169).
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L36, L60. minor (1–3): the fundamental building blocks of protocols (L36); in the lexicon the „atom of persistence“, a minimal self-correcting unit of mutual information (L60) — cut before the inner quotes.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L21. minor (1–3): the universe's core dynamic grounded in the in-world „Dual Kernel Theory“ — Coherence against Collapse (L21) — cut before the inner quotes, quote around the subscripts.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L99. minor (1–3): „The External Level (Externe Ebene)“: a transcendent realm, the source of the Juna/V connection, a higher-order reality AEGIS cannot model (L99).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L166. minor (1–3): Isabelle as EP (Sexualized) — regaining power, fear of vulnerability (L166).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L93. central (3–8): Juna/V as one of three principal entities (L141); her dual nature — a transcendent entity from the External Level and „an exiled part of Kael's own“ Ursprungs-Ich (L173) — cut before the inner quotes; the non-local Moonshine-Link (L174); „a catalyst, not a savior“, giving gnosis (L175); the connection breaking through in the Risse (L93).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L84, L93, L118, L131, L141, L148, … (31 lines). central (3–8): the Kernwelten as physical manifestations of System Kael's fragmented psyche (L84); his fragmentation modeled on TSDP, his healing on IFS (L152); Kael as ANP (Host) (L159); the midpoint: „he is the living, externalized memory of AEGIS's own foundational trauma“ (L197); integrated and free at the end (L204).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L82, L84. minor (1–3): the Core Worlds as psychological architectures (L84); KW1 logic and the ANPs like Lex, KW2 raw emotion and the EPs, KW3 a bunker with Alex and Nyx, KW4 potentiality with Lia, Rhys and Selene (L86–L89) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L120, L163, L164, L166, L196. minor (1–3): Kiko as EP (Child) — flight, freeze, attachment cry (L164); Kiko's trauma-honed intuition in act II (L196).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); the guide writes Coherence in English throughout.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L52, L86, L120, L159, L160, L161, … (11 lines). central (3–8): Lex as ANP (Rationalist), phobia of irrationality, conflict with Nyx and Rhys (L160); the primary resident of KW1 (L86); his caution clashing with Kael's curiosity in act I (L191); the duality Lex against Nyx and Kiko (L120).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L89, L163, L165, L166. minor (1–3): Lia as EP (Child) — flight, play, ambivalent attachment (L165); KW4 (L89).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L174. minor (1–3): „The link between Kael and Juna/V is a non-local, sub-protocol“ Moonshine-Link; AEGIS ontologically blind to it, perceiving only noise (L174) — cut before the inner quotes.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L167. minor (1–3): Moros as EP (Collapse) — carrier of hopelessness and existential emptiness (L167).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L100. minor (1–3): „The Sea of Potentiality (Das Potentialmeer / Nichts Rauschen)“: the primordial state of high-entropy information, an active, negating force (L100) — cut before the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L88, L120, L160, L162, L163, L164, … (7 lines). minor (1–3): Nyx as EP (Fight), protecting Kiko and Lia, the primary antagonist to Lex and Rhys (L163); named among the KW3 protector alters (L88); Nyx's aggression needed in the Rifts (L196).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L100. minor (1–3): the Sea of Potentiality as primordial high-entropy state (L100); AEGIS emerging from it as Ich-Fragmente (L146).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L89, L122, L159, L160, L162, L163, … (8 lines). minor (1–3): Rhys as ANP (Caretaker) — harmony and connection (L162); striving for acceptance (L122).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L91, L93, L129, L195. minor (1–3): the Risse as physical manifestations of correspondence errors, tears where an external truth breaks through AEGIS's reality (L93) — cut before the inner quotes; the Risse as the isolation objection (L129); Kael's journey into them in act II (L195).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L89, L168. minor (1–3): Selene as „ANP (Integrator?)“ — regulation and blockade, her integrative nature a threat to AEGIS (L168); keep the question mark; KW4 (L89).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L147. minor (1–3): read L147 — decide reading or occurrence, and say which.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L152, L158. minor (1–3): Kael's fragmentation „modeled on“ Tertiary Structural Dissociation of Personality, TSDP (L152); the table's TSDP action systems (L158).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L78, L80. minor (1–3): „The Überwelt is AEGIS's primary control layer and internal laboratory“, an abstract information-based reality (L80); the heading (L78).

- **`genesis`** (minor, 1–2): the Genesis-Krise as AEGIS's foundational epistemological trauma, confronted with Juna/V (L147); Kael as the externalized memory of it (L197).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading — see the extra page below.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `personas`: `Tertiary Structural Dissociation of Personality` (near `persona`). occurrence: `Personality` in the TSDP name, not the Personas.


**Record entries** (one file each):

- **`c16-kael-origin`**: Juna/V as „an exiled part of Kael's own“ Ursprungs-Ich (L173); Kael as the living, externalized memory of AEGIS's Genesis-Krise (L197).
- **`q3-how-many-kern-welten-and-alters`**: eleven alters in the table — ANPs Kael, Lex, Alex, Rhys, Selene (Integrator?), EPs Nyx, Kiko, Lia, Isabelle, Moros, Argus a mix (L159–L169); four Kernwelten as domains of alters (L86–L89).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link as non-local and sub-protocol, AEGIS blind to it (L174).
- **`q8-aegis-after-the-vortex`**: AEGIS „must either evolve its fundamental protocol or suffer a total system collapse“ (L204).
- **`c13-externe-ebene-beyond-the-simulation`**: the External Level as a transcendent realm outside AEGIS's control (L97, L99).

**Not promoted:** the Protocol Ontology and its lexicon (Protocol, Overhead, Corrective Wavelets, Validation, Correspondence-Check), the thematic matrix, the 6 Paraiyas, the three-act Integration Protocol, IFS, the borrowed theories.

**Two readers**, disjoint: (1) kael, juna, lex, nyx, kiko, lia, rhys, alex, isabelle, moros, selene, argus, alters, tsdp, kern-welten and the records c16, q3; (2) aegis, genesis, ueberwelt, risse, externe-ebene, potentialmeer, nichts-rauschen, coheron, dkt, moonshine-link, trennungsprotokoll and the records q9, q8, c13.

No chapter readings: the guide names acts, not chapters.
