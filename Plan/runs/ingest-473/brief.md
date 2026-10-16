# Brief — readings from document 473 (step 6)

1 document, one reader, one batch: `ingest-473`. Files go to `Plan/runs/ingest-473/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 473 | `concept-document-the-nature-of-the-foundation-juna-v-and-the` | 2025-10-15 | „the Foundation concept document“ (an unsigned English concept document with German names, „Concept Document: The Nature of the Foundation, Juna/V, and the Origin of the Simulation“, L11) | explains AEGIS's emergence from the Potentialmeer, the layered simulation (Überwelt, four Kernwelten), the Kohärenz Protokoll's dismemberment that produced Kael, the Juna/V link and The Foundation; it calls its framework „not a convenient plot device“ (L136), recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (137 lines for `concept-document-the-nature-of`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept document: write „the Foundation concept document explains …“. Quote the English as written; cut before bold markers, straight quotes and inner quotes. L94 names a philosopher — never quote it. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim).

## Pages — document 473, `concept-document-the-nature-of-the-foundation-juna-v-and-the`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L15, L25, L27, L33, L35, … (27 lines). central (4–8): AEGIS emerges from the primordial state as a minimal information fragment, the Ursprungs-Ich (L27), an autopoietic system whose principle is „AEGIS is what AEGIS prevents from not being.“ (L27 — cut before the bold, or describe); the crisis event a perturbation from the void, misread through pathologically narrow relevance criteria (L33, L35); AEGIS built a multi-layered simulated reality after the Genesis Crisis (L41); the Kohärenz Protokoll as AEGIS dismembering its own Ursprungs-Ich (L67); AEGIS as Kael's externalised perpetrator introject (L71); ontologically incapable of perceiving the Juna/V link (L96).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L71, L75, L103. minor (1–4): the barriers between the Alters read through the structural-dissociation theory (L71); functional multiplicity as Kael's path (L75); the Alters in the link's functions (L103).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L87. minor (1–4): Juna/V placed outside the simulation, a transcendent entity from the Externe Ebene (L87).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L13. not read: an occurrence — `Genesis` on L13 names the Genesis Crisis in the opening.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L11. minor (1–4): Juna/V a transcendent entity from the Externe Ebene (L87); the link the narrative's primary ontological exploit, a catalyst, not a solution (L83 — describe around the inner quotes).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L37, L41, L49, L55, L56, … (25 lines). central (4–8): „Kael is the primary, sentient fragment that resulted from this act of self-mutilation.“ (L67); AEGIS read as Kael's externalised perpetrator introject (L71); Kael's path is functional multiplicity (L75), a living refutation of AEGIS (L77); reaching The Foundation an epistemological, not physical, act (L121).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L47, L49; `Kernwelt` L47, L49, L53. minor (1–4): the Kernwelten glossed Core Worlds (L49); a table of four, each with a principle and function: KW1 Logos-Prime order and control, KW2 Mnemosyne-Archipel trauma-time and memory, KW3 Cerberus-Labyrinth defence and dissociative barriers, KW4 Kairos-Potentialis emergence and potential (L53–L57).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L35. not read: an occurrence — L35 names coherence in passing; the protocol is read on aegis and kael.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L89, L91. minor (1–4): the link named Moonshine-Link, a narrative synthesis of two concepts — quantum entanglement and a borrowed process concept (L91, L93 — never write L94's name); AEGIS cannot perceive it (L96); its three functions (L102–L104 — describe).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L17, L19. minor (1–4): the second name of the primordial state beside the Potentialmeer (L17, L19).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L17, L19. minor (1–4): the primordial state named „Das Potentialmeer“ (The Sea of Potentiality) and Nichts Rauschen (L17, L19); AEGIS emerges from it (L27).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L71. minor (1–4): the clinical theory used for the barriers between the Alters, written TSDP (L71).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L43, L45. minor (1–4): the Überwelt as a non-anthropomorphic and abstract realm, AEGIS's own construction (L43, L45).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `ontological exploit` (near `alex`). an occurrence: `ontological exploit` is not Alex.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). an occurrence: `Cerberus-Labyrinth` names a Kernwelt here, not the Guardian — recorded on Q5.
- `genesis`: `Genesis Crisis` (near `genesis`). an occurrence: `Genesis Crisis`.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna.
- `kairos`: `Kairos-Potentialis` (near `kairos`). an occurrence: `Kairos-Potentialis` names a Kernwelt here, not the Guardian — recorded on Q5.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the protocol's name.
- `logos`: `Logos-Prime` (near `logos`). an occurrence: `Logos-Prime` names KW1 here — recorded on Q5.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). an occurrence: `Mnemosyne-Archipel` names a Kernwelt here, not the Guardian — recorded on Q5.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). an occurrence: the borrowed theory's name.


**Record entries** (one file each, formatted as earlier entries):
- **`c16-kael-origin`**: the Foundation concept document has Kael as the primary sentient fragment of AEGIS's self-mutilation, the Kohärenz Protokoll dismembering AEGIS's own Ursprungs-Ich (L27, L67); recorded, not applied.
- **`q3-how-many-kern-welten-and-alters`**: the document gives four Kernwelten, KW1–KW4 (L53–L57); recorded.
- **`q5-guardians-and-kern-welten`**: the document names the four Kernwelten Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth and Kairos-Potentialis (L54–L57) — names elsewhere borne by Guardians; recorded, not resolved.

**No chapter readings**: the document numbers sections, not chapters.

**Not promoted:** The Foundation, Ursprungs-Ich, Perturbation from the Void, perpetrator introject, ontological exploit, Gnostic Injection, Covert Integration, gnosis/episteme, and the borrowed theories.

**One reader**: every page above and the three record entries.
