# Now

*What is open. One page, hard limit. Finished work leaves this file — git
remembers it. If this does not fit on a page, too much is open at once.*

**Updated:** 2026-09-16

## Doing

**Fetching the source corpus.** 27 of 680 landed. The mechanism is proven end to
end on one document and the tool handles parse, normalize, land, manifest
writeback and verification.

Next concrete move: `theorie-physik` (45 documents, none landed) — it is where
the load-bearing terms live, and it is a batch small enough to learn from.

```bash
python3 scripts/sources.py next --category theorie-physik --limit 5
# per drive_id: mcp__Google_Drive__read_file_content, then
python3 scripts/sources.py land --drive-id <id> --consume
python3 scripts/sources.py check
```

## Next

1. **Read three fetched documents by hand** and write their notes. This is what
   decides the note format — `Plan/learnings/read-source.md` carries the
   predictions to check it against.
2. **Gather the terms those three share** into the first candidate pages. About
   twenty pages by hand before any schema is written down.
3. **Then** look at what the pages actually needed, and automate that.

## Blocked, and on what

**44 source rows have no fetch path.** 43 are `md` and one is `mp3`; the Drive
connector's supported types cover neither. Needs a decision: skip them, fetch
them another way, or drop them from the manifest. Everything else can proceed
without this.

## Waiting on the author

- **`Plan/concept/` review** — three documents describe what is being built.
  Nothing blocks on it, but building against an unread plan is how the last one
  went wrong.
- **PR #43** — carries the concept documents and the reset. Clean, no conflicts,
  no CI.
- **The flat-heading question** (`Plan/learnings/fetch.md` §7). Source documents
  use bold where headings belong — one real heading in the first document
  against 21 bold pseudo-headings. Section-level retrieval does not exist on
  this corpus as fetched. Cheap to fix later against the stored raw checksums,
  so it is recorded rather than acted on.
