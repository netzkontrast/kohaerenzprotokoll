#!/usr/bin/env python3
"""Where a document-reader's tokens went, read from its subagent transcript.

    python3 transcripts.py [SUBAGENTS_DIR]            # print the table and the detail
    python3 transcripts.py [SUBAGENTS_DIR] --write    # and merge the numbers into transcripts.json

A transcript is Claude Code's own record of a subagent: one JSON row per
message, the API usage on every assistant row. It lives outside the
repository (~/.claude/projects/<project>/<session>/subagents/) and dies with
the container, so this script's printed output is what is kept.

Per reader: API calls, tokens by kind, the largest context, tool uses, what
was read and how often, what each phase cost (a call is charged to the phase
`runlog.py start` last opened), and how the run ended.

`cost` is a proxy, labelled as one: input + 1.25 x cache writes + 0.1 x cache
reads + 5 x output — the ratio of Sonnet's list prices. How the plan's usage
limit weighs the four kinds is not published; the proxy only ranks runs.

**Output tokens are not in the transcript.** Each assistant row carries the
usage of the stream's first event, where output is a handful of tokens; the
final count never reaches the file. So `out` is what the rows say (a floor,
not a count), and `wrote` is measured instead: the characters of every tool
call's input and every text block. Thinking is stored redacted and is in
neither.

**The context grows by more than the transcript shows.** Between two calls it
grows by what the first call wrote and the tool results it got back, and by
the thinking of that call, which is stored redacted. So `unseen` estimates the
thinking: the context's growth minus the visible characters divided by a
characters-per-token ratio calibrated on the same transcript (the median over
calls whose growth is mostly one large tool result, so thinking is small beside
it). It is an estimate and labelled so; a thinking-free run would show it near 0.

`transcripts.json` keeps numbers only — no prompt, no document text — keyed by
the agent id, so a run's `runlog.py reader --agent <id>` row joins it.
Standard library only.
"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

SCRIPTS = re.compile(r"scripts/([a-z_]+\.py)")
RUNLOG = re.compile(r"runlog\.py\s+\S+\s+(start|end)\s+(\w+)")


def default_dir():
    pats = glob.glob(os.path.expanduser(
        "~/.claude/projects/-home-user-kohaerenzprotokoll/*/subagents"))
    return max(pats, key=os.path.getmtime) if pats else "."


def first_prompt(rows):
    for r in rows:
        if r.get("type") == "user":
            c = r["message"]["content"]
            if isinstance(c, list):
                c = " ".join(x.get("text", "") for x in c if isinstance(x, dict))
            return c
    return ""


def cost(u):
    return (u["input"] + 1.25 * u["cache_write"] + 0.1 * u["cache_read"]
            + 5 * u["output"])


def description(path):
    try:
        return json.load(open(path.replace(".jsonl", ".meta.json"))).get("description", "")
    except (OSError, ValueError):
        return ""


def agent_type(path):
    meta = path.replace(".jsonl", ".meta.json")
    try:
        return json.load(open(meta)).get("agentType", "?")
    except (OSError, ValueError):
        return "?"


def analyse(path):
    rows = [json.loads(l) for l in open(path)]
    prompt = first_prompt(rows)
    m = re.search(r"slug `([a-z0-9\-]+)`", prompt)
    slug = m.group(1) if m else os.path.basename(path)
    wrote = 0
    usage = {}          # message id -> usage (last row wins)
    order = []          # message ids in order, with the phase open at the time
    phase = "setup"
    steps = []          # per API call: [context at its start, visible chars that followed it]
    tools = Counter()
    scripts = Counter()
    reads = Counter()
    result_chars = Counter()
    errors = 0
    tool_names = {}     # tool_use id -> name
    last_text = ""
    ts = [r["timestamp"] for r in rows if "timestamp" in r]
    for r in rows:
        if r.get("type") == "assistant":
            msg = r["message"]
            mid = msg.get("id")
            if mid not in usage:
                order.append((mid, phase))
                u0 = msg.get("usage", {}) or {}
                steps.append([u0.get("input_tokens", 0) + u0.get("cache_creation_input_tokens", 0)
                              + u0.get("cache_read_input_tokens", 0), 0, 0])
            usage[mid] = msg.get("usage", {})
            for c in msg.get("content", []):
                if c.get("type") == "tool_use":
                    n = len(json.dumps(c.get("input", {}), ensure_ascii=False))
                    wrote += n
                    steps[-1][1] += n
                    name = c["name"]
                    tools[name] += 1
                    tool_names[c["id"]] = name
                    inp = c.get("input", {})
                    if name == "Bash":
                        cmd = inp.get("command", "")
                        for s in SCRIPTS.findall(cmd):
                            scripts[s] += 1
                        for ev, ph in RUNLOG.findall(cmd):
                            phase = ph if ev == "start" else f"after-{ph}"
                    elif name == "Read":
                        reads[inp.get("file_path", "?").replace(
                            "/home/user/kohaerenzprotokoll/", "")] += 1
                elif c.get("type") == "text":
                    last_text = c.get("text", "")
                    wrote += len(last_text)
                    if steps:
                        steps[-1][1] += len(last_text)
        elif r.get("type") == "user":
            c = r["message"]["content"]
            if isinstance(c, list):
                for x in c:
                    if isinstance(x, dict) and x.get("type") == "tool_result":
                        body = x.get("content")
                        if isinstance(body, list):
                            body = " ".join(y.get("text", "") for y in body
                                            if isinstance(y, dict))
                        result_chars[tool_names.get(x.get("tool_use_id"), "?")] += len(body or "")
                        errors += bool(x.get("is_error"))
                        if steps:
                            steps[-1][1] += len(body or "")
                            steps[-1][2] += len(body or "")
    tot = Counter()
    per_phase = defaultdict(Counter)
    peak = 0
    for mid, ph in order:
        u = usage[mid] or {}
        k = {"input": u.get("input_tokens", 0),
             "cache_write": u.get("cache_creation_input_tokens", 0),
             "cache_read": u.get("cache_read_input_tokens", 0),
             "output": u.get("output_tokens", 0)}
        tot.update(k)
        per_phase[ph].update(k)
        per_phase[ph]["calls"] += 1
        peak = max(peak, k["input"] + k["cache_write"] + k["cache_read"])
    # chars per token, calibrated where one large tool result dominates a step's growth
    ratios = sorted((a[1] / (b[0] - a[0])) for a, b in zip(steps, steps[1:])
                    if a[2] >= 5000 and b[0] > a[0])
    ratio = ratios[len(ratios) // 2] if ratios else 3.0
    growth = sum(max(b[0] - a[0], 0) for a, b in zip(steps, steps[1:]))
    visible = sum(a[1] for a in steps[:-1])
    unseen = max(growth - visible / ratio, 0)
    return {"slug": slug, "agent": os.path.basename(path)[len("agent-"):-len(".jsonl")],
            "chars_per_token": round(ratio, 2), "context_growth": growth,
            "unseen_tokens": round(unseen), "unseen_share": round(unseen / growth, 2) if growth else None,
            "agent_type": agent_type(path), "wrote_chars": wrote,
            "path": os.path.basename(path), "start": min(ts),
            "end": max(ts), "calls": len(order), "tokens": dict(tot),
            "cost": cost(tot), "peak_context": peak, "tools": dict(tools),
            "scripts": dict(scripts), "reads": dict(reads),
            "result_chars": dict(result_chars), "errors": errors,
            "phases": {p: dict(v) | {"cost": cost(v)} for p, v in per_phase.items()},
            "ended": last_text.strip().replace("\n", " ")[:160]}


def seconds(a, b):
    from datetime import datetime
    f = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (f(b) - f(a)).total_seconds()


def main(argv):
    d = next((a for a in argv if not a.startswith("--")), None) or default_dir()
    runs = []
    for p in sorted(glob.glob(os.path.join(d, "agent-*.jsonl"))):
        rows = [json.loads(l) for l in open(p)]
        role = agent_type(p)
        if role not in ("document-reader", "wiki-reader"):
            head = first_prompt(rows)[:300]
            role = next((r for r in ("document-reader", "wiki-reader") if r in head), None)
        if not role:
            continue
        run = dict(analyse(p), role=role, description=description(p))
        if run["slug"].startswith("agent-"):
            run["slug"] = run["description"] or run["slug"]
        runs.append(run)
    runs.sort(key=lambda r: r["start"])
    print(f"{len(runs)} reader transcripts in {d}\n")
    print(f"{'document':46} {'min':>5} {'calls':>5} {'peak ctx':>8} {'wrote':>7} "
          f"{'unseen':>7} {'cache rd':>10} {'cost':>9}  ended")
    for r in runs:
        t = r["tokens"]
        print(f"{r['slug'][:46]:46} {seconds(r['start'], r['end'])/60:5.1f} "
              f"{r['calls']:5d} {r['peak_context']:8d} {r['wrote_chars']:7d} "
              f"{r['unseen_share'] or 0:7.0%} {t['cache_read']:10d} {r['cost']:9.0f}  {r['ended'][:40]}")
    print()
    for r in runs:
        print(f"== {r['slug']}  ({r['path']})")
        print("   tools:  ", ", ".join(f"{k} {v}" for k, v in sorted(r["tools"].items(), key=lambda x: -x[1])))
        print("   scripts:", ", ".join(f"{k} {v}" for k, v in sorted(r["scripts"].items(), key=lambda x: -x[1])))
        print("   result chars by tool:", ", ".join(f"{k} {v}" for k, v in sorted(r["result_chars"].items(), key=lambda x: -x[1])))
        print("   reads:  ", ", ".join(f"{k} x{v}" for k, v in sorted(r["reads"].items(), key=lambda x: -x[1])))
        print("   by phase (calls / output / cost):")
        for p, v in r["phases"].items():
            print(f"      {p:16} {v['calls']:4d} {v['output']:7d} {v['cost']:9.0f}")
        print(f"   tool errors: {r['errors']}")
        print()
    if "--write" in argv:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transcripts.json")
        kept = {}
        if os.path.exists(out):
            kept = {r["agent"]: r for r in json.load(open(out, encoding="utf-8"))}
        for r in runs:
            r = dict(r, minutes=round(seconds(r["start"], r["end"]) / 60, 1))
            r.pop("path", None)
            kept[r["agent"]] = r
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(sorted(kept.values(), key=lambda r: r["start"]), fh, indent=1, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {out}: {len(kept)} transcripts")


if __name__ == "__main__":
    main(sys.argv[1:])
