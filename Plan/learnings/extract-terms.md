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
is a term is **recorded per row rather than applied as a filter**.

> **Rule, added after document 2 and applied retroactively to document 1: a
> census describes one document and nothing else.** No count, comparison or
> expectation from another source appears in it. The first version of document
> 1's census broke this — it carried forward-looking notes about later documents
> and a checklist to apply to the next one — and that is precisely the
> contamination that makes a term look unimportant in the document where it
> conflicts. Comparison is a separate step, in `Wiki/compare/`, and only by
> keeping the two apart is what the comparison finds a result rather than an
> assumption carried in.
>
> `scripts/profile.py` exists so that *identical treatment* is mechanical rather
> than a promise: every census opens with the same probes in the same order.

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

## What document 2 added, extracted independently

94 candidates from 311 lines, with no reference to document 1 while reading.
Six special cases document 1 could not have shown:

**9. One hundred zero-width spaces sit inside the formulas.** `A₀` is stored as
`A0` + `U+200B`; the export flattened every subscript that way. A formal term
cannot be matched, quoted or cited reliably without normalising it — and a quote
typed by hand will never equal the same quote read from the file. **This is a
different failure from the typographic-quote one, and it defeats the same check.**

**10. 116 reference numbers are glued to the words they annotate.**
„Fixpunkttheoremen 6", „Autopoiesis 43". Superscript formatting was dropped, so a
bare integer follows the term. A quoted fragment either includes the number and
does not read as the term, or excludes it and does not match the file.

**11. Formal symbols are terms, and a word-based census finds none of them.**
`⊕` is the term the entire RSA critique turns on — „bleibt undefiniert" — and it
is one character. So are `θ`, `α`, `Σ`, `Δ`, `Π`.

**12. One symbol can carry three meanings in one document.** `E` is the coherence
function ^[L58], the edge set of the agent graph ^[L92] and entropy ^[L126].
Nothing marks the switch.

**13. A document's own summary table renames its own terms.** Five of eight
protocols are abbreviated differently in Table 1 than in the body —
„Rekursive semantische Autogenese" against „Rekursive Sem. Autogenese". One
document, two surfaces per term.

**14. Quotation marks mark citation here and invention in document 1.** Same
punctuation, inverted meaning, nothing marking which convention is in force. The
full consequence is in `Wiki/compare/001`.

## What the first comparison measured

**Of 27 terms document 1 carries, 21 do not occur in document 2 at all.** Of 25
terms document 2 carries, 24 do not occur in document 1. The overlap is six
strings.

**This inverts the premise this step was built on.** Nothing was overlooked in
document 2 — the terms are simply absent, and document 2 never mentions the novel
at all. Meanwhile every real conflict sits on a string the two documents *share*.

**String identity is anti-correlated with semantic identity in this pair.** Where
the words differ, the documents are about different things; where they match,
they mean incompatible things. A conflict detector built on shared strings finds
three candidates here and is wrong about one — `Zero-Trust`, which is an AEGIS
sub-function in one document and the external ZTA architecture in the other, and
not a disagreement at all.

That is the first support `gather-term.md` prediction 2 has ever had.

## Format is measured, stance is read, and the probe only catches one convention

Decision 004 removed the document-kind enum. What replaced it changed this step:

- **Format** is `scripts/profile.py` — the same probes, every document, in the
  same order.
- **Stance** is read per passage. *Whether* a document labels its own passages is
  format and is now counted; what those labels mean is not.

The `repeated labels` probe finds document 2's convention exactly — six labels,
38 occurrences, `Beschreibung x8` through `Probleme x4`.

**And it reports `none` for document 3, which marks 26 passages.** Document 3's
markers are `\[User Query\]` inline in running prose, not bold headings, so a
probe built on one document's convention is blind to the other's.

That is the honest state: **one marking convention is detected, at least two
exist, and a `none` means "no convention this probe knows about" rather than
"unmarked".** The probe is left narrow rather than widened to guess, because a
detector that half-recognises a convention is worse than one that admits it does
not.

Format does not follow from purpose, measured across the three read:

| | doc 1 | doc 2 | doc 3 |
|---|--:|--:|--:|
| headings | 0 | 34 | 24 |
| table rows | 0 | 19 | 9 |
| math symbol lines | 0 | 36 | 0 |
| zero-width spaces | 0 | 100 | 0 |
| repeated labels | none | 6 | none |
| question marks | 22 | 25 | 23 |

## What document 3 added, extracted independently

71 candidates from 331 lines. Two special cases, and the first one is the worst
found so far.

**15. German inflection defeats exact matching, and it is not a corner case.**
`Thermodynamik` as a noun occurs **zero times** in a document that argues about
thermodynamics five times — as `thermodynamischen` (4) and `thermodynamischer`
(1). A string-keyed census records the term as absent.

