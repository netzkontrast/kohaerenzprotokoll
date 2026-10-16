# Brief — readings from document 248 (step 6)

1 document, one reader, one batch: `ingest-248`. Files go to `Plan/runs/ingest-248/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 248 | `dramatica-storyform-fuer-romananalyse` | 2026-01-02 | „the Dramatica exegesis“ (an unsigned German research report) | a report building a Dramatica Storyform for the novel — Kael MC in Mind, AEGIS IC in Universe, the Moonshine-Link as RS in Psychology, the war of the kernels as OS in Physics — with a table it calls „zwingend korrekte Storyform“ (L261) and three open questions for the author; its claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (403 lines for `dramatica-storyform-fuer-roman`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of proposals: write „the Dramatica exegesis assigns / reads …“. Its Storyform values are its own, not `Plan/storyform/`'s; never compare them. Lines that report a numbered source („Das Dokument 8 sagt“) are that source as the report gives it. Cut quotations before reference numbers and inner quotes; `K\_1`/`K\_0` are escaped.

## Pages — document 248, `dramatica-storyform-fuer-romananalyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L37, L49, L88, L93, L95, L97, … (37 lines). central (3–8): AEGIS as IC in Universe (L98); operating on prediction and fear of the end, preventing the Nichts Rauschen (L130); blindly believing its axioms (L237); total control as Maxwell's demon (L199); needing energy (Coherons) not to die (L340); tragic, surviving only if it gives up control (L342).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L191. minor (1–4): the axis Control against Emergence at the core of the Dual Kernel Theory, Emergence as Dramatica's Uncontrolled (L191).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. minor (1–4): the novel's four terms set against Dramatica's building blocks, „Kollaps (Entropie)“ among them (L17); AEGIS's fear of the end, entropy (L130).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L358. not read: occurrence — `Genesis` at L358 stands in `Genesis Crisis`, the origin pain binding Kael and AEGIS, read on aegis if it adds; otherwise not read.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L291, L348. minor (1–4): the IC Solution Disbelief, doubt in its own logic „durch das Gödel-Gambit“ (L291); L348 if it names it.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L49, L93, L95, L97, L106, L130, … (9 lines). minor (1–4): Juna/V representing the potential, a possible future (L130); in the relationship with Kael and AEGIS (L106); among the four existence matrices as „Juna/V.10“ (L49).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L36, L49, L77, L79, L84, L93, … (35 lines). central (3–8): MC in Mind, his conflict not primarily physical (L79–L80); his ANPs using denial (L169); OS and MC sharing the problem Control, so Kael must be a Change Character (L225, L348); taking responsibility for AEGIS (L257); the EPs breaking in (L121).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L121. minor (1–4): „Kiko (Angst)“ among the EPs breaking into consciousness (L121).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L17, L29, L35, L48, … (15 lines). central (3–8): the four terms „Kohärenz (Ordnung), Kollaps (Entropie), Protokoll (Prozess) und Resonanz (Bindung)“ against Dramatica (L17); the isomorphy between the novel's laws and Dramatica (L17); a precise translation of the Dual Kernel Theory into narrative structure (L336).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L38, L104, L106. minor (1–4): the RS throughline, „Der Moonshine-Link“ (L104): the relationship between Kael and AEGIS (and Juna) as Trauma Loop and Validation War (L106); the RS as the Moonshine-Link (L38).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L148. minor (1–4): Kael and AEGIS having to become something new, „eine funktionale Multiplizität“ (L148).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L130, L249, L288. minor (1–4): the Nichts Rauschen, the future of dissolution AEGIS's whole being aims to prevent (L130); the temptation of giving up (L249); the IC Concern The Future (L288).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L121. minor (1–4): „Nyx (Wut)“ among the EPs breaking into consciousness (L121).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L272. minor (1–4): the Story Driver Action: external events („Risse“, system errors) forcing decisions (L272).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L35. not read: occurrence — `Simulation` at L35 is the simulation in the OS line; the line is read on kohaerenz if it adds.

- **`coheron`** (minor, 1): AEGIS needing energy (Coherons) not to die (L340).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). reading: AEGIS needing energy, „Coherons“, not to die (L340) — read on coheron.
- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`), `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Protokoll` and `Resonanz` are two of the novel's four terms in general, not these pages.
- `genesis`: `Genesis Crisis` (near `genesis`). occurrence: `Genesis Crisis`, the origin pain binding Kael and AEGIS (L358).
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: `Kollaps` is one of the novel's four terms (L17), read on kohaerenz.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence: `Protokoll` and `Resonanz` are two of the novel's four terms in general, not these pages.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence: `Protokoll` and `Resonanz` are two of the novel's four terms in general, not these pages.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Protokoll` and `Resonanz` are two of the novel's four terms in general, not these pages.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). occurrence: `Protokoll` and `Resonanz` are two of the novel's four terms in general, not these pages.


**Record entries** (one file each):

- **`q9-moonshine-link-boundary`**: the Moonshine-Link as the Relationship Story throughline between Kael and AEGIS (and Juna), a Trauma Loop and Validation War (L104–L106).

**Not promoted:** the Storyform table and its values, the four throughlines as pages, Trauma Loop, Validation War, Story Mind, the Quad structure, K_1/K_0, the three open questions, Fundament, V.10, Täter-Introjekt.

**One reader**: kael, aegis, juna, kohaerenz, moonshine-link, nichts-rauschen, multiplizitaet, goedel-gambit, kiko, nyx, emergenz, entropie, risse, coheron and the record q9. `genesis` and `ueberwelt` are occurrences.

**Chapter readings**: none.
