# Entity lists: what a per-document model reading is for, here

*2026-09-23. `scripts/entities.py` and the `entity-lists` workflow exist; a
four-document pilot ran and failed verification; the full run has not happened.*

## The goal they have to serve

The repository builds a wiki of term pages from 346 <!--state:sources.landed--> research documents. A person
reads one document at a time, and six have been read. Two things limit that loop
and neither is reading speed:

- **Choosing the next document.** `NOW.md` names what the wiki asks for (Q1, C5,
  Q3, `nexus`) and a person turns that into a qmd query. qmd ranks; it does not
  enumerate, and it misses — the line defining `KW1` is not in its top forty.
- **Knowing what is missing.** P10's fourth bucket, `MISSING`, is "the one that
  matters" and the one no check computes. The wiki has 56 <!--state:wiki.pages--> pages; nothing says
  which terms 40 documents use that none of them cover.

A corpus-wide list of entities addresses both — **if** it is a list of what the
documents contain, and not of what a model imagined they contain.

## Why a model, and why one per document

`corpus.py` can count any term it is given. What it cannot do is propose the
terms: German capitalises every noun, so a regex for names finds sentence starts,
and "roughly half of what has been found so far is invisible to one" (ingest
skill). Proposing is reading. 346 documents at human speed is the whole project.

One reader per document, blind to the others, for the same reason a census is
blind: a reader who has seen the corpus decides in advance what a document may
say. It also makes each list attributable and re-runnable one document at a time.

## What the model contributes, and what it does not

| the model supplies | the script supplies |
|---|---|
| **which** surfaces are entities in this document | **where** each occurs, in every document |
| **rank** — its judgement of what is central here | **how often** — a count that says how it counted |
| a **kind**, provisional | nothing about kinds |

So a number never comes from a list. A list says one model thought `Nexus`
mattered in one document; `search` says `Nexus` occurs in N documents, M times,
first at this line. The only model-derived signal kept is **rank**, and it is the
one thing `corpus.py` could never give: a document that *mentions* `Nexus` three
times and one that is *about* it look the same to a count.

## What each command answers

- **`missing`** — entities that occur in N+ documents and fold to no wiki surface.
  P10's `MISSING`, measured rather than guessed. It is a list of candidates for a
  person to look at, not a queue of pages to create: a page from an occurrence
  says nothing (ingest skill).
- **`doc <slug>`** — which known entities one document uses, and how widely each
  is used elsewhere. The profile of a document before reading it — for choosing
  it, never for reading it (the census stays blind).
- **`search`** — multi-word entities across line wraps (`Kern-Welt 1`,
  `Cognitive Firewall`), which `corpus.py`'s token index cannot answer.
- **`score`** — a model list against a reader's `03-candidates.md`, as two
  difference lists. That is the P27 measurement: two readers agree at F1 0.66.

## Things they could show that nothing here shows now

Unmeasured, written down so they can be checked when the lists exist:

- **Renames.** Two surfaces with disjoint document sets and adjacent dates —
  `Kael-Julia-Bindung` / `Kael-Juna-Verbindung` (J13), `Wächter` / `Guardian` —
  are exactly what `NOW.md` asks to watch for, and what `corpus.py timeline` can
  then confirm.
- **Variants.** The prompt asks for an abbreviation as its own row right after
  its full form, which proposes pairs for `judgements.jsonl` — to a person.

## What they may not do

- seed a census or a `03-candidates.md` — a model list is what gold scores
- create a page, a link or a conflict
- supply a number
- merge two surfaces — `Kern-Welt` and `Kern-Welten` stay two rows

## The pilot, and what it changed

Four documents, revision 1 of the prompt. 280 of 374 rows cited a line holding
the entity; no list reached 90%. Of the 94 failures, 39 wrote a form the document
never contains, 29 cited the wrong line, 26 were one to three lines off. One
reader stopped at line 1200 of 2498 and reported comprehensive coverage.

Against the two reader lists that exist: `roman-lokalitaeten` F1 0.67 — at the
human ceiling; `aegis-subplots` 0.13 — the model took the document's research
vocabulary (Kybernetik, Spieltheorie) where the reader took its world.

The line failures are P26's defect exactly: a typed identifier. Revision 2 takes
every line from `read.py --find`, which refuses a form the document does not
contain. The second failure — which entities count — is not fixed by a prompt,
and is why `score` exists.
