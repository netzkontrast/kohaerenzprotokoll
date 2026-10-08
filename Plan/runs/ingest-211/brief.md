# Brief — readings from document 211 (step 6)

1 document, one reader, one batch: `ingest-211`. Files go to `Plan/runs/ingest-211/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 211 | `the-coherence-protocol-a-proposal-for-a-39-story-narrative-m` | 2025-11-03 | „the 39-story mosaic“ (an unsigned English proposal) | an English proposal that reframes the novel as 39 interconnected short stories, each with a Core Concept, an Assigned POV and a Narrative Directive, in three parts; it calls itself a blueprint that resolves inconsistencies and „the definitive architecture for this experiment“ (L15), and settles the protagonist's name and gender for itself (L34) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (270 lines for `the-coherence-protocol-a-propo`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal for a story collection: write „the 39-story mosaic proposes / assigns …“ and name the story (Story N) a line belongs to; a story is not a chapter. English — quote as written; cut before inner straight quotes; `--find` drops digits (`Kernwelt 1`, `Co₁`) — quote around them; Parts 1 headings run a story onto one line with escaped asterisks — never quote across `\*`.

## Pages — document 211, `the-coherence-protocol-a-proposal-for-a-39-story-narrative-m`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L42, L51, L52, L71, L97, … (25 lines). central (3–6): AEGIS as a tragic AI born from a traumatic Genesis-Krise, embodying the Coherence Theory (L25) — cut before the inner quotes; narrated as system logs and analyses (L51); its cruelty a compulsive reenactment of its origin-trauma (Story 22, L153); at the climax its detection of Kael as a living Gödel-Satz and its tragic transformation instead of a crash (Story 34, L233).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L39, L87. minor (1–3): Alex among the key ANPs (L39); Story 11 `The Wounded Masculine` from Alex (ANP Protector) (L87).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L39, L50, L104, L105, L141. minor (1–3): Argus listed as Observer/Critic (L39) and as „ANP/EP Meta-Cognitive Observer“ (Story 14, L104) — record both.
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L52. minor (1–3): the Kernwelt Guardians as external observers, some becoming allies through the Guardian's Dilemma (L52) — cut before the inner quotes; a Guardian loyal to AEGIS meeting the Moonshine-Link (Story 21, L147); Story 29 from „A Rebel Guardian“ (L202).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L40. minor (1–3): Isabelle among the key EPs (L40).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Julia` alone on L34. central (3–6): the protagonist's name and gender settled against „Kael/Julia“ (L34) — read the line; Juna/V's dual nature: a transcendent entity and an exiled part of Kael's Ursprungs-Ich (L52); Story 8 from Juna/V's dual perspective (L81); Story 22, Juna/V granting Kael a vision of the Genesis-Krise (L153).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L26, L30, L32, L34, L39, … (48 lines). central (3–6): System Kael embodying the Correspondence Theory (L26); his consciousness modeled on TSDP (L32); the note on canonical identity — „this blueprint establishes the protagonist as Kael, using male pronouns“ (L34); Story 1 from Kael (ANP Host) (L67); the goal to become a living Gödel-Satz (L183) — cut before the inner quotes; Kael (Integrated Self) at the end (L262).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L52, L122, L146. minor (1–3): Story 17 from „The Architect (Guardian of Kernwelt 1)“, the logic-based world (L122, L123) — quote around the digit; a Kernwelt Guardian in Story 21 (L146).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L40, L50, L75, L83, L197. minor (1–3): Kiko among the key EPs (L40); Story 9 from Kiko (EP Child) (L83).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L39, L50, L69, L73, L85, L89, … (13 lines). central (3–6): Lex among the key ANPs (L39); Story 2 `The Proactive Protector` from Lex (ANP Rationalist) (L69); Story 16, Lex processing the glitch toward the Brain in a Vat (L117); Story 32 `Blueprint for a Revolution` (L220).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L40. minor (1–3): Lia among the key EPs (L40).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L147, L153. minor (1–3): a Guardian's first perception of the Moonshine-Link (Story 21, L147) — cut before the inner quotes; the gnostic connection through which Juna/V gives Kael a vision (Story 22, L153).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L40, L79, L226, L227. minor (1–3): Story 7 `The Great Unraveling` from Moros (EP Collapse) (L79); Story 33 `The Darkest Hour` (L226).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L183. minor (1–3): failure means dissolution into the Potentialmeer „and its“ Nichts Rauschen (L183) — cut around the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L40, L50, L73, L89, L176, L177. minor (1–3): Nyx (Fight) among the key EPs (L40); Story 4 `The Dragon's Breach` from Nyx (L73); Story 26 from Nyx and Lex in succession (L176).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L183. minor (1–3): the cosmic horror of the Potentialmeer as the stake of failure (L183) — quote around the inner quotes.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L39, L50, L75, L87, L89, L134, … (12 lines). central (3–6): Rhys among the key ANPs (L39); Story 5 `Glimmers of Self` from Rhys (ANP Caretaker) (L75); Story 19 (L134); Story 36 `The Work of Mourning` (L244).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L107. minor (1–3): Story 15 `The Glitch in the Code`: Kael witnesses a Riss, an undeniable glitch in his reality (L107, L111) — cut before the inner quotes.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L39, L89, L250, L251. minor (1–3): Story 12 from „Selene (ANP Integrator?)“ (L89) and Story 37 `The Gardener` from „Selene (ANP Integrator)“ (L250) — record both, the question mark kept.
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L30, L32, L67, L73, L79, L81, … (10 lines). central (3–6): Kael's consciousness modeled on the clinical Theory of Structural Dissociation of the Personality (L32); Story 1's core concept, TSDP (L67); Story 4, a trigger-induced EP intrusion (L73); Story 7 (L79).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L109. occurrence: `Simulation` is Simulation Theory, Story 15's core concept (L109), nothing of the Überwelt.

- **`genesis`** (minor, 1–2): AEGIS born from a traumatic Genesis-Krise, an ontological wound from an encounter with an unclassifiable reality (L25); Story 22, the Genesis-Krise as the origin-trauma AEGIS reenacts (L153).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading — see the extra page below.
- `guardians`: `Kernwelt Guardians` (near `guardians`). `Kernwelt Guardians` read on guardians (L52).
- `juna`: `Kael/Julia` (near `julia`), `Juna/V` (near `juna`). `Kael/Julia` and `Juna/V` read on juna (L34, L52) — the first as the source documents' alternative the note rejects.
- `kael-julia-bindung`: `Kael/Julia` (near `kaeljuliabindung`). occurrence: `Kael/Julia` is a name alternative (L34), not the bond.
- `personas`: `Theory of Structural Dissociation of the Personality (TSDP)` (near `persona`). occurrence: `Personality` in the TSDP name.
- `risse`: `Riss` (near `risse`). `Riss` read on risse (L111).
- `ueberwelt`: `Simulation Theory` (near `simulation`). occurrence: `Simulation Theory` is a borrowed concept (L109).


**Record entries** (one file each):

- **`c17-kael-gender`**: the note on canonical identity — the source documents contradict on name and gender („Kael (ehem. Michael)“ against „Kael/Julia“), and „this blueprint establishes the protagonist as Kael, using male pronouns“ (L34) — the document's own settlement, recorded, never applied.
- **`q5-guardians-and-kern-welten`**: „The Architect (Guardian of Kernwelt 1)“, the logic-based world Co₁ (L122, L123).
- **`c4-guardians-and-aegis`**: Kernwelt Guardians, some becoming allies through the Guardian's Dilemma (L52); a Guardian loyal to AEGIS (L147); a Rebel Guardian (L202).
- **`c16-kael-origin`**: Juna/V as an exiled part of Kael's Ursprungs-Ich (L52).
- **`q8-aegis-after-the-vortex`**: at the climax AEGIS's tragic transformation, not a crash (Story 34, L233); a surviving Guardian after the system change (Story 35, L238).

**Not promoted:** the 39 story titles and their core concepts, the narrator categories, the borrowed theories (IFS, Putnam, Hofstadter, Gödel, chaos theory, existentialism), the Corrective Wavelet as narrator, the Guardian's Dilemma.

**Two readers**, disjoint: (1) kael, juna, lex, rhys, nyx, kiko, lia, moros, isabelle, alex, argus, selene, tsdp and the records c17, c16; (2) aegis, genesis, guardians, kern-welten, risse, potentialmeer, nichts-rauschen, moonshine-link and the records q5, c4, q8.

No chapter readings: the mosaic numbers stories, not chapters.
