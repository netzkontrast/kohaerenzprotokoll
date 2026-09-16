---
description: >-
  Answer a question about the novel from the repository itself — Graph/, Wiki/,
  Canon/ and the manuscript — with every claim carrying the file and line it
  came from, and file the answer under Plan/queries/ when it is worth keeping.
argument-hint: "<question>"
---

# Ask — a cited answer, never a recollection

Answer from what the repository says, not from memory. Every claim carries its
source; anything the repository does not settle is named as an open question
rather than filled in.

## Where to look, in this order

```bash
python3 scripts/wiki_fts.py search "…"                    # the wiki, full text
grep -l "…" Graph/nodes/*.jsonl                           # codex, axioms, events, claims
grep -rn "…" Canon/                                       # normative canon prose
grep -rn "…" Manuscript/**/chapters/                      # what the prose actually says
```

`Graph/README.md` documents the record shapes. `tools/kpgraph` reads them in
Python when a question needs joins rather than greps:

```python
from tools import kpgraph
g = kpgraph.load()
[e for e in g.nodes("CodexEntry") if "Riss" in e.get("body", "")]
```

For outside research, `python3 scripts/research-tool.py search "…"` finds
open-access papers and files them under `Plan/research/`. Those are research,
never canon: they enter the repository through `/research-ingest`.

## Authority when sources disagree

1. For manuscript work, `Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md`
   is normative.
2. Inside the research-wiki loop, Canon is `unverified` until checked against
   the populated wiki, and a Canon/research conflict is an open question with
   no default winner (D-W12).
3. `Codex/**` is a generated view of `Graph/`; cite the graph record, not the
   view. To find the record, route through `Codex/GLOSSARY.md` to the partition
   index and open the one entry, rather than reading a whole category.

## Answer shape

- The answer, with `path:line` behind each claim.
- What the repository does not settle, as explicit questions for the author.
- Contradictions found along the way, quoted from both sides rather than
  resolved. Resolving one is `/kp-decide`, and it is the author's call.

Offer to file the answer as `Plan/queries/<slug>_<date>.md`. Ask before
writing it; do not file on your own.
