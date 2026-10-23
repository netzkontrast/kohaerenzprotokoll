---
name: digest
description: Read one wiki candidate page whole — every line it cites, opened with its context, plus the project's records and the other wiki pages that name the term — and write a German thought page (Wiki/terms/<slug>.md, form gedanken) holding every thought about the term once, with all its sources and stances, and a ledger proving every citation was accounted for. Use when asked to fully read, digest or prepare a term for promotion; never to decide a reading, merge readings or enter canon.
allowed-tools: Bash(python3 scripts/*), Bash(git:*)
---

# The full read of one term page

The plan and its reasons: `Plan/concept/term-digest_2026-10-23.md`. The author's answers of 2026-10-23: the
full read comes **before** promotion and its thought page is what the author reviews; one word of the author's
promotes the candidate and approves the page; up to two Sonnet readers (`term-digester`) may read chunks; the
session groups, writes and commits. The script is `scripts/digest.py`; run `selftest` once before a run.

```
digest.py plan <slug>              packet.json: every distinct citation, its window, barred lines, chunks
   │
   ▼ digest.py show <slug> NN       a reader per chunk (and one for `records`): chunks/NN.ledger.jsonl + NN.thoughts.jsonl
   ▼ defects                        each fixed on the candidate first, one commit naming its source document
   ▼ group                          the session: thoughts.jsonl (`from` names the chunk thoughts), groupings.jsonl
   ▼ digest.py join <slug>          ledger.jsonl, chunk ids mapped to final ids
   ▼ digest.py write <slug>         Wiki/terms/<slug>.md
   ▼ digest.py check <slug> · quotes.py · terms.py check
   ▼ commit „terms/<slug>: full read of the candidate as of <date>, <n> citations“
```

## 1 · A thought

One statement about the term that a source makes, written once in German, with every source that makes it:
`ref` (`doc.md:Lnn`), `stance` (`asserts`, `proposes`, `questions`, `rejects`, `reports`) and, where the words
matter, a `quote` taken from the line with `python3 scripts/read.py <doc> --find "…"` — never typed. Its `kind`
is its section: `definition`, `function`, `mechanism`, `origin`, `evolution`, `relation`, `differ`, `prose`,
`open`, plus `kurz` and `decided` for the session. Its `tag`: `S` a source says it; `K` the author decided it
(`links` names the decision, an answered Weiche, `kanon.md` or a decided conflict); `V` a proposal; `L` a gap;
`D` derived by the writer (`refs` names the thoughts, or `links` a file).

**Grouping is a judgement.** Two sources give one thought only where their cited lines state the same thing;
each keeps its own `ref` and `stance`. A source that hedges what another asserts is the same thought with a
different stance; a source that says something else is another thought, and the two name each other in
`differs_from` and get a `differ` thought saying how they differ. Every thought joining two or more documents
gets a row in `groupings.jsonl`: `{"thought", "docs", "why"}`.

## 2 · The ledger — what makes „every thought“ checkable

Every distinct citation of the candidate, and every record and wiki line in the packet, gets exactly one row:
`used` (with `thoughts`), `same-as` (with `note`: which ref says it), `context`, `occurrence`, `barred`,
`defect` (with `note`: what the reading claims and the line does not). `digest.py check` refuses a reference
without a row, a `used` row naming no thought, a thought citing a barred line, a joining thought without its
grouping, a page that is not the rendering of the run.

## 3 · The refusals that are not code

- **Never write or quote** an early name, a name the corpus gives after „ehem.“, a real person's name, the trauma
  symbol or a world code's expansion; never cite a line that holds one. `show` prints such a line as `[gesperrt]`;
  its reference is `barred`.
- **No gendered pronoun** for Kael, Juna, AEGIS or any part, also inside a quotation chosen for a thought.
- **No canon by the side door.** A source calling itself canon is `[S]` with stance `asserts`; only the author's
  decision linked is `[K]`.
- **No merge.** When unsure whether two lines say the same thing, keep two thoughts.
- **A defect is fixed on the candidate first**, as a commit naming the source document whose reading changed; on a
  reviewed part of a promoted candidate it is a question to the author with the fix proposed (decision 026).

## 4 · After the read

Record the numbers in `Plan/learnings/digest.md`: minutes and citations per chunk, thoughts per citation, rows per
state, defects, groupings. The author's review: `promote.py sheet <slug>` plus `digest.py status <slug>`; on the
author's words, `promote.py apply` and `terms.py approve` with the same words (one act).

## Provisional

```yaml
name: digest            # provisional — written 2026-10-23 before the first full read
# may not: decide which reading is right, merge readings, create a conflict record without the session's
#          reconciliation rule (decision 003), approve or promote anything
# retire when: three full reads show the author reviews by source rather than by thought
```
