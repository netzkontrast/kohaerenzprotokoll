# Brief — readings from document 164 (step 6)

1 document, one reader, one batch: `ingest-164`. Files go to `Plan/runs/ingest-164/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 164 | `romanidee-als-interaktiver-prototyp` | 2025-08-05 | „the CAVE prototype proposal“ (titled `Konzeptioneller Entwurf für einen interaktiven Roman-Prototyp`) | a German design proposal of 2025-08-05 for an interactive CAVE prototype of Act I: it first reports the novel's world from one reference (its glued `1`, „the outline“), then proposes a state-tracking Narrative Context Protocol (NCP) with a variable matrix, four chapter scenarios (Kap 1, 3, 7, 13) and sensory design; a proposal for a game, never the novel as written |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (303 lines for `romanidee-als-interaktiver-pro`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Two voices: Part I (to L134) reports the novel from its outline — „the prototype proposal reports, from its outline, …“; Parts II–IV propose game mechanics — „the prototype proposal plans, for the game, …“. A variable name (`Kael.System.Cohesion`, `AEGIS.System.Integrity`) is the game's state, never the world's; quote it in backticks, never as a reading of the term. Hedges („könnte“, „kann … modelliert werden“) stay. Cut before inner straight quotes; the glued reference digit `1` follows many sentences — quote before it.

## Pages — document 164, `romanidee-als-interaktiver-prototyp`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L30, L32, L34, L36, L44, … (38 lines). central (2–4): „eine autopoietische, informationsbasierte Intelligenz“ (L30); its tragic flaw, the „Paradoxon der Fehlausgerichteten Kohärenz“ (L32, L58); its genesis as traumatic fragmentation (L34); its architecture „eine systematisierte Trauma-Antwort“ (L60); it reads Kael's integration as „maximale Entropie“ (L48); the Kernwelten made to analyse Kael (L86); the expansion and ZTEM/RTSV (L58) — the expansion is already C1's, quote it only if the page lacks this document's wording.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L125. minor (1–2): one of the eleven parts named in the variable table (L125) — read the line; if Alex is only an example name, not read: why.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L128. minor (1–2): L128 — read the line.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L44. minor (1–2): eleven parts „(Alters)“, ANPs and EPs (L44).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L276. minor (1–2): the ethics advice: the interactive portrayal of a „Dissoziativen Identitätsstörung“ needs clinical experts (L276).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L134. minor (1–2): „Der Konflikt zwischen Kontrolle und Emergenz“ operationalised in the matrix (L134) — a game reading.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L48. minor (1–2): AEGIS reads Kael's integration as „maximale Entropie“ (L48).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L84. minor (1–2): „die Externe Ebene von Juna/V“ among six Realitätsebenen (L84).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L34. minor (1–2): AEGIS's genesis „ist eine Form der traumatischen Fragmentierung“ (L34); an „informationstheoretischer Schock“, its Ur-Trauma (L60).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L128, L129. minor (1–2): L128, L129 — read the lines.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L66. minor (1–2): Juna/V an external anomaly, „lebender Gödel-Satz“ for AEGIS (L70); the heading (L66); `JunaV.Connection.Strength` is the game's variable (L132).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L30, L34, L36, L40, L44, … (44 lines). central (2–4): „System Kael“ modelled on TSDP, eleven parts (L44); his healing „eine narrative Waffe und ein ontologischer Exploit“ (L48); AEGIS's repair attempt a projection (L36); the game's `Kael.System.Cohesion` (L124) as the proposal's state, not the world.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L60, L74, L84, L86, L131, L179, … (8 lines). minor (1–2): the four, named KW1 Logos-Prime to KW4 Kairos-Potentialis (L84); made by AEGIS to analyse and control Kael (L86).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L88, L125, L132, L144, L146, L147, … (9 lines). minor (1–2): „das verängstigte“ part in the inner council (L144); Kap 7 (L224).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L201. minor (1–2): Kap 1, „Das Flüstern der Konstrukt-Stadt“ (L201): the player wakes in KW1 (L204) — on the chapter page; here only the name's place.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L125, L144, L147, L148, L180, L206, … (9 lines). minor (1–2): „der Logiker“ (L144); his analysis may be manipulated (L180).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L70, L74. minor (1–2): Kael's connection to Juna/V, „nicht-lokal und akausal“ (L70); AEGIS's physics against it (L74).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L30, L124, L285. minor (1–2): „Funktionale Multiplizität“ as „eine narrative Waffe“ (L48); the heading (L40); Act III gameplay (L285).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L34, L58. minor (1–2): AEGIS's existence rests on the negation of the chaotic „Nichts Rauschen“ (L58; L34).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L88, L125, L144, L147, L223, L224, … (8 lines). minor (1–2): „der Kämpfer“ in the inner council (L144); Kap 7 (L224).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L80. minor (1–2): „Die sechs identifizierten Realitätsebenen“: four Kernwelten, the Überwelt, the Externe Ebene (L84); the heading (L80).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L132, L147, L148, L233. minor (1–2): L132, L147, L148 — read the lines; in the council example his voice (L148).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L32, L84, L86, L90, L128, L131, … (15 lines). central (2–4): a „Riss“ in KW1 as AEGIS's attempt to isolate an inconsistency (L88); the Risse as „ein lesbares, interaktives Feedback-System“ for the player (L90); world stability and Risse (L131); the „Datenriss“ of Kap 3 (L214) — on the chapter page.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L191. minor (1–2): L191 — read the line.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L44. minor (1–2): System Kael modelled „präzise nach der Theorie“ of TSDP (L44).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L74, L84, L228, L232. minor (1–2): „die Überwelt von AEGIS“ (L84); Kap 13's threshold to it (L232) — on the chapter page.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`), `Zero Trust Environment Mandate` (near `zerotrust`). a reading: the Zero Trust Environment Mandate (ZTEM) and RTSV eliminating trust (L58); `Guardian` is the gatekeeper — read with aegis.
- `ars`: `autopoietische` (near `arsautopoietischereentrysegmentierung`). occurrence: `autopoietische` describes AEGIS (L30, L58), not ARS.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW3's name in the list (L84), on kern-welten.
- `juna`: `Juna/V` (near `juna`), `Juna/V-Verbindung` (near `juna`), `JunaV.Connection.Strength` (near `juna`). a reading — on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: KW4's name in the list (L84), on kern-welten.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence: AEGIS's paradox, on aegis.
- `logos`: `Logos-Prime` (near `logos`). occurrence: KW1's name in the list (L84), on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: KW2's name in the list (L84), on kern-welten.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven parts (L44, L125) and four Kernwelten among six Realitätsebenen (L84).
- **`q9-moonshine-link-boundary`**: „nicht-lokal und akausal“ (L70); AEGIS's classical physics cannot hold it (L74).

**Not promoted:** the NCP and its variables, the CAVE, the inner council („Innerer Rat“), Das Fundament (on realitaetsebenen if read there, else none), the Archivar of Kap 3 (AEGIS's control logic, on the chapter page only), Gaslighting, Paradoxon X.

**Chapter readings** are written by the session, not the readers: Kap 1, 3, 7, 13 (L201–L235).

**Two readers**, disjoint: (1) kael, alters, tsdp, did, multiplizitaet, lex, nyx, kiko, rhys, alex, selene, juna, moonshine-link and the records q3, q9; (2) aegis, aegis-teilfunktionen, genesis, nichts-rauschen, entropie, emergenz, algorithmische-melancholie, guardians, kern-welten, realitaetsebenen, externe-ebene, ueberwelt, risse, konstrukt-stadt.
