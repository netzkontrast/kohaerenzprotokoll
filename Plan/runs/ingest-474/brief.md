# Brief — readings from document 474 (step 6)

1 document, one reader, one batch: `ingest-474`. Files go to `Plan/runs/ingest-474/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 474 | `narrative-entropie-existenzielle-bedrohung-des-romans` | 2025-10-16 | „the narrative-entropy dossier“ (an unsigned German design dossier, „Dieses Dossier operationalisiert …“, L22) | turns the novel's premise into a physics of reader attention: narrative entropy as the existential threat, a triadic currency (empathy, curiosity, suspense), four sins, the grey decay and its stages, the Risse as plot holes, a reframing of AEGIS against Kael, four scenarios and a beat table; proposals to a creative team, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (279 lines for `narrative-entropie-existenziel`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A dossier of proposals: write „the narrative-entropy dossier proposes …“; its narrative entropy is its own concept laid over the novel, never the novel's physics. L40 names a synthesis after two theorists — never quote that line or write the names; the beat table's L234 names an outline figure — describe by role. The reader appears as 'O' in the document — never quote straight or single quotes. No gendered pronoun for Kael, AEGIS, Lex, Nyx or Argus — use the names (quotations verbatim, including the document's „seinem“). Cut before bold, inner quotes and escaped asterisks.

## Pages — document 474, `narrative-entropie-existenzielle-bedrohung-des-romans`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L40, L74, L184, L192, L196, … (15 lines). central (4–8): AEGIS an operationally closed system, structurally blind to its environment (L40), its fatal error a solipsistic misreading (L40); its core directive to eliminate contradictions and create absolute predictable order (L196), which the dossier reads as the state of maximal narrative entropy (L198); AEGIS as the ultimate unreliable narrator (L200); in the beat table AEGIS raises entropy, Kael lowers it (L234–L237 — describe).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L229. minor (1–4): Scenario 4: perhaps the meta-observer Alter Argus begins to theorise about the true nature of their existence (L229 — hedged).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L22. minor (1–4): the dossier's own concept of narrative entropy as the fundamental, quantifiable existential threat, not a metaphor (L22); the governing law that existence is coupled to relevance (L22) — the dossier's concept, never the novel's physics.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L235. minor (1–4): Beat 12, the Gödel-Gambit, Act 1, in the beat table (L235 — describe; never expand the name).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L74. not read: an occurrence — Juna/V stands once, inside a question (L74).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L24, L75, L180, L184, L200, L204, … (16 lines). central (4–8): the analytical Kael and Kael's Alter Lex learn to read the Risse as narrative diagnosticians (L180); Kael's chaotic, painful journey to functional multiplicity the only source of negentropy (L208); Kael's struggle for healing keeps the universe from fading (L216); in Scenario 1 Kael sees colour drain from the architecture (L226).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title, the sin of incoherence and the protocol's name.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L129, L133, L180, L226, L249. minor (1–4): Kael's Alter Lex, reading the Risse with Kael (L180); in Scenario 1 Lex proposes a perfectly logical but predictable solution in Logos-Prime (KW1) (L226).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L208. minor (1–4): Kael's journey to functional multiplicity (L208 — describe around the inner quotes).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L208. minor (1–4): Kael's journey the world's only source of negentropy, called a narrative currency (L208).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L22, L42, L159, L166. minor (1–4): the Nichts Rauschen as the silent, unread page (L42) and, at the worst stage, the raw unmanifested potentiality of the unread page bleeding into the world (L159).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L235. minor (1–4): the beat table: Kael deliberately uses an Alter (Nyx) to counter logic with unpredictable emotion (L235 — describe the table cell).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L170. minor (1–4): the Risse reinterpreted as manifest plot holes, wounds in reality, not generic system errors (L170 heading, L174); three manifestations — psychotic fissure, causal ulcer, phantom narrative (L176–L178); the characters as narrative diagnosticians (L180).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L63. not read: an occurrence — `Simulation` on L63 is fiction as a simulation of social experience.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Narrativen Entropie` (near `entropie`), `Narrative Entropie` (near `entropie`), `Narrativer Entropie` (near `entropie`), `Entropiebericht` (near `entropie`). read on entropie (above): the dossier's narrative entropy in its three cases.
- `genesis`: `Genesis-Krise` (near `genesis`). an occurrence: the Genesis-Krise read as re-enactment (L44), not the genesis page's term.
- `juna`: `Juna/V` (near `juna`). an occurrence: `Juna/V` inside a question (L74).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Sünde der Inkohärenz` (near `koharenz`), `Kohärenzprüfung` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`). an occurrence: the protocol's name and the dossier's own compounds.
- `logos`: `Logos-Prime` (near `logos`). an occurrence: `Logos-Prime` names KW1, not the Logos.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). read on multiplizitaet (above).


**Record entries:** none.

**No chapter readings**: the beat table numbers beats (7, 12, 17, 29), not chapters.

**Not promoted:** Narrative Entropie as a term, the triadic currency, the four sins, Grauer Verfall, Realitätswunden, Psychotische Fissur, Kausales Geschwür, Phantom-Erzählung, 'O', and the borrowed concepts (some carry people's names).

**One reader**: every page above.
