# Brief — readings from document 100 (step 6)

1 document, one reader, one batch: `ingest-100`. Files go to `Plan/runs/ingest-100/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 100 | `roman-entwicklung-kohaerenz-und-leitfragen` | 2026-02-23 | „the Leitfragen report“ (titled `Systemische Tiefenanalyse und strategische Leitfragen zur narrativen Architektur von "Kohärenz Protokoll"`) | a German analyst's report of 2026-02-23 that reviews the project's master documents before automated chapter generation and poses ten open guiding questions, each with a status quo, the cracks it finds, the question and its sources; it settles nothing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (215 lines for `roman-entwicklung-kohaerenz-un`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A review: write „the Leitfragen report finds …“, „reports that the documents …“, „asks …“. **Most of what it says is its account of other documents** (its numbered sources 2, 5, 10, 11, 18, 31 …): say so every time — „the report cites a character concept with ten alters“ — never as the novel's state. Its own judgements („von außergewöhnlicher Qualität“, L177) and its demand for a „Ground Truth“ (L121) are recorded, not applied. Footnote digits glued to words (`Kapitel 3.10`) are reference markers; quote around them.

## Pages — document 100, `roman-entwicklung-kohaerenz-und-leitfragen`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L35, L50, L69, L73, L75, … (19 lines). minor (2–3): the Autopoiesis-System (L23); an „Entropie-Torwächter“ on a Zero-Trust-Architektur with Boundary Protocols against „Cross-Contamination“ (L83); its deletion of information as the cause of the world's decay (L139); the „Universal Reboot“ AEGIS initiates (L117, L119).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L46, L60, L63, L65, L143, L167, … (7 lines). central (2–3): the report's account of two rosters — 13 entities in a „Tiefenanalyse“ (Brief Julia) with Kael, Isabella, Data, Shadow, Lia, The Lost One, and exactly ten alters in a character concept: Kael, Limina, Nox, Echo, Flicker, Eos, Oblivion, Praetor, Index, Silas (L46); its five-row table with functions and Kernwelten (L56–L61).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L94, L105, L109. minor (1–2): system integrity and defence, every ambiguity a „Cyber-Angriff“ (L105).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L17. minor (1): DIS/DID as the condition behind the main figure, with a personal background (L17).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L95. minor (1) only if L95's `Emergenz` (Ly's psychology) says more than a table cell; else occurrence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L50. minor (1–2): AEGIS's deletion of information produces thermodynamic entropy, „digitale Wärme“ (L139); `Entropie-Torwächter` (L83).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L111. not read: `Genesis der Existenz` at L111 is a cited document's title — occurrence.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L77, L157. minor (1–2): the „Parakonsistentes Gambit“ and the „lebenden Gödel-Satz“ of the finale, Kapitel 36–39 (L69); the question how Kael proves AEGIS's incompleteness (L73, L75).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L58, L59, L81, L94, L105. minor (1–2): B, protectors and paranoia, Cerberus, the Baby-Monster group (L94).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L99, L103, L105, L109, L111, L211, … (7 lines). minor (2): the Guardians as AEGIS's agents and diagnostic instances (L103); LogOS and Mnemosyne profiled, Cerberus, Kairos and Sophia weaker (L105).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L19, L21, L23, L27, L34, L38, … (11 lines). central (2–3): the emotional anchor from the „Externen Ebene“, used synonymously with „V“, the Impact Character in Dramatica's domain Psychology (L23); four possible natures (L23); its question of Juna/V against Nova Ardent (L27, L34, L38).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L23, L25, L27, L35, … (33 lines). central (3–4): the protagonist, „Protagonisten Kael“ (L21), male; the report's account that in Kapitel 3 Kael, „Elite-Cybersoldat der Aegis Coalition“, is ordered to eliminate Nova Ardent (L25); the host ANP of the ten-alter table, KW1 (L57); its question whether Kael is a simulated avatar, a construct or a sub-process of Dr. Aris Thorne (L119); the persönlicher Hintergrund of Kael and DID (L17).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L95, L105, L107, L109. minor (1): the „Möglichkeits-Weber“ in the Lyons-Welt, Kapitel 26–29 (L107).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L48, L63, L79, L81, L97, L99, … (8 lines). central (2–3): four Kernwelten as ecological manifestations of Kael's inner landscape (L81); the table pairing each with psychology, Guardian, mathematical paradigm and an open transition mechanism, and **the early names in brackets — Konstrukt-Stadt (Co₁), Resonanz-Landschaft (McL), Grenzfeste (B), Möglichkeits-Garten (Ly)** (L92–L95).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L149, L153, L159. minor (1–2): the end, Kapitel 39 → 40/0, based on Kishōtenketsu, Ten to Ketsu as the climax (L153).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the novel's title (J9) — occurrence.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L35, L57, L81, L83, L92, L103, … (8 lines). minor (1–2): Co₁, the ANPs and rationality, LogOS, the Conway group, initialised by the reboot (L92); Kapitel 1's architectural storytelling (L81).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L46. minor (1): an EP in the 13-entity roster (L46).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L92, L103. minor (1–2): its blind spot toward the Partnerin — a category error, Juna fits no logical operator (L103).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L93, L103. minor (1–2): its blind spot — it misreads the Partnerin's presence as a past scar (L103).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L81, L95, L105. minor (1–2): Ly, creativity and potential, Kairos / Sophia, the Lyons group (L95); `Möglichkeits-Garten / Nexus` (L105).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Moonshine-Link` alone on L34. minor (1): Juna as the external „Moonshine-Verbindung“ (L27), the Moonshine-Link in the table (L34).
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L105. minor (1): `Möglichkeits-Garten / Nexus` for Kairos and Sophia (L105) — the slash, nothing more.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L119. minor (1): the reboot because the „Nichts Rauschen“ broke in (L119).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L46, L61, L167. minor (1–2): one of the ten — „Oblivion (Freeze)“ (L46), Freeze / trauma-holder in the Resonanz-Landschaft (L61).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L103. minor (1): the Partnerin (Juna) toward whom LogOS and Mnemosyne have their blind spots (L103).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L48. not read: `Personas` (L48) is the ordinary plural, not the page — occurrence.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L23, L73. minor (1): one of Juna's possible natures, a manifestation of the „Potentialmeers“ (L23); the collapse visualised in the Lyons-Welt or the Potentialmeer, Kapitel 37 (L73).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L48, L60, L61, L81, L83, L93, … (7 lines). minor (1–2): McL, the EPs and trauma, Mnemosyne, the McLaughlin graph (L93); „Welt 2“ where the EPs reside (L48).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L85, L115, L139; `Risse` L17, L50, L85, L139, L141, L147. minor (1–2): Glitches and Risse from the host's avoidance (L50); Landauer's digital heat; whether the Risse are transport channels (L85).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L46. minor (1–2): one of the ten — „Silas (Caretaker)“ (L46); distinguish him from `Silus`, who administers the simulation in the early drafts (L115) — the report writes both and does not connect them.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L95, L105, L107, L109. minor (1): the AEGIS-conform „Synthesis“, set against organic integration (L107).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L25, L35, L42, L44, L46, L56, … (9 lines). minor (1–2): TSDP and IFS as the blueprint for Kael's consciousness (L44); the ANPs' phobia of the EPs (L50).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L25. not read: `Simulation` is the ordinary word for AEGIS's world here, not the Überwelt (L25) — occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`), `Zero-Trust-Architektur` (near `zerotrust`), `Zero-Trust-Firewall` (near `zerotrust`). occurrence: `Guardian` and the Zero-Trust compounds are AEGIS's architecture as the report describes it, not its sub-functions — read on aegis.
- `entropie`: `Entropie-Torwächter` (near `entropie`). reading, above: `Entropie-Torwächter` with L139.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence: the title (J9); `Kohärenztheorie der Wahrheit` a borrowed theory (J16).
- `mosaik-herz`: `Mosaik-Herzens` (near `mosaikherz`). reading on mosaik-herz: the finale as a possible triumph of the „Mosaik-Herzens“ (L155).
- `personas`: `Apparently Normal Personality` (near `persona`). occurrence: `Apparently Normal Personality` is the clinical term (J69).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a child alter in the ten-alter roster (L46, L60), not the residual echoes — read on alters.


**Pages the census reaches only by the sentence:**

- **`landauer-signatur`** (minor, 1–2): Landauer's principle applied — deleting information produces „digitale Wärme“, AEGIS's order the cause of the Risse (L139); its sensory form and the „Daten-Parasit“ (Leech / Glitchwyrm) that feeds on it (L141–L145).
- **`algorithmische-melancholie`** (minor, 1): whether the Gödel trap leads to the described „Algorithmischen Melancholie“ (L73).
- **`blinder-fleck`** (minor, 1–2): the Guardians' „Blinde Fleck“ toward the Partnerin, rooted in their epistemology (L103); the question of Cerberus's, Kairos's and Sophia's blind spots (L109).
- **`mosaik-herz`** (minor, 1): the finale as a triumph of the „Mosaik-Herzens“ that gains autonomy, or a Sisyphus insight (L155).
- **`externe-ebene`** (minor, 1): Juna as an entity from the „Externen Ebene“ (L23).

**Not promoted** (no page): Nova Ardent (person, EP, Kapitel 3 target; and the catastrophe), Dr. Aris Thorne, Silus, the ten-alter names Limina, Nox, Echo, Flicker, Eos, Praetor, Index, the Daten-Parasit / Glitchwyrm, Neon Ashes, New Zenith, Universal Reboot, ARCHON / LeanRAG / NCP, the mathematical paradigms.

**Record entries** (one file each; the report's accounts of other documents, said as such):

- **`q3-how-many-kern-welten-and-alters`**: two rosters reported — 13 entities and ten named alters (L46) — and its question which is canon (L63); the four Kernwelten with the early names Co₁, McL, B, Ly in brackets (L92–L95), the first read source to set those names beside today's. Q3 ends with the author's two answers of 2026-10-05: append with the date 2026-02-23, say it predates both and changes neither; never edit the author's sections.
- **`c11-landauer-warmth-or-cold-ozone`**: „digitale Wärme“ from deletion (L85, L139), with visual heat shimmer (L143) — warmth, not cold.
- **`c4-guardians-and-aegis`**: only if the record's question is the blind spot's bearers — the Guardians' blind spot toward the Partnerin (L103); else skip and say why.
- **`q5-guardians-and-kern-welten`**: one Guardian per world, KW4 held by „Kairos / Sophia“ (L92–L95).
- **`q6-nexus-ueberraum-ueberwelt`**: `Möglichkeits-Garten / Nexus` (L105).
- **`c16-kael-origin`**: its question whether Kael is a simulated avatar, a psychological construct or a sub-process of Dr. Aris Thorne (L119), and the early drafts' real world of Dr. Thorne (L115).
- **`q8-aegis-after-the-vortex`**: the end as a recursive reset, Kapitel 40/0, the „Neon Ashes“ (L117, L153–L157); no Vortex.

**Chapter readings** are in `Plan/runs/ingest-100-kap/brief.md`.

**Split into three readers, one after the other:**
- Reader 1: kael, juna, aegis, alters, oblivion, silas, lia, tsdp, did, goedel-gambit, algorithmische-melancholie, kishotenketsu, mosaik-herz, risse, entropie, landauer-signatur, potentialmeer, nichts-rauschen, moonshine-link, externe-ebene, emergenz.
- Reader 2: kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, guardians, logos, mnemosyne, cerberus, kairos, sophia, partnerin, nexus, blinder-fleck.
- Reader 3: the record entries above, and then the chapter readings.
