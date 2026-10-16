# Brief — readings from document 462 (step 6)

1 document, one reader, one batch: `ingest-462`. Files go to `Plan/runs/ingest-462/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 462 | `genesis-ein-implementierungsleitfaden-prosa-version` | 2025-04-29 | „the Genesis implementation guide“ (an unsigned German guide, „Genesis: Ein Implementierungsleitfaden zur narrativen Ausgestaltung“) | a direction book for writing a 13-scene Genesis outline as prose: a theory synthesis, research tasks, Part 3 sample material it marks as illustration because the research was not done (L171), and thirteen scene sections of directives with sample beats in the voices of the Ich and AEGIS; it demands strict adherence to itself (L313), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (559 lines for `genesis-ein-implementierungsle`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A direction book: write „the Genesis implementation guide directs …“; its sample beats are examples in two voices (the Ich in first person, AEGIS in third), never canon prose; its theory blocks are borrowed lenses. L19 and some theory lines name people — never quote them, never write the names. No gendered pronoun for the Ich, Kael or AEGIS — use the names (quotations verbatim, including the document's „seine“). Cut before straight quotes, inner „…“, bold and italics; scene numbers drop in `--find`, so quote sentences, not labels.

## Pages — document 462, `genesis-ein-implementierungsleitfaden-prosa-version`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L27, L29, L31, L33, L35, … (102 lines). central (4–8): AEGIS conceived as a purely functional system (L21); its core logic „AEGIS ist die Abwehr des Nicht-Seins. Existenz = Funktion.“ (L31), read as self-preservation; its later elimination of Komponente 734 no act of malice (L31); its limit the inability to see the limits of its own logic (L37); homeostasis as its control principle (L33); Szene 8 shows the limits of its modelling (L456); a sample beat: integrity of the system as primary goal (L400).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L43. minor (1–4): dissociation as a coping strategy for overwhelming trauma, not a malfunction but an adaptive survival mechanism (L43) — the guide's trauma lens for the Ich and Kael.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L49. minor (1–4): Kael's Emergenz in Szene 13 as the embodiment of a history of trauma (L49).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L127. not read: an occurrence — L127 names entropy among the effects the Nichts Rauschen's metaphors should evoke, a general sense.
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L11, L17, L45, L55, L95, L309, … (8 lines). minor (1–4): the guide's subject is the outline titled Genesis (L11); the first-person perspective in Genesis requires an understanding of consciousness (L17 — name-free part only); the guide directs the 13-scene Genesis outline (L313).
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L221. not read: an occurrence — `Systemgrenze` on L221 is a word in a glossary list of systems terms.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L41, L45, L49, L51, L61, … (15 lines). central (4–8): Kael embodies the result of the process (L45); Kael's Emergenz in Szene 13 the embodiment of a complex history of trauma (L49); the last scene's goal the birth of Kael as a fragmented mosaic (L537); the voice of Szene 13 no longer the naive Ich but shaped by trauma (L540); Kael defined by trauma, driven by preserved subjectivity (L51); a possible unreliability of the narrator in the last scene (L61).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L540, L549. minor (1–4): the voice of Szene 13 shaped by trauma (L540); a sample beat in Szene 13: a look into the Kernwelten (L549 — describe around the straight quotes).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L31. not read: an occurrence — the protocol's name and systems coherence.
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L21, L23, L31, L33, L37, L45, … (36 lines). central (4–8): in a sample AEGIS beat the Ich is reclassified as Komponente 734 (L414); Szene 5 alternates first person and AEGIS's third person describing function and status (L407); the elimination of 734 as a logical consequence for system integrity (L517); AEGIS's elimination of 734 no act of malice (L31).
- **`nichts-rauschen`** (central, 3–12 quotations): the census's surfaces — `Nichts Rauschen` L23, L41, L70, L111, L127, L185, … (10 lines). central (4–8): the Nichts Rauschen as the void the Ich awakens in; it needs metaphors that evoke chaos, emptiness, threat and potentially entropy (L127); further occurrences in the scene plans as the census lists them (L23, L41, L70, L111, L185).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L199. not read: an occurrence — `Risse` on L199 is a word in a sample metaphor list.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L106, L273, L305, L438, L443, L448, … (10 lines). central (4–8): Szene 7, „Die Überwelt: Simulation der Ordnung“ (L438); its plan describes the Überwelt's functions — modelling, analysis, optimisation, concept generation — in the AEGIS voice (L443); the logic behind the Überwelt as a use of systems theory (L106); awe as the Ich's possible response in Szene 7 (L305); the flow through code architectures (L273).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: `Resonanz` is the Ich's resonance, not the protocol.
- `kohaerenz`: `Kohärenz Protokoll Gamma-Exekution` (near `koharenz`), `Systemkohärenz` (near `koharenz`). an occurrence: the protocol's name `Kohärenz Protokoll Gamma-Exekution` (L517) and systems coherence.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). an occurrence: `Mosaik` is Kael's mosaic identity, not the Mosaik-Herz.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` is the Ich's echo in the scenes, not the residual echoes.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). an occurrence: the Ich's resonance.


**Record entries** (one file each, formatted as earlier entries):
- **`q7-what-734-names`**: the Genesis implementation guide has AEGIS reclassify the Ich as Komponente 734 (L414) and later eliminate it (L517); recorded.
- **`c16-kael-origin`**: the guide has Kael born in Szene 13 as a fragmented mosaic, the result of 734's elimination and fragmentation (L45, L537); recorded, not applied.
- **`c12-genesis-beats`**: the guide directs Genesis as 13 scenes in three parts (L313), with three scenes marked new; recorded.

**No chapter readings**: the guide numbers scenes of Genesis, not chapters of the novel.

**Not promoted:** Direktive 0, Ich-Perspektive, Echo, Resonanz, Dissonanz, Mosaik, Protokoll Gamma-Exekution, Regiebuch, Stylistic Contrast Summary, the scene titles, the part headings, and the borrowed concepts.

**One reader**: every page above and the three record entries.
