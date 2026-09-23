# Entity lists — one per source document, written by a model

Each `<slug>.md` here is **one model's reading of one document**: the 50-100
entities it judged most important, most central first, each citing the file line
it was found on. The names are Claude Haiku 4.5's, one reader per document and
blind to every other document, by the `entity-lists` workflow; **the lines are
code's.** Since revision 3 the reader writes names only, to `names/<slug>.json`,
and `python3 scripts/entities.py place <slug> names/<slug>.json` writes the list:
each name at its first whole-word line, and every name the document does not
contain word for word dropped and listed on the file's `refused:` line.

**They are proposals, not a census.** A census (`Sources/terms/`) is exhaustive
and written by a person; a gold candidate list (`Plan/runs/<slug>/03-candidates.md`)
is written by a reader before any count. Nothing here may become either.

What they are for is being searched:

```bash
python3 scripts/entities.py verify            # does every cited line hold its entity?
python3 scripts/entities.py matrix            # every verified entity × every landed document
python3 scripts/entities.py missing           # used widely, no wiki page (P10's MISSING)
python3 scripts/entities.py doc <slug>        # which known entities one document uses
python3 scripts/entities.py search <entity>   # where, how often, first line
python3 scripts/entities.py score <slug>      # against a reader's list, where one exists
```

Three rules hold for everything derived from them:

- **A number comes from the search, never from a list.** A list says a model
  thought an entity mattered in one document; how often and where it occurs is
  counted.
- **A list whose cited lines mostly fail is a reconstruction** and `verify`
  reports it as one; `matrix` leaves it out.
- **The order is a model's judgement** of importance, kept as `rank` and never
  presented as a measurement.

Why these lists exist, and what they may and may not decide:
`Plan/concept/entity-lists_2026-09-23.md`.

```yaml
Plan/entities: provisional
# may not: seed a census, create a page, supply a count, or merge two surfaces
# retire when: missing/doc/search show nothing corpus.py and qmd did not already
```
