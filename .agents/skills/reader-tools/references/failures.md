# Measured failures, and what to write instead

Every entry below happened in this repository, and its evidence is named. Where a
check catches the failure, the check is named: run it before you finish, and never
argue with it. Where no check can see it, only your reading prevents it. Read this
page before your first quotation.

## Quotations — `read.py --find`, `quotes.py`, `readings.py`

1. **Quotation marks changed.** Open every quotation with „. In markdown, close it
   with “ or a straight `"`: `quotes.py` accepts both, and the notes measured
   2026-09-30 close 1968 quotations with `"` and 345 with “. Never close with `”`,
   which `quotes.py` does not read as a closing mark. **In JSON, close with “ only**:
   a straight `"` ends the string. *2026-09-30:* HyperExtract on Haiku closed
   „getaktet“ with a straight quote in 3 of 5 calls, and each broke its reply.
   **Copy the words from what `read.py <slug> --find "<words>"` prints; never retype
   them.**
2. **The right line, the wrong words.** „das Management“ was written for „dem
   Management“, one case changed. It was the first defect `quotes.py` ever found.
   Retyping is how it happens. Copy, as in 1.
3. **A joined or shortened quotation.** `…`, `[…]` or two passages in one „…“ are
   refused. Quote one contiguous span of one line; two passages are two quotations.
4. **A quotation across a line wrap.** The export wraps sentences, and the line
   number is part of the claim, so a span over two lines cannot resolve. Quote the
   fragment that stands on one line. `--find` names both lines when your words span
   them.
5. **A quotation that begins with a one- or two-digit number.** „39 fragmented
   chapters“ is refused, because the footnote rule strips a number glued to a word.
   Begin with a word: „resolving 39 fragmented chapters“. *R1, 2026-09-30.*
6. **A name under four characters, asked alone.** `--find` drops fragments shorter
   than four characters, so „Lex“ alone cannot be found. Quote the longer phrase it
   stands in. *R1.*
7. **Export escapes and lost symbols.** The export writes `K\_1`, `\*`, `\~`. Quote and
   count them exactly as the line writes them, escapes included. `read.py --count` and
   the count-mark check count the words as written. *R1.* Where the export lost a
   symbol, the line has a gap, and the quotation keeps it: R3 wrote „Chaitins Ω ist“
   where the line reads „Chaitins  ist“. Quote the words after the gap, and say in
   prose what was lost.
8. **An uncited quotation.** Every „…“ of eight or more characters carries its
   citation, `^[Lnn]` in a census or note and `^[?]` in a reading file, and that
   includes headings and difference lines. *The pilot put 11 uncited quotations on
   7 pages.* `readings.py check` refuses them now, and `quotes.py --strict` fails a
   census or note that has one. *R2 and R3, on Haiku, left 24, and three were words
   the document never writes* — „Achse VIII“ for „Achse VII & VIII“, „wird
   verifiziert“, and the Ω above. No check could see them, because no citation
   named a line to check them against.
9. **Quotation marks used for anything else.** Use „…“ only for words the document
   writes, and put a name you merely mention in backticks: `` `Hard Canon` ``. A
   straight `"` between two quotations confuses which citation belongs to which.

## Names and counts — `census.py check`, `reading_extract.py stage`, `quotes.py`

10. **A surface normalised.** A name given in its base form where the line writes
    it inflected: `Primäre Beobachtungs-Einheit` where the line has „Primären
    Beobachtungs-Einheit“. *2026-09-30, HyperExtract on Haiku: 2 of 17 rows refused
    as "surface absent".* Write a surface exactly as it stands on its line. If
    `read.py --count "<surface>"` says 0, the form is not the document's.
