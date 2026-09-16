# 003 — A conflict is recorded once, by subject, and term pages point at it

**Date:** 2026-09-16 · **Decided by:** Claude, under the author's grant · **Status:** chosen, not yet built

## What was chosen

A disagreement between sources gets **one record**, at
`Wiki/conflicts/<slug>.md`, with a stable id. Every term page whose readings are
involved shows the conflict in full, as `Wiki/candidates/aegis.md` already does,
and names the id.

The record is **append-only**. A conflict moves from open to resolved with the
resolution that settled it and is never deleted or rewritten.

**The record decides nothing.** It states that sources disagree, names at least
two of them with one cited position each, and stops. Resolution is the author's.

## Why

The AEGIS page carries two conflicts. One belongs to AEGIS alone. The other —
emergence from `∅` versus emergence within the simulation — belongs equally to
an `Emergenz` page that does not exist yet. Written on both pages, it becomes
two records of one disagreement, and a later source that settles it will be
checked against whichever copy someone happens to open.

This is not speculative. The retired system's probe run hit it live across four
documents:

> Two pairs are the same argument reached from different concepts —
> `die-13-alter`/`tsdp` on the alter count, `juna`/`moonshine-link` on the
> bond's origin. That duplication is why the ledger is keyed by entity as well
> as by concept.

Two of its seven conflicts were duplicates of each other. Ours is one of two on
the first page written.

Append-only is the second reason, and it is the one that pays late: the record
is *the memory that lets a document arriving in six months be checked against a
clash found today*. A conflict edited in place loses exactly that.

## What was rejected, and why

**Keeping conflicts only on term pages.** Simplest, and it is what page one
does. It fails the moment one conflict touches two terms — which is already
true.

**The retired design: agreement on the page, disagreement only in the ledger.**
Its schema said „the body asserts only what the sources agree on: no
contradictory statement is ever rendered onto a concept page". That is the right
shape for a page used at writing time, where unresolved argument is noise. It is
the wrong shape for this wiki, whose whole purpose is showing which source says
what. The novel rests; the argument is the product. **The conflict stays visible
on the page — the record is in addition, not instead.**

**Letting a source's own claim of authority resolve a conflict.** Explicitly
rejected. The retired pipeline allowed „unless one source explicitly supersedes
the other", and a document asserting that all disagreeing documents are
deprecated was believed — which silently dropped that concept out of the
contested count and the review queue. That document is in our corpus, landed.
**A gather step proposes; it never resolves.** Contested follows from the
presence of a disagreement, never from its resolution.

**A `resolution` field with values like `supersedes` / `both-valid`.** Same
failure in smaller form: as soon as the field exists, something fills it. It can
be added when an author actually resolves something.

## What would change our mind

- **Twenty pages produce fewer than three conflicts, none touching two terms.**
  Then the record is ceremony and the page alone is enough.
- **Conflicts turn out to be overwhelmingly false** — artefacts of wording
  rather than disagreements. The retired pre-registration predicted this
  (`gather-term.md` prediction 2) and the first evidence runs the other way: two
  real, zero false. If that reverses at twenty pages, what is needed first is
  the filter, not the record.

## Not decided here

Whether a conflict record has frontmatter, what fields, and whether the id is a
slug or a number. Twenty pages decide that, per P3. The decision here is that
**one conflict has one home**, not what the file looks like.
