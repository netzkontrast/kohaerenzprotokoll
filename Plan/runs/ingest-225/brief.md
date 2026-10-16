# Brief — readings from document 225 (step 6)

1 document, one reader, one batch: `ingest-225`. Files go to `Plan/runs/ingest-225/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 225 | `research-prompt-dramatica-dual-storyform-synthese-aegis-thro` | 2026-04-29 | „the storyform research prompt“ (a German research prompt for another AI) | a 1856-line prompt asking another AI to synthesise the two Dramatica storyforms and test whether AEGIS belongs in Storyform B's MC (H1, which it reports as the PDF canon), in OS with a Guardian as MC (H2, the commissioner's hypothesis) or split (H3); most of it is method; light pass: it reports a canon and asks questions, it settles nothing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1857 lines for `research-prompt-dramatica-dual`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prompt: what it states of the novel is mostly what it *reports* as the canon of a PDF and a memory („bindende Projekt-Kanon“, L279) — write „the storyform research prompt reports as canon …“; its hypotheses are hypotheses („H2, the commissioner's hypothesis“), its Step 8 items open questions. Its storyform letters match the repository's (A = Kael, B = AEGIS) but its values are its own report — never map them onto `Plan/storyform/`. Light pass: readings only where it states something of its own about the term; method sections are not read. **Never write anything about the author's person; its exclusion of an „autobiografischer Anker“ is not to be repeated on any page.** `--find` drops digits (`K0`, `K1`, `H1`) — quote around them.

## Pages — document 225, `research-prompt-dramatica-dual-storyform-synthese-aegis-thro`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L25, L38, L64, L156, L160, … (64 lines). central (2–4): the research question whether AEGIS sits in Storyform B's MC throughline or belongs in OS (L156); H1 „AEGIS = MC“ reported as the canon's status quo (L164), H2 „AEGIS-als-Totalität = OS, ein Guardian = MC“ as the commissioner's hypothesis (L165), H3 a split (L166); „Truth-Rotation: AEGIS = K0“ reported as canon (L283); the climax read double, AEGIS breaking into Algorithmische Melancholie (L1236).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L330, L333, L1236, L1248, L1296. minor (1–2): Beat 5 of the reported climax, „Rotation: → Algorithmische Melancholie“ (L1248); the open question whether it is a new form of emergent paraconsistent awareness (L1296).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L156, L1064, L1534. not read: light pass — one of four candidate Guardians for MC under H2; read on guardians (L1064).
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L288, L330, L552. not read: light pass — named only in the reported DKT vocabulary list (L288, L330).
- **`dkt`** (central, 3–12 quotations): the census's surfaces — `DKT` L40, L174, L269, L288, L330, L449, … (11 lines). minor (1–2): „DKT als Naturgesetz, nicht Metapher“ reported as canon (L288); no DKT terminology in Act I (L942).
- **`erason`** (minor, 1–4): the census's surfaces — `Erason` L288, L330, L552. not read: light pass — named only in the reported DKT vocabulary list (L288, L330).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L289. minor (1–2): „Klimax = Gödel-Gambit (Kap 35–36)“ reported as canon (L289) — quote around the digits.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L287, L307, L604, L1398. minor (1–2): under H2 a Guardian as Storyform B's MC (L165); the four candidates with roles — LogOS (Truth-Enforcement), Mnemosyne (Memory-Archive, setting of the climax), Cerberus (Boundary-Enforcement), Kairos/Sophia ambivalent, „im Wächter-Zwiespalt verfangen“ (L1062–L1065); AEGIS and the Guardians written in 3rd person, the alters in 1st, reported as canon (L287).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L30, L286, L306, L771, L819, L906, … (14 lines). minor (1–2): Juna's asymmetry reported as canon: a composite, IC in Storyform A, „strukturell außerhalb der Quad“ in Storyform B, never a deus ex machina, never physically described, only through effect (L286); the prompt forbids putting her into a standard quad position in B (L1394).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L283, L593, L604, L904, L907, L947, … (16 lines). central (2–3): „Kael = K1 (Coherence-Kern …)“ reported as canon (L283); Kael as MC (Mind) of Storyform A and IC (Mind) of Storyform B under H1 (L1117–L1118), „Kael als lebende Paradoxie“ (L907); the climax read double, Kael integrating (L1236).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L156, L1065, L1534. not read: light pass — one of four candidate Guardians for MC under H2, „Kairos/Sophia“; read on guardians (L1065).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. occurrence: the title (L15).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L947. not read: light pass — one sample mention in a method block (L947).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L156, L1062, L1534. not read: light pass — one of four candidate Guardians for MC under H2; read on guardians (L1062).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L156, L285, L333, L1063, L1244, L1252, … (7 lines). minor (1–2): the Mnemosyne-Archipel as the climax's setting, reported as canon with the Driver pivot at Kap 35–36 (L285); Beat 1 „Mnemosyne-Archipel → AEGIS-Erasure“ (L1244); Mnemosyne as Memory-Archive-Guardian, „Setting-Träger des Klimax“ (L1063).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L910, L1300, L1634. minor (1–2): the open question whether the Moonshine-Link is structurally exclusive to the Kael–Juna pair (L1300); Storyform A's RS as „Moonshine-Link als physische Anstrengung“ (L910).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L556. not read: light pass — one mention in a method sample (L556).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L156, L1065, L1534. not read: light pass — only as „Kairos/Sophia“, a candidate Guardian under H2; read on guardians (L1065).
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth-Rotation` L283, L297, L1103, L1107, L1148. minor (1–2): „Truth-Rotation: AEGIS = K0 … Kael = K1“ reported as canon (L283); the prompt forbids softening the Truth-Rotation verdict (L297); under H2 the K0 reading would be a story about a Guardian (L1108).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L269, L556, L593, L604, L616. not read: light pass — named as a source category of the method (L269, L593).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L908. occurrence: `Simulation` stands in „Manipulation der Simulation“, Storyform A's OS label (L908), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the H2 candidate, read on guardians, not the Integrity Guardian.
- `alters`: `Alter` (near `alters`). occurrence: `Alter` in „Alter, alle 1st Person POV“ (L287) and the de-canonised list (L309); read on guardians where it bears on POV.
- `chaitin-konstante`: `Chaitin` (near `chaitinkonstante`). occurrence: `Chaitin` stands in the reported mathematics vocabulary, „Chaitin Ω“ (L330); light pass.
- `formel-inversion`: `η-Formel` (near `formelinversion`). occurrence: `η-Formel` stands in the reported DKT vocabulary (L288); light pass.
- `garten-der-stillen-praesenz`: `Stille` (near `gartenderstillenpraesenz`), `Stille` (near `gartenderstillenprasenz`). occurrence: `Stille` is Beat 3 of the climax (L1246), not the garden.
- `kollaps-kernel`: `Kollaps-Kern` (near `kollapskernel`), `Kollaps-Kern` (near `kollapskernelk0`). occurrence: `Kollaps-Kern` stands in the reported canon („Erasure-Kollaps-Kern“, L283) and the vocabulary list (L330); read on truth-rotation; light pass.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is one of the de-canonised alter names (L309).
- `telefon-stille`: `Stille` (near `telefonstille`). occurrence: `Stille` is Beat 3 of the climax (L1246).
- `trennungsprotokoll`: `Trennungsprotokolle` (near `trennungsprotokoll`), `Trennungs-Protokoll-Gefüge` (near `trennungsprotokoll`). occurrence: `Trennungsprotokolle` stands in Storyform B's OS label (L909); light pass.
- `vortex`: `Wahrheits-Vortex` (near `vortex`), `Vortex-Inversion` (near `vortex`). occurrence: `Wahrheits-Vortex` and `Vortex-Inversion` stand in the vocabulary rule (L333) and a method sample; light pass.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: Beat 5 „Rotation: → Algorithmische Melancholie / Driver-Flip Action→Decision“ (L1248) reported from the memory canon and a PDF (L1240); the open question whether it is emergent paraconsistent awareness (L1296).
- **`q9-moonshine-link-boundary`**: the open question whether the Moonshine-Link is exclusive to the Kael–Juna pair (L1300).
- **`q1-guardians-and-aegis`**: under H2 AEGIS-as-totality in OS and a Guardian as MC, the four candidates with roles (L165, L1062–L1065).
- **`c14-aegis-first-person-chapter`**: reported as canon, the alters in 1st person, „außer AEGIS+Guardians = 3rd Person“ (L287).

**Not promoted:** H1/H2/H3, the Driver pivot, Witness Function, the DKT vocabulary list, the de-canonised alter names, the method sections, the output schema.

**One reader** (light pass): aegis, kael, juna, guardians, truth-rotation, goedel-gambit, algorithmische-melancholie, mnemosyne, moonshine-link, dkt, and the records q8, q9, q1, c14.

**Chapter readings**: Kap 35 and 36 — the reported climax, Gödel-Gambit and Driver pivot at „Kap 35–36“ / „Kapitel 35–36“ (L285, L289), by the session (`Plan/runs/ingest-225-kap/`).
