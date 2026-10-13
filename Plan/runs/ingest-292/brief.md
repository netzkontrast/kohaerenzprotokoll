# Brief — readings from document 291 (step 6)

1 document, one reader, one batch: `ingest-292`. Files go to `Plan/runs/ingest-292/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 291 | `roman-kapitel-ausformulierung-kohaerenz-protokoll` | 2025-04-18 | „the chapter-1 guide“ (an unsigned German guide to writing the first chapter of Teil 1) | a plan-voice guide to Teil 1, Kapitel 1: pillars on the Konstrukt-Stadt (KW1) and Kael, a beat-by-beat table 1.1a–1.15c, a section on Juna, and sections on perception, pacing, symbols and recommendations, pointing in brackets to other texts it does not contain; it calls itself an „Anleitung“ (L15) and a „Checkliste“ (L48) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (140 lines for `roman-kapitel-ausformulierung-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide: write „the chapter-1 guide wants / prescribes …“; what it says of Kael, Juna and the city is prescription for the chapter, not an event. The table ties intrusions to figures only in parentheses with a question mark — keep the hedge. Bracketed pointers (`[Kontext §4]`, `[41-153]` …) report other texts: never quote their content as this document's. Cut quotations around digits glued to words (`KW1`, `24 Beats`).

## Pages — document 291, `roman-kapitel-ausformulierung-kohaerenz-protokoll`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L25, L62, L81. minor (1–3): named with LogOS as the systems whose presence shows in the city's order, the city a monitoring mechanism (L25); L62, L81 only if they add.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L15, L31, L135. minor (1–3): Kael after the reboot „ohne bewusstes Wissen über seine DID oder die Simulation“ (L31); the „dissoziative Identitätsstruktur“ the chapter is to show (L15).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L55, L56, L68, L70, L79, L81, … (9 lines). central (3–6): „Das Juna-Enigma“ (L79): the cause of her distance to be kept deliberately ambivalent, offered as four options in a question (L81); her dialogue „ein abgespultes Protokoll“ (L55); a remote check-in (L68); she embodies the chapter's central question (L90).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L24, L27, L29, L31, … (48 lines). central (3–6): „der zentrale Wahrnehmungsfilter des Kapitels“ (L31), disoriented after the reboot and unaware of his DID or the simulation (L31); three kinds of inner intrusion — emotional floods, perceptual distortions, fragmented thoughts (L33–L39); a dominant personality „(Host/Architekt)“ undefined (L39); the core as contrast between cold outer reality and inner experience (L43); the hedged voice, close third person (L133).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the title `Kohärenz Protokoll`.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L15, L19, L21, L76, L81. central (3–6): more than a backdrop, a mirror of Kael's state and a subtle antagonist (L21); pure logic and order (L23); sterility and sensory deprivation (L24); a monitoring mechanism (L25); placed after the `UNIVERSAL REBOOT` (L21); its depiction deconstructs the illusion of stability (L129).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L25, L62, L81. minor (1–3): named with AEGIS as the systems whose presence shows in the city's order (L25); L62, L81 only if they add.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L76. minor (1–3): only if L76 places it (a table row); else not read.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L38, L58, L63, L88, L108, L110, … (9 lines). central (3–6): the first rift as a glitch, to be described as fleeting and ambiguous, real or not left open (L58); a stronger anomaly (L63); the cryptic command „Finde die Naht / Den Riss“ (L74), introduced as a cryptic instruction (L121); glitch and anomaly as symptoms of a faulty reality (L123).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L37, L56, L70. minor (1–3): an intrusion tied to Silas only in parentheses with a question mark, „Echo von Silas“ (L56); L37, L70 only if they add.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L31. not read: occurrence — `Simulation` (L31) is Kael's unawareness of it, read on kael.

- **`alters`** (minor, 1–3): the figures the table ties to intrusions only in parentheses with a question mark — Silas, Praetor, Nox, Limina, Echo, Index, „Hinweis auf Alter“ (L56, L64, L69); fear „assoziiert mit Praetor, Nox“ without a question mark (L37); none defined, all used as known. Keep the hedge.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is a symbol of the chapter (L63, L123), read on risse.
- `alters`: `Alter` (near `alters`). a reading — see the extra page below.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is Kael's „(Host/Architekt)“ (L39), read on kael.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is a perceptual symptom, not a persona.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` names a figure tied to an intrusion (L56, L64), read on alters.


**Record entries:** none.

**Not promoted:** KW1 and KW4 as labels, the UNIVERSAL REBOOT, Praetor, Nox, Limina, Index, Funke, Jansen, the Normalem Nachbarn, Gewohnte Welt and Perfect World, Der klare Hinweis, the Naht, the Spiegel, the Beat as a unit, Gamma-7, and the borrowed terms (Dissoziation, Derealisation, Depersonalisation, Uncanny Valley, Stream of Consciousness, Cliffhanger, Synästhesie, Show, Don't Tell).

**One reader**: every page above and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-292-kap/readings/kap-01--roman-kapitel-ausformulierung-kohaerenz-protokoll.md`): Kap 1 — the guide to Teil 1, Kapitel 1 (L11, L15): the four phases „Etablierung → Erste Risse → Eskalation → Fragmentierung“ (L104); the beat table (L46–L77), whose stated `24 Beats` (L48) and 25 rows differ — say so; the closing image of a broken mirror (L77) and a cliffhanger (L129). A guide, not the chapter.
