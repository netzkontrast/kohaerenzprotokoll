# 007 — Two documents may go to free models and Jev, to test the new tools

**Date:** 2026-09-24 · **Decided by:** the author, answering two questions · **Status:** chosen, enforced by `scripts/route.py`

## What was chosen

To test the tools installed on 2026-09-24 against real text, **two documents**
may be sent to third-party models, and nothing else from the corpus:

| document | why this one |
|---|---|
| `aegis-subplots-kapitelweise-system-exploration-docx` | document 5: a brief, with a reader's `03-candidates.md` written before counting |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | document 6: a gazetteer, with a reader's `03-candidates.md` and a second reading |

| service | allowed | how the limit is held |
|---|---|---|
| OpenRouter | **free models only** | a model is used only if its listed prompt and completion price are both 0 — checked in code on every call, never from a name |
| OpenRouter | **no provider that keeps prompts** | every request carries `provider.data_collection = "deny"`; a free model with no such endpoint answers 404 and is not used |
| TypeSafe (Jev) | per call | the same two documents; Jev saw these two already on 2026-09-23 |

The machine-readable form is `Plan/runs/route/consent.json`, and it is the one
encoding (P6): `route.py` refuses a call that declares any other document, and
refuses any request whose text contains a line of a landed document outside the
consent — so a tool that reads the wrong file is stopped by the router, not by a
prompt.

## Why these two and not the two named in the question

The question offered „two documents that already have a census and wiki pages,
e.g. `entropie-aegis` and `guardians-und-kern-welten-konzept`", and gave the
reason: so that each tool's output can be compared with what a person already
extracted. Measured afterwards, that reason rules the examples out.
`Plan/runs/README.md`: the first four documents' `03-candidates.md` are
**reconstructed from the finished census and cannot serve as a baseline for
scoring anything.** Documents 5 and 6 are the only two with a genuine reader's
list, they are the two the 2026-09-23 Jev test used — so TypeSafe sees nothing
new — and document 6 has a second, independent reading, which is where P27's
human ceiling (F1 0.66) comes from. Same answer, the two documents that can
carry it.

## What was rejected

- **Repository code and the tools' own examples only.** Nothing would leave the
  repository, and nothing would say how a tool reads *this* corpus — German,
  export-damaged, heavy with coined compounds. A review built on the tools'
  English demo texts would be a review of the demos.
- **Any landed document.** Not needed to answer the question, and each document
  sent is one more that a later decision cannot take back.
- **A paid cap of $2 or $10.** Free models only. A tool that no free model can
  serve is reported as **not reached** (P15) — never bought its way past.

## What it does not cover

- Notion. Nothing from the corpus goes to the Notion connector under this
  decision.
- Any document beyond the two, any later use of these two, and any paid model.
  Each is asked again, with its cost — the rule `NOW.md` already states for Jev.

## What would change our mind

A free endpoint that turns out to keep prompts despite `data_collection: deny`,
or a tool that sends text somewhere the router cannot see. Either ends the use
of free models for corpus text until the author decides again.
