# `Wiki/questions/` — a question that many pages ask, answered in one place

**This page type was deferred on purpose and has now earned its existence.**
`Plan/concept/wiki-system-plan_2026-09-16.md` wrote it down as a condition:

> No synthesis or question pages yet. Both were near-unused. **They earn their
> existence when a real need appears**, not before.

Source: [the earlier wiki plan](../../Plan/concept/wiki-system-plan_2026-09-16.md).

The need is measured rather than argued. `python3 scripts/relations.py --open`
harvests the `## Open` section of every term page; on 2026-09-17, when this type
was created, it found:

| | |
|---|--:|
| open statements across the wiki | **70** |
| distinct after folding repeats | **46** |
| statements that repeat another | **24** |
| pages carrying *`AEGIS` does not occur here* | **11** |

Eleven pages ask one question. Answering it would mean editing eleven pages, and
nothing would say they were the same question. That is the need.

The harvest has grown with the wiki: 128 <!--state:wiki.open_statements-->
open statements today, and 5 <!--state:wiki.questions--> question pages
promoted from them.

## What a question page is

A question that **more than one term page raises**, with the pages that raise it,
what would answer it, and nothing else. It is three things at once:

- **the single place an answer lands**, instead of eleven edits,
- **the work queue** — what a next document would have to say to be worth reading,
- **the evaluation set** — *can the wiki answer this yet?* is a question you can
  ask a program, and these are already written, attributed and in German-source
  terms.

## What it is not

**Not a conflict.** A conflict is two sources saying incompatible things and is a
property of a term — `Wiki/conflicts/`, decision 003. A question is *no* source
saying anything. C4 and Q1 are the same subject from the two sides: the conflict
records that two documents disagree about where the blind spot lives; the
question records that nothing read says how the Guardians relate to AEGIS.

**Not a copy of the term page's `## Open` section.** Those stay. They are that
source's honest record of what it did not settle, and they are the harvest this
type is derived from. A question page is promoted from them when the same
question appears twice.

## Promotion

A harvested statement is a **candidate**, the way a term is. Most are not
questions — `Everything except the role.` is prose, not something a document
could answer. Promotion is a person's call and the bar is:

1. it recurs on **two or more** pages, or a source names it as needing definition;
2. it states **what would answer it**, so it can be closed rather than argued;
3. it is answerable from the corpus in principle — not a question for the author.

## Frontmatter

```yaml
id: Q1
question: <one sentence, in the form a document could answer>
status: open | answered
raised_by: [<term page slugs>]          # the recurrence — the reason it exists
documents: [<source slugs that raised it>]
answered_by: <source slug>              # only when status is answered
conflict: C4                            # when a conflict covers the same subject; several: C6, C9
gathered: "2026-09-17"                  # when the page was written
```
