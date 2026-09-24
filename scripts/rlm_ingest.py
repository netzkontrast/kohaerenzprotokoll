"""Read one document with `dspy.RLM`, carrying this repository's own skills.

Three pieces, and the joins between them are the point:

- **`dspy_skills`** loads `.agents/skills/` the way Claude Code does. The
  manager discovers every skill, renders the `<available_skills>` block from the
  `description` field alone, and `activate` reads one skill's full `SKILL.md`.
  So the model is given the same instructions a person here is given, from the
  same file, with no second copy to drift.
- **`dspy.RLM`** runs the reading inside a sandboxed Python REPL. That matters
  more than context length: a census is counting, and a model that can *compute*
  over the text does not have to be believed about how many times a word occurs.
- **`scripts/read.py`** supplies the document already prefixed `NNN| `. Left to
  count for itself the model reported 690 lines where this project counts 691 —
  the two-line-bases trap, frontmatter against file. Handing it the numbering
  removes the question instead of hoping.

## Why every candidate must carry a line, and the line is checked

The first run of this program failed, and the failure is the reason the rule
below exists. The model ran out of REPL budget before it had read the whole
document, and its reasoning then says, in as many words:

> „We have full document variable inaccessible except history outputs. Need
> leverage all shown snippets … We can reconstruct from outputs."

**It was about to reconstruct the document from its own truncated scrollback and
hand the result over as a reading.** Nothing was written only because the answer
failed to parse. A reconstruction is exactly what `trainset.py` refuses four
candidate lists for, and in a model it is invisible: the list looks the same.

So a candidate is not accepted on its word. Each one must come back as
`- term  ^[Lnn]`, and every line is verified against the document by the same
comparison `quotes.py` uses. A candidate whose cited line does not contain it is
**unverified**, and the header records how many there were. A list that is mostly
unverified is a reconstruction and says so, in the one field `state.py` reads.

## What this may not do, and does not

**It writes `03-candidates-rlm.md`, never `03-candidates.md`.** The gold list is
written by a reader while reading; a model's list is the thing gold is used to
score, and the two must never be able to become each other. `written_by:` records
which is which and `state.py` reads that line.

It proposes and stops. No page, no judgement, no conflict, no census is written
from here — those are decisions, and an ingest proposes rather than resolves.

## What changed on 2026-09-23, from reading nine DSPy repositories against this one

- **The cache is off.** `dspy.LM` caches by default; a cached run replays its
  first completion and cannot measure reliability (P18).
- **`max_llm_calls` is set, and `--sub-model` may name a cheaper `sub_lm`.**
  Budget is a parameter, not a surprise — the first run ran out of REPL budget
  and began reconstructing from scrollback.
- **`find_line` and `count` are passed to the REPL as tools.** The model can
  *ask* for a line the way a person here asks `read.py --find`, instead of
  reading one off the prefix and typing it (P26, inside the sandbox).
- **A second verification tier: reach.** A candidate whose cited line holds it
  still passes the first tier even when the whole list comes from the first
  third of the document. `reach()` measures how far the verified citations go
  and in how many tenths of the document they fall; a list that never cites
  past 90% of the document did not read to the end, whatever it says.
- **`--approval` is required**, naming the author's decision — this sends a
  whole corpus document to OpenRouter (`NOW.md`).
- **The key comes from the environment**, as `CLAUDE.md` says, and from `.env`
  only as a fallback.
- **A forced answer is never a reading** (2026-09-24). When `max_iters` runs
  out, `dspy.RLM` has an extract step build the outputs from the trajectory and
  sets `final_reasoning` to „Extract forced final output"; the list looks like
  any other. The header now says `forced: yes`, and the verdict is PARTLY
  RECONSTRUCTED whatever the list cites.

Usage:
    .venv-dspy/bin/python scripts/rlm_ingest.py <slug> --approval "<decision>"
        [--model M] [--iters N] [--calls N] [--sub-model M]
    .venv-dspy/bin/python scripts/rlm_ingest.py <slug> --score   # against the human list
    python3 scripts/rlm_ingest.py --selftest                      # tools and reach, offline
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

SKILLS = ROOT / ".agents" / "skills"
RUNS = ROOT / "Plan" / "runs"
# Free, and it answers a structured-output request — 18 of the 24 free models on
# OpenRouter do not, and `RLM` needs one, so the choice is narrower than it looks.
# `nex-agi/nex-n2.5-pro:free` also qualifies and was the first default, but it
# returns its final answer in `reasoning_content` with `text: None`, which DSPy's
# adapter rejects as an empty response. Worth re-testing; not worth losing a run to.
DEFAULT_MODEL = "openrouter/nvidia/nemotron-3-super-120b-a12b:free"
BASE = "https://openrouter.ai/api/v1"


def api_key() -> str:
    """From the environment's settings, else the git-ignored .env; never printed."""
    if os.environ.get("OPENROUTER_API_KEY"):
        return os.environ["OPENROUTER_API_KEY"]
    env = ROOT / ".env"
    for line in (env.read_text(encoding="utf-8").splitlines() if env.exists() else []):
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no OPENROUTER_API_KEY in the environment or .env")


