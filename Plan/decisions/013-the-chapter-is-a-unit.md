# 013 — The chapter is a unit of the wiki, beside the term

**Date:** 2026-09-25 · **Decided by:** the author, in one sentence; the shape by
the session · **Status:** in use

## What was asked

> Extend the Wiki Pages with new Overview Pages - and start to Focus on Plot and
> the Chapters a Bit more

Decision 001 named the condition for its own revision: „if most questions are
about chapters and plot rather than terms, the unit is wrong". `NOW.md` had asked
the author whether the chapter should become a unit („A chapter table from
code"). This is the answer, and it widens the unit rather than replacing it —
the term pages stay as they are.

## What was chosen

- **`Wiki/chapters/kap-NN.md`, one page per chapter** of the planned novel,
  Kap 0 to Kap 40 — the highest number any read source counts. A page collects
  what every read source says about that chapter: one `## Reading` per document,
  quoted, cited to its line, attributed and unmerged. It is a term page's rule
  applied to a chapter, and it is written by a person the same way.
- **Where the sources differ, the page says so and stops**, under
  `## Where the sources differ`. Which title, world or beat the novel uses is
  the author's call; no date settles it (decision 006).
- **`Wiki/overview/`, pages that place rather than define.** `chapters.md` is
  derived by `scripts/chapters.py overview` from the chapter pages' `Title:`
  lines — every source's title for every chapter, side by side — and the check
  fails when it is stale. `plot.md` holds each source's macro structure (chapter
  count, acts and blocks with their ranges, modes, the Vortex) as readings, and
  where they differ.
- **`scripts/chapters.py`** checks what is decidable about the pages, derives
  the overview, and measures `MISSING` (P10): which read documents name a
  chapter as `Kap N` with no reading on that chapter's page. It says what its
  pattern cannot see — a range is not counted as naming each chapter in it, and
  a numbered list without `Kap` is invisible to it.
- **The first readings come from the eight read documents that go chapter by
  chapter**: the 2025 AEGIS subplots, the konsolidiertes Konzept and the
  Konzept-Iteration Genesis (2026-05-08), the strukturierter Outline
  (2026-05-18), the Kapitel-Kompendium (2026-05-30), and the storyform outline,
  „Kernwelten vollständig" and the Plot-Konkretisierung (2026-06-10). The other
  read documents' chapter mentions are what `missing` counts.
- **One commit per source document**, as for a term page: a commit adds one
  document's readings to every chapter page it touches, and names it.

## What was rejected, and why

**`GOAL.md`'s thirteen-section Kapitel-Dossier as the page schema.** Position,
Storyform, Slot-16-Routing, Reveal-Matrix, Anker, Locks, Manuskript-Stand and
the rest are sections before instances (P3, P4) — the failure that produced two
pages from five page types. The readings show which fields the sources actually
give per chapter; a schema can follow them.

**A chapter table from a parser alone.** A parser reads a template's fields; it
cannot say what a source says a chapter is *for*, and several of the eight
sources have no shared template. It remains a way to check a page, not to write
one.

**Chapters in the typed graph now.** `graph.py` has a self-check against the
files and a retrieval bench scored on the wiki's own labels; adding a node type
changes both. It waits until the pages have settled (`NOW.md`).

**New conflict records for every chapter-level difference.** Titles and worlds
differ between sources on many chapters, and a record per title would bury the
fifteen that are about the novel's substance. A difference is stated on its
chapter page; whether one earns a conflict record is a question for the author
(`NOW.md`).

## What would change our mind

- If the chapter pages are not consulted when a chapter is discussed, they are
  a second copy of the outlines and should shrink to the overview.
- If the author settles titles or worlds per chapter, the page gains a decided
  line under the positions, the way a conflict record does — and the schema
  question comes back with instances to answer it.
