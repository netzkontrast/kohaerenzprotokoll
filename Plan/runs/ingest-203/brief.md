# Brief — readings from document 203 (step 6)

1 document, one reader, one batch: `ingest-203`. Files go to `Plan/runs/ingest-203/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 203 | `romanentwurf-kohaerenz-protokoll-teil-1` | 2025-04-18 | „the chapter-1 draft“ (an unsigned working draft) | a German working draft for chapter 1 in three parts — research on narrative techniques, each ending in implications „für Konstrukt-Stadt & Michael“ (L19–L65); a 15-scene blueprint (L67–L203); a 15-scene prose sketch of Michael's day (L223 on) — with Michael and Julia, the earlier names of Kael and Juna; hedged throughout, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (376 lines for `romanentwurf-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A working draft: write „the chapter-1 draft proposes / sketches …“; the research part proposes, the blueprint plans, the prose sketch narrates — say which part a line is from. Its names are the early ones: Michael is read on kael (alias), Julia on juna — say so in the reading. Keep its question marks and hedges (`wahrscheinlich`, `könnte`, `(Cerberus-Intrusion?)`). German — quote as written; cut before glued footnote digits, `\[Kontext:` markers and inner straight quotes; the prose sketch's dialogue sits in straight quotes — quote only the narration around it.

