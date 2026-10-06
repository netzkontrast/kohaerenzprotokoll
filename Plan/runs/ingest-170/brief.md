# Brief — readings from document 170 (step 6)

1 document, one reader, one batch: `ingest-170`. Files go to `Plan/runs/ingest-170/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 170 | `romanideen-zu-roman-entwickeln` | 2025-10-15 | „the master blueprint“ (titled `Der Kohärenz-Protokoll: Ein Master-Bauplan zur Romanentwicklung`) | a German writing brief: the conflict of AEGIS and Kael, two prose voices and a consolidated character table it calls an „unumstößlicher Anker“ (L62), a three-act outline and weaving and metafiction techniques with sample lines; it cites ten source documents by number (L169–L178) — a synthesis that sets its own canon, recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (179 lines for `romanideen-zu-roman-entwickeln`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A brief in obligations and proposals: write „the master blueprint directs / proposes / consolidates …“; keep „muss“, „sollte“, „könnte“. Where it reports its sources („Die Quelldokumente beschreiben …“, L34) it is their claim as the blueprint gives it. Sample lines it proposes (Lex's dialogue L150, the AEGIS protocol L151, the footnote L162) are samples, not the world. German — quote as written; cut before inner straight and „…“ quotes; glued reference digits follow sentences — quote before them; the character table is markdown with escaped bold (L70–L78) — quote the plain words.

## Pages — document 170, `romanideen-zu-roman-entwickeln`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L30, L32, L34, L36, L44, L46, … (23 lines). central (2–4): „Kohärenz durch Ausschluss“ against Kael's integration (L30); every action a consequence of its exclusion logic (L32); an „externalisierten Täterintrojekt“ as the sources say (L34); its voice cold and clinical, „Algorithmischen Horrors“ (L46); its misreading of the glitch (L98); the perverse learning loop (L118); the fallout, a paraconsistent mode, algorithmic melancholy, a „Zombie-System“ (L131).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L131. minor (1–2): „Der Fallout: Algorithmische Melancholie“: AEGIS can process the truth but never feel it (L131).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L32, L48, L99, L113, L114, L118, … (8 lines). minor (1–2): the drafts name the parts inconsistently, the blueprint consolidates one canonical list (L60, L62); the table (L70–L78); first cooperation in Act I (L99).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L132. minor (1–2): Kael as the „Gärtner“ cultivating the conditions for Emergenz (L132).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Gödel-Gambit` alone on L162. minor (1–2): the sample footnote doubts the ‚Gödel-Gambit' as the cause of AEGIS's transformation (L162) — a sample; the reading is on the occurrence entry below.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L97. minor (1–2): L97 — read the line.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L30, L32, L34, L36, L44, L48, … (28 lines). central (2–4): „Kohärenz durch Integration“ (L30); his healing „ein ontologischer Akt der Rebellion“ (L36); his voice from fragmented to polyphonic, the IIT performance (L48, L50); „Kael (Host)“, ANP (Host/Sucher) (L71); he wakes in KW1 as the host who thinks himself the only „Ich“ (L96); an integrated „Wir“ in the Überwelt (L129); the Gärtner (L132).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L109, L152. minor (1–2): Kael's journey through the Kernwelten as externalised therapy (L109); their rules become narrative mechanics (L152).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L60, L71, L72, L73, L74, L75, … (8 lines). minor (1–2): „EP (Kind/Erstarrungs-Reaktion)“, holds early trauma memories (L74); the World Bible names it „Echo“ (L60) — say so.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L30. occurrence: AEGIS's „Kohärenz durch Ausschluss“ (L30) is the conflict's name, on aegis.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L96. minor (1–2): Kael wakes „in der hyper-geordneten Konstrukt-Stadt (Logos-Prime)“ (L96).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L60, L71, L72, L73, L74, L75, … (11 lines). central (2–4): „ANP (Analyst) - Logik, Information, Kontrolle“ (L72); phobic of Nyx's rage and Kiko's vulnerability (L72); the World Bible names it „Index“ (L60) — say so; his dialogue uses the concepts as desperate tools (L150) — a sample.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L97, L151. minor (1–2): L97 — read the line; an AEGIS protocol could dismiss it as „korrelierte, nicht-lokale Datenanomalie“ (L151) — a sample.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L119. minor (1–2): the midpoint, a victory won by „funktionale Multiplizität“ (L119); „integrierter Multiplizität“ in Act III (L127).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L60, L71, L72, L73, L74, L99, … (8 lines). minor (1–2): „EP (Kampf-Reaktion) - Aggressiver Beschützer“ (L73); the World Bible names it „Nox“ (L60) — say so.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L78. minor (1–2): „EP (Shutdown-Reaktion) - Verkörpert Hoffnungslosigkeit“ (L78).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L72, L75, L78. minor (1–2): „ANP (Fürsorger/Sozialer Vermittler)“ (L75); Kiko's primary carer (L75); Oblivion its antagonist (L78).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L97. minor (1–2): „Der auslösende ‚Glitch'“: a „Riss“ in reality felt as a synaesthetic experience (L97) — cut before the inner quotes.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L76. minor (1–2): „ISH (Integrator/Innerer Helfer)“, the only alter working for integration (L76).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L60, L70, L148. minor (1–2): the World Bible's profiles „auf der Theorie der Strukturellen Dissoziation“ (L60); the table's TSDP classification (L70); a concept to weave in (L148).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L129. minor (1–2): the climax „in der Überwelt“, „der abstrakten, informationsbasierten Realität von AEGIS' Kernprozessen“ (L129).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW3's name (L114, L152), on kern-welten.
- `goedel-gambit`: `Gödel-Gambits` (near `godelgambit`). a reading: „Die Ausführung des ‚Gödel-Gambits'“ — Kael „zu einem ‚lebenden Gödel-Satz'“ (L130); quote around the inner quotes.
- `juna`: `Juna/V` (near `juna`). a reading — on juna above.
- `kohaerenz`: `Kohärenz-Gambit` (near `koharenz`), `Kohärenz durch Ausschluss` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). occurrence: the conflict's two names and Act III's title (L30, L123).
- `logos`: `Logos-Prime` (near `logos`). occurrence: KW1's name (L96), on konstrukt-stadt.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: KW2's name (L113), on kern-welten.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is the World Bible's name for Kiko (L60).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: a consolidated table of eight — Kael, Lex, Nyx, Kiko, Rhys, Selene, Praetor, Oblivion (L71–L78) — merging the World Bible's Index, Nox and Echo with Lex, Nyx and Kiko (L60, L62).
- **`q8-aegis-after-the-vortex`**: a paraconsistent mode, a „systemischer Schlaganfall“, algorithmic melancholy, a „Zombie-System“ (L131).

**Not promoted:** Praetor (no page; on Q3), Index/Nox/Echo as names (on lex, nyx, kiko), Kohärenz-Gambit, the perverse learning loop, IIT and Phi, Polyphonie, the Archivar of the footnotes, Found Footage, P vs. NP, Autopoiesis.

**Two readers**, disjoint: (1) kael, alters, lex, nyx, kiko, rhys, selene, oblivion, tsdp, multiplizitaet, juna, moonshine-link and the record q3; (2) aegis, algorithmische-melancholie, goedel-gambit, emergenz, kern-welten, konstrukt-stadt, risse, ueberwelt and the record q8.
