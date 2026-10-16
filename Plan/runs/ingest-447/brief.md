# Brief — readings from document 446 (step 6)

1 document, one reader, one batch: `ingest-447`. Files go to `Plan/runs/ingest-447/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 446 | `konzept-expose-schwarzschild-protokoll-optimierung` | 2025-11-25 | „the event-horizon exposé“ (an unsigned German analytical report on a project it names after a physicist; call it only „the event-horizon exposé“) | a theory of truth as gravitation, a physics of the simulation, an attractor model (Logos, Eros, Abyssos, the reader 'O'), a character architecture, a genre synthesis and a governance proposal, paraphrasing ten cited research documents; a report (L24), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (448 lines for `konzept-expose-schwarzschild-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that proposes: write „the event-horizon exposé proposes …“; it paraphrases cited research documents (L409–L447), so its claims are its reading of them. Its project name and many lines carry real physicists' and thinkers' names (L22, L138, L209, L240, L280, L342): never write the project name nor any person's name, never quote a span containing one — describe around them. Elara Vance is a figure of a project it merges; name only where needed. Quote the German as written; cut before straight and single quotes, bold markers, escaped table markup and glued footnote digits. No gendered pronoun for Kael, Juna, AEGIS or Elara Vance — use the names (quotations stay verbatim).

## Pages — document 446, `konzept-expose-schwarzschild-protokoll-optimierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L44, L56, L113, L122, L126, L134, … (28 lines). central (4–8): the archive, run by the AI AEGIS, represents a coherence theory of truth in its purest, crystalline form (L44 — cut before the theory's name if needed); AEGIS as administrator of the simulation keeping entropy low in the Kernwelten (L138 — never quote the named demon); AEGIS cleans data to keep the simulation stable, the question where the entropy goes (L142); AEGIS shields the simulation against the Potentialmeer (L173); AEGIS uses Kael's fragmentation, the Kernwelten as conditioning chambers (L280 — describe, the line names a person).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L377. minor (1–4): the governance proposal allows „eine kontrollierte Emergenz“ — chaos (Abyssos) within rules (L377).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L138. minor (1–4): AEGIS keeps the entropy within the Kernwelten low (L138 — quote only the words after the named demon); where the entropy goes (L142); the Potentialmeer as realm of maximal entropy (L173).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L240, L276, L290, L389. minor (1–4): „Exilierte Anteile (Juna/V)“ carrying trauma, shame and forbidden truth, breaking through like the Risse (L276); Juna/V at the ontological level, domain „Universe“, a conflict of captivity and separation (L389).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L207, L233, L240, L241, L262, L270, … (18 lines). minor (1–4): the narrative as a wave function holding every course in superposition — „Kael entkommt“ among them (L207); the integration of Kael's personality as functional multiplicity (L241); AEGIS strengthens the separation of Kael's parts to keep Kael controllable (L280).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L138, L161, L173, L280, L342. minor (1–4): the Kernwelten as holographic projections (L161); entropy kept low within them (L138); designed by AEGIS as conditioning chambers (L280 — describe); the Potentialmeer beyond them (L173).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L22. not read: occurrences — the project's title line (L22) and the borrowed theory of truth; never quote them.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `Logos` L209, L213, L221, L225, L229, L254, … (12 lines). minor (1–4): section 4.3 „Das Dynamische System: Eros, Logos und Abyssos“ (L213) — the three attractors.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L241. minor (1–4): the integration of Kael's personality „(„Funktionale Multiplizität“)“ (L241 — quote around the nested quotes).
- **`negentropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Negentropie` alone on L142. minor (1–4): AEGIS cleans data to keep the simulation stable „(Negentropie)“, and the waste heat must go somewhere (L142).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L163, L169, L173, L178, L209, L245, … (7 lines). central (4–8): „Das Potentialmeer und die Dunkle Energie als Artefakt“ (L169); beyond the simulated Kernwelten the „Potentialmeer“ (or the Überwelt), the realm of chaos, infinite possibility and maximal entropy (L173 — quote around the nested quotes); the boundary to it as a possible projection surface (L163); dark energy as the price of computing new space, or the pressure of the Potentialmeer (L178).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L142, L173, L276. minor (1–4): exiled parts break through like „Rissen“ (L276); the Risse in the simulation (L142, L173).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L173. minor (1–4): the Potentialmeer „(oder die Überwelt)“ beyond the simulated Kernwelten (L173) — the exposé's wording, recorded, not decided.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `archiv-der-grenzen`: `Archiv` (near `archivdergrenzen`). an occurrence: `Archiv` is AEGIS's archive in the merged project, not the Archiv der Grenzen.
- `archiv-des-ungesagten`: `Archiv` (near `archivdesungesagten`). an occurrence: `Archiv` is AEGIS's archive, not the Archiv des Ungesagten.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: `Kaels` the genitive, not the dwelling.
- `kohaerenz`: `Schwerelosigkeit der Kohärenz` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrences: a borrowed theory and the report's coinage.


**Record entries** (one file, formatted as earlier entries — `ls Plan/runs/ingest-43*/readings/q6-*`):
- **`q6-nexus-ueberraum-ueberwelt`**: the event-horizon exposé writes the Potentialmeer „(oder die Überwelt)“ beyond the simulated Kernwelten (L173) — the Überwelt as the outer realm, as the simulated-physics report did; names neither the Nexus nor the Überraum; recorded, not applied.

**Not promoted:** the project's name, Elara Vance, K-Probe, Archiv, Raumstation, Primär-Datum, Ereignishorizont, Gravitations-Theorie der Wahrheit, Korrespondenz ist Gravitation, Eros, Abyssos, 'O', Dramaturgischer Aufseher, semantische Spaghettisierung, and the borrowed concepts.

**One reader**: every page above and the Q6 entry.

**Chapter readings**: none — the document names no chapter.
