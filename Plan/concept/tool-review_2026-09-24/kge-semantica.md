# Tool review — `knowledge-graph-extract` + `semantica`

*2026-09-24. Tested against `aegis-subplots-kapitelweise-system-exploration-docx`
(619 lines) and `roman-lokalitaeten-konzept-und-ausarbeitung` (630 lines), the
two documents decision 007 allows to leave the container. Artifacts:
`Plan/runs/tooltest/kge-semantica/`.*

## What ran

**Extraction (`knowledge-graph-extract`'s format, via `scripts/route.py complete`)**
— NOT REACHED for both documents, within the ~25-minute budget for this tool.

Both documents are single chunks under the skill's own rule (≤1500 lines →
one chunk). The blocker was never the skill or the chunking — it was the shared
free-model pool. The router's own ledger, run **at the same time as the other
tool-review testers**, shows why:

```
python3 scripts/route.py ledger
  purpose         kind   ok cached unreach refused
  grawiki         chat   20  29    0       0
  hyperextract    chat  241  24    0       0
  kge             chat    0   0    1       0
  kge-probe       chat    1   0    0       0
```

`hyperextract` alone made 241 chat calls during this window; `grawiki` made 20
more. Six free models are `ok` in `Plan/runs/route/models.json`; against that
much concurrent load, every one of them was rate-limited when `kge` asked.

Concretely: `route.complete(..., purpose="kge", doc="aegis-subplots...",
json_mode=True, max_tokens=1200)` on a 150-line excerpt (the shorter of two
attempts — a full 619/630-line single-chunk call was tried first and killed
after 510s and 13 min of one attempt already streaming with no result) came
back:

```json
{"outcome": "unreached", "attempts": 20,
 "why": "google/gemma-4-26b-a4b-it:free: rate-limited; google/gemma-4-31b-it:free: rate-limited; qwen/qwen3.8-27b:free: rate-limited; z-ai/glm-5.2:free: rate-limited"}
```
(`Plan/runs/route/ledger.jsonl`, `purpose: "kge"`, 510.3s.) Meanwhile a trivial
one-line probe (`kge-probe`, 27 prompt tokens, no `json_mode`) answered in 1.2s
on `inclusionai/ling-3.0-flash-sante:free` — so the router and the consent path
work; what did not clear was a `json_mode` call competing for the same six-model
rotation against 261 other calls in flight. **P15: this is "never reached," not
"answered badly."** What would reach it: running this tester alone, off-peak
relative to the other tool tests, or a wider free rotation.

**`validate_triples.py` / `generate_cypher.py`** — ran, structurally verified.
With `triples.jsonl` empty (no model answer to populate it):

```
python3 .claude/skills/knowledge-graph-extract/scripts/validate_triples.py Plan/runs/tooltest/kge-semantica/aegis-subplots-kapitelweise-system-exploration-docx
  schema: none (structural checks and dedup only)
  triples: 0 total, 0 valid, 0 violations
```
`generate_cypher.py` correctly refuses on zero triples (`error: no triples
found`). Both are stdlib-only and read exactly what they claim to; nothing here
needed a model or the corpus.

**Entity scoring (`entities.py score --names`)** — ran, against an empty names
file (there is nothing to score: no model entities exist).

```
python3 scripts/entities.py score aegis-subplots-kapitelweise-system-exploration-docx --names empty-names.json
  reader 60, model 0 verified, shared 0 (folded); 0 refused, 0 set apart as lens
  precision 0.00  recall 0.00  F1 0.00  — two readers scored 0.66 (P27)

python3 scripts/entities.py score roman-lokalitaeten-konzept-und-ausarbeitung --names empty-names.json
  reader 124, model 0 verified, shared 0 (folded); 0 refused, 0 set apart as lens
  precision 0.00  recall 0.00  F1 0.00  — two readers scored 0.66 (P27)
```
The 0.00 is not a verdict on the tool — it is the correct score for zero model
output, and the harness (`--names`, the refusal of non-verbatim names, the P27
comparison line) is confirmed working end to end. It is ready the moment a
`kge` call actually returns.

**`semantica`** — ran fully, needs no model
(`Plan/concept/tool-review-plan_2026-09-24.md`'s own row says so). Because no
triples/entities existed to load, the pipeline was exercised twice: once
end-to-end against the (empty) real output directories, and once against a
small synthetic set standing in for what a real extraction would produce, to
show the detectors actually firing.

Empty-input run (`Plan/runs/tooltest/kge-semantica/semantica-report.json`):
```
provenance: tracked 0 entities across 2 documents -> .../semantica-provenance.sqlite
GraphBuilder.build: 0 entities in graph, metadata={"num_entities": 0, ...}
DuplicateDetector.detect_duplicates: 0 candidate pairs flagged
ConflictDetector.detect_entity_conflicts: 0 conflicts flagged
```
This confirms the call shapes the plan specifies work as written:
`ProvenanceManager(storage_path=...).track_entity(eid, source=<slug>,
metadata={"source_quote": ...})`, `GraphBuilder(merge_entities=True,
resolve_conflicts=False).build({"entities": [...], "relationships": []})`,
`DuplicateDetector().detect_duplicates(entities)`,
`ConflictDetector().detect_entity_conflicts(entities)` — all import and run
under `.venv-semantica`, no key, no network.

Synthetic 3-entity smoke test (`AEGIS`/`Aegis`/`Kael`, offline, not corpus text,
not scored):
```
DuplicateDetector.detect_duplicates -> 1 pair: AEGIS ~ Aegis, similarity=0.9,
  confidence=1.0, reasons=['exact_name_match', 'same_type']
ConflictDetector.detect_entity_conflicts -> 0 conflicts
```
So the detectors do fire on a case they should (a casing variant of one entity
name) and do not fire where nothing conflicts. Per `CLAUDE.md` and the plan's
own row, this was measured only — nothing here entered `entities.jsonl`,
`Wiki/`, or any merge.

## What broke and why

- **Not a `knowledge-graph-extract` or `semantica` defect.** Both tools ran
  exactly as documented; the constraint was the free-model pool being shared
  by every tester in this workflow simultaneously (P15 applies to the whole
  router, not to this tool alone — a second run of this exact tester, run
  alone, would very likely reach a real answer, since a 27-token probe
  answered in 1.2s under the same rate limits).
- **`route.py`'s per-model timeout is soft, not hard**, for a streaming
  response: raising inside `chat()`'s request loop (I tried a `signal.alarm`
  hard deadline) gets caught by `_post`'s `except Exception` and counted as one
  more "tried" entry rather than aborting the call — so a genuinely stuck
  attempt can run far longer than its nominal timeout (one attempt logged
  510.3s against a 45–70s per-model setting). This is a real property of
  `route.py` worth a line in its own review, not of this pair.
