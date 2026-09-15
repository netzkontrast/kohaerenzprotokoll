# Sources — raw, immutable evidence layer

The 693 Google-Drive documents listed in
[Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md](../Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md)
land here as **markdown exports**, one file per document, and are never edited
afterwards (the Karpathy rule: the LLM reads raw sources, it does not write
them). None of them is canon — `Canon/` stays the normative corpus; everything
here is research the wiki (`Wiki/`, see `Plan/wiki/`) derives from.

| path | what | committed |
|---|---|---|
| `manifest.jsonl` | one line per document: `drive_id`, `title`, `slug`, `category`, `tier`, `format`, `index_date`, `byte_equal_copies`, plus export fields (`export_path`, `sha256`, `exported_at`, `duplicate_of`) filled by the fetch step | yes |
| `drive/<slug>.md` | markdown export (Drive MCP / `drive-markdown-converter`), UTF-8, LF | yes (decision pending, see concept §7) |
| `originals/` | binary originals (docx/pdf/mp3) | no (git-ignored) |

Rebuild the manifest from the index: `python3 scripts/source_inventory.py`
(`--check` exits 1 when stale; `--stats` prints tier/category/format counts).
Tiers: `T0-duplicate` (byte-equal copy of another export), `T1-superseded`
(older version of a later document), `T2-theory` (external science),
`T3-work` (work-related), `T4-out-of-scope`. T0/T1 are assigned after export
by hash and near-duplicate clustering; T2/T3/T4 come from the index sections.

Write access to this directory is meant to be denied for the agent
(`.claude/settings.json` → `permissions.deny`: `Write(Sources/**)`, `Edit(Sources/**)`);
only the fetch script and the inventory script write here.
