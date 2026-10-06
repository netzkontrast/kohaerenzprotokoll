# Brief — readings from document 111 (step 6)

1 document, one reader, one batch: `ingest-111`. Files go to `Plan/runs/ingest-111/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 111 | `plot-analyse-und-romanentwicklung` | 2026-02-22 | „the plot analysis“ (titled `Novel Writing Assistent: Umfassende Plot-Analyse und Weiterentwicklung des 'Kohärenz Protokolls'`) | an assistant's advice to the author of 2026-02-22, in German, second person: it reports the author's uploaded documents (a numbered reference list, L166–L218, items 1–4 and 6 the author's own) and proposes changes — slower pacing in Kap 1, an IFS table of the four worlds, Murdock's seven phases, Gödel, Moonshine and paraconsistent logic for the finale |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (218 lines for `plot-analyse-und-romanentwickl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Advice: two voices, kept apart in every reading. What the document **reports** from the author's documents (marked by a reference number, mostly 1 = `Kohärenz Protokoll`, 3 = the novel draft, 8 and 14 concepts) is written „the plot analysis reports …“; what it **proposes** (its five labels `Narrative Umsetzungsempfehlung`, `Konkrete Handlungsempfehlungen zur Plot-Optimierung`, `Inkonsistenz-Warnung`, `Narrative Integration`, `Handlungsanweisung für das Finale`, and every „sollte“, „lassen Sie“) is written „the plot analysis proposes …“ — never as the novel's fact. The mathematics (Gödel, Moonshine, paraconsistent logic, Landauer) is the assistant's applied metaphor. Kael is male (`er`, `seinen`).

