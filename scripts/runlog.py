"""Record what a run costs — phases, readers, and what the review corrected.

Until 2026-09-29 no run since document 4 recorded its duration, its tokens or
what the session's review changed in a reader's output, so no step of the
pipeline could be scored (`Plan/concept/pipeline-optimization_2026-09-29.md`,
step 1). This appends one JSON line per event with the clock, so no one types a
timestamp (P26), and refuses an event that would make the log say something
false.

    Plan/runs/<run>/run.jsonl          phases and readers
    Plan/runs/<run>/corrections.jsonl  what the review changed, one row per change

Usage:
    python3 scripts/runlog.py <run> start <phase>
    python3 scripts/runlog.py <run> end <phase>
    python3 scripts/runlog.py <run> reader <name> --model sonnet --tokens 96427 \
        --tool-uses 12 --ms 660945 [--pages aegis,kael] [--agent <id>]
    python3 scripts/runlog.py <run> correct <class> <page> "<before>" "<after>" [--document <slug>]
    python3 scripts/runlog.py <run> summary
    python3 scripts/runlog.py selftest

`--tokens` is what the Agent notification reports: the size of the reader's
last call, not what the run consumed. The twelve transcripts of 2026-09-29 put
the consumption at 12–22 million cache reads per reader against 325–462
thousand reported (`Plan/runs/reader-lab-2026-09-30/`). `--agent` names the
transcript, so `transcripts.json` joins the row; `--document` names whose
reading a correction changed, so the yield can be counted per document.

<run> is a document slug or a batch name; its folder under Plan/runs/ is created.
A phase never logged is „not recorded" in the summary, never 0 (P15, P23).
"""

from __future__ import annotations

import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "Plan" / "runs"

PHASES = ("read", "list", "count", "census", "note", "reconcile", "brief",
          "readers", "review", "record")
CLASSES = ("count", "comparison", "position", "join", "quotation", "straight-quote",
           "link", "shell", "frontmatter", "placement", "other")


class Refused(Exception):
    pass


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def events(folder: Path) -> list[dict]:
    f = folder / "run.jsonl"
    if not f.exists():
        return []
    return [json.loads(line) for line in f.read_text(encoding="utf-8").splitlines() if line.strip()]


def append(folder: Path, name: str, row: dict) -> dict:
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / name).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def phase(folder: Path, what: str, name: str, at: str | None = None) -> dict:
    if name not in PHASES:
        raise Refused(f"no phase {name!r}; phases: {', '.join(PHASES)}")
    # Open is the last event of the phase, not a set difference of names: until
    # 2026-09-30 a phase started a second time — a reader resumed after a stop —
    # counted as closed by its first end, and its second end was refused (R1).
    last: dict[str, str] = {}
    for e in events(folder):
        if e.get("event") in ("start", "end"):
            last[e["phase"]] = e["event"]
    open_ = {p for p, what_ in last.items() if what_ == "start"}
    if what == "start" and name in open_:
        raise Refused(f"phase {name!r} is already started and not ended")
    if what == "end" and name not in open_:
        raise Refused(f"phase {name!r} was never started, so its end would say nothing")
    return append(folder, "run.jsonl", {"event": what, "phase": name, "at": at or now()})


def reader(folder: Path, name: str, model: str | None, tokens: int | None,
           tool_uses: int | None, ms: int | None, pages: list[str], agent: str | None = None) -> dict:
    missing = [k for k, v in (("--model", model), ("--tokens", tokens),
                              ("--tool-uses", tool_uses), ("--ms", ms)) if v is None]
    if missing:
        raise Refused(f"a reader needs its usage as the Agent notification reports it: missing {', '.join(missing)}")
    row = {"event": "reader", "name": name, "model": model, "tokens": tokens,
           "tool_uses": tool_uses, "ms": ms, "pages": pages, "at": now()}
    if agent:
        row["agent"] = agent
    return append(folder, "run.jsonl", row)


def correct(folder: Path, cls: str, page: str, before: str, after: str,
            document: str | None = None) -> dict:
    if cls not in CLASSES:
        raise Refused(f"no correction class {cls!r}; classes: {', '.join(CLASSES)}")
    if not page or before == after:
        raise Refused("a correction names its page and changes something")
    row = {"class": cls, "page": page, "before": before, "after": after, "at": now()}
    if document:
        row["document"] = document
    return append(folder, "corrections.jsonl", row)


