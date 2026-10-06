# Brief — readings from document 162 (step 6)

1 document, one reader, one batch: `ingest-162`. Files go to `Plan/runs/ingest-162/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 162 | `deconstructing-reality-s-architecture` | 2026-02-27 | „the learner's guide“ (titled `Deconstructing Reality's Architecture`) | an English learner's guide of 2026-02-27 to the project: the Dual Kernel Theory, AEGIS's origin and logic, System Kael's roster of alters, the four Kernwelten with sensory signatures, the Risse, the Gödel-Gambit and the Moonshine-Link, a 39-chapter arc and an entity appendix; it reports „the documentation“ and calls the project „an allegory for the treatment of complex trauma“ (L76) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (334 lines for `deconstructing-reality-s-archi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide that reports the project's documentation: write „the learner's guide describes / reports …“; where it says „The documentation identifies“, it is the guide's report of other documents. English — quote as written, never translated; cut before inner straight quotes; German names it bolds go in backticks; the export lost the kernel symbols — never restore them.

## Pages — document 162, `deconstructing-reality-s-architecture`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L31, L37, L39, L43, L45, … (38 lines). central (2–4): its prime directive „AEGIS is what AEGIS prevents itself from not being“ (L31); Ontological Blindness (L33); „AEGIS did not begin as a god“, a fragment in the Nichts Rauschen (L47); a paradox „is a lethal pathogen“ (L55); the Externalized Perpetrator Introject (L137); the outcome, Algorithmic Melancholy and Zombie System (L226, L285).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L188, L314. minor (1–2): KW3 „a“ Zero-Trust environment (L188) — cut before the quotes; Cerberus's Zero-Trust / Paranoia (L314).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L103, L116. minor (1–2): „The Shieldbreaker / Protector“, a proactive strategic defender (L103).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L80. minor (1–2): System Kael, „a collection of distinct consciousnesses (Alters) sharing a body/mind“ (L80); the roster (L100–L128).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L174, L314. minor (1–2): KW3 Cerberus-Labyrinth (The Bunker) (L174); in the appendix „Guardian KW3“ (L314).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L19. minor (1–2): the DID frame of System Kael (L19) — read the line.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L23. central (2–4): the Dual Kernel Theory „defined in the project’s documentation as the“ (L23); the Coherence Kernel, order and information preservation (L31); the Collapse Kernel as the source of truth (L37); `K1`/`K0` in the conclusion (L293).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L43. minor (1–2): „The Genesis of AEGIS: From Void to Tyrant“ (L43); the Genesis Crisis (L45).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L218, L230, L284, L295. central (2–4): Kael's „Living Gödel Sentence“ (L223); AEGIS's dilemma, „If it accepts Kael, it admits a contradiction“ (L225); the weapon to the Moonshine-Link's delivery (L230); „Climax: The Gödel-Gambit“ (L284).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L233, L235, L267, L306. minor (1–2): „Juna is not an alter“ (L233), Juna/V an external entity; „External Anomaly“ in the appendix (L306).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L41, L47, L55, L57, L59, … (33 lines). central (2–4): „System Kael“, a collection of alters sharing a body (L80); the Host, social camouflage (L101); „Kael achieves Functional Multiplicity“ (L223); „Kael becomes“ the Gardener (L285).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L190, L315. minor (1–2): KW4 Kairos-Potentialis (The Garden) (L190); „Guardian KW4“ (L315).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L70, L142. central (2–4): the four worlds with nicknames and sensory signatures (L143–L204); KW4 „the only world where new things can be created“ (L204).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L116, L253, L257, L309. minor (1–2): in the roster (L116) and the appendix (L309).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. occurrence: the title (L15).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L102, L146, L253, L257, L275, L307. minor (1–2): „The Rationalist“, cold emotion-avoiding logic, mirroring AEGIS (L102).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L312. minor (1–2): „Guardian KW1“, ANP-Logic Proxy (L312).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L159, L212, L313. minor (1–2): KW2 Mnemosyne-Archipel (The Swamp) (L159); „Guardian KW2“, Memory Keeper (L313).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L71, L228, L230, L234, L267, L306, … (7 lines). minor (1–2): „the delivery system“ (L230); AEGIS „Ontologically Blind“ to it (L235).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L117, L310. minor (1–2): „The Persecutor / The Frozen“, the internal implosion (L117).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L39, L47, L72. minor (1–2): the primordial state „known as the“ Nichts Rauschen (Nothingness Noise), a roaring nothingness (L39); AEGIS's origin in it (L47).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L115, L116, L176, L253, L257, L275, … (7 lines). minor (1–2): „The Sentinel / Fighter“, the system's rage (L115).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L39. minor (1–2): the Nichts Rauschen line names the Potentialmeer (L39) — read the line.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L206, L208, L267. central (2–4): „The Risse (Rifts) are the central environmental mechanic that drives the plot“ (L208); „They are caused by the Isolation Objection“ (L211).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L128, L192, L311. minor (1–2): „Selene is unique“, an Internal Self-Helper, an observer part (L128).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L19, L76, L90, L294, L305. minor (1–2): the clinical model of System Kael (L19, L90).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L282. minor (1–2): „Kael enters KW4 (Potential) and the Überwelt (AEGIS's Core)“ (L282) — cut around the digit.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). occurrence unless the line defines Coherons — read it; else not read.
- `genesis`: `Genesis Crisis` (near `genesis`). a reading — on genesis above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the TSDP's full name.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: the roster the guide reports (L90–L128) with Aris and Elara, and „Tariq“ and „Nova“ as likely subsidiary ANP functions (L130); four Kernwelten; dated 2026-02-27.
- **`q8-aegis-after-the-vortex`**: AEGIS „crashes/transforms“ into Algorithmic Melancholy (L226), a „Zombie System“ (L285).
- **`q9-moonshine-link-boundary`**: „the delivery system“ (L230); AEGIS ontologically blind to it (L235).
- **`c6-guardians-count-and-pairing`**: the appendix pairs LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, Kairos–KW4 (L312–L315), no Sophia.

**Not promoted:** Ontological Blindness, Isolation Objection, Externalized Perpetrator Introject, Zombie System, the Gardener, Polyphonic Prose, Aris, Elara, Tariq, Nova (no pages; on Q3), the sensory signatures, the 39-chapter arc.

**Two readers**, disjoint: (1) kael, alters, did, juna, lex, alex, nyx, kiko, moros, selene, tsdp, moonshine-link, goedel-gambit and the records q3, q9; (2) aegis, aegis-teilfunktionen, dkt, nichts-rauschen, potentialmeer, genesis, risse, kern-welten, ueberwelt, logos, mnemosyne, cerberus, kairos and the records q8, c6.
