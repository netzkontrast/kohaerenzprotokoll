# A deviation in order, reported by the reader — 2026-10-05

The reader reports that before writing `03-candidates.md` it ran about 90 `read.py --find` and 11 `read.py --count`
queries on phrases and terms it was considering. Nothing was written from them before the list, and the list was written
before `capture.py --count`, so `capture.py`'s refusal was never crossed; but eleven counts were seen before the list
existed, which is the anchoring the rule against counting first is about (`.agents/skills/ingest/SKILL.md`, step 2).

`scripts/gold.py` rules the list gold (59 terms, 100 % in the document) because it can only see the files. Its
`written_by:` line says „before any count"; with this note beside it, that line means „before `capture.py --count`".
Whether a list written after a handful of `read.py --count` queries stays gold is the kind of thing decision 009 decides,
not this session; the list is left as written, unchanged, and this file says what happened.

The task template for unread documents (`Plan/runs/ingest-2026-10-05/task-template-full.md`) now forbids any
`--count` before the list is written.
