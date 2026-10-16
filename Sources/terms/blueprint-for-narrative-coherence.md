---
source: Sources/drive/blueprint-for-narrative-coherence.md
drive_id: "1KpldnyuDAmZK5uG7EpMAS3CUl-0TRxAizwqf5BHG9uw"
title: "Blueprint for Narrative Coherence"
category: plot-outline
index_date: "2025-10-15"
extracted: "2026-10-14"
candidates: 23    # the terms capture.py counted
---

# Term census — Blueprint for Narrative Coherence

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py blueprint-for-narrative-coherence`

```
  lines                77  (frontmatter ends at 9)
  body words           1574
  headings             2   bold-only lines 0
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    12   ascii quotes 8
  invisible characters none
  math symbol lines    0
  glued ref numbers    6
  repeated labels      none
  longest line         915 chars
```

## Stance, read per passage

The document is a narrated scene, not a report or a lock. Its heading reads „# **Chapter 1: The Whisper of Construct City**“ ^[L13]; the export keeps the digit in the line, and `read.py --find` drops it, so the citation is the heading with its number left out: „Chapter: The Whisper of Construct City“ ^[L13]. It carries one such chapter heading and one closing heading, „Referenzen“ ^[L67].

Passage L17 to L65 is third-person narration in the past tense, close on Kael. It opens „The hum was the first law of physics“ ^[L17]. Inside it two registers mix. One is the scene, what Kael sees, smells and does. The other is an explaining voice that names what the scene stands for, for example „the core survival strategy of the Apparently Normal Part of the personality“ ^[L35] and „the bleed-through of Kiko, the terrified child-part, trapped in a perpetual freeze response“ ^[L39]. Italic lines are Kael's own thoughts, such as „Post-reboot artifact“ ^[L35], and the drone's movements are given as italic speech, „The system is coherent“ ^[L61]. Neither register carries a label; the grammar is the only marker.

Passage L67 to L76 is a numbered list of eight references: titles of other texts, the last with a site and an access date. The body text carries small numerals glued to the end of sentences, for example after „absolute efficiency“ ^[L17]; the profile counts 6 glued reference numbers. The list is the document's own claim about what it drew on, and its titles are not read as terms here.

The document says nothing about its own status, canon or lock.

## Candidates and counts

23 candidates, written while reading and frozen by the count (`Plan/runs/blueprint-for-narrative-coherence/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `blueprint-for-narrative-coherence.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[blueprint-for-narrative-coherence.md:#7] | 7 | 7 | 17, 19, 23, 25, 31, 53, 65 |  |
| `Juna` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 51 |  |
| `Kiko` ^[blueprint-for-narrative-coherence.md:#2] | 2 | 2 | 39, 51 |  |
| `AEGIS` ^[blueprint-for-narrative-coherence.md:#2] | 2 | 2 | 39, 51 |  |
| `Logos-Prime` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 21 |  |
| `Construct City` ^[blueprint-for-narrative-coherence.md:#2] | 2 | 2 | 13, 21 |  |
| `Kernwelt 1` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 19 |  |
| `The Foundation` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 39 |  |
| `Moonshine-Link` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 51 |  |
| `Apparently Normal Part` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 35 |  |
| `child alter` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 51 |  |
| `Coherence through Negation` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 21 |  |
| `Algorithmic Horror` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 23 |  |
| `Nichts Rauschen` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 23 |  |
| `Nothingness Noise` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 23 |  |
| `flackerndes Licht` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 31 |  |
| `central nexus` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 41 |  |
| `maintenance drone` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 59 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `cognitive dissonance` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 17 |  |
| `freeze response` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 39 |  |
| `phobic avoidance response` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 35 |  |
| `gaslighting` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 59 |  |
| `quale` ^[blueprint-for-narrative-coherence.md:#1] | 1 | 1 | 51 |  |

## What the extraction ran into

No candidate counts 0, and none counts fewer standing alone than with compounds. The explanation of each is therefore in the table: every surface stands in the form it was listed.

Four things the reading met. First, the document is English prose with two German phrases set in italics, `Nichts Rauschen` and `flackerndes Licht`; both are listed as written, and the German `Kernwelt 1` stands inside English narration. Second, the digit in the chapter heading is glued to the word in the export line; `read.py --find` drops digits glued to words, so the heading could only be cited without its number. Third, `cognitive dissonance` counts 1 case-sensitive and `read.py --count "cognitive dissonance"` gives 2 case-insensitively, because L31 writes it with a capital initial at a sentence start; the table row is the lower-case surface. Fourth, the export left reference numerals glued to sentence ends (the profile counts 6 glued numbers), and the two quotation-mark styles are mixed, 12 typographic marks against 8 ASCII quotes.

The terms `Kohärenz Protokoll` and `The Coherence Protocol` stand only inside titles of cited works in the reference list and are not listed. `read.py --count "Kohärenz Protokoll"` gives `Kohärenz Protokoll` ^[blueprint-for-narrative-coherence.md:#3], all of them in references. The only chapter-level content is the one chapter heading at L13; the words `Kap` ^[blueprint-for-narrative-coherence.md:#0] and `Kapitel` ^[blueprint-for-narrative-coherence.md:#0] stand 0 times.

**Zeros:** 0.

**Standing alone less often than with compounds:** 0.
