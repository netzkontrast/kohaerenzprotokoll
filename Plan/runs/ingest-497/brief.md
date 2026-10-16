# Brief — readings from document 497 (step 6)

1 document, one reader, one batch: `ingest-497`. Files go to `Plan/runs/ingest-497/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 497 | `plot-exploration-kohaerenz-protokollkonzepte` | 2025-04-23 | „the plot-exploration report“ (an unsigned German report) | five plot concepts in one four-field template, a scored comparison, and a recommendation of concept 2 for further outlining; it restates the world as premises tagged „[Query-II]“ and calls them the project's established core concepts (L17), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (237 lines for `plot-exploration-kohaerenz-pro`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An exploration: write „the plot-exploration report proposes …“ (for a concept) or „restates …“ (for a [Query-II] premise); a concept's plot is one option among five, never canon. „DIS“ is Kael's condition in the novel. One concept title and several lines carry a person's name (L51, L67, L69, L91, L205, L218, L232) — never quote a span containing a person's name or a concept named after one. Quote verbatim; cut before bold, escaped brackets and inner quotes. No gendered pronoun for Kael, Juna, AEGIS in our own prose.

## Pages — document 497, `plot-exploration-kohaerenz-protokollkonzepte`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L24, L27, L31, L39, L44, … (42 lines). central (4–8): the restated premise: AEGIS seeks coherence through logic, control and demarcation (autopoiesis) (L23); AEGIS perceives the Kael-Juna connection as a threat (L24); its control attempts paradoxically produce instability, the Risse (L27); a fundamental paradox: designed for stability, it produces systemic instability (L39); concept 2 sets AEGIS's system at the centre, asking whether it can integrate a phenomenon like the K-J connection (L70).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L49. minor (1–4): research on the origin and function of alter identities (L49).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L49. minor (1–4): research on dissociative identity disorder, the origin and function of alter identities, for a respectful portrayal (L49).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L153, L169, L193, L205. minor (1–4): emergence as a research domain (L153); concept 5's Insel as a field or attractor rather than a place (L169); concept 5 as the most speculative approach, with research in emergence (L193).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Das Gödel-Gambit` L67, L69, L218, L232. not read: the page's term carries a person's name; under the project's privacy rule no reading is written onto it from this document.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L70, L121, L127, L128, L129, L130, … (10 lines). central (4–8): concept 4 shifts the focus to one or more Guardians, specialised agents or subsystems of AEGIS (L121); its question: what happens when a loyal servant of the system, a Guardian, doubts through what it observes (L122).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L24, L44, L69, L70, L87, L91, … (19 lines). minor (1–4): the K-J connection characterised by resonance and transcendence, perceived by AEGIS as a threat (L24); Juna as emotional anchor and catalyst in concept 1 (L44 — check); concept 3: the K-J connection possibly the next step in the evolution of coherence (L117); Kael and Juna stay central figures (L230).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L24, L26, L27, L31, L39, … (38 lines). central (4–8): Kael whose nature (DIS) aims at integration (L23); the Kernwelten as the places where Kael's psyche manifests (L26); concept 1's question whether Kael can heal the fragmented psyche before AEGIS's interventions harm Kael irreparably (L44); concept 5's Kael from the Insel (L148, L169 — check the lines).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L26, L43, L44, L49, L51, L52, … (13 lines). minor (1–4): the Kernwelten as the places where Kael's psyche manifests, labelled KW1-Logik, KW2-Emotion/Trauma, KW3-Abwehr, KW4-Potential (L26).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`personas`** (minor, 1–4): the census's surfaces — `Persona` L51. not read: an occurrence — `Persona` is a borrowed archetype on a line naming a psychologist (L51).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L25, L104, L147, L153, L156, L169, … (7 lines). minor (1–4): the ontological dichotomy between the Potentialmeer (chaos, potential) and the Kohärenz-Insel (L25); concept 5: the Insel as a field or attractor within the Potentialmeer (L169).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L27, L39, L70, L91, L226. minor (1–4): AEGIS's control attempts paradoxically produce instability, the Risse (L27); the escalation of system errors, the Risse, as a source of suspense in the recommended concept (L226).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names a Guardian, not the subfunction.
- `kohaerenz`: `Kohärenz-Insel` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). an occurrence: `Kohärenz-Insel` read on potentialmeer; `Kohärenz Protokoll` the title.
- `verschraenkungs-insel`: `Verschränkung` (near `verschrankungsinsel`). an occurrence: `Verschränkung` in the general physics sense.


**Record entries:** none.

**No chapter readings**: the report names no chapter (`Kap` 0, `Kapitel` 0).

**Not promoted:** the five concept titles, Kael-Juna-Verbindung as a surface, Kohärenz-Insel, the KW labels, the Query tags, Quantenschaum, and the borrowed concepts (several carry a person's name).

**One reader**: every page above.
