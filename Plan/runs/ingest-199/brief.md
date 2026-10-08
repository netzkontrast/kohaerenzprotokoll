# Brief — readings from document 199 (step 6)

1 document, one reader, one batch: `ingest-199`. Files go to `Plan/runs/ingest-199/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 199 | `narrative-architektur-fuer-kohaerenz-protokoll` | 2025-07-29 | „the craft handbook“ (titled `Die unterrepräsentierten Architekturen des „Kohärenz Protokolls“: Ein Handbuch zur narrativen Vertiefung`) | a German report in seven parts, each a theory section (Levinas, Popper, Aarseth, Fish, second-order cybernetics, Kishōtenketsu, Daoism and Śūnyatā) and a `Narrative Anleitung` of recommendations for writing the novel — typography, prose style per figure, a meta-level, pastiche per Kernwelt, an unreliable meta-narrator, Kael's healing arc as Kishōtenketsu; it cites the project only through its footnote 1 and makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (636 lines for `narrative-architektur-fuer-koh`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A handbook that recommends how to write: write „the craft handbook recommends / reads …“; what it says of the world it takes from footnote 1 (the existing project) — it adds ways of writing, not facts; its questions are questions. German — quote as written; cut before glued reference digits and before inner straight quotes (many terms stand in them); KW digits drop in `--find`.

## Pages — document 199, `narrative-architektur-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L43, L59, L67, L69, L77, L93, … (35 lines). central (2–4): AEGIS's action as „die systematische Perversion der Ethik nach Emmanuel Levinas“ (L59); its post-transformation prose, grammatically perfect but paradoxical (L243) — cut before the inner quotes; AEGIS as a possible author of unreliable footnotes (L393).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L111, L243. minor (1–2): how the prose in the AEGIS chapters could show its algorithmic melancholy — a question (L111); cut around the inner quotes.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L22. occurrence: the general word in the report's aim (L22).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L319, L574. minor (1–2): „Das“ Gödel-Gambit on the meta-level (L319) — read the section's first line; quote around the inner quotes.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L313, L332, L471. minor (1–2): reports of the Guardians as sub-systems with different voices (L313); two Guardians giving contradictory reports — a question (L332).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L255. minor (1–2): the connection to Juna/V shown by synaesthetic language (L255) — cut before the inner quotes.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L43, L51, L59, L67, L93, L103, … (36 lines). central (2–4): the depiction of Kael's TSDP-based psyche needs the utmost sensitivity (L51); his Gärtner axiom of non-intervention against Popper's paradox of tolerance (L67) — cut around the inner quotes; his fragmented perception in mixed typefaces (L181); his integration as polyphonic, choral prose (L245).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L181, L368, L395, L562; `Kernwelt` L181, L234, L368, L395, L562. minor (1–2): each Kernwelt in a different genre style — pastiche (L395) — quote around the KW digits; their rules kept in a codex (L562).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L245. occurrence: Kiko named in the polyphonic-sentence example (L245), read on kael.
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L412, L445, L467, L603, L628, L629. minor (1–2): „Strukturierung von Kaels Heilungsbogen als Kishōtenketsu“ (L445); the four-act table (L465–L475).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the project's name in the title (L13).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L245. occurrence: Lex named in the polyphonic-sentence example (L245), read on kael.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L433, L461. minor (1–2): „Kael (Integration / Funktionale Multiplizität)“ as polyphonic prose (L245) — quote the plain words; Śūnyatā against the Monstergruppe (L461).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L254. minor (1–2): long, flowing sentences for awe and gnosis, for the Nichts Rauschen (L254) — cut before the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L245. occurrence: Nyx named in the polyphonic-sentence example (L245), read on kael.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L395. minor (1–2): KW2 „(Resonanz-Landschaft)“ written as surrealist prose (L395) — quote around the digit.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L162, L166. minor (1–2): the Risse described in the novel should also be shown visually, typographically (L166) — cut before the inner quotes and the digit.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L47, L51, L376, L520, L522. minor (1–2): „(Theorie der Strukturellen Dissoziation der Persönlichkeit)“ (L51); read L376 or L520 for TSDP in the method.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L393. occurrence: the simulated world AEGIS constructs (L368, L393) is the setting's general sense, nothing of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world's name (L395), on kern-welten.
- `juna`: `Juna/V` (near `juna`). a reading — on juna above (`Juna/V`, L255).
- `logos`: `Logos-Prime` (near `logos`). occurrence: Logos-Prime is KW1 (L395), J49 — on kern-welten.


**Record entries:** none — the handbook recommends ways of writing and decides no question of the world.

**Not promoted:** the theories and their authors, the typographic and stylistic devices, the meta-narrator, Novelcrafter's codex, the Gärtner-Axiom (on kael).

**Two readers**, disjoint: (1) kael, juna, multiplizitaet, tsdp, kishotenketsu, nichts-rauschen, goedel-gambit; (2) aegis, algorithmische-melancholie, guardians, kern-welten, resonanz-landschaft, risse.
