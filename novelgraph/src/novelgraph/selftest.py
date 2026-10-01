"""Each case hands the chunkers the defect it must not have. No corpus, no model."""

from __future__ import annotations

from . import chunkers, store


def _doc() -> list[str]:
    lines = ["---", "title: x", "---", "# Teil A", ""]
    lines += [" ".join(["wort"] * 60) for _ in range(3)] + [""]          # 180 tokens of prose
    lines += ["## Kurz", "", "nur zwei", ""]                                # a section under min
    lines += ["| a | b |", "|---|---|"] + [f"| {'z ' * 40}| y |" for _ in range(14)] + [""]  # a 600+ token table
    lines += ["# Teil B", "", " ".join(["lang"] * 900)]                     # one line over max
    return lines


def selftest() -> list[str]:
    fails = []
    lines = _doc()
    p = store.chunkers()
    head = chunkers.chunk("t", "Titel", lines, 4, "heading@v1", p["heading@v1"])
    for r in head:
        if r["line_start"] < 4 or r["line_end"] > len(lines):
            fails.append(f"heading@v1 chunk {r} leaves the body")
        if chunkers.chunk_id("t", "heading@v1", r["line_start"], r["line_end"], r["sha"]) != r["id"]:
            fails.append("chunk id does not recompute")
    table = [i + 1 for i, l in enumerate(lines) if l.startswith("|")]
    holders = [r for r in head if r["line_start"] <= table[0] <= r["line_end"]]
    if not holders or holders[0]["line_end"] < table[-1]:
        fails.append(f"heading@v1 split a table: {holders}")
    long_line = len(lines)
    if not any(r["tokens"] > p["heading@v1"]["max"] and r["line_end"] == long_line
               and r["line_start"] >= lines.index("# Teil B") + 1 for r in head):
        fails.append("a line over max did not stay one chunk")
    kurz = lines.index("## Kurz") + 1
    if any(r["line_start"] == kurz for r in head):
        fails.append("a section under min stood alone instead of joining its neighbour")
    if not any(r["prefix"] == "Titel › Teil A" for r in head):
        fails.append(f"prefix is not 'Titel › H1': {[r['prefix'] for r in head]}")
    if any(r["line_start"] <= lines.index("# Teil B") + 1 <= r["line_end"] and r["line_start"] < lines.index("# Teil B")
           for r in head if r["tokens"] >= p["heading@v1"]["min"] and r["line_end"] > lines.index("# Teil B") + 1):
        fails.append("heading@v1 crossed a heading although the chunk had reached min")
    # one paragraph of lines 300 + 400 tokens: below target_min after the first, but together over max
    para = ["# P", " ".join(["a"] * 300), " ".join(["b"] * 400)]
    cut = chunkers.chunk("p", "P", para, 1, "heading@v1", p["heading@v1"])
    if any(r["tokens"] > p["heading@v1"]["max"] and r["line_start"] != r["line_end"]
           and not (r["line_end"] - r["line_start"] == 1 and para[r["line_start"] - 1].startswith("#")) for r in cut):
        fails.append(f"heading@v1 joined lines past max: {[(r['line_start'], r['line_end'], r['tokens']) for r in cut]}")
    sec = chunkers.chunk("t", "Titel", lines, 4, "section@v1", p["section@v1"])
    if [r["heading_path"] for r in sec] != [["Teil A"], ["Teil B"]]:
        fails.append(f"section@v1 expected two top-level sections, got {[r['heading_path'] for r in sec]}")
    flat = ["ein satz ohne überschrift"] * 5
    if len(chunkers.chunk("f", "F", flat, 1, "section@v1", p["section@v1"])) != 1:
        fails.append("section@v1 without headings is not the whole document")
    prose = [" ".join(["w"] * 50) for _ in range(30)]
    win = chunkers.chunk("w", "W", prose, 1, "window400@v1", p["window400@v1"])
    if len(win) < 2 or not all(a["line_end"] >= b["line_start"] for a, b in zip(win, win[1:])):
        fails.append(f"window400@v1 windows do not overlap: {[(r['line_start'], r['line_end']) for r in win]}")
    if chunkers.chunk("w", "W", prose, 1, "window400@v1", p["window400@v1"]) != win:
        fails.append("a chunker is not deterministic")
    return fails
