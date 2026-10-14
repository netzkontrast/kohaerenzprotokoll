# Brief — readings from document 479 (step 6)

1 document, one reader, one batch: `ingest-479`. Files go to `Plan/runs/ingest-479/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 479 | `managing-ontological-risk-defining-the-narrative-integration` | 2025-11-03 | „the ontological-risk report“ (an unsigned English strategy report, „Managing Ontological Risk“) | proposes how ‘Das Fundament’ enters the story without a Deus ex Machina: the Gnosis Protocol ties the resolution to Kael's earned multiplicity; seeded artefacts and a three-stage progression; a proposal, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (71 lines for `managing-ontological-risk-defi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal: write „the ontological-risk report proposes …“; what the narrative „must“ do is its prescription, never a fact of the story. L26 and L64 carry a figure named after a logician — never quote a span containing that name. Quote the English as written; cut before bold, escaped asterisks, straight quotes and inner quotes. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „his“).

## Pages — document 479, `managing-ontological-risk-defining-the-narrative-integration`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L24, L25, L26, L34, L40, … (14 lines). central (4–8): AEGIS's worldview of Kohärenz durch Negation, predicated on classical logic where a contradiction means collapse (L15); Episteme as AEGIS's mode of knowing (L34); AEGIS structurally blind to the Moonshine-Link (L41); the artefacts as unclassifiable noise to AEGIS, like its own Risse (L56); the climax confronts AEGIS's anti-dialetheic logic (L64 — quote only spans without the name).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L39. minor (1–4): functional multiplicity as co-consciousness and cooperation among Kael's internal alters (L39).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L41. minor (1–4): the Moonshine-Link formed with Juna/V as part of Kael's journey (L41).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L19, L24, L25, L26, … (25 lines). central (4–8): Kael's journey toward Kohärenz durch Integration against AEGIS's Kohärenz durch Negation (L15); the climax reframed as Kael perceiving and embodying a passive principle (L19); Gnosis as Kael's earned, experiential mode of knowing (L35); prerequisites: functional multiplicity grounded in TSDP, co-consciousness among the alters (L39), holding contradictory self-states (L40); the three-stage progression from fragmentation to co-consciousness to the final integrated state (L62–L64 — never quote the name in L64); the resolution as Kael acting on earned Gnosis (L43).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence — the title in L15; the two Kohärenz compounds are read on kael and aegis.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L41. minor (1–4): the Moonshine-Link with Juna/V, a non-local sub-protokollarische Verbindung, an ontologischer Exploit to which AEGIS is structurally blind (L41).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L56, L62. minor (1–4): AEGIS's system failures, the Risse, to which the artefacts seem analogous (L56); early on Kael experiences the artefacts like the Risse (L62).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L39. minor (1–4): functional multiplicity grounded in TSDP, integrating ANPs and EPs (L39).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz durch Negation` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). an occurrence: the title and the two worldview formulas, read on kael and aegis.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). an occurrence: the borrowed theory's name.


**No record entries**: the report touches no conflict or question record.

**No chapter readings**: the report names no chapter.

**Not promoted:** Das Fundament, Fundament Artefacts, Gnosis Protocol, Gnosis, Episteme, pre-gnosis, Earned Revelation, Unearned Intervention, Inner Council, Dance of the Parts, acousmatic harmony, dialetheischer Geist, and the borrowed concepts (one carries a person's name).

**One reader**: every page above.
