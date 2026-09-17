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

## What this may not do, and does not

**It writes `03-candidates-rlm.md`, never `03-candidates.md`.** The gold list is
written by a reader while reading; a model's list is the thing gold is used to
score, and the two must never be able to become each other. `written_by:` records
which is which and `state.py` reads that line.

It proposes and stops. No page, no judgement, no conflict, no census is written
from here — those are decisions, and an ingest proposes rather than resolves.

Usage:
    python3 scripts/rlm_ingest.py <slug> [--model M] [--iters N]
    python3 scripts/rlm_ingest.py <slug> --score        # against the human list
"""

from __future__ import annotations

import argparse
import os
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
DEFAULT_MODEL = "openrouter/nex-agi/nex-n2.5-pro:free"
BASE = "https://openrouter.ai/api/v1"


def api_key() -> str:
    """From the git-ignored .env, and never printed or written anywhere."""
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no OPENROUTER_API_KEY in .env")


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

Answer with the list and nothing else, one candidate per line, each line starting
with `- `. No commentary, no numbering, no counts."""


def run(slug: str, model: str, iters: int) -> Path:
    import dspy
    skills, instructions = briefing()
    lm = dspy.LM(model, api_key=api_key(), api_base=BASE, max_tokens=16000, temperature=0)
    dspy.configure(lm=lm)
    rlm = dspy.RLM("document: str, task: str -> candidates: str", max_iters=iters)

    started = time.time()
    result = rlm(document=numbered(slug),
                 task=TASK.format(skills=skills, instructions=instructions))
    elapsed = time.time() - started

    lines = [l.rstrip() for l in str(result.candidates).splitlines() if l.strip().startswith("- ")]
    out = RUNS / slug / "03-candidates-rlm.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"written_by: dspy.RLM, model {model}, {iters} iterations, {elapsed:.0f}s\n"
        f"ran: {date.today().isoformat()}\n\n"
        f"# Candidates (model) — {slug}\n\n"
        "> **Not a gold list.** A gold candidate list is written by a reader while\n"
        "> reading, before any count. This is the thing gold is used to score.\n\n"
        + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(lines)} candidates in {elapsed:.0f}s -> {out.relative_to(ROOT)}")
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
    parser.add_argument("slug")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--iters", type=int, default=12)
    parser.add_argument("--score", action="store_true")
    args = parser.parse_args(argv)
    if args.score:
        return score(args.slug)
    run(args.slug, args.model, args.iters)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
