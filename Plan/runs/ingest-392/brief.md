# Brief — readings from document 391 (step 6)

1 document, one reader, one batch: `ingest-392`. Files go to `Plan/runs/ingest-392/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 391 | `dramatica-storyform-validierung-und-synthese` | 2026-01-02 | „the validation report“ (an unsigned German Dramatica validation, 2026-01-02) | checks two storyform documents (Dokument A, valid; Dokument B, invalid) against Dramatica's rules and synthesises `Kohärenz-Prime` — A's domains with B's themes — with Kernwelten tied to domains and four research questions; it calls the result a „mathematisch präzise und thematisch resonante Basis“ — recorded, not applied; it predates decision 025 |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (401 lines for `dramatica-storyform-validierun`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A validation and synthesis: write „the validation report judges / proposes …“; what it says of Dokument A and B is its description of them, and its synthesis is a proposal — decision 025's storyforms stand. Quote the German as written; cut before glued footnote digits, escapes, table pipes and nested quotes. No gendered pronoun for Kael or Juna/V — use the names (quotations stay verbatim).

## Pages — document 391, `dramatica-storyform-validierung-und-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L52, L56, L58, L80, L97, … (17 lines). central (3–5): the synthesis defining AEGIS as a pathological way of thinking rather than a false universe (L169); AEGIS compulsively committed to its protocols, lacking responsibility for the emergent alters it deletes (L185); the Problem Order: „AEGIS scheitert nicht, weil es die Kontrolle verliert“ (L304).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L112, L185. minor (1–3): the Alters' egoism blocking intimacy in Dokument A's RS problem (L112); the emergent life forms (Alters) AEGIS deletes as errors (L185).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L201. not read: an occurrence (see below).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L56, L65, L87, L110, L128, L243, … (11 lines). central (3–5): Dokument A's IC: Juna existing outside the simulation, a situation challenging Kael (L65); the synthesis taking Juna out of the Psychology domain as an outsider, „ein Glitch, der nicht gelöscht werden kann“ (L249); in the final table Juna/V in Universe, „Der Glitch. Existenz außerhalb des Systems.“ (L374).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L52, L56, L58, L64, L65, L86, … (34 lines). minor (1–3): Kael stuck in the trauma reaction (L209); Dokument B's Kael as a „lebender Gödel-Satz“, which the report calls „eine brillante Metapher“ (L136); in the synthesis Kael must inject chaos into the core (L201).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L17, L78, L152, L305. minor (1–3): the synthesis tying each Kernwelt to a domain: Logos-Prime no longer only a situation, Mnemosyne-Archipel the manifestation of Mind, Kairos-Potentialis the world of Universe possibilities, Cerberus-Labyrinth the arena of Physics (L309–L312).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L66, L88, L267, L377. minor (1–3): the RS as the Moonshine-Link in Physics, the relationship as „physikalische Arbeit“ against the system's resistance (L66); in the synthesis „Die Beziehung ist Arbeit.“ (L273) and „Der Moonshine-Link. Arbeit am Widerstand.“ (L377).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L225. minor (1–3): the conflict of the lie of singularity against „der Wahrheit der Multiplizität („Wir sind viele“)“ — quote around the nested marks (L225).
- **`risse`** (minor, 1–4): the census's surfaces — `Der Glitch` L374. not read: an occurrence (see below).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L209. minor (1–3): Kael's trauma reaction tied to TSDP (L209).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L65. minor (1–3): Juna existing outside the „Simulation“ (L65).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.
- `kairos`: `Kairos-Potentialis` (near `kairos`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Prime` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.
- `logos`: `Logos-Prime` (near `logos`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.
- `truth-rotation`: `Truth` (near `truthrotation`). `Der Glitch` (L374) is Juna/V's label in the table, read on juna, not the Risse; the Kernwelt names read on kern-welten, worlds not Guardians; `lebender Gödel-Satz` on goedel-gambit; `Kohärenz Protokoll` the title and `Kohärenz-Prime` the report's synthesis; `Truth`, `Story Mind`, `Unproven` Dramatica terms; `Kohärenztheorie der Wahrheit` a borrowed concept.


**Pages beyond the draft:**
- `goedel-gambit` (minor, 1): Dokument B's „lebender Gödel-Satz“, called „eine brillante Metapher“ (L136); the living Gödel-Satz as pure logic destruction, chaos for the system (L201).

**Pages not read:** `kohaerenz` (L11, the title), `entropie` (L201, unpredictable humanity in the general sense), `risse` (the table's glitch is Juna/V) — occurrences.

**Record entries:** none. The report's synthesis keeps the domain assignment of its Dokument A (which agrees with storyform A of decision 025) and rejects Dokument B's (that of ingest 390); recorded in the reconciliation record.

**Not promoted:** Kohärenz-Prime, Validitätsprüfung, Dokument A and B as labels, the research questions, the Weaving table, every Dramatica value; the borrowed concepts.

**One reader**: kael, aegis, juna, moonshine-link, kern-welten, alters, tsdp, goedel-gambit, multiplizitaet, ueberwelt.

**Chapter readings**: none — the report names no chapters.
