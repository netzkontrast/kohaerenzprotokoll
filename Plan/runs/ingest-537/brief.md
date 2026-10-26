# Brief — readings from document 537 (step 6)

1 document, one reader, one batch: `ingest-537`. Files go to `Plan/runs/ingest-537/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 537 | `kohaerenz-protokoll-finaler-plot-blueprint` | 2025-04-20 | „the final plot blueprint“ | a German plot blueprint that answers the conceptual core questions (Teil 1), gives 39 steps in 3 × 13 with seven fields each (Teil 2) and calls itself complete and „schreibfertig“ (L15, L383); its own claim, recorded, not applied; the bond partner is named throughout by an earlier name|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (384 lines for `kohaerenz-protokoll-finaler-pl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan that declares itself final: write „the final plot blueprint proposes …“; never canon. **Never cite these lines (an earlier name or a person's name): 27,33,34,35,39,40,60,65,79,84,97,101,102,128,129,132,143,160,170,174,184,185,198,199,202,212,213,215,271,283,298,299,326,327,328,340,343,344,354,368,370,377.** Never write the bond partner's name in any form; never put Juna's name on what the blueprint says of the partner. `K-J-…` compounds are not glossed. No gendered pronoun for Kael, AEGIS or the Guardians in our own prose; quotations stay verbatim, cut before pronouns where possible.

## Pages — document 537, `kohaerenz-protokoll-finaler-plot-blueprint`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L28, L29, L33, L34, L35, … (118 lines). central: the Reboot as a failsafe after the v1.4 failure, its learning only pattern recognition (L41); v1.5's changes (L50–L52); fails at Einsamkeit and Zweck as an information-processing system (L56); AEGIS's analysis in 2.1–2.3, correct data, wrong interpretation (L227, L228); escalates and triggers the Welle (L269); completes the Reboot (L312).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L128. not read: `Alters` stands only on a line with an earlier name.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L34, L128. not read: `DID` stands only on lines with an earlier name.
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L23, L111, L115, L358, L372. minor: the Kohärenz-Insel as a self-organising entity (L23); the Instrumente der Ordnung as emergence (L111); emergence of new levels (L115, L358); the final act as emergence of a new state (L372).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L33, L34, L42, L56, L74, L79, … (22 lines). minor: AEGIS v1.5 optimises for minimal informational entropy (L56); AEGIS reads Kael's entering the Nexus as a catastrophic rise in „Entropie“ (L227, L228); seeks to eliminate the „Entropie“ (L269).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L67, L69, L79, L106, L107, L116, … (46 lines). minor: start as AEGIS's agents and intervene (L106, L241); their turning point from observing the discrepancy (L256); AEGIS notices their hesitation (L257); the split final, the renegades become Kael's allies (L356).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found (an earlier name) alone on L27. not read: the bond partner is named only by an earlier name, and the blueprint does not make the identity plain.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kael` alone on L27. central: Kaels Essenz as fragment or projection of a Kohärenz-Insel (L23 not — L33 is barred; use only L41, L42); the Instrumente der Ordnung as Kael's own emergent abilities (L42); searching for the Nexus (L200); the paradigm shift in the Nexus (L214); accepts the Kernwelten as psyche (L284); toward „Funktionale Multiplizität“ (L300); the final choice (L356).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L41, L103, L109, L111, L213, L227, … (22 lines). minor: the Kernwelten as psyche (L103, L284); a battlefield (L244); collapse in the Welle (L272); the journey through the Kernwelten (L297); their borders become visible (L357).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11) (J9).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L65, L300. minor: „Funktionale Multiplizität“ as parts cooperating as aspects of a coherent whole (L300).
- **`nexus`** (central, 3–12 quotations): the census's surfaces — `Nexus` L102, L103, L193, L197, L198, L199, … (20 lines). minor: the search for the Nexus (L193, L200); „Eintritt in den Nexus“ as end of Part 1 (L103, L207, L211); Kael's paradigm shift there (L214); the Guardians ordered to remove Kael from it (L241).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L23, L35, L39, L40, L83, L269, … (11 lines). minor: the unstructured space of pure possibility around AEGIS's domain (L23); access to it as a path out of AEGIS's control (L83); the Welle as the island's essence interacting with it (L270); its elements breaking into the Kernwelten (L272); glimpses at the end (L357, L371).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L23. not read: an occurrence — „andere Realitätsebenen“ (L357) as a hint, not the paged term.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L34, L40, L128, L131, L198, L199, … (11 lines); `Glitches` L128, L129, L142, L170, L198, L212, … (8 lines). minor: the expected logic of the environment „Risse bekommt“ (L128 is barred — not cited); glitches as name „The Glitch in Logic“ (L127). Read only from L127.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L40. not read: `Simulation` stands on a barred line (L40).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Mustererkennung` (near `mustererkennunganomaliedetektion`). an occurrence: Mustererkennung as AEGIS's learning (L41), read on aegis.
- `kael`: `Kaels` (near `kael`). a reading: `Kaels` — read on kael above.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: the possessive.
- `kohaerenz`: `Kohärenz-Insel` (near `koharenz`), `Kohärenz-Insel-Essenz` (near `koharenz`). occurrences: the Kohärenz-Insel and the title (J9).


**Reading by the sentence beyond the lookup:**
- **`protokoll-v14`** (minor): the Reboot after „das katastrophale Versagen der v1.4-Protokolle“ (L41); v1.5's faster response from the analysis of the v1.4 failure (L52); AEGIS (v1.4) reaching its limits (L200); v1.4 limitations (L228).

**Chapter readings:** none — the 39 steps are numbered 1.1–3.13, not `Kap`.

**Record entries:** none.

**Not promoted:** Kohärenz-Insel and its parts, K-J compounds, Gleichzeitigkeit, Instrumente der Ordnung, PMAS, CCPP, RIVE, SARM, OBP, v1.5, Reboot, Loyalisten, Zweifler, Welle von Unmöglichkeit, the step titles in German and English, the theory lenses.

**One reader**: every page above.
