# Brief — readings from document 232 (step 6)

1 document, one reader, one batch: `ingest-232`. Files go to `Plan/runs/ingest-232/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 232 | `dramatica-dual-storyform-mapping-analyse` | 2026-04-30 | „the storyform mapping analysis“ (an unsigned German research report) | a German report that tests mappings between two Dramatica storyforms (Kael and AEGIS) as a hypothesis tree with verdicts, keeps two alternatives (Ontologische and Prozessuale Transposition), steelmans a rejected construction and leaves the choice to the author (L253); hypotheses and verdicts, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (281 lines for `dramatica-dual-storyform-mappi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of hypotheses: write „the storyform mapping analysis tests …“, „… keeps …“, „… rejects …“ and name the branch or alternative a line belongs to; a hypothesis is a hypothesis, a verdict the report's own. Its storyform symbols were lost in the export (gaps after „Alternative“, „in“) — never fill them, quote around them; never map its storyforms onto `Plan/storyform/`.

## Pages — document 232, `dramatica-dual-storyform-mapping-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L53, L59, L61, L67, L69, L75, … (34 lines). central (2–4): „AEGIS (Antagonist-System) ist ein autopoietisches System“ (L53); the hypothesis that AEGIS fails at a dogmatic internal illusion, Mind (L59), allowed because „Dramatica erlaubt KI-Systeme in Fixed Attitude“ when the problem is a dogma (L61); the processual alternative: AEGIS's erasure as a physical process, AEGIS as MC in Physics (L67–L69); the rejected branch that AEGIS, with four Guardians, may never hold „I“ (L75).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L121. occurrence: `Alters` stands in a table cell about psychological warfare (L121); read on kael.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L75. not read: named once among the four Guardians (L75); read on guardians.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L15, L17, L89, L93, L203. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L15. minor (1–3): the Dual-Kernel-Theorie, in which every act of control produces the entropy it fights, read as a self-fulfilling dogma of the Mind domain (L89).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L89. occurrence: `Entropie` stands in the DKT sentence (L89), read on dkt.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L75, L103. minor (1–3): a tested and rejected branch: AEGIS's „dezentralen Architektur (vier Guardians: LogOS, Mnemosyne, Cerberus, Kairos/Sophia)“ as the reason it could never hold the pronoun I (L75).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L17, L33, L52, L54, L61, L69, … (27 lines). central (2–4): the report's summary: both surviving candidates anchor Juna inside the quad instead of in the paraconsistent space (L17); branch 1 rejected because an empty IC throughline tears the causal calculation (L54); Juna as IC in both forms, working through a zero-knowledge proof (L69, L100); Juna „spukt als Subtext“ in the RS (L122).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L59, L60, L62, L67, L88, L91, … (23 lines). central (2–4): the hypothesis that Kael experiences the conflicts as an external limitation, Universe (L59); Kael as „Mensch mit dissoziativer Identitätsstörung“ (L62); his inner dissociation as a process, Psychology (L67); the strongest counter-evidence, reducing „Kaels 13-Alter-System“ to a Universe situation (L91) — quote around the digits; his fight against the narrowness of the Konstrukt-Stadt (L171).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L75. not read: named once as „Kairos/Sophia“ among the Guardians (L75); read on guardians.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L98, L171. minor (1–3): the Universe mapping mirroring the physical limits of the Konstrukt-Stadt (L98); Kael fighting „gegen die physische Enge der Konstrukt-Stadt“ (L171).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L75. not read: named once among the four Guardians (L75); read on guardians.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L75. not read: named once among the four Guardians (L75); read on guardians.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L90, L122, L255. minor (1–3): the Moonshine-Link construct (vertex operator algebra on the Leech lattice) as an incomprehensible physical phenomenon (L90); its physical presentation in prose an „ungelöste stilistische Herausforderung“ (L255).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L17, L41, L137. minor (1–3): the system juggling erasures while the host orchestrates his multiplicity (L137).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L240. occurrence: `Risse` stands in the report's own reflection, „keine offensichtlichen Risse in der Logik“ (L240), not the world's Risse.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L75. not read: named once as „Kairos/Sophia“ (L75); read on guardians.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L232. occurrence: `Truth-Rotation` stands in the report's kickoff reflection (L232); not read.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L60, L62, L91, L93, L145, L234. minor (1–3): whether Kael in Universe can carry his TSDP dissociation (L60); the counter-evidence that a Universe situation misses TSDP's phenomenological depth (L91).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `Lateral-Extern` (near `alex`). occurrence: `Lateral-Extern` is an inversion type, not Alex.
- `alters`: `Alter` (near `alters`). occurrence: `Alter` stands in compounds and `Alternative` (L17); not read.
- `kairos`: `Kairos/Sophia` (near `kairos`). occurrence: `Kairos/Sophia` read on guardians (L75).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `sophia`: `Kairos/Sophia` (near `sophia`). occurrence: `Kairos/Sophia` read on guardians (L75).
- `vortex`: `Vortex-Inversion` (near `vortex`). occurrence: `Vortex-Inversion` is a mapping mechanism (L61); not the Vortex.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: a tested and rejected branch — AEGIS's decentralised architecture of four Guardians, LogOS, Mnemosyne, Cerberus, Kairos/Sophia (L75).
- **`q3-how-many-kern-welten-and-alters`**: „Kaels 13-Alter-System“ in the counter-evidence (L91).
- **`q8-aegis-after-the-vortex`**: the post-Vortex AEGIS signature in the Algorithmische Melancholie after the driver pivot, left open (L254).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link as an incomprehensible physical phenomenon (L90); its prose presentation unsolved (L255).

**Not promoted:** the mapping vocabulary (Involution, Domain-Bijektion, Triple-Stack), the two transpositions, ZKP, the Landauer link, the logs and audits.

**One reader**: aegis, kael, juna, guardians, dkt, konstrukt-stadt, moonshine-link, multiplizitaet, tsdp and the records q1, q3, q8, q9.

**Chapter readings**: none.
