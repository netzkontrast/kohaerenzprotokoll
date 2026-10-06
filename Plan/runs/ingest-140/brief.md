# Brief — readings from document 140 (step 6)

1 document, one reader, one batch: `ingest-140`. Files go to `Plan/runs/ingest-140/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 140 | `dual-plot-architecture-a-narrative-foundation-for-kohaerenz` | 2025-11-03 | „the dual plot architecture“ (titled `Dual Plot Architecture: A Narrative Foundation for 'Kohärenz Protokoll'`, L11) | an English design document of 2025-11-03: a Grand Argument Story as thesis (AEGIS), antithesis (System Kael) and synthesis (the Gödel Gambit) (L13–L39), four „Existenz-Matrizen“ (AEGIS, Kael with an alter table, Juna/V, Das Fundament, L41–L88), the four Kernwelten (L92–L110), a 39-chapter structure in three parts (L114–L132), a short-story mosaic (L136–L150) and a style methodology (L154–L179); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (180 lines for `dual-plot-architecture-a-narra`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design proposes: write „the dual plot architecture frames / proposes …“; English — quote as written, never translate; German terms in single quotes ('Nichts Rauschen', 'Das Fundament') and inner straight quotes — cut quotations before them. Kael is male; Juna/V is „it“ in places — write as it does.

## Pages — document 140, `dual-plot-architecture-a-narrative-foundation-for-kohaerenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L23, L24, L29, … (25 lines). central (2–4): „The Thesis: AEGIS's Coherence Through Negation and Control“ (L17); „framed not as a malicious entity but as a tragic one“ (L47); its tragic flaw the Paradoxon der Fehlausgerichteten Kohärenz (L50); its forced evolution to a paraconsistent state (L52).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L66, L106. minor (1–2): „Alex (ANP - Protector)“ (L66).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L33, L35, L74, L106, L142, L150, … (7 lines). minor (1–2): the alters' phobias and functional multiplicity (L33, L35, L74); the alter table (L63–L72).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L104, L106. minor (1–2): KW3's Guardian (L106).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L49. minor (1–2): „2.1.1 Genesis:“ AEGIS emerged from the Nichts Rauschen (L49) — cut before the quote.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel Gambit` L37, L132. minor (1–2): „The Synthesis: The Gödel Gambit“ (L37); Chapters 35–39 (L132).
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L110. minor (1–2): L110; the Guardians' behavioural loops (L170); the Guardian's Blind Spot story (L149).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L43, L50, L52, L76, L78, L80, … (9 lines). minor (1–2): „The Juna/V entity is a mysterious external force that operates outside of AEGIS's control“ (L78); the Impact Character (L81).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L27, L29, L33, L34, L39, … (35 lines). central (2–4): „The Antithesis: Kael's Coherence Through Integration“ (L27); modelled on TSDP (L58); „Kael (ANP - Host)“ (L64); his integrated self „a“ living Gödel-Satz — cut before the quote (L39).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L108, L110. minor (1–2): KW4 „the domain of the Guardians“ Kairos and Sophia (L110).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L92, L94, L142. central (2–4): „epistemological landscapes“ (L94); KW1 Logos-Prime (Construct-City), KW2 Mnemosyne-Archipel, KW3 Cerberus-Labyrinth, KW4 Kairos-Potentialis (L96–L108).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L69, L102, L163. minor (1–2): „Kiko (EP - Frightened Child)“ (L69); KW2 (L102).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9); the paradox on aegis.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L65, L98, L163. minor (1–2): „Lex (ANP - Analyst)“ (L65); KW1 (L98).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L70, L102. minor (1–2): „Lia (EP - Ambivalent Child)“ (L70).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L98. minor (1–2): „This world is the domain of the Guardian“ LogOS (L98).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L100, L102, L149. minor (1–2): KW2's Guardian (L102); a story from a Guardian such as Mnemosyne (L149).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L80. minor (1–2): „a non-local, sub-protocollary connection“ (L80).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L71. minor (1–2): „Moros (EP - Collapse)“ (L71).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L19, L49, L148, L171. minor (1–2): „a pre-real state of pure potentiality and high entropy“ (L49); its intrusion through the Risse (L171).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L68, L106, L163. minor (1–2): „Nyx (EP - Fighter)“ (L68); KW3 (L106).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L67. minor (1–2): „Rhys (ANP - Caregiver)“ (L67) — an ANP.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L51, L120, L171, L178. minor (1–2): the Risse's sensory signature (L171); typographical fragmentation mirroring them (L178); Part 1's first encounters (L120).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L72, L110. minor (1–2): „Selene (Integrating Self)“ (L72); most influence in KW4 (L110).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L110. minor (1–2): the same line (L110).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L29, L58, L63. minor (1–2): „Theory of Tertiary Structural Dissociation of the Personality (TSDP)“ (L58).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the role word.
- `guardians`: `Guardian` (near `guardians`). `Guardian` — on guardians above.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenz-Patching-Protokolle` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).
- `personas`: `Theory of Tertiary Structural Dissociation of the Personality` (near `persona`). occurrence: TSDP's full name, on tsdp.


**Record entries** (one file each):

- **`q7-what-734-names`**: the story „Component 734“ — the minimal I-fragment within the Nichts Rauschen before it was functionalized as Component 734 within AEGIS (L148).
- **`c14-aegis-first-person-chapter`**: a story „from the first-person perspective of the minimal“ I-fragment (L148) and one told by a Guardian through its logs (L149) — stories of the mosaic, not chapters.
- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten (L92–L110); nine alters in the table with TSDP classes (L63–L72), Rhys an ANP.
- **`c6-guardians-count-and-pairing`**: LogOS KW1, Mnemosyne KW2, Cerberus KW3, Kairos and Sophia KW4 (L98–L110) — dated 2025-11-03.
- **`c9-konstrukt-stadt-scale`**: „KW1: Logos-Prime (Construct-City)“ (L96) — KW1 only.

**Not promoted:** Existenz-Matrizen, Das Fundament (no page), strange attractor, ergodic literature, algorithmic horror, the short-story concepts, metafictional techniques.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, juna, moonshine-link, goedel-gambit, genesis, nichts-rauschen, risse, logos, mnemosyne, cerberus, kairos, sophia, guardians, and the entries q7, c14, c6.
- Reader 2: kael, lex, alex, rhys, nyx, kiko, lia, moros, selene, alters, tsdp, kern-welten, and the entries q3, c9.
