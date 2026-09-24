# Wiki — what the sources say, attributed and unmerged

One page per term. A page collects **every source's reading of that term**, each
with its source, its date, and the kind of statement it is. Where the sources
disagree, the page says so and stops.

**A term page never decides which reading is right.** That is the author's call.
A page that merged its readings would destroy the only thing it is for: which
source says what, and when.

## Layout

| path | what | who writes it |
|---|---|---|
| `candidates/` | one page per term, gathered from the notes, not yet reviewed | a person, one commit per page naming its source document |
| `conflicts/` | one record per disagreement, append-only | a person |
| `questions/` | one page per question more than one term page raises; its README says when a question earns a page | a person |
| `compare/` | the reconciliation record of each document against the pages as they stood | a person, from `scripts/reconcile.py`'s lookup |
| `index.json` | every page's surfaces and frontmatter, so reconciling never reads the wiki | `scripts/wiki_index.py` |
| `terms/` | promoted pages — **does not exist yet** | a person |

Nothing is promoted until enough candidates exist to show what promotion should
check; the schema follows the pages, not the other way round.

## What is here

**92 <!--state:wiki.pages--> pages, 12 <!--state:wiki.conflicts--> conflicts
and 5 <!--state:wiki.questions--> questions, from
13 <!--state:documents.reconciled--> reconciled documents.** The wiki is built
one document at a time: a frozen census is reconciled against the current
pages, and the record of each reconciliation is in `compare/`. The first three
files there are the full re-comparisons made before reconciling by lookup; each
superseded the last, which is how the step showed it did not scale.
`CLAUDE.md`, *State*, has what each document added and why.

Pages link to each other as `[[slug]]`: 329 <!--state:wiki.relations--> links,
none inferred — each marks a term the prose already wrote (decision 005).
`scripts/graph.py` reads the links, the frontmatter and every citation into a
typed graph, and `scripts/graphrag.py` retrieves attributed quotations from it,
never prose. Every quotation on a page is checked against the line it cites by
`scripts/quotes.py`.

## Why a reading carries its stance

A page that recorded only "what this source says about X" would present a
refutation as a definition, or a document's own premise as its conclusion. So
every reading says what kind of statement it is.

**Stance belongs to a passage, not to a document** (decision 004). The documents
themselves say so: one of the first three read labels its passages 38 times,
with six different labels — eight of them *describing* the thing it goes on to
reject. Another marks 26 passages as premises quoted back from its commission.
A single label per file could only ever record the loudest one.

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
*Michael* and *Julia*, a later one *Kael* and *Julia*, the latest *Kael* and
*Juna* — and the Kapitel-Kompendium states both renames itself. Without the
date, a reading under an old name looks like a claim about someone else.

The same applies to terms: `AEGIS` is expanded three incompatible ways within
two days, and `Entropie` carries three senses in the same window.

**No date settles anything, though.** Every draft is back in question
(decision 006): a newer document, or one that calls itself canon, is recorded
as saying so and never retires an older one.

## A page can have zero readings

`readings: 0` is a real state, and 1 <!--state:wiki.zero_readings--> page
carries it. A term that a source only *asks about*, or uses once as already
known, has **no reading in that source** — and a page that recorded the question
as a reading would turn the project's uncertainty into its position.

Such a page exists anyway, because the alternative is worse: a term nobody
wrote down leaves no hole, and the gap becomes invisible rather than open.

## Conflicts

`conflicts/` holds one record per disagreement, **append-only**, pointed at
from every page it touches (decision 003). A record states that sources
disagree, names at least two with a cited position each, and stops. A resolution
is added beneath the positions, with what settled it; `NOW.md`, *Questions for
the author*, lists every open one.

A record's frontmatter carries `id`, `subject`, `kind` (in its own words, not
from a list), `status` (`open`, or decided by the author with the date),
`first_seen`, `sources` and `pages`. Conflict detection is never mechanised: two
readings are compared by a person, and a program that guessed would reproduce
the `Zero-Trust` false conflict.

A conflict is two sources saying incompatible things. A question, where no
source says anything, lives in `questions/`.
