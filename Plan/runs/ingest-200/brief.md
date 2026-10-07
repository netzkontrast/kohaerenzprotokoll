# Brief — readings from document 200 (step 6)

1 document, one reader, one batch: `ingest-200`. Files go to `Plan/runs/ingest-200/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 200 | `dramatica-und-kohaerenz-protokoll-analyse` | 2026-04-27 | „the Dramatica loop analysis“ (an unsigned analysis report) | a German report that maps the Dramatica model onto the Kohärenz-Protokoll's cast and world in four loops of question, hypothesis and verification — the verification „bestätigt“ from data the file does not contain (L39) — then proposes four alternative storyforms, each with `Konzept & Design` and `Systemische Evaluation`, and closes that the architecture is robust (L167, L171) — its claims recorded, never applied; the author's storyforms are their own (decision 025) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (178 lines for `dramatica-und-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that claims verification: write „the Dramatica loop analysis maps / proposes …“; its `bestätigt` rests on data not in the file — say so where it matters; what it reports of Dramatica is Dramatica's (L27, L29, L81, L161). German with English Dramatica terms — quote as written; cut before glued reference digits and inner straight quotes; the export lost the kernel symbols (L23, L49, L51, L102, L115, L119, L171) — never quote across a gap; the table at L44–L47 has escaped bold.

## Pages — document 200, `dramatica-und-kohaerenz-protokoll-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L37, L39, L44, L49, L51, … (25 lines). central (2–4): AEGIS operating „auf Basis klassischer Logik“ against Kael (L23); the hypothesis that it „zwingend die Klasse Universe okkupieren muss“ (L37); its OS concern Understanding, to clean reality's faulty logic by rigid protocols (L59); the Risse come from AEGIS, „keine externen Angriffe“ (L51); its reality collapsing under entropy in the fourth storyform (L163).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L102. minor (1–2): the integrated state of the alters as „eine funktionale Demokratie“ (L102) — read around the gap.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L21, L49. minor (1–2): the DKT named as a primary source and the law of the world (L21); Kael as carrier of a kernel (L49) — never across the lost symbol.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L23. occurrence: the general word in the method's sentence (L23).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L15. minor (1–2): read L15 and L163 — narrative entropy in the method, and the entropy under which AEGIS's reality collapses in the fourth storyform.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L37, L39, L46, L47, L51, L59, … (14 lines). central (2–4): Juna/V as the IC in Psychology (Manipulation) (L46) — quote the plain words; the relationship Kael–Juna in Physics (L37, L47); the SS concern placed between Kael and „der Foundation“ (L59) — a tension with L37, record it.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L37, L39, L45, L47, L49, … (32 lines). central (2–4): Kael against AEGIS's classical logic (L23); „Kael hingegen ist Träger des Kernels“ (L49) — cut before the gap; „Kael ist in Logos-Prime integriert“ in the Ki (L63); „Im Masterkonzept ist Kael vermutlich ein“ start character (L147); he refuses Order and lets the simulation collapse in the fourth storyform (L163).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L99, L102, L163. minor (1–2): „Kiko trägt die geballte emotionale Sensibilität und Verwundbarkeit.“ (L99).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L57, L63, L149. minor (1–2): the Kishōtenketsu paradigm that „vier Phasen umfasst“ structures the passage through the worlds (L63); read L57 or L149.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L19. occurrence: the integrity check of the method (L19), the general word.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L97, L102, L163. minor (1–2): Lex „nutzt analytische Fähigkeiten zur strikten Problemvermeidung und Verdrängung“ (L97).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L61. minor (1–2): „KW1 (Logos-Prime) wird von der Entität LogOS bewohnt“ (L61) — quote around the digit.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L23. minor (1–2): read L23, where the method names Kael's multiplicity.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L98, L102, L149, L163. minor (1–2): Nyx as unrelenting protector and trauma bearer in the Cerberus-Labyrinth, solving NP-hard problems (L98) — read the line; the fourth storyform's focus on Nyx and Protection (L149).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L23, L51, L121, L149. central (2–4): „Die Risse sind also keine externen Angriffe“ but come from AEGIS's own erasure, after Landauer (L51); read L121 or L149.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L100, L102, L163. minor (1–2): Selene „fungiert als kreative Intelligenz“ searching new solutions (L100).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L21, L83, L95, L119, L149, L171. minor (1–2): the TSDP named as a source (L21); the fourth storyform brings the TSDP dynamics into focus (L149).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L63. occurrence: the simulation in the Kishōtenketsu passage (L63) is the setting's general sense, nothing of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world's name (L98), read on nyx.
- `entropie`: `narrative Entropie` (near `entropie`). occurrence: `narrative Entropie` is the method's term — a reading of entropy above only from L163.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the world's name (L61), J49.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Protokolls` (near `koharenz`), `Kohärenztheorie` (near `koharenz`), `Hyperkohärenz` (near `koharenz`). occurrence: the Protokoll's name; Kohärenztheorie and Hyperkohärenz are the analysis's terms.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the world's name (L61), J49.
- `personas`: `Personal Triumph` (near `persona`). occurrence: `Personal Triumph` is a Dramatica outcome (L161).
- `truth-rotation`: `Truth` (near `truthrotation`). occurrence: `Truth` is a Dramatica element, not the Truth-Rotation.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: „KW1 (Logos-Prime) wird von der Entität LogOS bewohnt“ (L61) — read the line for the other worlds.
- **`q8-aegis-after-the-vortex`**: in the fourth alternative storyform AEGIS's reality collapses under entropy (L163) — one alternative among four.

**Not promoted:** the Dramatica vocabulary and the four alternative storyforms (the author's storyforms are in Plan/storyform/, decision 025), the method's mechanisms (M0, the NCP), the Foundation, the Z-Buffer-Struktur, the borrowed theories.

**Two readers**, disjoint: (1) kael, juna, alters, lex, nyx, kiko, selene, tsdp, multiplizitaet, kishotenketsu; (2) aegis, dkt, entropie, risse, logos and the records q5, q8.
