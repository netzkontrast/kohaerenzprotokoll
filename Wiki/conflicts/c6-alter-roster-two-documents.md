---
id: C6
subject: Kael's Alter/Anteil roster — two complete, disjoint name sets
kind: two complete rosters for one system, no name in common
status: open
first_seen: "2026-09-17"
sources: 2
pages: ["alters", "kael"]
---

# C6 — two documents name Kael's inner system, and share no name

**Append-only.** This record decides nothing, and neither document that
supplies it has been changed by the other.

## The positions

| # | roster | size | source | ingested |
|--:|---|--:|---|---|
| 1 | `Limina`, `Nox`, `Echo`, `Flicker`, `Eos`, `Oblivion`, `Praetor`, `Index`, `Silas` (+ `Kael` as Host) | 10 | `charakterkonzepte-fuer-kohaerenz-protokoll` | reconciled |
| 2 | `Selene`, `Nyx`, `Kiko`, `Lia`, `Isabelle`, `Moros`, `Alex`, `Rhys`, `Lex`, `Argus` (+ `Kael` as the system) | 11 | `strukturelle-dissoziation-system-kael-analyse` | **not reconciled** |

## The measurement

Word-boundary occurrence count, both directions, over the landed text of each
document:

- Every name in roster 1 occurs **0** times in
  `strukturelle-dissoziation-system-kael-analyse`.
- Every name in roster 2 occurs **0** times in
  `charakterkonzepte-fuer-kohaerenz-protokoll`.

Two apparent hits before the word-boundary check — `Lia`/`Lex` as substrings
of `Julia`/`komplex` and similar — were false positives and are excluded.
`Kael` is the one name both documents use, and he is the host/system, not an
Alter/Anteil in either roster.

**This is the same shape as `C5`**: a complete set for one thing in one
document, a complete and different set for the same thing in another, zero
overlap. It is the fourth and largest instance of the pattern this corpus's
Alter rosters keep producing — see [[alters]] and
`Wiki/questions/q3-how-many-kern-welten-and-alters.md`, where three earlier
rosters (from `roman-lokalitaeten-konzept-und-ausarbeitung`,
`kohaerenz-protokoll-konzept`, and this document) already shared no names with
each other before this fourth, unreconciled one is even counted in.

## Why it is not simply a naming difference

Nothing here suggests the same nine or ten [[alters|Alters]] wearing different names.
Both documents propose full, independent ten/eleven-item structures for the
same one psyche, with their own role-types and their own hedges — this
document's `Nox`/`Persecutor` and `Praetor`/`Protector` do not obviously map to
anything named `Selene` or `Moros`, because neither document offers a
cross-reference and no third source has yet named both.

## What this is not

**Not resolved here, and not resolved by reconciling
`strukturelle-dissoziation-system-kael-analyse`.** That document is censused
and noted but not yet reconciled against the wiki — its own reconciliation is
the next document in `account.py order`, is a separate person's-call, and this
record does not pre-empt it. Raising the conflict is this reconciliation's
job; choosing which roster the novel keeps, if either, is not.

See `Plan/runs/judgements.jsonl` J83 for the one specific near-miss checked
directly: `Nyx` (roster 2) against `Nox` (roster 1), one letter apart and
zero-occurrence in both directions — `fold()` correctly keeps them apart.

## What would settle it

- A source that uses names from both rosters in one sentence.
- A source that states these are successive drafts of the same nine-or-so
  Alters, naming the correspondence rather than leaving it to be inferred from
  role-type alone.
- `strukturelle-dissoziation-system-kael-analyse`'s own reconciliation, which
  may surface a rule this record cannot mechanise.

## Not to be confused with

`C5`, the `Möglichkeits-Garten` scale conflict — the same "two complete sets,
zero overlap" shape, applied to locations rather than to Alters, and the first
conflict of that shape in the wiki.
