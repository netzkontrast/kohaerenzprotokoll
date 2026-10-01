# Task — one gold relation list

You read ONE research document of the Kohärenz-Protokoll corpus and write, while reading, what it
defines, what it sets against what, and what it says brings about what — in the vocabulary below.
This list is the gold that automated extractors are later scored against, so it must be your own
reading of the document and nothing else. Work from `/home/user/kohaerenzprotokoll`.

## Read only this

1. `Plan/briefings/extract.md` — procedural knowledge about German Drive exports.
2. The document, through `python3 scripts/read.py <slug> --from N --to M`, in chunks of at most 120 lines.

**Never open** `Plan/runs/<slug>/hyperextract/`, `Plan/hyperextract/`, `Wiki/`, `NOW.md`,
`Sources/terms/`, `Sources/notes/`, or any other file of `Plan/runs/`. Extractors have already
read this document; seeing what they found would make this list a copy of them instead of a
measure of them.

## What goes on the list

Three sections, in this order. A row cites the ONE file line that holds all of its surfaces as
whole words, and each surface is copied exactly as that line writes it (keep `\_`, `\&`; a short
noun phrase of at most six words, never a clause). Ask
`python3 scripts/read.py <slug> --find "<words>"` for the line when unsure.

**`## definitions`** — `- <term>  ^[Lnn]`. A line that defines, glosses or explains what a term
is: „X ist …“, „X bezeichnet …“, „unter X wird … verstanden“, „X, d. h. …“, „X (…)“ with an
explanation, a table row naming X with its description, or a heading followed by its defining
sentence (cite the line with the definition, and only if it also names the term). A line that only
uses the term, or says what it does or causes, is not a definition. Each defining line is its own row.

**`## contrasts`** — `- <source> | <type> | <target>  ^[Lnn]`, where the ONE line itself sets two
things against each other: „im Gegensatz zu“, „versus“/„vs.“, „einerseits … andererseits“,
„Spannung zwischen“, „nicht … sondern“, „statt“, „während … dagegen“, or a table row that sets them
in columns. Types:
- `contrasts_with` — set side by side as different;
- `in_tension_with` — held together as pulling apart;
- `opposes` — one works against the other;
- `complements` — a pair that needs both;
- `denies` — one is said not to be the other.

**`## causal`** — `- <cause> | <type> | <effect>  ^[Lnn]`, where the ONE line states the causal
step: führt zu, verursacht, löst aus, ermöglicht, verhindert, weil, daher, dadurch, erzwingt,
setzt voraus (or the English equivalents). Types:
- `causes` — one produces the other;
- `enables` — makes it possible;
- `prevents` — stops or blocks it;
- `triggers` — sets it off at a moment;
- `requires` — the effect cannot happen without the cause.

Never infer a relation from two lines, from nearness, or from what you know; never chain two
sentences. A relation the document reports from an outside source is still recorded — it is what
the line says. Be complete: every line that states one of these is a row, whether or not it
seems important.

## The file

`Plan/runs/<slug>/03-relations.md`, appended after each chunk. The first line is exactly

    written_by: gold subagent (Sonnet), 2026-09-30, while reading, blind to every extractor

then the three section headings with their rows. No other `- ` lines; observations, if any, go in
a paragraph at the end.

When the whole document is read:

```bash
python3 scripts/goldrel.py check <slug>     # every row parses and its line holds its surfaces
```

Fix what it names (a surface not on its line is usually a different form or the wrong line — ask
`read.py --find`), then

```bash
python3 scripts/goldrel.py freeze <slug>
```

After the freeze, never change the file. Write nothing else; never run `git`.

## Report

How many rows in each section; what `check` named before it held and what you changed; anything in
the document the vocabulary did not fit (a relation it states that none of the ten types names).
