# RLM, thought through again — what was transferred and what was left

*2026-09-17. Framed with the `/ideate` skill's structure — five generation paths,
a banlist, a filter, grounded writing. Its tooling belongs to another repository
(`tools/research_wiki.py`, Semantic Scholar, DeepXiv, a review LLM) and none of it
exists here, so the shape is borrowed and the content is this project's.*

## The mistake in the first transfer

RLM's idea: the corpus is never a prompt. It lives in a code environment as a
variable, the model writes expressions against it, and **only results enter a
context.**

Applied last round to `Wiki/` — 32 pages. Left untouched: `Sources/` — **409
documents, 2,460,498 words, of which 4 have been read.** One percent.

The idea was applied to the small thing and withheld from the large one.

And the evidence that it belonged on the large one was already in the session.
The two sharpest corrections both came from querying all 409:

- the renaming is a **cliff on one day**, not a drift — six documents on
  2025-04-17 carry Michael/Julia and zero carry Kael/Juna; seven on 04-18 the
  reverse, with no document mixing them on either day. This refuted a conclusion
  drawn from three documents.
- `Partnerin` appears in 23 documents and **17 of them also carry `Juna` or
  `Julia`** — refuting the conclusion, drawn from four documents, that the corpus
  never links them.

**Both were heredocs. Neither was a step. Neither survived.**

## The banlist

Rejected earlier in this work, and not to be re-proposed:

| rejected | why |
|---|---|
| subagent fan-out to move document bytes | moves the context leak, does not remove it |
| full re-comparison of all censuses per document | `O(n²)`; each comparison superseded the last |
| merging readings on a term page | destroys which source said what — the wiki's only job |
| mechanising conflict detection | reproduces the `Zero-Trust` false conflict |
| a fixed enum of document kinds | format does not follow from purpose (decision 004) |

## The ideas, by generation path

**A — landscape-driven. A corpus query layer.** *Built.* `scripts/corpus.py`:
`count`, `timeline`, `cooccur`, `first`, `where` over all 409, returning counts,
dates, categories and slugs — **never document text.** The two findings above are
now one command each.

**B — incremental. Make the matching mode explicit.** *Built, and it was needed.*
The first version counted substrings. `Julia` matches **33 documents as a
substring and 27 as a word** — the difference is `Julian`, `Julias`. A count that
does not say which it is cannot be compared with another count, and both get
quoted as the same fact. Whole-word is now the default and every answer names its
mode.

**C — combination. `corpus` × `index`.** A term page could cite corpus-wide
evidence — *this term appears in 207 documents across 11 categories, first on
2025-04-17* — without any of them being read. Not built; it is the obvious next
step and it needs a page format decision first.

**D — innovation. Break the assumption that a document is the unit of work.**
RLM suggests the unit could be a *query*: reconcile per term across all documents
rather than per document across all terms. **Rejected, and the reason is the
architecture:** a term-first pass reads many documents through one lens, which is
exactly the contamination the census exists to prevent. The unit stays the
document. Recorded so it is not re-proposed.

**E — cross-domain transfer. Recursion for a term at corpus scale.** „What does
the corpus say about AEGIS?" → 226 documents. Too many to read; that is precisely
the RLM case — map a cheap call over each, return one line, merge. **Not built,
and not yet needed**, because nothing is asking corpus-scale questions of a term
yet. The shape now permits it: `corpus.py where AEGIS` returns the document list
without the documents.

## What building it found immediately

**26 of the 409 landed documents have no frontmatter at all.** They are the first
batch, landed before the decision to add it, and nothing back-filled them.

`Sources/README.md` said *every* landed document opens with eight lines of
provenance. False for 26.

Worse, it is not cosmetic: **every ad-hoc count in this session used
`lines[9:]`**, which silently swallowed nine lines of content in those 26
documents. That is where `Julia` came back as 26 documents in one count and 27 in
another — not rounding, a systematic error in the cheaper method.

`scripts/profile.py` already found the boundary per document rather than assuming
it, deliberately. The heredocs did not, and nothing compared them until a tool
existed that did it the careful way every time.

**So the case for making a query a step rather than a heredoc is not tidiness.**
A heredoc encodes an assumption once and nobody audits it; a tool encodes it once
and everyone inherits the audit. `corpus.py` now prints the frontmatter gap on
every answer.

## What is still not transferred

- **The root writing its own queries.** `reconcile.py` and `corpus.py` are fixed
  programs, not code a model composes per question. That is a deliberate
  trade — deterministic and replayable against `judgements.jsonl` — and it is
  also the limit: a question nobody anticipated needs a new subcommand.
- **Experience recall.** 11 judgements exist in the right shape; nothing retrieves
  by similarity yet. Worth building at perhaps 50.
- **Compaction.** Not needed at 11 judgements and 32 pages. Named so it is not
  rediscovered.
