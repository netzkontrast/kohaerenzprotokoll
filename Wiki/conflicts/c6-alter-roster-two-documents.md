---
id: C6
subject: Kael's Alter/Anteil roster — two complete, disjoint name sets
kind: two complete rosters for one system, no name in common
status: open
first_seen: "2026-09-17"
sources: 2
pages: ["alters", "kael"]
---

# C6 — two documents name Kael's inner system, and share no name

**Append-only.** This record decides nothing, and neither document that
supplies it has been changed by the other.

## The positions

| # | roster | size | source | ingested |
|--:|---|--:|---|---|
| 1 | `Limina`, `Nox`, `Echo`, `Flicker`, `Eos`, `Oblivion`, `Praetor`, `Index`, `Silas` (+ `Kael` as Host) | 10 | `charakterkonzepte-fuer-kohaerenz-protokoll` | reconciled |
| 2 | `Selene`, `Nyx`, `Kiko`, `Lia`, `Isabelle`, `Moros`, `Alex`, `Rhys`, `Lex`, `Argus` (+ `Kael` as the system) | 11 | `strukturelle-dissoziation-system-kael-analyse` | reconciled |

## The measurement

Word-boundary occurrence count, both directions, over the landed text of each
document:

- Every name in roster 1 occurs **0** times in
  `strukturelle-dissoziation-system-kael-analyse`.
- Every name in roster 2 occurs **0** times in
  `charakterkonzepte-fuer-kohaerenz-protokoll`.

Two apparent hits before the word-boundary check — `Lia`/`Lex` as substrings
of `Julia`/`komplex` and similar — were false positives and are excluded.
`Kael` is the one name both documents use, and he is the host/system, not an
Alter/Anteil in either roster.

**This is the same shape as `C5`**: a complete set for one thing in one
document, a complete and different set for the same thing in another, zero
overlap. It is the fourth and largest instance of the pattern this corpus's
Alter rosters keep producing — see [[alters]] and
`Wiki/questions/q3-how-many-kern-welten-and-alters.md`, where three earlier
rosters (from `roman-lokalitaeten-konzept-und-ausarbeitung`,
`kohaerenz-protokoll-konzept`, and `charakterkonzepte-fuer-kohaerenz-protokoll`)
already shared no names with each other before this fourth roster, now also
reconciled, was even counted in.

## Why it is not simply a naming difference

Nothing here suggests the same nine or ten [[alters|Alters]] wearing different names.
Both documents propose full, independent ten/eleven-item structures for the
same one psyche, with their own role-types and their own hedges — this
document's `Nox`/`Persecutor` and `Praetor`/`Protector` do not obviously map to
anything named `Selene` or `Moros`, because neither document offers a
cross-reference and no third source has yet named both.

## What this is not

**Not resolved by reconciling `strukturelle-dissoziation-system-kael-analyse`,
even now that it has been.** That document's reconciliation added its own
side of the record above (roster confirmed unchanged, both an `ehem.` former
name and an English epithet for each of its eleven Anteile — see
[[alters|Alters]]) and chose which roster the novel keeps for none of it. An
ingest proposes; it never resolves a conflict it is the second half of.

See `Plan/runs/judgements.jsonl` J83 for the one specific near-miss checked
directly: `Nyx` (roster 2) against `Nox` (roster 1), one letter apart and
zero-occurrence in both directions — `fold()` correctly keeps them apart.

## What would settle it

- A source that uses names from both rosters in one sentence.
- A source that states these are successive drafts of the same nine-or-so
  [[alters|Alters]], naming the correspondence rather than leaving it to be inferred from
  role-type alone.

Neither document's own reconciliation surfaced such a rule — both readings
are recorded on [[alters|Alters]] and neither cross-references the other.

## Not to be confused with

`C5`, the `Möglichkeits-Garten` scale conflict — the same "two complete sets,
zero overlap" shape, applied to locations rather than to [[alters|Alters]], and the first
conflict of that shape in the wiki.
