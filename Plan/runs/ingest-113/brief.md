# Brief — readings from document 113 (step 6)

1 document, one reader, one batch: `ingest-113`. Files go to `Plan/runs/ingest-113/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 113 | `welt` | 2025-07-29 | „the Welt blueprint“ (titled `Weltenbau & Setting – „Kernwelten & Die Realitätsebenen“`) | a German answer of 2025-07-29 in an advisor's voice („Ah, mein geschätzter Kollege“, L28) to a research question on the six reality levels: a first pass profiles KW1–KW4, the Überwelt and the Externe Ebene with bracketed source notes `[aus voriger Antwort]` (L34–L78); a second pass repeats them under a new template and adds the Potentialmeer and the Fundament (L82–L146), then the interactions (L148–L158). It calls itself a „Bauplan“ (L32, L80) and hedges (`könnte`, `möglicherweise`) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (161 lines for `welt`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A blueprint in an advisor's voice: write „the Welt blueprint describes / profiles …“, keep its hedges (`könnte`, `möglicherweise`, `vielleicht`) as hedges, and say when a line is the first pass (L34–L78) or the second (L82–L158) where the two differ. Its world names are double: `Logos-Prime / Konstrukt-Stadt`, `Mnemosyne-Archipel / Resonanz-Landschaft`, `Cerberus-Labyrinth / Grenzfeste`, `Kairos-Potentialis / Möglichkeits-Garten` (J49: the first half is a world name, not the guardian's page). Kael is male. No chapter numbers; „im zweiten Akt“ (L122) only.

## Pages — document 113, `welt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L30, L36, L40, L41, L42, … (32 lines); `Entropic Gatekeeper` L70, L119. minor (2–3): the four Kernwelten made by AEGIS as labs (L36); the Überwelt its meta-level (L68); its function as „Entropic Gatekeeper“ (L70); AEGIS as a process (L119) — read only what the lines say.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L54. minor (1): KW3 the domain of Alex (Protektor-ANP) with Nyx (L54).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L52, L54, L102, L107. minor (1): the Guardian Kael meets in KW3 (L107); the world name Cerberus-Labyrinth is J49's, not a reading.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L61. occurrence unless more: `Emergenz` in KW4's lists (L61, L63, L110); read only if a line says what Emergenz is here.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L42. minor (1): the Überwelt defined by information theory and thermodynamics, Shannon entropy and data decay (L70); else occurrence.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L26, L73, L75, L84, L124, L128. minor (2–3): a mysterious level tied to Juna/V outside AEGIS's direct control, acting as „Moonshine-Link“ (L75); heading „Das Unbekannte Jenseits der Simulation“ (L124); possibly another reality or a healthy inner world before the fragmentation (L128); „ein offenes Rätsel“ (L130).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L138. occurrence unless more: AEGIS's „Genesis“ as negation (L138) — on potentialmeer; occurrence here.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L52, L102. minor (2–3): `KW3: Cerberus-Labyrinth / Grenzfeste`, domain of Alex and Nyx (L52, L54); brutalist, fortified (L55, L105); Kael meets the Guardian Cerberus (L107).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L122, L158. minor (1–2): each Kernwelt coupled to an AEGIS-Guardian (L88); the Überwelt their primary stage (L122); „keine anthropomorphen Avatare“, localised processes or fields (L158).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L61. minor (1–2): the Externe Ebene tied to Juna/V (L75, L126); Juna/V the counter-principle to AEGIS's cold logic (L75); her „Ankerpunkt“ a specific place (L130).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L30, L36, L40, L47, L50, … (24 lines). minor (2–3): the worlds externalise Kael's psyche (L30, L84); his Alters by world (L40, L54, L61); his journey begins in KW1 amnesic (L95); the Fundament as his ultimate understanding of the pattern (L146).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L11, L26, L34, L36, L68, L69, … (11 lines). central (2–4): four AEGIS-made, thematically specialised simulation environments representing Kael's psychic landscape, labs for AEGIS to analyse him (L36, L88); each coupled to a psychological domain and an AEGIS-Guardian (L88); their different logics (classical, FDE, relevance, dialetheic) mirror AEGIS's handling of contradiction (L36, L49, L56, L63).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L28. not read: the protocol's name and the title (L28, L40, L80) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L38, L90. minor (2–3): `KW1: Logos-Prime / Konstrukt-Stadt`, the domain of Lex, Kael's rational ANP, AEGIS's rigid order (L38, L40); sterile, geometric, shadowless light, classical logic (L92–L93); where Kael's journey begins, amnesic, and the first Risse appear (L95).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L40, L92. minor (1): KW1 the domain of Lex, Kael's rational ANP (L40, L92).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L61. minor (1): KW4, Lia (Kind-EP, Ambivalenz) (L61).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L59, L108. minor (2–3): `KW4: Kairos-Potentialis / Möglichkeits-Garten`, domain of Lia, Rhys and Selene (L59, L61); the „Möglichkeits-Weber (Ly)“ embodying potentiality (L61); the „Nexus-Interface Garten“ as a place in it (L111).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L75. minor (1): the Externe Ebene „fungiert als „Moonshine-Link““ offering an alternative coherence of resonance and empathy (L75).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L138. minor (1): AEGIS's genesis defined by preventing its dissolution into this „Nichts Rauschen“ (L138), named as the Potentialmeer.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L54. minor (1): KW3, Nyx (Kampf-EP) (L54).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L68, L70, L84, L119, L132, L134. minor (2): the undifferentiated pre-cosmic ground, „nicht Nichts, sondern die Möglichkeit von Allem“ (L134), active ontological pressure against AEGIS (L136); AEGIS's genesis as the negation of dissolving into this `Nichts Rauschen` (L138).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L11, L16, L26, L28, L32, L80, … (7 lines). central (2–3): „die sechs Realitätsebenen“ — four Kernwelten, the Überwelt, the Externe Ebene (L26); the second pass adds the Potentialmeer and a Fundament beneath (L84).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L96. minor (2–3): `KW2: Mnemosyne-Archipel` (L45), in the second pass `Mnemosyne-Archipel / Resonanz-Landschaft` (L96); the domain of the EPs, a trauma landscape, FDE logic (L47, L49, L98); Kael searches the `Mnemosyne-Archiven` (L47).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L61. minor (1): KW4, Rhys (Pflegender ANP) (L61).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L26, L43, L47, L50, L57, L64, … (16 lines). central (2–4): each world's „Manifestation von „Rissen““ (L43, L50, L57, L64, L71, L78) and `Risse & Entropie` (L94, L100, L106, L112, L121); Risse as system instability, short circuits between levels (L152); they correlate with compute-heavy events (L71).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L61. minor (1): KW4, Selene (das Selbst) (L61).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L26, L66, L68, L69, L76, L84, … (12 lines). central (2–4): the meta-level of AEGIS, its control centre and code level, not experienced like the Kernwelten, regulated by the AEGIS-Protokoll (L68, L117); a „Labor nach innen“ (L119); the primary stage of the Guardians, Kael's exploration of it in the second act as a hacking of AEGIS's ontology (L122); the Universal Reboot as a wave of pure information (L122).
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — `Vergessener Schrein` L48. minor (1): a cave „vgl. Vergessener Schrein“ as one possible element of KW2 (L48).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Architektur` (near `zerotrust`). occurrence: `Zero-Trust-Architektur` (L77) is what the Externe Ebene can bypass — on externe-ebene if at all.
- `entropie`: `Shannon-Entropie` (near `entropie`), `Risse & Entropie` (near `entropie`). `Shannon-Entropie` (L70) on entropie above; `Risse & Entropie` is a field label — occurrence.
- `juna`: `Juna/V` (near `juna`), `Juna/V-Verbindung` (near `juna`). J34: `Juna/V` is Juna; `Juna/V-Verbindung` (L61) the connection — on juna above.
- `junas-ankerpunkt`: `Ankerpunkt` (near `junasankerpunkt`). a reading: Junas „Ankerpunkt“, a specific place where her connection becomes manifest (L130).
- `kairos`: `Kairos-Potentialis / Möglichkeits-Garten` (near `kairos`), `Kairos-Potentialis` (near `kairos`). J49: `Kairos-Potentialis` is a world name — on moeglichkeits-garten, occurrence here.
- `kohaerenz`: `Kohärenzprotokoll` (near `koharenz`). occurrence: `Kohärenzprotokoll` is the protocol's name (L40).
- `logos`: `Logos-Prime / Konstrukt-Stadt` (near `logos`), `Logos-Prime` (near `logos`). J49: `Logos-Prime` is a world name — on konstrukt-stadt, occurrence here.
- `mnemosyne`: `Mnemosyne-Archipel / Resonanz-Landschaft` (near `mnemosyne`), `Mnemosyne-Archipel` (near `mnemosyne`), `Mnemosyne-Archiven` (near `mnemosyne`). J49: `Mnemosyne-Archipel` a world name — on resonanz-landschaft; `Mnemosyne-Archiven` (L47) the archives in that world — on resonanz-landschaft; occurrence here.
- `nexus`: `Nexus-Interface Garten` (near `nexus`). occurrence: `Nexus-Interface Garten` is a place in KW4 (L111) — on moeglichkeits-garten.


**Record entries** (one file each):

- **`c13-externe-ebene-beyond-the-simulation`**: the heading „Das Unbekannte Jenseits der Simulation“ (L124) beside „außerhalb von AEGIS' direkter Kontrolle“ (L75, L126) and its open nature (L128, L130) — a side, hedged.
- **`q1-guardians-and-aegis`**: the Guardians as „lokalisierte, dynamische Prozesse oder Felder“, pure information constructs whose existence is their function in the AEGIS-Protokoll (L158); each Kernwelt coupled to „einen AEGIS-Guardian“ (L88).
- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten with their Anteile — KW1 Lex, KW2 the EPs, KW3 Alex and Nyx, KW4 Lia, Rhys and Selene (L40, L47, L54, L61); append dated 2025-07-29, before the author's answers of 2026-10-05, changing neither.
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as AEGIS's meta-level and code level (L68, L117); a `Nexus-Interface Garten` as a place in KW4 (L111) — no Nexus or Überraum otherwise.
- **`q9-moonshine-link-boundary`**: the Externe Ebene „fungiert als „Moonshine-Link““ (L75), a non-local, sub-protocol connection that may bypass AEGIS's Boundary Protocols (L77).

**Not promoted:** Psycho-Architekturen, Environmental Storytelling, the logics (FDE, relevance logic, dialetheism, classical) — the blueprint's frame and borrowed concepts; the Fundament (L140–L146) — a level named here, on realitaetsebenen; Möglichkeits-Weber (Ly), Echowald, Nexus-Interface Garten, the Mnemosyne-Archiven — places and a figure named once, on their world's page; Post-Reboot-Zustand; `Glitch in the Matrix` — a trope.

**Split into two readers, one after the other:**
- Reader 1: kern-welten, realitaetsebenen, ueberwelt, externe-ebene, potentialmeer, nichts-rauschen, aegis, guardians, risse, moonshine-link, juna, junas-ankerpunkt, entropie, and the entries c13, q1, q6, q9.
- Reader 2: konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, vergessener-schrein, kael, lex, alex, nyx, lia, rhys, selene, cerberus, and the entry q3.
