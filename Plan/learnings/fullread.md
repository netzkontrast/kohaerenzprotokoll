# The full read — what the first one showed

The plan is `Plan/concept/term-digest_2026-10-23.md`. The tool is `scripts/fullread.py` and the procedure is the skill `full-read`. This file holds what the runs measured, one section per page, written as the run went.

## `genesis-klammer`, 2026-10-23 — the pilot

**What was read.** The packet has 92 distinct citations from 12 documents. It has 41 record lines: 3 from the project's own records (W14, C11, C12), 18 from other candidate pages, 20 from chapter pages. That makes 133 references in two source chunks (87 and 5) and one records chunk. With three non-blank lines of context on each side, the windows come to 1,589 source lines.

**Reader A (Sonnet, `full-reader`)** took about 7 minutes and 260,000 tokens for all three chunks. It wrote 75 thoughts:

- 66 in chunk 01 and 4 in chunk 02, all `[S]`;
- 5 in the records chunk, all `[D]`.

Every one of the 92 source citations is `used`. None is `same-as`, `context` or `occurrence`. This is a small, focused page: every line it cites says something about the frame. The records chunk came out as 6 used, 22 same-as, 2 context and 11 occurrence. A reported no defects on the candidate page.

**Corrections by the session before the page was written:**

- **Two cited lines name real persons.** They are `philosophie-im-detail` L693 and L738, two rows of a „Theorie-Anker“ table. They are now `barred` in the ledger. The thought resting only on L738 was dropped, and the one on L693 rests on L688 and L694 now. `fullread.py check` failed to see this because `BARRED` holds only the early names and the trauma symbol. **A real person's name cannot be listed in code, so the reader has to see it.** The check now refuses any citation the ledger itself marks `barred`.
- **A missed `[K]`.** C12 is decided by the author (four Genesis beats, the fourth in Kap 39, 2026-10-05). A marked its line `same-as`, but blind reader B saw the `status:` and wrote a `[K]` thought. The page now has it as g-002. **The records chunk needs the status of each record read, not only its line**; the reader instruction says so, and A did not do it.
- **Quotations inside the thought's own words.** The first render had 2 unresolved and 37 unchecked quotations. The cause: a „…“ in the thought text took the citation `quotes.py` paired with it, usually a bare citation of another line. `write` now puts after each such „…“ the citation of the line it stands on. `check` refuses one that stands on none of the thought's lines. That refusal found two real faults:
  - a paraphrase written inside quotation marks („erst war alles real, jetzt nicht mehr“ for „…jetzt ist es nicht mehr real“);
  - a formula that stands two lines above its cited heading (L115, not L121).

  Five quotation marks in derived thoughts (Kurz, the decision, W14) were removed, because those thoughts have no source line of their own.
- **Result:** 127 quotations checked, 0 unresolved, 0 unchecked; `fullread.py check` and `terms.py check` pass with 0 problems.

**The page** has 76 thoughts and about 3,700 words; the candidate page has about 2,500 words. A thought page is not shorter than the ledger it reads, and for a small page it is longer. It is ordered by question instead of by document. It also holds what the ledger left implicit: 10 explicit differences, 18 prose rules and the frame's relations to 9 other pages. Whether the author finds it easier to review is the author's to say. **A thought page for `aegis` cannot be a flat list**, so §9 of the plan, a second level for the large terms, is needed.

**Blind reader B (Sonnet, same packet, not shown A's files)** took about 8 minutes and 270,000 tokens and wrote 86 thoughts: 63 + 6 + 17.

- **The source chunks.** Every one of A's 70 source thoughts has a B thought sharing at least one citation, and every one of B's 69 has an A thought. The median best overlap of citations is 0.5 from A's side and 0.67 from B's. This is a proxy. **A thought-by-thought alignment by hand has not been done, so agreement on „every thought“ is still unmeasured.** What the proxy shows: no citation was used by one reader and ignored by the other, and both readers used all 92.
- **The records chunk.** Only 22 of 41 states agree. B turned the chapter pages' generated question lines (B- and S-questions under „Questions for this chapter“) into 7 `open` thoughts; A set them aside as occurrences. Those lines are navigation written by code (`chapter_sources.py`), not readings. **They do not belong in the packet.** Since the same day, `inbound()` skips the generated sections of a chapter page, as it already skips `Wiki/questions/reading/`. The packet now holds 30 record lines instead of 41, and the page counts 122 references.

**Cost, extrapolated from this one page.** About 3 reader-minutes and 110,000 tokens per 40 citations, about 1 thought per 1.2 source citations here. `aegis` (2,906 citations, 435 documents) would be about 20 chunks and 2,000+ thoughts at this density. The density will fall where documents repeat each other; that is what grouping across chunks is for, and it has not been tried yet. `genesis-klammer` fit in one chunk plus five references.
