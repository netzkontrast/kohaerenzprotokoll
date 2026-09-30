# The `ask` card, before and after today's learnings — Haiku subagents, 2026-09-30

On the author's „use Haiku subagents to test your improvements".

**Design.** The three stored packs, Juna `5d414114`, Genesis `00fcbf0d` and Moonshine
`a1253825`, were repacked with `ask.py repack`: **the same windows, graph and schema, only the
rules card swapped**.
- `.v1` is the card of `07d37d47^`, from before today's learnings.
- `.v2` is the current one: splicing, table cells, the document slug, translation, and
  calibrated `answerable`.

Twelve Haiku subagents answered, 3 packs × 2 cards × 2 repeats, each reading only its pack. The
instruction they got repeats none of the card's rules; before this run it did, which would have
given v1 the new rules. `route_bench.py sessions` scored every answer with `ask.verify` and
`ask.score`. The reference is Sonnet's placed lines, which is agreement, not gold. The rows are in
`rows.jsonl`.

| card | scored | score | precision | ref_hit | quotations on no line | German `says` | words per quotation | `answerable` on Juna (C7 disagrees) |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| v1 | 6/6 | 0.782 | 0.958 | 0.371 | 2 | 0.833 | 13.6 | `yes`, `yes` |
| v2 | 6/6 | 0.788 | 0.964 | 0.377 | 2 | **1.0** | 11.8 | **`partly`, `partly`** |

**What the card changed:**
- **The language rule works.** One v1 answer wrote English `says`; no v2 answer did.
- **The calibration works.** Both v1 answers on Juna said `yes`, although C7 records that the
  sources disagree there. Both v2 answers said `partly`.
- Quotations got shorter, closer to the 5–25 words the card asks for.
- On placement it changed nothing measurable: score and precision are equal within noise over six
  answers each. Haiku joined nothing with „…" under either card, so the splice rule had nothing to
  prevent here.

**What the run found in the pipeline**, fixed in code and applied to both arms alike:
1. **Umlaut spellings of slugs.** The corpus names documents both `koharenz-…` and `kohaerenz-…`,
   and Haiku „corrected" the spelling. The quotation then counted as outside the pack, although
   its words stood on a line the pack sent. `ask.resolve_doc` now maps a slug to the one pack
   document it names in the other spelling, and records `doc_as_written`. It never picks between
   two, and never reaches outside the pack. Three quotations were recovered.
2. **German quotation marks in JSON.** One v1 subagent closed „Systemfehler" with a straight `"`,
   which ends the JSON string, and its whole answer did not parse. `ask.loads_lenient` retries
   once with „…" closed by “. That answer now scores.

Six answers per card are a small sample, and the score difference is noise. The card is kept for
the two behaviours it demonstrably changed.
