# Brief — readings from document 255 (step 6)

1 document, one reader, one batch: `ingest-255`. Files go to `Plan/runs/ingest-255/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 255 | `research-prompt-dramatica-dual-storyform-mapping-md` | 2026-04-30 | „the mirroring prompt“ (a German research prompt) | a prompt for an executing agent asking for a Dramatica dual-storyform mirroring with at least two alternatives, specifying a frame (MIRROR), constraint blocks, methods, steps and an empty output template; it reports no finding, and its only statements about the novel are the capsules of its Story-Hintergrund (L187–L225); light pass |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1040 lines for `research-prompt-dramatica-dual`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass, a prompt: write „the mirroring prompt's background capsule gives …“; the capsules are the constraints it hands an agent, not findings. Read only where a capsule adds something of its own; the rest of the prompt (method, frame, template) is not read. It reports a user directive of 2026-04-29 that no earlier storyform is canon (L225): record it as the prompt's report, decide nothing.

## Pages — document 255, `research-prompt-dramatica-dual-storyform-mapping-md`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L197, L201, L205, L209, L213, L217, … (8 lines). minor (1–3): the capsule: a tragic god, autopoietic, operationally closed, misreading Qualia as noise, erasing by functioning rather than violence; its true Kollaps-Kern (K0) producing Landauer heat and entropy by erasure sweeps (L197).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L209. not read: light pass — named in a capsule list (L209), read on guardians.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L217, L313. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L217. minor (1–3): the capsule: AEGIS believes it is K1, the coherence kernel, but is K0, the entropy kernel; every act of control produces the entropy it fights (L217).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L197. not read: light pass — a prompt; no capsule adds to this page.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L209. minor (1–3): the capsule: four functional subsystems of AEGIS — LogOS, Mnemosyne, Cerberus, Kairos/Sophia — correlating with the four Kernwelten and showing inner guardian conflicts (L209).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L131, L175, L201, L205, L213, L313, … (17 lines). minor (1–3): the capsule: Impact-Charakter / Witness, a composite of quantum witness, Gödel sentence and Chaitin-Ω, irreducible and unmodellable for AEGIS, operationalised as a fifth position outside the standard Dramatica quad (L201).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L193, L205, L213, L313, L559. minor (1–3): the capsule: a human with DID, a 13-alter system — 5 ANPs, 5 EPs, 1 Sonder-Alter, 2 Spiegel-Alter (L193); the 13 alters by function, from Host to AEGIS-Echo (L213).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L209. not read: light pass — a prompt; no capsule adds to this page.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L209. not read: light pass — the four Kernwelten stand in the Guardians capsule (L209), read on guardians.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: light pass — a prompt; no capsule adds to this page.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L209. not read: light pass — named in a capsule list (L209), read on guardians.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L209. not read: light pass — named in a capsule list (L209), read on guardians.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L205, L313. minor (1–3): the capsule: a non-local connection Kael↔Juna over a vertex operator algebra on the Leech lattice (rank 24), orbifold-constructed, invisible to AEGIS (L205).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L209. not read: light pass — a prompt; no capsule adds to this page.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter-System` (near `alters`). occurrence: light pass, a prompt; not read.
- `chaitin-konstante`: `Chaitin` (near `chaitinkonstante`). occurrence: light pass, a prompt; not read.
- `entropie`: `Entropie-Kern` (near `entropie`). occurrence: light pass, a prompt; not read.
- `kairos`: `Kairos/Sophia` (near `kairos`). occurrence: light pass, a prompt; not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Kern` (near `koharenz`). occurrence: light pass, a prompt; not read.
- `kohaerenz-kernel`: `Kohärenz-Kern` (near `koharenzkernel`), `Kohärenz-Kern` (near `koharenzkernelk1`). occurrence: light pass, a prompt; not read.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: light pass, a prompt; not read.
- `sophia`: `Kairos/Sophia` (near `sophia`). occurrence: light pass, a prompt; not read.
- `vortex`: `Vortex-Inversion` (near `vortex`). occurrence: light pass, a prompt; not read.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: 13 alters — 5 ANPs, 5 EPs, 1 Sonder-Alter, 2 Spiegel-Alter (L193), listed by function (L213); four Kernwelten correlating with four Guardians (L209).
- **`q1-guardians-and-aegis`**: the Guardians as four functional subsystems of AEGIS (L209).
- **`q5-guardians-and-kern-welten`**: four Guardians — LogOS, Mnemosyne, Cerberus, Kairos/Sophia — correlating with the four Kernwelten (L209).
- **`q9-moonshine-link-boundary`**: Kael↔Juna, non-local, invisible to AEGIS (L205).

**Not promoted:** everything of the prompt's own — MIRROR, the constraint blocks, methods and steps, the Vortex-Inversion capsule, the output template.

**One reader**: kael, aegis, juna, guardians, moonshine-link, dkt and the records q3, q1, q5, q9. Light pass: logos, mnemosyne, cerberus and kern-welten are not read.

**Chapter readings**: none.
