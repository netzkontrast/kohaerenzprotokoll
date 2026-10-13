# Brief — readings from document 272 (step 6)

1 document, one reader, one batch: `ingest-273`. Files go to `Plan/runs/ingest-273/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 272 | `narrative-architecture-dossier-coherence-protocol` | 2026-01-02 | „the architecture dossier“ (an unsigned English design brief) | a design brief for a writing team: the Genesis-Krise as originating wound, AEGIS's definition and flaw, System Kael and an eleven-part cast table, a coherence/correspondence physics of the world, a three-act plot with German beat labels, and technique directives (`must`); it calls itself „the definitive architectural blueprint“ and „the master guide“ (L17), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (133 lines for `narrative-architecture-dossier`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A directive brief: write „the architecture dossier sets / directs / calls …“; its `must` lines are instructions to writers, not descriptions of the novel. Its tables are flattened to one line each (L61, L72): quote short single spans. German beat labels carry English glosses in parentheses.

## Pages — document 272, `narrative-architecture-dossier-coherence-protocol`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L27, L29, L33, L37, L47, … (20 lines). central (3–6): „Aegis ist, was Aegis verhindert, dass es nicht ist“, expanded „Autonomous Entropic Gatekeeper“, framed not as a simple villain (L29); an autopoietic loop and Hybris (L29); Kael's healing an existential threat to it (L37); a tragic antagonist (L77); its rigid protocol fails (L103).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L72. minor (1–3): in the cast table (L72), typed there.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L72. minor (1–3): in the cast table as `Mixed` (L72).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L130. minor (1–3): „Entropie/Risse“ visualised as data corruption, static, glitching geometry and data-weathering (L130).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L72. minor (1–3): in the cast table (L72).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L48, L88. minor (1–3): an agent like Juna/V whose influence forces the system's model to interact with an external environment (L48); a direct encounter with Juna/V as the inciting incident (L88).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L33, L37, L48, L49, L55, … (26 lines). central (3–6): „System Kael, is the living embodiment and externalization of AEGIS's trauma“, ANPs and EPs (L33); his healing an existential threat to AEGIS (L37); his journey the victory of correspondence (L49); the cast table, parts as aspects of one consciousness (L72); the midpoint: not a system flaw but the living memory of AEGIS's failure (L96).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L61, L72, L94, L123. minor (1–3): Kiko's hypervigilance in forced cooperation (L94); stream of consciousness when Kiko is active (L123).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L29. not read: occurrence — `Kohärenz` at L29 is inside AEGIS's definition, read on aegis.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L56, L61, L72, L89, L122, L126. minor (1–3): Lex and Rhys in strategic disagreement (L56); Lex's analytical prose style (L122).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L72. minor (1–3): in the cast table (L72).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L72. minor (1–3): in the cast table (L72).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L61, L72, L94, L122. minor (1–3): Nyx's aggression for defence (L94); aggressive, clipped prose when Nyx fronts (L122).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L56, L61, L72. minor (1–3): strategic disagreement with Lex (L56).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L130. minor (1–3): the Rifts as physical manifestations of decoherence, where the internal model meets an external environment (L48); a „Riss“ as inciting incident (L88); the dangerous environment of the Rifts (L94); „Entropie/Risse“ visualised (L130).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L72. minor (1–3): in the cast table as `Mixed` (L72).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L33, L51, L53, L72. minor (1–3): ANPs and EPs as the theory's parts (L33); TSDP named (L51, L53).

- **`genesis`** (minor, 1–2): the Genesis-Krise, „the single, originating wound of the narrative“, which exceeded the system's integrative capacity (L25).
- **`ueberwelt`** (minor, 1): the `Overworld` as „a fragile, isolated quantum system“ (L47).
- **`cache-kohaerenz`** (minor, 1–2): the cache-coherence analogy for Kael's system (L67) and its own internal „cache coherence protocol“ (L101).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). reading: `Genesis-Krise` the originating wound (L25), on genesis.
- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: `Gödel` names the theorem, not the Gambit, unless the climax line names the Gambit.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title and AEGIS's definition.
- `personas`: `Apparently Normal Personality parts` (near `persona`), `Emotional Personality parts` (near `persona`), `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's names for its parts, read on tsdp.
- `risse`: `Riss` (near `risse`), `Entropie/Risse` (near `risse`). reading: `Riss` (L88) and `Entropie/Risse` (L130).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: the cast table's eleven parts, Selene and Argus `Mixed` (L72).
- **`c16-kael-origin`**: System Kael „the living embodiment and externalization of AEGIS's trauma“ (L33); the living memory of AEGIS's failure (L96).

**Not promoted:** the autopoietic loop, Hybris, the Coherence and Correspondence Theories, the three-act Integration Protocol and its beat labels, the genre blend, the sensory lexicon.

**One reader**: every page above and the two records.

**Chapter readings**: none — the document names no chapter.
