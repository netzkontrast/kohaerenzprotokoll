<!-- 2026-10-05 ingest, a document with no run yet: steps 1–4 on the R5 setup, on Sonnet, one reader at a time. -->
Work in /home/user/kohaerenzprotokoll. Today is 2026-10-05. **You run on Sonnet.** Name it wherever your definition asks for the model: `written_by: document-reader subagent (Sonnet), 2026-10-05, while reading, before any count` and in the note's `read:` „… by a document-reader subagent (Sonnet)“.

Your document: slug `charaktere` (category charaktere, 397 lines). Nobody has read it; there is no run folder yet.

**Your rulebook is `Plan/runs/reader-lab-2026-09-30/card.md`** plus steps 1–3 of `.agents/skills/ingest/SKILL.md` (sections *1 · Open the run* to *3 · Count, then write the census*) for the candidate list. Read, in this order: the card, `.agents/skills/reader-tools/references/failures.md`, the two ingest sections, `Plan/briefings/extract.md`; then open the run and read the document. Never read a script's source, `Wiki/`, `NOW.md`, or another document's files.

Your job:
1. `python3 scripts/capture.py charaktere` and read `Plan/runs/charaktere/01-profile.txt` before the document.
2. **No `--count` of any kind before the list exists** — not `capture.py --count`, not `read.py --count`; `--find` to check a spelling is fine. Read the whole document with `python3 scripts/read.py charaktere` (in ranges with `--from/--to` if it is long). **Write `Plan/runs/charaktere/03-candidates.md` while you read**, before any count: a `written_by:` line, then one `- term` per line, each written as the document writes it (ask `read.py --find` when unsure); observations as paragraphs, never as `- ` bullets. The rule for what is a candidate is the briefing's: what the document names in the novel's world, the words it uses as its own terms, the borrowed concepts it applies.
3. `python3 scripts/capture.py charaktere --count`.
4. `python3 scripts/census.py draft charaktere`. Fill its two `<!-- reader: … -->` sections, delete the marks, save it as `Sources/terms/charaktere.md`; `python3 scripts/census.py check charaktere` must say „holds".
5. The note, `Sources/notes/charaktere.md`, in the card's skeleton. Every quotation copied from `read.py --find` output, every number from `read.py --count`.
6. `Plan/runs/charaktere/05-verify.txt`: every number your prose states, with the command that produced it.
7. `python3 scripts/claims.py draft charaktere`; copy `claims-draft.md` to `claims.md` and fill the last two cells of every row — **who says it** (`document`, or `source: <who>` when the line reports another text, a narrative, a theory or a person; then your sentence must say so too) and **holds?** (`yes`, or `fixed` after you changed the sentence). `python3 scripts/claims.py check charaktere` must say „holds".

Do not log runlog phases. Ask several quotations in one Bash call. Never run git.

**Lessons from earlier documents in this run.** (1) When the document quotes another text, a name or phrase inside that quotation is that text's, not the document's own — say whose words they are. (2) Put the citation directly after the closing „“ mark; a count mark directly after its backticked term. (3) `quotes.py --unchecked <file>` names an uncited line exactly. (4) `--find` drops digits glued to words; quote around them.

Before you finish: `census.py check` holds, `claims.py check` holds, and `python3 scripts/quotes.py --strict` on both files ends `strict: PASS` — paste that line for each file into your report; if either says FAIL, fix it and run it again.

Report:
- the document in two sentences;
- how many candidates you listed, and the zeros and what each is;
- anything the card or the failures page did not tell you that you needed;
- any tool that behaved wrongly.
