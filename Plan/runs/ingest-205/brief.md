# Brief — readings from document 205 (step 6)

1 document, one reader, one batch: `ingest-205`. Files go to `Plan/runs/ingest-205/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 205 | `100-konzepte-zur-vertiefung-fuer-kohaerenz-protokoll` | 2025-04-29 | „the hundred concepts list“ (an unsigned list) | a German list of 100 concepts worth deepening, in eight groups whose numbering restarts, each a bold name with a one-line `Begründung` — a working list from „unserer Diskussion und den Dokumenten“ (L13), defining almost nothing; its items are proposals and questions, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (140 lines for `100-konzepte-zur-vertiefung-fu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A list of concepts to deepen: write „the hundred concepts list names / gives as reason …“; an item is a topic and its `Begründung`, not a definition; an item that only asks (L22, L31, L47, L56) is recorded as a question. German — quote as written; cut before inner straight quotes; `--find` drops digits (`KW1`, `Co₁`, `Die 6 Paraiyas`) — quote around them; never quote across the item's opening `**`.

## Pages — document 205, `100-konzepte-zur-vertiefung-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L31, L32, L35, L36, L44, L46, … (36 lines). central (3–6): Autopoiesis explains AEGIS's focus on self-preservation and boundary, why it sees integration as a threat (L46); its contradiction Paradoxon X, „muss klar definiert und narrativ genutzt werden“ (L50); its control attempts must fail (L57); its reductionist approach failing on Kael's holistic character (L58); AEGIS as an example of misguided AI goals (L85); gaslighting as its manipulation technique (L87).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L71. minor (1–2): the „Zero-Trust-Prinzip (AEGIS)“ as „Konkretes Funktionsprinzip von AEGIS“, shaping KW3 and the Überwelt (L55); KW3 with Zero-Trust (L71).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L40, L71. minor (1–2): „Alex (Protektor-ANP - Loyalität)“: active protection, his loyalty a strength or a weakness (L40); KW3 as the domain of Alex and Nyx (L71).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L42. minor (1–2): „Argus (Beobachter/Kritiker - Meta-Kognition)“: self-reflection, at the risk of paralysis by criticism (L42).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L51. minor (1–2): „Kontrolle vs. Emergenz“ as the central conflict between AEGIS's goal and the nature of complex systems (L51) — the heading is not counted; quote the reason.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L56. minor (1–2): „Entropie-Management (AEGIS)“ as a core function of AEGIS, with the questions how it measures and fights entropy and how entropy shows (L56) — keep them as questions, cut before the inner quotes.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Externe Ebene` alone on L74. minor (1–2): „Die Externe Ebene (Juna/V)“: „Das Unbekannte außerhalb von AEGIS; Quelle der Verbindung/Hoffnung“ (L74).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L39. minor (1–2): „Isabelle (Sexualisierter EP - Kontrolle)“, a specific trauma reaction exploring power, control and sexuality (L39).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L30, L31, L37, L47, L74, L81, … (7 lines). minor (1–2): Juna/V as the Moonshine-Link, the nature of the connection asked — resonance, non-locality? — its function for Kael and threat to AEGIS (L81); attachment theory relevant for Juna/V (L30).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L23, L26, L29, L30, … (22 lines). central (3–6): TSDP as „Das Kernmodell für Kael“ (L17); what is the realistic goal for Kael — „Nicht unbedingt Fusion, sondern Kooperation“ (L26); the attachment theory explaining his difficulty with trust (L30); Kael constructing his identity by narrating (L31); the individuation process as frame for his journey (L29).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L19, L34. minor (1–2): „Kiko (Kind-EP - Angst/Freeze)“, carrier of the core vulnerability, his healing central (L34).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–2): „Kohärenz (Begriff & Ziel)“ as the central term — AEGIS's definition against Kael's and Selene's, integration (L132); Resonanz as its counterpart (L133). L11 is the title, an occurrence.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L28, L36, L69. minor (1–2): „Lex (Rationaler ANP - Kontrolle)“ representing AEGIS's logic in small (L36); KW1 as the domain of Lex/Kael-ANP (L69) — quote around the digit.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L28, L41, L72. minor (1–2): „Lia (Kind-EP - Ambivalenz)“, embodying closeness against fear, bringing creativity and play (L41).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L81. minor (1–2): „Juna/V (Moonshine-Link)“ — the connection's nature asked: resonance, non-locality? (L81) — a question.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L38. minor (1–2): „Moros (Kollaps-EP - Leere)“, the deepest trauma reaction, his integration the greatest challenge (L38).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L26. minor (1–2): „Integration vs. Funktionale Multiplizität“: not necessarily fusion, but cooperation (L26) — the heading is not counted; quote the reason.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L77. occurrence: `Nexus` stands in a list of symbolic places with Bunker and Schrein (L77), not the meta-space.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L19, L24, L27, L35, L71. minor (1–2): „Nyx (Kampf-EP - Wut/Schutz)“, embodying trauma rage, his dynamic with AEGIS (Paradoxon X) a conflict driver (L35); even destructive parts like Nyx meant to protect (L24); the Shadow deepening Nyx (L27).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L47, L115. minor (1–2): how AEGIS interacts with the outside — „Potentialmeer, Juna/V“ (L47), a question; the nature of the Potentialmeer as cosmic horror (L115).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L28, L37, L72. minor (1–2): „Rhys (Pflegender ANP - Empathie)“, central for connection and healing, but vulnerable (L37).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L53, L56, L75. minor (1–2): Gödel's theorems explaining the inherent Risse (L53) — cut before the inner quotes; the Risse „als Systeminstabilität“: manifestation of Paradoxon X, trauma breakthroughs, limits of the simulation (L75).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L23, L72, L132. minor (1–2): „Das Selbst (IFS/Selene)“ as the source of healing; „die Natur und Zugänglichkeit von Selene ist zentral für Kaels Bogen“ (L23); KW4 as the domain of Lia, Rhys and Selene (L72).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L17, L68. minor (1–2): „Tertiäre Strukturelle Dissoziation (TSDP)“ as the core model for Kael, with multiple ANPs and EPs (L17); the Kernwelten as manifestations of Kael's TSDP parts (L68).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Überwelt` alone on L55. minor (1–2): „Die Überwelt (AEGIS-Domäne)“: „Abstrakte, informationsbasierte Realität; Kontrast zu menschlicher Wahrnehmung“ (L73).

