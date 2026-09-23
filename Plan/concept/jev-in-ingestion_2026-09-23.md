# Where Jev could help ingestion, and where it may not

*2026-09-23. Nothing here is built. The SDK is installed in `.venv-typesafe`,
one call has been made with TypeSafe's own example text, and no project data has
been sent anywhere. This is the reasoning to check before the first real call.*

## What Jev is, in this project's terms

TypeSafe's System One model, `jev-latest`, takes a `state` and a map of typed
questions, and returns **probabilities, not text**. The three question types are:
`noul` (probability of yes), `choice` (one of a set, with a distribution) and
`score` (position on ordered levels, with a distribution). One request answers
all its questions in parallel. The one measured call took 0.6s and 414 input
tokens.

So Jev cannot write a census, a note, a quotation or a page. It can only **rank,
route and flag**. That makes it a better fit for this project than a generator,
because generating is what the principles forbid, but only in places where a
ranked or flagged answer goes to a person and never into the record.

## The rule that decides every placement

Each proposed use has to pass the same three questions from `PRINCIPLES.md`:

1. **Does its answer become part of the record, or only direct attention?** A
   number, a page, a link or a conflict is record. A reading order or a queue
   order is attention. Jev may only direct attention. A search result never
   becomes a number, and a Jev probability is a search result with better manners.
2. **Is there a labelled set to measure it against before it is trusted?** (P3,
   P16, P17, P27.) No use is adopted on a demo.
3. **Can it run offline?** (P5.) Every call is recorded to a fixture on first run
   and replayed from it after, so the check runs free, with no key.

## Where it does not go

These follow directly from rules already here. They are listed so that nobody
has to argue them again.

| step | why not |
|---|---|
| `03-candidates.md` | Gold is a person's reading. A model list is `03-candidates-rlm.md` at best, and Jev cannot enumerate anyway. |
| conflict detection | Never mechanised. Two readings are compared by reading them. `Zero-Trust` is the standing counter-example. |
| creating a page | A page from an occurrence says nothing. Jev saying "this passage defines X" is still an occurrence until a person reads it. |
| `[[links]]` | A link is never inferred. A guessed edge looks like a stated one once it is in the graph. |
| any count in prose | `state.py` measures. A probability summed over documents is a guess shaped like a number. |
| deciding a near match | `judgements.jsonl` records a person's decision and the rule in words. A model decision has no rule to replay. |

## Where it could go, in order of evidence available

### 1 · A second opinion on the near-match ledger — measurable today

`Plan/runs/judgements.jsonl` already holds 36 decisions a person made as
`one-term` or `two-terms`. That is a labelled set that exists before the tool
does, which no other placement has. One `noul` per pair: *do `a` and `b` name
the same concept?*

What it would tell us: whether Jev reads German morphology (plurals, inflection,
compounds, `AEGIS`/`Rest-AEGIS`). `NOW.md` names exactly those as where `fold()`
misses. It says the next improvement is **a rule, not a model**, and this does not
change that. Jev would be scored against the ledger the same way `fold()` is, as
a baseline to compare the rule against. It would not replace the rule.

What it may not do: become `mechanised_by`. The ledger's value is a rule stated
in words that code can replay. A Jev probability is not a rule, and a replay of it
is only a cache.

Why start here: the smallest data exposure of anything on this page (two
surface forms per call, no document text), a gold set that already exists, and
one afternoon of work.

### 2 · Choosing the next document — where the value is

`NOW.md` says the next document is not chosen and lists what the wiki asks for
in its own words: Q1 wants the Guardian/AEGIS relation stated **outside a
question**, C5 wants a garden placed inside a named Kern-Welt, Q3 wants the alter
count, `nexus` wants `Nexus`, `Überraum` and `Nexus-Interface` related.

Today that choice is made with qmd, and qmd is known to fail at it. BM25 favours
short, early chunks, and the line that defines `KW1` is not in its top forty for
`Kernwelt`. Q1's condition, *stated as an assertion and not as a question*, is
not something any lexical ranker can express.

That condition is exactly what a `noul` can express:

    state:    one passage, with its slug and line range
    question: "Does this passage assert how Guardians relate to AEGIS,
               rather than asking about it or proposing it?"

The shape would be: qmd `search` finds a wide candidate set of passages
(cheap), Jev reranks them against each open question's own condition, and
**a person reads the top few and chooses**. What goes into the record is the
choice, and the reading that follows it, and nothing Jev returned.

How to measure before trusting it: the six documents already ingested are the
labels. `NOW.md` notes that every `Wiki/questions/` page and conflict record
already says „a search finds this in `<slug>`". Hide that, rerank, and see where the known passage lands. That is
recall@k on a fixture that exists, and it is the same fixture `NOW.md` already
proposes for `qmd bench`, so the two can be compared on one table.

### 3 · Flagging stance per passage — useful, and the most dangerous

Decision 004: stance is read, per passage, and a single document holds several.
Document 5 was a brief, with 163 hedging words and 32 of 91 question marks in the
field closest to assertion, and it added zero pages on purpose. Knowing that
before reading is the point of `01-profile.txt`.

A `choice` per section, `asserts / proposes / asks / analyses another text`,
could sit beside the profile as a **provisional, clearly-labelled guess** at
where the hedging is.

The danger is the one decision 004 was written against: the profile is
*measured*, and a stance label next to it would look measured. So if this is
built it goes in its own file, `02b-stance-jev.txt`, never in `01-profile.txt`.
It is read *after* the reading, as a comparison, until it has been scored against
a person's stance marks on at least the six ingested documents. Carried with
the demotion lines:

```yaml
stance_jev: provisional
# may not: appear in the profile, gate a page, or be read before the document
# retire when: it disagrees with the reader's marks as often as two readers do
```

### 4 · Triage for the 17 unresolved quotations — probably not

`read.py --find` already names the nearest line by string. Jev could name the
nearest line by meaning, which is what the 11 "words the document does not
contain" cases need. But `NOW.md` is explicit that the tempting fix is the trap,
because repointing a number can make a citation resolve and the page wrong. A
second, semantic "nearest line" is one more tempting answer. Kept here only so it
is not re-proposed without that sentence.

## What has to be decided before any of it — by a person (P0)

**Whether corpus text may leave the repository at all.** Every use above except
the first sends passages of unpublished research for the novel to a third-party
API. The first sends only term surfaces. When this session tried to send the 36
ledger pairs, the environment's permission check stopped it as data leaving the
repository, and that was the right call to escalate rather than work around.
This is an author decision, not an engineering one.

## Cost, measured once

One call: 414 input tokens, 73 output, 0.6s, for three questions over one
sentence. A passage-level rerank for one open question over 40 qmd hits is 40
calls, or one call with 40 `noul` questions over a structured state. Which one
TypeSafe's limits allow is in their docs and has not been checked.

## If it is built

- one script, `scripts/jev.py`, standard library plus the SDK from
  `.venv-typesafe`, shelling out the way `sources.py` does to `.venv-tools`
- every request and response written to `Plan/runs/jev/` so it replays offline
  (P5) and can be inspected (`--trace` from the catalogue)
- repeats with no cache when measuring (P18)
- `TYPESAFE_API_KEY` from the environment only, never in a file in this repo
