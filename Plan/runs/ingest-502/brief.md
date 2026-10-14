# Brief — readings from document 502 (step 6)

1 document, one reader, one batch: `ingest-502`. Files go to `Plan/runs/ingest-502/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 502 | `roman-entwicklung-ontologie-trauma-horror` | 2026-04-16 | „the ontology-trauma-horror report“ (an unsigned German research report) | four sub-questions — philosophy, narratology, trauma and dissociation, cosmic horror — each testing a hypothesis, with proposals for the novel, then a synthesis that states identities of AEGIS and Juna; a research report and proposal, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (183 lines for `roman-entwicklung-ontologie-tr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report: write „the ontology-trauma-horror report reads/proposes …“. Its central person is only „der Protagonist“ — never write Kael for it. „DID“ is the protagonist's condition in the novel. The document names many real thinkers, writers, researchers and psychiatrists on nearly every line: NEVER write any of them, never quote a span containing one, and never write a concept named after one (the statistical boundary the report borrows for AEGIS carries a person's name — describe it as „a borrowed statistical boundary“, never name it). Lines L39, L47, L53, L64, L86, L88, L90, L138–L142 contain names: quote only short spans that contain none, or describe. Quote verbatim; cut before bold, escaped markup and footnote digits. No gendered pronoun for Juna, AEGIS or the protagonist in our own prose.

## Pages — document 502, `roman-entwicklung-ontologie-trauma-horror`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L39, L61, L63, L76, L90, L100, … (14 lines). central (4–8): AEGIS read as a borrowed statistical boundary that decides which information may exist within experience (L39 — quote only a name-free span such as „Sie ist die absolute statistische Membran“); AEGIS as no external computing machine but the macro-scale manifestation of the protagonist's morning process, „die Cortisol Awakening Response (CAR) des Universums“ (L138 — quote name-free spans only); the morning loss as the alters forced into local sleep so the host can function in AEGIS's world (L100); the closing image of a world that functions perfectly, AEGIS the flawless mechanics of existence (L146).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L86, L88, L146. minor (1–4): the alters as fragments the protagonist clings to, sorted out and deleted every second by the mechanics of existence (L146); waking as the alters forced into local sleep (L100).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L63, L80, L82, L84, L88, L90, … (8 lines). minor (1–4): the report reads waking for people with a dissociative identity structure as a traumatic neurochemical act, against its adversarial hypothesis (L80); the alters' neural areas forced into local sleep so the host can function (L100); the table's proposal that the morning extinction of DID plurality be felt as an infection by AEGIS's lawfulness (L63 — the span must contain no name).
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L53. not read: an occurrence — `Systemgrenze` describes a named writer's method, not the novel's wall.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L64, L132, L142. minor (1–4): Juna outside the report's central concept of boundary-drawing: „Juna operiert außerhalb der Tathandlung“ and escaping the AEGIS boundary (L142); not an ordinary Alter that can be forced into local sleep (L142); „Denk an Juna“ as an example of the brain's offers of meaning (L132). Do not quote the L64 or L142 spans that name an author or the borrowed boundary.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L82. not read: an occurrence — narrative coherence of the self in a neuroscience passage.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L47. not read: an occurrence — „Risse in der Realität“ in a named writer's fiction.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L39. minor (1–4): „AEGIS rechnet keine Simulation“ (L39): the report denies the simulation reading; the same at L138, AEGIS no machine „im Sinne einer klassischen Simulation“ (quote only name-free spans).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Record entries:** none.

**No chapter readings**: the report names no chapter (`Kap` 0, `Kapitel` 0).

**Not promoted:** the morning-loss vocabulary (Anker-Zustand, local sleep, hypnopompia), Weltmaschine, the hypothesis tags, the block labels, and every borrowed concept (most carry a person's name).

**One reader**: aegis, juna, alters, did, ueberwelt.
