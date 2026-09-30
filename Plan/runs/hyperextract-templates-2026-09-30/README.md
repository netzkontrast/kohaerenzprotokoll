# HyperExtract template revisions, 2026-09-30

Each revision is measured against the active template on the same document before it
could be promoted (`.agents/skills/hyperextract-learning/SKILL.md`). The model is Haiku
through `claude -p` (`scripts/he_claude.py`). The document is
`kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` (58 lines), whose note, by a
Sonnet reader, cites 25 lines.

## TermReadings r1 — not promoted

Parent `80f445fb2e07cf45`. r1 names the two failures of the first live pass in the
guidelines:
- a term exactly as its line writes it, inflection included;
- German „…“ copied as they stand.

| run | rows | candidates | refused | lines placed | of the note's 25 | lines the note lacks | calls (failed) | cost |
|---|---|---|---|---|---|---|---|---|
| active, b | 17 | 15 | 2 (surface absent) | 12 | 12 (48 %) | 0 | 3 (0) | $0.035 |
| active, c | 19 | 17 | 2 (surface absent) | 13 | 13 (52 %) | 0 | 3 (0) | $0.036 |
| r1, a | 14 | 14 | 0 | 10 | 10 (40 %) | 0 | 4 (1) | $0.035 |
| r1, b | 15 | 14 | 1 (quote not placed) | 11 | 11 (44 %) | 0 | 3 (0) | $0.035 |

**r1 removes the inflection refusals and covers fewer of the note's lines, so it is kept
here and not promoted.** The active template's two refusals are correct: the stage
refuses a surface the document does not write, and the passage stays for a reader to
see. Two runs a side measure little (P18).

**What HyperExtract adds on this document: nothing the note lacks.** Every line it
placed, in all four runs, is a line the note already cites, and it covered about half of
them. This is the first datapoint of the model comparison the author asked for on
2026-09-30. A second reader on Haiku through a template finds a subset of what a Sonnet
reader found; on longer documents that may differ.

The runs are in `Plan/runs/kohaerenz-protokoll-meta-foreshadowing-beobachter-logik/hyperextract/`.
The failures behind r1 are also on `.agents/skills/reader-tools/references/failures.md`,
for every reader.
