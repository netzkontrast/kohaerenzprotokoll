<!-- 2026-10-05 ingest: the R5 setup (card, census and claims drafted by code, strict gate), on Sonnet, one reader at a time. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-10-05. **You run on Sonnet.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Sonnet), …` and in the note's `read:` „… by a document-reader subagent (Sonnet)“. Which model read a document is how the models are compared later.

Your document: slug `textanalyse-existenz-system-und-leid` (category theorie-philosophie, 352 lines).

**For this run your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`.** It replaces the ingest skill and its references, which you do not open. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md` (the failures measured here and what to write instead), `Plan/briefings/extract.md`, then the document with `python3 scripts/read.py textanalyse-existenz-system-und-leid`. Never read a script's source.

What already exists is gold and frozen: `Plan/runs/textanalyse-existenz-system-und-leid/01-profile.txt`, `02-probes.txt`, `03-candidates.md` (written while reading and counted; never change it), `04-counts.txt`, `counts.json`. **Do not open `Plan/runs/textanalyse-existenz-system-und-leid/partial-2026-09-29/`**: it holds another model's unchecked drafts, and this run is your own reading.

Your job:
1. `python3 scripts/census.py draft textanalyse-existenz-system-und-leid`. Fill its two `<!-- reader: … -->` sections, delete the marks, and save it as `Sources/terms/textanalyse-existenz-system-und-leid.md`. Then `python3 scripts/census.py check textanalyse-existenz-system-und-leid` must say „holds".
2. The note, `Sources/notes/textanalyse-existenz-system-und-leid.md`, in the card's skeleton. Every quotation is copied from `read.py --find` output, and every number comes from `read.py --count`.
3. `Plan/runs/textanalyse-existenz-system-und-leid/05-verify.txt`: every number your prose states, with the command that produced it.

Do not log runlog phases: a stopped reader left a phase open, and the session measures your run from your transcript. Ask several quotations in one Bash call.

**Before you finish, the claims table.** Earlier readers passed every check they read and still had 4, 9 and 10 claims wrong, and each reported a gate as passing that had not. Code now drafts the table and reports the verdict; you fill judgement only.

```bash
python3 scripts/claims.py draft textanalyse-existenz-system-und-leid     # Plan/runs/textanalyse-existenz-system-und-leid/claims-draft.md: every cited sentence beside its line
```

Copy `claims-draft.md` to `Plan/runs/textanalyse-existenz-system-und-leid/claims.md` and fill the last two cells of **every** row:

- **who says it** — `document` when the line states it itself; `source: <who>` when the line reports another source (a theory, a person, a study, another document): a line that opens „Das Dokument …“, „Laut …“, „Nach dieser Theorie …“ or gives a name and a verb reports. If it reports, your sentence must say so too.
- **holds?** — `yes`, or `fixed` after you changed the sentence.

Read the lines you are unsure of with `python3 scripts/read.py textanalyse-existenz-system-und-leid --from N --to N`, several in one call. The **cues** column is code's reminder: a reporting cue in the line, or a sentence of yours that calls something open or undefined (ask `read.py --count` first). A sentence whose subject is not what the line's phrase describes is wrong even when every word is quoted right.

Then `python3 scripts/claims.py check textanalyse-existenz-system-und-leid` must say „holds“. For every place your census's section on what the extraction ran into explains a count, list its lines first (`grep -n` on `Sources/drive/textanalyse-existenz-system-und-leid.md`): a count says how many, only the lines say why.

Before you finish: `census.py check` holds, and `python3 scripts/quotes.py --strict` on both files ends `strict: PASS` — paste that line for each file into your report, and if either says FAIL, fix it and run it again. Never run git.

Report:
- the document in two sentences;
- the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
