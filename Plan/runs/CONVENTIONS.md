# Run artifacts — JSON conventions

Every step of every document writes a JSON file beside its human-readable
counterpart. **There is no fixed schema yet, and there deliberately will not be
one until enough documents exist to show what the fields need to be** — P4: no
structure without instances.

What there *is* is a small set of requirements, so that whatever gets written can
be read programmatically later without a migration.

## Required on every object

| field | value |
|---|---|
| `document` | the slug, exactly as in the manifest |
| `drive_id` | copied from the manifest, **never typed** |
| `step` | `profile` · `probes` · `candidates` · `counts` · `census` · `reconcile` · `verify` |
| `at` | ISO date |
| `by` | `scripts/capture.py` · `scripts/profile.py` · `hand` |

Everything else is free. A step that learns it needs a field adds it; nothing
breaks, because nothing reads a field it does not know about yet.

## Two rules about the free part

**1. A number in a JSON file is a count, not a judgement.** If a value required
reading to produce, it says so — `"by": "hand"` — so a later analysis can
separate what a program measured from what a person decided. Mixing them silently
is how a corpus-wide claim gets built on four judgements.

**2. Line numbers are file lines**, counting from line 1 including frontmatter,
exactly as a citation writes them. Body-relative numbers were emitted once and
resolve to the wrong text silently, because both are valid line numbers.

## The one that matters: `reconcile`

This is the object the whole idea rests on — reconciling each new document
against the wiki rather than against every earlier document, so the work stays
linear instead of not scaling at all.

```json
{
  "document": "aegis-emergenz-aus-der-leere",
  "drive_id": "1N3v…",
  "step": "reconcile",
  "at": "2026-09-16",
  "by": "hand",
  "state_before": {"pages": 14, "conflicts": 0},
  "new_terms":     ["rsa", "ecr", "ztv"],
  "new_readings":  [{"page": "aegis", "lines": [17, 126]}],
  "new_surfaces":  [{"surface": "Zero-Trust-Architektur", "page": "aegis-teilfunktionen",
                     "relation": "named-after", "conflict": false}],
  "new_conflicts": [{"id": "C1", "subject": "AEGIS", "pages": ["aegis"]}],
  "state_after":   {"pages": 24, "conflicts": 2},
  "minutes": 24
}
```

**What this buys later.** With one of these per document, the questions that
currently need reading become queries: does *new terms* fall as documents are
added? Does *new readings* hold up? Which pages accumulate the most sources, and
are those the ones that conflict? How much does a category cost on first contact?

None of that is worth building now. **All of it is impossible if the objects are
not written now**, which is the only reason they are.

## What is not JSON

The census, the note, the reconciliation record and the pages stay Markdown. They
are read by people, and the JSON is the part a program reads. Neither is derived
from the other yet; when one can be, that is the moment to say which is the
source.
