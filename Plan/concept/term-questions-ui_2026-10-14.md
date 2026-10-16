# Term questions and the authoring interface

Author request, 2026-10-14: 100 additional reading questions for each wiki term, including cross-term questions; reconsider the complete UI and make promoted terms visible.

Implementation targets:
- `Wiki/questions/reading/`: one checked, stable question bank per term. Reading prompts are proposals with an unchecked answer status, not new unresolved canon conflicts.
- `scripts/reading_questions.py`: coverage, identity, source anchors, relationships and offline refusal fixtures.
- `scripts/ui.py`, `scripts/ui.js`, `scripts/ui.html`: question workshop with search, term/category filters, pagination, deep links, local notes and export; separate term pages, reviewed ledgers and candidates; a promotion dossier and direct reading-to-question actions.
- `agents/`: the same question identities, paths and addresses available to tools.

Verification: exact per-term counts, valid anchors and unique IDs/texts, UI route roundtrips, filter and storage behavior, repository checks, desktop/mobile inspection. Promotion and canon remain the author's decisions.

The current Vercel URL is a deployment snapshot. This branch receives its own preview on push; a merge is needed to update production.

## What the interface was missing

The app treated every wiki entry as a candidate, even when its account had been
reviewed and a German term page existed. It concatenated the two reading layers
into one long page. A person could inspect evidence but had no short route from
reading a term to exploring a question and retaining an answer. A grid of every
read document crowded the wiki filters; the fixed desktop width also assumed a
particular viewport.

This change separates the layers under the same stable term address. Filters
show term pages, promoted candidates, remaining candidates, confirmed term pages
and readings added since review. The promotion dossier distinguishes review of
an account from approval of a German term page and from a canon decision.
Kishōtenketsu is the existing instance: reviewed account, draft term page.

The question workshop separates additional reading prompts from unresolved Q
records and the author agenda. Search, eight editorial lenses, direct/cross-term
filters, local work status and pagination make the volume usable. Selecting a
question exposes its terms and a local answer editor. Exports carry identity,
paths, addresses and notes. Browser storage failure is visible. The agent handover
copies only the instruction and file identity; it reads evidence in the repo.

The shared shell adapts to the viewport, preserves the established paper/ink
reading identity, supplies focus and selection states, and uses a scrollable
mobile navigation. The source-document grid is now an optional disclosure.

## Next changes that would earn their place

1. **Answer-to-impact navigation.** Link an answer to the affected chapters,
   storypoints and Weichen using explicit records. A co-mention is insufficient
   evidence that changing a term changes a chapter. First record several actual
   answer/impact examples by hand; then derive the view.
2. **A decision inbox.** Bring promotion requests, proposed answers and pending
   canon choices together, with the exact changed passages, dependencies and
   author wording. No button should manufacture approval or silently merge
   conflicting readings.
3. **Reviewed answer import.** Local notes need a version-aware import through a
   proposed repo change. Preserve question IDs, record the source snapshot and
   compare against newer canon before committing. This UI exports notes; it does
   not claim that local storage is a shared repository or a reliable backup.
4. **A term-first graph.** Start with the selected term and explicitly stated
   relations; expose supporting passages and optional chapter links. Keep the
   entire graph available as a secondary exploration view.
5. **An author reading mode.** A compact German term page, an optional evidence
   layer and a visible distinction between source claim and canon are the basis.
   The existing English work records remain attributed and unchanged; translating
   them is a separate editorial task.
6. **Asset and startup cost.** The app embeds a substantial research snapshot.
   Pagination bounds rendered question rows, but does not reduce transfer size.
   A later measured change could lazy-load per-term banks on the website while
   retaining the self-contained canvas. It needs explicit loading/error states
   and agent parity; no speculative framework migration is needed.

## Editorial limits of the question bank

The additional questions are structured exploration drafts. Topics and partners
are selected per term, and the first question per term is individually written;
the remaining wording is assembled through shared lenses. Exact counts and
unique wording do not prove that every question is equally useful. The workshop
lets the author select what deserves investigation. It does not turn volume into
10,600 independently diagnosed gaps or conflict records.
