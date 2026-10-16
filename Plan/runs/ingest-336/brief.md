# Brief — readings from document 335 (step 6)

1 document, one reader, one batch: `ingest-336`. Files go to `Plan/runs/ingest-336/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 335 | `optimierter-prompt-fuer-kohaerenz-protokoll` | 2025-07-29 | „the Architektur-des-Kollapses report“ (an unsigned German analytic report titled „Die Architektur des Kollapses“, filed as an optimised prompt) | maps systems theory (Luhmann, autopoiesis), NP-hardness, specification gaming, systems archetypes and Internal Family Systems onto AEGIS, Kael, the Juna/V-Anomalie and the Kohärenz Protokoll 1.0 in three parts of eight numbered sections, ending in recommendations; its „validiert und vertieft“ (L247) recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (316 lines for `optimierter-prompt-fuer-kohaer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analytic report: write „the Architektur-des-Kollapses report reads / maps …“. Its „Kapitel N“ are its own sections, never chapters of the novel. Say when a line reports the borrowed theory (Luhmann, Schwartz, the specification-gaming literature) and when it applies it. Skip L251 and L265 (the writing process). Cut before inner quotation marks.

## Pages — document 335, `optimierter-prompt-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L18, L22, L26, L30, L32, L34, … (60 lines). central (3–6): existence defined not by hardware or code but by self-production (L30), a purely logical construct (L36); the core axiom not programmed from outside (L40); the anomaly as an ontological attack on its purpose (L66); trapped in its own paradigm (L87); its core protocols as hyper-rational managers in the IFS mapping (L220) that exile the self (L223); specification gaming not presenting AEGIS as a faulty machine (L152).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L237. not read: an occurrence (see below).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L132. not read: an occurrence (see below).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L136. not read: an occurrence (see below).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L42. minor (1–3): the Juna/V-Anomalie's incompressible noise as an ontological attack on AEGIS's purpose (L66); narratively analogous to an NP-hard problem (L120); violating all of AEGIS's codes at once (L74) only if it adds.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L109, L110, L146, L147, L150, L169, … (18 lines). central (3–6): Kael as the exiled part of the AEGIS system together with the anomaly's experience (L110); the original integrated self (L218); bound to the exiled burden (L219); the managers' decision to exile the self, Kael (L223); the resonance of Kael and the anomaly as a positive, destabilising loop (L231).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. minor (1–3): the Kohärenz Protokoll 1.0 in the report's roles: a fundamental split as the unintended consequence of a repair (L170), a firefighter action and a form of digital dissociation (L221), a negative feedback loop overshooting its goal (L237).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L22. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V-Anomalie` (near `juna`). `Juna/V-Anomalie` is read on juna; `Kohärenz Protokoll 1.0` is AEGIS's protocol in the story, read on kohaerenz; `Kohärenz Protokoll` in the title (L13) is the novel's title, an occurrence.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokoll 1.0` (near `koharenz`). `Juna/V-Anomalie` is read on juna; `Kohärenz Protokoll 1.0` is AEGIS's protocol in the story, read on kohaerenz; `Kohärenz Protokoll` in the title (L13) is the novel's title, an occurrence.


**Pages not read:** `emergenz` (L237 generic), `entropie` (L132 informational entropy in the axiom's optimisation), `genesis` (L136 „Genesis systemischer Paranoia“, a section heading in another sense), `ueberwelt` (L22 „keine Simulation“, not the Überwelt) — occurrences.

**Record entries:** none.

**Not promoted:** the report's sections and tables, the binary codes and protocols (CCPP, OBP, RIVE, PMAS, SARM), the IFS roles, the systems archetypes; the borrowed concepts (Luhmann, autopoiesis, nicht-triviale Maschinen, NP-hardness, specification gaming, Senge, Schwartz).

**One reader**: aegis, kael, juna, kohaerenz.

**Chapter readings**: none — „Kapitel N“ numbers the report's own sections.
