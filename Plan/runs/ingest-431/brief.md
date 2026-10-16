# Brief — readings from document 430 (step 6)

1 document, one reader, one batch: `ingest-431`. Files go to `Plan/runs/ingest-431/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 430 | `kohaerenz-protokoll-kapitelstruktur-mit-konzepten-39-kapitel` | 2025-04-26 | „the concept chapter map“ (an unsigned German „Kapitelstruktur mit Konzepten (39 Kapitel)“) | all 39 chapters in three parts, each with three lines — what the narrator shows, what AEGIS does, and a fundamental concept the chapter applies; a plan, no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (402 lines for `kohaerenz-protokoll-kapitelstr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the concept chapter map plans …“ or „the concept chapter map's Kap 33 …“. Each chapter's heading stands at L15 + 10·(N−1); its narrator line is four lines below, its AEGIS line five, its concept line six. Kap 26 stands under Part 3's heading (L263), which gives 27–39 — recorded, not corrected. The concept lines name real thinkers and theories named after people (L340, L351 and others): never write those names nor quote a span containing one. The recurring trauma symbol of Kap 24 (L249) is the plan's Kernwunde for Kael: name it as that, no detail. Quote the German as written; cut before straight quotes, bold markers and escaped underscores. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). The world codes are named after mathematicians: never expand them.

## Pages — document 430, `kohaerenz-protokoll-kapitelstruktur-mit-konzepten-39-kapitel`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L20, L30, L40, L50, L60, L70, … (47 lines). central (4–8): Kap 1: logs Kael's integration, high logic adherence, suppressed intuition (L20); Kap 2: initiates the „Controlled Fragmentation Protocol“ to isolate M's attributes (L30); Kap 7: discovers the K-J vector signature as „alternatives Kohärenzprotokoll“ undermining the fragmentation (L80); Kap 30: registers Kael's identity change, „Kontrollverlust“ (L300); Kap 33: system collapse from unsolvable paradoxes or failed autopoiesis (L340 — describe, the line names a person); Kap 34: „(Nicht mehr existent oder nur noch als passive Datenreste)“ (L350); Kap 35–39: „(Irrelevant)“.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L201. minor (1–4): Kap 19: cache conflicts in everyday multiplicity (L199) and the concept line „Cache Kohärenz & Funktionale Multiplizität im Alltag“ (L201).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L90, L221, L331. minor (1–4): Kap 9: the emergence of an integrating function (L90); Kap 21's concept, emergence and creativity (L221); Kap 32's concept, emergence and self-organisation (L331).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L130, L381. minor (1–4): Kap 12: AEGIS scans Kael's state „hoher Kohärenz und niedriger Entropie“ (L130); Kap 37's concept, entropy and negentropy (L381).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L359, L399. minor (1–4): Kap 35: Kael/M and Juna meet „im Potentialmeer“ with mutual understanding (L359); Kap 39: the closing image of Kael/M and Juna exploring the Potentialmeer together (L399).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L20, L30, L90, L100, L110, L120, … (35 lines). central (4–8): Kap 2: Kael's dissociation registered as an expected consequence (L30); Kap 9: an integrating function, 'Kael-Self\_Integrator' (L90); Kap 11: self-concept as a cooperative system (L120); Kap 19: living with inner multiplicity, switches in everyday tasks (L199); Kap 32: the transformation into „Kael/M“, uniting human experience and M's complexity (L329); Kap 34: Kael/M leaves the ruins of AEGIS's system into the Potentialmeer (L349).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11); „alternatives Kohärenzprotokoll“ (L80, read on aegis) and Kap 39's title „Echo der Kohärenz“ name no term of the page.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L119, L120. minor (1–4): Kap 11: AEGIS updates Kael's profile: self-concept as a cooperative system ('Mosaik-Herz') (L120) — Kael's self-image, as the plan uses it.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L121, L201. minor (1–4): Kap 11: „funktionale Multiplizität als M's möglicher natürlicher Zustand“ (L120) and the concept line „Funktionale Multiplizität & Akzeptanz“ (L121); Kap 19: inner multiplicity in everyday life (L199, L201).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L381. minor (1–4): Kap 37's concept: ordered systems (Negentropie) counter the general tendency toward chaos (L381).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L229, L349, L359, L369, L379, L389, … (7 lines). minor (1–4): Kap 22: the presence of „des unkontrollierten Potentialmeers“ as the simulated reality destabilises (L229); Kap 34 „Exodus ins Potential“: Kael/M steps into „die Weite des Potentialmeers“ (L349); Kap 35 and 39 set Kael/M and Juna there (L359, L399).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L351. not read: an occurrence — „(Simulation)“ in Kap 34's concept line, which names a person (L351).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `alternatives Kohärenzprotokoll` (near `koharenz`), `Echo der Kohärenz` (near `koharenz`). occurrences: `alternatives Kohärenzprotokoll` (read on aegis) and the title `Echo der Kohärenz`.
- `therapie-schnittstelle-alpha`: `Alpha` (near `therapieschnittstellealpha`). an occurrence: `Alpha` stands in `Fragment Alpha`, not the therapy interface.
- `ueberwelt`: `B-Welt-Simulation` (near `simulation`), `Simulationsgrenze` (near `simulation`), `Simulationstheorie` (near `simulation`). occurrences: `B-Welt-Simulation`, `Simulationsgrenze` and `Simulationstheorie` name a world, a border and a borrowed theory.


**Record entries** (one file each, formatted as earlier entries — `ls Plan/runs/ingest-43*/readings/q7-*`, `ls Plan/runs/ingest-42*/readings/q8-*`):
- **`q7-what-734-names`**: in Kap 24 AEGIS analyses the recurring activation of „des Kern-Trauma-Fragments T-734“ in Kael and tries to decode it without understanding it (L250) — a trauma fragment; a plan, recorded, not applied; no detail of the symbol.
- **`q8-aegis-after-the-vortex`**: Kap 33: AEGIS collapses under unsolvable paradoxes or failed autopoiesis (L339, L340 — describe around the name); Kap 34: „(Nicht mehr existent oder nur noch als passive Datenreste)“ (L350); from Kap 35 „(Irrelevant)“.

**Chapter readings** (batch `ingest-431-kap`, one file per chapter, `Plan/runs/ingest-431-kap/readings/kap-NN--kohaerenz-protokoll-kapitelstruktur-mit-konzepten-39-kapitel.md`, Kap 1 to Kap 39, formatted as the files in `Plan/runs/ingest-422-kap/readings/`): the chapter's title in backticks (heading at L15 + 10·(N−1)) and what it plans, one bullet with one or two quotations from its narrator or AEGIS line (four and five lines below the heading). Never quote a concept line that names a person. Kap 24: the Kernwunde, no detail.

**Not promoted:** Kael/M, Kael-Self_Integrator, Fragment Alpha, K-J Vektor-Signatur, Controlled Fragmentation Protocol, Stress-Test Delta-7, Kern-Trauma-Fragment, the world codes, B-Welt, Jetzt-Raum, Inner Garden, Wächterin, the chapter titles, and the borrowed concepts.

**One reader**: every page above, the two record entries and the 39 chapter readings.
