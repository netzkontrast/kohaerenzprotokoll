<!-- R2, 2026-09-30: subagent_type document-reader on Haiku, run alone. The author: „use Haiku agents to Read the missing ones (and make a Note that they where Read by Haiku - so we can later judge how good each different Model is)". Changed against R1: the model (Haiku); the card and the failures page replace the ingest skill and its references; the census from census.py draft; a clean start, without the Sonnet reader's partial drafts. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-09-30. **You run on Haiku.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Haiku), …` and in the note's `read:` „… by a document-reader subagent (Haiku)“. Which model read a document is how the models are compared later.

Your document: slug `ki-narrative-kollaps-kohaerenz-paradoxie` (category theorie-logik, 191 lines).

**For this run your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`.** It replaces the ingest skill and its references, which you do not open. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md` (the failures measured here and what to write instead), `Plan/briefings/extract.md`, then the document with `python3 scripts/read.py ki-narrative-kollaps-kohaerenz-paradoxie`. Never read a script's source.

What already exists is gold and frozen: `Plan/runs/ki-narrative-kollaps-kohaerenz-paradoxie/01-profile.txt`, `02-probes.txt`, `03-candidates.md` (written while reading and counted; never change it), `04-counts.txt`, `counts.json`. **Do not open `Plan/runs/ki-narrative-kollaps-kohaerenz-paradoxie/partial-2026-09-29/`**: it holds another model's unchecked drafts, and this run is your own reading.

Your job:
1. `python3 scripts/census.py draft ki-narrative-kollaps-kohaerenz-paradoxie`. Fill its two `<!-- reader: … -->` sections, delete the marks, and save it as `Sources/terms/ki-narrative-kollaps-kohaerenz-paradoxie.md`. Then `python3 scripts/census.py check ki-narrative-kollaps-kohaerenz-paradoxie` must say „holds".
2. The note, `Sources/notes/ki-narrative-kollaps-kohaerenz-paradoxie.md`, in the card's skeleton. Every quotation is copied from `read.py --find` output, and every number comes from `read.py --count`.
3. `Plan/runs/ki-narrative-kollaps-kohaerenz-paradoxie/05-verify.txt`: every number your prose states, with the command that produced it.

Do not log runlog phases: a stopped reader left a phase open, and the session measures your run from your transcript. Ask several quotations in one Bash call.

Before you finish: `census.py check` holds, and `python3 scripts/quotes.py` on both files shows 0 unresolved and 0 unchecked. Never run git.

Report:
- the document in two sentences;
- the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
