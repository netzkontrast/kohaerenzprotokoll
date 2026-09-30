<!-- R4, 2026-09-30: subagent_type document-reader on Haiku, run alone. The one change against R3: the claims pass is a table, not prose. R3's pass wrote „Verified“ under each claim and left nine wrong; a table that copies the line's opening words and names its speaker makes the voice visible. The gate is `quotes.py --strict`, which R3's two uncited-quotation reports led to. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-09-30. **You run on Haiku.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Haiku), …` and in the note's `read:` „… by a document-reader subagent (Haiku)“. Which model read a document is how the models are compared later.

Your document: slug `angst-bei-komplexen-traumafolgen` (category theorie-psychologie, 273 lines).

**For this run your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`.** It replaces the ingest skill and its references, which you do not open. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md` (the failures measured here and what to write instead), `Plan/briefings/extract.md`, then the document with `python3 scripts/read.py angst-bei-komplexen-traumafolgen`. Never read a script's source.

What already exists is gold and frozen: `Plan/runs/angst-bei-komplexen-traumafolgen/01-profile.txt`, `02-probes.txt`, `03-candidates.md` (written while reading and counted; never change it), `04-counts.txt`, `counts.json`. **Do not open `Plan/runs/angst-bei-komplexen-traumafolgen/partial-2026-09-29/`**: it holds another model's unchecked drafts, and this run is your own reading.

Your job:
1. `python3 scripts/census.py draft angst-bei-komplexen-traumafolgen`. Fill its two `<!-- reader: … -->` sections, delete the marks, and save it as `Sources/terms/angst-bei-komplexen-traumafolgen.md`. Then `python3 scripts/census.py check angst-bei-komplexen-traumafolgen` must say „holds".
2. The note, `Sources/notes/angst-bei-komplexen-traumafolgen.md`, in the card's skeleton. Every quotation is copied from `read.py --find` output, and every number comes from `read.py --count`.
3. `Plan/runs/angst-bei-komplexen-traumafolgen/05-verify.txt`: every number your prose states, with the command that produced it.

Do not log runlog phases: a stopped reader left a phase open, and the session measures your run from your transcript. Ask several quotations in one Bash call.

**Before you finish, a claims pass as a table.** Two Haiku readers passed every check and still had 4 and 9 claims wrong, and R3's prose pass wrote „Verified“ under claims it had wrong. Make the pass a table in `05-verify.txt`, one row per paragraph of your note **and per paragraph of the census's two sections you wrote**:

`| paragraph | line | the line's first six words, copied from read.py | who says it | your sentence's subject | holds? |`

- Read the lines with `python3 scripts/read.py angst-bei-komplexen-traumafolgen --from N --to N`, several in one call, and **copy** the six words; never type them from memory.
- *Who says it* is the document itself, or another source it reports: a line that opens „Das Dokument …“, „Laut …“ or names a person or a framework as the speaker reports it. If the line reports a source, your sentence must say so.
- *Your sentence's subject* must be the thing the line's phrase describes. A phrase about a kernel is not about the AI system that is assigned to it.
- For every place your prose says something is open, undefined, missing or unnamed, ask `read.py --count "<its name>"` first and read every line it names.
- If a row does not hold, fix the note or census and write what you changed under the table.

Before you finish: `census.py check` holds, and `python3 scripts/quotes.py --strict` on both files exits 0 — paste its last line for each file into your report. Never run git.

Report:
- the document in two sentences;
- the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
