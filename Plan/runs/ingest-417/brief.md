# Brief — readings from document 416 (step 6)

1 document, one reader, one batch: `ingest-417`. Files go to `Plan/runs/ingest-417/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 416 | `roman-analyse-kohaerenz-protokoll-akt-i` | 2026-04-08 | „the Act I reader-psychology report“ (an unsigned German „Forschungsbericht“ on Act I, working title „Die Architektur der Dissoziation“) | applies borrowed theories of reading to thirteen chapter sections of Act I (Kap. 1–13, L51–L231), then a five-phase overview and a table of directives; it describes the chapters in the present tense as a plan of effects and makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (323 lines for `roman-analyse-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report on intended reader effects: write „the Act I reader-psychology report plans …“ or „its Kap. 6 …“; what it says of the chapters is a plan of effects, not the chapters as written. Quote the German as written; cut before straight and nested quotes, italics and bold markers and glued footnote digits. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). Never write a real person's name — the report names researchers and published authors (e.g. L25, L29, L31, L43); describe their concepts without the names, and never quote a line span that contains one. Nothing about the author's person.

## Pages — document 416, `roman-analyse-kohaerenz-protokoll-akt-i`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L29, L35, L41, L45, L69, … (25 lines). minor (1–3): the overpowering system AEGIS not intervening to save Kael in Kap. 11 (L195); the complex system demands of AEGIS solved by Kael or Lex in Kap. 5 (L111); further mentions of AEGIS's systems (L53 and the tables).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L125, L209. minor (1–3): the first semi-conscious interaction with an alter, „Nyx oder Alex“ (L125); among the dominant alters of the internal conference (L209).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L31, L35, L45, L97, L173, L209, … (10 lines). minor (1–3): „Einige der dreizehn Alters“ gaining first blurred contours in Kap. 9 (L173); the first conscious interaction of the dominant alters as a clinical milestone (L209).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L35. not read: an occurrence — a general sense in the report's theory section (L35).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L31, L83, L89, L195, L209, L263, … (7 lines). minor (1–3): „Durch das Aufblitzen von Junas Bild auf den Monitoren“ — Kael's loss made graspable (L83); Juna's status kept in suspension (L195); further mentions (L263).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L27, L31, L35, L41, L45, … (48 lines). central (4–8): Kael as the protagonist the reader is bound to (L31); Juna's image on the monitors making the ice-cold Kael graspable as a being with a history of loss (L83); Kael's inner monologue feeling own thoughts as foreign (L97); Kael's flashback triggered by failing gravity (L181); AEGIS not rescuing Kael in mortal danger (L195); „Die erste bewusste Interaktion der dominierenden Alters“ — Kael, Lex, Alex, Rhys — as the internal conference (L209).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L29. minor (1–3): the uncanny-valley phenomenon carried into the Konstrukt-Stadt (L29) — quote only words after the researcher's name on that line.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L69, L111, L209, L262. minor (1–3): Kael, „respektive sein Alter Lex“, acting flawlessly in Kap. 5 (L111); among the dominant alters of the internal conference (L209).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L125. minor (1–3): the first semi-conscious interaction with an alter, „Nyx oder Alex“, in Kap. 6 (L125).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L111. not read: an occurrence — persona in a general sense (L111).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L209. minor (1–3): among the dominant alters of the internal conference in Kap. 12 (L209).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L45. not read: an occurrence — glitches in the report's general description of dissociation (L45).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L27. not read: an occurrence — simulation in the sense of embodied cognition (L27).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `hitze-polaritaetsregel`: `Hitze` (near `hitzepolaritaetsregel`), `Hitze` (near `hitzepolaritatsregel`). decided with the pages above: `Kernwelt 1` read on kern-welten (below); `Hitze` the report's sensory motif, not the Hitze-Polaritätsregel; `Kohärenz Protokoll` the title.
- `kern-welten`: `Kernwelt 1` (near `kernwelt`). decided with the pages above: `Kernwelt 1` read on kern-welten (below); `Hitze` the report's sensory motif, not the Hitze-Polaritätsregel; `Kohärenz Protokoll` the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). decided with the pages above: `Kernwelt 1` read on kern-welten (below); `Hitze` the report's sensory motif, not the Hitze-Polaritätsregel; `Kohärenz Protokoll` the title.


**Pages beyond the draft:**
- **`kern-welten`** (minor, 1–2): the geometry of „der Kernwelt 1“ itself becoming the threat (L43) — quote only words after the novel's title on that line, never the line's named author; `Kernwelt 1` as the setting (L25).

**Record entries:** none.

**Chapter readings** (batch `ingest-417-kap`, one file per chapter, `Plan/runs/ingest-417-kap/readings/kap-NN--roman-analyse-kohaerenz-protokoll-akt-i.md`, Kap 1 to Kap 13, formatted as the files in `Plan/runs/ingest-397-kap/readings/`): each chapter's section in the report — its heading's title (`Kap. N „…“`, L51, L65, L79, L93, L107, L121, L135, L149, L163, L177, L191, L205, L219) and the effect and technique it plans, one bullet with one or two quotations from the section's own lines. A plan of effects, not the chapter as written. Never quote a span naming a real person.

**Pages not read:** entropie, kohaerenz, personas, risse, ueberwelt — occurrences.

**Not promoted:** Die Architektur der Dissoziation, Universal Reboot, K0-Narbe, Wartungsschächte, Subroutine-Interferenz, internen Konferenz, Co-Consciousness, axiomatische Lücke, and the borrowed concepts.

**One reader**: every page above and the 13 chapter readings.
