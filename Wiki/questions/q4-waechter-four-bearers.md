---
id: Q4
question: Which of the four things the corpus calls „Wächter" is the term, and how do the pages avoid claiming the word?
status: open
raised_by: ["aegis", "guardians", "personas", "grenzfeste", "kael"]
documents: ["guardians-und-kern-welten-konzept", "aegis-subplots-kapitelweise-system-exploration-docx", "kohaerenzprotokoll-aegis-und-systementropie", "roman-lokalitaeten-konzept-und-ausarbeitung"]
conflict: none — nothing contradicts anything; one word is simply doing four jobs
gathered: "2026-09-17"
---

# Q4 — one German word, four bearers

Found while reconciling document 5, when `Wächter` matched an alias already on
the [[aegis|AEGIS]] page and the match was wrong.

| # | what `Wächter` names | where | line |
|--:|---|---|--:|
| 1 | **AEGIS itself**, as „Wächter der systemischen Stabilität" | on the [[aegis]] page, from document 3 | — |
| 2 | **a Persona**, the one who primarily experiences the [[grenzfeste|Grenzfeste]] | `guardians-und-kern-welten-konzept` | 85 |
| 3 | **a Guardian**, in a subplot title — „Das Dilemma des Wächters" | `aegis-subplots-kapitelweise-system-exploration-docx` | 279 |
| 4 | **[[kael|Kael]]**, in the novel's final image | `aegis-subplots-kapitelweise-system-exploration-docx` | 531 |

The fourth is explicit:

> „Kael übernimmt vielleicht eine neue Rolle als eine Art Moderator oder Wächter
> dieser neuen, fragilen Ordnung." ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L531]

## Why this is not a conflict

No source contradicts another. German uses one word where the corpus has four
roles, and each use is locally correct. **The defect would be a page claiming the
word** — and one nearly did: `aegis` carries „Wächter der systemischen
Stabilität" as an alias, which is a *phrase*, but the index folds it to a key
that a bare `Wächter` matches.

## The pattern, which is what makes this worth a page

There is a distribution, and it is not random. In document 5, `Guardian` stands
alone 22 times across every analytic field; `Wächter` appears three times and
**never in analysis** — twice in invented subplot titles, once inside one.
**The English word is the analytic register and the German one the fictional
register.** If that holds across more documents it is a stance signal, not a
synonym.

## What would answer it

- Any document using `Wächter` in an analytic sentence would break the register
  pattern and make it a plain synonym problem.
- A glossary or an architecture document naming one bearer canonically.
- More [[personas|Personas]] named: if several are role-nouns like `Architekt`, `Echo`,
  `Funke`, `Sucher` and `Wächter`, then bearer 2 is a naming convention rather
  than a collision, and the question shrinks to three.

## Related

Judgement `J20` in `Plan/runs/judgements.jsonl`, whose rule is that `Wächter`
is never resolved by the surface.

## 2026-09-17 — document 6 breaks the register pattern, which was the test this page named

This page said what would answer it: „Any document using `Wächter` in an
analytic sentence would break the register pattern and make it a plain synonym
problem."

`roman-lokalitaeten-konzept-und-ausarbeitung` does exactly that, and further.

| | document 5 | document 6 |
|---|--:|--:|
| `Guardian` standing alone | 22 | **0** |
| `Wächter` standing alone | 3 | **12** |
| `Wächter` in an analytic sentence | 0 | 12 |

**`Guardian` does not occur in document 6 at all**, in 12,022 words that specify
the four bearers, their domains and their infrastructure:

> „die Domänen der jeweiligen Wächter (LogOS, Mnemosyne, Cerberus,
> Kairos/Sophia)" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L35]

> „Sitz von AEGIS und den Wächtern in ihrer Systemfunktion."
> ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L176]

### So the register hypothesis is wrong, and it was a measurement

„The English word is the analytic register and the German one the fictional
register" held on one document and fails on the next. **The distribution tracks
the document, not the register** — document 5 is an English-leaning subplot brief
and document 6 is a German worldbuilding catalogue, and each uses one word
throughout.

That removes the stance reading of bearer 3 and turns it into what it looked like
at first: a synonym problem across documents.

### A fifth use, and it is the ordinary German one

> „Cerberus (als Wächter der Mauer)" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L370]

Here `Wächter` is neither AEGIS, nor a Persona, nor the class of four, nor [[kael|Kael]] —
it is one of the four named as keeper of a specific structure. **Five bearers
now**, and the pattern that makes them one word is grammatical rather than
narrative.

### What still must not happen

A page claiming the word. The `aegis` alias „Wächter der systemischen Stabilität"
still folds to a key a bare `Wächter` matches, and document 6 would now map every
one of its twelve analytic uses onto `aegis` by lookup if `Wächter` were added as
a surface anywhere. **It was not added.** See `J33`.

### What would answer it now

A glossary, or any source that uses both `Guardian` and `Wächter` in the same
analytic passage and distinguishes them. Two documents each using one word
exclusively cannot settle whether the words differ.