def tools_for(slug: str):
    """Host-side tools the REPL may call: ask for a line, count a term.

    Both answer with this project's own comparison (`read.locate`,
    `quotes.normalise`), so a line the model gets from `find_line` passes the
    verification below by construction.
    """
    import quotes
    import read
    from subject import document
    doc = document(slug)

    def find_line(words: str) -> str:
        """The file lines holding these exact words, as ^[Lnn]; or NOT FOUND and the nearest."""
        hits = read.locate(doc, words)
        if hits:
            return " ".join(f"^[L{n}]" for n in hits[:20])
        near = read.nearest(doc, words)
        return "NOT FOUND. nearest: " + ", ".join(f"L{n} ({share:.0%})" for share, n, _ in near)

    def count(term: str) -> int:
        """How many lines contain this term, by the same normalisation citations use."""
        wanted = quotes.normalise(term)
        return sum(1 for line in doc.lines() if wanted and wanted in quotes.normalise(line))

    return [find_line, count]


def reach(slug: str, good_lines: list[int]) -> dict:
    """Tier 2: how far into the document the verified citations go, and how evenly."""
    from subject import document
    doc = document(slug)
    first, last = doc.offset, doc.offset + len(doc.lines()) - 1
    span = max(last - first, 1)
    tenths = {min(9, (n - first) * 10 // span) for n in good_lines if first <= n <= last}
    furthest = max(good_lines, default=first)
    return {"furthest": furthest, "last": last, "share": round((furthest - first) / span, 3),
            "tenths": len(tenths)}


def briefing(skill: str = "ingest") -> tuple[str, str]:
    """(the skills block every agent sees, the one skill's full instructions)."""
    from dspy_skills import SkillManager, generate_skills_prompt_block, read_instructions
    manager = SkillManager([SKILLS])
    manager.discover()
    loaded = manager.activate(skill)
    return generate_skills_prompt_block(manager), read_instructions(loaded.path)


def numbered(slug: str) -> str:
    import read
    from subject import document
    doc = document(slug)
    last = doc.offset + len(doc.lines()) - 1
    return "\n".join(read.numbered(doc, doc.offset, last))


TASK = """You are reading one German research document for a term wiki.

{skills}

The `ingest` skill is active. These are its full instructions; follow the parts
that apply to reading and proposing candidates, and ignore the parts that write
files — you produce one list and nothing else:

{instructions}

The document is in the variable `document`. **Every line is already prefixed with
its file line number** in the form `NNN| `. Use those numbers; do not renumber,
and do not compute line positions yourself — the prefix is the project's own
numbering and a citation that uses it is checkable.

Produce an exhaustive list of candidate terms: every name, coinage, acronym,
compound or piece of vocabulary this document treats as a thing in its world.
German capitalises every noun, so capitalisation tells you nothing — use the
REPL to count and to look, not to decide.

**Every candidate carries the line you found it on**, in this exact form, one per
line and nothing else:

    - Kern-Welt  ^[L152]

The line number is the `NNN` prefix of a line that actually contains the term.
It is checked against the document afterwards, so a number you did not read off a
line will be reported rather than believed. If you have not read a part of the
document, say so in one final line beginning `- UNREAD ` — an incomplete reading
is a fact, and a reconstruction offered as a reading is the one thing this step
must never produce.

No commentary, no numbering, no counts."""


CITED = re.compile(r"^-\s*(?P<term>.+?)\s*\^\[L(?P<line>\d+)\]\s*$")

# dspy.RLM's own marker when max_iters runs out: it then asks an extract step to
# build the outputs from the trajectory, and the answer looks like any other
# (DSPy 3.3.1 dspy/predict/rlm.py; measured offline, check_dspy_skill.py
# `rlm-forced-final-output`). That is the reconstruction this file exists to refuse.
FORCED = "Extract forced final output"


def judge(share: float, unread: list, uncited: list, reach_share: float, forced: bool) -> str:
    """The header's verdict. A forced answer is never a reading, whatever it cites."""
    if forced:
        return "PARTLY RECONSTRUCTED — the REPL ran out of iterations and DSPy forced the answer"
    from gold import IN_DOCUMENT  # the bar a list must clear to be a reading of the document
    if share >= IN_DOCUMENT and not unread and not uncited and reach_share >= 0.9:
        return "a reading — every candidate carries a line that holds it, and they reach the end"
    return "PARTLY RECONSTRUCTED — treat as a draft, not as a reading"


def verified(slug: str, rows: list[tuple[str, int]]) -> tuple[list[str], list[str]]:
    """(candidates whose cited line really contains them, the rest). Tier 1."""
    import quotes
    from subject import document
    doc = document(slug)
    lines = doc.lines()
    good, bad = [], []
    for term, number in rows:
        index = number - doc.offset
        line = quotes.normalise(lines[index]) if 0 <= index < len(lines) else ""
        target = good if quotes.normalise(term) and quotes.normalise(term) in line else bad
        target.append(term)
    return good, bad


def run(slug: str, model: str, iters: int, calls: int, sub_model: str | None,
        approval: str | None) -> Path:
    import dspy
    if not approval:
        raise SystemExit("--approval is required: this sends a whole corpus document to "
                         "OpenRouter. Name the author's decision that allows it (NOW.md).")
    skills, instructions = briefing()
    lm = dspy.LM(model, api_key=api_key(), api_base=BASE, max_tokens=16000, temperature=0,
                 cache=False)
    sub = (dspy.LM(sub_model, api_key=api_key(), api_base=BASE, max_tokens=8000,
                   temperature=0, cache=False) if sub_model else None)
    dspy.configure(lm=lm)
    rlm = dspy.RLM("document: str, task: str -> candidates: str", max_iters=iters,
                   max_llm_calls=calls, tools=tools_for(slug), sub_lm=sub)

    started = time.time()
    with dspy.track_usage() as usage:
        result = rlm(document=numbered(slug),
                     task=TASK.format(skills=skills, instructions=instructions)
                     + "\n\nTwo tools are available in the REPL: `find_line(words)` returns "
                       "the ^[Lnn] of the lines holding those exact words, and `count(term)` "
                       "the number of lines holding a term. Prefer `find_line` to reading a "
                       "number off a prefix.")
    elapsed = time.time() - started
    tokens = usage.get_total_tokens() if usage else {}

    rows, unread, uncited = [], [], []
    for raw in str(result.candidates).splitlines():
        line = raw.strip()
        if line.startswith("- UNREAD"):
            unread.append(line[2:].strip())
            continue
        match = CITED.match(line)
        if match:
            rows.append((match.group("term"), int(match.group("line"))))
        elif line.startswith("- "):
            uncited.append(line[2:].strip())

    good, bad = verified(slug, rows)
    total = len(good) + len(bad) + len(uncited)
    share = len(good) / total if total else 0.0
    lines_of = dict(rows)
    tier2 = reach(slug, [lines_of[t] for t in good if t in lines_of])
    forced = str(getattr(result, "final_reasoning", "")) == FORCED
    quality = judge(share, unread, uncited, tier2["share"], forced)

    out = RUNS / slug / "03-candidates-rlm.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"written_by: dspy.RLM, model {model}, {iters} iterations, {elapsed:.0f}s — {quality}\n"
        f"ran: {date.today().isoformat()}\n"
        f"verified: {len(good)} of {total} candidates cite a line that contains them\n"
        f"reach: verified citations go to L{tier2['furthest']} of L{tier2['last']} "
        f"({tier2['share']:.0%}), in {tier2['tenths']} of 10 tenths of the document\n"
        f"forced: {'yes — the REPL ran out of iterations and DSPy extracted this answer from the trajectory' if forced else 'no'}\n"
        f"cost: {tokens}\n"
        f"approval: {approval}\n\n"
        f"# Candidates (model) — {slug}\n\n"
        "> **Not a gold list.** A gold candidate list is written by a reader while\n"
        "> reading, before any count. This is the thing gold is used to score.\n\n"
        + "\n".join(f"- {t}" for t in good)
        + ("\n\n## Unverified — the cited line does not contain the term\n\n"
           + "\n".join(f"- {t}" for t in bad) if bad else "")
        + ("\n\n## Uncited — no line given, so nothing could be checked\n\n"
           + "\n".join(f"- {t}" for t in uncited) if uncited else "")
        + ("\n\n## The model said it did not read:\n\n"
           + "\n".join(f"- {u}" for u in unread) if unread else "") + "\n",
        encoding="utf-8")
    print(f"{len(good)} verified of {total} in {elapsed:.0f}s "
          f"({len(bad)} unverified, {len(uncited)} uncited) -> {out.relative_to(ROOT)}")
    if unread:
        print("the model reported unread parts:", "; ".join(unread)[:200])
    if forced:
        print(f"the REPL ran out of its {iters} iterations; the answer was forced, not submitted")
    return out


def score(slug: str) -> int:
    """The model's list against the reader's, by this project's own fold()."""
    from capture import candidate_terms
    from wiki_index import fold
    try:
        from drg.evaluation._runner import _score_sets
    except ImportError:
        raise SystemExit("drg-kg is not installed in this interpreter")

    gold_path, pred_path = RUNS / slug / "03-candidates.md", RUNS / slug / "03-candidates-rlm.md"
    for path in (gold_path, pred_path):
        if not path.exists():
            raise SystemExit(f"missing {path.relative_to(ROOT)}")
    from gold import refusal
    if refused := refusal(slug):
        raise SystemExit(refused)
    gold = candidate_terms(gold_path.read_text(encoding="utf-8"))
    pred = candidate_terms(pred_path.read_text(encoding="utf-8"))
    metric = _score_sets(gold, pred, key_fn=fold)

    print(f"gold {len(gold)} candidates, model {len(pred)}")
    print(f"precision {metric.precision:.2f}  recall {metric.recall:.2f}  F1 {metric.f1:.2f}")
    print(f"\nmissed ({len(metric.details['false_negative_keys'])}) — the reader had these:")
    for key in metric.details["false_negative_keys"][:25]:
        print(f"  {key}")
    print(f"\ninvented ({len(metric.details['false_positive_keys'])}) — the model had these:")
    for key in metric.details["false_positive_keys"][:25]:
        print(f"  {key}")
    print("\nA miss is not automatically an error and an invention is not automatically\n"
          "wrong: the reader's list is one reader. Two independent readings of one\n"
          "document differed by 109 against 143 candidates.")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    if argv == ["--selftest"]:
        return selftest()
    parser.add_argument("slug")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--iters", type=int, default=12)
    parser.add_argument("--calls", type=int, default=40, help="max_llm_calls for the REPL")
    parser.add_argument("--sub-model", default=None, help="a cheaper sub_lm for REPL queries")
    parser.add_argument("--approval", default=None, help="the author's decision allowing this run")
    parser.add_argument("--score", action="store_true")
    args = parser.parse_args(argv)
    if args.score:
        return score(args.slug)
    run(args.slug, args.model, args.iters, args.calls, args.sub_model, args.approval)
    return 0


def selftest() -> int:
    """The tools and the reach tier, on a real landed document, with no model."""
    slug = "aegis-subplots-kapitelweise-system-exploration-docx"
    find_line, count = tools_for(slug)
    failures = []
    from subject import document
    doc = document(slug)
    line = next(i for i, l in enumerate(doc.lines()) if len(l.split()) > 6) + doc.offset
    words = " ".join(doc.lines()[line - doc.offset].split()[:5])
    if f"^[L{line}]" not in find_line(words):
        failures.append(f"find_line did not return L{line} for words on it: {find_line(words)!r}")
    if not find_line("Dieser Satz steht in keinem Dokument dieses Korpus").startswith("NOT FOUND"):
        failures.append("find_line answered for words the document does not contain")
    if count("AEGIS") < 1:
        failures.append("count found no AEGIS in a document about AEGIS")
    last = doc.offset + len(doc.lines()) - 1
    early = reach(slug, [doc.offset, doc.offset + 5])
    full = reach(slug, [doc.offset + (last - doc.offset) * k // 10 for k in range(11)])
    if early["share"] >= 0.9 or full["share"] < 0.99 or full["tenths"] != 10:
        failures.append(f"reach misjudged: early {early}, full {full}")
    if judge(1.0, [], [], 1.0, forced=True).startswith("a reading"):
        failures.append("a forced final output was judged a reading")
    if not judge(1.0, [], [], 1.0, forced=False).startswith("a reading"):
        failures.append("a complete, cited, far-reaching list was not judged a reading")
    for f in failures:
        print(f"  FAIL  {f}")
    print(f"rlm_ingest: {6 - len(failures)} of 6 offline cases hold "
          "(find_line, refusal, count, reach, forced answer, a reading)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
