# qmd — the full command and flag surface

**`qmd <command> --help` prints the global help, not the command's.** The flags
below were read out of `dist/cli/qmd.js` in the installed package and checked by
running them. Where a flag is undocumented in the help text, it says so.

## Searching

| command | what it runs | cost here |
|---|---|---|
| `qmd search <q>` | BM25 full-text only | **0.24s**, no model |
| `qmd query <q>` | expansion model → BM25 + vector → reranker | **14.5s** uncached, CPU, no GPU |
| `qmd vsearch <q>` | vector similarity only | needs embeddings; returns nothing without them |

Shared flags: `-c <collection>` · `-n <count>` · `--json` · `--files` ·
`--explain` · `--min-score <f>` · `--max-bytes <n>` · `--format <fmt>` ·
`--xml` · `--glob <pattern>`

- **`--files`** — one compact line per hit: `#docid,score,qmd://path,"context"`.
  The cheapest machine-readable form.
- **`--explain`** — prints the title, the collection context and `Score: NN%`
  above each hit.
- **`--json`** — fields per hit: `docid`, `score`, `file`, `line`, `title`,
  `context`, `snippet`. `score` is a real value; `file` is a `qmd://` ref.
- **`--no-rerank`** (undocumented) — skips the reranker in `query`. It does
  **not** skip the expansion model, so it is not the fast path; `search` is.
- **`--intent <text>`** (undocumented) — the reranker's intent parameter. Note
  that a collection's *context* never reaches the model; this is the field that
  does.

### Query grammar

A query is either a single expand query or a document of typed lines. The two
cannot be mixed.

```
intent: what I am actually after
lex:    exact tokens, BM25
vec:    a phrase to match by meaning
hyde:   a hypothetical answer, embedded
```

`lex:` supports `"exact phrases"` and `-negation`. A bare single-line query is
implicitly `expand:`.

## Reading

| command | what it does |
|---|---|
| `qmd get <ref>[:from[:count]]` | one document, line-numbered, with the collection context above it |
| `qmd multi-get <glob or a,b,c>` | several at once |
| `qmd ls [collection[/path]]` | what is indexed, with size and mtime |

Flags: `--line-numbers` / `--no-line-numbers` · `--full-path` · `--from <n>` ·
`--max-bytes <n>` · `--format <fmt>` · `--xml`

A ref is `qmd://<collection>/<path>`, exactly as a search result prints it.

## Collections and context

```bash
qmd collection list                       # names, patterns, file counts, age
qmd collection show <name>                # path, pattern, include flag, contexts
qmd collection add <path> --name <n> --mask <globs>
qmd collection remove|rename <name>
qmd collection exclude <name>             # drop from default queries
qmd context add "qmd://<collection>/" "text"
qmd context list|rm
```

**`--mask` is the flag that restricts a collection; `--pattern` is ignored.** A
collection rooted at `.` without a mask indexes `Legacy/` and the vendored
packages — 1,382 files, tried and removed.

**In this project none of these are run by hand.** The collections live in the
committed `.qmd/index.yml`; see `setup.md`.

**A collection's context never reaches the reranking model.** Traced through
`addContext` → `getContextForFile` → `store.rerank()`: it is stored per
collection and path prefix, attached to results as metadata, and printed above
`get` output. It is documentation for a reader, which is not what „context"
suggests.

## Index maintenance

| command | notes |
|---|---|
| `qmd init` | **never run this here** — it overwrites the committed config |
| `qmd update [--pull]` | re-index; `--pull` runs `git pull` first |
| `qmd embed [-f] [-c <name>]` | build vectors. `--timeout <min>` defaults to 30, `0` disables |
| `qmd pull [--refresh] [--progress]` | download the three GGUF models |
| `qmd status` | documents, vectors, pending, collections |
| `qmd cleanup [--dry-run]` | drop inactive docs and orphans, compact FTS, vacuum |
| `qmd doctor` | device diagnostics — says whether a GPU is in use |
| `qmd trust [list\|revoke]` | approve a config's hooks, out-of-project paths or non-default models |

`qmd embed` also takes `--max-docs-per-batch` and `--max-batch-mb` to cap memory.
A small embedding model (≲350 MB) was measured by qmd at ~2048 tokens of
embedding context; Qwen3-Embedding-0.6B-Q8 at ~640 MB needs roughly 1190 MB per
batch.

## Skills, MCP, benchmarks

```bash
qmd skills list|get|path      # skills bundled IN the package: `qmd` and `release`
qmd skill show|install        # the package's own agent skill
qmd mcp [--http --port --host --daemon]
qmd bench <fixture.json> [--json] [-c <collection>]
```

**`qmd skill install` would overwrite this project's own `qmd` skill**, so
`setup_qmd.sh` does not run it. Read `qmd skill show` when you want the
package's version-matched text.

The package's own `references/mcp-setup.md` was removed from this skill rather
than kept: it instructs `npm install -g`, a hand-run `collection add` and an MCP
client, and all three contradict this project — the package is local, the
collections come from the committed config, and MCP is decided against. Leaving
it would have someone re-create by hand the drift the committed config fixes.

`qmd mcp` exposes **four** tools — `query`, `get`, `multi_get`, `status`. No
`collection`, `context`, `embed` or `bench`. **This project decided against
MCP**: a skill whose job is to describe every step should name commands a person
can type and disagree with, and MCP would hide the four things it does not
expose behind a surface that looks complete.

### `qmd bench`

An IR evaluation harness over **four backends** — `bm25`, `vector`, `hybrid`,
`full` — reporting `precision_at_k`, `recall`, `recall_at_1/3/5`, `mrr`, `f1`,
`latency_ms`, plus the expected files it missed.

```json
{ "description": "...", "version": 1, "collection": "sources",
  "queries": [{ "id": "...", "query": "...",
                "type": "exact|semantic|topical|cross-domain|alias",
                "description": "...", "expected_files": ["..."],
                "expected_in_top_k": 1 }] }
```

A failing backend is scored zero rather than erroring — **so a run without
embeddings measures their absence and not the backends.** No fixture exists yet;
the wiki's question pages and conflict records already contain „a search finds
this in `<slug>`" claims and are most of one.
