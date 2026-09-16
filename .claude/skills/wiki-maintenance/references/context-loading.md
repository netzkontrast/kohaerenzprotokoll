# Context-efficient manuscript loading

The goal is the smallest sufficient, spoiler-safe context packet for a
specific writing decision.

## Where the knowledge actually is right now

Read this before following the ladder, because it decides which rung you start
on. The wiki holds the *research understanding* and is currently empty of
promoted pages, so `Wiki/context-map.md` has no rows. The knowledge a chapter
needs — 602 codex entries, 111 world axioms, 56 story-time events — lives in
`Graph/` and renders into `Codex/`, and those carry no chapter window or
spoiler ceiling yet.

So today: **the wiki ladder is correct and will route nothing; the Codex is
where the answers are and has to be narrowed by hand.** The measurements and
the proposed fix are in
`Plan/wiki/codex-context-inventory_2026-09-16.md`; the migration is the open
task at the top of `todo.md` and is the author's to start.

Until then, narrow the Codex with the signal it already carries:

```bash
python3 scripts/wiki_fts.py search "…"        # wiki + Canon + Sources, heading-level
grep -o '"slug": "[^"]*"' Graph/nodes/codex_entry.jsonl | head
```

```python
# Which codex entries does this chapter actually put in play? Every entry
# carries `triggers`; scan the chapter text for them instead of loading the
# whole glossary. Roughly 40 entries fire per chapter, against 602 in total.
from tools import kpgraph
from pathlib import Path
g = kpgraph.load()
text = Path("Manuscript/.../chapters/03-….md").read_text(encoding="utf-8").lower()
for entry in g.nodes("CodexEntry"):
    triggers = [t.strip().lower() for t in entry.get("triggers", "").split(",") if len(t.strip()) >= 4]
    if any(t in text for t in triggers):
        print(entry["slug"], "—", entry["name"])
```

A trigger hit is spoiler-safe by construction: if the chapter is in an entry's
hit-set, the entry was already in play at or before that chapter. It does
**not** protect against a body that explains a later reveal, so an entry whose
body reaches forward still has to be read before it is used.

Always-on constraints do not appear as vocabulary and will never trigger:
the R-rules, the Sprach-DNA registers, voice and drafting guidance. Load those
from `Codex/GLOSSARY.md` by their `**Kategorie:**` (`rule`, `guidance`,
`voice`, `defect`, `theme`, `philosophy`), not by searching the chapter.

## Retrieval ladder

1. Establish task, target chapter, scene, and whether future spoilers are
   allowed. If the answer affects selection and is unknown, ask.
2. Read `Wiki/context-map.md`, not the entire Wiki. When it has no row for the
   target — which is the case for every chapter today — drop to the Codex
   narrowing above rather than loading `Codex/GLOSSARY.md` whole.
3. Filter by chapter window and require `spoiler_until <= target chapter` for
   spoiler-safe work.
4. Load `core` rows before `supporting`; load `evidence` only when the task
   needs substantiation.
5. Open the smallest matching page and only the relevant heading range.
6. Follow citations to exact source lines only when wording, evidence, or a
   conflict must be verified. Never load a complete raw source by default.
7. Stop when the writing decision is supported; more context is not
   automatically better context.

## Packet order

Build working context in this order:

1. task and chapter constraints;
2. the always-on writing constraints (R-rules, register, active world sensorik);
3. core synthesis/concept summaries;
4. open questions that materially affect the scene;
5. relevant detailed headings;
6. exact evidence excerpts.

Preserve source references in notes so claims can be rechecked without keeping
large source bodies in active context.

## Know what a packet costs

A packet nobody measured is a packet nobody trusts. The whole
`Codex/GLOSSARY.md` is ~71,700 tokens; a trigger-narrowed chapter packet plus
the rule cards and the axioms is ~23,600. Before reporting that a retrieval
path works, say what it loaded and roughly what it cost — a ladder that ends
in "and then read the glossary" has not done its job.

## Safety defaults

- Unknown spoiler ceiling means `40`, never "safe everywhere".
- Unknown chapter range means whole-novel scope until reviewed.
- A summary routes retrieval; it never substitutes for authority or evidence.
- Conflicting pages are loaded together and surfaced to the author; the
  maintenance workflow does not resolve the conflict.
