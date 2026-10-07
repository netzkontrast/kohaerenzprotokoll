# Brief — readings from document 189 (step 6)

1 document, one reader, one batch: `ingest-189`. Files go to `Plan/runs/ingest-189/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 189 | `analyse-des-kohaerenz-protokolls` | 2025-11-28 | „the protocol analysis“ (titled `Analyse des Kohärenz-Protokolls`) | a German research report in ten sections that analyses AEGIS, the Potentialmeer, the Genesis-Krise and the Ursprungs-Ich, the Kohärenz-Protokoll read as MESI cache invalidation and as tertiary structural dissociation, the four Kernwelten, Agnotologie and the Gödel-Gambit; section 8 is questions in AEGIS's voice, section 9 an English system prompt (L305–L359) — it says the protocol „ist keine metaphorische Umschreibung“ (L191), recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (435 lines for `analyse-des-kohaerenz-protokol`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that reports its sources: write „the protocol analysis reads / reports …“; a sentence opening „Die Dokumente …“ or carrying a glued reference number reports that source; section 8 is AEGIS's imagined voice and section 9 (English) a prompt — say so when you quote them. German — quote as written; cut before inner quotes and glued reference digits; the tables have escaped bold — quote the plain words; never quote across `$…$` formulas.

## Pages — document 189, `analyse-des-kohaerenz-protokolls`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L24, L26, L36, L60, L68, … (58 lines). central (2–4): „ein hyper-rationales, autopoietisches System“ with two expansions of its name (L24); its identity definition quoted from a source, „Aegis ist, was Aegis verhindert, dass es nicht ist.“ (L108); a first-order observer that does not see it is part of the system (L132); the Ursprungs-Ich integrated in it before the crisis (L163); the protocol split the ANP (AEGIS) from the EP (Kael) (L221); not evil but caught in an autopoietic paradox (L369).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L221, L229, L235, L237, L341. minor (1–2): Kael's EP shattered into Alters, „wie Nyx, Kiko, Moros“ (L221) — cut before or after the names; the Kernwelten made to hold the isolated fragments (L229).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L88. occurrence: `Emergenz` stands in KW4's table cell and in a phrase of the sources (L88, L239) — the general word.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L24. minor (1–2): the Potentialmeer as maximal entropy (L52) and as a heat bath (L68); AEGIS's existence against the entropic pull (L24).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L26, L263, L269. central (2–4): „Der finale Zusammenbruch des Systems wird durch das sogenannte“ Gödel-Gambit triggered (L269) — cut before the inner quotes; Kael reaches functional multiplicity and becomes unprovable by AEGIS's axioms (L269); the living Gödel statement and AEGIS's fatal recursion (L271).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L163, L267, L287, L339, L369, L387, … (7 lines). minor (1–2): the external entity named „Entität M“, Juna/V or Das Fundament (L163) — quote around the names; AEGIS must negate the Other (Juna), which was already part of its own Ursprungs-Ich (L369).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L132, L145, L219, L221, L229, … (18 lines). central (2–4): at once part and enemy of the system (L145); the EP split from the ANP (AEGIS) by the protocol (L221); in KW1 with Index (L236); he reaches functional multiplicity in the Gödel-Gambit (L269); the Ursprungs-Ich as Kael in the conclusion (L369); the structural dissociation into Kael and AEGIS (L371).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L145, L225, L229, L231. central (2–4): AEGIS created the Kernwelten to hold Kael's fragments and analyse the resonance patterns (L229); „Das System umfasst vier primäre Kernwelten“ (L231); the table: KW1 Logos-Prime (Die Konstruktstadt) to KW4 Kairos-Potentialis (Garten der Möglichkeiten), each with a logic and inhabitants (L236–L239) — quote the plain words.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L221. minor (1–2): among the fragments of the EP, with Nyx and Moros (L221).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L22. occurrence: the project's name in the report's title and opening (L22).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Die Konstruktstadt` L236. minor (1–2): KW1 Logos-Prime „(Die Konstruktstadt)“, a sterile world of perfect geometry, classical logic (L236) — quote the plain words.
- **`logos`** (minor, 1–4): the census's surfaces — `Logos` L218, L236, L341. minor (1–2): the ANP's row: „AEGIS / Logos-Prime“, defined by Logos (L218) — quote the plain words; Logos-Prime is KW1 (L236), J49.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L341. minor (1–2): KW2 Mnemosyne-Archipel, paraconsistent logic, trauma and memory (L237); a simulation where 734's shards were imprisoned, in the English prompt (L341).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L176, L180, L203, L267, L373. central (2–4): the Ursprungs-Ich's resonance with the anomaly: „Diese Verbindung wird im Roman als“ Moonshine-Link named (L176) — cut before the inner quotes; its objective, integration by resonance (L180); detected by the system's bus snooping (L203).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L221. minor (1–2): among the fragments of the EP, with Nyx and Kiko (L221).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L269. minor (1–2): Kael reaches „einen Zustand der Funktionalen Multiplizität“, integration without fusion (L269).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L68. minor (1–2): every ordered structure, „(Negentropie)“, faces the Potentialmeer's gradient (L68).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L44. minor (1–2): the substrate's names reported from the sources — Potentialmeer, Die Leere, Nichts Rauschen (L44).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L221. minor (1–2): among the fragments of the EP, with Kiko and Moros (L221).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L26, L40, L44, L52, L60, L68, … (10 lines). central (2–4): „ein dynamisches Feld reiner, unstrukturierter informationeller Potentialität“ (L44); maximal Shannon entropy (L52); all information in chaotic superposition, white noise (L60); a heat bath of infinite temperature (L68).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Die Resonanzlandschaft` L237. minor (1–2): KW2 Mnemosyne-Archipel „(Die Resonanzlandschaft)“, a fluid world shaped by emotion where the Risse break open (L237) — quote the plain words.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L237, L241, L371, L428. central (2–4): „Die“ Risse „(Glitches) in diesen Welten sind keine Grafikfehler“ but ontological leaks where the EP's truth breaks into the ANP's world (L241) — cut around the inner quotes; they break open in KW2 (L237).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L26, L209, L213, L217. minor (1–2): the protocol read through structural dissociation (L26, L209–L217); a „tertiären Dissoziation“ (L221).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L28. occurrence: „die Simulation absoluter Notwendigkeit“ (L28) is Sartre's bad faith in the report's thesis, nothing of the Überwelt.

