# Brief — readings from document 558 (step 6)

1 document, one reader, one batch: `ingest-558`. Files go to `Plan/runs/ingest-558/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 558 | `dialetheismus-im-kohaerenz-protokoll` | 2025-04-21 | „the dialetheism report“ | a report applying dialetheism and paraconsistent logic to AEGIS and the four core worlds, with two open hypotheses and recommendations; proposals, never canon|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (408 lines for `dialetheismus-im-kohaerenz-pro`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report: write „the dialetheism report proposes …“; its hypotheses stay hypotheses. **Never cite** L15, L21, L178, L182, L189, L191, L192, L209, L219, L268, L282, L307, L309, L313, L317 (earlier names). Quote no gendered pronoun.

## Pages — document 558, `dialetheismus-im-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L21, L26, L173, L175, … (41 lines). central: two hypotheses, A dialetheic (L177) and B anti-dialetheic (L187); a potentially tragic figure under B (L193); the core directive (L197); a hybrid recommended (L270).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L240. not read: `Emergenz` in its general sense (L240).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L243. not read: only in a heading (L243).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L15. not read: the surface on L15 is an earlier name.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kael` alone on L15. minor: the upgrade to version 1.5 (L204); Kael's data as a logical virus under B (L206).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L11, L15, L21, L27, L82, L211, … (14 lines); `Kernwelt` L11, L15, L21, L27, L55, L82, … (17 lines). central: four core worlds differentiated by their stance on contradiction (L213), KW1–KW4 headings (L215, L222, L229, L236).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: L11 is the title.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L178, L182, L189, L268. not read: every line that names it also holds an earlier name.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L185, L192, L193, L220, L267, L281. minor: cracks as a state both present and repaired (L183); resilience despite cracks under A (L185); glitches and cracks in KW1 (L220).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title phrase.


**Record entries:** none.

**Not promoted:** Hypothese A/B, the core directive, LP and every logic term, the logic table of the core worlds, EST.

**One reader**: every page above.
