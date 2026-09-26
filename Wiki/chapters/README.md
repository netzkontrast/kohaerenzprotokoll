# Chapters — what each source says a chapter is

One page per chapter of the planned novel, `kap-00.md` to `kap-40.md`. A page
collects **what every read source says about that chapter**: one
`## Reading — \`slug\`, date` per document, in the order the documents are
dated, each statement quoted and cited to its line. It is a term page's rule
applied to a chapter (decision 013).

**A chapter page never decides which reading the novel follows.** The sources
give the same chapter different titles, worlds and beats; the page lets each
stand and, under `## Where the sources differ`, says where they part and stops.
No date settles anything (decision 006).

## A reading

```
## Reading — `koharenz-protokoll-strukturierter-outline-2026-05-18-md`, 2026-05-18

Title: „Die Stimme im Rauschen“ ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L391]
Position: „Heldinnenreise innen“ ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L191]

- Plot beats: „Telefon-Stille als erster expliziter Anker“ ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L401]
```

- `Title:` and `Position:` appear only when the source gives them. Every
  `Title:` line feeds the derived overview, so it holds exactly one quotation.
- The bullets are the source's own substance for that chapter — what happens,
  where, whose view, storyform accents, locks, Genesis echo, leitmotiv — each a
  short verbatim quotation. English between the quotation marks is minimal.
- The source's stance marks stay: a passage it labels `[K]`, `[V]`, `[S]` or
  `[L]` says so beside its citation. A document that is a proposal says so in
  its reading's heading.

## Navigation, around the readings

Three sections are navigation, and none is a reading. Above the readings:

- `## What this chapter is about` — three to five German sentences summarising
  what the readings below say, naming each source where they differ and
  deciding nothing between them.

After `## Where the sources differ`:

- `## Questions for this chapter` — eight basic questions every author asks of
  a chapter, then the chapter's own, written against GOAL.md §4.5 and §5 before
  any search (`Plan/runs/qmd-chapters-2026-09-26/`).
- `## Candidate sources — unread, ranked by qmd` — the landed documents with no
  census that a vector search for those questions returned, and which
  questions returned each. A place to look, never a claim or a number.

`scripts/chapter_sources.py write` replaces all three whole. They carry no quotation
and no citation, so `chapters.py` and `quotes.py` see nothing in them.

## Frontmatter

```yaml
chapter: 7            # the number in the file name
status: candidate     # nothing is promoted, as for term pages
sources: 5            # the number of readings
ingested: [...]       # the documents read onto the page, one per reading
records: ["C7"]       # conflict and question records about this chapter
gathered: "2026-09-25"
```

## What checks it

`python3 scripts/chapters.py` fails on a page whose name and `chapter:`
disagree, a reading of a document no `reconcile.json` records as read,
`ingested:` or `sources:` that do not match the readings, a citation inside one
reading that names another document, a `[[link]]` to no page, a `records:` id
no record has, or a stale overview. `python3 scripts/quotes.py` checks every
quotation against its line, as on every other page.

`python3 scripts/chapters.py missing` names what is not here yet: every read
document that writes `Kap N` with no reading on that chapter's page —
91 <!--state:chapters.missing--> such mentions now. It does not count a range
(`Kap 14–26`) as naming each chapter in it, and it cannot see a numbered list
without `Kap`, so it under-counts.

## Committing

As for a term page: a commit adds one source document's readings to every
chapter page it touches, and its first line names that document.