**Pages the census reaches by another surface** (read them too):

- **`genesis`**: central (2–4): the Genesis-Krise, „auch bezeichnet als“ Der große Wandel, Perturbation aus der Leere or Ur-Trauma (L155) — quote around the names; the moment the paradox went into practice, structural dissociation into Kael and AEGIS (L371).
- **`komponente-734`**: minor (1–2): in the English prompt, „734 was your Origin-Self“ that touched the Void Entity (M/Juna) (L339); shattered into shards (Alters) and imprisoned in simulations (L341) — say it is the prompt's account, in AEGIS's address.
- **`algorithmische-melancholie`**: minor (1–2): „Diese Strategie führt jedoch zu einer“ Algorithmische Melancholie: AEGIS manages contradictions but never resolves them, Gnosis without Noesis (L147) — cut before the inner quotes.
- **`aegis-teilfunktionen`**: minor (1–2): the second expansion of AEGIS, „Autonomous Entropic Gatekeeper for Integrity Systems“ (L24), J60 — quote the plain words.
- **`moeglichkeits-garten`**: minor (1–2): KW4 Kairos-Potentialis „(Garten der Möglichkeiten)“, J61, where contradictions coexist, with Limina (L239) — quote the plain words.
- **`grenzfeste`**: minor (1–2): KW3 Cerberus-Labyrinth „(Die Grenzfestung)“, an endless bunker complex with Praetor and Nox (L238) — quote the plain words.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW3's name (L238), on kern-welten and grenzfeste.
- `entropie`: `Sog der Entropie` (near `entropie`), `Shannon-Entropie` (near `entropie`). a reading — on entropie above (`Sog der Entropie` L68; `Shannon-Entropie` the borrowed measure).
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` is the Ursprungs-Ich's response (L176), read on moonshine-link — not the Entropie-Resonanz-Protokolle.
- `genesis`: `Genesis-Krise` (near `genesis`). a reading — on genesis below.
- `grosse-mauer`: `Mauer` (near `groemauer`), `Mauer` (near `groemauersystemgrenze`), `Mauer` (near `grossemauer`). occurrence: `Mauer` is a figure for AEGIS's firewall in section 7, not the Große Mauer.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: KW4's name (L239), on kern-welten and moeglichkeits-garten.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Projekt Kohärenz` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`). occurrence: the Protokoll's name and the project's; „Fehlausgerichtete Kohärenz“ (L183) is AEGIS's diagnosis, read on moonshine-link.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: KW2's name (L237), on kern-welten — and a reading on mnemosyne above.
- `multiplizitaet`: `Funktionalen Multiplizität` (near `multiplizitat`). a reading — on multiplizitaet above.


**Record entries** (one file each):

- **`c16-kael-origin`**: an Ursprungs-Ich integrated in AEGIS before the crisis (L163); the protocol split the ANP (AEGIS) from the EP (Kael) (L221); Kael as the Ursprungs-Ich in the conclusion (L369, L371); the prompt's „734 was your Origin-Self“ (L339).
- **`q3-how-many-kern-welten-and-alters`**: four primary Kernwelten (L231); the EP shattered into Alters such as Nyx, Kiko, Moros (L221); inhabitants Index, Praetor, Nox, Limina (L236–L239).
- **`q7-what-734-names`**: „734 was your Origin-Self“, shattered into shards (L339, L341) — the English prompt's account.
- **`q8-aegis-after-the-vortex`**: algorithmic melancholy (L147); the fatal recursion of the Gödel-Gambit (L271); transcendence, not defeat (L373).
- **`q9-moonshine-link-boundary`**: the link as the Ursprungs-Ich's resonance, detected by bus snooping (L176, L203).

**Not promoted:** MESI and cache invalidation, Agnotologie, the Heuristik der Negation, Mauvaise foi, the Monster-Symmetrie, Ursprungs-Ich and Entität M (on C16 and juna), Index, Praetor, Nox and Limina (no pages; on Q3), the English prompt's labels.

**Two readers**, disjoint: (1) kael, juna, moonshine-link, alters, nyx, kiko, moros, tsdp, multiplizitaet, genesis, komponente-734 and the records c16, q3, q7, q9; (2) aegis, aegis-teilfunktionen, algorithmische-melancholie, potentialmeer, nichts-rauschen, negentropie, entropie, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, logos, mnemosyne, risse, goedel-gambit and the record q8.
