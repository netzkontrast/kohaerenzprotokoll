# Brief — readings from document 407 (step 6)

1 document, one reader, one batch: `ingest-408`. Files go to `Plan/runs/ingest-408/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 407 | `dramatica-dual-storyform-mapping-protokoll` | 2026-04-30 | „the dual-storyform mapping report“ (an unsigned German „Mathematische Mapping-Absicherung und duale Storyform-Synthese im Kohärenz-Protokoll“) | maps two storyforms — A „Heuristik der Integration“ with Kael, B „Phoenix Collapse“ with AEGIS as MC and Kael as IC — onto the DKT and group-theory vocabulary, sorted into consensus, contradictions, gaps and synthesis, with two mirroring alternatives, a 39-chapter phase model and a signpost table; it calls the mapping „stabil“ and the protocol ready (recorded, not applied); predates decision 025 |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (288 lines for `dramatica-dual-storyform-mappi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report on storyforms of its own: write „the dual-storyform mapping report says …“ and say whose storyform (its A or its B, or its Alternative 1 or 2) a value belongs to; its values are not storyforms A and B of decision 025 — never apply them. Where it settles a contradiction it reports, record its resolution as its own. Quote the German as written; cut before straight and nested quotes, bold markers and glued footnote digits; kernel symbols are missing in the export (empty parentheses, „dem -Kernel“), quote around them. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). Never write a real person's name; the document names several (L167, L169, L175) — describe what those lines say without them. The chapter ranges (L163–L185, L224–L235) get no chapter readings; single chapters do.