def summary(folder: Path) -> dict:
    ev = events(folder)
    out: dict = {"phases": {}, "readers": 0, "tokens": 0, "corrections": {}}
    for p in PHASES:
        starts = [e["at"] for e in ev if e.get("event") == "start" and e["phase"] == p]
        ends = [e["at"] for e in ev if e.get("event") == "end" and e["phase"] == p]
        if not starts or len(ends) < len(starts):
            out["phases"][p] = "not recorded"
            continue
        secs = sum((datetime.fromisoformat(b) - datetime.fromisoformat(a)).total_seconds()
                   for a, b in zip(starts, ends))
        out["phases"][p] = round(secs)
    readers = [e for e in ev if e.get("event") == "reader"]
    out["readers"] = len(readers)
    out["tokens"] = sum(r["tokens"] for r in readers) if readers else "not recorded"
    cf = folder / "corrections.jsonl"
    if cf.exists():
        for line in cf.read_text(encoding="utf-8").splitlines():
            if line.strip():
                c = json.loads(line)["class"]
                out["corrections"][c] = out["corrections"].get(c, 0) + 1
    return out


def selftest() -> int:
    cases = 0
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "run"
        def refuses(fn, *a) -> bool:
            try:
                fn(*a)
            except Refused:
                return True
            return False
        assert refuses(phase, f, "end", "read"), "an end with no start"
        cases += 1
        phase(f, "start", "read", "2026-09-29T10:00:00+00:00")
        assert refuses(phase, f, "start", "read"), "a second start"
        cases += 1
        assert refuses(phase, f, "start", "lunch"), "an unknown phase"
        cases += 1
        phase(f, "end", "read", "2026-09-29T10:30:00+00:00")
        # a phase resumed after a stop can be ended again, and both spans count
        phase(f, "start", "read", "2026-09-30T10:00:00+00:00")
        phase(f, "end", "read", "2026-09-30T10:10:00+00:00")
        assert summary(f)["phases"]["read"] == 2400, summary(f)
        cases += 1
        assert refuses(reader, f, "r1", "sonnet", None, 3, 10, []), "a reader with no usage"
        cases += 1
        reader(f, "r1", "sonnet", 1000, 3, 10, ["aegis"])
        assert refuses(correct, f, "vibes", "aegis", "a", "b"), "a correction with no class"
        cases += 1
        assert refuses(correct, f, "count", "aegis", "x", "x"), "a correction that changes nothing"
        cases += 1
        correct(f, "count", "aegis", "`Flight` 0", "`Flight` 0; `flight` 11")
        s = summary(f)
        assert s["phases"]["read"] == 2400 and s["phases"]["list"] == "not recorded", s
        assert s["tokens"] == 1000 and s["corrections"] == {"count": 1}, s
        cases += 1
        row = reader(f, "r2", "sonnet", 10, 1, 1, [], agent="a0caeac30b491d674")
        fixed = correct(f, "position", "kael", "a", "b", document="doc-x")
        assert row["agent"] == "a0caeac30b491d674" and fixed["document"] == "doc-x", (row, fixed)
        assert "agent" not in reader(f, "r3", "sonnet", 10, 1, 1, []), "an agent where none was given"
        cases += 1
    print(f"runlog: {cases} of {cases} cases hold (end without start, double start, unknown phase, "
          "a phase resumed and ended, reader without usage, unclassed correction, empty correction, "
          "summary, a transcript and a document named)")
    return 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if len(argv) < 2:
        print(__doc__)
        return 2
    folder, verb, rest = RUNS / argv[0], argv[1], argv[2:]

    def opt(name: str):
        if name in rest:
            return rest[rest.index(name) + 1]
        return None
    try:
        if verb in ("start", "end"):
            row = phase(folder, verb, rest[0])
        elif verb == "reader":
            num = lambda k: int(opt(k)) if opt(k) is not None else None  # noqa: E731
            row = reader(folder, rest[0], opt("--model"), num("--tokens"), num("--tool-uses"),
                         num("--ms"), [p for p in (opt("--pages") or "").split(",") if p],
                         opt("--agent"))
        elif verb == "correct":
            row = correct(folder, *rest[:4], document=opt("--document"))
        elif verb == "summary":
            row = summary(folder)
        else:
            print(__doc__)
            return 2
    except Refused as e:
        print(f"refused: {e}")
        return 1
    print(json.dumps(row, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
