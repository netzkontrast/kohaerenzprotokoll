#!/usr/bin/env python3
"""Assemble the smallest sufficient codex packet for one chapter.

    python3 scripts/context_packet.py --chapter 3           # the packet
    python3 scripts/context_packet.py --chapter 3 --paths   # just the files to open
    python3 scripts/context_packet.py --chapter 3 --json
    python3 scripts/context_packet.py --chapter 3 --full    # full bodies everywhere

Every codex body together is ~84,400 tokens — the whole corpus or nothing.
This returns three tiers instead, naming files in the partitioned tree under
`Codex/entries/`. The rules live in `Graph/schema.yaml`:

* **always-on** — the categories that constrain prose without appearing in it
  (rule, guidance, voice, defect, theme, philosophy). Rendered as name plus a
  40-word card; `--full` gives the bodies.
* **chapter-anchored** — entries whose `triggers` occur in that chapter's
  prose. Full bodies, because this is what the chapter is actually about.
* **world axioms** — all of them; they are short and none is chapter-local.

The window is computed on every run rather than stored, so nothing goes stale
and it sharpens as chapters are written. Membership is spoiler-safe by
construction: a chapter is in an entry's window only if a trigger occurs in
that chapter, which means the entry was already in play at or before it.

**What this does not do.** It cannot tell that an entry introduced early
explains a late reveal inside its own body. A real per-entry spoiler ceiling
depends on the story encoding and weaving and on worldbuilding, so it is not
guessed here; `Graph/schema.yaml` records it as planned. Read a body before
using it when the chapter is early and the entry is central.

`--paths` prints one file per line and nothing else, so a caller can open
exactly those and no more.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpcodex, kpgraph  # noqa: E402  (needs ROOT on the path)

CHARS_PER_TOKEN = 4
EXIT_OK, EXIT_CANNOT_RUN = 0, 2


def approx_tokens(chars: int) -> int:
    return chars // CHARS_PER_TOKEN


def packet_paths(data: dict) -> list[str]:
    """Every codex file the packet refers to, in tier order."""
    return [kpcodex.entry_path(e) for e in data["always_on"] + data["anchored"]]


def render(data: dict, full: bool) -> str:
    chapter = data["chapter"]
    lines = [f"# Context packet — chapter {chapter}\n",
             "Assembled by `scripts/context_packet.py` from `Graph/` through the rules in",
             "`Graph/schema.yaml`. The chapter window is computed, never stored.\n"]

    lines.append(f"## Always-on constraints ({len(data['always_on'])})\n")
    lines.append("These hold for every chapter and never appear as vocabulary.\n")
    for entry in data["always_on"]:
        body = entry.get("body", "")
        text = body if full else kpcodex.summary(body)
        lines.append(f"- **{entry.get('name', entry['slug'])}** "
                     f"(`{kpcodex.partition_of(entry)}`) — {text}")
    lines.append("")

    lines.append(f"## In play in chapter {chapter} ({len(data['anchored'])})\n")
    for entry in data["anchored"]:
        lines.append(f"### {entry.get('name', entry['slug'])}  `{entry['slug']}`\n")
        lines.append(kpcodex.first_paragraph(entry.get("body", ""), limit=10_000) if full
                     else kpcodex.summary(entry.get("body", "")))
        lines.append("")

    lines.append(f"## World axioms ({len(data['axioms'])})\n")
    for axiom in data["axioms"]:
        lines.append(f"- **[{axiom.get('severity', '?')}]** {axiom.get('text', '')}")
    return "\n".join(lines) + "\n"


def corpus_tokens(graph) -> int:
    """What loading every codex body would cost — the baseline to beat."""
    return approx_tokens(sum(len(e.get("body", ""))
                             for e in graph.nodes("CodexEntry")))


def cost(data: dict, full: bool) -> dict:
    always = sum(len(e.get("body", "")) if full else len(kpcodex.summary(e.get("body", "")))
                 for e in data["always_on"])
    anchored = sum(len(e.get("body", "")) for e in data["anchored"])
    axioms = sum(len(a.get("text", "")) for a in data["axioms"])
    return {"always_on_tokens": approx_tokens(always),
            "anchored_tokens": approx_tokens(anchored),
            "axiom_tokens": approx_tokens(axioms),
            "total_tokens": approx_tokens(always + anchored + axioms)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--chapter", type=int, required=True, help="chapter number, 0-40")
    parser.add_argument("--paths", action="store_true", help="print only the files to open")
    parser.add_argument("--json", action="store_true", help="print the packet as JSON")
    parser.add_argument("--full", action="store_true", help="full bodies for the always-on tier too")
    args = parser.parse_args(argv)

    if not (ROOT / "Graph").is_dir():
        print(f"no graph at {ROOT / 'Graph'}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    chapters = kpcodex.chapter_texts(ROOT)
    if args.chapter not in chapters:
        print(f"no chapter {args.chapter}; found {min(chapters)}-{max(chapters)}", file=sys.stderr)
        return EXIT_CANNOT_RUN

    graph = kpgraph.load(ROOT)
    data = kpcodex.packet(graph, args.chapter, chapters)
    if args.paths:
        print("\n".join(packet_paths(data)))
        return EXIT_OK
    if args.json:
        print(json.dumps({"chapter": data["chapter"],
                          "cost": {**cost(data, args.full),
                                   "corpus_tokens": corpus_tokens(graph)},
                          "paths": packet_paths(data),
                          "always_on": [e["slug"] for e in data["always_on"]],
                          "anchored": [e["slug"] for e in data["anchored"]]},
                         ensure_ascii=False, indent=2))
        return EXIT_OK
    print(render(data, args.full))
    spend = cost(data, args.full)
    print(f"<!-- ~{spend['total_tokens']} tokens "
          f"(always-on {spend['always_on_tokens']}, chapter {spend['anchored_tokens']}, "
          f"axioms {spend['axiom_tokens']}) against ~{corpus_tokens(graph):,} "
          "for every codex body -->")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
