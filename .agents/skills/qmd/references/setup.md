# The qmd setup: what is committed, what is rebuilt, and why

## One configuration, in one file, in git

`.qmd/index.yml` **is committed.** qmd is built for this — its own `trust.ts`
says:

> „A project-local `.qmd/index.yml` arrives with a `git clone`, and
> `findLocalConfigPath` adopts it automatically for any command run inside the
> tree."

So the collections, their contexts and the three model URIs travel with the
repository, and a clone is configured before its first command.

**It used to be the other way round**, and that was the defect: `.qmd/` was
git-ignored entirely and `setup_qmd.sh` rebuilt the collections from
`collection add` arguments. One configuration in two places — the shell argument
and the YAML qmd wrote from it — free to drift, with the authoritative copy
untracked. The stale contexts printed above search results were the visible
symptom.

What stays git-ignored: `index.sqlite` (~100 MB, derived), its `-wal`/`-shm`,
and the embed lock.

### The file

```yaml
global_context: >          # prepended to what a reader sees about the project
editor_uri_template: …     # optional, for clickable links
models:
  embed:    hf:ggml-org/embeddinggemma-300M-GGUF/embeddinggemma-300M-Q8_0.gguf
  rerank:   hf:ggml-org/Qwen3-Reranker-0.6B-Q8_0-GGUF/qwen3-reranker-0.6b-q8_0.gguf
  generate: hf:tobil/qmd-query-expansion-1.7B-gguf/qmd-query-expansion-1.7B-q4_k_m.gguf
collections:
  <name>:
    path: Sources/drive        # RELATIVE — see below
    pattern: "**/*.md"
    ignore: []                 # optional
    includeByDefault: false    # optional; omit for true
    update: "…"                # a shell hook — NOT used here, see the gate
    context:
      "": "what this collection is for"
      "/subdir": "what that subdirectory is for"
```

**Paths must be relative.** qmd resolves a project-local config's relative paths
against the directory containing `.qmd`, not against the working directory — so
a relative path works in every clone, and the absolute path a `collection add`
writes works only on the machine that ran it.

### Three model slots, pinned to qmd's own defaults

| slot | model | size |
|---|---|--:|
| `embed` | `embeddinggemma-300M-Q8_0` | ~300 MB |
| `rerank` | `Qwen3-Reranker-0.6B-Q8_0` | ~610 MB |
| `generate` | `qmd-query-expansion-1.7B-q4_k_m` | ~1.2 GB |

**The small embedding model is already qmd's default** — the alternative,
`Qwen3-Embedding-0.6B`, is roughly twice the size. Naming them explicitly costs
nothing and means a future qmd changing its default cannot silently invalidate
every vector.

They live in `~/.cache/qmd/models`, **outside the repository**, so a fresh
container has none. Without the embedding model `qmd embed` cannot run, and
every vector search then returns „No results found" with a warning and exit 0 —
it looks like an answer.

### The approval gate, and how to stay out of it

qmd gates three fields in a project-local config, because each can reach outside
the project: `update:` hooks, a `collections.*.path` pointing outside the tree,
and a non-default model URI. An unapproved config makes every clone prompt
before its first query, and a non-interactive caller gets `skip` rather than a
prompt — so an agent would silently run without them.

**This config arms none of it**: every path is inside the project, all three
models are the built-in defaults, and there are no hooks. If you add any of the
three, `qmd trust` is the approval and the digest re-arms the moment it changes.

## What a fresh clone still needs

Four things git cannot carry:

| | size | command |
|---|--:|---|
| the npm package | ~50 MB | `npm install --prefix .tools-node @tobilu/qmd` |
| the three models | ~2.1 GB | `qmd pull` |
| the SQLite index | ~100 MB | `qmd update` |
| the embeddings | in the index | `qmd embed --timeout 0` |

```bash
scripts/setup_qmd.sh            # all four, plus the PATH shim
scripts/setup_qmd.sh --check    # report what is missing, change nothing
```

`--check` reports the package, the committed config, the PATH shim, the agent
skill, **whether the index's collections match the config's**, how many
embeddings are pending, and coverage. Both sides of the collection comparison
are derived from the file: the version that carried the number `6` reported
„7 of 6" the first time a collection was added.

### The PATH shim

The skill declares `allowed-tools: Bash(qmd:*)` and the package lives in the
git-ignored `.tools-node/`, so `qmd` is not on `PATH` in a fresh container.
Without a shim the skill fails with „command not found", **which reads like the
tool is broken rather than absent.** `setup_qmd.sh` writes
`/usr/local/bin/qmd`, which resolves the project-local binary and otherwise
prints how to install it.

### `qmd skill install` is deliberately not run

It would overwrite this project's own `qmd` skill with the package's bootstrap.
The bootstrap is still worth reading — `qmd skill show` prints it — but it
teaches the tool, and this skill teaches the corpus.

## Embedding, and what it costs

`qmd embed` is CPU-only here; `qmd doctor` reports the device. Progress is
visible in `qmd status` as `Vectors:` against `Pending:`. The default
`--timeout` is 30 minutes and will stop a large run part-way — pass
`--timeout 0`.

Partial embeddings are not an error state and not a working one either:
`vsearch` returns nothing, and `query`'s vector leg contributes nothing, while
both exit 0.
