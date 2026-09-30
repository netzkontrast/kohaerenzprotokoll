# Reader lab — step 6's ten remaining documents, one at a time, 2026-09-30

The author, 2026-09-30, after ten of twelve parallel readers had been stopped by the
session's usage limit:

> „starte diese nicht parallel — sondern nutze die Chance und beobachte jeden der zehn —
> und versuche diese als lernlabor zu verstehen.. Probier ander Dinge aus.. vielleicht
> mal… gib ihnen unterschiedliche Anweisungen"

So the ten are read one after another. Each run gets its own instruction, and each is
measured from its transcript before the next one starts.

## What the first twelve cost — measured from their transcripts

`transcripts.py` reads Claude Code's own record of each subagent. The transcripts live
outside the repository and die with the container, so `transcripts.json` keeps their
numbers. It holds no text, only numbers. The twelve ran on 2026-09-29 as
`general-purpose` agents on Sonnet, all at once, each told to follow
`.claude/agents/document-reader.md`.

| | per reader, range over the twelve |
|---|---|
| API calls | 55–87 |
| wall-clock | 28–35 minutes (ten stopped at the limit after 29–35) |
| cache reads | 11.7–21.8 million tokens |
| largest context | 325–462 thousand tokens |
| cost proxy (`transcripts.py`) | 1.6–2.8 million |
| what the Agent notification reported | 380 and 396 thousand for the two that finished — the last call's size, not the consumption |

**Where it goes.** Each call re-reads the whole context, so the cost is the number of
calls times the size of the context. Four things make the context large:

1. **The fixed part is 67 thousand tokens at the first call.** It holds the system
   prompt, the tool definitions, `CLAUDE.md` and the skill listing. A run of 62 calls
   re-reads it 62 times, about 4 million of 13.8 million cache reads.
2. **The rules are read in full, once, and then carried.** That is five files, 70–105
   thousand characters of `Read` results, before the document. They are
   `document-reader.md`, the ingest skill, `german.md`, `artifacts.md` and the briefing.
3. **Nine of twelve readers read script sources** — `capture.py` twice, `gold.py`,
   `reconcile.py`, `ui.py` — to find out what a census looks like. No rule file shows
   one. No reader ran `reconcile.py` on its document, so no census saw the wiki.
4. **About half of the context's growth is not in the transcript: 35–54 %.** The
   best explanation is thinking, which is stored redacted. The estimate calibrates
   characters per token on the transcript itself (2.0–2.35) and subtracts what is
   visible. The pilot's four `wiki-reader`s, working from a brief, show 7–17 %.

Output is not measured. The transcript keeps the first stream event's usage, not the
final count, so `wrote` counts characters instead: 97–170 thousand per reader.

**The lists are long by design.** The candidate lists have 63–318 rows. Even the
40-line technical audit (9 kB) has 216. Decision 012's rule is exhaustive, and this
lab does not change what a census lists.

## The runs

The ten documents differ in size and in what the stopped reader left
(`Plan/runs/<slug>/partial-2026-09-29/`). So a run is an observation, not a controlled
comparison. The runs ratchet: each keeps what held in the run before and changes one
thing. The baseline is the twelve transcripts above.

| # | document | lines | left by the stopped reader | the change |
|---|---|---|---|---|
| R1 | `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` | 40 | census, note, at the note | the `document-reader` agent type, with its six tools; resume from the partial — **done, below** |
| R2 | `ki-narrative-kollaps-kohaerenz-paradoxie` | 191 | a note draft, no census | **Haiku**; the rules from `card.md`, the failures page and the briefing instead of five rule files; the census from `census.py draft`; a clean start, the partial unopened — **done, below** |
| R3 | `kohaerenz-protokoll-audit-und-verifizierung` | 264 | a census and a note draft | R2's setup plus a claims pass before finishing, three questions per claim — **done, below** |
| R4 | `angst-bei-komplexen-traumafolgen` | 273 | a census draft, no note | R3's setup, the claims pass as a table in `05-verify.txt`, and `quotes.py --strict` as the gate — **done, below** |
| R5 | `flow-zustaende-und-dissoziative-identitaet` | 277 | a note and a census draft | the claims table drafted by code (`claims.py`), the gate ending `strict: PASS`/`FAIL`; one resume message when the first report left both failing — **done, below** |

