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
python3 scripts/entities.py score <slug>      # against the document's list, where scripts/gold.py rules it gold
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
`Plan/concept/entity-lists_2026-09-23.md`. Today 5 <!--state:entities.lists-->
lists exist and 4 <!--state:entities.readings--> of them verify as readings;
`NOW.md` has the numbers per list.

## The German–English map

`bilingual.md` (and `bilingual.jsonl`, the same rows for code) pairs German and
English surfaces of one entity across the whole corpus, written by
`scripts/bilingual.py`: code finds the pairs the corpus writes itself, free
models propose counterparts from a name alone, and Jev judges each pair over the
lines where both occur. Every stage is cached under `Plan/runs/bilingual/`, so
`--replay` reruns it with no key and no network. It is a list of proposals: no
pair has become a judgement, and `graphrag.py ask --gloss` uses one only to
route a question, labelled as a gloss.

```yaml
Plan/entities: provisional
# may not: seed a census, create a page, supply a count, or merge two surfaces
# retire when: missing/doc/search show nothing corpus.py and qmd did not already
```
