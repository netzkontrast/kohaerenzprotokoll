# Rules as the project: derive once, adapt the code, file the exceptions

*2026-09-17. Three asks in one — stop re-reading every document, let the rules be
worked out by the work rather than designed up front, and let whoever works a step
change that step's code the way an RLM changes its own.*

They turn out to be the same structure.

## 1 · Derive once

The documents are immutable: `Sources/drive/**` is write-denied and every
manifest row carries a `sha256`. So a derived fact stays true until either the
document changes — it will not — or **the rule that produced it changes**, which
happens constantly.

That makes the cache key `(sha256, rule version)` and the invalidation exact.

```
scripts/rules/*.py        one file per rule — the project's learned structure
scripts/derive.py         runner: caches, invalidates, honours exceptions
Plan/derived/<slug>.json  the cache, keyed per rule
Plan/rules/exceptions.jsonl   document × rule × reason
```

Measured over 409 documents and three rules:

| | |
|---|--:|
| cold, nothing cached | 1,227 derivations, **2.0s** |
| warm, nothing changed | 0 derivations, **0.4s** |
| one rule's `VERSION` bumped | **409** re-run, 818 reused |
| a corpus term question | **no document opened** |

The third row is the one that matters. Adding a rule runs only the new rule;
changing a rule re-runs only that rule. Nothing ever re-reads a document to
answer a question that was already answered.

## 2 · The rules are the project, and they are written by doing the work

A rule is deliberately small:

```python
NAME    = "structure"
VERSION = 1
def applies(doc) -> bool
def derive(doc) -> dict
```

That is the whole contract, because **the unit an agent working a step changes is
a rule.** The three that exist were not designed; each field in them is there
because a document had it and a reader needed it — the heading count because one
category has a median of 2 and another 23, the zero-width-space count because one
document had 100 of them inside its formulas.

Which structures matter, and how contents relate, is not knowable in advance.
`scripts/rules/` is the residue of finding out. **On another corpus the directory
starts empty**, and that is what makes the method transferable rather than the
rules.

## 3 · A document that does not fit gets an exception, not a special case

`applies()` is the rule's own opinion about scope. An **exception** runs the other
way: a person saying *this rule must not run on that document, and here is why.*

```json
{"document": "kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md",
 "rule": "surfaces",
 "reason": "a glossary: every line is a term, so the surface index would return
            the whole document as vocabulary and drown every count",
 "revisit": "when corpus.py can weight a hit by how term-dense its document is"}
```

It is honoured, and **reported on every run.** A rule that quietly skips what it
cannot handle teaches nobody anything; one with an exception filed against it is a
question someone can come back to — which is why the record carries a `revisit`
condition and not just a reason.

## 4 · What it found within minutes of existing

**`Kael` wears 95 surfaces across the corpus. `Kohärenz` wears 73.** The
inflection and compound problem that four documents kept surfacing one instance at
a time, answered corpus-wide in 0.6 seconds without opening a file.

And a page is probably misnamed:

| term | documents | occurrences | dates |
|---|--:|--:|---|
| `Kael-Julia-Bindung` — **what the page is called** | **1** | 16 | 2025-04-19 only |
| `Kael-Juna-Verbindung` | 9 | 31 | 2025-04-23 … 2026-06-10 |
| `Kael-Juna-Phänomen` | 6 | 78 | 2025-05-10 … 2025-08-05 |

The page is named after **the one document that happened to be read.** Recorded as
judgement `J13` with the rule it produced: *before naming a page from a read
sample, ask the corpus what it calls the thing.*

This is the first time the corpus has corrected the wiki rather than the other way
round, and it cost no reading at all.

## 5 · Two views of a count, and they must never be confused

The index counts a compound as **one** token: `Kael-Julia-Bindung` does not add to
`Kael`. A `\bKael\b` regex over raw text counts the head inside every compound —
**293 documents against the index's 287.**

Neither is wrong. They answer different questions, and the danger is quoting them
as the same fact. So `corpus.py` says which path it used on every answer, and
`corpus.py family <head>` turns the difference into the useful thing: the
surfaces a term actually wears.

Recorded as judgement `J12`, replayable.

## What this does not do

- **A rule is still code a person writes.** An agent adapting a step means editing
  `scripts/rules/`, bumping a VERSION and re-running — not a model composing a
  query at runtime. That is deliberate: every derivation stays replayable, and
  `scripts/judgements.py` can check the rules against the decisions that produced
  them. The cost is that an unanticipated question needs a new rule.
- **The index holds capitalised tokens only.** Lowercase words and phrases fall
  back to reading, and `corpus.py` says so rather than returning a confidently
  empty answer.
- **`Plan/derived/` is git-ignored.** It came to **14MB** across 409 files, which
  is too much to carry for something rebuilt in two seconds. The rules are the
  record; the cache is not. Anyone cloning runs `scripts/derive.py` once.
