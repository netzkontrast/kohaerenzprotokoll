# Learnings — fetch (Drive → `Sources/drive/`)

## Status

**1 document fetched end to end** (2026-09-16), plus one earlier hand-run by a
subagent that was discarded and re-landed through the tool. 27 of 680 landed
in total; the other 26 predate this work and were fetched by an unknown path.

Everything below marked *measured* comes from that one document. Everything
marked *predicted* comes from the manifest and has not been run yet. One
document proves a mechanism, not a pattern — treat the counts as a hypothesis
until a batch has run.

## What the step is

Read a Google Drive document named by its `drive_id` in `Sources/manifest.jsonl`,
write it to `Sources/drive/<slug>.md` with provenance frontmatter, and record
the result back into the manifest row.

---

## Learnings

### 1. The document body never has to enter a model context — *measured*

`mcp__Google_Drive__read_file_content` does not return a large result inline. It
writes the result to disk and hands back a path:

```
/root/.claude/projects/<project>/<session>/tool-results/
    mcp-Google_Drive-read_file_content-<epoch_ms>.txt
```

The file is JSON with a single key: `{"fileContent": "<the whole document>"}`.

This is the single most useful thing found so far. Fetching 654 documents
through a context would have cost millions of tokens to move bytes between two
disks. Instead the agent makes one call, sees a path, and a console tool does
the rest.

### 1b. Only *large* results spill. Small ones land in the caller's context — *measured, and it cost me*

Learning 1 is true above a size threshold and false below it. A `.docx` whose
`fileContent` was ~30,000 characters came back **inline**, straight into the
calling context — roughly 10k tokens for one document.

This is the sharpest operational constraint in the whole fetch, and it inverts
the naive plan:

> **The main session must never fetch.** Every document below the spill
> threshold enters its context in full. At 654 documents this is millions of
> tokens spent moving bytes, which is precisely what learning 1 appeared to
> have solved.

Fetching is therefore always delegated to a subagent, whose context absorbs the
inline case and is discarded afterwards. The subagent reports counts, never
content.

Consequence for the tool: `land` cannot assume a spill file exists. It needs a
path for content that arrived inline — `--stdin` — so a subagent can pipe what
it received without the main session ever seeing it.

*Discovered by doing it wrong:* fetching
`AEGIS Singularität jenseits Entropiegleichung .docx` directly, which put the
whole document into the session that was trying to avoid exactly that.

### 2. The spill arrives as an *error*, not a result — *measured*

The call reports `result (78,383 characters) exceeds maximum allowed tokens`.
The path is inside that message. So the good path looks like a failure, and any
runner must read the error rather than treat it as one.

Consequence for the workflow: a fetch loop cannot use "did the call succeed" as
its signal. The reliable signal is *"is there a new spill file"*, which is what
`scripts/sources.py land` uses.

### 3. The spill filename is not predictable — *measured*

It carries a millisecond timestamp. `land` therefore takes the newest spill
under `/root/.claude/projects` by mtime rather than constructing a name.

That works for sequential fetches and **breaks for concurrent ones** — two
parallel fetches race for "newest". Any parallel runner must pass `--spill`
explicitly with the path from its own call's error message.

### 4. The manifest lies about size, by 2.4× — *measured*

Manifest `fileSize` for the test document: **31,909 bytes**. Actual Drive text
representation: **77,559 bytes**. Google Docs report an internal size unrelated
to their text export.

Consequence: never use manifest size to decide "small enough to read inline".
Expect nearly every document to spill.

### 5. Normalization is systematic, so it belongs on write — *measured*

In the one document: **673 of 852 lines** carried trailing whitespace, and the
file did not end with a newline. Both are converter behaviour, so both are
identical across all 654.

`land` normalizes CRLF→LF, strips trailing whitespace, and enforces exactly one
final newline — nothing else. Citations into these files are line ranges, and a
citation cannot be stable if the file is not. Normalizing later would change
every checksum already recorded.

Both hashes are kept: `sha256_raw` for what Drive returned, `sha256` for the
file as written.

### 6. Three noise classes are deliberately left alone — *measured*

Not cleanup but interpretation, so they stay:

- **333 backslash escapes**, 145 of them `\[` from citation markers like
  `\[1\]`, plus `\_` inside URLs. Converting `\[` → `[` could create accidental
  link syntax.
