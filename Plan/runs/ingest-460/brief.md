# Brief — readings from document 460 (step 6)

1 document, one reader, one batch: `ingest-460`. Files go to `Plan/runs/ingest-460/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 460 | `kohaerenz-protokoll-thematische-tiefenanalyse` | 2025-04-28 | „the thematic blueprint“ (an unsigned German report, „strategische thematische Blaupause“, L5) | groups the novel's themes into four clusters, maps them onto three plot phases, applies borrowed theories to Kael, AEGIS and Juna/V, and ends in four Blaupausen tables of hedged proposals per phase; it calls itself a roadmap (L323), no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (328 lines for `kohaerenz-protokoll-thematisch`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of readings and proposals: write „the thematic blueprint reads …“; its theory blocks are borrowed lenses, its matrix assignments „exemplarisch“ (L56), its table cells hedged with question marks. Lines L24, L78, L172 and many theory lines name real people — never quote them, never write the names. World codes (Co₁, McL, B, Ly) may stand as written, never expanded. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „Er“). Cut before inner quotes, escaped bold and italics.

## Pages — document 460, `kohaerenz-protokoll-thematische-tiefenanalyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L35, L36, L37, L39, L41, … (75 lines). central (4–8): the central paradox: AEGIS's methods of enforcing coherence destabilise the system (L41); AEGIS embodies an externalised, rigid trauma-coping strategy (L43); the fragmentation of Kael a control strategy, not a side effect (L35); AEGIS trapped in a dilemma, a failure built in (L178); AEGIS seems to follow a functionalist or information-based ontology (L184 — hedged).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L24, L43, L76, L207. minor (1–4): `Zero-Trust` listed among AEGIS's principles (L24 — name-free part only, or describe) and as a rigid rule fostering avoidant attachment (L207).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L35, L52, L117. minor (1–4): `Cache Kohärenz` named as Kael's problem, the psychic manifestation of the system's control (L35); in the matrix (L52, L117).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L23. minor (1–4): the cluster of psyche and trauma lists DID among the models applied to Kael's inner state (L23 — name-free part only).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L24. not read: an occurrence — L24 names control against emergence as a theme in general terms, on a line with a person's name.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L25. not read: an occurrence — L25 lists ontological themes in general terms.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L287. minor (1–4): in Phase 1 of the plot events the Guardians as agents of control (L287 — describe around the inner quotes).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L26, L37, L43, L52, L53, L54, … (36 lines). central (4–8): the connection V/Juna gains a specific psychological function, not only an external force (L145); AEGIS cannot understand or control V (L226); the Moonshine-Link as a connection between Kael and Juna (L209); V/Juna acts beyond a plot device (L321); the pair written as Juna/V and V/Juna.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L35, L36, L37, L43, L44, … (65 lines). central (4–8): the cluster of psyche, identity and trauma gathers Kael's inner state (L23 — quote only the name-free start); Kael's fragmentation as AEGIS's control strategy (L35); the worlds activate or mirror Kael's logician, shadow and child, and creative parts (L65, L67, L68); Kael's relation to AEGIS an insecure attachment (L139); Kael's journey an individuation process (L128 — describe, the concept is borrowed).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L36, L37, L52, L58, L61, L74, … (21 lines). central (4–8): the Kernwelten as diagnostic arenas (L52) and ontological laboratories (L199); the matrix maps each world to a part of Kael — Co₁ order and logic, McL network and relationship, B chaos and shadow, Ly potentiality and emergence (L65–L68, codes as written, never expanded); designed to isolate and analyse parts (L276); proposed designs per world (L243–L245).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L1. not read: an occurrence — the title and coherence in the psychological sense.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L209, L258. minor (1–4): the Moonshine-Link symbolises a connection between Kael and Juna, working independently of the system's rules (L209); moonlight as its motif (L258 — describe around the inner quotes).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L43, L172, L299. minor (1–4): a hedged Blaupause cell: confrontation with the Potentialmeer P? (L299); AEGIS's position against the Potentialmeer (L43) — read only name-free lines.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L77. not read: an occurrence — L77 hints at another level of reality in a hedged matrix cell, a general sense.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L24, L44, L53, L76, L77, L156, … (22 lines). central (4–8): the Risse as system instabilities, visual glitches, the limits of AEGIS's control (L247); in the phases: life in the system and its Risse (L76), an epistemology of the Risse (L77); first Risse as unexplained phenomena, AEGIS trying to close them (L287); the Risse growing larger and more frequent (L288).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L78, L276, L288. minor (1–4): the Überwelt as the system environment that heightens separation and control (L276) and shows surveillance architecture (L288); in the matrix (L78 — a line with a name: describe, never quote).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Record entries** (one file each, formatted as earlier entries):
- **`q3-how-many-kern-welten-and-alters`**: the thematic blueprint maps four coded worlds (Co₁, McL, B, Ly) each to a part of Kael — logician, network, shadow and child, creative (L65–L68); recorded.
- **`q1-guardians-and-aegis`**: the blueprint has Guardians meet Kael in Phase 1 as agents of control (L287); recorded.

**No chapter readings**: the blueprint numbers phases, not chapters.

**Not promoted:** the four clusters, Kernparadoxon, Cache Kohärenz as Kael's problem (already a page), Query Context, Blaupausen, the phase names, and the borrowed theories (several carry people's names).

**One reader**: every page above and the two record entries.
