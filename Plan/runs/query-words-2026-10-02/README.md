# One query-word function, step 5 of SPEC.md — 2026-10-02

Before this step, three lexical finders split a question into search words three ways, with three stop lists:

| finder | words | minimum length | stop list |
|---|---|---|---|
| `askdb.fts_query` (the `bm25-lines` finder of `ask`, and `bm25rel`) | `\w[\w-]*`, case kept | 3 | 45 words |
| `kg.search` | `\w+` | 1 | none |
| novelgraph `Index.bm25` | `[^\W_]\w*`, lowercased | 2 | 120 words (`lex.STOP`) |

`ask.skills_for` filtered a fourth way. Now all four ask `askdb.query_words(text, min_len=2)`:
- tokens are `[^\W_][\w-]*`, so a hyphenated name stays whole;
- lowercased, in order, each once;
- the one stop list is the union of the old ones plus `do`, `does` and `did`;
- two characters are enough, which keeps the corpus' short names (KI, K0, KW).

novelgraph keeps `lex.STOP` for what it *indexes* (surfaces, lemmata); changing it would change the index without
changing its stamp.

## What changed per question — `words.py`, `words.json`

`words.py` holds the three old builders verbatim and prints, for each of the 24 frozen questions, the words each old
builder asked and what `query_words` adds or drops.

- **`ask`'s finder:** 11 questions unchanged. 14 function words dropped (`not`, `does`, `has`, `that`, `they`, `with`,
  …) and 3 numbers added (`33`, `36`, `38`, chapter numbers the 3-character minimum lost).
- **`kg.search`:** loses 107 function words and single letters. Hyphenated names stay whole (`kern-welten`,
  `moonshine-link`).
- **novelgraph:** 17 unchanged. Hyphenated names are whole and `who` is dropped.

## Measured, offline, on the frozen cases

- **`ask.py bench`** (72 000 bytes): **0.303 / 0.101 → 0.324 / 0.113** (document / line recall). Six cases change;
  none loses document recall. C11 loses line recall (0.159 → 0.148) while gaining documents (0.366 → 0.561).
  English function words in an OR query had been ranking lines by `not` and `does`. The run is
  `Plan/runs/ask/bench-2026-10-02-72000-3ddf659c.json`.
- **novelgraph recall@8**, `heading@v1` (`novelgraph_recall.py`, `novelgraph_recall.json`):

  | search | document recall | cases better / worse |
  |---|---|---|
  | BM25 | 0.066 → 0.062 | 4 / 3 |
  | vector | unchanged, as it must be | — |
  | hybrid | 0.068 → 0.069 | 2 / 2 |

  All of this is within the noise of 24 dependent cases.

The gold is circular (evaluation audit §0): these numbers say the change loses nothing the bench can see. They do not
say it discovers more.
