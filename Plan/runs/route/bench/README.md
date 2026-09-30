# Free OpenRouter models on `ask` packs — 2026-09-30

On the author's „Search for the best openrouter free Model — and pin the repo to this — also add a
List with the top 5 free Models — you can run 10 openrouter Trials in Parallel … (Max 50 calls)".

`scripts/route_bench.py` ran it. There were three rounds, 10 in parallel, and **49 model calls**.
Nine of them were replayed from `route.py`'s recording after the first round crashed in the
scorer, and those cost nothing. The rows are in `runs-2026-09-30.jsonl`; the crashed first round
is `round1-crashed-2026-09-30.jsonl`.

## Candidates

OpenRouter lists 16 free models today. Six of them take `data_collection: deny`, which
decision 007 requires:
- ling-3.0-flash-sante;
- gemma-4-26b;
- gemma-4-31b;
- dots-3-note-preview;
- north-mini-code;
- qwen3.8-27b.

The Nvidia, Poolside and Liquid models refuse that policy. The Inkling models are forbidden. The
Nex models, ling-fin and GLM are no longer listed.

## Packs

Every candidate answered the same three stored packs, pinned to itself (P16). Each pack is about
60,000 characters:
- `5d414114`: Juna, first direct appearance;
- `00fcbf0d`: Genesis;
- `a1253825`: Moonshine-Link.

## Ranking (`report`)

| # | model | usable | answered | score | precision | ref_hit | German | quotations on no line | s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | `inclusionai/ling-3.0-flash-sante:free` | **0.731** | **9/9** | 0.731 | 0.926 | 0.276 | 1.0 | 3 | 18.9 |
| 2 | `google/gemma-4-26b-a4b-it:free` | 0.415 | 3/6 | 0.830 | 1.0 | 0.433 | 1.0 | 0 | 73.6 |
| 3 | `dots-studio/dots-3-note-preview:free` | 0.401 | 5/9 | 0.722 | 0.95 | 0.191 | 0.667 | 1 | 28.4 |
| 4 | `cohere/north-mini-code:free` | 0.256 | 3/6 | 0.512 | 0.667 | 0.153 | 0.333 | 1 | 59.9 |
| 5 | `google/gemma-4-31b-it:free` | 0.138 | 1/6 | 0.831 | 1.0 | 0.438 | 1.0 | 0 | — |
| – | `qwen/qwen3.8-27b:free` | 0 | 0/4 | — | — | — | — | — | — |

`best.json` holds ranks 1 to 5. `route.rotation()` tries them first in that order, and
`ask.py --backend route` prefers rank 1.

## How to read it

- **`usable` is score × answer rate.** A free model's shared pool can refuse for minutes at a time.
  Qwen was rate-limited on all four calls, the Gemmas on most, with up to 23 attempts in 240 s. A
  pinned default has to answer first. Ling answered 9 of 9 in about 19 s.
- **`ref_hit` is agreement with Sonnet, not correctness.** It is the share of the lines Sonnet's
  landed answer placed that a model's placed claims reached. Rule 10 applies: what Sonnet did not
  cite is not wrong.
- **The Gemmas scored best when they answered**: precision 1.0, and the highest `ref_hit`. But
  three and one answers out of six are not a measurement a pin can rest on. If they stop being
  rate-limited, run this again.
- **Quotations on no line** are discarded by `verify` either way. Of the five in round 1, one was
  a real fabrication: north-mini translated a German line into English and presented it as a
  quotation. The four others were splices: two passages joined with „…", table cells stitched
  together, one quotation filed under the wrong document. Each lowers precision, and none vetoes
  the ranking (`route_bench.py`'s docstring has why).
- **German:** Rule 4 of the card asks for `says` in German. Ling and the Gemmas kept it every
  time, dots two answers in three, north-mini one in three.
- **The `s` column** averages the seconds of answered calls. A row replayed from the recording
  took 0.1 s, so for gemma-4-31b, whose one answer was replayed, the number says nothing and is
  left out.

Three packs and at most three repeats are a small sample. The ranking is a measurement of one day
at noon, and a rerun can replace it.
