# Brief — readings from document 214 (step 6)

1 document, one reader, one batch: `ingest-214`. Files go to `Plan/runs/ingest-214/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 214 | `narrative-kernentwicklung-aegis-und-system-kael` | 2025-11-03 | „the development dossier“ (an unsigned planning dossier) | a German „Narratives Architektur- und Entwicklungsdossier“ that frames the novel as the tragedy of AEGIS and of System Kael, the fragmented man AEGIS made in the image of its own trauma; it sets out the coherence-correspondence law, a three-act integration plan with a table of the parts' roles, and advice on technique and genre — a plan, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (294 lines for `narrative-kernentwicklung-aegi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A planning dossier: write „the development dossier plans / frames …“ and keep its hedges (`Es könnte`, `Integratorin?`, `potenzielle`). German — quote as written; cut before glued footnote digits (`Kohärenz Protokolls“ von AEGIS.6`) and inner quotes; tables carry escaped bold — never quote across them.

## Pages — document 214, `narrative-kernentwicklung-aegis-und-system-kael`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L30, L32, L36, L40, L42, … (26 lines). central (3–6): the novel as a tragedy whose root is AEGIS's own definition, „Aegis ist, was Aegis verhindert, dass es nicht ist“ (L40) — cut before the glued digit; its rigidity as Hamartia and Hybris (L42); AEGIS externalising its trauma by structuring a human mind after its own fragmentation (L50); AEGIS as the ultimate coherentist (L75); at the end a choice — accept the truth and evolve or suffer total system collapse (L166) — cut before the glued digit.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L83, L184. minor (1–3): Alex among the four ANPs of the TSDP analysis the dossier cites (L83).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L83. minor (1–3): Argus, with Selene, one of two parts with mixed functions (L83).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cache-Kohärenz` alone on L70. minor (1–3): read L70 — decide reading or occurrence and say which.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L42, L115, L145, L232, L258, L259. minor (1–3): the risse as visual manifestations of entropy and data corruption (L145); the sensory lexicon for entropy and the Risse (L232).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L135. minor (1–3): in act I „die rigide Kontrolle der Überwelt durch die“ Guardians of AEGIS is established (L135) — cut before the inner quotes; the dossier does not define them.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L83, L87. minor (1–3): Isabelle among the five EPs (L83).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L73. minor (1–3): the Risse where external truth breaks through, Juna/V among it (L73) — read the line; in act I the inciting incident „Es könnte eine Begegnung mit Juna/V sein“ (L136); Kael accompanied by Juna/V into the Risse (L145).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L46, L50, L52, L54, L73, … (32 lines). central (3–6): System Kael as „die lebendige, atmende Verkörperung des Traumas von AEGIS“ (L50); at least eleven identified parts (L52); the narrative core sentence — „die Reise eines fragmentierten Mannes, Kael“ facing the digital god who made him in the image of its own trauma (L54); the midpoint: Kael is the system's founding trauma, a living memory of the Genesis-Krise (L155) — cut before the inner quotes; Kael (ANP-Host) in the role table (L181).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L83, L85, L116, L150, L184, L221. minor (1–3): Kiko among the five EPs (L83); Kiko's fear as Kael's unexplained panic (L184); a stream of consciousness when Kiko has control (L221).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13); the coherence theory is read on aegis and ueberwelt.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L83, L86, L116, L137, L164, L182, … (10 lines). central (3–6): Lex among the four ANPs (L83); Lex's rigid logic against Rhys's empathy as inner indecision (L86); Lex arguing for caution in act I (L137); Lex (ANP-Rationalist) in the role table (L182); analytic prose when Lex has control (L219).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L83. minor (1–3): Lia among the five EPs (L83).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L83. minor (1–3): Moros among the five EPs (L83).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L117. minor (1–3): read L117 — the table row on unity against diversity; decide reading or occurrence.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L83, L85, L87, L116, L150, L164, … (8 lines). minor (1–3): Nyx among the five EPs (L83); Nyx needed against aggressive, corrupted data forms in the Risse (L150); Nyx (EP-Kampf) in the role table (L183); aggressive, clipped prose when Nyx has control (L220).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L83, L86, L118, L137, L156, L184, … (7 lines). minor (1–3): Rhys among the four ANPs (L83); Rhys (ANP-Fürsorger) in the role table (L185); Rhys's empathy against Lex's logic (L86).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L73, L145, L146, L151, L182, L183, … (9 lines). central (3–6): „Die“ Risse as physical manifestations of the isolation objection against the coherence theory (L73) — cut before the inner quotes; act II's descent into the Risse, unstable regions of the Überwelt where AEGIS's control fails (L145); the Risse as fragmented memories of the Genesis-Krise (L151).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L83, L156, L186. minor (1–3): Selene and Argus as parts with mixed functions (L83); „die potenzielle Integratorin“ (L156); „Selene (Integratorin?)“ in the role table (L186) — keep the question mark.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L50, L79, L83, L100, L260. minor (1–3): the TSDP as the moment-to-moment physics of the protagonist's consciousness (L83); Kael's inner world as described in the TSDP analysis (L50).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L70, L72, L135, L145, L204. minor (1–3): the Überwelt under AEGIS's control operating on the coherence theory (L72); the Risse as unstable regions of the Überwelt (L145); hard science fiction as the language of AEGIS and the Überwelt (L204).

- **`genesis`** (minor, 1–2): the Genesis-Krise as the founding trauma, „die ursprüngliche Wunde“ (L30) — read the line; its Big Bang of the psychological landscape (L32).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading — see the extra page below.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Fehlausgerichteten Kohärenz` (near `koharenz`), `Neue Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`), `Dekohärenz` (near `koharenz`). occurrences: the title; `Fehlausgerichteten Kohärenz` is AEGIS's Hamartia, read on aegis; `Neue Kohärenz` is the act III heading.


**Record entries** (one file each):

- **`c16-kael-origin`**: AEGIS externalised its trauma by structuring a human mind after its own fragmentation (L50); AEGIS made Kael in the image of its own trauma (L54); Kael *is* the system's founding trauma, a living memory of the Genesis-Krise (L155).
- **`q3-how-many-kern-welten-and-alters`**: four ANPs, five EPs and two mixed parts after a cited TSDP analysis (L83), „mindestens elf“ (L52).
- **`q8-aegis-after-the-vortex`**: AEGIS's choice between accepting the truth and evolving, or a total system collapse (L166).
- **`c17-kael-gender`**: „die Reise eines fragmentierten Mannes, Kael“ (L54) — male, without naming the question.

**Not promoted:** the Integrationsprotokoll, the duality matrix, the genre trinity, the sensory lexicon, Hamartia and Hybris.

**Two readers**, disjoint: (1) kael, lex, nyx, kiko, rhys, lia, moros, isabelle, alex, argus, selene, tsdp, multiplizitaet and the records q3, c17; (2) aegis, genesis, ueberwelt, risse, entropie, guardians, juna, cache-kohaerenz and the records c16, q8.

No chapter readings: the dossier names acts, not chapters.
