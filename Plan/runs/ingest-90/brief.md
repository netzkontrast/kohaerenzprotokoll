# Brief — readings from document 90 (step 6)

1 document, one reader, one batch: `ingest-90`. Files go to `Plan/runs/ingest-90/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 90 | `weltenkonzept-fuer-kohaerenz-protokoll-tsdp-basiert` | 2025-04-29 | „the world concept“ (titled `Weltenkonzept für „Kohärenz Protokoll“ (TSDP-basiert)`) | a German design concept of 2025-04-29 for the novel's six realities (L13–L17): KW1 Konstrukt-Stadt (Guardian LogOS, L19), KW2 Resonanz-Landschaft (Mnemosyne, L41), KW3 Grenzfeste (Cerberus, L63), KW4 Möglichkeits-Garten (Kairos/Sophia, L85), the Überwelt of AEGIS (L107) and the Externe Ebene of Juna/V (L131), each by one template — `Konzeptueller Kern`, `Eigenschaften` (Ästhetik, Sensorik, Atmosphäre), `Gesetzmäßigkeiten`, `Schnittstellen/Risse`, `Beziehung zu Anteilen`; the alters' reactions are hedged proposals (`könnte`, `wahrscheinlich`, `evtl.`); it makes no canon claim and refers to another text it does not name (L13) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (156 lines for `weltenkonzept-fuer-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design concept: write „the world concept proposes …“ or „describes …“; its alters' reactions are `wahrscheinlich` and `könnte` — keep the hedge in the quotation. Headings start with a digit (`4. KW4: …`) that `--find` drops: quote from the word after it. Bold labels carry `**`: quote the text after the label. A bare „…“ for a word you merely mention counts as an uncited quotation: use backticks. The Externe Ebene section writes its own laws as „Unbekannt“ (L144) and its look as questions: record the question marks. Chapter content: the document names no chapter.

## Pages — document 90, `weltenkonzept-fuer-kohaerenz-protokoll-tsdp-basiert`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L21, L32, L54, L65, L98, … (14 lines). central (3–5): the Überwelt as AEGIS's domain (L107 on, `Entropie-Management`), AEGIS/LogOS enforcing consistency in KW1 (L32), and its reach into KW2 and KW4 (L54, L98).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L65, L76, L120. minor (1–2): `Zero-Trust` in the Überwelt (L120) and L65, L76 — what the lines say.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L61, L82, L105, L152. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L39, L104, L129. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L63, L76. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L109, L120, L144. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L131. minor (2–3): section 6 (L131 on): Realität außerhalb von AEGIS' Kontrolle, `Gesetzmäßigkeiten: Unbekannt` (L144), the `Ankerpunkte` (L145 on).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L63. minor (2): section 3 (L63 on), KW3 with Cerberus.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L60, L82. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L17, L121, L131, L133, L150. minor (2–3): the Externe Ebene as „Entität: Juna/V“ (L131) — the world, its unknown laws and its anchor points; the alters' reactions (L133 on).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L17, L21, L38, L43, L61, … (15 lines). central (3–5): Kael as ANP-Host in each world's `Beziehung zu Anteilen` (L43, L61), the structure (L17) — the six realities as aspects of his psyche and an outside; his ambivalence toward the Externe Ebene (L150).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L85, L98. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L17. minor (2–3): the overview (L17): four Kern-Welten as aspects of Kael's psyche; each with its Guardian.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L39, L60, L83, L105, L151. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title (L11) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L19. minor (2): section 1, `Konstrukt-Stadt (Guardian: LogOS)` as KW1 (L19) — one world of four.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L38, L61, L82, L105, L127, L152. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L39, L60, L83, L104, L151. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L19, L32. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L41, L54. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L85. minor (2–3): section 4 (L85 on), `Möglichkeits-Garten (Guardian: Kairos/Sophia)` as KW4 — a world, not a region.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L39, L60, L83, L105. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L39, L60, L82, L105, L152. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L13. minor (1–2): the introduction's „Realitätsebenen („Welten“)“ (L13) and the six-level structure (L17).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L41. minor (2): section 2 (L41 on), KW2 with Mnemosyne.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L39, L60, L83, L104, L151. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L17, L33, L55, L77, L99, L121, … (8 lines). minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L39, L61, L82, L104, L151. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L85, L98. minor (1–2): what the world concept says of it — 1–3 quotations, with the world's section.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L11, L13. minor (1–2): the title and introduction: `TSDP-basiert` (L11, L13), the six realities integrating the TSDP structure of System Kael.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L17, L107. minor (2–3): section 5 (L107 on): the purely digital level, domain of AEGIS.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9): the title `Weltenkonzept für „Kohärenz Protokoll“`, no new reading.


**Record entries** (one file each; write one only where the concept speaks to the record's question):

- **`c5-garten-scale`**: KW4 as a Kern-Welt (L85) — one of four worlds.
- **`c9-konstrukt-stadt-scale`**: Konstrukt-Stadt as KW1 only (L19).
- **`c6-guardians-count-and-pairing`** and **`q5-guardians-and-kern-welten`**: the guardian by world — LogOS, Mnemosyne, Cerberus, Kairos/Sophia (L19, L41, L63, L85).
- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten (L17).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as a fifth reality (L107) — only if the line bears on the question.
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene as a reality outside AEGIS's control (L131 on).

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, externe-ebene, ueberwelt, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, logos, mnemosyne, cerberus, kairos, sophia, tsdp, aegis-teilfunktionen, entropie, risse, realitaetsebenen, and the seven records.
- Reader 2: the alters' pages (lex, alex, argus, isabelle, kiko, lia, moros, nyx, rhys, selene).
