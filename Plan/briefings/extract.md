---
step: extract
version: 8
covers_documents: 6
new_findings_last_document: 3
---

# Briefing — before extracting a document

**Read this before opening the document. Read nothing else about it.**

This is the draft of the prompt the extraction step will eventually carry. It is
written as **questions about the document in front of you**, never as facts about
other documents — that distinction is what makes it safe to read first.

## Two kinds of knowledge, and only one contaminates

| | example | in this briefing |
|---|---|---|
| **document knowledge** | „`Überwelt` appeared in document 1, look for it" | **never** — it decides in advance what matters, which is the failure the census exists to prevent |
| **procedural knowledge** | „German inflection defeats exact matching" | **always** — it is what the last four documents taught about German Drive exports |

So: no slug, no count, no term from another document appears below. The evidence
behind each question is in `Plan/learnings/extract-terms.md`, which is read
**after** the first pass or when stuck — not before.

## 0 · Before reading

```bash
python3 scripts/capture.py <slug>                    # opens the run, writes 01 and 02
python3 scripts/profile.py --frontmatter <slug>      # the census header, from the manifest
```

`Plan/runs/<slug>/` now holds this run. **Every step writes into it** — that is
how the process becomes something that can be studied instead of something that
happened.

**Never type a `drive_id`, title or date.** One was fabricated once, and a wrong
identifier looks exactly like a right one.

Note what the profile says before forming any impression: headings, tables,
invisible characters, repeated labels, escapes. The extraction changes shape
depending on them.

## 1 · Read the whole document, with line numbers, before counting anything

**Write every candidate into `Plan/runs/<slug>/03-candidates.md` as you read,
one `- term` per line.** This is the only artifact of the run a program cannot
produce and the baseline any model gets scored against, so it is written *during*
the read, not reconstructed after.

`--count` refuses to run without it. **Counting first anchors the list to
whatever a regex proposes**, and roughly half of what has been found so far is
invisible to one.

Extraction starts at the first line after the frontmatter. Citations count from
line 1. Two line bases over one file, by design.

### What goes on the list (decision 012)

Two readers see the same things and list different amounts of them. The
selection is where they differ, so it follows a rule:

- **List** what the document names in the novel's world: a figure, a place, an
  object, an event, a law of its physics.
- **List** a word the document uses as its own term: it defines it, marks it
  (`[K]`, `[V]` …), sets it in bold, or heads a section or a table column with it.
- **List** a borrowed concept the document applies to the world, and mark it as
  lens: under a `## lens` heading, or with `(lens)` after it.
- **Leave out** a noun in its ordinary sense, a phrase of the argument, and the
  title of a cited work.
- **Write each surface as the document writes it.** Where the document joins two
  names, `A/B` or `A (B)`, list the joined form and each name.

Do not open the wiki to decide what to list; the census describes this document
and nothing else. After it is frozen, `reconcile.py` sweeps the text for every
surface of every page. So a term you judged ordinary is still found if the wiki
has a page for it, and nothing the wiki knows depends on this list.

**Write observations as paragraphs, never as `- ` bullets.** The count tells a
term from a sentence by punctuation, so a bulleted sentence without a comma is
counted as a candidate. A term that carries a comma — a title, `A, B` — is left
out of the count, and the count's header names it.
A term with an ordinal is left out the same way — a period and a space make
`1. Person` a sentence — so count it by hand in `05-verify.txt`. A bullet that
wraps is judged by its first line alone.

## 2 · Questions to carry while reading

**Surfaces — is one thing wearing several names?**

- Does an acronym also travel as a spelled-out role, or the reverse?
- Does a term appear in singular and plural, and would a count split them?
- Is anything inflected — a noun the document only ever uses as an adjective?
- Does a summary table, abstract or heading abbreviate a term the body spells out?
- Does the document switch to a short form partway through?
- Is there a term whose *idea* recurs where the *word* does not?
- Does the document write a suspended compound — „Funktions-, Phobie- … und
  Beziehungs-Profil"? Only the last member is written whole; list what is
  written, and expect an expanded member to count zero.

**Boundaries — is one name wearing several things?**

- Does one symbol or word carry more than one meaning here?
- Do two terms share a substring and mean different things?
- Is a term borrowed from a discipline, and does the document mean it that way?

**Marking — what is the document asserting?**

- Does the document label its own passages? With what, and what do the labels do
  — say how to read a passage, or name a field in a template?
- What do quotation marks mean **in this document**? They may mark invention, or
  citation of something else. Both occur; nothing announces which.
- Which candidates appear **only inside a question**? Those have no reading.
- Which appear only as something the document restates before rejecting?
- Does the document write samples in a voice, or lists of words a voice uses? A
  term that stands only there is diction — a reading needs a sentence about the
  thing, the same way a term inside a question has none.
- Does the document restate *other* documents — an index of locks, a list of
  sources with dates? That is this document's claim about them, not their text.

**Gaps — what is assumed?**

- Which terms are used as already known and defined nowhere here?
- Is the document's own root term among them?
- Are several named in one list or parenthesis and none explained?
- Does the document name something as undefined that it depends on?

**Self-consistency — does the document contradict itself?**

- Does a stated count match the content? Does the document flag it?
- Are heading labels unique? Do any collide?
- Does it name a conflict among its own sources? A conflict it reports has two
  sides, and only one of them may be in front of you.
- Does one word number more than one series — levels, layers, stages — so that
  „2" means two different things in two tables?
- Is every candidate written as *this* document writes it? A `0 word 0 in` after
  a reading is a name that came from somewhere else — memory of another source is
  the easiest contamination to miss.

**Export damage — what did the conversion do?**

- Invisible characters inside formulas, from flattened subscripts?
- Reference numbers glued to the words they annotate, from dropped superscripts?
- Backslash escaping inside terms and quotation marks?
- Typographic and ASCII quote glyphs mixed in one file?
- Emphasis inside a phrase — `*funktional* wütend`? The count reads the marked
  line, so the phrase counts zero; the quotation check reads it unmarked.

Each of these defeats exact matching and quote verification **silently**.

## 3 · Count mechanically, and let the counts correct the list

```bash
python3 scripts/capture.py <slug> --count            # writes 04-counts.txt
```

A count that disagrees with the reading is usually right about the number and
wrong about the meaning. Both get recorded. Its line numbers are **file** lines,
as a citation writes them.

## 4 · Verify every number before it goes into prose

Numbers written from memory have been wrong three times so far, and one
`drive_id` was fabricated outright. Re-run the count for each number that appears
in a sentence, **and write the commands and their output to
`Plan/runs/<slug>/05-verify.txt`** — a verification nobody can see is a claim
that it happened.

## 5 · Record afterwards

In the census: the profile, the candidates, and **what the extraction ran into**.

In this briefing, bump the header and add any question this document needed that
was not already here. **A finding no question anticipated is the measurement** —
if it stays high, the briefing is not yet carrying the method.

## What this briefing does not decide

Whether a candidate is really a term. Whether two surfaces are one thing. Whether
a disagreement matters. Those are the reasons a person is doing this.
