# Wiki/terms — the author's page for one term

A **term page** is written from a candidate page the author reviewed (decision 026), for
the author to work with: **German**, short, and every point tagged with its status and its
evidence (`GOAL.md` §1.2). It keeps apart what the project has **decided** — only an author's
decision carries `[K]` — and what the sources only **say**: `[S]`, research, never canon
(decision 006). The candidate page stays the ledger of every reading, and the term page
links to it rather than repeating it.

```yaml
kind: term page      # provisional — one instance (kishotenketsu), written by hand 2026-10-08
                     # may not: decide a reading, enter canon, stand in for the candidate page
                     # retire when: five term pages exist and the author has used none of them
```

| tag | means | must carry |
|---|---|---|
| `[K]` | the author decided it | a link to `Plan/decisions/`, an answered `Plan/weichen/` sheet, `Manuscript/kanon.md` or a decided conflict |
| `[V]` | a proposal | a source citation `^[slug.md:Lnn]` or a link into `Plan/` |
| `[S]` | a source says it | a source citation `^[slug.md:Lnn]` |
| `[L]` | a gap — nothing settles it | — |
| `[D]` | derived by whoever wrote the page | a link, or a path or command in backticks |

The sections, in order: Kurz · Was das Projekt entschieden hat · Was die Quellen sagen ·
Wo die Quellen auseinandergehen · In der Prosa · Offen · Autor-Notizen · Herkunft.
`## Autor-Notizen` holds the author's own block between `<!-- autor:anfang -->` and
`<!-- autor:ende -->`; no tool writes it and no rule applies inside it.

**1 <!--state:wiki.terms--> term page, 0 <!--state:wiki.terms_approved--> approved.**

```bash
python3 scripts/terms.py finds <slug>      # where the project's own records name the term
python3 scripts/terms.py scaffold <slug>   # a new draft; refuses a candidate the author has not reviewed
python3 scripts/terms.py check             # every rule above; on GitHub with every push
python3 scripts/terms.py approve <slug> --words "<the author's words>"
```

A draft is written by a session or the author; only the author approves. An approved page
is pinned (outside the author's block) and `check` fails when it changes. When its
candidate is re-reviewed or has readings waiting under `## Since review`, `check` notes
the term page as **behind** — it is still true of the state it names. The process, its
reasons and the questions it leaves: `Plan/concept/wiki-terms_2026-10-08.md`.
