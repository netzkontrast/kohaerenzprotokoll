# Wiki — what the sources say, attributed and unmerged

One page per term. A page collects **every source's reading of that term**, each
with its source, its date, and the kind of document it came from. Where the
sources disagree, the page says so and stops.

**A term page never decides which reading is right.** That is the author's call.
A page that merged its readings would destroy the only thing it is for: which
source says what, and when.

## Layout

| path | what | who writes it |
|---|---|---|
| `candidates/` | gathered from notes, not yet reviewed | gathered by hand, for now |
| `terms/` | promoted by a person | a person |

`terms/` does not exist yet. Nothing is promoted until enough candidates exist to
show what promotion should check.

## Why a reading carries its stance

A page that recorded only "what this source says about X" would present a
refutation as a definition, or a document's own premise as its conclusion. So
every reading says what kind of statement it is.

**Stance belongs to a passage, not to a document** (decision 004). The documents
themselves say so: one of the three read labels its passages 38 times, with six
different labels — eight of them *describing* the thing it goes on to reject.
Another marks 26 passages as premises quoted back from its commission. A single
label per file could only ever record the loudest one.

| a reading is | when |
|---|---|
| a **premise** | the source is stating what was already believed — often marked, e.g. `[User Query]` |
| a **verdict** | the source is judging the term, not defining it |
| a **finding** | the source concluded it |
| a **restatement** | the source is reproducing someone else's claim, not making one |
| **asked** | it appears only inside a question, and is no reading at all |

There is **no fixed list of document types.** How a document came to be says
nothing about how it is built — three documents in one category, five days apart,
had 0, 34 and 24 headings.

## Dates are load-bearing

The corpus supersedes its own names, and not all at once. One document says
*Michael* and *Julia*, a later one *Kael* and *Julia*, current canon *Kael* and
*Juna*. Without the date, a reading under an old name looks like a claim about
someone else.

The same applies to terms: `AEGIS` is expanded three incompatible ways within
two days, and `Entropie` carries three senses in the same window.

## A page can have zero readings

`readings: 0` is a real state and five pages carry it. A term that a source only
*asks about*, or uses once as already known, has **no reading in that source** —
and a page that recorded the question as a reading would turn the project's
uncertainty into its position.

Those pages exist anyway, because the alternative is worse: a term nobody wrote
down leaves no hole, and the gap becomes invisible rather than open.

## What is here

**24 pages and 2 conflicts**, from **2 of the 4 documents with a census.** The
wiki is built one document at a time: a frozen census is reconciled against the
current pages, and the record of each reconciliation is in `Wiki/compare/`.

| document | date | new terms | new readings | new surfaces | new conflicts |
|---|---|--:|--:|--:|--:|
| `entropie-aegis` | 2025-04-17 | 14 | 13 | — | 0 |
| `aegis-emergenz-aus-der-leere` | 2025-04-19 | 10 | 2 | 1 | **2** |

Both conflicts sit on terms the two documents **share**. Nothing they do not
share produced one.

## Conflicts

`Wiki/conflicts/` holds one record per disagreement, **append-only**, pointed at
from every page it touches. A record states that sources disagree, names at least
two with a cited position each, and stops.

| id | subject | positions | sources |
|---|---|--:|--:|
| `C1` | AEGIS is expanded incompatibly | 3 | 2 |
| `C2` | Entropie means two incompatible things | 2 | 2 |

About twenty pages get written by hand before any schema is written down. The
schema follows the pages; the pages do not follow a schema.
