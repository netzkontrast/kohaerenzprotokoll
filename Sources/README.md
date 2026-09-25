# Sources — the only layer that is true

The research documents exported from Google Drive, the manifest that indexes
them — 613 <!--state:sources.total--> rows, 371 <!--state:sources.landed--> of
them landed — and, beside each document that has been read, its term census and
its note. Everything else in this repository is derived from the documents in
`drive/`.

**Documents are immutable once landed.** They are written by
`scripts/sources.py` and by nothing else — `.claude/settings.json` denies the
Write and Edit tools on `Sources/drive/**` so that a hand cannot edit a source
while a checksum claims it is untouched.

None of it is canon. A source says what someone wrote on a particular day; what
that *means* is decided in `Wiki/`, by a person.

## Layout

| path | what | written by |
|---|---|---|
| `manifest.jsonl` | one row per document — the spine | `scripts/sources.py` |
| `duplicates.jsonl` | the rows folded away as copies, each naming the row it duplicates | `scripts/dedupe.py` |
| `drive/<slug>.md` | the landed document, UTF-8, LF | `scripts/sources.py`, and nothing else |
| `terms/<slug>.md` | the term census of one document, exhaustive — 16 <!--state:documents.with_census--> | a reader |
| `notes/<slug>.md` | what one document says about the terms that matter, quoting with line numbers — 16 <!--state:documents.with_note--> | a reader |

A census and a note describe their one document and nothing else: no count,
comparison or expectation from another source (`CLAUDE.md`, *The process*).

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
covered 26 of the then 680 rows went unnoticed long enough to become the shape of
the project.

`fetch` talks to the Drive connector directly over HTTP JSON-RPC. **No model
reads a document at any point** — not the session that runs it, not a subagent.
It needs a live Claude Code session, because the connector config and the
session token are session-scoped, and it says so when either is missing.

## Two routes, chosen by format

| format | rows, 2026-09-24 | landed | route |
|---|---:|---:|---|
| `gdoc` | 560 | 333 | `read_file_content` — the text export |
| `docx` | 12 | 12 | `download_file_content` → markitdown |
| `md` | 39 | 26 | the text route — see below |
| `pdf` | 1 | 0 | `download_file_content` → markitdown |
| `mp3` | 1 | 0 | **none** |

A Google Doc has no original file, so the text export is all there is. Anything
with an original is downloaded as bytes and converted instead, which preserves
what the author marked up.

**What the split does *not* cost is headings, and an earlier version of this
page said otherwise.** It claimed the text export flattens structure and that
"section-level retrieval works on the converted formats and does not work on
Google Docs" — generalised from the first document landed, which had one real
heading against 26 lines of bold. Counted across everything on disk on
2026-09-16, before the corpus was deduplicated:

| format | landed | median headings | with ≥5 | with none |
|---|---:|---:|---:|---:|
| `gdoc` | 360 | 17 | 270 | 18 |
| `docx` | 45 | 17 | — | — |

**The medians are identical.** `argus-chronist-der-wandlung` is an outlier, not a
representative, and one sample was used to describe 590 documents. Section-level
retrieval works on both routes. The 18 gdocs with no headings are a small,
listable set rather than a property of the format.

The claim is left here rather than quietly deleted, because the mistake is the
useful part: it is P18 — one attempt measures nothing — applied to our own
documentation instead of to a model.

`md` was listed as having no route, and 4 of the 43 rows were landed, so the
connector serves at least some of them. On 2026-09-24, on the author's yes, the
canon-era rows were fetched with `fetch --since 2026-05-01 --include-md`, and all
26 `md` among them came through the text route. 26 of the now 39 `md` rows are
landed. The other 13 and the one `mp3` stay deferred by decision (2026-09-16). `fetch` skips what it cannot route and prints
that it did, so nothing can be mistaken for landed.

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

## Duplicate exports

Drive holds up to five exports of the same document — a gdoc export, a docx
export, a `kopie` of each, a second run of both — each with its own `drive_id`,
so each landed as its own row. 409 files were 346 documents.

`python3 scripts/dedupe.py` folded 67 <!--state:sources.folded--> extra files
away — 63 at first, and four more from the canon-era landing: the file left
`Sources/drive/`, the row left `manifest.jsonl` and moved in full to
`duplicates.jsonl`, which `sources.py next` filters against by `drive_id` so a
folded document is never offered for fetching again.

**The surviving copy is not the longest one.** The gdoc export is longer and
carries less — its extra words are `end list` markers, its missing words are the
URLs behind the footnotes. `scripts/dedupe.py` has the measurement and the full
ranking; `Plan/runs/dedupe.json` has the decision per group.

## Frontmatter, and what it costs

**All but 23 <!--state:sources.without_frontmatter--> of the
371 <!--state:sources.landed--> landed documents** open with eight lines of
provenance drawn from the manifest. Those were landed before this decision was
taken, and nothing has back-filled them.

That matters more than it looks: code which assumes the body starts at line 10
silently swallows nine lines of content in those files. Several ad-hoc counts in
this repository's history did exactly that. `scripts/profile.py` and
`scripts/corpus.py` **find** the boundary per document instead, and
`corpus.py` prints how many documents lack it on every answer.

The eight lines, where they exist:

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
`T0-duplicate` marked a byte-equal copy of another export and was skipped by
`fetch`. No row carries it any more — the two that did were folded away by
`scripts/dedupe.py`, which subsumes it and catches the copies that are not
byte-equal as well.

**35 <!--state:sources.repeated_titles--> titles still appear on more than one
row, and they are not duplicates.** They survived a Jaccard comparison at
0.8 that folded 63 files away, so their content genuinely differs. This used to
read „55 duplicate titles but only 2 rows marked `T0-duplicate`, so deduplication
is incomplete", which drew the right conclusion from the wrong evidence: **a
shared title was never evidence of a duplicate**, and by the time content was
actually compared, the titles had stopped predicting it. `Blueprint` is a title
someone reuses, not a document landed twice.
