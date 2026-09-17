# An independent design for this exact problem, and where it disagrees

**Source:** `dspy-wiki-compile` in `netzkontrast/dspy-agent-skills`, installed
2026-09-17. Its one-line scope is this project's: *compile immutable sources
into an LLM-maintained wiki — extract claims with line-range citations, decide
per existing page between flag / update / create, print a knowledge diff.*

It was written without reference to this repository. That makes the overlap
worth something and the disagreements worth more.

## Where it agrees, having been built separately

| its rule | here |
|---|---|
| „Sources are never modified" | `Sources/drive/**` is write-denied; `sources.py` is the only writer |
| „Drafts go to a candidates area. Promotion is a human step" | `Wiki/candidates/`, 46 pages, nothing promoted, `Wiki/terms/` does not exist |
| „The diff is the receipt" — print reinforced / challenged / new / gaps before writing | `Wiki/compare/reconcile-NN-*.md`, per document, append-only |
| „Health before lint" — free structural checks before spending tokens | `derive.py` caches by `(sha256, VERSION)`; `reconcile.py` answers by lookup |
| „challenged must map to a conflict" | decision 003 — a conflict gets its own record and the page stops |

Five rules, arrived at twice. That is the strongest evidence this repository has
that its shape is not arbitrary.

## The number that matters

Its metric weights six axes. **The heaviest, at 0.30, is `citations resolve`** —
higher than merge quality, higher than diff consistency. Its named failure is
`citation does not resolve: file:start-end 'quote'`.

`scripts/quotes.py` was written the same day, before this skill was read, and
does exactly that. **It reports 17 unresolved.**

So an independent design says the thing this repository currently fails is the
single most important axis. The 17 are not cleanup to get to eventually; on this
reading they are the highest-value open item in the wiki. `NOW.md` lists them.

## Where it disagrees, and why we keep ours

**„Extract everything before merging anything."** A two-phase batch compile: a
concept in three sources becomes one draft with three sources, not three drafts.

This repository does the opposite on purpose, because it was asked for:
*„jedes einzelne Dokument vollständig im Wiki erfasst — jedes neue Dokument muss
dann nur gegen das Wiki abgeglichen werden, statt überhaupt nicht zu skalieren."*

Both are right about different corpora. Batch gives a better first wiki and
costs `O(n²)` in comparisons; per-document gives a worse first wiki and costs
`O(census) + O(judgement)` forever. With 409 files and 357 documents, batch is
not affordable and per-document is the only one that finishes.

**Kept, not adopted** — and the cost is real: the first three documents each
produced a full re-comparison that superseded the last, which is what the
per-document order was introduced to stop.

## The gap it names that we do not have

**„A reviewed page is authoritative. Conflicting content is `flag`ged with the
conflicts listed; `update` is only for additions without dispute. The metric
scores a protected update at 0."**

This repository has **no such rule**, because it has no reviewed pages — nothing
has been promoted, so the case has never come up. It will on the first promotion,
and the question is not small: when a new source contradicts a page a person has
signed off, the source cannot silently win and the page cannot silently win.

The skill's answer — *flag, list the conflicts, never update in place* — is
compatible with decision 003 and stronger than it, because 003 governs conflicts
between sources and says nothing about a conflict between a source and a human
judgement.

**Not adopted yet. Recorded so the first promotion does not have to invent it.**

## What this does not change

The skill is a DSPy program and this pipeline has no LM in it. Every step here is
deterministic Python or a person. Adopting its *rules* costs nothing; adopting
its *implementation* would mean putting a model where there is currently a
measurement, and none of the findings above argue for that.

`dspy-local-runtime` removes the practical blocker — `claude -p` answers here
with no API key, verified — so the choice is now a design decision rather than an
environment limit. It stays no.