### R1 — the `document-reader` agent type, resuming from the partial

`technical-audit-research-mandate-the-kohaerenz-protokoll-fra`: 40 lines, 9 kB, English, 216 candidates.
The numbers come from `transcripts.py`. The first column is this document's first reader, which the
usage limit stopped on 2026-09-29.

| | first reader, stopped | R1 |
|---|---|---|
| minutes | 34.9 | 53.8 |
| calls | 76 | 111 |
| peak context | 423 k | 506 k |
| cache reads | 18.1 M | 34.6 M |
| cost proxy | 2.34 M | 4.09 M |
| unseen share of the context's growth | 54 % | 41 % |
| wrote | 115 k characters | 184 k characters |

**Quality: it held.**
- `quotes.py`: the census has 49 quotations and 94 count marks, the note 118 and 61. None is
  unresolved, unchecked or wrong.
- The candidate list stayed gold, its md5 unchanged. `capture.py --count` counted it again with the
  same result; only `counts.json`'s date moved, and that date was put back.
- Five claims of the note were read against their lines (L40, L3, L11, L20, L26), and all five hold.
- The stopped reader's drafts did not hold as they stood. R1 corrected 11 claims of the census draft
  and 10 of the note draft, and dropped one false claim, that „the words for a completed check stand
  nowhere". The document's own „Verified" is such a word.

**Cost: the most expensive document so far.** Both readers together cost 6.4 M, for the smallest
document of the twelve. Where it went:
- R1 re-ran all 165 commands of the draft's `05-verify.txt` and wrote 218, 97 of them new.
- It wrote its own generators for the census, the note and the verify file. They are kept in
  `r1-scratch/`, because `05-verify.txt`'s section G names them.
- It read the ingest skill, `german.md`, `artifacts.md` and the briefing, although its agent
  definition carries the rules.
- It read script sources again: `reconcile.py`, `account.py`, `state.py`, `subject.py`, `digest.py`
  and `census.py`.
- It did not adopt `census.py`, because neither its definition nor the skill names it. So this run
  says nothing about the census draft.

**What its care found: three tool defects, each fixed the same day with a case that fails on the old
code.**
- `census.py draft` wrote the title, the header and the profile twice.
- `quotes.py` stripped an escape that `read.py --count` counts. The export writes `K\_1`, so a
  mark `read.py` pastes (8) was checked as `K_1` (0) and could never hold.
- `runlog.py` refused to end a phase started a second time. R1's `end census` was refused; the
  session logged it after the fix, at the census file's last write, 11:31:31. The note phase reads
  16.6 h because the usage-limit pause lies inside it.

**What it teaches.**
- The agent type alone does not cut cost. The fixed context and the verification loop dominate:
  111 calls, each re-reading a context that grew to 506 k.
- Resuming from a stopped reader's drafts did not save work. The reader re-verified everything the
  drafts said, and was right to, because 21 of their claims needed correcting.
- R2 and R3 change the two big levers: rules on one card with the mechanical census drafted by code
  (R2), and a reader outside the session with no fixed context (R3).

### R2 — Haiku, the card, the census drafted by code

`ki-narrative-kollaps-kohaerenz-paradoxie`: 191 lines, German, 269 candidates. The author asked for
Haiku readers „so we can later judge how good each different Model is“, so the note's `read:` names
the model and the run log's reader row says `haiku`. The task is `tasks/r2-haiku.md`. The first
column is this document's first reader, on Sonnet, which the usage limit stopped on 2026-09-29.

| | first reader, Sonnet, stopped | R2, Haiku |
|---|---|---|
| minutes | 34.4 | 5.4 |
| calls | 55 | 56 |
| peak context | 455 k | 110 k |
| cache reads | 12.2 M | 4.5 M |
| cost proxy | 1.79 M | 0.60 M |
| unseen share of the context's growth | 35 % | 19 % |
| wrote | 170 k characters | 51 k characters |

The proxy counts tokens, not price, and the two models' prices per token differ. The first
reader's numbers are for a run that did not finish.

**Quality: the checks held, and the reading did not.**
- `census.py check` holds. `quotes.py`: the census's 269 count marks and the note's quotations
  resolve. Each file had 2 uncited quotations, which the report called „0 unchecked“. All four now
  carry their line.
