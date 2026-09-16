# 002 — Normalize source documents on write, mechanically only

**Date:** 2026-09-16 · **Decided by:** Claude, under the author's grant · **Status:** done

## What was chosen

`scripts/sources.py land` normalizes every document as it is written:
CRLF and CR become LF, trailing whitespace is stripped from every line, and the
file ends with exactly one newline. Both checksums are recorded — `sha256_raw`
for what Drive returned, `sha256` for the file on disk.

Three noise classes are deliberately left untouched: the converter's bulk
backslash escaping (333 in the first document, 145 of them `\[`), bold used
where headings belong (21 pseudo-headings against one real heading), and
bibliographies collapsed onto a single 2,408-character line.

## What was rejected, and why

**Normalizing at ingest instead of on write.** Citations into these files are
line ranges, and a citation cannot be stable if the file is not. Every consumer
would also have to redo the same cleanup, which is a second encoding of one rule.

**Normalizing later.** It would change every checksum already recorded, and the
noise is systematic — 673 of 852 lines in the first document — so it is identical
across all 654 remaining.

**Cleaning the three noise classes too.** That is interpretation, not cleanup.
Converting `\[` to `[` can create accidental link syntax. Promoting bold to
headings is a guess about the author's intent, applied to 654 documents at once,
and a silent rewrite at that scale is exactly what the normalization rule exists
to prevent.

## What would change our mind

The bold-as-heading decision has a known cost: section-level retrieval does not
work on a corpus with one heading per document. If the wiki comes to need "the
part of this source that discusses X", the promotion becomes worth doing — and
it stays cheap, because `sha256_raw` lets any document be re-derived from its
original bytes.

## Consequences

`Plan/learnings/fetch.md` §5–§7 carries the measurements. The flat-heading cost
is recorded in `NOW.md` under what is waiting on the author, so it is visible
rather than buried in a tool's docstring.
