# Brief — readings from document 450 (step 6)

1 document, one reader, one batch: `ingest-450`. Files go to `Plan/runs/ingest-450/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 450 | `kohaerenz-protokoll-monster-plot-entwicklung` | 2025-04-23 | „the Monster plot blueprint“ (an unsigned German plot proposal written as a research report, „Analyse an den Grenzen des Verstehens“) | sets AEGIS's directive of coherence by Abgrenzung against the Kael-Juna connection read as the Monstergruppe, with Kael's integration in an inner-parts model, six Kernwelten, an act-by-act beat sheet marked as examples and a proposed concept matrix; proposals throughout, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (300 lines for `kohaerenz-protokoll-monster-pl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal: write „the Monster plot blueprint proposes …“ — its beats are „Beispielhafte Beats – Ausarbeitung erforderlich“ (L192), its matrix a recommendation. Its `[User Query …]` labels are the export's, never quoted. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim). Never write a real person's name nor a term carrying one, nor quote a span containing one (the borrowed paradoxes, theorems and psychologists).

## Pages — document 450, `kohaerenz-protokoll-monster-plot-entwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L13, L15, L17, L19, L21, … (104 lines). central (4–8): AEGIS's core directive: systemic coherence by Abgrenzung (L17); first classifies the connection as a threat or system error (L21); its tools — deduction, data analysis, simulation, decomposition — unfit for the connection (L29, L75–L80); its definition of coherence „inhärent brüchig“ (L33); a significant system failure at the midpoint (L212); its fate at the end left open: changed, neutralised or contained (L223); its failure more than a plot element (L289).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L47, L122. minor (1–4): the connection reaches the disparate, fragmented or rejected parts of Kael's psyche, the Alters (L47); the inner parts (Exilanten, Manager, Feuerlöscher, L116–L118) — describe, the model is borrowed.
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L25, L35, L49, L53, L266. minor (1–4): the K-J connection should be shown as a strongly emergent phenomenon whose properties cannot be derived from the parts (L53); section B integrates emergence (L49).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L65, L96, L181, L210, L235. minor (1–4): Guardians stationed in the Kernwelten to oversee or carry out the experiments, direct witnesses of AEGIS's failure (L181); in Akt II the loyalty of some Guardians begins to crumble (L210); the document never introduces them with a definition.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L19, L37, L41, L43, L45, … (19 lines). central (4–8): introduced with Kael as K-J (L17); the connection escapes every classification by AEGIS (L19); Juna's role mostly left open: perhaps supporting as mentor (L139), the study of Juna's origin or nature „falls zutreffend“ (L81), the fate of Juna settled only at the end (L223).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L19, L37, L41, L43, L45, … (68 lines). central (4–8): Kael and Juna introduced as K-J (L17); the connection reaches disparate or rejected parts of Kael's psyche, the Alters (L47); an inner-parts model as language for Kael's inner world (L112); at the start „Zu Beginn ist Kael innerlich zerrissen“ (L123); the climax: Kael does not defeat AEGIS by outwitting it (L222); „Kael repräsentiert den Weg der Integration“ (L246); Kael's success as the refutation of AEGIS's premise (L158).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L46, L55, L81, L140, L162, L166, … (25 lines); `Kernwelt` L46, L55, L81, L140, L162, L166, … (29 lines). central (4–8): the Kernwelten as active elements of the thematic structure, each embodying specific concepts (L166); six worlds — Chaos-Welt, Quanten-Verschränkungs-Welt, Logik-Paradox-Welt, Autopoiesis-Welt, Liminalitäts-Welt, Gedächtnis-Welt (L168–L173); AEGIS uses them to test hypotheses about the connection (L179), the connection must subvert the rules in each (L180); the worlds as metaphors of AEGIS's own inner state (L186); the first Kernwelt confrontation in Akt I (L201).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — L11 is the title; `Kohärenz durch Abgrenzung` / `Integration` are the document's own pair.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L69. not read: an occurrence — L69 says the connection is a signal from a level of reality beyond AEGIS's programming, a general sense, not the named Realitätsebenen.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L88, L92, L96, L104, L181, L186, … (11 lines). central (4–8): section C names positive feedback loops as the Risse (L92); the vicious circles manifest as the cracks in the system (L96); each failure in a Kernwelt sharpens the Risse (L181).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: an occurrence — `Simulation` on L29 is one of AEGIS's methods.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz durch Abgrenzung` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title and the document's own pair `Kohärenz durch Abgrenzung` / `Kohärenz durch Integration`.
- `landauer-signatur`: `Dauer` (near `landauersignatur`). an occurrence: `Dauer` is the ordinary word.


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–2): Monstrous Moonshine serves as the metaphor for the non-local connection of K-J (L46 — quote around the inner quotes); the connection tied to fundamental truths AEGIS is blind to (L69).

**Record entries** (one file each, formatted as earlier entries — `ls Plan/runs/ingest-44*/readings/q*-*`):
- **`q8-aegis-after-the-vortex`**: the Monster plot blueprint leaves AEGIS's end open — irrevocably changed, neutralised or contained (L223); recorded, not applied.
- **`q3-how-many-kern-welten-and-alters`**: the blueprint names six Kernwelten, each a concept (L168–L173); recorded.
- **`q1-guardians-and-aegis`**: the blueprint has the Guardians stationed in the Kernwelten to oversee or carry out AEGIS's experiments, their loyalty crumbling in Akt II (L181, L210); recorded.

**No chapter readings**: the blueprint names no chapter; its structure is three acts.

**Not promoted:** Kohärenz durch Abgrenzung / Integration, K-J-Verbindung, Monstergruppe, the six worlds' names, Teufelskreise, Ontologischer Mismatch, Exilanten, Manager, Feuerlöscher, Mapping-Matrix, Testgelände für AEGIS, and the borrowed concepts.

**One reader**: every page above and the three record entries.
