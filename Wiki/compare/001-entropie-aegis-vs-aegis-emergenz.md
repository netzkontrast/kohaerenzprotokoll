---
step: compare
inputs:
  - Sources/terms/entropie-aegis.md
  - Sources/terms/aegis-emergenz-aus-der-leere.md
compared: "2026-09-16"
---

# Compare — `entropie-aegis` × `aegis-emergenz-aus-der-leere`

Both censuses were written independently, from their own document only, using the
same template and the same structural probes. **Neither knew about the other.**
This file is the first time they meet, and it exists as a separate step so that
what the comparison finds is a result rather than an assumption carried in.

Two documents, same category, **two days apart**, both titled about AEGIS.

## The measurement

| | doc 1 `entropie-aegis` | doc 2 `aegis-emergenz-aus-der-leere` |
|---|---|---|
| kind | brief | critique |
| body words | 1,314 | 6,548 |
| headings | **0** | **34** |
| table rows | 0 | 19 |
| math symbol lines | **0** | **36** |
| zero-width spaces | 0 | **100** |
| glued ref numbers | 0 | **116** |

**Of 27 terms document 1 carries, 21 do not occur in document 2 at all.**
Of 25 terms document 2 carries, 24 do not occur in document 1.

The whole overlap is **six strings**: `AEGIS`, `Entropie`, `Zero-Trust`,
`Selbstorganisation`, `Kybernetik`, `Komplexität`.

## The inversion

The risk this step was built to catch was: *a term obviously important in one
document gets overlooked in the next, and that is where the conflict hides.*

**What the measurement shows is the opposite, and it is sharper.** Nothing was
overlooked. The terms are simply **absent** — Überwelt, Risse, Guardians,
Kern-Welten, Michael, Julia, DID, Negentropie, all zero in document 2. Document 2
never mentions the novel at all.

And every real conflict sits on a string the two documents **share**:

| shared string | doc 1 | doc 2 | relation |
|---|---|---|---|
| `AEGIS` | Autonomous Entropic Gatekeeper for Integrity Systems ^[entropie-aegis.md:L19] | Autogenic Emergent General Intelligence System ^[…leere.md:L17] **and** Autonomous Entropic Generative Integrity Substrate ^[…leere.md:L126] | **conflict** |
| `Entropie` | used 53×, undefined; three external senses commissioned ^[entropie-aegis.md:L29-33] | „schöpferische Matrix" ^[aegis-emergenz-aus-der-leere.md:L126], and the postulate's usage judged to „weicht signifikant von der Standarddefinition ab" ^[…leere.md:L130] | **conflict** |
| `Zero-Trust` | an AEGIS **sub-function** ^[entropie-aegis.md:L65] | **Zero-Trust-Architektur (ZTA)**, an external cybersecurity architecture used as a comparison point for ZTV ^[…leere.md:L67] | **not a conflict** |

**So string identity is anti-correlated with semantic identity here.** Where the
words differ the documents are simply about different things; where the words
match, they mean incompatible things. A conflict detector built on shared strings
would find three candidates in this pair and be wrong about one of them.

## The one false conflict, and why it is false

`Zero-Trust` is a named AEGIS sub-function in document 1 and the established
cybersecurity architecture ZTA in document 2, where it is a *yardstick* the
postulate is measured against and explicitly distinguished from:

> „ZTA verifiziert jedoch Zugriffsanfragen anhand von Identitäten, Gerätehygiene
> und vordefinierten Policies, **nicht allein durch interne Selbstkonsistenz**"
> ^[…leere.md:L67]

The true relation is not disagreement: **the project named a sub-function after
an existing architecture.** Recording it as a conflict would put a question to
the author that has an obvious answer, and `gather-term.md` predicted exactly
this failure class — *apparent conflicts outnumbering real ones* — which until
now had no supporting evidence. It has one.

## Quotation marks mean opposite things in the two documents

| | what quotation marks mark | examples |
|---|---|---|
| doc 1 | **invention** — the document is coining vocabulary | „Daten-Verwitterung", „Reinigungswellen", „Entropie-Signatur", „Überwelt" |
| doc 2 | **citation** — the document is quoting the postulate it attacks | „Entropie-Resonanz-Protokolle", „Realitätsurgrund", „schöpferische Matrix" |

Nothing in either document marks which convention is in force. The punctuation is
identical; the meaning is inverted.

**This is the finding with the widest consequences.** A citation checker reads a
quoted fragment as a promise about a source. In document 1 that promise is never
made, and a checker would report every coinage as a fabricated quote. In document
2 the promise is made about a document **that is not in the corpus** — the
postulate being criticised is not among the landed sources — so the quote cannot
be verified either.

## What this says about the process

**1. Independent extraction is what made the measurement possible.** Had document
2 been read with document 1's term list in hand, `Überwelt` and `Risse` would
have been searched for, not found, and recorded as absent — which is the same
answer. But `Zero-Trust` would have been recorded as a hit on a known term, and
the collision is only visible when the second reading says, on its own, *this is
an external architecture*.

**2. The comparison is largely mechanical and the censuses are not.** Diffing two
finished censuses is a script. Producing one is reading. The split is clean, and
it is where the tool boundary lies.

**3. Two documents may share a category and almost no vocabulary.** Both are
`theorie-physik`, two days apart. Category predicts nothing about term overlap.

## Carried to the term pages

- `AEGIS` — three expansions across the two documents, unresolved, both sources cited
- `Entropie` — the sense conflict, with document 2's own verdict on the deviation
- `Zero-Trust` — **one page, two referents**, marked as a naming relation rather than a disagreement
- Everything else — single-source, no conflict available yet
