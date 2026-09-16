# Learnings — extract terms (one source → its term census)

## Status

**One document done by hand, 2026-09-16** — `entropie-aegis`, 99 lines, 46
candidate terms. Census in `Sources/terms/entropie-aegis.md`.

**This step did not exist in the process until now.** It was created because
reading and gathering, the two steps either side of it, both silently drop
terms: a note records what a document *says*, so it keeps what is important
*there*, and a term page is only ever built from terms someone already thought
to look for.

## Why it exists — the failure it is meant to catch

A term that is obviously important in document 1 gets extracted. The same term,
mentioned once and in passing in document 2, gets missed — **and document 2 is
where it contradicts document 1.** The conflict is then invisible, and nothing
about the wiki reveals that anything was lost, because a missing term leaves no
hole.

The census is exhaustive on purpose. Judgement about whether a candidate really
is a term is **recorded per row rather than applied as a filter**, so that the
next document can be checked against what the last one found, including the rows
that looked like nothing.

## What the step is

Read one document line by line and list **every candidate term**, with its
occurrence count, its lines, whether the document defines it, and — the column
that carries the value — **why this row might be handled differently in the next
document.**

Then a carry-forward list: the rows to check explicitly against the next source.

## What the first document produced

46 candidates from 99 lines. Eight kinds of special case, each found rather than
predicted:

**1. A role name travels without its acronym.** `Entropic Gatekeeper` appears 7
times, four of them with no `AEGIS` beside it. Document 3 calls the same role
„Wächter der systemischen Stabilität" — **same role, different language, zero
shared characters.** No string match finds this, in either direction.

**2. Substrings are not terms.** `Guardians` (3×) and `Integrity Guardian` (1×)
are different things in one document. `Negentropie` contains `entropie` and
means its opposite. Three collisions in 99 lines.

**3. The root term is used as known and commissioned at the same time.**
`Entropie` occurs 53 times in the body and is never defined. Three *other* senses
are explicitly asked for — thermodynamic, information-theoretic, metaphorical —
while the project's own working sense runs through the document as if settled. A
page saying „this source defines entropy as X" would be wrong four ways.

**4. Quotation marks mark invention, not attribution.** „Daten-Verwitterung",
„Reinigungswellen", „Entropie-Signatur" are all coined by this document inside
quotes. **A citation checker reads quotation marks as a promise about a source.**
Here they promise the opposite. The two uses are indistinguishable by punctuation
and must be told apart by position: inside a proposal, or inside a claim.

**5. A term can survive in substance and vanish in surface.** `Quarantänezonen`
^[L59] reappears in document 3 as „Quarantäne instabiler Daten" ^[…:L49] —
the mechanism kept, the coined word dropped. Tracking the word loses it;
tracking the idea is not mechanical.

**6. Sixty percent of this document is questions.** `Alters`,
`Entropie-Signatur` and `Negentropie` appear **only inside questions**. An
extractor that treats every sentence alike records four terms the document asks
about as four terms it asserts. `status: asked` exists because of this.

**7. Four terms are named in one parenthesis and explained nowhere.**
Zero-Trust, Cognitive Firewall, Integrity Guardian, SIS ^[L65]. High confidence,
zero content. `SIS` is not even expanded — so if a later document expands it,
**the two will not match on string.**

**8. Names change independently, not as a set.** This document says Michael and
Julia. Document 3 says Kael and Julia. Canon says Kael and Juna. Already
recorded in `read-source.md`, and the census is where it becomes checkable.

## How this was actually done — the procedure, step by step

Recorded so the tool is derived from what the work *was*, not from a description
of it written afterwards. Each step notes whether a program could do it.

**1. Read the whole document with line numbers, in two passes of ~45 lines.**
```bash
cat -n Sources/drive/entropie-aegis.md | sed -n '1,45p'
cat -n Sources/drive/entropie-aegis.md | sed -n '45,100p'
```
*Mechanical.* The overlap at line 45 was accidental and turned out useful — the
section header at L45 was read in both passes and in both contexts.

**2. Write down every candidate while reading, before counting anything.**
*Judgement, and it must come first.* Counting first would have anchored the list
to whatever a regex found, and four of the eight special cases are things no
regex proposes.

