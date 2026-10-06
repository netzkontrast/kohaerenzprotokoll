# Brief — readings from document 163 (step 6)

1 document, one reader, one batch: `ingest-163`. Files go to `Plan/runs/ingest-163/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 163 | `kohaerenz-protokoll-architecture-synthesis` | 2026-04-28 | „the architecture synthesis“ (titled `Final Architecture Validation, Inversion-Tested Concept Synthesis, and Plot-Outline-Ready Bilingual Brief`) | a bilingual EN/DE brief of 2026-04-28 that puts the architecture through a „Phönix-Mode inversion test“ (L21) axis by axis, with appendices, the audit log of the process that wrote it (Part III, a first person naming no speaker) and a plot-outline handoff (Part IV); its verdicts („Inversion Superior“, „Pass“) are its own — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (416 lines for `kohaerenz-protokoll-architectu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A brief that proposes an inverted architecture and grades it: write „the architecture synthesis proposes / places / judges …“, never as canon. Its central move is the inversion — AEGIS from K₁ to K₀, Kael from K₀ to K₁ (L23, L27, L288) — and every reading on a kernel page says it is that brief's inversion, and what it inverted from („the canonical architecture positioned …“, L23). Part III (L214–L328) is the process's audit log: „the audit log reports …“, never the brief's claim — its L231 states the opposite alignment as a contradiction it found in its inputs. Quote English as English and German as German, never translated; the export lost nothing but the kernel subscripts keep (`K₁`, `K₀`) — quote them as written; cut before inner straight quotes.