11. **A count typed.** Ask `read.py <slug> --count "<words>"` and paste the mark it
    prints, `` `X` ^[<slug>.md:#N] ``. Never type N (P26). A zero is an inflection,
    export damage or a true absence; say which.
12. **A frozen list changed.** `03-candidates.md` is gold once counted (decision
    009). Never edit it, and never edit `counts.json` or `04-counts.txt`.

## Claims — no check can see these, only reading

13. **The prose says more than the line.** This was *7 of the 11 defects of the
    quality sample of 2026-09-29*:
    - a beat number wrong;
    - a plural read as a singular;
    - a self-description misread;
    - a gap credited that the line does not name;
    - a figure left out;
    - „Guardians“ written where the line says „Carrier“.

    *R2, Haiku, 2026-09-30, five of the note's claims:*
    - a phrase given to the wrong subject: the line calls the kernel „ein
      idealisiertes logisches System“, the note gave it to AEGIS;
    - another document's sentence given as the document's own: the line opens
      „Das Architekturdokument konstatiert explizit“;
    - „remains open“ for an index the document defines 114 lines later;
    - „cites two other documents“ where its reference list names twelve.

    *R3, Haiku, an audit of another document:* the note gave the audit's reports of
    the Protokoll — „Das Protokoll argumentiert“, „wird im Protokoll als … bezeichnet“
    — as the audit's own claims, five times, although its own claims pass had looked
    at those lines. The audit marks its verdicts „Das Audit bestätigt“.

    Before each claim, reread the cited line. State only what it states, and name
    the thing as the line names it. Ask who says it: a line that opens „Das
    Dokument …“, „Das Protokoll …“ or „Laut …“ reports another source.
14. **A gap credited that the document fills.** Before you write that something
    stays open, undefined or unnamed, ask `read.py <slug> --count "<its name>"` and
    read every line it names. *R2:* the CSI was called undefined at L34 and is
    defined at L148.
15. **A comparison with other documents.** „every later source“, „the only one“,
    „the oldest read source“: *2 defects and 13 minor findings of that sample.* Say
    nothing about another document unless you cite that document in the same
    paragraph. `lint_readings.py` flags the phrases it knows.
16. **A number in prose that no command produced.** „Four to three alters per
    world“ was written where the table gives two to three. *2 defects.* Every
    number your prose states is in `05-verify.txt` with the command that produced
    it. **Paste the command's output there; never retype it.** *R2:* the verify file
    listed eight counts, three of them attached to the wrong word, and the note's
    `stance_marker_count` said 31 where the eight summed to 21.
17. **A canon claim applied.** „ground truth“, „single source of truth“,
    „structurally verified“: record what the document says of its own standing, and
    never let it decide anything.

18. **A check result reported, not run.** R2 reported „0 unresolved, 0 unchecked“;
    `quotes.py` printed 2 unchecked in each file. R3 reported the same over 20. Run
    `quotes.py --strict`, whose exit status says it, and paste its last line into
    your report.

## Formats — `readings.py`, `census.py`

19. **A plural reading heading.** `## Readings —` is refused, because no
    frontmatter counts it. Write `## Reading — `<slug>`, <date>, <prose name> —
    <what it adds>`.
20. **A mechanical table edited.** `census.py check` compares every row, the
    frontmatter, the profile and the facts with what `census.py draft` writes. Fill
    only the two `<!-- reader: … -->` sections.

## Working economically — measured cost, not a check

21. **Reading script sources to learn a format.** *9 of 12 readers on 2026-09-29
    did.* Your definition, the card and this page say what each tool answers;
    `--help` is enough.
22. **Re-verifying what you were not asked to verify.** R1 re-ran 165 commands of a
    stopped reader's drafts, and was the costliest run (proxy 4.09 M). Start from
    the frozen list and the document. Another reader's partial draft is not input
    unless your task says so.
23. **One question per call.** Each call re-reads your whole context, so ask
    several quotations in one Bash call:
    `python3 scripts/read.py <slug> --find "…"; python3 scripts/read.py <slug> --find "…"`.
    Keep your reasoning between calls short.
