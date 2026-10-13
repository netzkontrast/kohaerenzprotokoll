# Brief — readings from document 221 (step 6)

1 document, one reader, one batch: `ingest-221`. Files go to `Plan/runs/ingest-221/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 221 | `the-coherence-protocol-a-world-bible` | 2025-10-15 | „the world bible“ (an unsigned English world bible) | an English reference in five parts — metaphysics, AEGIS's architecture, System Kael's alters, the simulated realities, the central dialectic — that calls itself „the canonical and authoritative reference“ (L13): its claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (196 lines for `the-coherence-protocol-a-world`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A reference that defines: write „the world bible defines …“ or „… names …“; its canon claim (L13) is recorded once as its claim, never applied. English — quote as written; German names stand in italics or headings with escaped asterisks — quote the English words around them. `--find` drops digits (`KW1`, `D2`) — quote around them.

## Pages — document 221, `the-coherence-protocol-a-world-bible`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L29, L36, L38, L42, L44, … (30 lines); `Entropic Gatekeeper` L58, L60, L80. central (3–6): AEGIS (Autonomous Entropic Gatekeeper for Integrity Systems) as a tragic autopoietic system, not a villain (L60); emerged from a minimal information fragment fighting the Nothingness Noise (L64); its axiom „AEGIS is what AEGIS prevents itself from not being.“ (L66), existence through negation (L68); a layered hybrid architecture — LFI core, Discursive Logic modules, a perverse learning loop (L74–L76); the Paradox of Misaligned Coherence, Paradoxon X (L84); Algorithmic Horror (L88).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `zero-trust` L80. minor (1–3): a „zero-trust“ principle analogous to Byzantine Fault Tolerance, every piece of information validated without trusting its source (L80).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `alters` L75, L84, L104, L106, L107, L113, … (11 lines). central (3–6): „alters“ as the two primary types of self-states, ANPs and EPs (L104–L107); phobias between the parts (L109); the table of eight alters with TSDP classification (L117–L125); functional multiplicity, not fusion — the alters continue to exist as a team (L131, L137).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L80, L164. minor (1–3): Cerberus as one of the four Guardians (L80); KW3 Cerberus-Labyrinth, The Boundary Fortress, Relevance Logic / NP-Complete, domain of Praetor and Nox (L164).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L62. minor (1–3): „Genesis and Core Philosophy“ (L62): AEGIS emerged from a minimal information fragment fighting for survival against the Nothingness Noise (L64).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L80. minor (1–3): Guardians as specialized, autonomous agents AEGIS employs in the Core Worlds — LogOS, Mnemosyne, Cerberus and Kairos (L80) — quote around the names.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L40, L42, L46, L52, L180, L187. minor (1–3): Juna/V and Kael connected by the Moonshine-Link (L40–L42); Kael and Juna as „two parts of a single, inseparable system“ (L46); Kael experiencing Juna's emotional state as colour, sound or taste (L52); Kael / Juna / The Foundation as coherence through integration (L187).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L42, L46, L51, L52, L75, L84, … (20 lines). central (3–6): Kael as „not a singular identity but a complex, adaptive system“, a society of self (L100); Tertiary Structural Dissociation (L104); „Kael (ANP, Host/Searcher)“ as one row of the alter table (L118) — quote around the escapes; the Index vs. Nox dyad (L127); functional multiplicity as goal (L131); the dialetheic mind (L141); the Moonshine-Link as catalyst for his healing (L52).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L80, L165. minor (1–3): Kairos as one of the four Guardians (L80); KW4 Kairos-Potentialis, The Garden of Possibilities, Explorative/Dialetheic Logic, domain of Limina and Silas (L165).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L155. minor (1–3): the four Core Worlds (Kernwelten) as simulated realities, each with a logical principle and a facet of Kael's psyche (L155–L157); the table KW1–KW4 with principle, domain and aesthetic (L162–L165) — quote around the digits.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the novel's title „Kohärenz Protokoll“ (L13).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L80. minor (1–3): LogOS as one of the four Guardians (L80); KW1 Logos-Prime, The Construct City, Classical Logic / P-Class, domain of Index and Kael (L162).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L80, L163. minor (1–3): Mnemosyne as one of the four Guardians (L80); KW2 Mnemosyne-Archipel, The Resonance Landscape, Paraconsistent Logic, domain of the EPs (L163).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L40, L42, L48. central (3–6): the Juna/V Moonshine-Link as a disruptive, transcendent connection outside AEGIS's control (L42); a non-local, sub-protocol connection, quantum entanglement and Whitehead's prehension (L44–L47); its three functions — Ontological Exploit, a „living Gödel-Satz“ (L50); Structural Blind Spot (L51); Catalyst for Healing (L52).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts Rauschen` L21, L23. minor (1–3): Das Nichts Rauschen (The Nothingness Noise), also Die Leere, as an active, high-entropy Potential Sea of uncompressed informational noise (L23); its visual, auditory and psychological manifestations (L25–L27); the force against which AEGIS defines itself (L29).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L124, L127. minor (1–3): „Oblivion (EP, Shutdown Response)“: total shutdown, hopelessness, numbness (L124) — quote around the escapes; the dyad Silas vs. Oblivion (L127).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L167, L169; `Glitches` L169. minor (1–3): „Cracks“ (Risse) or Glitches with a dual nature (L167–L169): for AEGIS symptoms of instability (L171), for Kael moments where the dissociative barriers weaken (L172); the seams of the two models (L174).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L121, L127, L165. minor (1–3): „Silas (ANP, Caretaker)“, compassionate caretaker and mediator (L121) — quote around the escapes; Silas vs. Oblivion (L127); KW4's domain with Limina (L165).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L102, L117. minor (1–3): the Theory of Structural Dissociation of the Personality (TSDP) as Kael's clinical framework (L102–L104); the alter table's TSDP classification (L117).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L151, L153. minor (1–3): the Digital Überwelt as the abstract, information-based reality where AEGIS's core processes run, the system's „mind“ (L151–L153).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `Ontological Exploit` (near `alex`). occurrence: `Ontological Exploit` is the Moonshine-Link's function (L50), not Alex.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title `Kohärenz Protokoll` (L13, L149, L180).
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: `Theory of Structural Dissociation of the Personality` is TSDP's full name (L102), read on tsdp.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is an alter's name (L123), not the residual echoes.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: four Guardians named — LogOS, Mnemosyne, Cerberus and Kairos (L80); no Sophia.
- **`q5-guardians-and-kern-welten`**: the four Guardian names (L80) beside the four world names Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis (L162–L165); the document does not say how they relate.
- **`q1-guardians-and-aegis`**: Guardians as AEGIS's specialized, autonomous agents (L80).
- **`q3-how-many-kern-welten-and-alters`**: eight alters (L118–L125) and four worlds, each world assigned alters or parts (L162–L165).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as AEGIS's information-based domain, its „mind“ (L153).
- **`q9-moonshine-link-boundary`**: a non-local, sub-protocol connection AEGIS is structurally blind to (L44, L51).

**Not promoted:** The Foundation, Paraiyas, The Connection, Index, Praetor, Nox, Echo, Limina, the dyads, the Dialetheic Mind, Algorithmic Horror, LFI and Discursive Logic, the perverse learning loop, the comparison table.

**Two readers**, disjoint: (1) kael, juna, alters, silas, oblivion, tsdp, kern-welten, logos, mnemosyne, cerberus, kairos, ueberwelt, risse; (2) aegis, aegis-teilfunktionen, genesis, guardians, moonshine-link, nichts-rauschen and the records c6, q5, q1, q3, q6, q9.

**Chapter readings**: none — the world bible names no chapter.
