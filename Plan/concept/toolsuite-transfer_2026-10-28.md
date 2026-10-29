# What the toolsuite took from the other repositories (2026-10-28)

The author's instruction of 2026-10-28: look at every repository given to this session and bring the most useful things
into this repository's toolsuite. The survey of all 31 repositories is
[rebuild-with-agency_2026-10-26.md](rebuild-with-agency_2026-10-26.md) §6, one row per repository with what to take and
what must not come. This round builds from that matrix. It does not survey the repositories a second time.

**How the items were chosen.**
- Mechanical only: nothing that decides canon, judges prose or calls a model.
- First, what the pilot of Kap 1 Szene 1 showed was missing
  ([pilot ledger](../runs/writing/kap-01/pilot-szene-1_2026-10-27.md), F1–F12).
- Then what guards a surface that is now public (decision 032).

Each item is one standard-library script or one function. Each has a self-test that can fail, is registered in
`selftests.py` as a `std` suite, and has a row in `scripts/README.md`. None is in CI: adding a CI step is the
author's call.

## Taken

| from | what | here | the pilot entry or rule it answers |
|---|---|---|---|
| `writer-skills` (per-scene knowledge test: a scene is read against what must or must not be in it) | a decided sentence that names a scene is a duty of that scene | `brief.py duties()`; the briefing lists `Pflicht Szene N` under *Entschieden*; `manuscript.py check` prints each duty as a query and records `pflichten N zu lesen` in the scene head | F10, F11 |
| `writing-intelligence` (voice-metric vector with a drift direction) | German sentence and paragraph rhythm; the word-level diff of two versions | `voice_metrics.py measure · compare · baseline · check` | pilot step 5 (the diff between draft and the author's version); step 6 (a baseline from approved text only) |
| `agent-file` (share gate: scan exported state before it leaves) | scan the built website for what the MCP server withholds | `share_check.py`, importing `rag.WITHHELD_LINE` | decision 029 §3 withholds those lines on `/mcp`, but the frames were never scanned; Q-aegis-agent-pilot-01 |
| `worldbuilder` (per-kind schema, cross-reference check) | every reference on a figure or world card resolves | `cards.py check` | "a link is never inferred": worldbuilder's auto-fix is left behind |
| `narrative-context-protocol` (Core 3.0.0-rc.1, Dramatica profile 1.0.0-rc.1; "preserve, do not normalise") | the emitted NCP document against byte-pinned copies of both schemas, plus three cross-checks Core accepts and should not | `ncp_check.py`; `Plan/storyform/ncp/schema/` (from afa8d86); a `std` suite for the cross-checks, a `jsonschema` suite for the schemas (`not run` without the package) | second round, 2026-10-28 |
| `lit-critic` (cross-run finding identity, dispositions that follow a finding) | an editor's finding keeps its identity across runs; the author's disposition follows it | `findings.py import · list · dispose`, `Plan/runs/writing/ledger.jsonl` | ported as a design. lit-critic keys with Python's salted `hash()`; here the key is sha256 of the file and the verbatim line |

## What running them found, on the first day

- **Szene 1 has six duties.**
  - Two are the ones the continuity read found: W28 (the Löschliste) and W20 (the line that shows the maintenance falls to Kael).
  - A third duty was missed by both reads of the draft. The W7 answer says, for Szene 1: „Kaels Name fällt, weil die alte Frau fragt.“
    The draft has no name and no question.
  - The other three are W2, W3 and SP. The draft carries them, as far as the author's reading will show.
  - Every duty is a query. No code judges one answered.
- **The published frames carry the withheld names.**
  - Scope: `share_check.py` over `Plan/derived/web` and `Plan/derived/ui`.
  - Count: 6,364 matches in 9 files, 5,545 of them as whole words. In `Main.dc.html` alone: 959 matches, 796 as whole words.
  - Most whole-word matches are two of the names. The other matches sit inside other words, because `rag.py`'s pattern has no word boundaries.
  - The earlier figure of 883 in the session's question was a different count, not a measurement of this.
  - The check changes nothing. The frame scrub stays the author's question.
  - The pattern's lack of word boundaries also makes `/mcp` withhold harmless lines (a line containing „Foreshadowing“).
    That errs toward withholding. Whether to bound it is the author's rule (decisions 028, 029), so it is left as it is.
- **The NCP document passes both schemas**, and none of the three cross-checks fires. Core itself accepts a payload
  without a declaration and a version mismatch between the two; the probe that showed it is in the script's docstring.
- **The cards are clean.** `cards.py check` gives 0 findings over 28 cards.
- **The ledger holds the pilot's two editor reports.** 19 sightings, 18 findings. One line was cited by both reports; it is one finding, seen twice.

## Not taken this round, and why

From §6, still open, each one waiting on something named:
- the `development.json` shadowing check (`BuildYourOwnHarness`) — **already there**: `storyform.py`'s
  `development_audit` refuses any field outside the chapter fields („structural overrides are not allowed“), every
  storypoint that does not resolve in `a.json`/`b.json`, and every storypoint the weave does not give the chapter.
  Nothing to transfer;
- the layer scope lint (`self-driving-agents`) — deferred: `Plan/derived/` holds 591 entries, most of them per-document files, from
  many writers, and declaring each view's reads and writes is the store inventory `SPEC.md` §9 owes first;
- the settled-directions registry (`epistemic-protocols`) — a registry is only as good as its entries, and which
  directions count as settled is the author's to say; an empty registry would be a dormant surface;
- the setup/payoff ledger (`writer-skills`). It waits on question 6 of the rebuild concept: where 734, the Genesis steps and the Vortex are planted;
- the style check (`lit-critic`). It needs a style sheet whose syntax the author approves. `prose_rules.py` already checks the confirmed rules mechanically;
- the pressure coach (`literary-skills`), the prompt-brief (`prompt-architect`), the flag-only reviewer (`dspy-agent-skills`) and the calibration (`metadpy`).

**The rule held for every item:** no item writes `Manuscript/`, `Wiki/` or `Sources/`, decides a reading or a duty,
or sends text anywhere. Four of them read the author's words and record them only verbatim.
