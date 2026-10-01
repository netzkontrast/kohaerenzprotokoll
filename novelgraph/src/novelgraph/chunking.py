"""Line-exact chunking. Splits within a source line require a future schema."""
import hashlib
import re
from .repo import split_body

HEAD = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chunk_id(slug, method, first, last, content_sha):
    return hashlib.sha1(f"{slug}|{method}|{first}|{last}|{content_sha}".encode()).hexdigest()[:12]


def headings(text):
    body, offset = split_body(text)
    tree, stack, paths, fence = [], [], {}, None
    for n, line in enumerate(body.split("\n"), offset):
        mark = re.match(r"^\s*(`{3,}|~{3,})", line)
        h = HEAD.match(line) if fence is None else None
        if h:
            level, title = len(h[1]), h[2]
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            tree.append(dict(line=n, level=level, title=title, path=[v for _, v in stack]))
        paths[n] = [v for _, v in stack]
        if mark:
            marker = mark[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and line.strip() == marker:
                fence = None
    return tree, paths, offset


def slice_text(lines, first, last):
    return "\n".join(lines[first - 1:last])


def make_chunks(slug, title, text, method, config, count):
    lines = text.split("\n")
    tree, paths, offset = headings(text)
    spans = []
    if not any(s.strip() for s in lines[offset - 1:]):
        return [], tree
    if method == "section@v1":
        level = min((h["level"] for h in tree), default=1)
        starts = sorted(set([offset] + [h["line"] for h in tree if h["level"] == level]))
        spans = [(a, b - 1) for a, b in zip(starts, starts[1:] + [len(lines) + 1])]
    else:
        # Atomic units are complete source lines, paragraphs, tables and code.
        units, pending, fence, table = [], [], None, False

        def flush():
            nonlocal pending
            if pending:
                units.append((pending[0], pending[-1]))
                pending = []

        for n in range(offset, len(lines) + 1):
            line = lines[n - 1]
            mark = re.match(r"^\s*(`{3,}|~{3,})", line)
            is_table = line.lstrip().startswith("|") and "|" in line.lstrip()[1:]
            if fence is None:
                if HEAD.match(line):
                    flush()
                    units.append((n, n))
                    continue
                if not line.strip():
                    flush()
                    table = False
                    continue
                if bool(pending) and is_table != table:
                    flush()
            pending.append(n)
            if mark:
                marker = mark[1]
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence) and line.strip() == marker:
                    fence = None
            table = is_table
        flush()
        # Oversized prose paragraphs split at line boundaries; tables/fences do not.
        small = []
        maximum = config.get("max", config.get("target", 400))
        for a, b in units:
            raw = slice_text(lines, a, b)
            if count(raw) > maximum and not lines[a - 1].lstrip().startswith(("|", "```", "~~~")):
                first, size = a, 0
                for n in range(a, b + 1):
                    length = count(lines[n - 1])
                    if size and size + length > maximum:
                        small.append((first, n - 1))
                        first, size = n, 0
                    size += length
                small.append((first, b))
            else:
                small.append((a, b))
        target = config.get("target", 400)
        first, last, size = None, None, 0
        for a, b in small:
            length = count(slice_text(lines, a, b))
            boundary = method == "heading@v1" and first is not None and paths.get(a) != paths.get(first)
            if first is not None and (boundary or size + length > maximum or size >= target):
                spans.append((first, last))
                first, size = None, 0
            if first is None:
                first = a
            last, size = b, size + length
        if first is not None:
            spans.append((first, last))
        if method == "window400@v1":
            # Line-aligned overlap, at least the trailing line nearest the budget.
            overlapped = []
            for i, (a, b) in enumerate(spans):
                if i:
                    prev_a, prev_b = spans[i - 1]
                    budget, used, start = target * config.get("overlap", 0.15), 0, a
                    for n in range(prev_b, prev_a - 1, -1):
                        length = count(lines[n - 1])
                        if used + length > budget:
                            break
                        start, used = n, used + length
                    # Never start inside a table or fence block.
                    if any(u <= start <= v and lines[u - 1].lstrip().startswith(("|", "```", "~~~"))
                           for u, v in units):
                        start = a
                    a = start
                overlapped.append((a, b))
            spans = overlapped
    out = []
    for a, b in spans:
        while a <= b and not lines[a - 1].strip():
            a += 1
        while b >= a and not lines[b - 1].strip():
            b -= 1
        if a > b:
            continue
        raw = slice_text(lines, a, b)
        content_sha = sha(raw)
        path = paths.get(a, [])
        out.append(dict(id=chunk_id(slug, method, a, b, content_sha), line_start=a,
                        line_end=b, heading_path=path, sha=content_sha,
                        tokens=count(raw), prefix=" › ".join([title] + path)))
    return out, tree