Worse on a term that carries a conflict: **`emergent` appears in seven distinct
surface forms** — Emergente, Emergentes, emergente, emergentem, emergenten,
emergenter, emergentes — 13 occurrences, beside 13 of the noun `Emergenz`. A
string-keyed index sees eight terms where there is one. Document 2 has the same
split in different proportions (20 nouns, 8 adjectives across four forms).

This is the case for stemming, and it is also the case *against* doing it
blindly: `Negentropie` contains `entropie` and means its opposite, so a stemmer
that is merely aggressive merges a term with its negation.

**16. A document abbreviates its own central term halfway through.**
`Kael-Julia-Bindung` 16 times, then `K-J-Bindung` 5 times from ^[L151]. Nothing
announces the switch. Document 2 did the same thing by a different route — its
summary table renaming five of eight protocols — so **two of three documents
rename their own terms internally.**

## The three-way comparison changed the pair's rule

`Wiki/compare/002` supersedes `001`, which is itself a finding: **a comparison
written at n=2 should expect to be superseded.**

Five terms appear in all three documents; sixteen of 33 appear in exactly one.

001 said string identity is anti-correlated with semantic identity. With three
documents a sharper statement holds: **of the five terms in all three, the three
the project owns each carry a conflict and the two it borrowed carry none.**

A borrowed term is stable because its meaning is anchored outside the corpus. A
project term drifts because nothing anchors it. So the test for where conflicts
live costs no reading at all — *does this word mean something outside this
project?* — and is made once per term.

**`Kohärenz` is the proof.** One occurrence in document 1, 48 in document 2, 25
in document 3, and two incompatible senses that only emerged at n=3: system
stability measured by redundancy, and truth-by-self-consistency, which document 2
criticises as risking solipsism. **A reading of document 1 would have dropped it
entirely** — it carries nothing there on its own, and it is in the census only
because the census is exhaustive.

## Document 4, and the first fabricated identifier

`guardians-und-kern-welten-konzept`, `worldbuilding`, chosen from
`scripts/profile.py --summary` because that category has a median of **2
headings** against `theorie-physik`'s 23 — the sharpest structural contrast in
the corpus. **Selection may use knowledge of other documents; extraction may
not.** Recorded as a rule, because it is the one place cross-document knowledge
is legitimate.

**17. The census frontmatter was typed, and one field was invented.** The
`drive_id` written into the census was a fabrication — a plausible-looking Drive
identifier that belonged to nothing. It was caught by comparing against the
manifest, and it would have been invisible otherwise: a wrong id looks exactly
like a right one, and it breaks the single guarantee the repository rests on.

The response is not care. `scripts/profile.py --frontmatter <slug>` now emits the
census header from the manifest, so the field is copied rather than typed, and
every existing census and note was checked against the manifest — all seven match.

**18. Sixteen repeated labels that are a schema, not a stance.** Nine fields per
Guardian, eight per world, filled uniformly for five and four entities. The
`repeated labels` probe counts them correctly and they mean something entirely
different from document 2's `Beschreibung`/`Bewertung`. **The same probe finds
two unrelated things**, and only reading tells them apart.

That the corpus contains a **filled page schema for exactly the kind of entity
the wiki builds pages for** is worth more than the census entry: it is a page
format somebody already designed against this material.

**19. A document's own count contradicts its own content, and it says so.** „die
vier zentralen Hüter" against five named Guardians — correct, because two share a
world, and flagged in a parenthetical at ^[L96]. A tally taken from the prose
without reading that line is off by one.

**20. Two `### A.` headings in one section**, at ^[L98] and ^[L110]. Heading-based
addressing collides, and the duplicate is in the source.

**21. Singular and plural split the count.** `Kern-Welten` 9, `Kern-Welt` 9 — one
term, two rows, each half the true frequency. Same class as the inflection
problem in document 3 and cheaper to fix.

## What the four-way comparison changed

`Wiki/compare/003` supersedes `002`, which superseded `001`. **Each comparison so
far has been superseded by the next**, which is now a pattern rather than an
accident.

**A rule keyed to "shared by every document" gets weaker with each document
added**, because the intersection shrinks — 002's five terms became one at n=4.
Keyed to "shared by three or more" it gets stronger. The conflict finding itself
survives the restatement.

**And a comparison cannot answer a question about the corpus.** The four read
documents never link `Partnerin` to `Juna`/`Julia`, and the obvious conclusion —
that the corpus does not — is false: **17 of the 23 documents using `Partnerin`
also use one of the names.** Only a check against all 409 could tell those apart,
and it has to be run separately and said separately.

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
