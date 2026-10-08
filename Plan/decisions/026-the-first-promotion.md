# 026 — The first promotion: Kishōtenketsu, reviewed in place and pinned

**Date:** 2026-10-08 · **Decided by:** the author (that the page is promoted), the session (how, provisionally) · **Status:** in use, the mechanism provisional

## What was asked

> Kishōtenketsu - promote diese Wikiseite - und generell lass uns mal über den Prozess der Wiki Seiten promoten nachdenken

## What was chosen

1. **`Wiki/candidates/kishotenketsu.md` is promoted.** It carries `status: reviewed` and `reviewed: 2026-10-08`, and the first row of
   `Plan/runs/promotions.jsonl` holds the author's words above, the sha256 of the reviewed part, the 24 documents it covered and the
   coverage then: 30 landed documents write the term, 23 have a reading on the page, 7 are unread.
2. **Promotion records a review of the account, never a choice of reading** (`Plan/concept/promotion_2026-10-08.md` §1). The page
   still collects every reading attributed and unmerged; what the novel holds stays in `Manuscript/kanon.md`, conflict resolutions
   and Weichen.
3. **The page stays in `Wiki/candidates/`.** A field, not a folder: 23 scripts, the app's addresses and the graph read that folder.
   `Wiki/terms/` is not created.
4. **A source read after the review never changes the reviewed part.** `readings.py` appends its reading under `## Since review`;
   `link.py` leaves the reviewed part alone; `python3 scripts/promote.py check`, on GitHub with every push, fails when a reviewed part
   changed or a page's status and the ledger disagree. The author's next yes folds the waiting readings in (`promote.py apply`).
   This answers, provisionally, the question open since 2026-09-17 — a reviewed page and a new source that contradicts it.
5. **`promote.py sheet` is the review sheet**: four measured checks that refuse a promotion (quotations, every source read through,
   frontmatter, links), three that are noted (readings waiting, open conflicts, coverage), and five points for a person.

## What was rejected

- **Moving promoted pages to `Wiki/terms/`** — every reader of `Wiki/candidates/` would need a second path, and an address would
  change on promotion.
- **Demoting a page on any change** — the review would be lost the first time the pipeline touched the page, silently.
- **Refusing new readings on a reviewed page** — the page would fall behind the corpus without showing it, and the ingest would stop
  at every reviewed term.

## What would change our mind

The author's answers to the concept's §7: the rule for a later source, the field against the folder, whether unread documents should
refuse a promotion, what promotion should unlock, and who prepares the next ones. `status: reviewed` carries a `retire when`: the
day the author says what promotion is for and this field does not carry it.
