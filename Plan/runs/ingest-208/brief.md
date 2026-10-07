# Brief — readings from document 208 (step 6)

1 document, one reader, one batch: `ingest-208`. Files go to `Plan/runs/ingest-208/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 208 | `analyse-und-uberarbeitung-des-gesamtplots-mit-subplots` | 2025-05-02 | „the subplot revision“ (an unsigned plot revision) | a German analysis of an earlier plot draft „basierend auf den 39 Kernkonzepten“ (L17) that integrates five subplots (L19–L23) and rewrites the plot as 39 one-line chapters in three parts, each tagged with subplot numbers (L35–L83) — a proposal, marking nothing as canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (88 lines for `analyse-und-uberarbeitung-des-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A revision proposal: write „the subplot revision plans / tags …“, name the chapter a line belongs to; its hedges (`Fundament?`, `Könnte`) stay. German — quote as written; cut before inner straight quotes; `--find` drops the digit in `KW1`–`KW4` — quote around it; the subplot tags are bold (`**Subplot 1**`) — never quote across them.

## Pages — document 208, `analyse-und-uberarbeitung-des-gesamtplots-mit-subplots`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L17, L20, L21, L22, L25, … (26 lines). central (3–6): the subplot Lex' Systemanalyse & AEGIS' Paradoxon turns AEGIS from a generic control AI into a system with a specific flawed logic (L20) — cut before the inner quotes; Kael recognises AEGIS as the steering instance (Kap 14, L53); AEGIS offers a deal (Kap 29, L73); `Der Fall des Wächters`: AEGIS defeated or changed, the paradox resolved (Kap 36, L80).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L37, L43. minor (1–3): Alex (ANP) becomes active, a focus on protection (Kap 3, L37); Alex's role in KW3 (Kap 9, L43).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L56. minor (1–3): „Kael (Lex/Argus) entdeckt AEGIS' Kernparadoxon“ (Kap 17, L56).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L37, L43. minor (1–3): a hint of Cerberus (KW3) (Kap 3, L37); Kael explores KW3 and Cerberus (Kap 9, L43) — quote around the digit.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L13, L21, L61. minor (1–3): the subplot Das Mysterium Juna/V & die Externe Ebene brings in an element outside AEGIS's control that offers hope (L21); hints at the Externe Ebene (Kap 22, L61).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L43. minor (1–3): chapter 9 `An Mauern der Grenzfeste`: Kael explores KW3, defence and fear (L43).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L54, L55, L62, L80. minor (1–3): the subplot Die Wächter als Agenten & Charaktere makes AEGIS's control tangible through characterised agents whose domains are the Kernwelten (L22) — cut before the inner quotes; Guardians in the Überwelt (Kap 15, L54); Kael meets them and understands their blind spots (Kap 16, L55); the fate of the Guardians (Kap 36, L80).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L13, L21, L25, L45, L61, L64, … (12 lines). central (3–6): the subplot Das Mysterium Juna/V, outside AEGIS's control (L21); first hints of Juna/V at the first Riss (Kap 11, L45); clearer contact (Kap 25, L64); Juna/V intervenes actively (Kap 30, L74); Kael's and Juna/V's actions trigger the collapse of AEGIS's control (Kap 32, L76); open questions on Juna/V at the end (Kap 39, L83).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L17, L19, L22, L25, L33, … (32 lines). central (3–6): Kaels Weg zur Funktionalen Multiplizität as the core subplot that shapes his agency in every phase (L19); Kael (Host) wakes in KW1 with amnesia (Kap 1, L35); crisis forces cooperation (Kap 13, L47); a significant sacrifice of the Kael-System (Kap 33, L77); apotheosis (Kap 34, L78); Kael living as a stable system (Kap 38, L82).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L22, L33, L60. minor (1–3): the Wächter's domains, the Kernwelten, structure the exploration (L22); Kael returns to the Kernwelten with new understanding (Kap 21, L60).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L38, L40. minor (1–3): first EP intrusions, Kiko and Lia (Kap 4, L38); trauma memories and EPs in KW2 (Kap 6, L40).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11); `Paradoxon der Fehlausgerichteten Kohärenz` is AEGIS's paradox, read on aegis (L20).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L36. minor (1–3): chapter 2 `Echos in der Konstrukt-Stadt`: Lex dominant, trying to understand KW1's logic (L36).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L13, L20, L25, L36, L45, L54, … (7 lines). minor (1–3): Lex (ANP) becomes dominant in Kap 2, phobia of chaos (L36); Kael (Lex) analysing AEGIS's architecture in the Überwelt (Kap 15, L54); the first Riss challenging Lex's logic (Kap 11, L45).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L38, L40. minor (1–3): first EP intrusions, Kiko and Lia (Kap 4, L38); KW2 (Kap 6, L40).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L36, L42. minor (1–3): a confrontation with „LogOS' Starrheit“ (Kap 2, L36); AEGIS (LogOS, Mnemosyne) using Kael's weaknesses for gaslighting (Kap 8, L42).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L39, L40, L42. minor (1–3): confrontation with Mnemosyne in KW2 (Kap 5, L39); „Mnemosyne manipuliert Erinnerungen“ (Kap 6, L40); gaslighting (Kap 8, L42).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L83. minor (1–3): functional multiplicity at the thematic close (Kap 39, L83); the subplot named for it (L19).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L39. minor (1–3): chapter 5 `Der Ruf der Resonanz-Landschaft`: Kael drawn into KW2, emotion and memory (L39).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L38. minor (1–3): „Rhys (ANP) tritt hervor“, a focus on care (Kap 4, L38).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L35. minor (1–3): chapter 1 `Der Glitch im Spiegel`, first glitches in reality (L35); chapter 11 `Der erste Riss`, a significant Riss in the simulation (L45).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L19. minor (1–3): the subplot Kaels Weg zur Funktionalen Multiplizität „(TSDP)“ as the core (L19).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L54, L71. minor (1–3): Kael (Lex) analyses AEGIS's rules and architecture, the Überwelt (Kap 15, L54); Kael enters AEGIS's core and the Überwelt (Kap 27, L71).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the Guardians' name (L47), read on guardians.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). `Paradoxon der Fehlausgerichteten Kohärenz` read on aegis (L20); the title an occurrence.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: the Wächter's domains are the Kernwelten (L22); LogOS in KW1 (Kap 2, L36), Cerberus in KW3 (Kap 3, 9, L37, L43), Mnemosyne in KW2 (Kap 5, 6, L39, L40); Guardians in the Überwelt (Kap 15, L54).
- **`c4-guardians-and-aegis`**: the Wächter as AEGIS's agents and characters (L22); AEGIS using LogOS and Mnemosyne for gaslighting (L42).
- **`q8-aegis-after-the-vortex`**: chapter 36 `Der Fall des Wächters` — „AEGIS besiegt/verändert“ (L80); the collapse of AEGIS's control (Kap 32, L76).
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene as an element outside AEGIS's control (L21).

**Not promoted:** the five subplot labels, the 39 Kernkonzepte, the Fundament, Heroine's Journey, Hero's Journey and the journey stages, Meta-Ebene.

**Two readers**, disjoint: (1) kael, juna, lex, alex, rhys, kiko, lia, argus, tsdp, multiplizitaet, externe-ebene and the record c13; (2) aegis, guardians, logos, mnemosyne, cerberus, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, risse, ueberwelt and the records q5, c4, q8.

**Chapter readings**: 39, written by the session (`Plan/runs/ingest-208-kap/`).
