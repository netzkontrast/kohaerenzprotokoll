# Brief — readings from document 461 (step 6)

1 document, one reader, one batch: `ingest-461`. Files go to `Plan/runs/ingest-461/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 461 | `kohaerenz-protokoll-themenanalyse-und-anreicheru` | 2025-04-28 | „the theme enrichment report“ (an unsigned German report, „strategisches Forschungsdokument“, L15) | groups the novel's themes into clusters across three phases, applies borrowed theory lenses to Kael, AEGIS, Juna/V and the coded core worlds in five foci, and gives techniques; nearly every statement about the figures is a conditional suggestion („Könnte“), recorded, never applied; it calls itself a thematic toolbox (L283)|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (288 lines for `kohaerenz-protokoll-themenanal`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of suggestions: write „the theme enrichment report suggests …“ and keep its conditionals. Its theory blocks name people before each concept (L24, L33, L112, L121 and others) — never quote such a line, never write a name. World codes Co₁, McL, B, Ly may stand as codes, never expanded. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „Ihr“ and „Sein“). Cut before inner „…“, bold and italics.

## Pages — document 461, `kohaerenz-protokoll-themenanalyse-und-anreicheru`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L36, L42, L43, L54, L63, L87, … (57 lines). central (4–8): AEGIS's nature may be explored through systems theory (L63); the central paradox: the attempt at total order possibly produces chaos (L126), not a simple good-against-evil frame; open questions — does AEGIS understand its own role (L123), does it operate purely logically (L130); AEGIS as the anti-resonance pole (L201); its ethics open whether it has consciousness or malice (L228); the incompleteness theorems applied to AEGIS metaphorically or literally (L124 — describe without the name).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L32. minor (1–4): DID among the identity-and-psyche analogies of the self cluster (L32).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L31, L33, L53, L63, L69, L72, … (12 lines). central (4–8): emergence among the being-and-knowing cluster (L31) and control against emergence (L33 — name-free part only); Kael's journey embodies emergence and increasing complexity (L131); further mentions as the census lists them (L53, L63, L69, L72).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L125, L138, L144. minor (1–4): Co₁ represents a low-entropy system (L142), Ly high entropy and complexity (L144); entropy in the cluster on order (L125, L138).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L132, L234. minor (1–4): the Guardians could represent different facets of the system — rigid controllers, agents who question the logic, or ones showing emergent behaviour (L132); could represent different ethical stances in the system (L234).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L42. minor (1–4): Juna/V represents order and interaction — connection, resonance, non-locality — and possibly access to other levels of reality (L64); the connection to Juna/V a primary axis (L191), Juna/V embodies resonance (L200), a remedy to AEGIS's instrumentalism (L195); quantum non-locality as a strong metaphor for it (L193).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L36, L42, L44, L62, L82, L86, … (62 lines). central (4–8): Kael embodies mainly self and subjectivity (L62); Kael's arc from dissociation and misrecognition to struggle and integration (L93); the fragmentation to be shown in the vocabulary of structural dissociation and inner parts (L93); Kael could move from observed to observing system (L131); Kael's journey embodies emergence and growing complexity (L131).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L60, L65, L74, L86, L122, L123, … (13 lines). central (4–8): each world should embody specific thematic facets (L65); Co₁ extreme order and control (L69), anti-resonant (L211), forcing performativity (L272); McL could explore knowledge and truth (L70); B could embody the cyclic struggle (L71); Ly rich in contrast to Co₁ (L72), fluid adaptable spaces (L108); Co₁ low-entropy, Ly high entropy (L142, L144) — codes as written, never expanded.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L112, L274. minor (1–4): the Mosaik-Herz in the list of recurring symbols, mosaics as integrated fragments (L112 — a line with a name: describe only; L274).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L112. not read: an occurrence — `Persona` on L112 is a mask symbol, not the personas page's sense.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L121, L178, L211, L262. minor (1–4): whether AEGIS is an open system interacting with the Potentialmeer (L121 — a line with a name: describe only); in the mythic reading the sea stands for original chaos or potentiality (L262).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L64. not read: an occurrence — L64 says Juna/V possibly gives access to other levels of reality, a general sense.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L33, L43, L51, L122, L143, L148, … (8 lines). minor (1–4): Risse listed as a symbol of instability (L148); further mentions in the phases (L43, L51, L122, L143).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L31. not read: an occurrence — `Simulation` on L31 is a theme in the cluster list.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna.
- `kiko`: `KI-Kontrollproblem` (near `kiko`). an occurrence: `KI-Kontrollproblem` is the AI control problem, not Kiko.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). an occurrence: `Simulationshypothese` is the borrowed hypothesis.


**Record entries** (one file each, formatted as earlier entries):
- **`q3-how-many-kern-welten-and-alters`**: the theme enrichment report assigns themes to four coded core worlds, Co₁, McL, B and Ly (L69–L72); recorded.
- **`q1-guardians-and-aegis`**: the report suggests the Guardians could represent facets of the system or ethical stances within it (L132, L234); recorded.

**No chapter readings**: the report names no chapter.

**Not promoted:** the clusters and their names, the phase names, Narrative Manifestation, Environmental Storytelling, Gaslighting, Core Worlds, and the borrowed theories (several carry people's names).

**One reader**: every page above and the two record entries.
