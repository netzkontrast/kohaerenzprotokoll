<!-- R3, 2026-09-30: subagent_type document-reader on Haiku, run alone. The author: „use Haiku agents to Read the missing ones (and make a Note that they where Read by Haiku - so we can later judge how good each different Model is)“. Changed against R2: one thing — a claims pass before finishing, because R2's mechanical checks held and four of sixteen claims did not; the failures page carries R2's four as items 13, 14, 16 and 18. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-09-30. **You run on Haiku.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Haiku), …` and in the note's `read:` „… by a document-reader subagent (Haiku)“. Which model read a document is how the models are compared later.

Your document: slug `kohaerenz-protokoll-audit-und-verifizierung` (category audit, 264 lines).

**For this run your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`.** It replaces the ingest skill and its references, which you do not open. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md` (the failures measured here and what to write instead), `Plan/briefings/extract.md`, then the document with `python3 scripts/read.py kohaerenz-protokoll-audit-und-verifizierung`. Never read a script's source.

What already exists is gold and frozen: `Plan/runs/kohaerenz-protokoll-audit-und-verifizierung/01-profile.txt`, `02-probes.txt`, `03-candidates.md` (written while reading and counted; never change it), `04-counts.txt`, `counts.json`. **Do not open `Plan/runs/kohaerenz-protokoll-audit-und-verifizierung/partial-2026-09-29/`**: it holds another model's unchecked drafts, and this run is your own reading.

Your job:
1. `python3 scripts/census.py draft kohaerenz-protokoll-audit-und-verifizierung`. Fill its two `<!-- reader: … -->` sections, delete the marks, and save it as `Sources/terms/kohaerenz-protokoll-audit-und-verifizierung.md`. Then `python3 scripts/census.py check kohaerenz-protokoll-audit-und-verifizierung` must say „holds".
2. The note, `Sources/notes/kohaerenz-protokoll-audit-und-verifizierung.md`, in the card's skeleton. Every quotation is copied from `read.py --find` output, and every number comes from `read.py --count`.
3. `Plan/runs/kohaerenz-protokoll-audit-und-verifizierung/05-verify.txt`: every number your prose states, with the command that produced it.

Do not log runlog phases: a stopped reader left a phase open, and the session measures your run from your transcript. Ask several quotations in one Bash call.

**Before you finish, a claims pass: R2, on Haiku, passed every check and still had four of sixteen claims wrong.** For every paragraph of your note, take its main claim and run `python3 scripts/read.py kohaerenz-protokoll-audit-und-verifizierung --from N --to N` on the line it cites (several lines in one call). For each, ask three questions and fix the claim if one fails: *Whose words are these* — the document's own, or another source it reports („Das Dokument …“, „Laut …“)? *About what* — is the subject of the phrase the thing your sentence names? *Is anything you call open, missing or undefined really so* — ask `read.py --count` for its name first. Write the paragraphs you checked, and what you changed, at the end of `05-verify.txt`.

Before you finish: `census.py check` holds, and `python3 scripts/quotes.py` on both files shows 0 unresolved and 0 unchecked — paste its last line for each file into your report. Never run git.

Report:
- the document in two sentences;
- the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
