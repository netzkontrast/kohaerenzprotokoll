# 024 — `Manuscript/` becomes the novel's workspace: canon, working drafts, and nothing else

**Date:** 2026-10-05 · **Decided by:** the author (what), the session (how) · **Status:** in use

## What was asked

> Bau das in die ui ein… denke darüber nach wie du die Arbeit am Roman selbst ui massig gestalten willst… los eine
> Sektion nur für Manuskript und die chapter die Charaktere etc.. ähnlich dem Wiki nur hier nur Canon und Arbeitsdruck,rmte

„Das“ is the assessment of the material (`Plan/runs/writing/book/developmental-editor_2026-10-05.md`). The last word
reads as „Arbeitsdrucke“ or „Arbeitsentwürfe“: working drafts.

## What was chosen

1. **Two strata, and only two.** The novel's workspace holds **canon** and **working drafts**. A wiki reading never
   appears in it as content; a card or chapter may link to its wiki page as research, labelled so.
2. **One canon ledger, `Manuscript/kanon.md`.** A table of the author's decisions about the book, each with an id, a
   date and where it stands, and a list of approved chapters. Today it holds C6 and C9 and no chapter.
   - A card, a chapter or a Weiche is canon in the app **only if it names an id from this ledger**. `ui.py --check`
     fails on an id the ledger does not hold.
   - Nothing becomes canon because a source, a majority of sources or a draft says so (decision 006).
3. **Cards** for the cast (`Manuscript/figuren/`) and the world (`Manuscript/welt/`), one file each.
   - Front matter: `name`, `kind`, `kanon` (ledger ids), `match` (the surfaces the app counts in the drafts) and,
     optionally, `wiki` (the research page).
   - Body: `## Kanon`, `## Arbeitsstand` (one line per draft, naming the file), `## Offen`.
   - The first 26 cards were written by the session from the ledger and the drafts in `Manuscript/`. Figures that
     exist only in a session's draft say so.
4. **The app's „Manuscript“ screen gets tabs:** Overview, Chapters, Cast, World, Plot, Decisions and Findings.
   - **Overview** shows tiles (canon entries, approved chapters, drafts, cards, open Weichen, findings) and the
     workspace's README.
   - **Chapters** groups each `kap-NN/` folder's drafts with the findings that read them.
   - **Cast** and **World** show the cards, each with a derived table: how often its surfaces occur in each draft,
     counted, not inferred.
   - **Plot** shows `plot/`.
   - **Decisions** shows the ledger and every sheet in `Plan/weichen/`, open unless the ledger names it.
   - **Findings** shows `Plan/runs/writing/`. The findings stay where `writing-skills` rule 6 puts them; the app only
     shows them beside the drafts. Findings about the parked Legacy draft are marked as such.
   - Every item has an address on the website: `#/manuscript/<tab>/<id>`.
5. **A sheet for W0** (`Plan/weichen/w0-kern.md`), the Weiche the assessment proposes before W2.

## What was rejected

- **A third research layer.** The cards do not collect what the sources say. That is the wiki's job, and mixing
  the two is how a source's claim would start to look like a decision.
- **Status fields on each draft.** Canon is stated once, in the ledger, so that it cannot be stated twice and
  differently.
- **Cards generated from the wiki.** They would fill the cast with readings, not decisions.

## What it does not decide

- **Any content.** Every card except the five Guardians' and the two world cards that cite C9 says „Nichts
  entschieden“ under `## Kanon`.
- **Whether the session's invented figures belong in the book.** Each card says so and asks.
- **Who writes the prose** (question A of the writing plan).

## What would change our mind

- The author wants the canon stated somewhere else, or per file.
- The cards fill with readings instead of decisions: then they have become a wiki and go back to being one.
