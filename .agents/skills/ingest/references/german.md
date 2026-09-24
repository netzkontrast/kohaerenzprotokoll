# German, and the matching it defeats

Every item here was found by doing the work, not by planning it. They are the
reason a census cannot be produced by a pattern, and the reason the candidate
list is written by a reader before anything counts.

## Capitalisation carries no information

German capitalises **every** noun. So a pattern over capitalised tokens finds
sentence starts, ordinary nouns and nothing distinguishing — and misses the
inflected and lower-case surfaces a term actually wears in running text.

`scripts/corpus.py` holding capitalised tokens only is a defect in it, not a
design. Treat any capitalisation-based shortcut as a source of both false
positives and false negatives at once.

## Inflection splits a term from itself

The same term appears as `Kern-Welt`, `Kern-Welten`, `der Kern-Welt`,
`Kern-Welten-` inside a compound. A count that does not say which surface it
counted answers a different question each time it runs.

`capture.py --count` therefore reports every term **twice** — standing alone,
and including compounds — and lists the inflected surfaces it found.
**A term at `0 word` is written differently in this document, not absent.**

Eight of the 24 labelled pairs `fold()` misses are plurals or inflections
(2026-09-24); the rest are slashes, renames, modifiers and abbreviations.
Decision 010 set the reach of a plural rule for the eight — a scored rule in
`pairs.py`, which reconciliation does not use — so the morphology question is
narrower, and not closed: whether `fold()` adopts that rule is the author's
(`NOW.md`).

## The German definite article is never a term boundary

`Die Konstrukt-Stadt` and `Konstrukt-Stadt` are one term. `fold()` strips a
leading `der`/`die`/`das` before comparing, and the judgements ledger records
that as a rule in words rather than as a special case in code.

`fold()` is a comparison key, not a stemmer. It strips the article, case,
diacritics and punctuation, and it does nothing about plurals.

## Umlauts expand, and the encoding decides whether they do

Slugs expand `ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`. Drive titles arrive with the umlaut
sometimes composed (NFC) and sometimes decomposed (NFD), and a decomposed `ä`
survives an ASCII fold as a bare `a` — which is how `singularität` became
`singularitat` in a first pass of the dedupe. **Normalise to NFC before folding**,
never after.

## The substring trap, four times now

Two terms sharing a substring are not the same term, and a short string is a
substring of far too much:

- `Riss` inside `Rissbildung-Protokoll`
- `Kern-Welt` inside `Kern-Programm`
- an empty or punctuation-only fragment is a substring of **everything**, so a
  matcher that normalises a quote down to nothing will resolve it against any
  line at all

Match whole terms. Guard a minimum comparable length — `reconcile.py` uses
`SHORTEST_COMPARABLE = 4` — and apply it everywhere a comparison happens, not
just in the function where the bug was first seen. It has appeared in
`near_matches`, in `intra_list_pairs`, and in a quote normaliser.

## Word boundaries need more than `\b`

`V` occurs 7 times as a name and 198 times as a letter inside other words.
`\b` does not help because the surrounding characters are word characters.
`capture.py` uses `(?<![\w-])term(?![\w-])` and reports the bounded and unbounded
counts side by side, because which one is right depends on the term.

## Export damage that is not a defect

The converter escapes `\[`, `\"`, `\*`, `\_`; markdown emphasis wraps words the
source did not emphasise; a blockquote adds `> `; footnote numbers are glued to
the word they annotate; inline attribution markers like `[User Query]` are
inserted. None of these is a wrong quotation, and a checker that does not undo
them reports false failures.

The scale is measured: the predecessor's uncalibrated checker reported **46
citation-resolution errors that reduced to 6 genuinely wrong out of 150
claims** — 19 fixed by unifying quote glyphs, 21 by stripping enclosing
punctuation. **An uncalibrated quote checker reported a model as five to eight
times worse than it was.** `quotes.normalise` is where this is handled, and it is
shared with `read.py --find` so both sides agree.

## Language detection needs an escape hatch

A `de`/`en` detector run over this corpus penalises names, numbers and formulas,
which belong to neither. A `language_unknown` outcome is required, or the check
reports damage where there is none.

## And what no rule settles

- **Whether a descriptor is a term.** `Kontrollinstanz` appears three times and
  never without AEGIS beside it. Recorded as a descriptor. Only reading decides.
- **Whether an imported term has become project vocabulary.** `Negentropie` is
  information theory in one document and a property of the Kael–Julia bond in
  another. Somewhere between those it stopped being a citation.
- **Whether two surfaces are one term**, where no article or inflection rule
  reaches — `Multiplizität` against `funktionale Multiplizität`.
- **Whether a candidate is a term at all**, as against a word the author used
  twice.
