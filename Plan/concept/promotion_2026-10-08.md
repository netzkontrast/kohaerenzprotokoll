# Promoting a wiki page — what it is, what it checks, what it protects

*2026-10-08. Asked for by the author: „Kishōtenketsu - promote diese Wikiseite - und generell lass uns mal über den Prozess der
Wiki Seiten promoten nachdenken“. Built as a proposal with one instance; every choice below is `provisional` until the author
answers §7. The first promotion is decision 026.*

Until today the wiki had a step drawn in every diagram — `review (a person) → Wiki/terms/` — and nothing behind it. `Wiki/README.md`
said why: „Nothing is promoted until enough candidates exist to show what promotion should check; the schema follows the pages.“
106 pages later the pages can show it, and one question had been waiting since 2026-09-17: what happens when a source read after
the review contradicts a page the author signed (`Plan/questions-for-the-author.md`, „needed before the first promotion“).

## 1. What a promotion says — and what it does not

**It says: the author reviewed this account.** The readings say what their lines say, with their stance; the differences between
sources are all listed; the lead paragraph — the one place a page speaks in its own voice — claims nothing the readings do not
carry. It says this *as of* a named set of documents, and records how many documents that name the term were still unread.

**It does not say which reading is right.** A promoted page still collects readings attributed and unmerged, and where they
disagree it still says so and stops. Deciding a reading is canon, and canon has its own places: `Manuscript/kanon.md`, a conflict
record's resolution, a Weiche's answer. If promotion also meant „this is what the novel holds“, every review would become a canon
decision taken by the side door, without the alternatives a Weiche sheet lays out. Keeping the two apart is the one structural
choice here that is not provisional: the author can still decide otherwise, but then promotion needs a second field, not this one.

**It changes no reader's behaviour yet.** Nothing ranks, filters or trusts a reviewed page differently: what promotion should unlock
is the author's question (§7.4), and a change to retrieval is measured on the labels, not argued (CLAUDE.md, *Model calls*).

## 2. Where it lives — a field, not a folder

| | `Wiki/terms/` (the old plan) | `status: reviewed` in place (built) |
|---|---|---|
| scripts that read `Wiki/candidates/` | 23 must learn a second folder | none changes |
| the app's addresses, `#/wiki/<slug>` | change on promotion, or need a redirect | stay |
| graph node ids, `[[links]]`, `git log` of the page | the file moves; history needs `--follow` | stay |
| a withdrawal | moves the file back | one field and one ledger row |

So a promoted page stays where it is and carries `status: reviewed` and `reviewed: <date>`. **The record is
`Plan/runs/promotions.jsonl`**, append-only like `judgements.jsonl`: per promotion or withdrawal the page, the date, who, the
author's words verbatim, the sha256 of the reviewed part, the documents it covered and the coverage measured then. The folder
`Wiki/terms/` is not created; `Wiki/README.md` says so in its row.

```yaml
status: reviewed     # provisional — one instance (kishotenketsu, 2026-10-08)
                     # may not: decide a reading, enter canon, rank retrieval
                     # retire when: the author says what promotion is for and this field does not carry it
```

## 3. The rule for a source read after the review

The question of 2026-09-17, with the three answers that were on the table:

| | what happens | what it costs |
|---|---|---|
| a — **demote on change** | any new reading turns the page back into a candidate | the review is lost silently, the first time the pipeline touches the page |
| b — **block** | a reviewed page takes no new readings | the page falls behind the corpus and does not show it; the ingest stops at every reviewed term |
| **c — keep and append (built)** | the reviewed part is pinned; a new reading lands under `## Since review` at the end of the page | the page shows two layers until the author looks again |

**c, in detail.** `readings.py` puts the reading of a reviewed page — and its line for the differences — under
`## Since review — read after the author's review of <date>, not yet reviewed`, never into the date order above. A new reading that
contradicts a reviewed one gets its conflict record as every contradiction does (decision 003); the page's `conflict:` field names
it, and the frontmatter is outside the pin. `link.py` does not mark mentions in a reviewed part. The author's next look is a
re-review: `promote.py apply` folds the waiting readings into date order and their difference lines into place, and pins the new
state under the author's new words. A hand edit to a reviewed part — even a fix — fails `promote.py check` (on GitHub with every
push) until it is reverted or the author re-reviews; a defect found in a reviewed page is therefore a question to the author with
the fix proposed, not a commit.

## 4. The review sheet

`python3 scripts/promote.py sheet <page>` measures what can be measured and lists what a person has to judge; `ready` runs the
measured part over every term page. **Refuses** means `apply` will not promote.

| check | refuses? | why |
|---|---|---|
| every quotation resolves, none unchecked | refuses | a review of a misquote signs the misquote |
| every document in `ingested:` has a census, a note and a reconciliation | refuses | a reading from a scan, never reconciled, has not passed the frozen census (CLAUDE.md, *The process*) |
| the frontmatter is what the body derives | refuses | the counts the app shows must be the page's |
| every `[[link]]` resolves | refuses | |
| readings waiting under `## Since review` | noted | `apply` folds them in; the author has then seen them |
| open conflict records naming the page | noted | a review shows a conflict; only the author's decision on the record settles it |
| coverage: landed documents that write one of the page's surfaces, read or unread | noted | the review is of what was read; the sheet says how much was not |