- **Bold used where headings belong**: 21 lines of `**Teil I: …**` against
  **one** real ATX heading in the whole document.
- **Collapsed mega-lines**: 9 lines over 1,000 characters, and the bibliography
  is a single 2,408-character line holding 19 URLs.

### 7. Flat headings will hurt section-level retrieval — *measured, unresolved*

Following from 6: a document with one real heading is flat to anything that
retrieves by section. If the wiki ever wants "the part of this source that
discusses X", that capability does not exist on this corpus as fetched.

This is the most consequential open question in this file. It is recorded and
not acted on, because promoting bold to headings is a guess about the author's
intent and the fix is cheap to apply later against stored `sha256_raw`.

### 8. What survives cleanly — *measured*

Tables came through as well-formed pipe tables (two of them, 6 and 16 rows,
4 columns each, with separator rows). No smart quotes, no tabs, no NBSP, no
BOM, no CR, no C0 controls, no HTML, UTF-8 throughout. No truncation: the
document ended mid-bibliography at source 19 of a list that reads complete.

### 9. Not all 680 are Google Docs — *measured from the manifest*

| format | rows | connector support |
|---|---:|---|
| `gdoc` | 590 | yes |
| `docx` | 45 | yes |
| `md` | 43 | **not in the supported list** |
| `pdf` | 1 | yes |
| `mp3` | 1 | **no** |

The connector's documented mime types cover Docs, Slides, Sheets, PDF, Word,
Excel, PowerPoint, OpenDocument and images. `text/markdown` and audio are absent.
So **44 rows need a different path or an explicit decision** — and none of them
has been tried.

### 10. The manifest's deduplication is incomplete — *measured*

**55 duplicate titles**, but only **2** rows marked `T0-duplicate` and only 2
carrying `duplicate_of`. Slugs are unique (0 collisions), so the export will not
overwrite anything — but it will fetch the same content repeatedly under
different slugs.

Seen directly in `theorie-physik`: *"AEGIS Singularität jenseits
Entropiegleichung .docx"* and *"AEGIS Singularität jenseits Entropiegleichung
Kopie.docx"* are adjacent rows, neither marked as a duplicate of the other.

`sha256_raw` makes this detectable after the fact: two rows with the same raw
hash are the same document. That check costs nothing once a batch has landed.

---

## What the tool must handle

Each item traces to a numbered learning.

- Take the newest spill by mtime, and accept an explicit `--spill` for parallel
  use (3).
- Parse `{"fileContent": …}` rather than treating the file as text (1).
- Normalize on write, mechanically only, and record both checksums (5, 6).
- Draw the slug and all frontmatter from the manifest row, never from the
  document (so provenance cannot drift).
- Write the manifest row back — `export_path`, `sha256`, `sha256_raw`,
  `exported_at` — or the inventory stays blind (this was missing from the
  hand-run).
- Refuse to overwrite an existing file without `--force`.
- Report a file the manifest does not claim, and a row whose file has gone
  (`check`).
- **Untried:** `docx`, `pdf`, `md` and `mp3` rows (9); duplicate detection by
  `sha256_raw` (10); rate limiting at volume.

## What stays judgement

- **Which documents are worth fetching.** Tier and category are the dials; the
  choice is the author's.
- **Whether bold-as-heading becomes real headings** (7). A guess about intent,
  applied to 654 documents at once, is exactly the kind of silent rewrite that
  the normalization rule exists to prevent.
- **What to do with a truncated document.** None seen yet; when one appears it
  needs a person, because the tool cannot know what is missing.
- **Whether two same-hash documents are one source or two contexts** (10).

## Measurements

*All 2026-09-16, one document (`argus-chronist-der-wandlung`, `charaktere`, T3-work).*

| | |
|---|---|
| manifest-reported size | 31,909 bytes |
| Drive text returned | 77,559 bytes |
| spill file on disk | 79,023 bytes (JSON envelope included) |
| landed file after normalization | 75,840 bytes · 9,945 words · 852 lines |
| lines with trailing whitespace, before | 673 of 852 |
| lines with trailing whitespace, after | 0 |
| subagent wall clock, one document | ~108 s including tool loading |
| corpus landed | 27 of 680 (3.8 %) |
| LLM cost | none — no model reads the content |

Predicted from these, unverified: 654 remaining × ~77 KB ≈ **50 MB** of
markdown, against the ~21 MB the manifest's own sizes would suggest.