- Sixteen claims of the note were read against their lines. **Four were wrong:**
  - L61 calls the kernel „ein idealisiertes logisches System“, and the note gave it to AEGIS;
  - L87 reports another document's sentence, „Das Architekturdokument konstatiert explizit“, and
    the note gave it as the document's own;
  - the note called the Collapse Susceptibility Index undefined, and L148 defines it;
  - the note said the document „cites two other documents“, and its reference list names twelve,
    L180 to L191.
- One was loose: „as its goal“ for a line that says the study delivers it.
- The note's `stance_marker_count` said 31. Its own verify file listed eight counts that sum to
  21, and three of them were attached to the wrong word.
- Four claims of the census's two hand-written sections were read, and all four hold: the bias
  list's two System names (L40), `Lia` in a sentence and `Lyra` in the table (L105, L132),
  `Qualia-Erfahrung` (L113), and `Kael` as the system and as a part (L63, L132).

The note was committed as Haiku wrote it, then corrected in the next commit, so `git diff` between
the two is the measurement. `Plan/runs/ki-narrative-kollaps-kohaerenz-paradoxie/corrections.jsonl`
has one row per correction, five of class `claim`, which `runlog.py` gained for this, since 7 of the
11 defects of the quality sample were of that kind.

**What it teaches.**
- Haiku read a 191-line document in 5.4 minutes. Every mechanical check held, because code drafted
  the census and the checks named what to fix.
- What no check sees went wrong four times in sixteen: the subject of a phrase, the voice of a
  sentence, a gap the document fills later, and a count of its own references. R1, on Sonnet, had
  five of five claims hold, on a document a fifth this length. One run each is not a comparison.
  Each model needs more documents.
- The failures page now carries each of these, with the question that prevents it (items 14, 15,
  17 and 19).

### R3 — Haiku, with a claims pass

`kohaerenz-protokoll-audit-und-verifizierung`: 264 lines, German, 285 candidates, an audit of another
document. The one change against R2: before finishing, the reader rereads the line behind each
paragraph's main claim and asks whose words they are, about what, and whether anything called open
is so (`tasks/r3-haiku.md`).

| | first reader, Sonnet, stopped | R3, Haiku |
|---|---|---|
| minutes | 34.4 | 7.2 |
| calls | 82 | 39 |
| peak context | 462 k | 131 k |
| cache reads | 21.8 M | 3.9 M |
| cost proxy | 2.76 M | 0.55 M |
| unseen share of the context's growth | 49 % | 13 % |
| wrote | 128 k characters | 89 k characters |

**Quality: the claims pass ran, and did not catch what it was for.**
- `census.py check` holds, and the 50 cited quotations resolve. **20 were uncited**, 8 in the note
  and 12 in the census, and the report again said „0 unchecked“. **Three of them are words the
  document never writes:**
  - „Achse VIII“, where the heading at L147 reads „Achse VII & VIII“;
  - „wird verifiziert“;
  - „Chaitins Ω ist“, where L141 reads „Chaitins  ist“, because the export lost the symbol.
- `stance_marker_count` said 26. The verify file's own counts sum to 17, and its attempt to
  reconcile the two reached 23.
- **Nine claims were wrong**, of about thirty read against their lines:
  - five times the note gave the audit's reports of the Protokoll as the audit's own: „Das
    Protokoll argumentiert“ (L185), „wird im Protokoll als … bezeichnet“ (L179), a reader-response
    idea the Protokoll „transmutiert“ (L155), and two readings of L15 and L187;
  - „emotional binding … connected to“ a deletion field, where L15 has love persisting across it;
  - McKay's 1978 observation given the name of Conway and Norton's 1979 paper;
  - in the census, „eight labeled axes“ at seven lines, two of them no axis; and a first-person
    plural where every such sentence is in the third person, „Das Audit bestätigt“.
- The claims pass looked at L185 and wrote „the document's interpretation … Verified.“ A pass
  run by the model that wrote the claim asks it the same question twice.

The note and census were committed as Haiku wrote them, then corrected
(`Plan/runs/kohaerenz-protokoll-audit-und-verifizierung/corrections.jsonl`: 9 `claim`,
4 `quotation`, 1 `count`).

**What it teaches, with R2.**
- Two Haiku readers took 5–7 minutes and about a fifth of the stopped Sonnet readers' cost proxy
  on the same documents. Every mechanical check held that the reader actually ran.