## Pages — document 111, `plot-analyse-und-romanentwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L27, L31, L33, L43, L69, … (21 lines). central (3–5): the expansion „Autonomous Entropic Gatekeeper for Integrity Systems“ (L23); the reported self-definition by negation (L23, ref. 1); AEGIS eliminating Shannon entropy through the ZTEM, filtering and erasing memories (L27); the proposed irony that the harder it fights chaos the more heat it makes (L33); the proposed Gödel reading — why AEGIS cannot simply delete Juna (L105–L109); the finale: Kael sends his state to PMAS (L135).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L27. minor (1): `Zero-Trust Execution Model` (ZTEM) as AEGIS's means against Shannon entropy (L27), reported with ref. 3.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L63, L69, L117, L121, L133, L143, … (7 lines). minor (1–2): „nicht alle zehn Alters gleichzeitig agieren“ (L63) — the count is the document's; the Alters as „Symmetrie-Dimensionen“ (L121).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L72, L75, L119, L148. minor (1–2): row 3's guardian (L72); the `Inkonsistenz-Warnung` — Cerberus and Nox on the same misguided premises (L75); trying to isolate Kael from Juna (L148).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L15. minor (1): DID not as a horror trope but as an adaptive survival strategy (L57), reported as the author's concept with ref. 15; a DID system is inherently contradictory (L129).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L73. minor (1): row 4's function „Raum für kreative Emergenz“ (L73) — read only if more than a cell; else occurrence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L15. minor (1–2): Shannon entropy (unpredictability) against thermodynamic entropy released as heat by the Landauer principle, „der thermodynamische Preis der Ordnung“ (L27–L29) — the assistant's application.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L109. minor (1–2): Juna and the Externe Ebene „existieren *außerhalb* dieses Systems“ (L109); Juna as the j-function from the Externe Ebene (L117); the bridge to Juna (L121) — note the doc writes `Externen Ebene` too.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L15. minor (1): `Genesis der Existenz` named as the metaphysical document the author uploaded (L15, and ref. 2 at L169) — read only if it says more than the title; else occurrence.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L72, L75, L148, L160, L162. minor (1–2): row 3 — Cerberus, Firefighter/Protectors, Praetor, Nox, Oblivion (L72); called `Beta-Rho-5` (L75).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L63, L119, L145, L181. minor (1–2): the confrontations proposed as epistemological and psychological debates, not fights (L145); the guardians declaring the Kael–Juna link „Moonshine“ (L119).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L41, L83, L91, L105, L109, L117, … (11 lines). central (3–5): her face flickering in the draft's Kap 1 (L41, reported from ref. 3); partitioned at the Universal Reboot (L83); met in the descent (L91); the proposed Gödel sentence for AEGIS (L109) and j-function (L117); Cerberus trying to isolate Kael from her (L148).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L27, L31, L37, L41, L43, L45, … (38 lines). central (4–8): the unknowing „Host“, an ANP, waking after a universal reboot (L41); the reported Kap 1 draft and the pacing problem (L41–L43); the proposal: no explicit emotions in the first chapters, „der logische Verifikator“ dominated by a Manager part (L45), somatic signs instead (L49–L51); Murdock's seven phases on him (L83–L95: Gamma-Phi, `Kohärenz-Optimierer Stufe 2`, IP-K1123 at Beta7, the descent, the Mosaik-Herz); the finale — Kael *und* M (L133), PMAS (L135).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L73. minor (1): row 4's guardian `Kairos / Sophia` (L73); the document does not say one guardian or two.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L15, L31, L61, L63, L113, L160, … (7 lines). central (2–3): the proposed table assigning each Kern-Welt a guardian, an IFS category, Alters and a narrative function (L67–L73), introduced as the assistant's structuring (L63); the worlds mirror the IFS model fractally (L63, ref. 8). The world symbols after the names are lost in export (L70–L73).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title and the protocol's name (L11, L13, L63, L156) — occurrence (J16).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L31, L37, L70, L83, L85, L141, … (8 lines). minor (1–2): row 1 of the table — LogOS, Manager (ANP), Kael, Index, Limina (L70); the draft's Kap 1 `Welterkundung Konstrukt-Stadt` with Uncanny-Valley architecture (L37); the maintenance drones proposed for Kap 1–3 (L141).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L70, L93, L109, L119, L129, L150. minor (1–2): row 1's guardian (L70); the logic Murdock's phase 6 says must be healed, not destroyed (L93); classical logic of LogOS and AEGIS (L129).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L53, L71, L147. minor (1–2): row 2's guardian (L71); proposed to hold Kael in a loop of nostalgia or trauma, thinking that healing (L147).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L73, L160. minor (1–2): row 4 — Kairos / Sophia, Exiles & Emergent Parts, Echo, Flicker, the Selbst (L73); written `Möglichkeiten-Garten` and `Ly-Welt` at L121, where the Moonshine metaphor is proposed.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L95, L117. minor (1–2): accepted in Murdock's phase 7 (L95); the integrated Kael „das Mosaik-Herz mit all seinen Alters“ as the monster group (L117).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L45. minor (1): the proposal to slow recognition „um die spätere Wucht der Multiplizität zu erhöhen“ (L45).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L23, L91. minor (1–2): reported as an active sea of potential, `Śūnyatā` (L23); proposed as the liminal space of Murdock's phase 5, the descent (L91).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L72. minor (1): row 3, `Oblivion` (Freeze) (L72).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Potentialmeer` alone on L23. minor (1): the „aktives Potentialmeer (Śūnyatā)“ that the Nichts Rauschen acts as (L23).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L53, L71, L143, L160. minor (1–2): row 2 — Mnemosyne, Manager & Caretaker, Silas, Eos, Sub-Netzwerk Gamma-Phi (L71); the second world where the emotional barriers give way (L53); it „reagiert auf Emotionen“, called `McL-Welt` (L143).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L25, L31, L51. minor (1–2): the proposal that the Risse be zones of „digitaler Abwärme“ (L31), not only visual glitches; the crack in Transitkorridor 3 reported from Kapitel 1 (L31); the smell of damp earth kept as a subtle warning (L51).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L71. minor (1): row 2, `Silas` (Caretaker) (L71).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L73. minor (1): row 4's `Kairos / Sophia` (L73).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L21. not read unless it says more: `Simulation` only in a heading and „Realitätssimulation“ (L19, L21) — occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust Execution Model` (near `zerotrust`). a reading — the ZTEM line L27 (on the page above).
- `entropie`: `Shannon-Entropie` (near `entropie`). a reading — `Shannon-Entropie` L27 (on the page above).
- `genesis`: `Genesis der Existenz` (near `genesis`). occurrence: the title of an uploaded document (L15, L169).
- `kohaerenz`: `Kohärenz Protokolls` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Optimierer Stufe 2` (near `koharenz`), `Cache-Inkohärenz` (near `koharenz`). occurrence: the protocol's name and the title (L11, L13, L63, L156); `Kohärenz-Optimierer Stufe 2` (L87) is a rank, reported from ref. 1 — on kael; `Cache-Inkohärenz` (L150) the conflict the syntax should mirror — on kael if at all.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a child Alter's name (L73, L143), not the Residual-Echos.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: position 1 again, „Autonomous Entropic Gatekeeper for Integrity Systems“ (L23), in a report of 2026-02-22 that names its source as ref. 1.
- **`c11-landauer-warmth-or-cold-ozone`**: the proposal that the Risse be zones of „digitaler Abwärme“ where the air smells of burnt ozone (L31) — heat and ozone together, and its Kap 1–3 drones whose repair costs light/heat (L141); a proposal, not a chapter's fact.
- **`c13-externe-ebene-beyond-the-simulation`**: Juna and the Externe Ebene exist „*außerhalb* dieses Systems“ (L109), the formal system of AEGIS.
- **`q3-how-many-kern-welten-and-alters`**: „nicht alle zehn Alters“ (L63) beside a table that names Kael, Index, Limina, Silas, Eos, Praetor, Nox, Oblivion, Echo, Flicker and the Selbst (L70–L73) — the document's own count beside its own list; append dated 2026-02-22, before the author's answers of 2026-10-05, and changes neither.
- **`q5-guardians-and-kern-welten`**: the pairing LogOS–Konstrukt-Stadt, Mnemosyne–Resonanz-Landschaft, Cerberus–Grenzfeste, Kairos / Sophia–Möglichkeits-Garten (L70–L73), with IFS categories.

**Not promoted:** the IFS categories (L59), Murdock's phases (L83–L95), Gödel, Monstrous Moonshine, the j-function, paraconsistent logic (L107–L131) — borrowed concepts the assistant applies; Index, Limina, Eos, Praetor, Nox, Flicker, Echo as Alters with no page; the place names Transitkorridor 3, Datenknotenpunkt Gamma-7, Sub-Netzwerk Gamma-Phi, Beta-Rho-5, McL-Sigma-3, IP-K1123, Beta7; Wir-Geflecht, Jetzt-Raum, PMAS. The Moonshine-Link (Q9) is not named: the document's Moonshine is a metaphor.

**Split into two readers, one after the other:**
- Reader 1: aegis, aegis-teilfunktionen, nichts-rauschen, potentialmeer, risse, entropie, genesis, ueberwelt, did, kohaerenz, externe-ebene, juna, and the entries c1, c11, c13.
- Reader 2: kael, alters, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, logos, mnemosyne, cerberus, kairos, sophia, guardians, silas, oblivion, mosaik-herz, multiplizitaet, emergenz, and the entries q3, q5.
