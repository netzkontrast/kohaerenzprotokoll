# Brief — readings from document 147 (step 6)

1 document, one reader, one batch: `ingest-147`. Files go to `Plan/runs/ingest-147/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 147 | `projektplanung-fuer-kohaerenz-protokoll` | 2025-12-05 | „the planning report“ (titled `Projektplanung für Kohärenz Protokoll`) | a German planning report proposing a „Maximal-Plotter“ workflow (Notion/Obsidian, Scrivener, meta-prompting) for the novel: the K₁/K₀ ontology as database tags, the four Kernwelten as writing-rule containers, System Kael as a Systemkarte, a three-phase Gravitations-Architektur for 39 stories mapped onto Hamilton's 40-chapter model, a table of open plot questions; it calls itself a proposal (L19) and restates other documents by reference number |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (419 lines for `projektplanung-fuer-kohaerenz-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A planning report proposes a workflow: write „the planning report proposes / assigns …“. What it restates from a numbered source (Writer's Bible, Agentive Narrative …) is that source's claim as the report renders it — say so. Its „Ch N“ are chapters of Hamilton's 40-Chapter Plot Module, not Kaps of the novel — never map them. German — quote as written; cut quotations before inner quotes and before reference digits glued to a word; `K₁`/`K₀` in backticks.

## Pages — document 147, `projektplanung-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L42, L44, L47, L138, L166, … (18 lines). minor (1–2): Lex „der natürliche Verbündete von AEGIS“ (L138); the open-question row: a slot for AEGIS's perspective as log entries, „AEGIS wird tragisch“ (L359); AEGIS cannot see the Moonshine-Link (L361).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L81. minor (1–2): the aggressive defence of KW3, „(Nyx, Alex)“ (L81).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L119. minor (1–2): section 3.2's analysis of the alters and their conflicts (L119–L147), profiles taken from the Writer's Bible (L121); who fronts in a scene (L107).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L112, L117. minor (1–2): Argus as co-conscious observer, „(z.B. Argus, Kael)“ (L112).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L29. minor (1–2): the „Dual Kernel Theory“ (DKT) of Kohärenz (K₁) and Kollaps (K₀) as „der physikalische Motor der Welt“ (L29); the ontology table (L42–L45).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L87. occurrence: KW4's container label (L87) — see the sweep.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L166. occurrence: inside a sample prompt (L166) — see the sweep.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L198, L362, L378. minor (1–2): the resolution row: the stories must prepare that Kael becomes a paradox, AEGIS's axioms established first (L362).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L21, L44, L91, L185, L215, L217, … (8 lines). minor (1–2): Juna/V break reality in the Riss-Zone (L44); the „Juna-Verbindung“ in KW4 (L91) and its total collapse in the Hamilton mapping (L217).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L44, L99, L111, L112, … (15 lines). central (2–4): „System Kael“, a system of ANP and EP after the TSDP (L99); the Systemkarte instead of a character sheet (L103); Kael as host who denies the others (L123–L128); Kael becoming a paradox (L362).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L49, L51, L185, L199, L295, L342. central (2–4): the four Kernwelten as „externalisierte psychologische Zustände des Protagonisten Systems“ (L51); each a container with a writing rule — Logos-Prime „Keine Metaphern. Reine Deskription.“ (L62), Mnemosyne-Archipel (L67), Cerberus-Labyrinth (L77), Kairos-Potentialis (L87–L92).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L71, L114, L147, L151, L156, L191, … (8 lines). minor (1–2): an EP of KW2 (L71); „Kiko (EP - Freeze/Child)“, bearer of the trauma (L150–L153).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L21, L29, L166, L298, … (15 lines). central (2–4): Kohärenz (K₁) against Kollaps (K₀) (L29); K₁ places of maximal order (L42); the Integraler Status, simultaneity of K₁ and K₀ (L45); the pacing rule against too long in K₁ (L47); AEGIS's „Kohärenz durch Negation“ (L166).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L61, L111, L114, L117, L132, L138, … (14 lines). central (2–4): „Lex (ANP - Rationalist)“ (L135), „der natürliche Verbündete von AEGIS“ (L138), the conflict to escalate in Phase II (L138).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L71. minor (1–2): an EP of KW2, „(Kiko, Lia)“ (L71).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L217. minor (1–2): part of the Mnemosyne-Archipel falls into the Nichts-Rauschen (L230); an important place destroyed in the Hamilton mapping (L217).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L361, L379. minor (1–2): the catalyst row: define it under Quantenverschränkung/Prehension, and show „dass AEGIS diesen Link nicht sehen kann“ (L361).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L45. minor (1–2): the Integraler Status, „funktionalen Multiplizität“ and integration (L45).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L43, L230. minor (1–2): „Ein Teil des Mnemosyne-Archipels stürzt ins Nichts-Rauschen“ (L230), an irreversible cost.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L81, L111, L117, L142, L147, L167, … (11 lines). central (2–4): „Nyx (EP - Fight)“ (L144), „Nyx hasst Lex für dessen Passivität und Kiko für deren Angst“ (L147); aggressive defence in KW3 (L81).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L19. occurrence: „Risse“ in the narrative (L19) — see the sweep.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L359. minor (1–2): in the antagonist row with the Genesis-Krise (L359).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L97, L99, L114, L270, L307, … (7 lines). minor (1–2): System Kael based on the Theorie der Strukturellen Dissoziation der Persönlichkeit (TSDP) (L99).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L298. occurrence: `Simulation` names a writing method (L298) — see the sweep.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world name, read on kern-welten.
- `genesis`: `Genesis-Krise` (near `genesis`). a reading only if the reader finds more than the question „Was ist die Genesis-Krise“ (L359); else occurrence.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the world name, read on kern-welten.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: Kollaps (K₀) is the principle, read on kohaerenz and dkt.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the world name, read on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). a reading — on mnemosyne above.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — on multiplizitaet above.


**Record entries** (one file each):

- **`c14-aegis-first-person-chapter`**: a story slot „Voices from the Machine“ for AEGIS's perspective as log entries (L359); dated 2025-12-05.
- **`q9-moonshine-link-boundary`**: AEGIS cannot see the link; to be defined under Quantenverschränkung/Prehension (L361).

**Not promoted:** Maximal-Plotter, Mosaik-Struktur, Gravitations-Architektur (Ergosphäre, Ereignishorizont, Singularität), Irreversible Kosten, Riss-Zone, Integraler Status, Enforcer, Systemkarte, the Hamilton mapping, the workflow and tool vocabulary (LeanRAG, Meta-Prompting, Chain-of-Density, P-SYS …), borrowed models (Save the Cat, Hero's Journey, Hamartia, Autopoiesis).

**Chapters:** none — its „Ch N“ are Hamilton's model chapters, not the novel's.

**Two readers**, disjoint: (1) kael, lex, nyx, kiko, lia, alex, argus, alters, tsdp, juna and the record q9; (2) aegis, kohaerenz, dkt, kern-welten, mnemosyne, nichts-rauschen, multiplizitaet, goedel-gambit, moonshine-link, trennungsprotokoll and the record c14.
