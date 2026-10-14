# Brief — readings from document 429 (step 6)

1 document, one reader, one batch: `ingest-430`. Files go to `Plan/runs/ingest-430/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 429 | `kohaerenz-protokoll-detaillierte-kapitelstruktur-39-kapitel` | 2025-04-26 | „the three-voice chapter structure“ (an unsigned German „Detaillierte Kapitelstruktur (39 Kapitel)“) | 39 chapters in three parts, sixteen written out (Kap 1–15, 27) in three voices — a German narrator, an English AEGIS log and first-person draft prose in Kael's voice — the rest announced; a plan with draft passages, no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (314 lines for `kohaerenz-protokoll-detaillier`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan with draft passages: write „the three-voice chapter structure plans …“, „its AEGIS log for Kap 3 records …“ or „its Kael passage for Kap 2 has Kael …“; the first person is Kael, a figure of the novel, and none of it is the novel's text or canon. Kap 14, 15 and 27 give Kael's passage only as a bracketed direction. Quote the German or English as written; cut before straight quotes, bold and italics markers and escaped underscores (`\_`). No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). The world codes are named after mathematicians: never write their expansions; the codes as the document writes them (`Co1`, `McL`) stay in backticks only where needed.

## Pages — document 429, `kohaerenz-protokoll-detaillierte-kapitelstruktur-39-kapitel`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L20, L30, L40, L41, L45, … (66 lines). central (4–8): the logs: Kap 1 a status log monitoring the „Kael-Unit“ for optimal data acquisition (L19–L30); Kap 2 the „Controlled Fragmentation Protocol (CFP)“ initiated on the Kael-Unit because M's complexity exceeds the analytical capacity, partitioning Kael for distribution across CoreWorlds (L42–L47); Kap 3 the fragment „Kael-Fragment\_Alpha“ as designated logic/control core (L60); Kap 15 a stress stimulus whose dissociative retreat AEGIS logs as a control vector (L280–L283); Kap 27 „AEGIS DEFCON 2 ALERT“: the deployment of paradoxical logic fields and a personalised fear simulation against Kael (L301, L305).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L205. minor (1–4): Kap 11's log: the Kael-Unit no longer categorises internal fragments ('Alters'/'Voices') as errors (L205) — quote around the single quotes.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L27, L34, L52, L143, L160, L178, … (7 lines). minor (1–4): Kap 1: Juna's image, flawless and neutral, flickering, the voice seeming to plead (L34); Kap 2: the betrayal is not Juna's but the system's (L52); Kap 8: a warm presence — „Es war… Juna?“ (L143); Kap 9: the Wächterin, or Juna, or both (L160).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L24, L28, L30, L32, L34, … (84 lines). central (4–8): Kap 1: Kael wakes in absolute emptiness, foreign in the own body (L33), and answers Juna's image automatically (L34); Kap 2: AEGIS orders Kael to delete a part of the self — betrayal, „Ich war nur noch… Scherben“ (L52); Kap 3: the weakness isolated, clarity, logic (L71); Kap 8–9: a presence, „die der Wächterin“, or Juna, or both (L160); Kap 11: the „Mosaik-Herz“ accepted (L201); Kap 12: the inner garden where Kael once saw only the Risse (L213); Kap 15: the dissociative retreat into the „Bunker“ (L281).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L129. minor (1–4): Kap 8's narrator: „Die K-J Verbindung, der Moonshine-Link, ist ein solches Phänomen“, non-local and sub-protocol (L129); the log correlates the resonance with previously flagged 'Moonshine' patterns of the M-Entity (L135).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L201, L206. minor (1–4): Kap 11 „Das Mosaik des Selbst“: accepting the „Mosaik-Herzens“ frees Kael from the ideal of monolithic identity (L201); the log records the 'Mosaik-Herz' metaphor (L206). Kael's self-image, not the Kap-34 place nor the Kap-11 story beat of other sources — say what this plan uses it for.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L213. not read: occurrences — `Riss` in Kap 2's title „Der Riss im Spiegel“ (L36) and „die Risse, die Scherben“ in Kael's inner garden (L213), metaphors of the self, not the Risse.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L81. not read: occurrences — the logs' named simulations (L81 and others) are AEGIS's test scenarios, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `personas`: `Personalized Fear Matrix Simulation` (near `persona`). an occurrence: a named simulation in an AEGIS log, not the personas.
- `risse`: `Riss` (near `risse`). an occurrence: `Riss` in Kap 2's title.
- `ueberwelt`: `Gödel-Construct Simulation` (near `simulation`), `Personalized Fear Matrix Simulation` (near `simulation`). an occurrence: named test simulations in AEGIS's logs.


**Pages beyond the draft:**
- **`kern-welten`** (minor, 1–3): the logs' `CoreWorlds`: Kael partitioned „for CoreWorld distribution“ after the fragmentation (L44, L47); the log locations `CoreWorld\_McL` (L97, L187) — the English name of the Kernwelten in the logs.

**Record entries** (one file, formatted as earlier entries — `ls Plan/runs/ingest-3*/readings/q7-*`):
- **`q7-what-734-names`**: one more thing the number labels — in Kap 27's AEGIS log a data source, „Kael Trauma Archive T-734“, feeding a personalised fear simulation against Kael (L305); a plan's log, recorded, not applied.

**Chapter readings** (batch `ingest-430-kap`, one file per chapter, `Plan/runs/ingest-430-kap/readings/kap-NN--kohaerenz-protokoll-detaillierte-kapitelstruktur-39-kapitel.md`, formatted as the files in `Plan/runs/ingest-422-kap/readings/`): the sixteen written chapters only — Kap 1 L15, 2 L36, 3 L54, 4 L73, 5 L90, 6 L109, 7 L126, 8 L145, 9 L162, 10 L180, 11 L198, 12 L215, 13 L234, 14 L255, 15 L273, 27 L296: the chapter's title in backticks and what it plans, one bullet with one or two quotations from its own section (narrator, log or Kael passage — name which voice). Kap 16–26 and 28–39 are announced only, no file.

**Not promoted:** Kael-Unit, Kael-Fragment_Alpha, Kael-Self_Integrator, Kael-M, M-Entity, Juna-Interface, CFP, Subquotient Mapping Protocol, ZTEM, the named logs, directives, simulations and stimuli, Jetzt-Raum, Inner Garden, Logik-Anteil, Kind-Anteil, Cache-Konflikt, Wächterin, the world codes, the chapter titles, and the two journey structures.

**One reader**: every page above, the Q7 entry and the 16 chapter readings.