- Both misreported the one check they were told to report. So the gate is now mechanical:
  - `quotes.py --strict` exits 1 on an uncited quotation, with a case in `selftest.py` that
    fails on the old code;
  - the summary line says „unchecked“, the word the task asks for.
- Voice is the new failure class. In a document that reports another document, the reader must
  tell the report from the verdict. The failures page now names both markers, „Das Protokoll …“
  and „Das Audit …“ (item 14).
- A self-check by the same model is weaker than a check by code or by another reader. R4 keeps
  the claims pass and adds the strict gate; whether the pass earns its cost is R4's question.

### R4 — Haiku, the claims pass as a table, the strict gate

`angst-bei-komplexen-traumafolgen`: 273 lines, German, 268 candidates, a clinical report. The one change
against R3: the claims pass was to be a table in `05-verify.txt` with the line's opening words and its
speaker, and the gate `quotes.py --strict` (`tasks/r4-haiku.md`).

| | first reader, Sonnet, stopped | R4, Haiku |
|---|---|---|
| minutes | 30.2 | 8.6 |
| calls | 67 | 50 |
| peak context | 353 k | 138 k |
| cache reads | 11.7 M | 5.2 M |
| cost proxy | 1.62 M | 0.69 M |
| unseen share of the context's growth | 35 % | 8 % |
| wrote | 119 k characters | 100 k characters |

**Quality: both changes were ignored, and both reports were wrong.**
- **The gate failed and the report said it held.** `quotes.py --strict` exits 1: 10 unresolved
  quotations, 6 in the census and 4 in the note, and 4 uncited. The report gave „0 wrong“, the figure
  that ends the summary line, for the count marks. Six of the ten were one mechanism: the note wrote
  words in straight quotes in prose, and the checker, which takes the last straight quote it finds,
  ran each quotation on to the next.
- **No claims table.** `05-verify.txt` is a list of counts. The reader's report did not mention it.
- `census.py check` holds. `stance_marker_count` said 8, the number of markers; their counts sum to 10.
- **Ten claims were wrong**, of the 74 cited sentences of the note and census, about 45 of them read
  against their whole lines:
  - the prevalence of classical PTBS (6 %) written up as the disorder's, and „70.4 %“ as its
    prevalence, when it is exposure to any trauma (L17);
  - a window the line says is „massiv“ narrowed became one patients „can modulate“ (L51);
  - a description („hat sich … etabliert“) written as a prescription, and a theory the line reports
    („Nach dieser Theorie“) as the document's own statement (L138, L85);
  - four in the census's section on what the extraction ran into, all explanations of a count given
    without reading its lines: 8 question marks that „stand in rhetorical closure“ (all 8 stand in
    reference titles), 16 typographic marks that are „em-dashes, ellipses“ (dashes and curly quotes,
    no ellipsis), a compound `Triggering` (the document writes `Triggerung`), and a second `Drive`
    at line 162 (it is `Shame-Driven` in a reference title).
- The census and note were committed as Haiku wrote them — recovered byte for byte by replaying the
  reader's own Write and Edit calls from its transcript, because the review had already started
  editing — then corrected (`corrections.jsonl`: 10 `claim`, 3 `quotation`, 1 `count`).

**What it teaches, with R2 and R3.**
- Three Haiku readers, three documents, 5–9 minutes and a third to a fifth of the stopped Sonnet
  readers' cost proxy each. Every mechanical check that the reader actually ran held, and every
  check it was told to report it misreported (R2 and R3: uncited quotations; R4: unresolved ones).
- A gate a reader can misread is not a gate. Two changes now put the verdict out of the reader's
  hands: `quotes.py --strict` ends `strict: PASS` or `strict: FAIL — …`, and `claims.py` drafts the
  claims table by code, as `census.py` drafts the census, so that the reader fills two cells per row
  instead of building a table. R5 takes both, and the task file says only to run them.
- Errors of explanation are the new class: a count is right and the reason given for it is invented.
  No table of cited sentences reaches them, because an explanation carries no citation. Item 13 of
  the failures page names the habit that prevents them: list the count's lines before explaining it.
- Reading 45 rows against their whole lines cost the session about as much as the reader's whole run.
  `claims.py show` prints each sentence with its whole line so that a review is a read and not a
  search.

