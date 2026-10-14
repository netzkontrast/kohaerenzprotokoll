# Brief — readings from document 514 (step 6)

1 document, one reader, one batch: `ingest-514`. Files go to `Plan/runs/ingest-514/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 514 | `kohaerenz-protokoll-narrative-architekturanalyse` | 2025-07-29 | „the narrative architecture analysis“ (an unsigned German strategy text) | five parts proposing how to narrate AEGIS, the Kael system, Juna/V, Das Fundament and the reader, borrowing concepts from information theory, chaos theory and cache coherence; proposals in the modal mood, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (340 lines for `kohaerenz-protokoll-narrative-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A strategy text: write „the narrative architecture analysis proposes …“. Its parts Lex, Kiko and Rhys appear as style examples. Many lines name real thinkers, authors or scientists (e.g. L34, L96, L110, L114): never write a name, never quote a span containing one or a possessive formed from one; cut before. No gendered pronoun for Kael, Juna, AEGIS or the parts in our own prose; quotations stay verbatim (the document writes „Er“, „Ihre“).

## Pages — document 514, `kohaerenz-protokoll-narrative-architekturanalyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L18, L22, L30, L34, L36, L42, … (28 lines). central (4–8): narrating the inner experience of a non-human intelligence in logical and existential collapse, beyond the archetype of the murderous AI (L22); control attempts creating a positive feedback loop that raises instability (L42); MAD as the central metaphor of AEGIS's self-destruction, training on its own filtered outputs (L46); a tragic figure „nicht weil es böse ist“, its tragic flaw its own core programming (L72); perversely instantiating „Kohärenz zu erreichen“ as total elimination of the unpredictable (L76); its arc ending in self-recognition, Anagnorisis (L213).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L34, L76. minor (1–4): AEGIS's detection of the Leere/anomaly as a signal of maximal entropy (L34 — cut before the scientist's name); L76 as the census lists it.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L62. minor (1–4): the table's deadlock: two subsystems, e.g. Guardians, requesting resources to control Kael, freezing a region of a Kernwelt (L62).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L80, L133, L137, L145, L147, L155, … (11 lines). central (4–8): Juna/V not entering a Kernwelt physically but manifesting as a reality overlap, e.g. a scent in Logos-Prime (L147); Kael's perception becoming synaesthetic when Juna/V's influence is strong (L157); „*Anwesenheit* ist das Argument“ (L169); in the final sections AEGIS's clinical language merging with the resonant language of Juna/V (L205).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L38, L54, L58, L59, L60, L61, … (35 lines). central (4–8): „funktionale Multiplizität“ not shown as a pathology to be cured by fusion (L88); the co-presence of parts in Kael's deep POV performed by the prose itself (L96 — cut before the names); the Kernwelten as symbolic landscapes that represent and shape Kael's states (L110 — name-free span), Kael's literal environment (L112); synaesthetic perception under Juna/V's influence (L157).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L54, L61, L106, L110; `Kernwelt` L54, L61, L62, L106, L110, L147. minor (1–4): the four Kernwelten as symbolic landscapes and Kael's literal environment (L110, L112 — name-free spans); a Kernwelt freezing in a deadlock (L62).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L99, L102. minor (1–4): Kiko (fear): prose becomes fragmented and staccato, focus narrowed to threats (L99).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L13, L22, L42, L46, L76, L129, … (12 lines). central (4–8): AEGIS's goal „Kohärenz zu erreichen“, perversely read as eliminating the unpredictable (L76); rigid coherence raising instability (L42); „Cache Coherence“ as the central metaphor for Kael's parts, each part's cache synchronised with main memory (L129).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L98, L102. minor (1–4): Lex (logical analysis): prose becomes analytical, with long complex sentences (L98).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L88, L204. minor (1–4): „funktionale Multiplizität“ as the goal, not a pathology cured by fusion (L88); L204 as the census lists it.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L244. not read: an occurrence — the meta-narrator as a „Persona“ within the narrative system (L244), not the page's personas.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L100, L102. minor (1–4): Rhys (protector): syntax declarative and direct, focus on action and control (L100).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L46, L50, L54, L64. minor (1–4): the Risse not random but direct causal consequences of AEGIS's actions, tied to specific failures of its control algorithms (L54); the table of algorithm failures and their Risse (L56–L64).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). recorded on Q5 (below): `Cerberus-Labyrinth` names a Kernwelt.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: `Resonanz` in the general sense.
- `kairos`: `Kairos-Potentialis` (near `kairos`). recorded on Q5 (below): `Kairos-Potentialis` names a Kernwelt.
- `logos`: `Logos-Prime` (near `logos`). recorded on Q5 (below): `Logos-Prime` names a Kernwelt.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). recorded on Q5 (below): `Mnemosyne-Archipel` names a Kernwelt.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). an occurrence: `Resonanz` in the general sense.


**Record entries** (one file, formatted as earlier entries):
- **`q5-guardians-and-kern-welten`**: the narrative architecture analysis names four Kernwelten — Logos-Prime (rationality/host), Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis (L114–L117 — quote the names and their parenthetical labels only, cut before any person's name); recorded, not applied.

**No chapter readings**: `Kap` 0; `Kapitel` once as a hypothetical example (L234).

**Not promoted:** MAD, Cache Coherence as a surface, the four world names as surfaces, Meta-Erzähler, Anagnorisis, Gnosis, Realitätsüberlappung, and the borrowed concepts (several named after people).

**One reader**: every page above and the Q5 entry.
