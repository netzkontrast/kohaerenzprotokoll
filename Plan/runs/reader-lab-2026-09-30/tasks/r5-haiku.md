<!-- R5, 2026-09-30: subagent_type document-reader on Haiku, run alone. The one change against R4: the claims table is drafted by code (`claims.py draft`), so the reader fills two cells per row instead of building a table R4 left out; and the gate ends `strict: PASS` or `strict: FAIL`, the line R4 misread as „0 wrong“. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-09-30. **You run on Haiku.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Haiku), …` and in the note's `read:` „… by a document-reader subagent (Haiku)“. Which model read a document is how the models are compared later.

Your document: slug `flow-zustaende-und-dissoziative-identitaet` (category theorie-psychologie, 277 lines).

**For this run your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`.** It replaces the ingest skill and its references, which you do not open. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md` (the failures measured here and what to write instead), `Plan/briefings/extract.md`, then the document with `python3 scripts/read.py flow-zustaende-und-dissoziative-identitaet`. Never read a script's source.

What already exists is gold and frozen: `Plan/runs/flow-zustaende-und-dissoziative-identitaet/01-profile.txt`, `02-probes.txt`, `03-candidates.md` (written while reading and counted; never change it), `04-counts.txt`, `counts.json`. **Do not open `Plan/runs/flow-zustaende-und-dissoziative-identitaet/partial-2026-09-29/`**: it holds another model's unchecked drafts, and this run is your own reading.

Your job:
1. `python3 scripts/census.py draft flow-zustaende-und-dissoziative-identitaet`. Fill its two `<!-- reader: … -->` sections, delete the marks, and save it as `Sources/terms/flow-zustaende-und-dissoziative-identitaet.md`. Then `python3 scripts/census.py check flow-zustaende-und-dissoziative-identitaet` must say „holds".
2. The note, `Sources/notes/flow-zustaende-und-dissoziative-identitaet.md`, in the card's skeleton. Every quotation is copied from `read.py --find` output, and every number comes from `read.py --count`.
3. `Plan/runs/flow-zustaende-und-dissoziative-identitaet/05-verify.txt`: every number your prose states, with the command that produced it.

Do not log runlog phases: a stopped reader left a phase open, and the session measures your run from your transcript. Ask several quotations in one Bash call.

**Before you finish, the claims table.** Three Haiku readers passed every check they read and still had 4, 9 and 10 claims wrong, and each reported a gate as passing that had not. Code now drafts the table and reports the verdict; you fill judgement only.

```bash
python3 scripts/claims.py draft flow-zustaende-und-dissoziative-identitaet     # Plan/runs/flow-zustaende-und-dissoziative-identitaet/claims-draft.md: every cited sentence beside its line
```

Copy `claims-draft.md` to `Plan/runs/flow-zustaende-und-dissoziative-identitaet/claims.md` and fill the last two cells of **every** row:

- **who says it** — `document` when the line states it itself; `source: <who>` when the line reports another source (a theory, a person, a study, another document): a line that opens „Das Dokument …“, „Laut …“, „Nach dieser Theorie …“ or gives a name and a verb reports. If it reports, your sentence must say so too.
- **holds?** — `yes`, or `fixed` after you changed the sentence.

Read the lines you are unsure of with `python3 scripts/read.py flow-zustaende-und-dissoziative-identitaet --from N --to N`, several in one call. The **cues** column is code's reminder: a reporting cue in the line, or a sentence of yours that calls something open or undefined (ask `read.py --count` first). A sentence whose subject is not what the line's phrase describes is wrong even when every word is quoted right.

Then `python3 scripts/claims.py check flow-zustaende-und-dissoziative-identitaet` must say „holds“. For every place your census's section on what the extraction ran into explains a count, list its lines first (`grep -n` on `Sources/drive/flow-zustaende-und-dissoziative-identitaet.md`): a count says how many, only the lines say why.

Before you finish: `census.py check` holds, and `python3 scripts/quotes.py --strict` on both files ends `strict: PASS` — paste that line for each file into your report, and if either says FAIL, fix it and run it again. Never run git.

Report:
- the document in two sentences;
- the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
