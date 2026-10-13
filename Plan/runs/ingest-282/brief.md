# Brief — readings from document 281 (step 6)

1 document, one reader, one batch: `ingest-282`. Files go to `Plan/runs/ingest-282/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 281 | `a-guide-to-the-society-of-self-understanding-system-kael` | 2025-10-15 | „the society guide“ (an unsigned English guide) | an explanatory guide to System Kael's eleven alters in three groups — four Daily Life Managers (ANPs), five Trauma Holders (EPs), two System Guides — each with role, core motivation, core fear and a scene where it acts, ending on the Rhizomatic Self; it calls itself „a compassionate tool“ (L15) and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (142 lines for `a-guide-to-the-society-of-self`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide: write „the society guide describes / places …“; its scene numbers are mangled by the export (`Scene 1.2` → `Scene.2`), so name scenes by title in backticks. Each alter's opening sentence is the reading; one or two quotations per alter.

## Pages — document 281, `a-guide-to-the-society-of-self-understanding-system-kael`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L39, L105, L113, L123. minor (1–3): AEGIS's intrusions and its most brutal attack that brings Moros forth (L113); the gaslighting attempt Argus identifies (L127).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L53, L55, L59. minor (1–3): „Alex is the system's pragmatic crisis manager.“ (L55); his conflict with Nyx (L59).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L15, L35, L63, L65, L73, L81, … (9 lines). minor (1–3): the personalities as alters coexisting in Kael's mind, an internal society (L15); not symptoms to be cured but survivors to be integrated (L17).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L121, L123, L127. minor (1–3): „Argus functions as a detached, meta-cognitive critic.“ (L123); identifying the therapeutic language as gaslighting (L127).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L99, L101. minor (1–3): „Isabelle holds a particularly difficult trauma response“ (L101).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L97. minor (1–3): Lia's emergence triggered by the hopeful connection to Juna/V (L97).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L17, L23, L31, L35, … (12 lines). central (3–6): System Kael as an internal society (L15); the goal functional multiplicity (L17); „As the Host, Kael is the alter who spends the most time interacting with the external world.“ (L39); his fear of being overwhelmed (L42); the Rhizomatic Self (L141).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L67, L81, L83, L85. minor (1–3): „Kiko is a young child alter“ (L85); Rhys's realisation in `The Child in the Maze` (L67).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L45, L47, L51. minor (1–3): „Lex is the system's rational analyst“ (L47).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L81, L91, L93. minor (1–3): „Lia is another child alter“ (L93); her emergence through Juna/V (L97).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L107, L109, L139. minor (1–3): „Moros represents the system's most profound trauma response“ (L109); his emergence in Chapter 24 after AEGIS's most brutal attack (L113).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L59, L75, L77, L89, L113. minor (1–3): „Nyx is the system's aggressive protector“ (L77).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L61, L63, L89, L113. minor (1–3): „Rhys is the system's internal caregiver“ (L63); fighting Kiko's fears only makes them stronger (L67).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L129, L131. minor (1–3): an Internal Self Helper sharing qualities of ANPs and EPs (L131); introducing a collective in the first internal council (L135).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L23. minor (1–3): the story „rigorously modeled on a clinical framework called“ TSDP (L23); the ANP/EP table (L25–L29).

- **`multiplizitaet`** (minor, 1): „functional multiplicity“, harmonious collaboration where every alter is heard (L17).
- **`guardians`** (minor, 1): „the Guardian's paradoxical question“ in `The Coherence Check` (L51).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the questioner in `The Coherence Check` (L51), not the Integrity Guardian.
- `guardians`: `Guardian` (near `guardians`). reading: „the Guardian's paradoxical question“ to Lex in `The Coherence Check` (L51).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's name, read on tsdp.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven alters — four ANPs (Kael, Lex, Alex, Rhys), five EPs (Nyx, Kiko, Lia, Isabelle, Moros), two System Guides (Argus, Selene) (L33–L131).

**Not promoted:** the Rhizomatic Self, Daily Life Managers, Trauma Holders and System Guides as labels, the scene titles, Dr. Thorne.

**One reader**: every page above and the record.

**Chapter readings**: Kap 24 — written by the session (Moros's emergence, L113).
