# Brief — readings from document 244 (step 6)

1 document, one reader, one batch: `ingest-244`. Files go to `Plan/runs/ingest-244/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 244 | `kapitel-1-generierungsprozess` | 2025-11-25 | „the chapter-1 report“ (a German report signed by an in-world analyst) | a report that sets out the Dual Kernel Theory and KW1, reads the rendering glitches as trauma symptoms, sets chapter 1 into itself in four sequences with commentary, and forecasts chapter 2; a draft and its analysis, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (668 lines for `kapitel-1-generierungsprozess`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Two voices: the report's commentary (write „the chapter-1 report reads …“) and the chapter text it sets in (write „in the chapter text the report quotes …“) — never the chapter as approved. The voice „Finde die Naht, Kael.“ (L564) has no speaker; do not name one. Chapter pages are written by the session (`Plan/runs/ingest-244-kap/`). `K\_1` and `K\_0` are escaped; cut before reference numbers glued to words.

## Pages — document 244, `kapitel-1-generierungsprozess`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L44, L47, L85, L134, L158, L438, … (9 lines). minor (1–4): „der antagonistische Systemverwalter“ (L47); the flicker as visual proof of AEGIS's inability (L85); spending massive energy to keep the room in K_1 (L158).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L647. not read: occurrence — `Emergenz` at L647 stands in a reference title.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L45. minor (1–4): the Kollaps-Kernel as the principle of entropy, extinction and irreversible computation (L45); rust as an entropic process (L472).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L13. not read: occurrence — `Genesis` at L13 is in the report's title.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L83, L84, L176, L210, L220, L228, … (10 lines). central (3–8): in the chapter text Juna in the doorway (L210) and „Der Zyklus beginnt“ (L228); the report's interaction line, Juna as projection/construct (L176); its two textures, „Juna ist sicher“ against „Juna ist ein Konstrukt“ (L83–L84).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L27, L44, L55, L57, L58, L107, … (57 lines). central (3–8): acting as ANP with amnesia about his traumatic past (L57); in the chapter text waking in his unit (L122, L128), the Vertex Explosion of his hands (L548); the voice „Finde die Naht, Kael.“ (L564) with no speaker; the forecast that he has left the Ergosphäre (L633).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L635. not read: occurrence — `Kairos` at L635 is cyclic, traumatic time against Chronos, not the Guardian.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: occurrence — the title (L13).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L44. minor (1–4): „Das Prinzip der Ordnung, Persistenz und reversiblen Berechnung.“ (L44), consciousness its subjective signature.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L45. minor (1–4): „Das Prinzip der Entropie, Auslöschung und irreversiblen Berechnung.“ (L45), exerting erosive pressure.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L37. minor (1–4): KW1, „auch bekannt als Konstrukt-Stadt oder Logos-Prime“ (L37); in the chapter text the city named Logos-Prime (L184).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L45. minor (1–4): „die „Leere“ (Moros)“ among the Kollaps-Kernel's manifestations in the table (L45); stands once, unexplained.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L47, L124, L156, L158, L621. minor (1–4): the absence of dust and smell as proof of active Negentropie (L158); Sterile Stille in the summary table (L621).
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L657. not read: occurrence — `Nexus` at L657 is a forum name in a reference.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L45, L462, L464, L480, L482, L562. minor (1–4): the wrath (Nyx) in the table (L45); the impulse as the breakthrough of an Emotional Part per TSDP, Nyx (night/wrath) (L482); in the chapter text „Wer war Nyx?“ (L464).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L29, L45, L68, L654; `Risse` L29, L45, L68. minor (1–4): the Risse in causality as Glitches (L29); the Glitches as precise indicators, not random errors (L68); Z-Fighting, Texture Stretching, Vertex Explosion as its kinds (L76, L93, L107).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L29, L55, L482. minor (1–4): the theory the analysis applies (L29); Kael as ANP (L55–L57); the EP breakthrough „gemäß TSDP“ (L482).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L23. not read: occurrence — `Simulation` at L23 is a section heading on the report's mandate.

- **`kern-welten`** (minor, 1–3): `Kernwelt 1 (KW1)` the system's starting state, also Konstrukt-Stadt or Logos-Prime (L37); in chapter 2 Kael may no longer be in the stable KW1 (L633).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). occurrence: `Genesis-Krise` stands once, unexplained.
- `kern-welten`: `Kernwelt 1 (KW1)` (near `kernwelt`), `Kernwelt 1` (near `kernwelt`). reading (J26): `Kernwelt 1 (KW1)` read on kern-welten — the starting state of the system, the stable KW1 Kael leaves (L37, L633).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Textur A (Kohärenz)` (near `koharenz`). occurrence: the title; `Textur A (Kohärenz)` the report's label for the simulation's lie (L83).
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` names the city, read on konstrukt-stadt, not LogOS.
- `personas`: `Depersonalisation` (near `persona`). occurrence: Depersonalisation is a symptom, not the Personas.


**Record entries** (one file each):

- **`c9-konstrukt-stadt-scale`**: KW1, „auch bekannt als Konstrukt-Stadt oder Logos-Prime“ (L37) — Konstrukt-Stadt as KW1.
- **`c10-knuckles-in-kap-1`**: in the chapter-1 text the report quotes, polygons break from Kael's knuckles in a Vertex Explosion (L548); no blood is written. A 2025-11 draft, not canon.

**Not promoted:** the Dual Kernel Theory's table, K_1/K_0, Z-Fighting, Texture Stretching, Vertex Explosion, Rost-Pixel, Sterile Stille, the black-hole zones (Ergosphäre, Ereignishorizont, Photonensphäre), Naht, Logos-Prime, the signing analyst.

**One reader**: kael, juna, aegis, nyx, moros, risse, tsdp, konstrukt-stadt, kern-welten, kohaerenz-kernel, kollaps-kernel, negentropie, entropie and the records c9, c10. Occurrences: emergenz, genesis, kairos, kohaerenz, nexus, ueberwelt.

**Chapter readings**: Kap 1 (L111, L122, L128, L548) and Kap 2 (L633), by the session (`Plan/runs/ingest-244-kap/`).
