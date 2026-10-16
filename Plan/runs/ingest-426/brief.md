# Brief — readings from document 425 (step 6)

1 document, one reader, one batch: `ingest-426`. Files go to `Plan/runs/ingest-426/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 425 | `romanplot-kohaerenz-protokoll-entwicklung` | 2025-04-25 | „the optimised blueprint“ (an unsigned German „Plot-Blueprint (Optimierter Entwicklungsauftrag)“) | a frame with three tables (figures, arcs, borrowed concepts), then 39 numbered steps (`Schritt`) in three acts, character arcs, rendering advice and three open end scenarios; calls itself a robust, flexible template (L580, L585), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (632 lines for `romanplot-kohaerenz-protokoll-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the optimised blueprint plans …“ or „the optimised blueprint's step 4 …“; its steps are hedged proposals, and its end is three scenarios (L479–L481), none chosen. It names no chapter: its units are 39 `Schritt` in Akt 1–3 (L153, L289, L427) — never call a step a chapter. Quote the German as written; cut before straight quotes, bold and italics markers and glued footnote digits (144 of them). No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name nor a term carrying one (the incompleteness theorems, L69, L74, L128), and never quote a span containing one.

## Pages — document 425, `romanplot-kohaerenz-protokoll-entwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L20, L21, L22, L33, … (167 lines). central (4–8): „AEGIS ist durch Trennung, Analyse und Selbsterhaltung mittels Grenzziehung definiert“ (L17); „AEGIS ist als autopoietisches System konzipiert“ (L68); it cannot verify its own consistency, which leads to the Risse (L74 — describe the theorem); „AEGIS ist nicht einfach nur böse“ (L79); AEGIS's inner state *is* Kael's environment, the Kernwelten its externalised analytic processes (L87); the K-J connection its fundamental blind spot (L95); the three end scenarios — collapse, transformation, partial collapse (L479–L481).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L48, L102, L106, L145. minor (1–4): „Kaels Alters (IFS-Teile)“ (L102): protectors as Manager and Feuerlöscher, the Verbannten (L102, L315); the arc from fragmentation to self-leadership (L47, L49).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L21. minor (1–4): Kael's „dissoziative Identitätsstörung (DID) ist keine inhärente Pathologie“ (L21) but a consequence of AEGIS's experiment.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L128. not read: an occurrence — complexity/emergence among Akt II's borrowed emphases (L128).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L20, L38, L68, L118, L127, L149, … (11 lines). minor (1–4): the Potentialmeer as a meta-space „mit hoher Entropie bzw. Möglichkeit“ (L20); entropy among the borrowed concepts of Tabelle 2 (L133–L149).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L103. minor (1–4): „AEGIS Subsysteme/Guardians“: a Guardian programme could embody rigid adherence to protocol and AEGIS's autopoietic self-preservation, another subsystem wrestle with paraconsistent data (L103); step 4 „Der Wächter“ — an AEGIS subsystem in KW2 trying to control Kael's emotional outbursts (L189, L191); the ending asks what became of the subsystems/Wächter (L523).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L22, L36, L89, L91, L94, L143, … (24 lines). minor (1–4): the table: Juna as „Moonshine-Aspekt, Verbindungskatalysator“, external anchor and goal for Kael (L36); „Juna selbst könnte Aspekte dieser Verbindung verkörpern“ (L94); the K-J connection non-local, below AEGIS's protocol level (L22).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L22, L34, L35, L36, … (174 lines). central (4–8): „Als menschlicher Avatar von M dient Kael als primäres Interface und Experimentierfeld für AEGIS“ (L21); the DID not an inherent pathology (L21); Kael begins in fragmentation (L47) and ends in self-leadership and harmony of the inner system (L49); healing and plot are one process (L51); afterwards an open question, whether Kael lives in the Potentialmeer (L550).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L17, L35, L39, L47, L48, L60, … (24 lines); `Kernwelt` L17, L35, L39, L47, L48, L59, … (37 lines). minor (1–4): the table: „Thematische Labore (Logik, Emotion, Angst, Potential)“ (L39); „Die Kernwelten sind Externalisierungen von AEGIS' internen analytischen Prozessen und deren Scheitern“ (L87); their side figures, „Kernwelt-Manifestationen“ (L104); step 10 could take place in any KW or an in-between (L255); scenario A: the Kernwelten dissolve (L479).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L20, L38, L68, L85, L96, L118, … (33 lines). minor (1–4): M exists within the Potentialmeer, „einem Meta-Raum reiner Potentialität mit hoher Entropie bzw. Möglichkeit“ (L20); the table: fundamental setting, source of M, beyond AEGIS's control (L38); „Das Potentialmeer ist der Inbegriff dessen, was AEGIS fürchtet und nicht kontrollieren kann“ (L390); rendering advice: a seething sea of pure potentiality (L570).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L95. not read: an occurrence — „einer tieferen, kohärenteren Realitätsebene“ in the general sense (L96).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L61, L74, L78, L87, L118, L128, … (18 lines). minor (1–4): AEGIS's inability to prove its own consistency leads to systemic instability, „den im Konzept erwähnten“ Risse (L74); the Risse are literal breaks in AEGIS's cognitive architecture (L87); Akt II's emphasis: complexity and system instability, Risse (L128).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L96. minor (1–4): the K-J connection as an ontological intrusion from the Potentialmeer into AEGIS's „künstliche, fragmentierte Simulation“ (L96); the connection needs no classical communication within AEGIS's simulated reality (L22).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading, on moonshine-link below: the K-J connection represents the „Moonshine“ aspect of M (L22, L36).


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–2): the K-J connection represents „den "Moonshine"-Aspekt von M“ — cut before the straight quote (L22); the table gives Juna the „Moonshine-Aspekt“ (L36).

**Record entries** (one file each, formatted as earlier entries — `ls Plan/runs/ingest-42*/readings/q1-*`, `q8-*`):
- **`q1-guardians-and-aegis`**: the optimised blueprint makes Guardians AEGIS's subsystems, personifying its inner conflict (L103), and step 4's „Wächter“ an AEGIS subsystem in KW2 (L189); a plan, recorded, not applied.
- **`q8-aegis-after-the-vortex`**: three end scenarios side by side, none chosen — collapse, transformation, partial collapse/transformation (L479–L481); the ending asks what became of the subsystems (L523).

**Not promoted:** M, the K-J connection and its spellings, KW1–KW4, Kernwelt-Manifestationen, the IFS roles (Beschützer, Manager, Feuerlöscher, Analytiker, Verbannten, Kern-Exile), Selbst-Energie, Wächter-Subsysteme, Parias, Happy Family, Friendly Giant, Sporadizität, Ruf zum Erwachen, Datenpanne, the 39 steps, and the borrowed concepts.

**One reader**: every page above and the two record entries.

**Chapter readings**: none — the document names no chapter; its units are 39 steps in three acts.
