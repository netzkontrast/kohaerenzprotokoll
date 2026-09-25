# Overview — pages that place, never define

A term page says what one term is in each source, and a chapter page what one
chapter is. An overview page lays many of them side by side, so a question
about the whole — how many chapters, which act a chapter falls in, what each
source calls it — has one place to be asked (decision 013).

| page | what | how it is written |
|---|---|---|
| [chapters.md](chapters.md) | every chapter, with every source's title for it and the records about it | **derived** by `python3 scripts/chapters.py overview` from the chapter pages; the check fails when it is stale |
| [plot.md](plot.md) | the novel's macro structure as each source lays it out — chapter count, acts and blocks with their ranges, modes, the Vortex — and where the sources differ | by a person, one `## Reading` per document, like a term page |

**An overview adds no reading of its own.** Every statement on it is a
quotation cited to its line, or a pointer to a page that holds one. Where the
sources differ it says so and stops, as every page here does.
