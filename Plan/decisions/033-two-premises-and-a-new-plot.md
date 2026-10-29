# 033 — the world keeps two premises; a completely new plot is proposed

**Date:** 2026-10-28 · **Decided by:** the author · **Status:** the premises hold; the new plot is a proposal

## What was asked

The author, 2026-10-28, verbatim, in the conversation of the session on PR #198:

- „Mir gefällt der Plot noch garnicht - aber das worldbuilding - lass das mal als nächstes überholen“
- „Vielleicht sollten wir im ersten Kapitel rein aegis lesen… Millionen von Jahren Simulation“
- The two answers that followed, chosen from options the session put:
  - „Beides, Welt zuerst“, to „Was soll ich als Nächstes überholen?“;
  - „Kap 1 wird AEGIS“, to „Wie soll AEGIS' Simulation über Millionen Jahre ins Buch kommen?“.
- Then, interrupting the session before it acted on them: „Denk noch mal nach und Update zunächst deine Tools - und dann
  möchte ich nur noch die wahrheitstheorie und die Dual Kernel Theorie als worldbuilding Vorraussetzungen… bitte schlag
  mit einem komplett neuen Plot vor“
- And: „Einer der Spaß macht - wir sind immerhin im Information Universum. - also ist jeder Gedanke auch eine Projektion“

## What was chosen

1. **The world has two premises and no others: the Wahrheitstheorie and the Dual-Kernel-Theorie.**
   - Each is a card of `kind: voraussetzung` in `Manuscript/welt/`: `wahrheitstheorie.md` and `dual-kernel-theorie.md`.
   - Every chapter's briefing carries both (`brief.py`).
   - What the theories contain is what the sources say, cited on the cards as `[S]`. The author decided that they are
     premises, not which reading of them holds.
2. **The author's sentence „wir sind immerhin im Information Universum. - also ist jeder Gedanke auch eine Projektion“
   is recorded as the author's own reading of the premises**, on the Dual-Kernel card's `## Kanon`.
3. **Everything else that was world rests.** It is not deleted: the files stay, their ideas stay readable, and git
   keeps their history.
   - The six old world cards rest: `kernwelten`, `konstrukt-stadt`, `grauzone`, `grenzfeste`, `loeschwaerme`, `spindel`.
     Each carries `status: ruht` and `ruht_seit: "033"`.
   - The canon rows `Kernwelten` and `C9` rest. They are listed in `Manuscript/kanon.md` § Ruhend; the table keeps
     the author's words as they were given.
   - The tools read a resting card or row as history:
     - `brief.py` does not present it as decided;
     - `manuscript.py check` does not make a duty of it;
     - `cards.py lint` names every line of a text that leans on a resting world card, as a query.
   - The Landauer physics of the `loeschwaerme` card is not lost: the Landauer bridge is part of the Dual-Kernel-Theorie
     as the sources state it, so the premise card claims the word.
4. **A completely new plot is proposed**, in `Plan/runs/writing/book/neuer-plot_2026-10-28.md`.
   - It stands on the two premises only. It follows the author's answer that Kap 1 is AEGIS: millions of years of
     simulation.
   - It is a proposal, not canon (decision 006 and the rule at the head of `kanon.md`).

## What this does not decide

- **The old plot's decisions are not retired by this decision.** Its rows (storyforms A and B, the weave, the Weichen
  answered on 2026-10-27, W10-A/B, C14, Q3, the cards of the figures) hold until the author approves a new plot.
- The plot proposal lists, row by row, which of them it would overtake. Retiring them is one act of the author's,
  at the plot's gate, not a session's inference.
- **The prose rules in `Manuscript/regeln.jsonl` are not changed.**
  - Two of them, L5 (no AEGIS voice in Kap 1) and L3 (the first sentence of Kap 1 is Kael's), cannot hold beside
    the answer „Kap 1 wird AEGIS“.
  - The proposal names them. They are retired when the plot is.
- **Whether the theories carry the old vocabulary** (Coherons, Erasonen, the Persistenzgleichung, the Phase Alignment
  Lock) is open. The sources state it; the cards cite it as `[S]`; the proposal uses what it needs and marks it so.

## What was rejected

- **Deleting the old world cards and rows.** "A construct is demoted, not deleted" (CLAUDE.md). The Kernwelten and
  the Grauzone were the only way to ask some questions, and a new plot may want one back by the author's word.
- **Retiring the whole old plot now, on the strength of „Mir gefällt der Plot noch garnicht“.** A dislike asks for a
  proposal; it does not decide which of the old answers fall.

## What would change our mind

- The author names a third premise, or takes one of the two back.
- The author reads the proposal and keeps something of the old world. The resting card goes back to holding by a
  new decision, and its `status: ruht` line goes.
