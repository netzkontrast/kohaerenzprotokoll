# Brief — readings from document 210 (step 6)

1 document, one reader, one batch: `ingest-210`. Files go to `Plan/runs/ingest-210/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 210 | `the-coherence-protocol-a-worldbuilding-bible` | 2025-11-03 | „the worldbuilding bible“ (an unsigned English bible for a creative team) | an English worldbuilding bible that calls itself „the authoritative guide“ (L15) — Protocol Ontology, four thematic axes, the worlds, AEGIS, System Kael with nine alters, Juna/V, the plot to a Living Gödel-Satz and the Foundation, and a glossary; close in content to documents 207 and 209, worded apart — its claims recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (208 lines for `the-coherence-protocol-a-world`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A bible that states its world as fact: write „the worldbuilding bible states / defines …“; where it agrees with documents 207 and 209, read only what it adds or words differently (nine alters, Selene as Integrator/Self, the Foundation as strange attractor, the Resonanzkaskade), and say so. English — quote as written; cut before inner straight quotes; `--find` drops digits and subscripts (`KW1`, `K₁`) — quote around them; L179 and L184 run a sentence into the next word.

## Pages — document 210, `the-coherence-protocol-a-worldbuilding-bible`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L55, L63, L72, L81, L82, L90, … (31 lines). central (2–5): „a system whose villainy is born from its own foundational trauma“ (L131); emerged from „Ich-Fragmenten“ of the Potentialmeer (L134) — cut before the inner quotes; the Genesis-Krise encounter with Juna/V triggering a cascade (L135) — read the line; enforcing the Coherence Theory as Autonomous Entropic Gatekeeper (L136).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L109. minor (1–3): KW3 representing „Defense, Paranoia, and Zero-Trust“ (L109).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L109, L152. minor (1–3): Alex as Protector ANP, phobia of helplessness (L152); a protector of KW3 (L109).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L144. minor (1–3): „The following table profiles the key alters within System Kael“ (L144) — nine rows (L149–L157), no Lia and no Argus.
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L23, L197. minor (1–3): read L23 for the Coherons as building blocks of K₁ — quote around the subscript.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L23. minor (1–3): reality emerging from two computational domains „as described by the Dual Kernel Theory“ (L23).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L120. minor (1–3): „The External Level (Externe Ebene)“: the source of the Juna/V connection, a transcendent reality AEGIS cannot model (L120).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L157. minor (1–3): Isabelle as Sexualized EP (L157).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L82, L120, L135, L136, L159, L161, … (11 lines). central (2–5): Juna/V as „The Transcendent Anomaly“, the catalyst that breaks open both closed systems (L159, L161); a transcendent entity from the External Level and an exiled part of Kael's Ursprungs-Ich (L163) — cut before the inner quotes; a catalyst, not a savior (L165).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L55, L63, L72, L81, L90, L105, … (26 lines). central (2–5): Kael as the story's unified protagonist whose psychological state is the causal source of the world's instability (L140) — cut before the inner quotes; Host ANP (L149); the move to functional multiplicity (L179); the climax as the moment Kael achieves it, a high-Φ state, the Living Gödel-Satz (L185).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L103. minor (1–3): „The Core Worlds are tangible manifestations of Kael's psyche“ (L105); KW1 Lex, KW2 the EPs, KW3 Alex and Nyx, KW4 Rhys and Selene (L107–L110) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L154, L155. minor (1–3): Kiko as Freeze/Fear EP, carrying the system's deepest fear (L155).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L107, L150. minor (1–3): Lex as Rational ANP, mirroring AEGIS's logic on a micro scale (L150); KW1 his domain (L107).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L164, L205. minor (1–3): the link as non-local and sub-protocol, a synthesis of quantum entanglement and Whitehead's prehension (L164); read the glossary line L205.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L156. minor (1–3): Moros as Collapse/Emptiness EP, his integration the system's greatest challenge (L156).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L121, L204. minor (1–3): the Sea of Potentiality „also known as“ Nichts Rauschen (L121) — cut before the inner quotes; the glossary line L204.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L109, L154. minor (1–3): Nyx as Fight EP, fierce protector of Kiko (L154); KW3 (L109).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L121. minor (1–3): „The Sea of Potentiality (Das Potentialmeer)“, the primordial high-entropy state (L121); AEGIS's origin (L134).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L110, L151. minor (1–3): Rhys as Caregiver ANP (L151); KW4 (L110).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L112, L114, L203. minor (1–3): the Risse as the physical manifestation of systemic instability and of the isolation objection (L114) — cut before the inner quotes; read the glossary line L203.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L110, L153. minor (1–3): Selene as „Integrator/Self“, a regulator and source of inner wisdom, viewed as an anomaly by AEGIS (L153) — the other bibles type her ANP (Integrator?); KW4 (L110).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L135. minor (1–3): read L135 — decide reading or occurrence and say which.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L142. minor (1–3): the origin of Kael's fragmentation structured by Tertiary Structural Dissociation (TSDP) (L142).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L99, L101. minor (1–3): „The Überwelt is AEGIS's primary control layer and internal laboratory“ (L101); the heading (L99).

- **`genesis`** (minor, 1–2): the Genesis-Krise as AEGIS's tragic flaw, an encounter with a transcendent anomaly, Juna/V (L135) — read the line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading — see the extra page below.


**Record entries** (one file each):

- **`c16-kael-origin`**: Juna/V as an exiled part of Kael's Ursprungs-Ich (L163).
- **`q3-how-many-kern-welten-and-alters`**: nine alters in the table (L149–L157), Lia and Argus absent, Selene as Integrator/Self; four Kernwelten as the domains of parts (L107–L110).
- **`q9-moonshine-link-boundary`**: entanglement and prehension (L164).
- **`c13-externe-ebene-beyond-the-simulation`**: the External Level outside AEGIS's direct control (L118, L120).

**Not promoted:** the Protocol Ontology terms, the four axes, the Foundation („Das Fundament“, a strange attractor, L183 — no page), IIT and high-Φ, the glossary.

**Two readers**, disjoint: (1) kael, juna, lex, nyx, kiko, rhys, alex, isabelle, moros, selene, alters, tsdp, kern-welten and the records c16, q3; (2) aegis, aegis-teilfunktionen, genesis, ueberwelt, risse, externe-ebene, potentialmeer, nichts-rauschen, coheron, dkt, moonshine-link, trennungsprotokoll and the records q9, c13.

No chapter readings.
