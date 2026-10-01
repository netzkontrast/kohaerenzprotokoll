# Task — one gold candidate list

You read ONE research document of the Kohärenz-Protokoll corpus and write its candidate list:
steps 1–3 of `ingest`, nothing after. Engineering prose is English; terms stay as the document
writes them. Work from the repository root `/home/user/kohaerenzprotokoll`.

## Read only this

1. `Plan/briefings/extract.md` — procedural knowledge about German Drive exports.
2. `.agents/skills/ingest/references/german.md` — what a pattern misses in German.
3. The document, through `python3 scripts/read.py <slug>` (in chunks with `--from N --to M`).

Never open `Wiki/`, `NOW.md`, `Sources/terms/`, `Sources/notes/`, another document's
`Plan/runs/`, or any script's source. You know nothing about the wiki; that is the point.

## Steps

```bash
python3 scripts/runlog.py <slug> start read
python3 scripts/capture.py <slug>            # writes 01-profile.txt and 02-probes.txt
```

Read the whole document, first line to last. **While reading, write
`Plan/runs/<slug>/03-candidates.md`**, one `- term` per line, before any count. The rule
(decision 012) — list every candidate term of this document:

- what it names in the novel's world (figures, places, systems, artifacts, events, numbers used as names);
- the words it uses as its own terms (coinages, labels, section concepts it defines or relies on);
- the borrowed concepts it applies (theories, authors' concepts, clinical or physical terms), under a `## lens` heading.

Write each surface exactly as the document writes it after export (keep `\_`, `\&`); a
joined pair `A (B)` or `A/B` is listed whole and then by each name, unless the parenthesis
is a description. Before a multi-word phrase goes on the list, ask
`python3 scripts/read.py <slug> --find "<phrase>"`. Group headings (`## …`) are
organisation only. **Observations go in paragraphs, never as `- ` bullets**, and never use a
comma inside a term line.

The first line of the file is exactly:

    written_by: gold subagent (Sonnet), 2026-09-30, while reading, before any count

then one sentence on how the list was made.

When the list is complete, and only then:

```bash
python3 scripts/runlog.py <slug> end read
python3 scripts/capture.py <slug> --count     # writes 04-counts.txt and counts.json — freezes the list
python3 scripts/gold.py <slug>                # must say GOLD
```

**After the count, never change `03-candidates.md`.** A zero in the count is recorded, not
fixed: in your report name each zero and what it is (an inflection, export damage, or a term
the document lacks). If `gold.py` fails `of the document`, report it; do not edit the list.

Write nothing else: no census, no note, no `05-verify.txt`. Never run `git`, `reconcile.py`,
`census.py`, `wiki_index.py`, `link.py` or `readings.py`.

## Report

The document in two sentences; how many candidates; the zeros and what each is; the
`gold.py` verdict line; anything the briefing did not anticipate.
