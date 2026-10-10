# Term pages — the process from a candidate to the author's page

*2026-10-08. Asked for by the author, after the first promotion: „Lass mal den Prozess und die nötigen Tools und Scripte die du
brauchst für Wiki terms Pages“. The sentence has no verb; it is read as „build the process, and the tools and scripts it needs,
for the pages in `Wiki/terms/`“ (decision 027). Built by P3: the first page, `Wiki/terms/kishotenketsu.md`, by hand, then the
checks around what it needed. Everything here is `provisional` until the author answers §8.*

## 1. Two pages for one term, and why

| | candidate page `Wiki/candidates/<slug>.md` | term page `Wiki/terms/<slug>.md` |
|---|---|---|
| for | the research: every source's reading | the author's work on the novel |
| language | English work prose, German quotations | German (`GOAL.md`: „Wiki-Inhalte … auf Deutsch“) |
| unit | one section per source document, by date | one section per question the author asks of a term |
| what it says about canon | nothing — it never decides a reading | what the author **decided** (`[K]`, linked), apart from what sources **say** (`[S]`) |
| written by | `readings.py` from readers' files, one commit per document | a session or the author, from the reviewed candidate |
| reviewed | promotion, `status: reviewed` (decision 026) | approval, `status: approved` |

The term page does not replace the candidate and does not repeat it: it links to it for every reading. It answers what the
candidate cannot — what the project has settled, what stays open, what the sources say the prose must or must not do — in the
form `GOAL.md` §4.6 asks for: every point with its source and its status. The first question answered on 2026-10-08 (decision
026, a field not a folder) stands: the review is a field on the candidate; the folder `Wiki/terms/` now holds something else,
the page written *from* a reviewed candidate.

## 2. The process

```
candidate grows (ingest, readings.py)
   │
   ▼  promote.py sheet <slug>  →  the author: „promote …“  →  promote.py apply      (decision 026)
reviewed candidate
   │
   ▼  terms.py scaffold <slug>     refuses an unreviewed candidate; writes frontmatter, sections, the measured lines
   ▼  terms.py finds <slug>        every line of the project's own records that names the term — the [K] material
   ▼  a writer fills it in         German, every bullet tagged; citations asked of read.py --find or taken from the candidate's verified lines
   ▼  quotes.py · terms.py check   every quotation on its line; every rule of §3
draft term page  ──commit──  „terms/<slug>: draft from the reviewed candidate of <date>“
   │
   ▼  the author: „…“  →  terms.py approve <slug> --words "…"
approved term page (pinned outside the author's block)
   │
   ▼  a source read later → the candidate's ## Since review → terms.py check: „behind“
   ▼  the author re-reviews the candidate → the writer updates the term page, status back to draft → the author approves again
```

**One commit per term page**, and its first line names what it was written from — the candidate's review date, or for an update
the document that made the candidate move. That is the rule for wiki pages (CLAUDE.md, *Committing a wiki page*) carried over:
`git log Wiki/terms/<slug>.md` is the page's provenance.

## 3. What is checked, and what stays judgement

| decidable — `terms.py check`, on GitHub with every push | judgement — the writer, then the author |
|---|---|
| the candidate is reviewed, and `candidate_hash` names one of its reviews | which points belong on the page at all |
| the eight sections, in order; none empty (`- [L] …` when nothing is known) | whether `Kurz` is fair to all readings |
| every line is a bullet opening `[K]`, `[V]`, `[S]`, `[L]` or `[D]`; `[M]` refused | whether a `[D]` derivation is sound |
| `[S]` cites a landed document line; `[V]` a line or `Plan/` | whether `[S]` picks the source's own words for the point |
| `[K]` links a decision file, an answered Weiche, `kanon.md` or a decided conflict | whether the linked decision says what the bullet says |
| every quotation on its line (`quotes.py`, as for every wiki file) | |
| every link resolves; the page reads as German (function words) | |
| the author's block exactly once; outside it, an approved page unchanged | |
| behind: the candidate re-reviewed, or readings waiting under `## Since review` (noted) | |

`terms.py selftest` has a case for every row on the left that can fail (18 cases, `selftests.py`), each shown failing on the
defect it names.

## 4. What it deliberately does not do

- **No model writes a term page.** The scaffold writes only what code can know: the frontmatter, the sections, the coverage line.
  The prose is a writer's, its citations asked of `read.py`, never typed (P26).
- **No reading is merged.** `[S]` points stay attributed; where sources differ, the page lists them and stops (P13).
- **No canon by the side door.** `[K]` needs a link to the author's decision; a source calling itself `[K]` or „kanonisch“ is
  quoted as `[S]` (decision 006). The first page quotes the glossary's own „[K]“ inside an `[S]` bullet.
- **No term page without a reviewed candidate**, and no approval without the author's words (P0).
- **No glossary yet.** `GOAL.md` §4.6 wants one with „in Prosa verboten“ and „diegetische Form“; it can be derived from the
  `## In der Prosa` sections once a few pages exist (P4), not before.

## 5. The first page — what writing it by hand showed

- **The project's own position was not where it was expected.** No decision file, no `kanon.md` entry and no storyform file names
  Kishōtenketsu; only W1 does, in its question. So the page found a real gap: after W1 (A, then B as a check) it is not settled
  whether Kishōtenketsu is recipe like the storyforms or one of the models the treatment is diagnosed against. It is on the page
  as `[L]` and below as a question. `terms.py finds` lists those places for every next page.
- **Citing a decision's words is not a source quotation.** `quotes.py` counts a quoted sentence from `Plan/weichen/` as unchecked;
  the page states the decision and links it instead, and `terms.py` checks the link.
- **A frontmatter key with digits is invisible** to the shared parser (`wiki_index.frontmatter` reads `[a-z_]+`), so the field is
  `candidate_hash`.
- **Slugs are noise in a search for the term**: `romanstruktur-duale-erzaehlung-und-kishotenketsu` names a document, not the term,
  so `finds` ignores text in backticks and citations.

## 6. The app

The project app shows a term page first, under the term's existing address (`#/wiki/<slug>`): its sections as „Begriffsseite · …“,
a chip with its status, then the candidate's readings after a divider. No new address, so `ui.py --check`'s two-way address check
is unchanged.

## 7. Which pages next

A term page needs a reviewed candidate, and the sheet (`Plan/runs/promotion-2026-10-08/ready.md`) says which candidates are ready
to be put to the author: 24 pass every check, 79 pass the refusing checks but have unread documents or open conflicts. What a term
page is *for* decides the order better than the sheet does: the terms the next chapters need (`Plan/storyform/development.json`
and the chapter pages say which) before the clean ones.

## 8. Questions for the author

1. **Is this what you meant?** The message had no verb; the reading here is „build the process and tools for `Wiki/terms/`“.
2. **The sections** — Kurz, Was das Projekt entschieden hat, Was die Quellen sagen, Wo die Quellen auseinandergehen, In der Prosa,
   Offen, Autor-Notizen, Herkunft. Missing one you want (e.g. „Kapitel“, where the term matters in the book), or one too many?
3. **German** for term pages, while candidates stay English — yes?
4. **Kishōtenketsu after W1** — recipe like the storyforms, or a model for the diagnosis? The page's first `[L]`.
5. **Which terms next**, and who writes them: a session drafts, you approve — per page, or in batches?