- **`kern-welten`** (minor, 1–3): „Kernwelten als Psychologische Architektur“ — not only settings but manifestations of Kael's psyche and TSDP parts (L68); KW1 Ordnung/Logik the domain of Lex (L69), KW2 Emotion/Erinnerung of the EPs (L70), KW3 Abwehr/Paranoia of Alex and Nyx (L71), KW4 Potentialität/Kreativität of Lia, Rhys and Selene (L72) — quote around the digits.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Prinzip (AEGIS)` (near `zerotrust`). read on aegis-teilfunktionen (L55).
- `entropie`: `Entropie-Management (AEGIS)` (near `entropie`). read on entropie (L56).
- `externe-ebene`: `Die Externe Ebene (Juna/V)` (near `externeebene`). read on externe-ebene (L74).
- `kern-welten`: `Kernwelten als Psychologische Architektur` (near `kernwelt`), `Kernwelten als Psychologische Architektur` (near `kernwelten`). a reading — see the extra page below.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz (Begriff & Ziel)` (near `koharenz`). `Kohärenz (Begriff & Ziel)` read on kohaerenz (L132); `Kohärenz Protokoll` the title, an occurrence.
- `ueberwelt`: `Die Überwelt (AEGIS-Domäne)` (near `uberwelt`), `Simulationshypothese & Kritiken` (near `simulation`). `Die Überwelt (AEGIS-Domäne)` read on ueberwelt (L73); `Simulationshypothese & Kritiken` the borrowed hypothesis (L62), an occurrence.
- `vergessener-schrein`: `Schrein` (near `vergessenerschrein`), `Schrein` (near `vergessenerschreintraumalokus`). occurrence: `Schrein` stands in a list of symbolic places (L77), without the Vergessener Schrein's sense.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: ten named parts with roles (L34–L42) and four Kernwelten each the domain of parts — KW1 Lex/Kael-ANP, KW2 the EPs, KW3 Alex/Nyx, KW4 Lia/Rhys/Selene (L69–L72): a correspondence of worlds to parts, not one to one.
- **`q9-moonshine-link-boundary`**: „Juna/V (Moonshine-Link)“ — the link named for the connection, its nature asked (L81).
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene as „Das Unbekannte außerhalb von AEGIS“, source of connection and hope (L74).

**Not promoted:** the borrowed theories (Jung, IFS, Ricoeur, Butler, Hermans, Floridi, Whitehead, Rosa, Foucault, Gödel), Paradoxon X, the Fundament and the six Paraiyas, Fundamentale Symmetrie, the narrative techniques, the Novelcrafter tools, the Resonanz-Gefüge, the KW short codes Co₁, McL, B, Ly.

**Two readers**, disjoint: (1) kael, kiko, nyx, lex, rhys, moros, isabelle, alex, lia, argus, selene, tsdp, multiplizitaet, kern-welten and the record q3; (2) aegis, aegis-teilfunktionen, emergenz, entropie, risse, ueberwelt, externe-ebene, potentialmeer, juna, moonshine-link, kohaerenz and the records q9, c13.

No chapter readings: the list names no chapter (it mentions „39 Kapitel“ only as a total, L108).