## Pages — document 407, `dramatica-dual-storyform-mapping-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L32, L40, L49, L69, L71, … (20 lines). central (4–8): AEGIS (Autonomous Entropic Gatekeeper for Integrity Systems) watching the coherence kernel's Konstrukt-Stadt (L23); in its Storyform B „AEGIS zwingend als Main Character“ (L32), in its table Overall Story with the Konstrukt-Stadt (L49); contradictory placings of AEGIS in the kernel hierarchy and its resolution „AEGIS ist, was AEGIS verhindert“ — cut before italics markers, quote around them (L71–L75); MC in the even chapters in Alternative 2 (L154); AEGIS's attempts to heal the dissociation as an antagonistic act (L253).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L155, L176. minor (1–3): in Alternative 2 „Juna fungiert als die Chaitin-Konstante“, the incompressible fixed point in both storyforms (L155); its discovery in Kapitel 19–22 (L176).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L157, L241, L247, L251. minor (1–3): Alternative 2 „ideal für die Darstellung der DID-Thematik“ (L157); Kael's structural dissociation (DID) as no defect but a survival architecture (L251).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L13, L17, L48, L73, L109, L121, … (9 lines). The sweep found `Dual-Kernel-Theorie (DKT)` alone on L13. minor (1–3): the validation of the dual-storyform structure „unter Anwendung der Dual-Kernel-Theorie (DKT)“ (L13); the architecture „durch die Dual-Kernel-Theorie und die VOA-Konstruktion mathematisch abgesichert“ (L195).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L24. not read: an occurrence — entropy as what the collapse kernel manifests (L24), read on kollaps-kernel.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L31, L34, L36, L50, L61, L137, … (15 lines). central (4–8): its Storyform A: Kael's engagement with „der relationalen Tiefe von Juna“ (L31); Juna not only a character but a mathematical-structural anchor in the simulation (L36); in its table Relationality, Influence Character (You) (L50); the Juna-Asymmetrie-Bruch in Sektor 04 (L61, L63) resolved as a functional paradox (L195); Juna as the Chaitin constant (L155); Juna unmasked as „Mosaik-Herz“ in Kapitel 23–26 (L177).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L32, L44, L51, L86, L89, … (21 lines). central (4–8): its Storyform A follows „den Integrationsprozess des Protagonisten Kael“ (L31); in its Storyform B Kael is the Influence Character, a „lebende Dialetheia“ (L32); in its throughline table Kael is the Interface with the Witness-Funktion, Main Character (I) (L51); its resolution: „Kael ist das Interface, durch das das System sich selbst wahrnimmt.“ (L89); in Alternative 2 Kael and AEGIS share the MC slot, Kael in the odd chapters (L154); Kael the operator who witnesses Juna (L191); Kael becoming „Netzwerker“ (L184).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title (L13).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L21. minor (1–3): „dem Kohärenz-Kernel“, the reversible, information-preserving domain founding the Konstrukt-Stadt (L21, L23).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L21. minor (1–3): „dem Kollaps-Kernel“, the irreversible collapse, entropy and the arrow of time, entering as noise or glitches (L21, L24).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L23, L49, L207. minor (1–3): the coherence kernel as the foundation of the Konstrukt-Stadt, a hyper-structured environment eliminating erosion (L23); in its table the Konstrukt-Stadt with AEGIS as Overall Story (L49); a lattice algebra as blueprint for the Konstrukt-Stadt (L207).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L23, L81. minor (1–3): earlier descriptions of the city stressing total surveillance and global consistency „durch LogOS“ (L81).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L177, L233. minor (1–3): in Kapitel 23–26 Juna unmasked as „Mosaik-Herz“ (L177); the signpost table's row 31-34 „Das Mosaik-Herz“ (L233).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L40, L226; `Glitches` L24. minor (1–3): the repression of traumatic memories generating physical heat that leads to the Risse (L40); the collapse kernel entering as „Rauschen“ or „Glitches“ (L24); the table's row 7-10 „Zeitdilatation / Risse“ (L226).
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L63. minor (1–3): the conflict over the evaluation of the systemic „Bruchs“ in Sektor 04 (L63); early PDFs calling it an unstable system error or „Erzählloch“ (L65).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L36. not read: an occurrence — the simulation in the general sense (L36).
- **`verschraenkungs-insel`** (minor, 1–4): the census's surfaces — `Verschränkungs-Insel` L79. minor (1–3): „In Kapitel 33 wird eine „Verschränkungs-Insel“ beschrieben“ — cut before the nested quote — causally isolated from the rest of the system (L79); its isolation an effect of entanglement undermining AEGIS's access (L82).
- **`vortex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vortex` alone on L88. minor (1–3): the „Story-Mind Vortex“ in which Kael and AEGIS are inseparably entangled, per a final architecture validation the report cites (L88).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Zielkohärenz` (near `koharenz`). decided with the pages above: `Juna-Asymmetrie-Bruch` read on juna and sektor-04; `Rauschen` the collapse kernel's noise, read on risse with `Glitches`; `Autonomous Entropic Gatekeeper for Integrity Systems` AEGIS's expansion, read on aegis; `Story-Mind Vortex` read on vortex; `Zielkohärenz` the final status report's phrase; `Dual-Kernel-Theorie` read on dkt.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). decided with the pages above: `Juna-Asymmetrie-Bruch` read on juna and sektor-04; `Rauschen` the collapse kernel's noise, read on risse with `Glitches`; `Autonomous Entropic Gatekeeper for Integrity Systems` AEGIS's expansion, read on aegis; `Story-Mind Vortex` read on vortex; `Zielkohärenz` the final status report's phrase; `Dual-Kernel-Theorie` read on dkt.
- `vortex`: `Story-Mind Vortex` (near `vortex`). decided with the pages above: `Juna-Asymmetrie-Bruch` read on juna and sektor-04; `Rauschen` the collapse kernel's noise, read on risse with `Glitches`; `Autonomous Entropic Gatekeeper for Integrity Systems` AEGIS's expansion, read on aegis; `Story-Mind Vortex` read on vortex; `Zielkohärenz` the final status report's phrase; `Dual-Kernel-Theorie` read on dkt.


**Pages beyond the draft:**
- **`externe-ebene`** (minor, 1): Kapitel 36–39's „Grenzüberschreitung zum externen Level (Köln 2026)“ (L185); in Kapitel 36 Kael looks into the screen (L215).

**Record entries** (one file, formatted as earlier entries on C13 — `ls Plan/runs/ingest-*/readings/c13-*`):
- **`c13-externe-ebene-beyond-the-simulation`**: the report's phase model crosses the border „zum externen Level (Köln 2026)“ in Kapitel 36–39 (L185) — recorded, not applied and not decided.

**Chapter readings** (batch `ingest-408-kap`, one file per chapter, `Plan/runs/ingest-408-kap/readings/kap-NN--dramatica-dual-storyform-mapping-protokoll.md`, formatted as in `Plan/runs/ingest-397-kap/readings/`):
- **`kap-24`**: „Kapitel 24 führt „Epigenetische Geister“ ein“ — cut before the nested quote — which change the neural structure through the architecture, not yet tied to the kernels (L109).
- **`kap-33`**: the Verschränkungs-Insel described in Kapitel 33, causally isolated from the rest of the system (L79).
- **`kap-35`**: the separation of Kael and AEGIS „eine phänomenale Illusion, die in Kapitel 35 dekonstruiert wird“ (L89).
- **`kap-36`**: Kael looking into the screen in Kapitel 36 (L215).

**Pages not read:** entropie, kohaerenz, ueberwelt — occurrences.

**Not promoted:** Storyform A „Heuristik der Integration“, Storyform B „Phoenix Collapse“, Phoenix Mode, lebende Dialetheia, Witness-Funktion, Wir-Geflecht, Protokoll-Instanz, 5. Position, Juna-Asymmetrie-Bruch, Erzählloch, Dialetheia-Toleranz, Spiegelungs-Alternative 1 and 2, Orthogonale Inversion, Möbius-Verschränkung, Wärme-Metrik, Epigenetische Geister, RIVE-Protokolle, Secure Isolation State, Netzwerker, Pixel der Realität, Zielkohärenz, Survival Architecture, and the borrowed concepts.

**One reader**: every page above, the C13 entry and the four chapter readings.
