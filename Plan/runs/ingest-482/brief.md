# Brief — readings from document 482 (step 6)

1 document, one reader, one batch: `ingest-482`. Files go to `Plan/runs/ingest-482/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 482 | `report-reorienting-the-central-conflict-as-a-call-to-wholene` | 2025-11-03 | „the Call-to-Wholeness report“ (an unsigned English report, „Reorienting the Central Conflict as a ‚Call to Wholeness‘“) | recasts the central conflict as Kael's internal reintegration, Juna/V as Kael's exiled core, the Moonshine-Link grounded in borrowed physics and philosophy, and the climax as four causal steps; it calls itself a global directive (L5), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (64 lines for `report-reorienting-the-central`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A directive that revises an earlier conception (its own table, L17–L18): write „the Call-to-Wholeness report redefines …“ or „directs …“; never a fact of the story. L34 names a philosopher and carries a physicist-named bridge; L54 a logician-named figure — never quote a span containing a person's name. Quote the English as written; cut before bold, escaped asterisks and inner quotes. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „her“ and „his“).

## Pages — document 482, `report-reorienting-the-central-conflict-as-a-call-to-wholene`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L34, L41, L48, L54, L55, L57. minor (1–4): AEGIS ontologically blind to the quantum-level link, perceiving it as uncorrelated system noise (L41); AEGIS's brittle, fragmented logic against Kael's healed state (L48); the paradoxical collapse into algorithmic melancholy (L55).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L7. minor (1–4): the report redefines Juna/V from a separate, external entity (previous conception) to the primary exiled part of Kael's original self, the Exilant exiled during the Genesis-Krise (L18 — describe around the bold); the leakage of Juna/V's pain as the Herold (L24); Juna/V as catalyst providing gnosis, not a savior (L42); the homecoming of Juna/V (L53). The table states its own revision of the earlier conception: record both sides as the report gives them.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L5, L9, L11, L18, L22, L24, … (19 lines). central (4–8): the plot reframed as Kael's internal Call to Wholeness, to reintegrate a lost part (L22); the Herold as the leakage of Juna/V's pain through Kael's system (L24); Kael's Manager parts as authors of an unreliable narrative, creating Gedächtnislücken (L25); the quest for reintegration of the exiled Juna/V (L26); the climax: functional multiplicity integrating ANPs and EPs, Juna/V's homecoming (L53); embodying the 6 Paraiyas (L54 — never quote the name); victory on the four thematic axes (L57).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L5. not read: an occurrence — the title.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L30, L32, L34, L41. minor (1–4): the Moonshine-Link grounded as a non-local, sub-protocollar connection (L34 — quote only spans without names); inherent and unbreakable, a consequence of the separation from the Ursprungs-Ich (L40); invisible to AEGIS, the perfect narrative exploit (L41).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). an occurrence: `Genesis-Krise` names when Juna/V was exiled, read on juna.
- `juna`: `Juna/V` (near `juna`), `leakage of Juna/V's pain` (near `juna`). a reading: `Juna/V` and the leakage of Juna/V's pain, read on juna.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.


**Record entries:** none.

**No chapter readings**: the report names no chapter.

**Not promoted:** Call to Wholeness, Exilant, Herold, Manager, Gedächtnislücken, Ursprungs-Ich, The Foundation, functional multiplicity, Paraiyas, algorithmic melancholy, Victory Through Wholeness, Paradoxical Collapse, the four axes' terms, and the borrowed concepts (several carry a person's name).

**One reader**: every page above.
