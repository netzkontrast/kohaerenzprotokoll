# Brief — readings from document 475 (step 6)

1 document, one reader, one batch: `ingest-475`. Files go to `Plan/runs/ingest-475/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 475 | `narrative-physik-attraktoren-leserbewusstsein` | 2025-10-16 | „the narrative-physics framework“ (an unsigned German framework text in four parts) | sets the reader („'O'“) as transcendent observer and co-creator of the story-system, reads glitches as the reader's disturbance, defines Logos, Abyssos and Eros as three strange attractors — definitions it says it constructs because its sources leave them undefined (L79) — and ends in a structural recommendation; it calls its quantum language a metaphor (L44); recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (295 lines for `narrative-physik-attraktoren-l`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A framework that constructs its own definitions: write „the narrative-physics framework constructs …“; its attractor definitions are its own (L79), its physics a metaphor (L44). Lines L32, L121, L132 and others name people or carry name-derived concepts — never quote them, never write the names. The reader's designation 'O' stands in single quotes — never quote it. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim). Cut before bold, italics, escaped asterisks and inner quotes.

## Pages — document 475, `narrative-physik-attraktoren-leserbewusstsein`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L36, L58, L91, L93, L105, L123, … (10 lines). central (4–8): AEGIS misreads the principle of being perceived: only what the system perceives exists (L36); under Logos, AEGIS's methods cultivate predictable functional parts and remove emotional data (L91); the central conflict a triadic struggle, not a duality (L123); AEGIS's control protocol in the table (L130).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L132. minor (1–4): emergence and self-organisation in the Eros row of Table 2 (L132 — describe; the row also names a theorist).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L58, L101, L105, L131, L159, L255, … (7 lines). minor (1–4): Abyssos as the drive towards entropy and dissolution, the force that decomposes structures (L101); glitches as localised entropic events (L58); the reader as a fundamental force of chaos (L58).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L119, L121, L132, L281. minor (1–4): Eros's manifestation, Kael's healing as the reintegration of exiled parts such as Juna/V (L119 — quote only the name-free start); Juna/V in the Eros row of Table 2 (L132 — describe).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L66, L68, L70, L103, L119, L121, … (17 lines). central (4–8): Kael's whole journey to healing and functional multiplicity the primary manifestation of Eros (L119); the glitches' effects on Kael in Table 1 (L66–L70); Kael's perception that of an unreliable narrator made of parts, managers suppressing information (L217); the narration as a measurement with a faulty device (L219).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L91; `Kernwelten` L91. minor (1–4): KW1, Logos-Prime, the epitome of Logos among the Kernwelten (L91).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `Logos` L58, L67, L68, L69, L71, L79, … (18 lines). central (4–8): Logos defined as a force striving for coherence, logic, control, stasis and negentropic stability (L87), the drive that creates predictable closed systems; its primary manifestation „die KI AEGIS“ (L91) and KW1, Logos-Prime, its epitome (L91); the table gives AEGIS's control protocol and KW1 (L130); Logos as one of three competing strange attractors (L156); a pathological reaction, not neutral (L123) — the framework's own construction (L79).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L119. minor (1–4): Kael's journey to functional multiplicity as Eros's primary manifestation (L119 — describe around the inner quotes).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L58, L130, L253, L254. minor (1–4): Logos striving for negentropic stability (L87); Eros an anti-entropic force creating emergent, dynamic structures (L115); the table's negentropy (L130).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L52, L56, L58. minor (1–4): the glitches as the literalised in-world manifestations of the reader's interaction (L56), localised entropic events (L58); Table 1 pairs each anomaly with a reader correlate and an effect on Kael (L66–L70).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L103, L217, L234. minor (1–4): TSDP named in the account of AEGIS's methods (L103) and of Kael's parts (L217, L234), without a defining sentence.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L30. not read: an occurrence — `Simulation` on L30 is the story-system in general.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `multiplizitaet`: `Funktionalen Multiplizität` (near `multiplizitat`). read on multiplizitaet (above).
- `nichts-rauschen`: `Nichts` (near `nichtsrauschen`). an occurrence: `Nichts` in the Abyssos row, not the Nichts Rauschen.
- `personas`: `multiple personale Erzähler` (near `persona`). an occurrence: `multiple personale Erzähler` is a narrative technique.


**Record entries:** none.

**No chapter readings**: the framework names no chapter.

**Not promoted:** Abyssos, Eros, the three attractors as a model, 'O', Mitschöpfer, Kontrollparameter, Leerstellen, Die Frakturierte Untersuchung, Echo-Intrusion, and the borrowed concepts (several carry people's names).

**One reader**: every page above.
