# Brief — readings from document 87 (step 6)

1 document, one reader, one batch: `ingest-87`. Files go to `Plan/runs/ingest-87/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 87 | `roman-entwicklung-kohaerenz-protokoll-json` | 2026-02-26 | „the research report“ (titled `Forschungsbericht: Systemarchitektur, Ontologie und narrative Dynamik des „Kohärenz Protokolls“`) | a German research report of 2026-02-26 in nine numbered sections: ontology (two kernels, Nichts-Rauschen, Potentialmeer, Fundament, L23–L39), physical constraints (L41–L63), a table of the four Kernwelten, the Überwelt and the Externe Ebene (L65–L79), System Kael with eleven alters (L81–L109), AEGIS and four Guardians (L111–L133), the four Dramatica throughlines (L135–L195) and a three-act progression of Kap 1–39 by act (L197–L217); it calls itself „eine erschöpfende“ analysis (L21), claims no canon, and ends with six references |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (233 lines for `roman-entwicklung-kohaerenz-pr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report: write „the research report says …“ or „describes …“ — it reports, it decides nothing. Its numbered footnote digits glued to sentence ends (`…Simulation.1`) are not text: quote around them; `--find` drops digits glued to words (`KW1`). The table rows (L71–L79) escape their bold (`\*\*`): quote the cell text, not the markup. Inner „…“ inside a quotation end it for the checker: cut before the inner mark and name the term in backticks. Chapter content goes on the chapter pages (a later batch, by act only); on a term page, at most one or two beats by act.

## Pages — document 87, `roman-entwicklung-kohaerenz-protokoll-json`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L21, L31, L33, L39, L49, … (31 lines). central (4–6): section 6.1, the cognitive logic of AEGIS (L115 on); the two kernels (2.1, L27–L33); its delegation to four Wächter (L128); its role in the throughlines (7.1) and the Purge of Akt III (L217).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L93, L187. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L153. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L76, L85, L165, L211. minor (2): „elf hochspezialisierten Anteilen (Alters)“ (L85) and the ANP/EP/ISH sections (5.1–5.3).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L95. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L76, L132. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L31. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L31. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L79, L217. minor (2): the table row „Externe Ebene“ (Köln, Februar 2026, L79) — Kael as a patient with KPTBS, ADHS and DIS, cared for by his partner Juna; and L217.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L17, L57, L181, L217. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L78, L111, L126, L211. minor (2–3): section 6.2 — four sub-algorithmic Wächter (L128), each with its world and boundary (L129–L133); residing in the Überwelt (L78).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L104, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L31, L55, L79, L94, L103, L144, … (14 lines). central (3–5): Juna as the IC, „Juna / Die Anomalie“ (7.3, L169 on); Juna as Kael's partner in the Externe Ebene (L79); the Moonshine-Link (7.4).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L33, L39, L49, L57, … (30 lines). central (4–6): System Kael (section 5, L81–L85) — eleven alters, the goal `Funktionale Multiplizität` (L85); the MC throughline (7.2, L155 on); his path through the three acts (L205, L211, L217).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L133. minor (1): „Kairos / Sophia“, Wächterin of KW4 (L133).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L65, L67. minor (2): section 4 and its table (L65–L79), the four worlds with their logic and diction.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L91, L102. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the novel's title (L11) — occurrence (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L31. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L31. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L74. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L92, L93, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L103, L187. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L130, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L75, L131, L164, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L172, L183. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L105, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L17. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L78, L211, L217. minor (1–2): the Überwelt named Nexus (L78) and Akt II's ascent into the Nexus (L211).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L35, L37. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L91, L93, L101, L132, L187. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L79. minor (1): Juna as „seiner Partnerin“ in the Externe Ebene (L79).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L35, L37, L144. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L94, L211. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L120. minor (1): `Glitches` at L120, if the line says what they are; else occurrence, say why.
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L205. minor (1): `Sektor 04` (L205) as Akt I places it.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L109. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L133. minor (1): „Kairos / Sophia“, Wächterin of KW4 (L133).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L81, L83. minor (1–2): what the research report says of it — 1–3 quotations, with its section.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L78, L128, L207, L211. minor (2): the table row „Überwelt (Nexus)“ (L78), the Nexus of Akt II (L211).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Die Anomalie` (near `mustererkennunganomaliedetektion`). occurrence (J69): `Die Anomalie` is Juna's IC label (L169), not the metric.
- `dkt`: `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). a reading on `dkt`: section 2.1, the Dual-Kernel-Theorie (L27–L33).
- `kairos`: `Kairos-Potentialis` (near `kairos`), `Kairos / Sophia` (near `kairos`). readings, above (J34: a slash in a name the wiki has).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Checkliste` (near `koharenz`), `Paradoxon der fehlausgerichteten Kohärenz` (near `koharenz`). occurrences: the title and compounds (J9, J12).
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading on `multiplizitaet`: the goal of System Kael (L85), and L17, L217.
- `sophia`: `Kairos / Sophia` (near `sophia`). a reading, above.


**Record entries** (one file each; write one only where the report speaks to the record's question):

- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene row, Köln, Februar 2026 (L79), and L217.
- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten plus Überwelt and Externe Ebene (L65–L79); eleven alters (L85).
- **`c6-guardians-count-and-pairing`** and **`q5-guardians-and-kern-welten`**: four Wächter, each paired with a world (L128–L133).
- **`q6-nexus-ueberraum-ueberwelt`**: „Überwelt (Nexus)“ (L78).
- **`q9-moonshine-link-boundary`**: the RS throughline, `Der Moonshine-Link` (7.4, L183 on).

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, externe-ebene, partnerin, guardians, ueberwelt, nexus, kern-welten, konstrukt-stadt, logos, mnemosyne, cerberus, kairos, sophia, dkt, kohaerenz-kernel, kollaps-kernel, nichts-rauschen, potentialmeer, entropie, emergenz, goedel-gambit, algorithmische-melancholie, moonshine-link, risse, sektor-04, and the six records.
- Reader 2: the alters' pages (alters, alex, argus, isabelle, kiko, lex, lia, moros, nyx, rhys, selene), mosaik-herz, multiplizitaet, tsdp.
