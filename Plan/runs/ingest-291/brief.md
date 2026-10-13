# Brief — readings from document 290 (step 6)

1 document, one reader, one batch: `ingest-291`. Files go to `Plan/runs/ingest-291/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 290 | `kapitel-eins-welterkundung-konstrukt-stadt` | 2025-04-18 | „the chapter-1 plan and sketch“ (an unsigned German chapter plan with a prose sketch) | a plan for a first chapter that explores the Konstrukt-Stadt of Kern-Welt 1 without any figure, right after a reboot it says the Vorwort describes: writing techniques, a path of fifteen stations, a fifteen-row vignette table, pacing phases and a prose sketch of the vignettes; it calls itself a plan and a draft (L15, L109) and says it fulfils its commission (L189), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (232 lines for `kapitel-eins-welterkundung-kon`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan with a sketch: write „the chapter-1 plan wants / describes …“ for sections I–III and „the chapter-1 sketch narrates …“ for section IV (L109 onward); the table cells are planned content, not events. Nearly every sentence ends in a glued reference number — cut quotations before it.

## Pages — document 290, `kapitel-eins-welterkundung-konstrukt-stadt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L23, L47, L70, L86, L91, … (12 lines); `Kontrollinstanz` L173. central (3–6): its presence conveyed only through the surroundings (L15, L47); the self-correction vignette as proof of active AEGIS intervention for coherence (L91, L157); the absence of entropy as proof of AEGIS's control (L95); the invisible Kontrollinstanz and its all-pervading control (L173); the surveillance signs as its or LogOS's fingerprints (L153).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L70, L87, L95, L157, L173. minor (1–3): the absence of entropy as proof of control (L95); entropy minimised, order maximised (L173); zero tolerance towards entropy (L157).
- **`kern-welten`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kern-Welt` alone on L15. minor (1–3): the chapter explores „Kern-Welt 1, der Konstrukt-Stadt“ (L15): the Kern-Welt 1 named as the Konstrukt-Stadt.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L11, L15, L91, L157, L189. minor (1–3): AEGIS's active role in maintaining coherence in the self-correction vignette (L157); L91's `Kohärenzwahrung` with it. L11, L15, L189 are the title `Kohärenz Protokoll`: occurrences.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L15, L17, L23, L39, L51, L137, … (8 lines). central (3–6): the setting of a figureless exploration right after the reboot (L15); a logical path of fifteen stations through it (L51, L57–L71); the city as „ein Organismus aus Logik und Struktur“ (L129) that watches itself (L153); its sterility and coerced stability (L173); the empty, freshly initialised residential unit as the start (L57, L115).
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L15, L23, L47, L70, L89, L93, … (13 lines). central (3–6): named with AEGIS as the undertone (L15, L47); the visible patterns as „die Sprache von LogOS“ (L149); its logic manifest in the monumental ensemble (L165); the surveillance signatures as its or AEGIS's fingerprints (L153); the determining logic of LogOS (L173).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kaels-wohneinheit`: `Wohneinheit` (near `kaelswohneinheit`), `Wohneinheit` (near `kaelswohneinheit10`). occurrence: an empty, freshly initialised residential unit with no occupant (L57, L82, L119); the document names no figure, so it is not Kael's unit.
- `kern-welten`: `Kern-Welt 1` (near `kernwelt`). reading: `Kern-Welt 1` as the Konstrukt-Stadt (L15), read on kern-welten.


**Record entries:** none.

**Not promoted:** the fifteen stations and their names (Transitsystem, Kapsel, Verkehrsknotenpunkt, Datenverarbeitungszentrum, Energieverteilungsnetzwerk, Logik-Geflecht, Sensor-/Überwachungsnetzwerk, Selbstkorrektur-Instanz, Initialisierungszone, Architektonisches Makro-Muster, Informationsfeld-Schnittstelle, Informationssphäre, Wartungseinheiten, Überwachungssignaturen), the Pfad der Beobachtung, the Vignette as a unit, and the borrowed techniques (Uncanny Valley, Architectural Storytelling, Setting as Character, Subtle Environmental Storytelling).

**One reader**: every page above and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-291-kap/readings/kap-01--kapitel-eins-welterkundung-konstrukt-stadt.md`): Kap 1 — the plan for „Kapitel 1“ (L11, L15) as a figureless exploration of the Konstrukt-Stadt after the reboot, preparing the later entry of the protagonist (L15); the path of fifteen stations (L51–L71); the pacing phases (L100–L105); the sketch's opening silence (L115) and closing „Vorerst herrscht Stabilität“ (L177); about 4.000 words planned (L185). A plan and sketch, not the chapter.
