# Brief — writing a new term page from the 2026-09-25 scan

The ten scans in this folder named terms the wiki has no page for. A page writer
turns one such term into `Wiki/candidates/<slug>.md`. Working directory:
`/home/user/kohaerenzprotokoll`. Read `Wiki/README.md` and two existing pages
(`Wiki/candidates/erason.md`, `Wiki/candidates/truth-rotation.md`) first, and
copy their shape exactly.

## Which documents a page may quote

Only these thirty — the twenty read documents (every file in `Sources/notes/`)
and the ten scanned (every `<slug>.md` in this folder except the briefs). Never
another landed document, never `Legacy/`. Find every one of the thirty that uses
the term: `grep -il "<surface>" Sources/drive/<slug>.md` for each, and try the
term's other surfaces (hyphenation, English/German, abbreviation).

## A reading, not an occurrence

A page is made of readings: what a document **says the term is or does**. A
document that only names it in a list, a title or a reference gives no reading —
leave it out, or record it in one line under `## Occurrences only` with its line.
If after gathering the term has fewer than one real reading, do not write the
page; report that instead. **A page created from an occurrence says nothing and
looks like it says something.**

## Rules that the checks enforce

- Canon prose is German and never translated. Quote exactly; write your own
  sentences in English.
- Every quotation is `„exact words“ ^[<slug>.md:Lnn]` — the reference names its
  document, always (a bare `^[Lnn]` is not allowed on a page). The line number
  comes from `python3 scripts/read.py <slug> --find "<exact words>"`, never from
  memory or from a scan. One quotation, one line; no ranges inside a quotation.
  A quotation containing quote marks is shortened so it contains none.
- One `## Reading — `<slug>`, <date>` section per document, in date order
  (date from `Sources/manifest.jsonl`, field `index_date`). Say the stance when it
  matters: premise, finding, verdict, restatement, a proposal (`[V]`), a lock (`[K]`).
- **Attributed and unmerged.** Where documents disagree, add
  `## Where the sources differ` and state each position with its source — then stop.
  Never say which is right, never say a conflict is settled, never let a date or
  a document's claim to be canon decide anything (decision 006). If the term
  touches an existing conflict (C1–C15 in `Wiki/conflicts/`), set `conflict:` to
  its id and say how, in one line.
- Link other pages as `[[slug]]` or `[[slug|Surface]]` only where the prose
  already names the term, only to pages that exist in `Wiki/candidates/`, and
  once per page per term. Never link inside a quotation.
- Frontmatter, exactly these keys:
  ```
  ---
  term: <the dominant surface, as the documents write it>
  status: candidate
  sources: <number of documents with a reading>
  readings: <same number>
  conflict: <C-ids, or none yet>
  ingested: ["<slug>", ...]      # every document with a reading, date order
  gathered: "2026-09-25"
  ---
  ```
- Under the title, one bold sentence saying what the term is **according to the
  sources**, then the readings, then `## Open` with what no source settles.
- End the page with this line, verbatim:
  `Gathered 2026-09-25 from the ten-document scan (\`Plan/runs/haiku-scan-2026-09-25/\`) and the read documents; the scanned documents have no census and no reconciliation yet.`

## Before you finish

```bash
python3 scripts/quotes.py Wiki/candidates/<slug>.md   # must say 0 unresolved, 0 unchecked
python3 scripts/wiki_index.py --check
```

Write only your own new page files. Do not edit any existing file, do not run
`link.py --apply`, `wiki_index.py` without `--check`, or git. Reply with, per page:
the slug, the documents with a reading, the quotes.py line, and any conflict or
question the readings touch that the records do not hold yet.
