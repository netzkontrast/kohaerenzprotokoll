# 005 — A link is `[[slug]]`, a term in backticks is not a link

**Date:** 2026-09-17 · **Decided by:** the author, against a claim of mine that was wrong · **Status:** chosen, applied

## What was chosen

Two marks, two meanings, and they stop being the same mark:

| written | means |
|---|---|
| `` `Nexus` `` | the term, named |
| `[[nexus]]` | the link, set |
| `[[nexus\|Nexus-Vorstufe]]` | the link, set, with the prose left exactly as it read |

`scripts/relations.py` derives the graph from `[[…]]` and from nothing else, and
reports a `[[…]]` pointing at no page as a **broken link** rather than silently
dropping it. `scripts/link.py` performed the one-pass migration and stays, so the
same pass can close the gap again after new pages are written.

## Why — and the claim this corrects

**The author's sentence was: „ein Wiki ohne Links ist kein Wiki."** It was aimed
at a statement of mine that was wrong twice over.

I had written that `Wiki/` contains zero `[[links]]` and treated that as a
decision against linking. Measured:

- there were **48 links**, written `` `slug` `` — „no `[[…]]`" is a fact about
  markup and says nothing about whether pages link
- what `Legacy/Plan/wiki/repo-survey_2026-09-15.md` rejected was a model
  **inferring** edges, and it says in the same line that canon links must be
  **explicit**

Turning „do not let a model guess an edge" into „the wiki has no links" is the
delete-instead-of-demote failure `CLAUDE.md` names, and it cost a
recommendation: it is how the broken-link lint family got dismissed as having
nothing to check.

**It had plenty to check.** 21 of 46 pages had nothing linking to them, and
`relations.py --unmarked` found **158** places where one page wrote another
page's term in prose and left it unmarked — more than three times the marked
links. `aegis`, the corpus's most central term, was an orphan with its name
standing unmarked in other pages **68 times.**

A page that reads as connected and measures as an orphan is a markup problem.

## What the migration was not allowed to do

Rewriting prose in a repository whose quotations are checked against source
lines is how a citation silently stops resolving. So the pass runs only in
linkable prose and masks out the frontmatter, fenced code, inline code, anything
inside „…", an existing link, and **every line carrying a `^[` citation,
entirely** — a line that cites is evidence and is not edited to make a graph look
better.

**The first run broke two quotations anyway.** The quote mask was line-bounded
and German quotations wrap, so `[[logos]]` landed inside a „…" on two pages.
`quotes.py` went 17 → 19 and named both. The mask is multi-line now, the pass was
redone from a clean tree, and `quotes.py` is back at 17 — unchanged, which is the
proof the second run was safe.

That is the whole argument for having built `quotes.py` before this, and it is
worth recording that the check earned its keep on the first change that could
have used it.

## Result

| | before | after |
|---|--:|--:|
| links | 48 | **133** |
| orphans | 21 | **16** |
| isolated pages | 12 | **9** |
| unmarked mentions | 158 | **56** |
| unresolved quotations | 17 | **17** |

The 56 that remain are mentions whose first occurrence sits inside a quotation,
a citation line or a heading — places the pass may not touch. They are a
measurement, not a backlog.

## What was rejected

**Staying with `` `slug` ``.** No migration, and 48 working links. But a mention
and a link stay indistinguishable, so every term written in code font counts as
an edge and the graph cannot tell a cross-reference from a word.

**`[[…]]` for new pages only.** Two conventions forever, which is the kind of
half-decision this repository has already paid for once.

**Inferring links with a model.** Not reopened, and not what this is. Every one
of the 133 links marks a term the prose already wrote; no edge was invented, and
`relations.py` still says so in its own output.

## What would change our mind

**Orphans that are the finding rather than the flaw.** 15 of the 16 remaining
orphans are mentioned nowhere at all — and `ani`, `ars`, `ecr`, `pms`, `rsa`,
`snk` and `nullpunkt-protokoll` are exactly what `Q2` asks about: seven terms one
document introduced and did nothing but evaluate. Their isolation *is* the
answer. If a future check reported orphans as uniform damage it would be
destroying that signal, so `--unmarked` separates „mentioned and unmarked" from
„mentioned nowhere" and says which is which.
