# Sources — the only layer that is true

680 research documents exported from Google Drive, plus the manifest that
indexes them. Everything else in this repository is derived from here; nothing
here is derived from anything else.

**Documents are immutable once landed.** They are written by
`scripts/sources.py` and by nothing else — `.claude/settings.json` denies the
Write and Edit tools on `Sources/drive/**` so that a hand cannot edit a source
while a checksum claims it is untouched.

None of it is canon. A source says what someone wrote on a particular day; what
that *means* is decided in `Wiki/`, by a person.

## Layout

| path | what | committed |
|---|---|---|
| `manifest.jsonl` | one row per document — the spine | yes |
| `drive/<slug>.md` | the landed document, UTF-8, LF | yes |

A manifest row carries `drive_id`, `title`, `slug`, `category`, `tier`,
`format`, `index_date` from the Drive index, and once landed: `export_path`,
`sha256`, `sha256_raw`, `exported_at`.

`drive_id` and `slug` come from the index and are never re-derived, so a
citation written today still resolves after a re-fetch.

## Working with it

```bash
python3 scripts/sources.py status                       # by category and tier
python3 scripts/sources.py check                        # manifest against disk
python3 scripts/sources.py fetch --category theorie-physik
```

`check` is the one to run habitually. It reports rows never fetched, rows whose
file has gone, checksums that no longer match, and files no row claims. Nothing
compared the manifest against the disk before, which is how an export that
covered 26 of 680 documents went unnoticed long enough to become the shape of
the project.

`fetch` talks to the Drive connector directly over HTTP JSON-RPC. **No model
reads a document at any point** — not the session that runs it, not a subagent.
It needs a live Claude Code session, because the connector config and the
session token are session-scoped, and it says so when either is missing.

## Two routes, chosen by format

| format | rows | route |
|---|---:|---|
| `gdoc` | 590 | `read_file_content` — the text export |
| `docx` | 45 | `download_file_content` → markitdown |
| `pdf` | 1 | same |
| `md` | 39 | **none yet** — deferred, see below |
| `mp3` | 1 | **none yet** |

The split is not cosmetic. A Google Doc has no original file, so the text export
is all there is — and it flattens structure: the first one landed had **one**
real heading against 21 lines of bold standing in for headings. Anything with an
original is downloaded as bytes and converted instead, which preserves what the
author marked up. Measured across the 45 `.docx` in `theorie-physik`: **931 real
headings, median 23 per document.**

So section-level retrieval works on the converted formats and does not work on
Google Docs. That is a property of those 590 documents, not a bug to fix.

`md` and `mp3` have no route: the connector lists neither `text/markdown` nor
audio among its supported types. By decision (2026-09-16) they stay unfetched
for now. `fetch` skips them and prints that it did, so they cannot be mistaken
for landed.

## What is normalized, and what is not

On write, mechanically only:

- CRLF and CR become LF
- trailing whitespace stripped from every line — 673 of 852 lines in the first
  document had it
- exactly one final newline

Deliberately untouched, because it is interpretation rather than cleanup:
backslash over-escaping (`\[1\]`, 333 of them in one document), bold used where
headings belong, and bibliographies collapsed onto a single line.

Normalizing happens on write rather than at read time because citations are line
ranges — a file has to be stable or every citation into it is fragile — and
because normalizing later would change every checksum already recorded.

Both checksums are kept: `sha256_raw` is what the connector returned, `sha256`
is the file on disk. Anything left untouched above can therefore be revisited
without re-fetching.

## Frontmatter, and what it costs

Every landed document opens with eight lines of provenance drawn from the
manifest:

```yaml
---
drive_id: "1lIkki…"
title: "Argus: Chronist der Wandlung"
slug: "argus-chronist-der-wandlung"
category: "charaktere"
tier: "T3-work"
index_date: "2025-05-13"
fetched: "2026-09-16"
---
```

This reverses an earlier decision, and the earlier reasoning was sound: with no
frontmatter, a citation's line numbers point at source text only. It is recorded
here rather than silently dropped.

The trade was made the other way because a file that cannot say what it is
becomes unusable the moment someone opens it without the manifest in hand — and
an agent reading one document in isolation is the normal case, not the
exception.

**The consequence, stated so it is unambiguous:** a citation
`^[Sources/drive/<slug>.md:120-134]` counts lines from line 1 of the file **as
it sits on disk**, frontmatter included. There is no offset to remember and no
second convention.

## Tiers

`T2-theory` is external science and theory. `T3-work` is project work.
`T0-duplicate` marks a byte-equal copy of another export and is skipped by
`fetch`.

The manifest has **55 duplicate titles** but only **2** rows marked
`T0-duplicate`, so deduplication is incomplete. Slugs are unique, so nothing
overwrites anything — but the same content can land twice under different
slugs. `sha256_raw` makes that detectable after the fact: two rows with the same
raw hash are the same document.
