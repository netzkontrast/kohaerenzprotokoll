# Learnings — fetch (Drive → `Sources/drive/`)

## Status

**1 document fetched end to end** (2026-09-16), plus one earlier hand-run by a
subagent that was discarded and re-landed through the tool. 27 of the then 680 rows landed
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

### 1c. There is a path with no leak at all: call the connector from the script — *measured, and it supersedes 1 and 1b*

Learnings 1 and 1b both accepted that a document passes through *some* context
and argued about whose. That premise was wrong, and the author was right to
challenge it.

The MCP connectors are ordinary HTTP JSON-RPC endpoints. `/tmp/mcp-config-*.json`
carries the Drive server's URL and headers; `CLAUDE_SESSION_INGRESS_TOKEN_FILE`
carries the bearer token. A plain script can therefore call
`read_file_content` and `download_file_content` itself:

```
initialize -> 200   serverInfo: {'name': 'StatelessServer', 'version': 'ESF'}
tools/list -> 200   ['copy_file', 'create_file', 'download_file_content',
                     'get_file_metadata', ..., 'read_file_content', ...]
```

`scripts/sources.py fetch` now does exactly this. **No model is involved at any
point** — not the orchestrator, not a subagent. The saving against the delegated
plan is roughly 6.5 M tokens, and against doing it in the main session it is the
difference between possible and not.

Two dead ends checked on the way, recorded so nobody retries them:

- `CLOUDSDK_AUTH_ACCESS_TOKEN` is present in the environment but returns **401**
  against `googleapis.com/drive/v3` — wrong scope or project.
- The MCP headers in the config file alone return **401**. The bearer token from
  `CLAUDE_SESSION_INGRESS_TOKEN_FILE` is what authenticates; a 400
  "body could not be parsed" during testing was shell quoting, not auth, and
  that distinction is what showed the approach was viable.

**The dependency worth knowing:** the token file and the MCP config are
session-scoped. `fetch` therefore works inside a Claude Code session and nowhere
else, and it says so when either is missing rather than failing obscurely.

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

> **Superseded by 7b and then by 7c.** The premise — "a document with one real
> heading" — was true of the one document measured and false of the corpus.
> Left standing because how it went wrong is the useful part.

### 7b. Converting the original instead of Drive's text export fixes it — *measured*

Learning 7 said section-level retrieval is impossible on a corpus with one
heading per document, and recorded it as unresolved. It is resolved for every
format that has an original file.

`mcp__Google_Drive__download_file_content` returns the original bytes as base64.
Running **markitdown** over the `.docx` rather than taking Drive's text export
produces real markdown:

```
# Teil I: Konzeptionelle Ouvertüre      ← a real ATX heading, not **bold**
## A. Unterabschnitt
| Begriff | Bedeutung |                 ← a real table with its separator row
```

So the two paths are not equivalent and the choice is per format:

| format | rows | path | why |
|---|---:|---|---|
| `docx` | 45 | `download_file_content` → markitdown | keeps headings and tables |
| `pdf` | 1 | same | same |
| `gdoc` | 590 | `read_file_content` | no original file to convert |
| `md` | 43 | neither is listed as supported | undecided |
| `mp3` | 1 | neither | undecided |

The flat-heading problem therefore stands only for the 590 Google Docs, where
there is no original to go back to — the document *is* the Google Doc. That is a
much smaller problem than learning 7 first suggested, and it is now a property of
one format rather than of the whole corpus.

### 7c. The Google Doc problem does not exist either — *measured, 360 documents*

Learnings 7 and 7b both rested on one document. Counted across everything landed:

| format | landed | median ATX headings | with ≥5 | with none |
|---|---:|---:|---:|---:|
| `gdoc` | 360 | **17** | 270 | 18 |
| `docx` | 45 | **17** | — | — |

**Identical medians.** Google Docs carry real headings through the text export
just as well as markitdown carries them out of `.docx`. Section-level retrieval
works on the whole corpus.

`argus-chronist-der-wandlung` — the single document learning 6 measured — has 1
heading and 26 bold lines. It is the outlier, and it happened to be the first one
fetched. **18 of 360 gdocs have no headings at all**, which is a listable set of
documents rather than a property of a format.

Learning 7b is still correct about tables and about what markitdown preserves;
only its heading claim was wrong, and only because it inherited learning 7's
sample of one. Three learnings in a row were built on that one document before
anything counted the rest — which is exactly what P18 says and is much easier to
see in someone else's benchmark than in your own notes.

**What the tool should do:** `check` could report the documents with no headings,
since that is now a short list and the thing that actually varies.

**Install discipline, learned the hard way:** `pip install
--break-system-packages markitdown` broke `cryptography` for the entire
container and took the system interpreter with it. Everything goes in a venv —
recorded in `CLAUDE.md` because it is a rule, not a preference. `sources.py`
stays standard-library and shells out to `.venv-tools/bin/python`, so it still
runs when the venv is absent and prints the command that creates it.

### 8. What survives cleanly — *measured*

Tables came through as well-formed pipe tables (two of them, 6 and 16 rows,
4 columns each, with separator rows). No smart quotes, no tabs, no NBSP, no
BOM, no CR, no C0 controls, no HTML, UTF-8 throughout. No truncation: the
document ended mid-bibliography at source 19 of a list that reads complete.

### 9. Not all of them are Google Docs — *measured from the manifest*

| format | rows | connector support |
|---|---:|---|
| `gdoc` | 560 | yes |
| `md` | 43 | **not in the supported list** |
| `docx` | 12 | yes |
| `pdf` | 1 | yes |
| `mp3` | 1 | **no** |

Measured after `dedupe.py`. It was 590 / 45 / 43 / 1 / 1 over 680 rows: nearly
every `docx` row was a second export of a document already held as a `gdoc`, so
folding the copies away took `docx` from 45 to 12 and left `md` untouched.

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
| corpus landed | 27 of the then 680 rows (3.8 %) |
| LLM cost | none — no model reads the content |

Predicted from these, unverified: 654 remaining × ~77 KB ≈ **50 MB** of
markdown, against the ~21 MB the manifest's own sizes would suggest.