For a person (the sheet's checklist): the lead paragraph; each reading's prose against its line; whether `## Where the sources
differ` is complete and holds nothing more; whether one of its differences should be a conflict record; whether the unread documents
should be read first.

**Who.** P0 makes promotion the author's alone. A session may run the sheet, fix what it finds on a candidate page (each commit naming
its document, as always), and propose; `apply` refuses without `--words`, the author's words verbatim. It cannot prove who spoke —
neither can a decision file — but it makes the claim checkable in the ledger and in git.

## 5. The first instance — Kishōtenketsu

The sheet before any change found two defects and one stale claim; each was fixed in its own commit on a candidate page
(PR #186):

- a duplicate difference line, from `als-ihr-narrativer-architekt-blicke-ich-auf-das-r`, under `## Where the sources differ` —
  a reader's `<!-- differ -->` line repeating a quotation its reading already gave (L134);
- the provenance note said the scanned documents „have no census and no reconciliation yet“: true on 2026-09-25, false since —
  all 24 are reconciled;
- the page said nothing about coverage: 30 landed documents write the term, 23 have a reading here (one more, the world-sensorik
  drafting document, writes only `ketsu`), 7 are unread — among them `bewerte-kishotenketsu-als-zentrales-narrativ`, a
  document whose subject is the term, and two that write it 15 and 11 times.

Then every measured check held, and the page was promoted on the author's words. The sheet as it stood is
`Plan/runs/promotion-2026-10-08/kishotenketsu.md`; the record is the first row of `Plan/runs/promotions.jsonl`.

**What the page cannot know about itself.** Decision 025 made Dramatica the recipe and W1 made theory a diagnosis; Kishōtenketsu
is now one lens the `developmental-editor` skill applies or re-scopes. That is the project's position, not a source's reading, so it
is not on the page; promotion does not change that (§1).

## 6. What the 106 pages look like against the sheet

`python3 scripts/promote.py ready`, 2026-10-08, is in `Plan/runs/promotion-2026-10-08/ready.md`. Its summary is in §8, measured
after the tool was built rather than estimated before.

## 7. Questions for the author

1. **The rule for a later source (§3)** — c as built (pinned, a `## Since review` section, re-review on your word), or a or b.
2. **A field or a folder (§2)** — `status: reviewed` in place as built, or `Wiki/terms/` after all. *Answered in part 2026-10-08:* the
   author asked for term pages; they are a second page written from the reviewed candidate (decision 027), and the review stays a field.
3. **Coverage** — may a page be promoted while documents that name its term are unread (Kishōtenketsu was, at 23 of 30, as you
   asked), or should the sheet refuse above some number — and should `bewerte-kishotenketsu-als-zentrales-narrativ` be read now?
4. **What promotion is for.** Today it protects and shows. Possible next uses, none built: the app lists reviewed pages first; the
   writing skills may cite a reviewed page as „the research says“ (never as canon); `graphrag.py` marks evidence from reviewed pages —
   the last only if the bench shows it helps.
5. **Who prepares** — whether a session may run the sheet over the next pages and propose a batch („these five are clean“), with you
   saying yes per page or per batch.

## 8. Measured: the term pages against the sheet

`python3 scripts/promote.py ready`, run 2026-10-08 after the promotion, over all 106 term pages (`Plan/runs/promotion-2026-10-08/ready.md`):

| what the sheet found | pages |
|---|---|
| refuses: one quotation unchecked (`ani`, `personas`, `ztv`) | 3 |
| nothing refuses, nothing noted | 24 |
| nothing refuses; unread documents name the term | 53 |
| nothing refuses; open conflicts on the page and unread documents | 21 |
| nothing refuses; open conflicts on the page | 5 |

So the mechanical part is not what holds promotion back: 103 of 106 pages pass it. What decides is coverage and the open conflicts — the big pages are the least covered (`aegis`: 504 landed documents write it, 189 have a reading on the page, 289 are unread), and the clean 24 are the small, local terms: `aegis-metriken`, `archiv-des-ungesagten`, `ars`, `datenverarbeitungsknoten-7g`, `ecr`, `entropie-resonanz`, `entropie-signatur`, `evaluierungseinheit`, `formel-inversion`, `garten-der-stillen-praesenz`, `genesis-klammer`, `junas-ankerpunkt`, `lex`, `nullpunkt-protokoll`, `ouroboros-struktur`, `pms`, `residual-echos`, `rsa`, `schleuse-7`, `snk`, `system-monitor`, `therapie-schnittstelle-alpha`, `thermodynamischer-phaenomenalismus`, `vermittler-stimme`. Seven of them (`ars`, `ecr`, `entropie-resonanz`, `nullpunkt-protokoll`, `pms`, `rsa`, `snk`) keep their readings in the older format without `## Reading` headings, which the sheet does not yet look at.

*Correction during the run:* the first `ready` refused 15 large pages for „every source read through“, all for one document, `entropie-aegis`. It is reconciled — in the first full re-comparison, `Wiki/compare/001-entropie-aegis-vs-aegis-emergenz.md`, not in a `reconcile-NN` record — and `promote.py` now asks what `state.py` counts, a run directory holding a `reconcile.json`.