## Pages — document 203, `romanentwurf-kohaerenz-protokoll-teil-1`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L27, L33, L39, L45, L61, L261. minor (1–3): the logic of the Konstrukt-Stadt as „die Logik von AEGIS und LogOS“, aimed at system stability (L27); the world operating on AEGIS logic, stability over humanity (L61); the supervisor's voice „ebenso neutral wie die von AEGIS“ (L261).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L49, L50, L51, L65, L216. central (3–8): intrusions of other parts, „Alters“, as foreign thoughts and feelings (L49); the intrusions pointing to the alters named in the context — „Mnemosyne, Cerberus, Kairos/Sophia, Architekt“ — logic to the Architekt, memory and sadness to Mnemosyne, fear and protection to Cerberus, insight and time to Kairos/Sophia (L51); the blueprint's field `Michaels Dominanter Zustand/Alter` — Host/Kern-Selbst (L75), Architekt (L115).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L51, L97, L147, L197. minor (1–3): Cerberus as one of Michael's alters, for fear, aggression and protective impulses (L51); the blueprint's hedged „(Cerberus-Intrusion?)“ (L197) — a question mark the reading keeps.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L33, L39, L47, L49, L62, L63, … (8 lines). minor (1–3): the intrusions of an unrecognised DID (L49); hints of unexpected emotion point to Michael's DID (L33); his amnesia about the reboot as a protective mechanism, „(oder von AEGIS initiiert?)“ (L39) — keep the question.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L21. minor (1–3): the Konstrukt-Stadt, the goal of Kern-Welt 1, actively suppressing „Chaos und Entropie“ after the reboot (L21) — cut before `\[Kontext`.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Julia` L27, L32, L44, L45, L64, L81, … (31 lines). central (3–8): Julia — the early name of Juna; read on juna as the alias and say so: her distance „distanziert/formal/unterkühlt“ may come from compulsion in the system, not coldness, „Ist sie unter AEGIS' Kontrolle?“ (L45) — a question; her formality as a mask (L45); in the prose sketch she is already at the counter, her voice „klar, melodisch, aber ohne Wärme“ (L233, L235) — quote the narration, not the dialogue.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Michael` L20, L21, L26, L27, L33, L38, … (97 lines). central (3–8): Michael — the early name of Kael (the page's alias); read as such: the absence of visible history mirrors „Michaels eigene Amnesie bezüglich des Reboots“ (L21); his amnesia as a protective mechanism (L39); the 15 scenes establish his „Gewohnte Welt“ (L69) — cut before the inner quotes; in the prose sketch the system confirms „Michael Einheit 734“ (L257); his waking (L229).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L51. minor (1–3): Kairos/Sophia as one alter of Michael's, for insights and temporal anomalies (L51).
- **`kern-welten`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kern-Welt` alone on L21. minor (1–3): the Konstrukt-Stadt as the goal of „Kern-Welt 1“, a space of rationality and order (L21).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); `Kohärenzalgorithmen` (L261) and `Harmonische Kohärenz` are the prose sketch's words, not the term.
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L21, L26, L27, L33, L39, L45, … (13 lines). central (3–8): its uncanny perfection as „eine direkte Manifestation der Kontrolle durch LogOS“ (L21); its logic is AEGIS's and LogOS's, not human (L27); Michael's minimalist, geometric Wohneinheit in it (L73); the transit corridor as „ein Wunderwerk der Geometrie“ (L251); the view on it from the unit (L193).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L21, L27, L60. minor (1–3): the Konstrukt-Stadt's perfection as control „durch LogOS“ (L21); the logic „von AEGIS und LogOS“ (L27); perfection as a sign of LogOS's control (L60).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L51, L65, L97, L127, L177, L187. minor (1–3): Mnemosyne as one of Michael's alters, for flashes of memory and sadness (L51); the blueprint's „(Möglicher Mnemosyne/Cerberus-Flicker?)“ (L97) — keep the question.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L32, L33, L62, L98, L273, L285. minor (1–3): these „Risse“ point to the simulation and to Michael's fragmentation (L33) — cut before the inner quotes, or quote the words after them; glitches as hints at the simulation (L33); read L273 or L285 for a glitch in the prose sketch.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L51. minor (1–3): Kairos/Sophia as one alter of Michael's (L51) — the same line as on kairos.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L32. occurrence: `Simulation` is the world's general nature as a simulation (L32, L33), nothing of the Überwelt.

- **`komponente-734`** (minor, 1–2): in the prose sketch the system confirms „Michael Einheit 734“ (L257) and the supervisor addresses him as „Einheit 734“ (L261) — 734 as Michael's own unit designation; quote the narration L257, the address sits in straight quotes.
- **`kaels-wohneinheit`** (minor, 1–2): Michael's „minimalistische, geometrische Wohneinheit in der Konstrukt-Stadt“ (L73); the prose sketch's room with sourceless light (L229).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is the general word.
- `kaels-wohneinheit`: `Wohneinheit` (near `kaelswohneinheit`), `Wohneinheit` (near `kaelswohneinheit10`). a reading — Michael's „minimalistische, geometrische Wohneinheit in der Konstrukt-Stadt“ (L73); see the extra page below.
- `kairos`: `Kairos/Sophia` (near `kairos`). read on kairos and sophia (L51).
- `kern-welten`: `Kern-Welt 1` (near `kernwelt`). read on kern-welten (L21).
- `kohaerenz`: `Kohärenzalgorithmen` (near `koharenz`), `Harmonische Kohärenz` (near `koharenz`). occurrences: words of the prose sketch's system.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is one of Michael's alters (L51), not the server architecture.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is the clinical symptom.
- `sophia`: `Kairos/Sophia` (near `sophia`). read on sophia (L51).


**Record entries** (one file each):

- **`q7-what-734-names`**: „Michael Einheit 734“ (L257) — here 734 is the protagonist's own unit number in the system, not an AEGIS antagonist unit.
- **`q3-how-many-kern-welten-and-alters`**: four alters named „Mnemosyne, Cerberus, Kairos/Sophia, Architekt“ (L51), besides the Host/Kern-Selbst (L75); the Konstrukt-Stadt as Kern-Welt 1 (L21) — names other documents give to Guardians, given here to alters.

**Not promoted:** the Architekt and the Host (on alters), Supervisor Einheit 12 and Einheit 451, Datenknotenpunkt Gamma-7, Sektor Delta-9, the music title, the narrative techniques (Uncanny Valley, Chekhov's Gun, Show, don't tell).

**Two readers**, disjoint: (1) kael, juna, alters, did, cerberus, mnemosyne, kairos, sophia and the record q3; (2) aegis, konstrukt-stadt, logos, kern-welten, entropie, risse, komponente-734, kaels-wohneinheit and the record q7.

**Chapter reading**: one, Kap 1, written by the session (`Plan/runs/ingest-203-kap/`).