**3. Count each candidate mechanically, with lines, and let the counts correct
the list.**
```bash
for t in "AEGIS" "Entropic Gatekeeper" …; do
  n=$(grep -o "$t" "$D" | wc -l)
  l=$(grep -n "$t" "$D" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//')
  printf "%-22s %3s   L%s\n" "$t" "$n" "$l"
done
```
*Mechanical, given the list.* This is where **`Guardian` came back as 4 and had
to be split into `Guardians` (3) and `Integrity Guardian` (1)** — the count
disagreed with the reading, and the count was right about the number while the
reading was right about the meaning.

**4. Probe the collisions the counts implied.**
```bash
grep -on "Integrity Guardian\|Guardians\|Guardian" "$D"
grep -o "[A-Za-zäöüÄÖÜ-]*[Ee]ntropie[a-zäöü-]*" "$D" | sort | uniq -c | sort -rn
```
*Mechanical.* The second one surfaced `entropie-aegis` — **the slug, from the
frontmatter** — which is how special case F1 was found. It was not looked for.

**5. Write the census, with a `risk` column filled in per row.**
*Judgement, entirely.* The risk column is the file's reason to exist and nothing
proposes its contents.

**6. Verify every number that went into prose.**
```bash
sed -n '1,9p' "$D" | grep -oin "entropie[a-zäöü-]*"   # frontmatter contribution
grep -o "Entropie" "$D" | wc -l                         # 54
sed -n '10,$p' "$D" | grep -o "Entropie" | wc -l        # 53
```
*Mechanical, and it caught a real error:* the census first said „44 times",
carried over from step 3's regex, which grouped compounds separately. The exact
string occurs **53 times in the body, 54 in the file**. Corrected before commit.

**The shape this implies.** Steps 1, 3, 4 and 6 are a program. Steps 2 and 5 are
a person, and step 2 must run *before* the program or the program decides what
gets seen. So the tool is not an extractor — it is:

> **a counter that takes a list of candidates and reports occurrences, lines,
> collisions and frontmatter contamination**, leaving both the proposing and the
> judging to whoever is reading.

That is a much smaller tool than „extract the terms", and it is the one the work
actually asked for.

## What the tool must handle

Each is decidable, and each was found by doing the work rather than by planning
it:

- **Skip the frontmatter, but not for citations.** Lines 1–9 carry `title` and
  `slug`, and the slug is a term by construction. Extraction counts from line
  10; citation counts from line 1. **Two line bases over one file, by design.**
- **Normalise the converter's escaping** before matching. `\"Julia\"` at L71 is
  a quoted name with backslashes. Every coinage in the census is quoted, so a
  matcher that does not normalise misses all of them.
- **Match on whole terms, never substrings.**
- **Distinguish a question from a claim**, at least well enough to set `asked`.
- **Carry the previous document's census in.** The carry-forward list is the
  whole mechanism: without it, the next extraction starts blind and repeats the
  failure this step exists to prevent.

## What stays judgement

- **Whether a descriptor is a term.** `Kontrollinstanz` appears 3 times and
  never without AEGIS beside it. Recorded as a descriptor. Nothing decides this
  but reading.
- **Whether an imported term has become a project term.** `Negentropie` is
  information theory here and a property of the Kael–Julia bond in document 3.
  Somewhere between those two it stopped being a citation and started being
  vocabulary.
- **Whether two surfaces are one term.** `Multiplizität` here,
  `funktionale Multiplizität` elsewhere in the corpus.
- **Whether a candidate is a term at all**, as against a word the author used
  twice.

## Open questions

- **Does the census belong in `Sources/` or in `Wiki/`?** It is derived from one
  source and describes only that source, which argues for `Sources/`. It is also
  the input to the wiki and not a fact about the document. Filed under
  `Sources/terms/` for now, alongside `Sources/notes/`, and the reasoning is
  here rather than in the filename.
- **One census per document, forever?** 409 documents is 409 files. Fine while
  written by hand; a question once a program writes them.
- **What is the census's relationship to the note?** Today: the census is
  exhaustive and mechanical-ish, the note is selective and interpretive. They
  were written in that order for document 1 only by accident — the note came
  first. **Predicted: census before note is the better order**, because the note
  can then say why it skipped what it skipped. Untested.

## What we will watch for

- How many candidates a typical document yields, and whether 46-in-99-lines
  holds or was an artifact of a dense brief.
- **Whether the carry-forward list actually catches anything.** This is the
  step's entire justification, and it is unproven until document 2.
- How much of the census is noise the author never wants to see.
- Whether the eight special cases above are the whole set or the first eight.
