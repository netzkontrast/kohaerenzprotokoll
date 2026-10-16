# Session method — read only for the operation in hand

Operational detail moved from CLAUDE.md on 2026-10-13. Startup, authority and model permissions live in CLAUDE.md; these sections cover correcting claims/constructs and wiki commit provenance.

## Changing your mind

Two different things get corrected here, and treating them the same way is how this project has gone wrong in both directions at once.

### A claim is measured, or marked unmeasured

A claim says something is true of the repository or the corpus; it is backed by a count or explicitly marked as not yet counted, and when a measurement contradicts it, it is
simply wrong: change it and leave the correction beside it with how it went wrong. The failure mode is **too slow** — the heading claim was generalised from one document and survived three learnings before anything
counted the other 359. **A search result never becomes a number**: qmd ranks and does not enumerate (`Kernwelt` is in 144 landed documents and a forty-hit list is not a census of that); every number comes from `corpus.py`,
`duplicates.py` or a count, which say what they counted and how.

### A construct is demoted, not deleted

A construct — a field, a category, a name, a folder, a template — is not true or false; it is useful or it is not, and its test is use, not argument. The failure mode is **too fast**:
when `kind: brief | critique | result` drew the objection *don't commit to fixed document types* it was removed outright in the same turn, and the finding that *a result closes a question an earlier brief asked* lost the
distinction it needed. So a construct is never deleted on first objection; it is demoted in place:

```yaml
kind: brief          # provisional — a first-pass guess, not established
                     # may not: explain format, decide how a passage is read
                     # retire when: 20 documents show it predicts nothing
```

**`provisional`** says it is a guess, so nothing downstream leans on it without saying so; **`may not`** is the objection kept, as the reach it loses; **`retire when`** names the evidence that would end it, so the next argument is a
measurement. A construct that has carried a `may not` for twenty documents without once being useful can go, quietly, with no decision file. One that is **actively wrong** — keeping it would make someone assert something false —
leaves with a decision file, and its idea is written down in `PRINCIPLES.md`'s catalogue. **Be quick to measure a claim and slow to remove a construct**: they feel like one virtue and are opposites — a claim that survives
because nobody counted is a lie the repository tells itself, and a construct that dies on first objection takes with it every question it was the only way to ask.


## Committing a wiki page

**Every revision of a page in `Wiki/` is committed immediately, and the commit message names the source document the change came from.** One page changed is one commit, and the first line says which document caused it:

```
aegis: second expansion from aegis-emergenz-aus-der-leere
entropie: schöpferische Matrix from aegis-emergenz-aus-der-leere, conflict C2
guardians: five named bearers from guardians-und-kern-welten-konzept
```

Several pages may share a commit **only when one source document caused all of them in one reconciliation**, and the message still names that document. `git log --oneline Wiki/candidates/aegis.md` is then the page's
provenance, and a wrong reading is removable — every page a misread document touched is one `git log --grep=<slug>` away. **A commit that changes a page without naming a source document is the defect.** Two exceptions,
each naming what it is instead: **a corpus-wide re-measurement** (a landing batch, or `dedupe.py` folding copies away, makes every page that wrote a denominator like „among the 409 landed" wrong; such a commit changes
a number, never a reading), and **the navigation on the chapter pages** — `## What this chapter is about`, `## Questions for this chapter`, `## Candidate sources` and `## Raw qmd answers` are written by
`scripts/chapter_sources.py` from a run in `Plan/runs/qmd-chapters-2026-09-26/`, carry no citation or reading, are replaced whole on every run, and their commit names the run (the raw answers are copied by code into
```` ```qmd ```` fences in `Plan/runs/qmd-chapters-2026-09-26/raw/kap-NN.md`; `quotes.py` skips that info string and no other).