## Pages — document 163, `kohaerenz-protokoll-architecture-synthesis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L27, L31, L33, L39, L42, … (63 lines). central (2–4): „AEGIS’s claimed coherence is an exclusionary simulation“ (L23), the inversion making it „the true K₀“ (L23, L27); „AEGIS claims to be the agent of K₁“ and is „the true K₀ vector“ (L137); it „operates strictly on this principle“ of coherence truth (L155); Storyform B's outcome, Failure/Good, an „Algorithmic Melancholy“ (L61, L376); its LFI-Kern (L73, L187).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L69. minor (1–2): the German Storyform B line (L69); the English names it on L61 and L376.
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L42. minor (1–2): „Relationship Story — Kael & The Alters“ (L42) — read the line.
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L27, L81, L202. minor (1–2): Juna as „Chaitin-Konstante (Ω)“ (L81); the appendix abstract (L202); L27 if it names it — read the line.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L131, L133, L274, L288, L290, L321, … (8 lines). The sweep found `Dual-Kernel-Theorie (DKT)` alone on L131. minor (1–2): „Dual-Kernel Theory (DKT), as theorized by Giannakopoulos“ (L133); the DE abstract (L131); the axis table, inverted (L288).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L131. minor (1–2): the DE abstract tests the kernels against „thermodynamischer Entropie“ (L131): the physical sense.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L23, L27, L77, L79, L81, L163, … (21 lines). central (2–4): „Juna's ontology is finalized as a composite construct“ (L79): Gödel-sentence and Chaitin's constant; she provides the Moonshine-Link and „she remains the extradiagetic anchor“ (L79, L81); the Witness Function's entanglement layer (L177); the verdict, „a composite of (c) and (d)“ (L212).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L27, L31, L33, L37, L40, … (61 lines). central (2–4): the inversion making his reality „the true K₁“ (L23, L27); Storyform A's Main Character, Domain Universe (L40); „Kael embodies Correspondence“ (L157); 11 entities integrated, „Functional Multiplicity“ presented to the LFI-Kern (L73, L75); „Kael acts as the Prover“ (L178); the Vortex beats (L187–L189); „The Gardener“ (L99).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L73, L137, L187, L373. minor (1–2): among the 11 entities (L73) and the EPs AEGIS erases (L137, L187).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L1. occurrence: the title (L1).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L65. minor (1–2): Storyform B's Objective Story, „Der Zusammenbruch der Konstrukt-Stadt“ (L65).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L73, L187, L373. minor (1–2): an ANP among the 11 entities (L73, L187).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L23, L27, L79, L81, L163, L169, … (8 lines). minor (1–2): Juna provides it, via Whitehead's prehension (L79); the DE abstract validates it on Vertex Operator Algebra (L163); AEGIS „topologically blind“ to it (L169).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L73, L137, L187, L373. minor (1–2): among the EPs AEGIS erases (L137, L187).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L73, L75, L375. minor (1–2): the rendering boundary resolving into „a Mosaik-Herz“ at the Vortex Inversion (L73, L75); „Mosaik-Herzen“ in the handoff (L375).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L27. minor (1–2): „Functional Multiplicity“ presented to AEGIS (L73), „Funktionalen Multiplizität“ (L75) — the German writes it in „…“: cut inside; L27 if it says it — read the line.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nichts-Rauschen` alone on L27. minor (1–2): AEGIS's flawless inner consistency „als selbstreferenzielles Nichts-Rauschen entlarvt“ (L27) — the brief's metaphor, recorded as it stands.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L73, L137, L187, L373. minor (1–2): among the EPs AEGIS erases (L137, L187).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L27, L43, L51, L381. minor (1–2): Storyform A's driver, Action „manifesting as reality glitches“ (L43, L51); Kael's loops preserve information „über Risse hinweg“ (L27).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L41, L49, L348. minor (1–2): Storyform A's Influence Character, „Selene/The Guardian“, Domain Mind (L41, L49, L348).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L221. minor (1–2): „the Archivist“ among Kael's 11 entities — in the audit log (L221): „the audit log reports“.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L188. minor (1–2): „AEGIS initiates the ultimate Trennungsprotokoll“ in beat 2 (L188).
- **`truth-rotation`** (minor, 1–4): the census's surfaces — `Truth Rotation` L290. minor (1–2): the axis table: „The Truth Rotation perfectly aligns with the DKT inversion“ (L290); the rotation confirmed (L31, L33).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L139, L294, L322, L381. minor (1–2): Kael's „dissociative loops (TSDP)“ preserve mutual information (L139); the reader axis (L294).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L27. not read: L27's „exkludierende Simulation“ is AEGIS's claimed coherence, not the simulation as a place — an occurrence.
- **`vortex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vortex` alone on L23. central (2–4): „The Vortex Inversion occurs at the exact climax“ (L73), `Wahrheits-Vortex` in German (L75); „the singular plot mechanism that forces the inversion of the two storyforms“ (L185); the three beats (L187–L189); the handoff (L373, L375).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Kern` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence: the project's name and the truth theory, no reading of Kohärenz itself.
- `kohaerenz-kernel`: `Kohärenz-Kern` (near `koharenzkernel`), `Kohärenz-Kern` (near `koharenzkernelk1`). a reading: `Kohärenz-Kern (K₁)` placed with AEGIS by „the canonical architecture“ and then Kael's by the inversion (L27); the Correspondence Theory mapped to it (L31, L33).
- `kollaps-kernel`: `Kollaps-Kern` (near `kollapskernel`), `Kollaps-Kern` (near `kollapskernelk0`). a reading: `Kollaps-Kern (K₀)` — Kael's by the canonical architecture, AEGIS's by the inversion (L27); the Coherence Theory mapped to it (L31, L33).
- `vortex`: `Vortex Inversion` (near `vortex`), `Wahrheits-Vortex` (near `vortex`). a reading — on vortex above.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: „11 entities“ (L73, L75) with Lex, Nyx, Kiko, Moros, Vesper and, in the audit log, Silas (L187, L221).
- **`q8-aegis-after-the-vortex`**: Storyform B, Failure/Good, an „Algorithmic Melancholy“ (L61, L376); „The system fails“ (L375).
- **`q9-moonshine-link-boundary`**: no classical signal, the no-signaling theorem (L169); AEGIS topologically blind.

**Not promoted:** Vesper, the Gardener, The Foundation, Sea of Potentiality, the Paraiyas, the Witness Function, the LFI-Kern, Sector 04, Dualitäts-Disziplin, Storyform A/B (their pages are `Plan/storyform/`), Optionlock, the truth theories, OSIRIS, the scholars, the Landauer heat (physics of erasure, not the sensory rule of C11).

**Two readers**, disjoint: (1) kael, juna, alters, selene, silas, lex, nyx, kiko, moros, multiplizitaet, tsdp, moonshine-link, mosaik-herz, chaitin-konstante and the records q3, q9; (2) aegis, dkt, kohaerenz-kernel, kollaps-kernel, truth-rotation, vortex, trennungsprotokoll, risse, konstrukt-stadt, algorithmische-melancholie, entropie, nichts-rauschen, and the record q8.
