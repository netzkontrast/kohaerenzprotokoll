# Brief — readings from document 234 (step 6)

1 document, one reader, one batch: `ingest-234`. Files go to `Plan/runs/ingest-234/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 234 | `research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m` | 2026-04-30 | „the storyform rebuild prompt“ (a German research prompt) | a 1210-line prompt asking another AI to build a dual-storyform mirror rule and at least two alternative dual storyforms; it declares the earlier Storyform A and B no longer canon (L183, L284, L399) and carries a „Compact Primer“ of the novel (L347–L399); light pass: readings only from the primer |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1211 lines for `research-prompt-dual-storyform`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prompt with a primer: what it states of the novel is the primer's summary — write „the storyform rebuild prompt's primer states …“; its claim that the earlier storyforms are no longer canon is its claim, reported, never applied. Method sections are not read. `--find` drops `K0`, `K1`, `13`, `24` — quote around them. Never write anything about the author's person.

## Pages — document 234, `research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L311, L327, L359, L363, L367, L371, … (13 lines). minor (1–2): „Autopoietisches, operativ geschlossenes System“ that takes itself for the coherence kernel but is the collapse kernel, producing Landauer heat through erasure sweeps; fate: Algorithmische Melancholie (L363) — quote around the digits; the „Roman-Pointe“: AEGIS takes itself for K1 but is K0 (L383).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L363. minor (1–2): AEGIS's „Schicksal: Algorithmische Melancholie“ (L363).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L355. occurrence: `Alters` stands in Kael's line (L355); the alter system is read on alters through the near match below.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L371. not read: named only in the Guardian list (L371); read on guardians.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L383, L387. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L383. minor (1–2): the Dual-Kernel-Theorie: K0 the collapse kernel, irreversible erasure, generating the arrow of time; K1 the coherence kernel, atemporal (L383) — quote around the digits.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L371, L379. minor (1–2): „Guardians (4)“ — LogOS, Mnemosyne, Cerberus, Kairos/Sophia — „vier Sub-Wächter-Instanzen unter AEGIS“, each assigned to one Kernwelt, bearers of the Wächter-Zwiespalt: loyalty to AEGIS against emerging insight (L371) — quote around the digit and the inner straight quotes.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L140, L300, L311, L359, L367, L379, … (8 lines). minor (1–2): Juna as Witness Function, zero-knowledge verifier and Husserlian spectator at once, „algorithmisch irreduzibel, für AEGIS unmodellierbar“, „nie als Deus ex Machina, nie physisch beschreibbar“ (L359).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L355, L359, L367, L379, L465, L527, … (7 lines). minor (1–2): „Fragmentierter Host eines DIS-Systems“ with thirteen alters in four groups, the phenomenological stage of the whole book (L355) — quote around the digits.
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L371. not read: named only as „Kairos/Sophia“ in the Guardian list (L371); read on guardians.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L311, L371, L375. minor (1–2): „Vier diegetische Schauplätze, jeweils einer Computational-Class zugeordnet“, each a narrative phase, KW2–KW3 holding the climax levels (L375) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. occurrence: the title (L15).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L371. not read: named only in the Guardian list (L371); read on guardians.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L371, L690. not read: named in the Guardian list (L371) and in a method step (L690); read on guardians.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L359, L367, L1160. minor (1–2): „Nicht-lokale Verbindung zwischen Kael und Juna“, placed through vertex operator algebras of the Monster group and the Leech lattice, structurally invisible to AEGIS's sensors (L367).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L379. not read: light pass — named only in the primer's alter-system line (L379); read on alters.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L371. not read: named only as „Kairos/Sophia“ (L371); read on guardians.
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth Rotation` L395. minor (1–2): „Truth Rotation“ as the climax mechanism: what is true in Storyform A is functionally inconsistent in Storyform B, and this inversion produces the Vortex (L395) — quote around the inner straight quotes.
- **`vortex`** (minor, 1–4): the census's surfaces — `Vortex` L395, L1160. minor (1–2): the Vortex produced by the inversion of the Truth Rotation (L395).

- **`alters`** (minor, 1–2): the primer's `Alter-System` line: ANPs (Kael-Host, Lex-Rationalist, Alex-Beschützer, Rhys-Pfleger, Selene-ISH), EPs (Nyx-Fight, Kiko-Freeze, Lia-Ambivalent, Isabelle-Sexualisiert, Moros-Kollaps), Sonder (Argus-Meta), Spiegel (Silas-Juna-Echo, Oblivion-AEGIS-Echo); all thirteen in first-person POV (L379) — quote around the digits.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter-System` (near `alters`). a reading — the `Alter-System` line, see the extra page below.
- `coheron`: `Coheronen` (near `coheron`). occurrence: `Coheronen` stands in the DKT line (L383), read on dkt.
- `erason`: `Erasonen` (near `erason`). occurrence: `Erasonen` stands in the DKT line (L383), read on dkt.
- `kairos`: `Kairos/Sophia` (near `kairos`). occurrence: `Kairos/Sophia` read on guardians.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenzkern` (near `koharenz`). occurrence: the title and `Kohärenzkern`, read on dkt.
- `kohaerenz-kernel`: `Kohärenzkern` (near `koharenzkernel`), `Kohärenzkern` (near `koharenzkernelk1`). occurrence: `Kohärenzkern` is K1 in the DKT line (L383), read on dkt.
- `kollaps-kernel`: `Kollaps-Kern` (near `kollapskernel`), `Kollaps-Kern` (near `kollapskernelk0`). occurrence: `Kollaps-Kern` is K0 in the DKT line (L383), read on dkt.
- `ouroboros-struktur`: `Ouroboros` (near `ouroborosstruktur`). occurrence: `Ouroboros` stands in a method passage; not read.
- `sophia`: `Kairos/Sophia` (near `sophia`). occurrence: `Kairos/Sophia` read on guardians.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: thirteen alters in four groups (5 ANP, 5 EP, 1 Sonder, 2 Spiegel) (L355, L379); four Kernwelten (L375).
- **`q5-guardians-and-kern-welten`**: four Guardians, „jeder einer der vier Kernwelten zugeordnet“ (L371).
- **`q1-guardians-and-aegis`**: the Guardians as „Sub-Wächter-Instanzen unter AEGIS“, torn between loyalty and emerging insight (L371).
- **`c14-aegis-first-person-chapter`**: the alters in first person, „AEGIS und Guardians in 3. Person POV“ (L379) — quote around the digit.
- **`q8-aegis-after-the-vortex`**: AEGIS's fate, Algorithmische Melancholie (L363); the post-Vortex AEGIS status named among what research might not settle (L1160).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link structurally invisible to AEGIS's sensors (L367); its boundary named among what research might not settle (L1160).

**Not promoted:** the mirror rule and its vocabulary, T1–T7, the method scaffold, Wächter-Zwiespalt, Witness Function, the computational classes.

**One reader** (light pass, primer only): kael, juna, aegis, moonshine-link, guardians, kern-welten, alters, dkt, truth-rotation, vortex, algorithmische-melancholie and the records q3, q5, q1, c14, q8, q9.

**Chapter readings**: none.
