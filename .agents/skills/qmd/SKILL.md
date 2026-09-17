---
name: qmd
description: Search and read this project's German corpus with qmd — which collection answers which question, why search is 0.24s and query is 14.5s, and the rule that a search result is never a number. Use when looking for a passage, a term, a decision already made, or when a search returns less than it should.
allowed-tools: Bash(qmd:*), Bash(scripts/setup_qmd.sh:*), Bash(python3 scripts/qmd_coverage.py:*)
---

# qmd, for this corpus

`qmd` indexes this project's markdown and answers a German phrase with a file
and a line. It is a **place to look**. Every number that goes into a page or a
learning comes from `corpus.py`, `duplicates.py` or a count — never from a
search result. That rule is in `CLAUDE.md` and it is the one this skill exists
to keep.

For the package's own version-matched instructions: `qmd skill show`.
For the full command and flag surface, read `references/commands.md`.
For how the setup is built and restored, read `references/setup.md`.

## Pick the collection first, the query second

Seven collections, named for **purpose** rather than folder.

| ask it when you want | collection |
|---|---|
| a passage in a source document | `sources` |
| what a term page, conflict or question already says | `wiki` |
| every candidate term one document proposed | `census` |
| what one document was read as saying, quoted | `notes` |
| concept notes, decisions, learnings, run artifacts | `plan` |
| **what has already been decided, and why** | `decisions` |
| any layer, when you do not know which | `all` |

`decisions` and `all` are **excluded from default queries** because they overlap
the others — name them explicitly with `-c`.

`decisions` is the one worth reaching for first: it spans the reconciliation
records, conflict records, question pages, `Plan/decisions/` and the judgement
ledger. Eight reconciliation records alone are ~950 lines, and a hit plus
`qmd get` reads a dozen.

## Three search commands, and the difference is not small

```bash
qmd search "blinder Fleck kategoriale Unfähigkeit" -c sources    # 0.24s, BM25, no model
qmd query  "blinder Fleck kategoriale Unfähigkeit" -c sources    # 14.5s, expands + reranks
qmd vsearch "Wächter am Tor" -c wiki                             # vectors only
```

**Use `search` by default.** It is BM25, runs no model, and for a corpus of
coined German compounds an exact term is usually what you have.

`query` runs a 1.7B expansion model and a 0.6B reranker on CPU — this container
has no GPU and says so. **14.5s, measured on a query never asked, twice.** A
repeated query returns in 0.24s from the index's `llm_cache`, which is how „about
0.2s" once got written down as a general claim. Never put `query` in a loop.

`vsearch` needs embeddings. `scripts/setup_qmd.sh --check` reports how many are
pending; while any are, `vsearch` returns „No results found" **with a warning
and exit 0** — it looks like an answer.

## Writing a query for German

The corpus is full of coined compounds, and that changes what works:

- **Lowercase is fine.** Matching is case-insensitive.
- **Do not grep for capitalised words** to find terms — German capitalises every
  noun, so the signal is nil.
- **A compound is its own token.** `Entropie` does not match `Entropiegewinn`;
  they are separate tokens in the index. Search for the compound you mean, or
  for both.
- **Structured queries** let you say which leg does what:

```bash
qmd query $'lex: Kern-Welten Guardians\nvec: wer bewacht welche Welt'
qmd query $'hyde: Jeder Guardian ist einer Kernwelt zugeordnet.'
```

`lex:` is BM25, `vec:` is vector similarity, `hyde:` embeds a hypothetical
answer. **`vec:` and `hyde:` contribute nothing until embeddings finish.** A
plain single-line query is implicitly `expand:` and runs the expansion model.

## Read the hit, not the snippet

```bash
qmd search "Wächter" -c decisions -n 3
qmd get "qmd://decisions/Plan/runs/judgements.md:273:12"
```

`get <ref>:<from>:<count>` prints numbered lines, with the collection's context
above them. That is the loop worth learning: **search to find the line, `get` to
read a dozen lines around it** instead of the whole file.

`multi-get` takes a glob or a comma-separated list when you need several.

## From Python

```python
from qmd import search, get          # scripts/qmd.py
for hit in search("blinder Fleck", collection="sources"):
    doc = hit.document()             # subject.Document when the hit is a landed source
```

`scripts/qmd.py` parses `--json` once and resolves `qmd://collection/path` to a
real `Path` once. **A `Hit` says where to look and carries no claim about the
corpus**; `hit.document()` is the handoff back to the tools that measure.

## When a search returns less than it should

```bash
scripts/setup_qmd.sh --check       # package, config, collections, embeddings, coverage
python3 scripts/qmd_coverage.py    # non-zero if a directory is in no collection
qmd update                         # re-index after files change
```

**A file in no collection is absent from every search and nothing says so** — the
search just returns less and looks like it worked. That is why coverage is
checked rather than remembered.

Two more silent failures worth knowing:

- **Running `qmd` outside the project queries a different, empty index.** The
  config is found by walking up from the working directory. `cd` to the
  repository root first.
- **`.qmd/index.yml` is committed and `qmd init` overwrites it.** Never run
  `init` here. If the file is missing, it is a restore: `git checkout .qmd/index.yml`.

## What this skill will not do

- Turn a search result into a number. Ranked results are a place to look.
- Replace `Wiki/index.json` in reconciliation, which must stay
  `O(census) + O(judgement)` and never scan the corpus.
- Run `qmd bench` before embeddings exist — it would measure their absence, and
  score the `vector` and `full` backends near zero by construction.
