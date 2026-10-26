# Brief — readings from document 535 (step 6)

1 document, one reader, one batch: `ingest-535`. Files go to `Plan/runs/ingest-535/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 535 | `kohaerenz-protokoll-the-official-project-handbook` | 2026-01-02 | „the project handbook“ | an English handbook that calls itself „the canonical, single source of truth“ (L17) and gives „the final, unchallengeable ruling“ (L33): the AEGIS-versus-Kael thesis, rulings, the DKT, the two systems, a 39-slot structure with four Kernwelten and mandated prose rules; its canon claim is its own and is recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (132 lines for `kohaerenz-protokoll-the-offici`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A self-declared canon: write „the project handbook rules …“, „… calls … canonical“; its rulings are its claims, never the novel's canon. **Never cite L83's third table row** (an earlier name) — quote only the named rows. Never quote a span naming a person or a concept named after one (L41's „living …-Satz“, L57–L59). No gendered pronoun for Kael, AEGIS or any part in our own prose; quotations stay verbatim and are cut before „his“/„He“ where possible; never quote „male host“.

## Pages — document 535, `kohaerenz-protokoll-the-official-project-handbook`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L27, L41, L55, L61, … (18 lines). central (3–8): „'Coherence  instead of  Truth'“ (L21); exclusionary order, phobia of paradox (L23); fate ruled: transformed, not destroyed (L41); „not a malevolent villain but a tragic, self-maintaining (autopoietic) system“ (L67); operational closure, LFI, discursive logic, the „Paradox of Misaligned Coherence“ (L73–L75); the ultimate manifestation of K₁ (L55); its voice cold and clinical, „Algorithmic Horror“ (L115, L117).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L83. minor: the ANP row „The Protector-ANP“, a strategic defender, strategy Sublimation, domain External Conflict (L83).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L27, L74, L126. minor: AEGIS's discursive logic treats each alter as a separate speaker (L74); intrusions in italics represent the phobias between alters (L126).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L51, L53. minor: the Dual Kernel Theory as the engine of existence (L51); the perpetual cycle of K₀ and K₁ (L55).
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L45. minor: the ruling that the Wächter-Zwiespalt is canonical, allowing doubt and dissent among the antagonist faction (L45).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L23, L25, L27, L39, L41, … (19 lines). central (3–8): „'Coherence  through  Integration'“ (L21); emergent order from accepting contradictory parts (L23); the host of a TSDP/IFS system (L39 — quote no „male“); the climax driven by Kael's integrated consciousness (L43); „not a monolithic individual but a complex, fragmented system“ (L79); the ANP row „The Host“ (L83); the voice from fragmentation to a „choric 'we'“ (L121, L127).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L95, L97; `Kernwelt` L95, L97. minor: active components inside the Überwelt, each an externalisation of a facet of Kael's psyche and of AEGIS's logic (L97); the four worlds KW1 Logos-Prime, KW2 Mnemosyne-Archipel, KW3 Cerberus-Labyrinth, KW4 Kairos-Potentialis with their principles (L97); worlds designed by AEGIS to test and control (L87).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L85. minor: the EP row „The Wounded Child“, an Exile holding core trauma, strategy Attachment Cry, KW2 (L85).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11) (J9).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L83. minor: the ANP row „The Rationalist“, the „System Administrator“, strategy Intellectualization, KW1 (L83) — cut before „He mirrors AEGIS“ or quote „mirrors AEGIS“ alone.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L85. minor: the EP row „The Apothecary“, Freeze/Shutdown, hopelessness and dread, KW2 (L85).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L85. minor: the EP row „The Avenger“, the system's rage, Fight, KW3 (L85).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L39, L79, L81, L83, L85. minor: the protagonist's system „TSDP-diagnosed, IFS-guided“ (L39); TSDP as the diagnostic framework for the fragmentation (L79).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L97. minor: „the purely information-based control plane that serves as AEGIS's operational network“, holding the Kernwelten (L97).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `KW3: Cerberus-Labyrinth` (near `cerberus`), `Cerberus-Labyrinth` (near `cerberus`). an occurrence: the world KW3 Cerberus-Labyrinth, read on kern-welten.
- `genesis`: `Genesis-Krise` (near `genesis`). a reading: AEGIS's tragic origin „Genesis-Krise“ (L41) — read below.
- `kairos`: `KW4: Kairos-Potentialis` (near `kairos`), `Kairos-Potentialis` (near `kairos`). an occurrence: the world KW4, read on kern-welten.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `logos`: `KW1: Logos-Prime` (near `logos`), `Logos-Prime` (near `logos`). an occurrence: the world KW1, read on kern-welten.
- `mnemosyne`: `KW2: Mnemosyne-Archipel` (near `mnemosyne`), `Mnemosyne-Archipel` (near `mnemosyne`). an occurrence: the world KW2, read on kern-welten.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). an occurrence: „Rauschen“ is AEGIS's word for noise (L23), not the paged Nichts-Rauschen.
- `personas`: `Theory of Structural Dissociation of the Personality (TSDP)` (near `persona`). an occurrence.


**Readings by the sentence beyond the lookup** (English names for paged terms, J100):
- **`genesis`** (minor): AEGIS's tragic origin „Genesis-Krise“ (L41).
- **`algorithmische-melancholie`** (minor): AEGIS's fate, „permanent  ""algorithmic melancholy.""“ (L41).
- **`kohaerenz-kernel`** (minor): „The Coherence Kernel (K₁)“, order and preservation, AEGIS its ultimate manifestation (L55).
- **`kollaps-kernel`** (minor): „The Collapse Kernel (K₀)“, entropy and erasure, a „correspondence check“ (L55).
- **`multiplizitaet`** (minor): the arc toward „functional multiplicity“ (L39).

**Record entries:** none.

**Not promoted:** Exclusionary/Emergent Order, Self-Referential/Integrative Logic, Correspondence-Based Truth, ANP-EP Phobia, Wächter-Zwiespalt, K₀ and K₁ as surfaces, the person-named protocol and its terms, ontological mass, Semantic Tidal Forces, Great Fact, LFI, Discursive Logic, Paradox of Misaligned Coherence, The Sentinel, Mosaic-Structure, slots, Gravitational Architecture and its three phases, Algorithmic Horror, Dual-Voice Strategy, choric 'we', titration, Performative Prose, IFS, dialetheism, gnosis, episteme.

**One reader**: every page above.
