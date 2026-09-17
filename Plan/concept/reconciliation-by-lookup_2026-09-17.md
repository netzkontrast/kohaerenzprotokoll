# Keeping reconciliation cheap: the wiki as a variable, not as a prompt

*2026-09-17. The problem is that reconciliation grows with the wiki, and the
wiki is the part that must keep growing.*

## The cost, stated plainly

Reconciling one document against the wiki **by reading the wiki** costs context
proportional to the wiki. At 32 pages that is affordable. At 400 it is the entire
budget, and every document after that is more expensive than the one before —
which is the definition of a step that does not scale.

Reading the pages is also the wrong instrument. Most of what a reconciliation
decides is not a reading question at all.

## The borrowed idea

**Recursive language models** — many small calls over a *recursive definition of
code-based evaluation*, where the full context is never handed to the model as a
prompt. The data sits in a code environment as a **variable**, and the model
writes expressions against it. What enters a context is the *result* of a query,
not the corpus.

Applied here:

| | |
|---|---|
| the variable | `Wiki/index.json`, derived from page frontmatter |
| the query layer | `scripts/reconcile.py` — folded surface lookup, containment, intra-list pairs |
| what reaches a reader | **a handful of rows**: the items no lookup settles |
| what is never loaded | **any page body** |

So the cost per document becomes `O(census) + O(judgement bucket)` instead of
`O(wiki)`. The census is bounded by one document. The judgement bucket is bounded
by how ambiguous that document is — **not by how large the wiki has become.**

## What is decidable by lookup, and what is not

Three of the four things a reconciliation produces are lookups:

| outcome | how it is decided |
|---|---|
| **already there** | the candidate matches a page this document is already recorded on |
| **new reading** | it matches a page this document has not contributed to |
| **new term** | it matches no known surface |

The fourth is not, and the split is the whole design:

| **needs judgement** | it *nearly* matches — a fold away, a containment, a shared stem — and whether that is one term or two is what no lookup settles |

**And one thing is deliberately not attempted: whether a new reading conflicts
with one already on the page.** Two readings can only be compared by reading
them. A program that guessed would produce exactly the false conflict a
shared-string detector produces — `Zero-Trust` as an AEGIS sub-function against
`Zero-Trust-Architektur` as the external standard, which is a naming relation and
not a disagreement.

## Measured, on document 4 against 32 pages

```
19 candidates — 12 decided by lookup, 7 need judgement
```

The seven are the right seven: five are article-prefixed duplicates **inside the
document's own candidate list** (`Die Konstrukt-Stadt` beside `Konstrukt-Stadt`),
and two are compounds that fold near `kohaerenz` — `Kohärenz-Programm`, the
system's name, and „Das Seelen-Kohärenz-Protokoll", the project's. Neither is the
abstract property the page is about, and **only reading settles that.**

### The first version scored better and was wrong

Without intra-list detection it reported **21 of 23 decided**, because
`Die Konstrukt-Stadt` and `Konstrukt-Stadt` both came back as new terms — it would
have silently created two pages for one world, and no later reconciliation would
ever have noticed.

Adding the check **lowered the score and raised the truth.** A pre-classifier is
measured by what it sends to judgement correctly, never by how little it sends.

### And an index blind spot caused a real miss

`Hüter` was classified as a new term. It is German for Guardian and the
`guardians` page exists — but that page carries no `aliases`, so the index cannot
see the connection.

`scripts/wiki_index.py --check` lists **20 gaps of exactly this kind** and the
reconciler prints a line pointing at it. The check was written before the miss and
predicted it, which is the argument for having it.

## Where the recursion goes next

Only the judgement bucket is expensive, and it is expensive **per item, not per
wiki**. So it recurses naturally:

- an item names one or two pages
- a reader — a person now, a small model later — opens **those pages only**
- it returns one line: same term, or two terms, and why

That is many small evaluations over a large structure, none of which sees the
structure. The unit of work stops being "the wiki" and becomes "this pair".

**None of that is worth building yet.** What matters is that the shape now allows
it: the expensive part is isolated, bounded and countable, and
`reconcile-pre.json` records how many items it contained for each document.

## What this does not fix

- **The census still reads one whole document.** That is bounded and it is where
  the judgement belongs.
- **The index is derived from frontmatter, so pages must carry their surfaces.**
  Eleven of 32 do. The other 21 are the gaps, listed rather than assumed away.
- **`fold()` is not a stemmer**, deliberately. `Kern-Welten` and `Kern-Welt` fold
  together; `Negentropie` and `Entropie` do not. A stemmer aggressive enough for
  German inflection also merges a term with its negation.
