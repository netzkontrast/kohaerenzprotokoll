# 027 — Term pages in `Wiki/terms/`, written from a reviewed candidate

**Date:** 2026-10-08 · **Decided by:** the author (that the process and its tools are built), the session (how, provisionally) · **Status:** in use, provisional

## What was asked

> Lass mal den Prozess und die nötigen Tools und Scripte die du brauchst für Wiki terms Pages

The sentence has no verb. The session read it as „build the process, and the tools and scripts it needs, for the pages in
`Wiki/terms/`“, following the first promotion (decision 026) the same day. If something else was meant, the pages and the
script can go; nothing else reads them.

## What was chosen

1. **A term page is a second page for a term, not the candidate moved.** `Wiki/terms/<slug>.md` is written from a candidate the
   author reviewed, in German, every bullet tagged `[K]`/`[V]`/`[S]`/`[L]`/`[D]` with the evidence its tag needs, and it keeps
   what the author decided (`[K]`, linked) apart from what sources say (`[S]`, cited). The candidate stays the ledger of
   readings; decision 026's field stays the review.
2. **The first page by hand** (`kishotenketsu`, a draft), then `scripts/terms.py` around what it needed: `finds`, `scaffold`
   (refuses an unreviewed candidate), `check` (on GitHub), `approve` (refuses without the author's words; the row goes to
   `Plan/runs/promotions.jsonl` with `layer: terms`), and a selftest of 18 cases.
3. **The app shows a term page first**, under the term's address, then the candidate's readings.

## What was rejected

- **Moving the reviewed candidate to `Wiki/terms/`** — the reasons of decision 026, and it would leave the author's page in
  English, one section per source.
- **Generating the term page from the candidate by code or a model** — a term page's points are judgements; code writes only
  what it can know (frontmatter, sections, the coverage line), and no model's choice becomes a page (CLAUDE.md).
- **A glossary now** — `GOAL.md` §4.6 wants one; it waits for a few pages' `## In der Prosa` sections (P4).

## What would change our mind

The author's answers to `Plan/concept/wiki-terms_2026-10-08.md` §8 — above all whether this is what was meant. The page type
carries `retire when: five term pages exist and the author has used none of them`.
