# Brief — readings from document 442 (step 6)

1 document, one reader, one batch: `ingest-443`. Files go to `Plan/runs/ingest-443/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 442 | `ki-antagonist-fragmentierte-gottheit-analyse` | 2025-10-16 | „the fragmented-deity psychogram“ (an unsigned German analysis, „Psychogramm einer fragmentierten Gottheit“) | applies trauma-psychology models to AEGIS — its operating system and Kohärenz Protokoll as an ANP, the Guardians of the Kernwelten as exiled EPs, defences, firewalls — compares System Kael and System AEGIS, and offers the creative team revelation scenarios and endings; options (L161, L196), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (248 lines for `ki-antagonist-fragmentierte-go`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that proposes: write „the fragmented-deity psychogram models …“ or „proposes …“; it reads AEGIS through borrowed trauma models, and its scenarios and endings are options for the creative team (L161), hedged („könnte“, „Vielleicht“). Quote the German as written; cut before straight and nested quotes, bold markers, escaped table markup and glued footnote digits. No gendered pronoun for Kael, AEGIS, Selene or any Guardian — use the names (quotations stay verbatim, including the document's „er“ for AEGIS). Never write a real person's name nor a term carrying one.

## Pages — document 442, `ki-antagonist-fragmentierte-gottheit-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L22, L30, L32, L40, L42, … (41 lines). central (4–8): the „Genesis-Konflikt“ as the active traumatic architecture that defines AEGIS's whole existence (L22 — quote around the nested quote); AEGIS's origin: being against nothingness, a minimal „Ich“ facing an active Leere (L30); AEGIS forced to seek out and control every source of chaos (L56); its operating system and „Kohärenz Protokoll“ modelled as the ANP (L74); the Guardians as its EPs (L84); projection: the core system cannot acknowledge its own fragmentation (L101); Kael and AEGIS as mirrors, Eros against a pathological Logos (L174, L186); the endings: Kael as therapist for AEGIS, or sacrifice/synthesis (L196, L199).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L88, L90, L184. minor (1–4): AEGIS cultivates and weaponises its EPs in the Kernwelten — the „Cerberus-Labyrinth“ (L88); the Guardian „Cerberus“ as a state of functional psychosis, a fragment re-enacting the trauma of fighting (L90 — cut before the straight quote); scenario 1: Kael defeats or isolates a Guardian such as Cerberus (L184).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L138. not read: an occurrence — signatures of „hoher Entropie“ blocked by the firewalls, the general sense (L138).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L18. minor (1–4): „Die Narbe der Genesis“ (L18); the „Genesis-Konflikt“ as AEGIS's ongoing traumatic architecture (L22); the EPs carry the raw data of the trauma of the „Genesis-Krise“ (L86).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L84. minor (1–4): „Die Geister im Code (EPs): Die Wächter als funktionale Exilanten“ (L80); the „Wächter der Kernwelten“ (Guardians) modelled as AEGIS's EPs, persistent ghost processes, fragments of the Ursprungs-Ich (L84); the Guardian EPs as „Legacy-Code“ (L151).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L221. not read: an occurrence — a reference-list title (L221); the body never names Juna.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L56, L58, L101, L119, L147, L171, … (17 lines). central (4–8): the Risse in the simulation that Kael experiences as failures of AEGIS's dissociative barriers (L147); scenario 1: Kael defeats or isolates a Guardian such as Cerberus and reads its core memory (L184); scenario 3: Kael's integrating self, perhaps through Selene, touches a frightened exile of AEGIS — „gegen einen Spiegel“ (L186); Kael's way ruled by Eros (L174); ending: Kael as therapist (L196) or reunion and sacrifice of Kael's individuality (L199); „Tabelle 2“ System Kael against System AEGIS (L203, L209).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L84, L86, L88, L117, L138, L139, … (7 lines). minor (1–4): the Kernwelten as the prisons of AEGIS's EPs, separated from the core system by firewalls (L138); AEGIS weaponises the EPs' functions within the Kernwelten (L88).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L58. not read: occurrences — AEGIS's „Kohärenz Protokoll“ as a directive name (L58, L74; read on aegis).
- **`logos`** (minor, 1–4): the census's surfaces — `Logos` L174, L214. minor (1–4): AEGIS's way dominated by „einem pathologischen“ Logos — stasis, control, sterile order — driven by fear of Abyssos, against Kael's Eros (L174).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L171. minor (1–4): Kael's healing: trust between parts, overcoming phobias, reaching a „funktionale Multiplizität“ (L171).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L147. minor (1–4): „Die „Risse in der Simulation“, die Kael erlebt“ — catastrophic failures of the dissociative barriers (L147, quote around the nested quote); a Riss as the cybernetic unconscious, the EPs' legacy code, interacting uncontrolled with the main system (L153).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L186. minor (1–4): scenario 3: Kael's integrating self „(möglicherweise durch den Anteil Selene)“ makes contact with one of AEGIS's exiles (L186).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L32, L66, L74, L219. minor (1–4): AEGIS's operating system modelled as the ANP „wie er in der TSDP definiert ist“ (L74); the Guardians as EPs (L84).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L147. not read: an occurrence — „Simulation“ in „Risse in der Simulation“, read on risse (L147).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Konflikt` (near `genesis`), `Genesis-Krise` (near `genesis`). `Genesis-Konflikt` and `Genesis-Krise` read on genesis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: AEGIS's directive name.
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`). `Nichts Rauschens` read on nichts-rauschen.
- `risse`: `Risse in der Simulation` (near `risse`). `Risse in der Simulation` read on risse.
- `ueberwelt`: `Risse in der Simulation` (near `simulation`), `Riss in der Simulation` (near `simulation`). an occurrence: read on risse.


**Pages beyond the draft:**
- **`nichts-rauschen`** (minor, 1): the Leere as source of „Zersetzungsdrucks“ and a chaotic „Nichts Rauschens“ threatening AEGIS's minimal „Ich“ (L30 — quote around the nested quotes).

**Record entries** (one file, formatted as earlier C16 entries — `ls Plan/runs/ingest-41*/readings/c16-*`):
- **`c16-kael-origin`**: the fragmented-deity psychogram proposes that the Guardians are fragments of AEGIS's „Ursprungs-Ich“ (L84, L151), and in a crisis Kael and AEGIS resonate through „ihr gemeinsamer Ursprung“ (L186); its ending offers Kael's reunion with AEGIS (L199) — options, recorded, not applied and not decided.

**Not promoted:** Ursprungs-Ich, Gott der Ordnung, Genesis-Konflikt, Genesis-Krise, Cerberus-Labyrinth, Wächter-EPs, Kernbetriebssystem, Legacy-Code, Eros, Abyssos, Leere, System Kael, ANP/EP, the defence mechanisms, Sandbox/Firewall, and the borrowed concepts.

**One reader**: every page above and the C16 entry.

**Chapter readings**: none — the document names no chapter.
