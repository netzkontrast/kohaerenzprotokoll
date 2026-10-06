# Brief — readings from document 123 (step 6)

1 document, one reader, one batch: `ingest-123`. Files go to `Plan/runs/ingest-123/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 123 | `kohaerenz-protokoll-kapitel-outline-generierung` | 2026-04-30 | „the 39-chapter outline“ (titled `Kohärenz Protokoll — 39-Kapitel-Outline (Dual-Storyform-Encoding)`, L11) | a German outline of 2026-04-30, generated from a research prompt (reference 5, L1630): a synopsis (L13–L17), a dual-storyform table (L24–L31), a 13-alter table (L35–L47), then each of Kapitel 1–39 in three acts with Worum/Konzepte/Was passiert/POV/Foreshadowing and an encoding per storyform; appendices (L1560–L1626) that discard legacy material „nach dem Reset vom 2026-04-30 (Kanon-Dok 1)“ and log its own contradictions. It rates itself „Confidence: HIGH“ per chapter |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1630 lines for `kohaerenz-protokoll-kapitel-ou`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline proposes: write „the 39-chapter outline has / sets / discards …“; its claims of canon, of a reset on 2026-04-30 and of discarded names (Anhang B, L1572–L1578) are recorded as its claims, never applied; „[Vorschlag]“ marks its own proposals. Footnote digits glued to sentence ends (`.3`, `.2`) are export damage — cut quotations before them. Kael is male (er). Chapter pages are done by the session.

## Pages — document 123, `kohaerenz-protokoll-kapitel-outline-generierung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L46, L113, L117, L119, L133, … (105 lines). central (2–4): Universe throughline of storyform B (L26); „AEGIS ist operativ K0, glaubt aber K1 zu sein (Dialetheia)“ (Anhang F, L1603; also L1582); the Heat-Spike feedback loop of its Landauer heat (L1360); after the Vortex „AEGIS ist nicht tot, sondern tief in sich gekehrt“ (L1409).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L42, L169, L171, L181, L463, L545, … (17 lines). minor (1–2): „Protector (ANP)“ (L42); his part in the Schein-Verhalten (L767).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L849, L1407. minor (1–2): introduced with Post-Vortex (L1407); AEGIS as „eine weinende, gigantische Maschine“ (L1409).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L1576. minor (1–2): discarded: „Wächter Cerberus, Kairos, Sophia: Verworfen“ (L1576).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L731. occurrence unless L731 says more than Oblivion's argument that resistance makes „endlose Entropie und Schmerz“ — then minor (1).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L659. occurrence: `Genesis-Erkenntnis` L731 names a realisation, not the page's sense.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L29, L45, L129, L131, L137, … (47 lines). central (2–4): first a „Leerstelle, die er nur "Juna" nennen kann“ (L17); IC in both storyforms (L29; resolution L1604); „Juna als TSDP-Alter von Kael: Verworfen“ (L1575); „Juna wird im Text nicht direkt beschrieben“ (L1239); the simulated Juna as an empty shell (L1167).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L26, L29, L35, L40, … (125 lines). central (2–4): the host, ANP (L40); storyform A's MC in Mind (L26), B's IC „Kael als Paradoxie“ (L29); Köln 2026 at a constant 21 °C (L15); presents himself as „Komponente 734“ (L767); the closing routine mirroring Kapitel 1 (L1479).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L1576. minor (1–2): the same line, L1576.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L767. minor (1–2): Kael presents himself to AEGIS as „Komponente 734“ (L767).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L51, L57, L273, L391, L537, L587, … (9 lines). minor (1–2): „Die Konstrukt-Stadt präsentiert sich als ein fehlerfreies Hard-SF-Horror-Szenario“ (L51); soft after the Vortex, the 21°C constant broken (L1409).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L41, L93, L97, L99, L101, L109, … (34 lines). minor (1–2): „Rationalist (ANP)“ with Kälte and Hypoventilation (L41); one line of his role in Akt I if the document gives one (L1590).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L95. minor (1–2): L95 — `LogOS` among Kapitel's introduced concepts; read what the chapter says of it, or occurrence if only listed.
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L201, L203, L205, L209, L225, L227, … (16 lines). central (2–4): „der Wächter-Entität Mnemosyne, die gefährliche Erinnerungen nicht thermisch löscht, sondern kognitiv isoliert“ (L201, L205); the pantheon reduced to Mnemosyne and the Lösch-Pol (L1576).
- **`moonshine-link`** (central, 3–12 quotations): the census's surfaces — `Moonshine-Link` L31, L45, L209, L431, L657, L659, … (13 lines). central (2–4): the RS throughline of storyform A in Physics (L31); Silas carries it (L45, L659); where Silas holds it open the sweep fails (L1065).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L323, L537, L771, L1201, L1477. minor (1–2): the Wir-Geflecht converging in Akt III „zur funktionalen Multiplizität“ (L47); L1477.
- **`oblivion`** (central, 3–12 quotations): the census's surfaces — `Oblivion` L46, L355, L357, L359, L727, L731, … (16 lines). central (2–4): „AEGIS-Echo (EP)“ (L46); gains influence in Sektor 04 (L355) and argues for giving up (L731); his final arc seeing through AEGIS's offered peace (L1101).
- **`ouroboros-struktur`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Ouroboros-Struktur` alone on L1574. minor (1–2): „widerspricht der K1-Logik der Ouroboros-Struktur aus Kanon-Dok 2“ (L1574) — the discarded Universal Re-Connecting; the Ouroboros-Schluss of Kapitel 39 (L1475–L1477).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L43, L137, L241, L243, L423, L427, … (17 lines). minor (1–2): „Caregiver (EP)“, Schweiß, Fieber, Arc zur Akzeptanz (L43) — EP here; say so, nothing more.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L57. minor (1–2): `thermische Risse` among Kapitel 1's concepts (L57) — read only if a chapter says what they are; else occurrence.
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L169, L355, L809, L881, L941. minor (1–2): Kael's work in Sektor 04 (L355); what L169 says.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L44, L319, L321, L331, L623, L625, … (15 lines). minor (1–2): „Internal Self Helper (EP)“, Arc zur Mediatorin (L44); the mediator who stages the Schein-Verhalten (L767).
- **`silas`** (central, 3–12 quotations): the census's surfaces — `Silas` L45, L205, L207, L209, L217, L227, … (21 lines). central (2–4): „Juna-Echo (EP)“, „Träger des Moonshine-Links“ (L45); established as its keeper (L209); activates it (L659) and tears it open inward (L911).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L1576. minor (1–2): the same line, L1576.
- **`telefon-stille`** (minor, 1–4): the census's surfaces — `Telefon-Stille` L131, L1360. minor (1–2): the antiquated terminal (L131–L133) and „Die absolute Telefon-Stille durchdringt das System“ (L1360).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L689, L691, L693, L695, L1203, L1599. minor (1–2): Kapitel 18 „Die Anatomie des Trennungsprotokolls“ (L689–L691): Kael maps it and grasps the city's purpose.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L849, L1101, L1358, L1360, L1393. minor (1–2): introduced in L1358 with Lebende Dialetheia and Heat-Spike; prepared at L849.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L35, L39, L205, L253, L317, L427, … (7 lines). minor (1–2): „Das 13-Alter-System (TSDP)“ (L35) and the TSDP-Funktion column (L39).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L30. occurrence: `Simulation` in the OS throughline (L30).
- **`vortex`** (central, 3–12 quotations): the census's surfaces — `Vortex` L245, L945, L1015, L1101, L1201, L1235, … (18 lines). central (2–4): the Vortex in Kapitel 35/36 (headings; L1015) with its five beats (Anhang D, L1590); the Vortex-Heat-Spike foreshadowed at L245.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `13-Alter-System` (near `alters`). occurrence — the 13-Alter-System is read on tsdp (L35); no page `alters` reading.
- `genesis`: `Genesis-Lüge` (near `genesis`). occurrence: `Genesis-Lüge` is the outline's name for a realisation.
- `ouroboros-struktur`: `Ouroboros` (near `ouroborosstruktur`). a reading — on the page above.
- `risse`: `thermische Risse` (near `risse`). on risse above.
- `ueberwelt`: `Köder-Simulation` (near `simulation`). occurrence: `Köder-Simulation` names AEGIS's bait, not the Überwelt.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: „Das 13-Alter-System“ (L35), seven named carriers (L40–L46) and „Die restlichen 6 namenlosen Alter“ (L47); Anhang F's own resolution of 13 vs 10 vs 7 (L1605); fifteen alter names „Dekanonisiert“ (L1577). Rhys an EP here (L43).
- **`q7-what-734-names`**: Kael presents himself as „Komponente 734“ (L767).
- **`q8-aegis-after-the-vortex`**: „AEGIS ist nicht tot, sondern tief in sich gekehrt“ (L1409).
- **`q9-moonshine-link-boundary`**: Silas „Träger des Moonshine-Links“ (L45); RS throughline in Physics (L31).
- **`c6-guardians-count-and-pairing`**: Cerberus, Kairos, Sophia discarded, „das Pantheon wurde auf Mnemosyne und den Lösch-Pol reduziert“ (L1576) — position 3, dated 2026-04-30.
- **`c7-juna-first-appearance`**: Juna first as a silence in the net Kael names „Juna“ (L17); „Juna wird im Text nicht direkt beschrieben“ (L1239).
- **`c11-landauer-warmth-or-cold-ozone`**: Ozon with the anomalies (L15, L59, L241) and Kapitel 39 „es riecht nicht nach Ozon“ (L1479); Landauer heat in the sweeps (L239, L1360).

**Not promoted:** Lösch-Pol and Erasure-Sweeps (on mnemosyne and C6), Wir-Geflecht (on multiplizitaet), Lebende Dialetheia, Heat-Spike, Taschenuhr, Reader-Substrate, the M13 method and the appendices' audit vocabulary.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, juna, moonshine-link, mnemosyne, cerberus, kairos, sophia, logos, konstrukt-stadt, telefon-stille, truth-rotation, algorithmische-melancholie, vortex, entropie, ouroboros-struktur, risse, and the entries q8, q9, c6, c7, c11.
- Reader 2: kael, lex, alex, rhys, selene, silas, oblivion, multiplizitaet, tsdp, sektor-04, komponente-734, trennungsprotokoll, and the entries q3, q7.
