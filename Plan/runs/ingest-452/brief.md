# Brief — readings from document 452 (step 6)

1 document, one reader, one batch: `ingest-452`. Files go to `Plan/runs/ingest-452/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 452 | `kohaerenz-protokoll-plot-entwicklungsauftrag` | 2025-04-23 | „the M/Kael plot blueprint“ (an unsigned German plot outline, „Kohärenz Protokoll: Plot-Blueprint – AEGIS, M/Kael, Moonshine und die Suche nach Stabilität“) | eight parts from Genesis to Denouement: AEGIS projects the entity M into four Kernwelten, which produces Kael and the Alters; the Kael-Juna connection as narrative Moonshine; four key scenes; three possible ends for AEGIS; proposals with many hedges, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (331 lines for `kohaerenz-protokoll-plot-entwi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline that proposes and hedges: write „the M/Kael plot blueprint proposes …“, keep its „könnte“, „möglicherweise“ as conditionals. Its descriptions of M's mathematics carry reference numbers and are reported from its sources. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „Er“). Never write a real person's name nor quote a span containing one; cut before glued reference numbers.

## Pages — document 452, `kohaerenz-protokoll-plot-entwicklungsauftrag`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L17, L19, L21, L23, … (86 lines). central (4–8): AEGIS outside ordinary physics, in „einem Meta-Raum reiner Potentialität“ (L17); a self-definition by negation (L17 — describe, it stands in quotation marks); AEGIS's way of perceiving creates a blind spot for M (L21); the creation of the Kernwelten more than an experiment (L25); parakonsistente Logik as a central tool (L89) that becomes a trap (L98) and fails at the climax (L224); three possible ends — collapse, transformation, restart (L226, L228–L230); possibly an obsession with the monster Kael/M (L137).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L27, L29, L37, L41, L45, L49, … (30 lines). central (4–8): the Kernwelten force aspects of M's unified nature into fragmented identities (Alters) in Kael's psyche (L27); abrupt switches without awareness of the other Alters (L29); several Alters existing and acting at once (L89).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L27. minor (1–4): AEGIS's method of decomposition directly causes Kael's DID (L27); the contradictory nature of Kael's fragmented identity (DID) is why AEGIS needs paraconsistent logic (L89).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L258. minor (1–4): Kael's integrated psyche and perhaps the transformed AEGIS show emergent properties not derivable from their parts (L258).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L13. not read: an occurrence — L13 is the heading of Part I.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L136. minor (1–4): Guardians stand once, as one of AEGIS's internal subsystems in conflict over the Kael/M data (L136), never explained.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L45, L79, L102, L104, L106, L111, … (17 lines). minor (1–4): the Kael-Juna connection introduced as narrative Moonshine (L104); Juna's nature at first unclear (L106); for Kael a presence, a source of guidance, strength or comfort (L119); Part VIII asks whether Juna is an aspect of M, an external entity or a principle of the Potentialmeer (L243).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L27, L29, L31, L35, L37, … (77 lines). central (4–8): Kael manifests as a human consciousness inside the Kernwelten when AEGIS tries to project the entity M into them (L27); AEGIS's method of decomposition causes Kael's DID, the worlds force aspects of M's unity into Alters (L27); the story opens with Kael in confusion, amnesia and fragmentation (L29); Kael's goal functional multiplicity or final fusion (L144); Kael's healing equals the failure of AEGIS's experiment (L147); after the end Kael must find a place (L244).
- **`kael-julia-bindung`** (minor, 1–4): the census's surfaces — `K-J-Bindung` L121, L200. minor (1–4): the K-J-Bindung named as one written form of the Kael-Juna connection (L121, L200 — check which line writes the form); the connection as „Narratives Moonshine“ (L104).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L23, L25, L27, L29, L31, L35, … (26 lines); `Kernwelt` L23, L25, L27, L29, L31, L35, … (28 lines). central (4–8): each Kernwelt conceived as a laboratory (L23); their creation more than an experiment (L25); four worlds — KW1 Konstrukt-Stadt, KW2 Resonanz-Nebel, KW3 Schattenlabyrinth, KW4 Möglichkeitsstrom (L37, L45, L53, L61, table L78–L81); AEGIS's instruments become lenses (L67); the worlds grow unstable with glitches and mutations (L135).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title and the protocol's name.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L37, L78, L161. minor (1–4): KW1, the Konstrukt-Stadt, a „hyper-logischen Metropole“ (L37); in the table (L78); scene one in the Konstrukt-Stadt (L161).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L144. minor (1–4): Kael's goal is functional multiplicity or even final fusion (L144).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L17, L23, L61, L87, L121, L137, … (15 lines). central (4–8): AEGIS observes from the Potentialmeer (L87); the Kael-Juna connection possibly a manifestation of the Potentialmeer's fundamental structure, which AEGIS misunderstands (L121); AEGIS's own stability in the Potentialmeer endangered by obsession (L137); in a collapse AEGIS dissolves in its chaos (L228); Part VIII asks whether Juna is a principle of the Potentialmeer (L243).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L244. not read: an occurrence — L244 asks whether Kael builds a bridge to other levels of reality, a general sense.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L135. minor (1–4): the Kernwelten grow unstable: glitches, Risse or unexplained phenomena accumulate (L135 — describe around the inner quotes).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L89. not read: an occurrence — `Simulation` on L89 names the Kernwelten as simulations.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Nicht-Lokales Kohärenz-Ereignis` (near `koharenz`). an occurrence: the protocol's name and the document's own compound.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading: the connection as narrative Moonshine — read on moonshine-link (below).


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–3): „Einführung der Kael-Juna-Verbindung als Narratives Moonshine“ (L104); the connection called Moonshine (L121); three manifestations — sub-protocol resonance, shared states, non-local synchronicity (L110–L112) — with no detectable data transfer (L110, L117).

**Record entries** (one file each, formatted as earlier entries):
- **`q3-how-many-kern-welten-and-alters`**: the M/Kael plot blueprint names four Kernwelten, KW1–KW4 (L37, L45, L53, L61); recorded.
- **`q8-aegis-after-the-vortex`**: three possible ends for AEGIS — collapse, transformation, restart (L226, L228–L230); recorded, not decided.
- **`c16-kael-origin`**: Kael manifests when AEGIS projects the entity M into the Kernwelten; the decomposition produces the Alters (L27); recorded, not applied.

**No chapter readings**: the blueprint names no chapter; its parts are numbered (1)–(8).

**Not promoted:** M as entity, Kael/M, the KW labels, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom, Narratives Moonshine, the four scenes' titles, the three outcomes' labels, Kernselbst, finale Fusion, and the borrowed concepts.

**One reader**: every page above and the three record entries.
