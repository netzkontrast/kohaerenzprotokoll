---
step: extract
version: 4
covers_documents: 4
new_findings_last_document: 5
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
python3 scripts/profile.py <slug>                    # the structural facts
python3 scripts/profile.py --frontmatter <slug>      # the census header, from the manifest
```

**Never type a `drive_id`, title or date.** One was fabricated once, and a wrong
identifier looks exactly like a right one.

Note what the profile says before forming any impression: headings, tables,
invisible characters, repeated labels, escapes. The extraction changes shape
depending on them.

## 1 · Read the whole document, with line numbers, before counting anything

Write down every candidate while reading. **Counting first anchors the list to
whatever a regex proposes**, and roughly half of what has been found so far is
invisible to one.

Extraction starts at the first line after the frontmatter. Citations count from
line 1. Two line bases over one file, by design.

## 2 · Questions to carry while reading

**Surfaces — is one thing wearing several names?**

- Does an acronym also travel as a spelled-out role, or the reverse?
- Does a term appear in singular and plural, and would a count split them?
- Is anything inflected — a noun the document only ever uses as an adjective?
- Does a summary table, abstract or heading abbreviate a term the body spells out?
- Does the document switch to a short form partway through?
- Is there a term whose *idea* recurs where the *word* does not?

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

**Gaps — what is assumed?**

- Which terms are used as already known and defined nowhere here?
- Is the document's own root term among them?
- Are several named in one list or parenthesis and none explained?
- Does the document name something as undefined that it depends on?

**Self-consistency — does the document contradict itself?**

- Does a stated count match the content? Does the document flag it?
- Are heading labels unique? Do any collide?

**Export damage — what did the conversion do?**

- Invisible characters inside formulas, from flattened subscripts?
- Reference numbers glued to the words they annotate, from dropped superscripts?
- Backslash escaping inside terms and quotation marks?
- Typographic and ASCII quote glyphs mixed in one file?

Each of these defeats exact matching and quote verification **silently**.

## 3 · Count mechanically, and let the counts correct the list

A count that disagrees with the reading is usually right about the number and
wrong about the meaning. Both get recorded.

## 4 · Verify every number before it goes into prose

Numbers written from memory have been wrong three times so far. Re-run the count
for each one that appears in a sentence.

## 5 · Record afterwards

In the census: the profile, the candidates, and **what the extraction ran into**.

In this briefing, bump the header and add any question this document needed that
was not already here. **A finding no question anticipated is the measurement** —
if it stays high, the briefing is not yet carrying the method.

## What this briefing does not decide

Whether a candidate is really a term. Whether two surfaces are one thing. Whether
a disagreement matters. Those are the reasons a person is doing this.
