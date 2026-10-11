# Brief — readings from document 242 (step 6)

1 document, one reader, one batch: `ingest-242`. Files go to `Plan/runs/ingest-242/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 242 | `kapitelanreicherung-mit-fundamentalen-konzepten` | 2025-04-28 | „the concept analysis“ (an unsigned German report) | a report assigning one fundamental concept from trauma, dissociation and systems theory to each of the 39 chapters of a plot draft, in a table with a reason per chapter (L30–L72); a „praktischer Leitfaden“ for the writing, proposals, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (80 lines for `kapitelanreicherung-mit-fundam`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A thematic key: write „the concept analysis assigns / reads …“. Its chapters are a 39-chapter plot draft of its own, not the chapters as written. Several figures carry its own question mark (Nyx? L33, Moros? L36, Alex? L39, Kiko? L40, Täterintrojekte? L53): keep the question mark. Chapter readings are written by the session in `Plan/runs/ingest-242-kap/`; do not write chapter pages.

## Pages — document 242, `kapitelanreicherung-mit-fundamentalen-konzepten`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L30, L38, L44, L46, L47, … (17 lines). central (3–6): the systemic control the premise names (L17); Juna/V perceived by AEGIS as a system disturbance PP-SYS-01 (L38); AEGIS trying to keep control as homeostasis through new methods, producing feedback loops and tensions, Paradoxon X, PP-SYS-03 (L47); its control broken at the climax (L70).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L39, L46, L49, L57. minor (1–4): among the ANPs coordinating in everyday life (L46), with a question mark in the first cooperation (L39); among the core parts preparing for the confrontation (L57).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L56. minor (1–4): among the principles AEGIS rejects, the „Paraiyas“, that Kael begins to value (L56).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L38, L50. minor (1–4): the external connection Juna/V offering resonance and validation, a healing impulse from outside (L38); a stabilising resource in everyday life despite AEGIS's interference (L50).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L30, L32, L34, L39, L40, L46, … (14 lines). central (3–6): the ANP trying to function in AEGIS's world (L30); his decision to give up the Bunker's protection (L40); beginning to read the Risse as hints of deeper truths or the Fundament (L51); the cost of masking for System Kael (L52); Kael/Selene accompanying Kiko to the core trauma (L66).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L31, L40, L45, L61, L66. minor (1–4): an EP emerging from the betrayal (L31); the bearer of the core trauma whose call starts the confrontation (L61); accompanied protectively to the trauma memory (L66).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: `Kohärenz` alone at L11 is the novel's title; not read.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L32, L46, L57. minor (1–4): an ANP with Kael in the Bunker's compartmentalisation (L32); among the ANPs coordinating in everyday life (L46).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L36, L68. minor (1–4): „Moros' Auftreten?“, with its question mark, in the Bunker's stagnation (L36); becoming conscious of Moros in the acceptance of all parts (L68).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L46, L76. minor (1–4): „Funktionale Multiplizität / Ko-Bewusstsein“ as chapter 15's concept (L46); the acceptance of functional multiplicity as a possible goal instead of full fusion (L54).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L33, L45. minor (1–4): „Nyx?“, with its question mark, as a chaotic form of dissociative coping, rebellion against the Bunker (L33); triggered again by reality (L45).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L39, L46, L49, L57. minor (1–4): among the parts beginning to cooperate (L39) and coordinating in everyday life (L46); among the core parts preparing for the confrontation (L57).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L51. minor (1–4): Kael reading „Risse“ in AEGIS's control of reality not as errors but as hints of deeper truths or the Fundament (L51).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L49, L57, L63, L66, L70, L78. central (3–6): Selene as „das Selbst“, the inner mentor in chapter 30 „Licht der Wächterin“ (L63); Selene/ICH taking conscious leadership at the climax (L70); Kael/Selene as a pair (L49, L66).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the novel's title.
- `personas`: `Depersonalisation / Derealisation` (near `persona`). occurrence: Depersonalisation is a symptom, chapter 8's concept (L37); not the Personas.


**Record entries** (one file each):

- **`q4-waechter-four-bearers`**: chapter 30 titled „Licht der Wächterin“, in which Selene, „das Selbst“, steps forward as the inner mentor (L63) — the feminine `Wächterin` borne by Selene.

**Not promoted:** the 39 concepts, the three journeys (HJn, Zyklische Bewährung, HJ), the Bunker, Paraiyas, PP-SYS-01/03, Paradoxon X, Kerntrauma, Täterintrojekte.

**One reader**: aegis, kael, selene, juna, kiko, lex, nyx, moros, rhys, alex, multiplizitaet, risse, emergenz and the record q4. `kohaerenz` is an occurrence.

**Chapter readings**: Kap 1–39, one row each (L30–L72), by the session (`Plan/runs/ingest-242-kap/`).