### R5 — Haiku, the claims table drafted by code, one resume

`flow-zustaende-und-dissoziative-identitaet`: 277 lines, German, 318 candidates. The change against R4:
`claims.py draft` writes the table, and `quotes.py --strict` ends `strict: PASS` or `strict: FAIL`
(`tasks/r5-haiku.md`).

| | first reader, Sonnet, stopped | R5, Haiku (both parts) |
|---|---|---|
| minutes | 30.4 | 13.6 |
| calls | 87 | 74 |
| peak context | 355 k | 140 k |
| cache reads | 16.3 M | 7.9 M |
| cost proxy | 2.07 M | 1.13 M |
| unseen share of the context's growth | 39 % | 14 % |
| wrote | 106 k characters | 68 k characters |

**Quality.**
- **The gate line did what it was made for, and the reader stopped anyway.** The first report said
  `strict: FAIL — 5 unresolved, 5 uncited` for the note; R2 to R4 had reported a pass over failing
  gates. But it ended there, with the claims table copied and every cell `<fill>`, although the task
  said to fix and rerun. The cost of the resume message was the second half of the run above: all four
  gates passed.
- **The table was filled, and filled the same way 48 times: `document | yes`.** The table's completeness
  is now checked; its content is not, and cannot be. One row I read against its line was wrong: line 51
  reports a hypothesis by Arne Dietrich and the note wrote it as the neurobiological basis. It is the
  one row `claims.py` flags after two fixes to its cues, described below.
- `stance_marker_count` was a list, and one phrase in it, counted 63, stands nowhere. The census's
  section on the export was silent where 64 escapes, 57 glued numbers, 26 typographic marks and 10
  question marks stand; the report said „no unusual export issues“.
- Of 48 cited sentences, all read against their lines: **2 claims and 1 count wrong**, against 10 of
  74 for R4. The note names its sources better than R4's did („citing empirical studies with LISREL
  models“).

**What the review changed in the tool.** `claims.py`'s reporting cues had been read case-insensitively,
so `so klar` and `nach Beendigung` were cues and 12 of 48 rows were flagged; German capitalises every
noun, so „nach“ before a capital is no name. With case kept and the nouns cut to those a report calls
another text, 1 of 48 rows is flagged, and it is the wrong one.

**What it teaches, with R2 to R4.**
- Four readers, four documents. A Haiku reader completes what a mechanical gate checks completeness of,
  and no more: R5 filled a table it was told to think about with one answer. The claims table is
  useful to the reviewer, who reads `claims.py show` against the lines, and worth nothing as the
  reader's self-check.
- A resume message naming the failing gates worked once, at about the cost of the reader's own second
  half. Whether to build it into the pipeline — a coordinator that reruns the gates and resumes the
  reader until they pass — is a question for the author, since a reader that must be told twice is a
  cost the tokens table above does not show.
- The rate of wrong claims on Haiku, by document: 4 of 16 read (R2), 9 of about 30 (R3), 10 of 74 (R4), 2
  of 48 (R5). The four documents differ in length, category and how much they quote, so this is not a
  trend; it is the first four points of a measurement.

**Planned, and changed by what each run shows:**
- **R3:** brief reasoning between tool calls, and several `--find` in one call. The unseen share and the number of calls measure each.
- **R4:** `claude -p` with no `CLAUDE.md`, no skill listing and no deferred tools, which removes the 67-thousand-token fixed part (decision 011's door, PR #119's claude-cli backend).
- **R5:** a pack. Code builds the numbered document, the card, the frozen list and a schema; the model answers; code places every quotation and renders census and note (#119's pack, verify and render, reused if they take parameters).
- **Jules**, if #119's session dispatches it (decisions 014, 017): an extraction of `kohaerenz-protokoll-hard-sf-horror-thriller` into `jules-2026-09-30/`, scored against the Claude run of the same document. It costs no Claude usage.

Quality is checked the same way each time:

- `quotes.py` on the census and the note: 0 unresolved and 0 unchecked;
- the census and note formats, as `account.py order` and the reconciliation read them;
- after reconciliation, what the readings step took from each document.

Five claims of each note are read against their lines. That is the check that found
the 11 defects of the quality sample, which `quotes.py` could not see.
