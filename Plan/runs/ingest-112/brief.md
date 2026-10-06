# Brief — readings from document 112 (step 6)

1 document, one reader, one batch: `ingest-112`. Files go to `Plan/runs/ingest-112/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 112 | `romananalyse-kohaerenz-plot-kritik` | 2026-02-23 | „the publisher's report“ (titled `Analytischer Verlagsbericht: „Kohärenz Protokoll“ – Strukturelle, philosophische und narrative Evaluation`) | a German publisher's evaluation of 2026-02-23 that summarises the manuscript and its concept documents (a numbered reference list from L174, items 1–3, 9, 10, 14 among the author's own), with a Kern-Welten table (L53–L59) and a ten-Alters table with IFS roles (L77–L89), then criticises it (prologue, passivity, didactic tone, L117–L143) and recommends revisions (L145–L162); it claims its core „mit absoluter Sicherheit“ (L15) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (205 lines for `romananalyse-kohaerenz-plot-kr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A review: two voices, kept apart in every reading. What the report **summarises** of the manuscript and its concept documents (a reference number on the line) is written „the publisher's report summarises …“ or „reports …“; what it **criticises** and **recommends** (L117–L162, „muss“, „sollte“) is written „the report criticises …“, „recommends …“ — never as the novel's fact. The mathematics (Monster Group, Moonshine, Gödel, Landauer) is the report's account of the manuscript's metaphors. Kael is male (`der Protagonist`, „männlichen Protagonisten“ L161).

