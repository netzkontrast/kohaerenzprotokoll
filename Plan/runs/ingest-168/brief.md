# Brief — readings from document 168 (step 6)

1 document, one reader, one batch: `ingest-168`. Files go to `Plan/runs/ingest-168/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 168 | `the-coherence-protocol-a-narrative-design-world-architecture` | 2026-01-02 | „the design brief“ (titled `The Coherence Protocol: A Narrative Design & World Architecture`) | an English design brief for a creative team that calls itself „the authoritative guide“ (L15): the two kernels, AEGIS's genesis, the logics and the physics of information, System Kael's roster, the four Kernwelten with sensory signatures, the Risse, a three-act outline, the Gödel-Gambit and the Moonshine-Link, writing directives and a glossary; its authority is its own claim — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (218 lines for `the-coherence-protocol-a-narra`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A brief that codifies: write „the design brief codifies / directs / describes …“, never as settled. English with German names — quote as written; German names in backticks; cut before inner straight quotes; the kernel symbols are escaped in the export (`K\_1`, `K\_0`) — never quote across them; tables are flattened onto L35, L39, L57, L61 and the glossary is comma-separated (L193–L217).

## Pages — document 168, `the-coherence-protocol-a-narrative-design-world-architecture`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L19, L23, L27, L29, L31, … (22 lines). central (2–4): the Coherence Kernel K1 „embodied by the antagonist system“ (L23); its genesis, „a tragic entity forged by trauma“, a fragment in the Nichts Rauschen (L31); classical logic (L35); an „Externalized Perpetrator Introject“ (L71); the outcome, crash or „Algorithmic Melancholy“, a zombie system (L158); the glossary (L195).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L106, L215. minor (1–2): KW3's „Zero-Trust“ environment — cut before the quotes (L106); Cerberus's Zero-Trust / Paranoia (L215).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L57. minor (1–2): in the ANP table (L57) — read the line.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L102, L215. minor (1–2): „Guardian KW3“, Defense System (L215); KW3: Cerberus-Labyrinth (The Bunker), the domain of Nyx and Soren (L102, L104).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L19. central (2–4): the Coherence Kernel K1 as order (L23) and the Collapse Kernel K0 as entropy and „the ultimate source of objective truth“ (L27); the kernels mirror the psychological conflict (L19); the Monster Group K0 and modular functions K1 (L164).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L29. not read: no line on it beyond a name — say so.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L148, L151, L162. central (2–4): „an epistemological checkmate derived from Gödel's Incompleteness Theorems“ (L153); System Kael becomes a „Living Gödel Sentence“ — cut before the inner quotes (L156); the dilemma (L157); Act III, the alters execute it (L148); delivered via the Moonshine-Link (L162).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L134, L162, L165, L199. minor (1–2): „an external entity, Juna/V“ (L162); first contact in Act I (L134); the link lets her give Kael strength and gnosis (L165); „External Anomaly“ in the glossary (L199).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L27, L31, L35, L45, … (26 lines). central (2–4): „System Kael“, „a collection of distinct consciousnesses, or alters, sharing a single mind“ (L49); 11 core alters plus an ISH (L53); the Host (L57); paraconsistent logic (L35, L197); the three acts (L133, L140, L147).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L112, L217. minor (1–2): „Guardian KW4“, Potential (L217); KW4: Kairos-Potentialis (The Garden), „the only world where new things can be created“ (L112, L116).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L39, L82, L124. central (2–4): „The settings … known as the Kernwelten“, „externalized diagnostic charts of System Kael's mind“ (L82); the four with domains and sensory signatures (L84–L120).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L61, L78, L185, L205. minor (1–2): unburdened of his terror into „Playfulness“ and „Intuition“ (L78); the glossary, Child (L205).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: no line on it beyond a name — say so.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L57, L86, L185, L201. minor (1–2): „Rationalist“, „Mirrors AEGIS“ (L201); KW1 the domain of Kael and Lex (L86).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L211. minor (1–2): „Guardian KW1“, ANP-Logic Proxy (L211); KW1: Logos-Prime (The Cage) (L84).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L93, L213. minor (1–2): „Guardian KW2“, Memory Keeper (L213); KW2: Mnemosyne-Archipel (The Swamp), the domain of Lyra and the EPs (L93, L95).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L39, L134, L160, L162, L166, L199. central (2–4): „a connection between Kael and an external entity, Juna/V“ (L162); its name from Monstrous Moonshine (L164); „a backdoor connection“ (L165); „Non-Local Resonance“ and a blind spot of AEGIS (L166).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L61, L207. minor (1–2): „Persecutor“, „Shame, Implosion“ (L207); the EP table (L61).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L27, L31, L39, L177. minor (1–2): AEGIS's genesis „within the chaotic Nichts Rauschen“ (L31); Cosmic Horror for the Genesis-Krise, the Void and the Nichts Rauschen (L177).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L61, L77, L104, L203. minor (1–2): the „Fighter“ unburdened into a focused „Guardian“, the system's chief of security (L77); KW3 the domain of Nyx and Soren (L104).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L122, L124, L134. central (2–4): „the central environmental mechanic driving the plot“, tears in the simulation, caused by the „Isolation Objection“ (L124); they shatter Act I's stability (L134).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L67, L114, L209. minor (1–2): „Internal Self-Helper (ISH) / Integrator“ (L67); KW4 the domain of Selene and Elara (L114); the glossary (L209).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L45, L57, L61, L65, L75, L197. minor (1–2): the narrative architecture modelled on TSDP (L45); the roster's categories (L57, L61).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). a reading: Coherons, „atoms of persistence“ — cut before the quotes (L39).
- `genesis`: `Genesis Crisis` (near `genesis`), `Genesis-Krise` (near `genesis`). a reading: „The Genesis of AEGIS: A Tragedy of Ontological Horror“ (L29, L31); Kael's „Genesis Crisis“ in Act I (L134); the Genesis-Krise as cosmic horror (L177).
- `guardians`: `Guardian` (near `guardians`). a reading: the glossary's four Guardians, one per KW (L211–L217); Nyx's unburdened role „Guardian“ (L77) is another sense — say so.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the project's name in the prose.
- `personas`: `Theory of Structural Dissociation of the Personality (TSDP)` (near `persona`). occurrence: the TSDP's full name (L45).


**Record entries** (one file each):

- **`c4-guardians-and-aegis`**: the Moonshine-Link „a fundamental blind spot“ in AEGIS's panopticon (L166).
- **`c6-guardians-count-and-pairing`**: four Guardians, LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, Kairos–KW4 (L211–L217), no Sophia.
- **`q3-how-many-kern-welten-and-alters`**: „11 core alters plus an Internal Self-Helper“ (L53); four Kernwelten; Lyra, Soren and Elara named as domains' alters (L95, L104, L114).
- **`q8-aegis-after-the-vortex`**: „It crashes or transforms“ into Algorithmic Melancholy, a zombie system (L158).
- **`q9-moonshine-link-boundary`**: subjective data, not packets (L166).

**Not promoted:** the two kernels' English names (on dkt), Operational Closure, Correspondence-Check, the War of Logics, Coherons' companions in the L39 table, Society of Self, Positive Intent, Externalized Perpetrator Introject, Trauma Loop, Unburdening, the sensory signatures, Isolation Objection, Validation War, Paradox of Misaligned Coherence, Non-Local Resonance, Ontological Blindness, Polyphonic Prose, Dual-Voice Strategy, the Gardener's Mandate, Lyra, Soren, Elara (no pages; on Q3).

**No chapter readings:** the outline gives acts by chapter range only (L130, L137, L144), which are not read.

**Two readers**, disjoint: (1) kael, juna, tsdp, lex, alex, nyx, kiko, moros, selene, moonshine-link, goedel-gambit and the records q3, q9, c4; (2) aegis, aegis-teilfunktionen, dkt, nichts-rauschen, genesis, coheron, risse, kern-welten, logos, mnemosyne, cerberus, kairos, guardians and the records q8, c6.
