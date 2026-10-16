# Brief — readings from document 278 (step 6)

1 document, one reader, one batch: `ingest-279`. Files go to `Plan/runs/ingest-279/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 278 | `kohaerenz-protokoll-synthese-integration` | 2025-12-05 | „the integrated synthesis“ (an unsigned German research report) | a research report calling itself „Integriertes Kohärenz-Protokoll“ that synthesises numbered source documents: System Kael and its parts, AEGIS, the Dual Kernel Theory, the war of truth theories, a mosaic and gravitation architecture with four chapter zones, Juna and the Moonshine-Link, and a three-phase plan; it calls itself the operative executive of a research task and ends „Status: Protokoll aktiv.“ (L241), its claims |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (284 lines for `kohaerenz-protokoll-synthese-i`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis report: write „the integrated synthesis reports / describes / plans …“; much of it reports its source documents („Die Dokumente …“) — say so. Its plan (L205–L243) is advice. **Do not read or cite L17 beyond the label „System Kael“, L19, L150, L213–L222, L231 or L237** (passages outside the novel's world). Kernel symbols are written as `$K\_1$`/`$K\_0$`; quote around them.

## Pages — document 278, `kohaerenz-protokoll-synthese-integration`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L61, L63, L65, L67, L70, L71, … (31 lines). central (3–6): „Autonomous Entropic Gatekeeper for Integrity Systems“, „eine tragische Figur“ (L63); autopoietic, its binary code of coherence (L67–L69); its Hamartia (L70); a Maxwell's demon whose memory wipes produce more entropy, the cracks its waste heat (L73, L79); the domain of K1 with the ANPs (L93); its fate as the documents describe it, Algorithmische Melancholie (L139); failing by coherence through subtraction (L239).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L39, L46. minor (1–3): „Alex fungiert als hypervigilantes Abwehrsystem“ (L39).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L139. minor (1–3): „Die Dokumente beschreiben das Schicksal von AEGIS“ as Algorithmische Melancholie (L139).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L83, L87, L103. minor (1–3): „Dual Kernel Theory (DKT)“, attributed with a hedge (L83); consciousness at the border of the kernels (L103).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. not read: occurrence — `Entropie` (L19) in a passage not read.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L63. minor (1–3): the Genesis-Krise as the occasion of the exiled Ursprungs-Ich (L194); `Genesis` at L63 names a source document's title.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L188, L190, L192, L194, L198, L201, … (7 lines). central (3–6): „Juna/V“ as catalyst (L190); the documents point to a double nature, the exiled Ursprungs-Ich of AEGIS and Kael, with the Genesis-Krise as occasion (L194); the Moonshine-Link (L198); AEGIS cannot see the connection (L200).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L25, L27, L31, L37, … (37 lines). central (3–6): „System Kael“ (L17, the label only); defined in the core documents as tertiary structural dissociation (L27); „Kael (Host)“ with amnesias for the trauma (L37); the goal not fusion but functional multiplicity (L51); the cracks as EP intrusions into his perception (L59); a living Gödel-Satz (L137); winning by coherence through addition (L239).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L46, L47, L56, L59, L102, L220. minor (1–3): „Ein Kind-Anteil, der die existentielle Angst“ carries (L46); among the EPs of K0 (L102).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: occurrence — the title (L15).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L85, L89. minor (1–3): `$K\_1$` „Der Kohärenz-Kernel“ (L89), the domain of AEGIS and the ANPs (L93).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L85, L98. minor (1–3): `$K\_0$` „Der Kollaps-Kernel/Erasure Field“ (L98), manifest as the Nichts Rauschen, the trauma, the EPs and death (L102).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L38, L93, L161, L219, L237. minor (1–3): „Lex ist ein hochspezialisierter ANP“ (L38).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L196, L198. minor (1–3): „Moonshine-Link“ resting on quantum entanglement (L198); AEGIS cannot see it (L200).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L47, L102. minor (1–3): „Moros verkörpert die totale Unterwerfung“ (L47).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L15, L138, L179. minor (1–3): „Funktionaler Multiplizität“ with co-consciousness, cooperation and systemic responsibility (L51, L55–L56); the lower-case form (L138) only if it adds.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L102. minor (1–3): K0 manifest as the „Nichts Rauschen“ (L102).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L45, L47, L55, L56, L102, L221. minor (1–3): „Nyx ist die Trägerin der Wut“ (L45).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L59, L79. minor (1–3): the „Risse“ and anomalies not software errors but EP intrusions into the ANP's perception (L59); AEGIS's waste heat (L79).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L21, L23, L255. minor (1–3): the clinical theory applied to Kael (L23); tertiary structural dissociation (L27).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L23. not read: occurrence — `Simulation` (L23) in a general sentence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Emergenz-Check` (near `emergenz`). occurrence: `Emergenz-Check` a plan step (L230).
- `genesis`: `Genesis-Krise` (near `genesis`). reading: `Genesis-Krise` (L194).
- `kohaerenz`: `Integriertes Kohärenz-Protokoll` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Der Code der Kohärenz` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence: the report's own name, the title, AEGIS's code (read on aegis) and the theory (read on aegis).
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `Mnemosyne-Archipel` a world's name (J49).
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: `Mosaik` the workflow's structure, not the Mosaik-Herz.


**Record entries** (one file each):

- **`c16-kael-origin`**: the documents point to Juna's double nature, the exiled Ursprungs-Ich of AEGIS and Kael, with the Genesis-Krise (L194) — as the synthesis reports it.
- **`q8-aegis-after-the-vortex`**: the documents describe AEGIS's fate as Algorithmische Melancholie (L139).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link rests on quantum entanglement and AEGIS cannot see it (L198–L200).

**Not promoted:** the gravitation architecture and its zones, the slots, the mosaic workflow, Rhizom, the Ereignishorizont-Dilemma, the PAPA model, the three-phase plan and its steps, the Golden Source Documents.

**One reader**: every page above and the three records; never the excluded lines.

**Chapter readings**: none — the four zones name chapter ranges (L157–L175) as a structure, not a reading of any chapter.
