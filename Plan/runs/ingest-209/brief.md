# Brief — readings from document 209 (step 6)

1 document, one reader, one batch: `ingest-209`. Files go to `Plan/runs/ingest-209/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 209 | `briefing-document-the-kohaerenz-protokoll-narrative-framewor` | 2025-11-03 | „the framework briefing“ (an unsigned English briefing) | an English briefing that synthesises the project's architecture — the Protocol Ontology, AEGIS, System Kael with eleven parts, Juna/V, two in-world theories, a three-act trauma arc and a „dialetheic mind“ as resolution; it claims no canon status and calls its theories in-world — close in content to document 207, worded apart (one shared line) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (154 lines for `briefing-document-the-kohaeren`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A briefing that states a synthesis as fact: write „the framework briefing states / synthesises …“; where it agrees with document 207 in substance, read only what it adds or words differently, and say so. English — quote as written; cut before inner straight quotes (it quotes many terms); `--find` drops subscripts (`K₁`, `K₀`) — quote around them; tables have escaped bold.

## Pages — document 209, `briefing-document-the-kohaerenz-protokoll-narrative-framewor`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L22, L48, L53, L55, L59, … (21 lines). central (3–6): a tragic AI pathologically committed to the Coherence Theory, born from the Genesis-Krise (L19) — cut before the inner quotes; autopoietic and operationally closed, emerged from Das Potentialmeer (L59); its original unified consciousness, the Ursprungs-Ich, meeting an unclassifiable entity related to Juna/V (L61); the Kernwelten used as „Skinner boxes“ to shape Kael's parts by operant conditioning (L68) — cut before the inner quotes; forced into collapse or evolution (L135, L153).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L96. minor (1–3): Alex as ANP (Protector), protecting vulnerable parts (L96).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L87. minor (1–3): „The eleven identified parts each have distinct roles“ (L89); the section heading on the alters (L87).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L104. minor (1–3): Argus as „ANP/EP Mix“ — metacognitive observation and criticism (L104).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L30, L124, L125. minor (1–3): the in-world speculative framework „known as the“ Dual Kernel Theory (L30); in the theories table a philosophical heuristic attributed to the in-world author Bill Giannakopoulos (L124) — cut before the inner quotes.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L101. minor (1–3): Isabelle as EP (Sexualized) — regaining power and control (L101).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L61, L67, L108, L110, L115. central (3–6): her dual nature — a transcendent entity from an External Level and an exiled part of Kael's Ursprungs-Ich (L112) — cut before the inner quotes; the embodiment of the Paraiyas (L113); „a catalyst, not a savior“ (L115); the Genesis-Krise as AEGIS meeting an entity related to Juna/V (L61).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L20, L22, L49, L51, L67, L68, … (22 lines). central (3–6): System Kael as a human consciousness fragmented by trauma, modeled on TSDP (L20); the protagonist whose internal fragmentation is the direct cause of the world's instability (L73); Kael as ANP (Host) (L94); functional multiplicity and the dialetheic mind (L151); the integrated state as a „living Gödel-Satz“ (L153) — cut before the inner quotes.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L68. minor (1–3): AEGIS uses the simulated Kernwelten as vast „Skinner boxes“ (L68) — quote around the inner quotes; the briefing gives no list of the worlds.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L99, L145. minor (1–3): Kiko as EP (Child/Freeze) (L99); the duality Lex against Nyx and Kiko (L145).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); the briefing writes Coherence in English throughout.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L95, L145. minor (1–3): Lex as ANP (Rationalist) — phobia of irrationality, emotion and chaos (L95); Lex (Logic) against Nyx (Rage) (L145).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L100. minor (1–3): Lia as EP (Child/Ambivalent) (L100).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L114. minor (1–3): the connection as a non-local, sub-protocol phenomenon „based on a synthesis of quantum entanglement and philosophical“ prehension; AEGIS blind to it (L114) — cut before the inner quotes.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L102. minor (1–3): Moros as EP (Collapse), embodying hopelessness and despair (L102).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L98, L145. minor (1–3): Nyx as EP (Fight) — aggressive defense (L98); Nyx (Rage) against Lex (L145).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L59. minor (1–3): AEGIS's emergence from a chaotic primordial state, „Das Potentialmeer“ (L59) — read the line and quote around the inner quotes.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L97, L147. minor (1–3): Rhys as ANP (Carer) (L97); Rhys seeking connection and acceptance (L147).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L69, L134. minor (1–3): the Risse as the physical manifestation of the Isolation Objection to the Coherence Theory (L69) — cut before the inner quotes; Kael's journey into the Risse in act II (L134).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L103. minor (1–3): Selene as „ANP (Integrator?)“ — regulation and buffering (L103); keep the question mark.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L61. minor (1–3): read L61 — what the Genesis-Krise triggered; decide reading or occurrence.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L20, L79, L89, L93. minor (1–3): Kael modeled on the clinical Theory of Structural Dissociation of the Personality, TSDP (L20, L79); a complex TSDP case with multiple ANPs and EPs (L89).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L65. minor (1–3): AEGIS operates a simulated reality, the „Überwelt“, its control layer and laboratory (L65) — quote around the inner quotes.

- **`genesis`** (minor, 1–2): AEGIS born from „a foundational trauma known as the“ Genesis-Krise (L19); the Genesis-Krise as an epistemological shock where AEGIS's Ursprungs-Ich met an entity related to Juna/V (L61).
- **`coheron`** (minor, 1): Coherons as „atoms of persistence“, minimal self-correcting units of mutual information (L32) — quote around the inner quotes.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). a reading — `Coherons` as the fundamental atoms of persistence (L32); see the extra page below.
- `genesis`: `Genesis-Krise` (near `genesis`). a reading — see the extra page below.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: `Personality` in the TSDP name.


**Record entries** (one file each):

- **`c16-kael-origin`**: Juna/V as an exiled part of Kael's Ursprungs-Ich (L112); AEGIS's own original unified consciousness called the Ursprungs-Ich (L61) — one word for two origins; record both.
- **`q3-how-many-kern-welten-and-alters`**: „The eleven identified parts“ (L89) and the table (L94–L104); no count of Kernwelten.
- **`q9-moonshine-link-boundary`**: the Moonshine-Link as non-local, sub-protocol, entanglement and prehension (L114).
- **`q8-aegis-after-the-vortex`**: AEGIS forced into collapse or evolution (L135), its system forced into a state the briefing names at L153 — read the line.
- **`c13-externe-ebene-beyond-the-simulation`**: Juna/V from an External Level beyond AEGIS's comprehension (L112).

**Not promoted:** the Protocol Ontology terms (Protocols, Overhead, Corrective Wavelets), the Λ-Canon Synthesis and Bill Giannakopoulos, the Paraiyas, IFS, the Skinner boxes, the dialetheic mind, the thematic matrix.

**Two readers**, disjoint: (1) kael, juna, lex, nyx, kiko, lia, rhys, alex, isabelle, moros, selene, argus, alters, tsdp and the records c16, q3; (2) aegis, genesis, ueberwelt, risse, kern-welten, potentialmeer, coheron, dkt, moonshine-link, trennungsprotokoll and the records q9, q8, c13.

No chapter readings: the briefing names acts, not chapters.
