# Brief — readings from document 427 (step 6)

1 document, one reader, one batch: `ingest-428`. Files go to `Plan/runs/ingest-428/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 427 | `holographisches-prinzip-fuer-kohaerenz-protokoll` | 2025-04-26 | „the holography report“ (an unsigned German research report on a holographic principle for the novel, which it calls KP) | weighs the principle as metaphor, worldbuilding device, plot mechanism and theme against AEGIS, the Potentialmeer, the simulation, M and the K-J connection, and recommends integrating it (L297); proposals, no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (383 lines for `holographisches-prinzip-fuer-k`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report that proposes: write „the holography report proposes …“; its physics sections (L19–L71) report cited sources, so nothing there is about the novel; what it says of the novel is conditional („könnte“) and it says itself its explanations stay speculative (L223). Quote the German as written; cut before straight quotes, bold and italics markers and glued footnote digits. No gendered pronoun for AEGIS — use the name (quotations stay verbatim). Physics terms carrying a real person's name (the information bound and others, L108, L122) are never written nor quoted — describe them („a bound on information density“).

## Pages — document 427, `holographisches-prinzip-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L16, L38, L93, L103, L122, L132, … (21 lines). minor (1–4): AEGIS as „Leser und Interpreten dieser grenzflächenkodierten Information“ (L93); whether AEGIS builds on the principle by design is asked and answered with possibilities (L103); a hard, physically motivated limit on AEGIS's omnipotence (L122) — describe the bound, never name it; even a god-like AI like AEGIS could be subject to these limits (L134).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L145. not read: an occurrence — emergence in the summary table's physics sense (L145).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L26. not read: an occurrence — entropy in the physics section, a cited source's sense (L26).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L114, L150. minor (1–4): the Kernwelten „könnten als unterschiedliche holographische Projektionen verstanden werden“ from the same M-based substrate (L114); the table: „Verschiedene Projektionen desselben Hologramms“, travel between worlds as a change of projection, asked as a question (L150).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L16, L59, L93, L94, L103, L104, … (20 lines). minor (1–4): the Potentialmeer as „chaotische, informationsbasierte Potentialmeer als Außenwelt“ and „die kritische Grenze zwischen Simulation und Potentialmeer“ (L16); a possible conflict if M were to describe the Potentialmeer, resolved by letting M describe only the inside (L169).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L16, L104, L110, L146, L147, L193, … (11 lines). minor (1–4): three proposed explanations of the Risse at the boundary between simulation and Potentialmeer (L104): an information overflow at the boundary (L108 — describe the bound), projection errors „bei der holographischen Projektion der Grenzinformation in den Bulk der Simulation“ (L109), and granularity of spacetime (L110); the report calls them speculative (L223, L229).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L16, L26, L59, L71, L93, L94, … (43 lines). minor (1–4): the simulation(s) AEGIS maintains as „Schutzbarriere“ (L16); the summary table: the simulation as hologram/projection, a bulk reality emerging from boundary information (M) (L145).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `archiv-der-grenzen`: `Grenze` (near `archivdergrenzen`). an occurrence: `Grenze` is the holographic boundary, not the Archiv der Grenzen nor the Große Mauer.
- `entropie`: `Verschränkungsentropie` (near `entropie`). an occurrence: entanglement entropy, a borrowed physics concept.
- `grosse-mauer`: `Grenze` (near `groemauersystemgrenze`), `Grenze` (near `systemgrenze`). an occurrence: `Grenze` is the holographic boundary, not the Archiv der Grenzen nor the Große Mauer.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–3): „Die nicht-lokale K-J Verbindung (Moonshine-Signatur) lässt sich metaphorisch mit Korrelationen auf einer holographischen Grenze verknüpfen“ (L95); the principle could supply a pseudo-scientific mechanism for the K-J connection (L123), conditional on whether the project already has one (L171).

**Record entries:** none.

**Pages not read:** emergenz, entropie, kohaerenz — occurrences.

**Not promoted:** Holographisches Prinzip, HP, Boundary and Bulk, Boundary-Beschreiber, M als Boundary-Theorie, AdS/CFT, Raumzeit-Granularität/Pixelierung, Holometer-Experiment, Wächter-KI, Schutzbarriere, NZT-Ideal, VOA, and the borrowed physics concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
