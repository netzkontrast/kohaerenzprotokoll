# Brief — readings from document 431 (step 6)

1 document, one reader, one batch: `ingest-432`. Files go to `Plan/runs/ingest-432/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 431 | `monstergruppe-primzahlen-plot-neukonstruktion` | 2025-04-26 | „the prime-number blueprint“ (an unsigned German plot blueprint joining the Monster group and a prime-number metaphor) | a framework table, then 39 chapters/beats in three acts — Kap 1–5 and 39 singly, the rest in ranges — each with the same fields; the prime-number metaphor kept for AEGIS's reductionism alone; calls itself final and its frame definitive (L15, L23), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (243 lines for `monstergruppe-primzahlen-plot-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the prime-number blueprint plans …“ or „the prime-number blueprint's Kap 4 …“. It names Kap 1–5 (L42, L52, L63, L73, L84) and Kap 39 (L184) singly and Kap 6–38 only in ranges (L94, L104, L119, L130, L140, L154, L164, L174) — a range is never a single chapter. Its AEGIS log lines are sample text. Quote the German as written; cut before straight and single quotes, bold markers and glued footnote digits. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name.

## Pages — document 431, `monstergruppe-primzahlen-plot-neukonstruktion`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L32, L33, L34, … (75 lines). central (4–8): the table: AEGIS „als Wächter-KI (Existenz durch Negation)“, fragile, seeking stability, simulating realities as analysis tools (L32); the prime-number metaphor reserved for AEGIS's analytic reductionism and its failure (L36); Kap 2 AEGIS's nature as guardian AI and the metaphor introduced (L54); Kap 4 the simulation as defence and analysis tool (L75); Kap 5 the failure of reductionism (L86); Kap 31–35: AEGIS created from/by the Potentialmeer as a defence mechanism (L167); Kap 36–38: AEGIS's final state (L176).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L99, L122. minor (1–4): Kap 6–10: Kael relies on emerging fragments ('Alters') — cut before the single quotes (L99); Kap 14–17: Kael interacts consciously with the fragments (Alters) and learns their abilities (L122).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L34, L78, L227. minor (1–4): the table: Kael's fragmentation „(DID-analog)“ as reaction to AEGIS's attempts at decomposition (L34).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L19. not read: an occurrence — „Paradoxon/Emergenz“ as Act 2's label (L19).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L35, L107, L146, L187. minor (1–4): Kap 11–13: a brief non-local contact through the K-J connection, perhaps with Juna (L107); the climax: coordination with Juna „(falls vorhanden)“ (L146); Kap 39: „potenziell Juna“ (L187) — Juna's presence is hedged throughout.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L33, L34, L35, L36, L40, L45, … (75 lines). central (4–8): the table: protagonist whose core structure resonates with the M foundation, fragmentation (DID-analogous) as reaction to AEGIS's attempts at decomposition (L34); Kap 1 Kael's „normalen“ life in a Kernwelt controlled by AEGIS and the first glitch (L45); Kap 6–10 Kael relies on emerging fragments (L99); Kap 14–17 Kael works with the fragments consciously (L122); Kap 31–35 Kael learns AEGIS's origins (L167); Kap 39 Kael (and potentially Juna) find a way to exist in the stabilised M reality (L187).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L45. minor (1–4): Kap 1: Kael's „normalen“ life „innerhalb einer von AEGIS kontrollierten Kernwelt“ (L45) — the one mention.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11, L15) and Kap 39's title „Coda: Kohärenz“.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L19, L32, L164, L166, L167, L168, … (8 lines). minor (1–4): the table: the Potentialmeer as „Prä-reales Substrat“ (L32); the cracks and the potentiality of the Potentialmeer in Act 2 (L19); Kap 31–35: AEGIS created from/by the Potentialmeer as a defence mechanism, an attempt to tame its potentiality by simulation (L166, L167); cosmic horror of the Potentialmeer (L172).
- **`risse`** (minor, 1–4): the census's surfaces — `Der Glitch` L42, L46. minor (1–4): Kap 1: „Der Glitch ist der erste Riss“, a moment's flicker where the deeper M structure shows (L46); AEGIS's log watches for structural fault lines, 'Faktorisierungsrisse' (L80); the cracks in the simulated reality (L19).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L15. minor (1–4): the M structure as the framework (OS/physics) of the simulation (L33); AEGIS's simulation as defence and analysis tool (Kap 4, L75); AEGIS tried to tame potentiality by simulation (L167).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Coda: Kohärenz` (near `koharenz`). occurrences: the title and Kap 39's title.


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–3): the table: the K-J connection as „Emergente Signatur tiefer M-Symmetrien“, sub-protocol/non-local, Kael's anchor (L35); the climax: the K-J connection (Moonshine signature) shields Kael or enables coordination with Juna (L146).

**Record entries:** none.

**Chapter readings** (batch `ingest-432-kap`, one file per chapter, `Plan/runs/ingest-432-kap/readings/kap-NN--monstergruppe-primzahlen-plot-neukonstruktion.md`, formatted as the files in `Plan/runs/ingest-422-kap/readings/`): Kap 1 (L42), 2 (L52), 3 (L63), 4 (L73), 5 (L84) and 39 (L184) only — the chapter's title in backticks and what it plans, one bullet with one or two quotations from its own block. The ranges get no file.

**Not promoted:** Monstergruppe (M) als Fundament, M-Substrat, Primzahl-Metapher, K-J Verbindung (Moonshine-Signatur), Kael-Entität, Sandbox, Protokoll Omega, Eindämmungsprotokoll K-Alpha, Primzahl-Gitter, Faktorisierungsrisse, Nebenfigur, the chapter titles, the field labels and the borrowed concepts.

**One reader**: every page above and the six chapter readings.
