# Brief — readings from document 539 (step 6)

1 document, one reader, one batch: `ingest-539`. Files go to `Plan/runs/ingest-539/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 539 | `roman-plot-konzept-kohaerenz-protokoll` | 2025-04-20 | „the plot concept“ | a German plot concept: 39 steps in three parts, answers to a research brief section by section, a coherence-type table, arcs for Kael, AEGIS and the Guardians and the world's states; hedged throughout as proposal; tags like „[Genesis: 1.1]“ cite outside texts|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (269 lines for `roman-plot-konzept-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A hedged concept: write „the plot concept proposes …“; never canon. **Never cite these lines (an earlier name or a person-named principle): 15,19,23,27,29,30,31,33,41,43,49,53,68,81,86,96,142,171,192,202,205,208,216,217,258,260,264.** Never write the bond partner's name; `K-J-…` compounds are not glossed. A tag „[Genesis: …]“ names an outside text, not the genesis page. No gendered pronoun for Kael, AEGIS or the Guardians in our own prose; quotations stay verbatim, cut before pronouns.

## Pages — document 539, `roman-plot-konzept-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L19, L20, L21, L23, L27, … (76 lines). central: the crisis reaction „Reinitialisierung seiner Kernfunktionen“ (L40, L114); learns the pattern of Kael's integration, v1.5 (L50); its purpose only self-preservation (L181); in Part 1 a self-assured administrator escalating with v1.4 (L226).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Cognitive Firewall` L30, L39. minor: the Welle overwhelms AEGIS's boundary filters „(**OBP, Cognitive Firewall**)“ (L39).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L29, L31. not read: `Alters` stands only on barred lines.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L29, L51, L77, L202; `Dissoziative Identitätsstruktur` L77. minor: the DID symptoms recede with integration (L51); the dissociative identity structure as symptom of the fragmentation of Kael's essence by AEGIS's control (L77).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L65. minor: the Potentialmeer's rules are „Fluss und Emergenz“, and AEGIS emerged from it (L65).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L15, L29, L30, L39, L52, L67, … (12 lines). minor: Kael's essence's „Entropie“ as qualitative complexity (L76); AEGIS's coherence as low, calculable entropy (L201).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L92. not read: only a heading on L92; its content stands on a barred line (L96).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L15. not read: `Genesis` is a tag citing an outside text („[Genesis: 1.1]“), not the page's term.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L20, L27, L30, L32, L33, L37, … (15 lines). minor: changing perspectives in Part 2 (L20); some rigid enforcers, others curious (L32); become decisive (L37); for them the cracks are proof of system failure (L172).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L68. not read: the bond partner is named only by an earlier name.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kael` alone on L15. central: Kael interacts with Guardians across the Kernwelten (L32); takes control of the integration journey (L47); reaches integration, DID symptoms recede, then „Einsamkeit“ (L51); confronts AEGIS v1.5 (L52); Kael's essence as qualitative complexity (L76); Part 3 arc (L218).
- **`kael-julia-bindung`** (minor, 1–4): the census's surfaces — `K-J-Bindung` L39, L68. not read: the page awaits renaming under decision 028.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L23, L27, L29, L31, L32, L33, … (16 lines). minor: Kael meets Guardians across them (L32); fractures in the consistency of the constructed reality, Kernwelten and Überwelt (L170); begin as oppressive constructs mirroring Kael's fragmentation, devastated by the Welle (L248).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title (L11) and compounds (J9).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L39, L53, L61, L65, L66, … (20 lines). minor: pre-logical informational potentiality, a plenum of contradictory possibilities (L65); Kohärenz-Inseln arise from it (L66); floods the Überwelt in the Welle (L106); Gleichzeitigkeit as connectedness in it (L190); its arc from mythical origin to threat to goal (L250).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L96. not read: on a barred line (L96).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L19, L27, L31, L32, L39, L41, … (13 lines). minor: widespread „Risse“ in the Überwelt (L39); fractures in the constructed reality's consistency (L170); proof of failure for the Guardians (L172); reveal code and glimpses of the Potentialmeer (L259); caused by AEGIS's escalation (L226).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L23, L31, L39, L43, L50, L65, … (16 lines). minor: suffers cracks and reality degradation (L39); flooded with raw potentiality (L106); v1.5 strengthens its borders (L132); starts as AEGIS's ordered domain, damaged in the Welle (L249).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kael`: `Kaels` (near `kael`), `Kael-Problem` (near `kael`). a reading: `Kaels`, `Kael-Problem` — read on kael above.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: the possessive.
- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`), `Insel massiver Kohärenz` (near `koharenz`), `K-J-Kohärenz` (near `koharenz`), `Bibliothek der Kohärenz` (near `koharenz`), `Kaskade von Inkohärenz` (near `koharenz`), `wertvolles Strukturvorgehen der selbst-Kohärenz` (near `koharenz`), … (7). occurrences: Kohärenz-Inseln, Bibliothek der Kohärenz, Kohärenz-Typ and the rest (J9).


**Reading by the sentence beyond the lookup:**
- **`protokoll-v14`** (minor): AEGIS's coherence „(v1.4/v1.5)“ in the table (L201); in Part 1 applying its established protocols „(v1.4)“ (L226).

**Chapter readings:** none — steps, not `Kap`.

**Record entries:** none.

**Not promoted:** Kohärenz-Inseln, K-J compounds, Kael-Problem, Welle von/der Unmöglichkeit, Reinitialisierung, Protokoll v1.5, Gleichzeitigkeit, Einsamkeit, Zweck, Bibliothek der Kohärenz, the coherence types, the Genesis and Forschungsauftrag tags, the theory lenses.

**One reader**: every page above.
