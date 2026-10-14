# Brief — readings from document 494 (step 6)

1 document, one reader, one batch: `ingest-494`. Files go to `Plan/runs/ingest-494/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 494 | `plot-blueprint-methodik-kohaerenz-protokoll` | 2025-04-20 | „the plot-blueprint method handbook“ (an unsigned German handbook, „Methodisches Handbuch zur Ausarbeitung des Plot-Blueprints“, L11) | twelve narrative techniques (A–L) with principles and proposals for working out the 39 plot points, a technique matrix and a seven-field template; a method handbook in the plan voice, pointing to unseen material through bracketed „Kontext“ markers, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (404 lines for `plot-blueprint-methodik-kohaer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A method handbook: write „the plot-blueprint method handbook proposes …“ or „asks for …“; its examples (z.B.) are examples, never story facts; a „[Kontext n]“ marker points to material not in the file — never treat it as the handbook's own claim. „DIS“ is Kael's condition in the novel. The handbook names real authors and a reference list — never quote a span containing a person's name. Quote verbatim; cut before bold, italics, escaped brackets and inner quotes. No gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose.

## Pages — document 494, `plot-blueprint-methodik-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L16, L32, L34, L38, L52, L58, … (41 lines). central (4–8): AEGIS's domain, Überwelt and control level, shown cold, logical, controlling, perhaps subtly faulty (L52); AEGIS's aim framed as fighting information entropy, eliminating perceived noise including Kael's nature and the K-Juna connection (L193); AEGIS misreads the K-Juna connection as maximal information entropy, its control raising instability, the Risse (L194); AEGIS paradoxical, designed for order, causing chaos through rigidity (L217); AEGIS as machine, gatekeeper, rigid structure among the proposed metaphors (L173).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L31, L51, L72, L78, L93, L106, … (22 lines). central (4–8): the Kern-Welten environments mirroring the dominant alter's mindset (L31); alters with specific abilities and roles within the inner system (L114); alter functions linked to coping (L112); perspectives shifting between alters as they become dominant (L132); conflicts between alters, e.g. Praetor seeking safety against Flicker seeking exploration, Nox undermining Kael (L152 — examples).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L168. minor (1–4): entropy among the abstract ideas to make concrete (L168); entropy as decay, noise, heat death, Kipple among the metaphors (L173); entropy a central, active force defining AEGIS's motivation and the core conflict (L201).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L156, L176, L258, L338, L344, L345. minor (1–4): growing doubt within Guardians such as LogOS or Mnemosyne as they watch the K-Juna paradox and AEGIS's failure (L156); the Guardians representing specific protocols or functions (L176); the Guardians' possible loyalty shifts (L258).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L33, L153, L156, L173, L174, L193, … (16 lines). central (4–8): Kael's core conflict between the wish for coherence/Juna and fear (L153); the K-Juna paradox: AEGIS reads Kael's source of coherence as entropy (L194, L214); the K-Juna connection as resonance, light, a sub-protocol signal among proposed metaphors (L173); a task failing because of the K-Juna paradox (L174).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L16, L31, L51, L58, L73, L74, … (43 lines). central (4–8): the core aim includes psychological authenticity, especially regarding Kael's DIS and subjective experience (L16); Kael's inner experience of dissociation, fragmentation and memory gaps first (L111); the DIS anchored in Kael's initially unclear trauma history (L112); Kael's journey toward awareness, cooperation and integration or functional multiplicity (L115); Kael the host (L132); Kael's core conflicts: the wish for coherence/Juna against fear instilled by AEGIS and trauma (L153); Kael paradoxical, fragmented yet striving for unity (L217).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L31, L38, L51, L58, L71, L72, … (13 lines); `Kern-Welt` L31, L34, L38, L51, L58, L71, … (16 lines). central (4–8): environments of the Kern-Welten mirroring the inner state: rigid geometry in KW1, decaying structures in KW2, oppressive architecture in KW3 (L31 — examples); the Kern-Welten are psychological landscapes (L38); KW2 the Mnemosyne-Archipel and KW3 the Cerberus-Labyrinth infused with psychological horror (L235).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L156. minor (1–4): LogOS among the Guardians whose inner conflict grows (L156).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L156, L235. minor (1–4): Mnemosyne among the Guardians whose doubt grows (L156); KW2 named Mnemosyne-Archipel (L235).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `funktionale Multiplizität` alone on L106. minor (1–4): Kael's journey toward integration or functional multiplicity as the central arc (L115).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L196. minor (1–4): Kael's integration reducing a high psychological entropy, creating inner order/Negentropie (L196).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L32, L54, L175, L194, L195, L259, … (7 lines). minor (1–4): the Risse embodying the system instability the paradox causes (L175); AEGIS's control raising instability, the Risse (L194); glitches („Rissen“) and Kipple showing rising entropy (L195).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L34, L52, L71, L354; `Simulation` L16, L38, L134, L139, L195, L237, … (8 lines). minor (1–4): different environmental approaches for each Kern-Welt, the Überwelt and the AEGIS control level (L34); the Überwelt and the AEGIS control level as AEGIS's domain (L52); conceptual clarity on AEGIS and the simulation (L16); decay and glitches within the simulation showing rising entropy (L195).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). an occurrence: `Cerberus-Labyrinth` names KW3, read on kern-welten.
- `entropie`: `Entropie als Narratives Mittel` (near `entropie`), `Informationsentropie` (near `entropie`). a reading: `Informationsentropie` and entropy as a narrative means, read on entropie and aegis.
- `kohaerenz`: `Kohärenz-Insel` (near `koharenz`). an occurrence: `Kohärenz-Insel` named in passing, not the page's term.


**Record entries:** none.

**No chapter readings**: the handbook names no chapter (`Kap` 0, `Kapitel` 0); it speaks of 39 plot points.

**Not promoted:** the twelve techniques (EST and the rest), the K-Juna-Paradoxon and K-Juna-Verbindung as surfaces, AEGIS-Kontrollebene, the protocols OBP, RIVE, SARM, PMAS and CCPP, the alter names Nox, Praetor and Flicker, Kipple, Welle von Unmöglichkeit, and the borrowed concepts.

**One reader**: every page above.
