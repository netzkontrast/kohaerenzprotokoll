# Brief — readings from document 235 (step 6)

1 document, one reader, one batch: `ingest-235`. Files go to `Plan/runs/ingest-235/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 235 | `kohaerenz-protokoll-spannungsfelder-vertiefen` | 2025-04-28 | „the tension-points analysis“ (an unsigned German analysis) | a German analysis that sorts the project's tension points into five kinds of conflict, explains Paradoxon X and Cache Kohärenz through borrowed therapy and systems theory, and gives scene, dialogue, symbol and plot advice; it hedges throughout and makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (387 lines for `kohaerenz-protokoll-spannungsf`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that hedges and advises: write „the tension-points analysis supposes …“, „… proposes …“; keep its „mutmaßlich“, „wahrscheinlich“, „möglicherweise“ and its conditionals; its advice („sollte“) is advice, its questions are questions. Borrowed theory (IFS, Jung, cybernetics) is its lens. It writes borrowed terms in straight quotes — quote around them.

## Pages — document 235, `kohaerenz-protokoll-spannungsfelder-vertiefen`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L29, L50, L59, L63, L67, … (63 lines). central (2–4): Paradoxon X as „Das Kernparadoxon“: „AEGIS' Kontrollmethoden erzeugen die Instabilität, die sie verhindern sollen“ (L79); AEGIS „mutmaßlich auf klassischer Logik basierend“ (L80); AEGIS's influence on memory „ambivalent“ (L155); Paradoxon X as „der narrative Motor“ (L145).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L63, L69, L90, L92, L122, L143, … (9 lines). minor (1–3): AEGIS's „Zero-Trust-Architektur“ set against healing (L90).
- **`cache-kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Cache Kohärenz` L51, L109, L113, L121, L133, L147, … (19 lines). central (2–4): Cache Kohärenz as „die narrative Manifestation der gestörten Gedächtnis- und Identitätskontinuität bei Kael“ (L151); arising when the protective walls crumble, or when the protections are too strong (L152); „das erlebbare Symptom der tiefen psychologischen Fragmentierung“ (L157).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L370. occurrence: `DID` stands in a reference title (L370).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L85, L92, L102, L125, L140, L142, … (8 lines). occurrence: `Emergenz` names emergence in general, of Kael's psyche and the Verbindung V (L85, L92, L102), not AEGIS's emergence.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L32, L61, L79, L90, L94, L96, … (24 lines). central (2–4): „Die Beziehung zwischen Kael und Juna“ as „ein zentraler Konfliktherd“ (L96); „Juna/V repräsentiert eine alternative Form der Kohärenz“ (L102); its questions whether Juna is aware, whether AEGIS manipulates her too (L99) — questions, not answers.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L21, L23, L51, L55, L59, … (71 lines). central (2–4): Kael's Personas modelled on Internal Family Systems (L23); Kael possibly experiencing his memories as fragmented (L51); the Kernwelten as stages for Kael's inner dramas (L73).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L29, L50, L59, L63, L70, L73, … (18 lines); `Kernwelt` L29, L50, L59, L63, L70, L73, … (20 lines). minor (1–3): „Die Kernwelten (Co₁, McL, B, Ly) sind als diagnostische Arenen konzipiert“ (L70); „externalisierte Bühnen für Kaels innere Dramen“ (L73); the advice that each world should provoke a specific inner conflict (L253).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L30, L40, L50, L70, L100, L253. minor (1–3): „Kiko, als verletzliches Kind-Teil“ (L30).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L29, L30, L31, L32, L40, L50, … (11 lines). minor (1–3): „Lex, als logisch-rationaler Anteil“ (L29); Kiko against a Manager, „(Lex/Rhys?)“ with its own question mark (L30).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L264. occurrence: `Multiplizität` stands in a piece of writing advice (L264).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L29, L32, L50, L55, L100, L120. minor (1–3): Nyx as the repressed Shadow in a Jungian reading (L55).
- **`personas`** (minor, 1–4): the census's surfaces — `Personas` L23, L55, L100, L111, L167, L189, … (7 lines). minor (1–3): Kael's Personas modelled on psychological theories such as IFS (L23); „Ontologie der Personas“: their ontological nature unclear and a source of conflict (L111).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L30, L32, L50, L98, L100, L253. minor (1–3): Rhys named with a question mark as a possible Manager (L30); Rhys's need for the Verbindung V against AEGIS's suppression (L98).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L190. minor (1–3): glitches and system failures as consequences of Paradoxon X, in a piece of design advice (L190).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L55, L275. minor (1–3): Selene as possibly the conscious ego in a Jungian reading (L55); the core Self, „Selene/Wächterin“, mediating between the parts (L275).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L23, L46, L51, L63, L73, L90, … (14 lines). minor (1–3): TSDP among the borrowed models the analysis applies (L46, L51); read as its lens.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L108. occurrence: `Simulation` stands in „Simulationsunsicherheit“, a question whether all of Kael's reality is simulated (L108), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` names resonance in general (L92, L102), not the Entropie-Resonanz-Protokolle.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache Kohärenz-Problem` (near `koharenz`). occurrence: the title; `Cache Kohärenz-Problem` read on cache-kohaerenz.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` in general, not the Resonanz-Landschaft.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: `Simulationshypothese` is the borrowed simulation hypothesis.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten written as Co₁, McL, B, Ly, diagnostic arenas (L70).

**Not promoted:** the five conflict kinds, Spannungspunkte, the borrowed models (IFS, Jungian shadow, second-order cybernetics), Verbindung V, Exiles/Managers/Firefighters, the writing advice.

**One reader**: aegis, cache-kohaerenz, kael, juna, kern-welten, lex, kiko, nyx, rhys, selene, personas, tsdp, aegis-teilfunktionen, risse and the record q3.

**Chapter readings**: none.
