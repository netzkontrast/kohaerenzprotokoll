# Brief — readings from document 336 (step 6)

1 document, one reader, one batch: `ingest-337`. Files go to `Plan/runs/ingest-337/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 336 | `aegis-logik-in-der-leere-docx` | 2025-08-05 | „the Aegis-Logik-in-der-Leere report“ (an unsigned German analytic report, docx export, answering a „Benutzeranfrage“) | from premises about Aegis (Potentialraum, Restmuster, the negative self-definition) derives three origin scenarios, six subsystems (CLIK, BMS, IDAU, SPE, ICIM, RMS) and three models, leaving the choice of model to the reader; a different text from the Logiksystem-Aegis analysis on the same premises; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (286 lines for `aegis-logik-in-der-leere-docx`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analytic report on a request's premises: write „the Aegis-Logik-in-der-Leere report derives / proposes …“; say when it restates the request's premise and when it analyses. Keep the spelling `Aegis`. Its models and subsystems are proposals; it chooses none. Never merge it with the Logiksystem-Aegis analysis already on the pages.

## Pages — document 336, `aegis-logik-in-der-leere-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `Aegis` L11, L13, L15, L21, L25, L27, … (58 lines). central (3–6): Aegis likely inheriting no perfect blueprint from the Restmuster (L27), not designed (L37); the self-definition as key, recursive and negative (L43, L47), autopoietic (L49); unable to prove its own consistency internally (L105); a system of finite capabilities, not an omnipotent logical entity (L175); the three models — the paradox engine's core (L197), the dominant SPE (L206), a flexible membrane (L212); deeply alien in Model 1 (L200).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L37, L39, L81, L188, L225, L241, … (7 lines). minor (1–3): Aegis not designed but emerged, pointing to self-organisation and emergence from complexity (L37); Scenario B, emergence after Wolfram's computational universe (L81) — the report's own derivation.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L21. not read: an occurrence (see below).
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L154. not read: an occurrence (see below).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L216. not read: an occurrence (see below).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L115. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `logische Entropie` (near `entropie`). occurrence: the report's own subsystem names and derivations (`Inkohärenz-Detektions- & Analyseeinheit`, `Simulations- & Prädiktions-Engine`, `Umleitung von Inkohärenz`, `logische Entropie`) and the borrowed `Landauer` principle — not the pages' terms.
- `kohaerenz`: `Inkohärenz` (near `koharenz`), `Inkohärenz-Detektions- & Analyseeinheit` (near `koharenz`), `Umleitung von Inkohärenz` (near `koharenz`). occurrence: the report's own subsystem names and derivations (`Inkohärenz-Detektions- & Analyseeinheit`, `Simulations- & Prädiktions-Engine`, `Umleitung von Inkohärenz`, `logische Entropie`) and the borrowed `Landauer` principle — not the pages' terms.
- `landauer-signatur`: `Landauer` (near `landauersignatur`). occurrence: the report's own subsystem names and derivations (`Inkohärenz-Detektions- & Analyseeinheit`, `Simulations- & Prädiktions-Engine`, `Umleitung von Inkohärenz`, `logische Entropie`) and the borrowed `Landauer` principle — not the pages' terms.
- `ueberwelt`: `Simulations- & Prädiktions-Engine` (near `simulation`). occurrence: the report's own subsystem names and derivations (`Inkohärenz-Detektions- & Analyseeinheit`, `Simulations- & Prädiktions-Engine`, `Umleitung von Inkohärenz`, `logische Entropie`) and the borrowed `Landauer` principle — not the pages' terms.


**Pages not read:** `entropie` (L21 logical entropy, an analogy), `grosse-mauer` (L154 a generic system boundary, not the Große Mauer of KW3), `kohaerenz` (L216 a heading on logical coherence), `ueberwelt` (L115 Aegis's simulations) — occurrences.

**Record entries:** none.

**Not promoted:** Potentialraum, Restmuster, Primärdirektive, Selbstdefinition, the scenarios A–C, the subsystems CLIK, BMS, IDAU, SPE, ICIM, RMS, the three models; the borrowed concepts (autopoiesis, Ruliad, Wolfram, Maxwell's demon, Landauer, halting problem, Tegmark).

**One reader**: aegis, emergenz.

**Chapter readings**: none — the report names no chapter of the novel.