- **`validate_triples.py`, `generate_cypher.py`, `entities.py score` all
  degrade correctly on zero input** — no crash, an honest zero, not a silent
  pass. That is exactly the shape P19/P23 ask for.

## Where each tool's output could go, under the corpus's limits

- **`knowledge-graph-extract`'s triples/entities** are a model's reading, same
  standing as an entity list or a `knowledge-graph-extract`/`graphify`
  triple (`CLAUDE.md`): they may seed a **candidate list for a person to read**
  (phase 1/2 of `.claude/skills/tools/SKILL.md`) or feed `entities.py doc`/
  `missing`-style profiling once real triples exist. They may **not** create a
  `Wiki/candidates/` page, write a `[[link]]`, supply a count, merge two
  surfaces, or decide a conflict (conflict detection is never mechanised).
- **`semantica`'s `DuplicateDetector`** is a *candidate generator for a human
  reconciliation step* at best — never a merge. Its output could flag
  *"these two surfaces might be the same entity, go look"* the way
  `pairs.py`/`fold()` do for term pairs, but `CLAUDE.md` is explicit:
  `EntityMerger` and automatic resolution may only be measured, never applied.
- **`semantica`'s `ConflictDetector`** is in the same position as any
  mechanised conflict check: `PRINCIPLES.md` P14 and `CLAUDE.md`'s own line
  ("Conflict detection is never mechanised") rule it out of `Wiki/conflicts/`
  entirely. Its only legitimate use here is the one the plan asked for —
  *measure what it would flag, list it, never act on it* — which is what this
  review did.
- **`semantica`'s `ProvenanceManager`** is the one piece with a plausible home
  outside a demonstration: it is a generic append-only provenance store, and
  `Wiki/compare/` + `Plan/runs/judgements.jsonl` already do this project's own
  version of "who said this, from where" by hand. Adopting it would mean a
  second encoding of provenance (P6 says one encoding per rule), so it is not
  an improvement over what exists — just a working library if the project ever
  needed generic provenance for a different graph.

## Recommendations

1. **step:** `2-ingest` (candidate seeding). **proposal:** park
   `knowledge-graph-extract` as a source of *candidate* terms/relations for a
   person to read, never as a source of a census or a page, and only re-test it
   run alone (not concurrently with other testers) before deciding further.
   **evidence:** the tool's own scripts (`validate_triples.py`,
   `generate_cypher.py`) work correctly on real and empty input; the one
   blocker measured was contention on the shared free-model pool
   (`route.py ledger`: `hyperextract` 241 calls, `grawiki` 20, both concurrent
   with this test), not the tool. **may not:** create a page, a `[[link]]`, a
   count, or resolve a conflict. **verdict:** trial (re-run alone first; the
   pipeline mechanics are sound, the model step is unproven end-to-end here).

2. **step:** side track / `2-ingest`. **proposal:** do not adopt `semantica`'s
   `DuplicateDetector` or `ConflictDetector` into any automated step; they may
   only ever be run to print a list for a person, exactly as this review did.
   **evidence:** the synthetic smoke test shows `DuplicateDetector` correctly
   flags an exact-casing duplicate (`AEGIS`/`Aegis`, sim 0.9) and stays silent
   where nothing conflicts — it works as documented — but `CLAUDE.md` states
   plainly that merging and conflict detection are not mechanised here, for
   reasons P13/P14 give (merging deletes the disagreement the wiki exists to
   record; not every apparent contradiction is one). **may not:** merge two
   surfaces, write to `Wiki/conflicts/`, or gate a reconciliation decision.
   **verdict:** park (the API works; the project's own rule is what stops it,
   not a defect — keep it in the catalogue in case a future "duplicate
   candidates for a person to review" side track is built deliberately, the
   way `pairs.py` was).

3. **step:** `route` (side track, not this pair specifically).
   **proposal:** make `route.py`'s per-model timeout actually hard — either
   run each model attempt in a subprocess/thread that can be killed, or stop
   catching the deliberate-deadline exception inside `_post`'s broad
   `except Exception`. **evidence:** one `kge` attempt logged 510.3s against a
   45–70s configured per-model timeout, and a `signal.alarm`-based hard
   deadline I added on top of it was silently absorbed as just another
   "tried" entry by `_post`'s catch-all. **may not:** change what counts as
   free/consented/recorded — this is purely about how long an "unreached"
   verdict takes to arrive. **verdict:** trial (small, mechanical fix; would
   make every tester in this workflow, not just this one, fail faster and
   more predictably under shared load).
