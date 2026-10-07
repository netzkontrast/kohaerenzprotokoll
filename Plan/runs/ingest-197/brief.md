# Brief — readings from document 197 (step 6)

1 document, one reader, one batch: `ingest-197`. Files go to `Plan/runs/ingest-197/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 197 | `roman-konzept-kael-aegis-simulation` | 2025-05-01 | „the simulation concept“ (titled on Kael, AEGIS and the simulation) | a German concept paper that „skizziert die narrative Architektur“ (L15) of a novel in three parts: System Kael with a trauma-fragmented identity (Kael-Host, Lex, Nyx, Kiko) against AEGIS, an entropy-managing system in a possibly simulated reality; Juna/V, the Fundament, the Kernwelten, the Risse and the Netz as plot elements, and five resolution scenarios (L258–L264); 37 web references behind glued numbers — it calls itself a „robuste Grundlage“ (L280), no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (321 lines for `roman-konzept-kael-aegis-simul`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept paper that proposes and asks: write „the simulation concept proposes / asks …“; many lines are questions — record them as questions. German — quote as written; cut before glued reference digits and before the `\[User Query\]` markers (export residue); cut before inner straight quotes; `--find` drops digits glued to words.

## Pages — document 197, `roman-konzept-kael-aegis-simulation`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L21, L22, L29, L30, L34, … (75 lines). central (2–4): „Das antagonistische System, AEGIS“, „Autonomous Entropic Gatekeeper for Integrity Systems“, whose „Kernfunktion ist das Management von Entropie“ (L22); its purpose clearer in part 2, the question of its consciousness more relevant (L119); „Ist es nur ein fehlerhaftes Werkzeug seiner Schöpfer“ (L175); Kael's goal possibly not its destruction (L197).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L21, L28, L34, L42, L44, L49, … (23 lines). central (2–4): „Kaels Identität ist fragmentiert“ into alters (L21); alter-specific goals — Lex, Nyx (L66); full integration against functional multiplicity (L169).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L305. occurrence: `DID` stands only in a reference title (L305).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L15, L22, L29, L30, L34, L107, … (15 lines). central (2–4): AEGIS's core function, „das Management von Entropie“ (L22); keeping the simulation's integrity by controlling entropy — uncertainty, complexity, deviation (L121); Kael's integration as more complexity, a fundamental question (L121).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L125, L185. minor (1–2): first hints of Juna/V, perhaps through the Risse or on the „Externen Ebene“ (L64) — quote around the inner quotes; Kael tries to reach it (L125); its truth revealed in the resolution (L185).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L22, L119. minor (1–2): the Wächter's behaviour mapped by Lex (L106); read L22 and L119 for the Guardians.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L64, L108, L125, L154, L178, L185, … (9 lines). central (2–4): „Juna/V-Mysterium“, an external entity perhaps outside AEGIS's control (L64); „Ihre Natur und Absichten bleiben zunächst unklar“, „Sind sie die ursprünglichen Simulanten“ (L125); allies, the simulators themselves or guardians of a higher level (L185).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L28, L30, L34, L36, … (80 lines). central (2–4): „Kaels Identität ist fragmentiert“ (L21); his mind fragmented to cope with trauma, parallel to the outer reality (L34); his integration perhaps the key to the system (L36); from survivor to investigator (L115); five endings for him (L260–L264).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L49, L50, L65, L66, L102, L106, … (11 lines); `Kernwelt` L49, L50, L65, L66, L102, L106, … (12 lines). central (2–4): „subjektive innere Landschaften, die psychologisch und thematisch kodiert sind“ (L49); each Kernwelt hides secrets about Kael's trauma and the simulation (L65); explored with the AEGIS-Überwelt in part 2 (L102).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L21, L54, L55, L66, L77, L91, … (10 lines). minor (1–2): „Der Kiko-Alter“ (L54) — read the line.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L36. occurrence: the general word in the integration sentence (L36).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L21, L49, L55, L66, L77, L89, … (11 lines). minor (1–2): „Lex (kühl, logisch, analytisch“ (L55); obsessed with decoding AEGIS's logic (L66); maps AEGIS (L106).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L21, L169, L195, L260. minor (1–2): the „funktionale Multiplizität“ as a goal (L36) — cut before the digit; as the healthier therapeutic aim than full integration (L169).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L21, L48, L54, L55, L66, L77, … (11 lines). minor (1–2): the aggressive Nyx taking control in a dangerous switch as inciting incident (L48) — cut before inner quotes; Nyx's own agenda (L66).
- **`oblivion`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Oblivion` alone on L264. occurrence: `(Oblivion)` in the fifth ending is extinction, the word, not the alter (L264).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L128. minor (1–2): the Fundament as „eine tiefere Realitätsebene unterhalb der bekannten Simulation“ (L128).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L50, L64, L106, L108, L115, L121, … (9 lines); `Glitches` L50, L203. central (2–4): „Anomalien, Glitches oder Inkonsistenzen in der wahrgenommenen Realität“ (L50); Kael learns to use and provoke the Risse (L115) — cut before inner quotes.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L22, L29, L30, L65, L100, L108, … (45 lines). central (2–4): the simulation hypothesis as the setting (L22, L29); evidence for the simulated reality confirmed in part 2 (L108); the „AEGIS-Überwelt“ explored as the Netz (L102) — cut before inner quotes; who are the Simulanten (L108).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is a clinical symptom (L28), not the Personas.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: five resolution scenarios — integration and transformation, liberation and escape, Pyrrhic victory, assimilation and understanding, system collapse (L258–L264).
- **`c16-kael-origin`**: Juna/V perhaps „die ursprünglichen Simulanten“ (L125); the questions of the resolution (L185) — no origin of Kael given; say so.

**Not promoted:** the Fundament (on realitaetsebenen), the Simulanten, the Netz, DIS/ASDS/OSDD, Bostrom's trilemma, the simulation hypothesis.

**Two readers**, disjoint: (1) kael, alters, lex, nyx, kiko, multiplizitaet, juna, externe-ebene and the record c16; (2) aegis, entropie, guardians, kern-welten, risse, ueberwelt, realitaetsebenen and the record q8.
