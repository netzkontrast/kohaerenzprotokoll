# Every script, its surface, and what it leaves behind

The pipeline is scripts, not commands. This is the full surface; the loop that
orders them is in `SKILL.md`.

## The verb

```bash
python3 scripts/account.py <document|term|pair|corpus|order> [id]
```

One operation at several scales. `order` takes no id and answers whether the
pipeline's dependency order holds — it is the check that refuses to pass while
any document is half-processed.

## Per document

| command | writes |
|---|---|
| `read.py <slug> [--from N --to M]` | the document to stdout, each line prefixed `NNN\|` |
| `read.py <slug> --find "<words>"` | `^[Lnn]`, or a refusal naming the nearest lines — exit 1 |
| `capture.py <slug>` | `Plan/runs/<slug>/01-profile.txt`, `02-probes.txt`, `run.md` |
| `capture.py <slug> --count` | `04-counts.txt`, `counts.json` — refuses without `03-candidates.md` |
| `profile.py <slug>` | structural facts to stdout |
| `profile.py --frontmatter <slug>` | the census header, drawn from the manifest so no identifier is ever typed |
| `reconcile.py <slug>` | `Plan/runs/<slug>/reconcile-pre.json` and a printed classification |

`read.py` serves the same text in both directions and neither stores anything:
the numbers it prints are **file** lines, the ones a citation names, and `--find`
asks exactly the question `quotes.py` will ask later, through the same
`missing_part` on the same normalised line. So a citation `--find` produced
cannot fail the check. When it refuses it says why — the words are on no single
line, or they span two, which cannot be cited at all because the line number is
part of the claim.

`04-counts.txt` reports each term **twice** — standing alone, and including
compounds — because one number cannot answer it in German, and lists the
inflected surfaces found. A term at `0 word` is written differently here, not
absent.

## Corpus-wide

```bash
python3 scripts/corpus.py <count|timeline|cooccur|first|where|family|plan> <term>
python3 scripts/duplicates.py [--term T] [--threshold F] [--groups]
python3 scripts/dedupe.py [--apply]              # default is a dry run
python3 scripts/derive.py                        # apply every rule, cached by (sha256, rule VERSION)
```

`corpus.py` answers from the derived index without reading a document.
`duplicates.py --term` counts a term both ways, over files and over documents.

## Checks

```bash
python3 scripts/state.py [--prose|--check|--get KEY]
python3 scripts/quotes.py [FILE ...]
python3 scripts/judgements.py [--open|--render]
python3 scripts/qmd_coverage.py
python3 scripts/sources.py check
python3 scripts/selftest.py
python3 scripts/relations.py
python3 scripts/trainset.py
```

- `state.py` with no flag derives everything and writes `Plan/state.json`.
  `--prose` reads every `.md` outside `Legacy/` and fails on a stale number.
- `quotes.py` with no argument checks the repository; with a file, that file.
  It reports **unresolved** and **uncheckable** separately and never conflates
  them.
- `judgements.py` re-renders `Plan/runs/judgements.md` on every normal run, so
  the searchable copy cannot lag behind the `.jsonl` it derives from.
- `relations.py` derives the page graph from `[[slug]]` links, the orphans, the
  open statements harvested from every page's Open section, and `--unmarked`:
  where a page writes another page's term in prose and does not link it. A
  backticked `` `Term` `` names a term and is **not** a link (decision 005).
- `link.py` marks those, one link per page per target, and refuses to touch the
  frontmatter, code, a heading, a blockquote, anything inside „…", or any line
  carrying a `^[` citation. Dry run by default; `--apply` writes. Run
  `quotes.py` after — the first pass broke two quotations and that is how they
  were found.
- `selftest.py` runs the checkers against deliberate defects and asserts **which**
  one each reports. It cites a real landed document, so the whole resolution path
  runs: frontmatter, slug lookup, export unescaping, emphasis, blockquote
  wrapping, glued footnote numbers.
- `trainset.py` turns the ledger into examples and prints the `fold()` baseline
  live — never hardcoded, because it moves when the ledger grows.

## Fetching

```bash
python3 scripts/sources.py next --category <cat> --limit 5
# → mcp__Google_Drive__read_file_content per drive_id; it spills to a path
python3 scripts/sources.py land --drive-id <id> --consume
python3 scripts/sources.py status
```

**Never open the spill file.** `land --consume` parses it, normalises, writes
`Sources/drive/<slug>.md`, records both checksums and verifies. No model reads a
document's bytes in this step.

`next` filters against `Sources/duplicates.jsonl` by `drive_id`, so a folded
document is never offered again.

## Substrate

`subject.py` is the one place the corpus becomes addressable — every other
script asks it for a document, its body and its frontmatter offset. It raises on
a landed row whose file is gone rather than skipping it, because a silently
shrinking corpus makes every count quietly wrong.

`wiki_index.py` derives `Wiki/index.json` from page frontmatter. `reconcile.py`
answers by lookup against it and never scans the wiki.

`qmd.py` is the Python handoff to search: `search()`, `vsearch()`, `get()`,
`update()`, `collections()`, and `Hit.document()` back to `subject.Document`.

## Setup

```bash
scripts/setup_qmd.sh [--check]
```

Installs what git cannot carry: the npm package, the three GGUF models, the
SQLite index and the embeddings. The configuration itself is committed at
`.qmd/index.yml`.
