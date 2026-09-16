# Sources — raw, immutable evidence layer

The index
[Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md](../Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md)
lists 693 Google-Drive documents. The 13 appendix rows are `T4-out-of-scope`
and excluded from the manifest by default (D-W9), so `manifest.jsonl` carries
**680 records**. Each of them lands here as a **markdown export**, one file per
document, and is never edited afterwards (the Karpathy rule: the LLM reads raw
sources, it does not write them). None of them is canon — `Canon/` stays the
normative corpus; everything here is research the wiki (`Wiki/`, see
`Plan/wiki/`) derives from.

| path | what | committed |
|---|---|---|
| `manifest.jsonl` | one line per document: `drive_id`, `title`, `slug`, `category`, `tier`, `format`, `index_date`, `byte_equal_copies`, plus the export fields (`export_path`, `sha256`, `exported_at`, `truncated`) filled by the fetch step and the dedup fields (`duplicate_of`, `superseded_by`) set by `scripts/source_dedup.py` | yes |
| `drive/<slug>.md` | markdown export (Drive MCP / `drive-markdown-converter`), UTF-8, LF | yes (D-W1) |
| `originals/` | binary originals (docx/pdf/mp3) | no (git-ignored) |

Rebuild the manifest from the index: `python3 scripts/source_inventory.py`
(`--check` exits 1 when stale; `--stats` prints tier/category/format counts;
`--include-out-of-scope` keeps the 13 appendix rows). Slugs are disambiguated
over all 693 rows before the appendix is dropped, so the 680 surviving slugs
never change. A rebuild carries the export and dedup fields of the existing
manifest over by `drive_id`, so `--check` keeps passing after exports.

Tiers: `T0-duplicate` (byte-equal copy of another export), `T1-superseded`
(older version of a newer document), `T2-theory` (external science),
`T3-work` (work-related), `T4-out-of-scope`. T0/T1 are assigned after export
by hash and near-duplicate clustering (`scripts/source_dedup.py`); T2/T3/T4
come from the index sections.

Write access to this directory is meant to be denied for the agent
(`.claude/settings.json` → `permissions.deny`: `Write(Sources/**)`, `Edit(Sources/**)`);
only the fetch procedure below, the inventory script and the dedup script write here.

## Fetch procedure

One document, end to end. The manifest record is identified by its `drive_id`
and its `slug`; both come from the index and are never re-derived.

1. **Locate the file in Drive** (Drive MCP): `get_file_metadata` with the
   record's `drive_id` confirms the title and mime type; `search_files` by
   title is the fallback when an id has moved.
2. **Read the content**: `read_file_content` for Google Docs (returns the
   markdown rendering); `download_file_content` for `.md` and `.txt` files
   (the raw bytes, base64 — `read_file_content` would escape their markdown)
   and for `docx`, `pdf` and other binaries, which are converted to markdown
   with the `drive-markdown-converter` skill. Binaries go to `originals/`
   (git-ignored), never into `drive/`. A result above the harness limit is
   saved as a JSON file (`{fileContent: …}` or `{content: <base64>, …}`);
   the helper in step 4 reads either shape.
3. **Write `Sources/drive/<slug>.md`** as the pure markdown body: UTF-8, LF,
   no frontmatter and no header line — every piece of metadata lives in the
   manifest, so a citation `^[Sources/drive/<slug>.md:L-L]` points at source
   text only.
4. **Fill the export fields** of the manifest record:
   - `export_path`: `Sources/drive/<slug>.md`
   - `sha256`: of the file bytes (`sha256sum Sources/drive/<slug>.md`)
   - `exported_at`: the UTC date of the export, `YYYY-MM-DD`
   - `truncated`: `true` when the read tool cut the content (a size cap, a
     "content truncated" notice, a body that ends mid-sentence against the
     Drive metadata size) or when the file is under 200 bytes; otherwise `false`

   Steps 3 and 4 are one command: `python3 scripts/source_export_mark.py
   --slug <slug> --from-json <saved result>` (or `--from-text <file>`)
   normalises the body (UTF-8, LF, trailing whitespace stripped, one final
   newline), writes the file, hashes it and rewrites only that manifest
   record; `--truncated` records an incomplete export and the helper refuses
   a body under 200 bytes or with a truncation notice unless the flag is
   given. The markdown rendering of a Google Doc can stop a few characters
   before the end of its last line: `download_file_content` with
   `exportMimeType: text/plain` returns the complete line, and `--tail-from
   <plain.txt>` appends exactly the verified remainder (exit 4 when the last
   line is not a prefix of one plain-text line).
5. **Run the dedup pass**: `python3 scripts/source_dedup.py` hashes every
   non-truncated export, marks byte-equal copies `T0-duplicate`
   (`duplicate_of`) and older drafts `T1-superseded` (`superseded_by`).
   `--dry-run` previews, `--check` exits 1 when the manifest would change.
6. **Verify the manifest**: `python3 scripts/source_inventory.py --check`
   prints `manifest up to date` (the export and dedup fields are carried over;
   only index-derived fields can make it stale).
7. **Index the text**: `python3 scripts/wiki_fts.py build` adds the new export
   to the BM25 candidate finder.

A truncated export (`truncated: true`) is **never ingested** into `Wiki/`: the
dedup pass skips it, the ingest refuses it, and it is re-fetched — in heading
chunks when the document is larger than one read — until the file is complete
and `truncated` is set back to `false` with a fresh `sha256`.