## Pages — document 112, `romananalyse-kohaerenz-plot-kritik`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L29, L31, L37, … (19 lines); `Kontrollinstanz` L17. central (3–5): the Kontrollinstanz AEGIS „(Autonomous Entropic Gatekeeper for Integrity Systems)“ (L17), the reductionist attempt to stabilise a traumatised system by force and logic; misreads the healing as entropy (L19); minimises Shannon entropy and deletes the unknown, Juna, as error (L29); the Landauer heat of its fight (L31); autopoietic, its logic implodes at the Gödel loop (L43); compared to Asimov's Multivac, „ein traumatisierter Multivac“ (L111).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L17, L71, L81, L99, L112, L131, … (7 lines). minor (1–2): ten distinct Alters from childhood trauma (L17, L71); the table of ten with IFS roles (L77–L89) — the count is the report's; integration of „dieser zehn Anteile“ (L91).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L58, L84. minor (1): KW3's guardian, sees every openness as intrusion (L58); Praetor triggers conflicts with Cerberus (L84).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L15. minor (1): the work as an allegory of DID projected onto an AI-run simulation (L15).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L99. minor (1): Kael from „Architekten“ to „Gärtner“ der Emergenz (L99).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L17, L19, L25, L27, L29, L31, … (14 lines). central (2–4): the report's account of the duality — thermodynamic (Clausius, Boltzmann, L27) and Shannon entropy (L29), joined by Landauer (L31); healing as „Entropie“ misread (L19); integration not by suppressing „Entropie“ (L91).
- **`entropie-signatur`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie-Signatur` alone on L156. minor (1): the report recommends that Echo's breakthrough not be told as a „Anstieg der lokalen Entropie-Signatur“ (L156) — the manuscript's phrase as the report quotes it.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L168. minor (1): only in the report's closing question whether the Externe Ebene is the real world of the therapists or another simulation level (L168) — a question, write it as one.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L123. occurrence unless more: `Genesis der Existenz` is the prologue the report would cut (L123, L151) — read on genesis only if it says what the prologue holds (L123: AEGIS's evolution in the Nothing).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L58. minor (1): KW3, Cerberus, „Klaustrophobisch, labyrinthisch, paranoid“ (L58).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L17, L47, L49, L178. minor (1–2): the Guardians represent defence mechanisms and cognitive functions (L17); the table of their blind spot regarding Juna (L49, L55–L59).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L19, L29, L39, L43, L49, L55, … (12 lines). central (3–5): an external ontological anomaly, standing for connection and healing (L19); deleted as error by AEGIS (L29); the guardians' blind spot regarding her (table header L55, `Partnerin`); the recommendation that she not be reduced to a „Manic Pixie Dream Girl“ and get goals of her own, as representative of Monstrous Moonshine (L161).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L37, L39, L43, L47, L61, … (20 lines). central (4–6): the „Host“ of a system split into ten Alters (L17); the Monster Group as metaphor for his psyche, irreducible (L37), his search for prime factors as `Kohärenz-Verifikator`; table row Kael (Host), Manager (ANP), amnesia, POV (L80); Teil 1 and Teil 2 (L97–L99): Universal Reboot, LogOS's validation test failed by Gödel, „funktionalen Multiplizität“, from „Architekten“ to „Gärtner“; the critique of his passivity (L141–L143) and the recommendation of active resistance (L162).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L59. minor (1): sees only chaos and potential, misses reintegration (L59).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L17, L47, L178; `Kern-Welt` L17, L47, L55, L178. minor (1–2): four Kern-Welten each watched by a Guardian (L17, L47), materialising the theory of structural dissociation; the table (L53–L59) with KW1–KW4.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L37, L47, L71, L91, … (13 lines). central (1–2): healing called „Kohärenz“ (L71), not the annihilation of the Alters; the Mosaik-Herz as a new „residierende Kohärenz“ (L91); else the title (J9) — occurrence for title lines.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L43, L56, L61, L97, L129, L152, … (7 lines). minor (1–2): KW1, LogOS, „Hypergeometrisch, kristallin, deterministisch, steril“ (L56); the Uncanny-Valley aesthetic, energy lines and silence (L61); the novel begins there after a Universal Reboot (L97).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L56, L97, L157. minor (1–2): KW1's guardian, sees emotions as noise (L56); the validation test of Teil 1 (L97); the recommended scene of LogOS „repairing“ Kael's grief (L157).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L57. minor (1): KW2's guardian, mistakes the partner for a closed scar (L57).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L59. minor (1): KW4, `Kairos & Sophia`, „Fließend, dynamisch, emergent“ (L59).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L91. minor (1): a metaphor for a new coherence „die Widersprüche aushält“ (L91).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L71. minor (1): „funktionalen Multiplizität“ as Kael's first step after the failed test (L97).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L151. minor (1): the fight against the „Nichts-Rauschen“ in the cut prologue's background (L151).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L87, L131. minor (1): Exile (Trauma-Halter), the Freeze response (L87).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L55. minor (1): Juna as „Partnerin“ in the table's blind-spot column (L55–L59).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L57, L152. minor (1): KW2, Mnemosyne, „Nicht-linear, traumgleich, neblig“ (L57).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L97; `Risse` L31. minor (1): the Glitches linked to Juna that Kael meets (L97); `Risse` at L31 only if the line says more.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L89. minor (1): Manager / Caretaker, „Der Pflegende“, promotes the „Wir-Geflecht“ (L89).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L59, L151. minor (1–2): seeks integration by eliminating differences (L59); the recommendation that the Genesis lore come late, in a dialogue with the Guardian *Sophia* (L151).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L31. not read: `Simulation` only in passing (L31) — occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`), `Zero-Trust-Architektur` (near `zerotrust`). occurrence: `Guardian` is the world guardians, `Zero-Trust-Architektur` (L47) AEGIS's segmentation in passing — on kern-welten if at all.
- `genesis`: `Genesis der Existenz` (near `genesis`). as above: the prologue's title.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — L97 (on the page above).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a child Alter (L86, L156), not the residual echoes.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: position 1 again, „Autonomous Entropic Gatekeeper for Integrity Systems“ (L17), in a report of 2026-02-23 that cites its reference 1.
- **`c11-landauer-warmth-or-cold-ozone`**: the Landauer heat as the report's account of the concept, „digitale Abwärme“ (L31), and its closing question where it accumulates (L169) — no chapter, no ozone; record only if the reader finds it adds to the record, else skip and say so.
- **`c13-externe-ebene-beyond-the-simulation`**: the report asks, and does not answer, whether the Externe Ebene is the real world of the therapists or a further simulation level (L168).
- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten KW1–KW4 (L56–L59) and ten Alters, its table naming Kael, Limina, Index, Nox, Praetor, Eos, Echo, Oblivion, Flicker, Silas (L80–L89). Append dated 2026-02-23, before the author's answers of 2026-10-05, changing neither.
- **`q5-guardians-and-kern-welten`**: LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, `Kairos & Sophia`–KW4, each with a blind spot regarding Juna (L56–L59).

**Not promoted:** the IFS categories (L65–L69); the Monster Group, Monstrous Moonshine, Gödel, autopoiesis (L35–L43) — the report's account of borrowed concepts; Limina, Index, Nox, Praetor, Eos, Echo, Flicker — Alters with no page, on Q3; the literary comparisons (Egan, Pynchon, Asimov, Ruff, Chiang, L109–L113); McL-Sigma-3, Beta-Rho-5, Daten-Parasit, Wir-Geflecht, Kohärenz-Verifikator; `Manic Pixie Dream Girl`.

**Split into two readers, one after the other:**
- Reader 1: aegis, entropie, juna, kohaerenz, externe-ebene, nichts-rauschen, did, emergenz, entropie-signatur, genesis, risse, mosaik-herz, partnerin, and the entries c1, c11, c13.
- Reader 2: kael, alters, multiplizitaet, kern-welten, guardians, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, logos, mnemosyne, cerberus, kairos, sophia, oblivion, silas, and the entries q3, q5.
