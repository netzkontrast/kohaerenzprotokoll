"""Promotion: the author's review of a term page, pinned so it cannot change unnoticed.

A term page in `Wiki/candidates/` collects every read source's reading of one term,
attributed and unmerged. **Promoting it records that the author reviewed that
account** — the readings faithful to their lines, the differences listed, the lead
sentence fair — as of the documents it then held. It decides nothing about which
reading is right: that stays in `Manuscript/kanon.md`, a conflict record's
resolution or a Weiche. `Plan/concept/promotion_2026-10-08.md` has the reasons
and the alternatives; decision 026 records the first one.

    status: reviewed          # provisional — the first promotion, 2026-10-08
                              # may not: decide a reading, enter canon, rank retrieval
                              # retire when: the author says what promotion is for and
                              #              this field does not carry it

**Where it lives.** The page stays where it is — 23 scripts, the app's addresses
and the graph read `Wiki/candidates/` — and carries `status: reviewed` and
`reviewed: <date>`. Every promotion and withdrawal is a row in
`Plan/runs/promotions.jsonl`, append-only: the page, the date, who, **the author's
words verbatim**, the sha256 of the reviewed part, the documents it covered and
the coverage measured then.

**What is pinned.** The body from the end of the frontmatter to the heading
`## Since review` (or the end). The frontmatter is not pinned: `ingested`,
`sources`, `readings` are derived and `conflict` names records that come later.

**A source read after the review** never changes the reviewed part.
`readings.py` puts its reading — and its line for the differences — under
`## Since review` at the end of the page, so the pipeline keeps flowing and the
page shows what the author has not seen. A contradiction gets its conflict record
as always (decision 003). `apply` again folds those readings into date order and
pins the new state; that is a re-review, and it needs the author's words again.

Usage:
    python3 scripts/promote.py sheet <page>      # the review sheet: what is measured, what a person judges
    python3 scripts/promote.py ready             # every term page against the mechanical checks
    python3 scripts/promote.py apply <page> --words "<the author's words>" [--by author]
    python3 scripts/promote.py withdraw <page> --words "<the author's words>"
    python3 scripts/promote.py check             # fail if a reviewed part changed or status and ledger disagree
    python3 scripts/promote.py selftest
"""

from __future__ import annotations

import datetime
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "Wiki" / "candidates"
LEDGER = ROOT / "Plan" / "runs" / "promotions.jsonl"
SINCE = "## Since review"
DIFFERS = "*Where it differs:*"
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
READING = re.compile(r"^## Reading — `([^`]+)`", re.M)
SHORTEST_SURFACE = 4

sys.path.insert(0, str(ROOT / "scripts"))


# --- the page --------------------------------------------------------------

def split(text: str) -> tuple[str, str]:
    """(frontmatter with its fences, body)."""
    m = FRONT.match(text)
    return (m.group(0), text[m.end():]) if m else ("", text)


def status(text: str) -> str:
    from wiki_index import frontmatter
    return frontmatter(text).get("status", "")


def is_reviewed(text: str) -> bool:
    return status(text) == "reviewed"


def since_at(body: str) -> int:
    """Where `## Since review` starts in the body, or len(body)."""
    m = re.search(r"^" + re.escape(SINCE) + r"\b", body, re.M)
    return m.start() if m else len(body)


def reviewed_part(text: str) -> str:
    body = split(text)[1]
    return body[:since_at(body)].rstrip()


def frozen_end(text: str) -> int:
    """Characters of `text` no tool may rewrite: frontmatter and reviewed part of a reviewed page, else 0."""
    if not is_reviewed(text):
        return 0
    front, body = split(text)
    return len(front) + since_at(body)


def digest(text: str) -> str:
    return hashlib.sha256(reviewed_part(text).encode("utf-8")).hexdigest()


def since_readings(text: str) -> list[str]:
    body = split(text)[1]
    return READING.findall(body[since_at(body):])


def append_since(page: str, section: str, differ: list[str]) -> str:
    """A reading for a reviewed page: appended under `## Since review`, nothing above it touched."""
    block = section.rstrip("\n")
    if differ:
        block += "\n\n" + DIFFERS + "\n\n" + "\n".join(differ)
    if SINCE not in page:
        on = _field(page, "reviewed") or "?"
        head = f"{SINCE} — read after the author's review of {on}, not yet reviewed"
        return page.rstrip("\n") + "\n\n" + head + "\n\n" + block + "\n"
    return page.rstrip("\n") + "\n\n" + block + "\n"


def fold_since(page: str) -> str:
    """The re-review: every reading under `## Since review` into date order, its differ lines into place."""
    from readings import add_differ, insert, DATE_IN_HEAD
    front, body = split(page)
    at = since_at(body)
    rest = body[at:]
    page = front + body[:at].rstrip("\n") + "\n"
    blocks = re.split(r"(?m)^(?=## Reading — )", rest)[1:]
    for block in blocks:
        section, _, tail = block.partition(DIFFERS)
        differ = [line for line in tail.strip().splitlines() if line.strip()]
        date = DATE_IN_HEAD.match(section)
        page = add_differ(insert(page, section.strip() + "\n", date.group(1) if date else "9999", False), differ)
    return page


def _field(text: str, key: str) -> str:
    from wiki_index import frontmatter
    return frontmatter(text).get(key, "")


def set_fields(text: str, fields: dict[str, str | None]) -> str:
    """Set (or with None remove) scalar frontmatter fields, after `status:`."""
    front, body = split(text)
    lines = front.rstrip("\n").split("\n")[1:-1]
    for key, value in fields.items():
        idx = next((i for i, line in enumerate(lines) if line.startswith(key + ":")), None)
        if value is None:
            if idx is not None:
                del lines[idx]
            continue
        line = f"{key}: {value}"
        if idx is not None:
            lines[idx] = line
        else:
            after = next((i for i, l in enumerate(lines) if l.startswith("status:")), len(lines) - 1)
            lines.insert(after + 1, line)
    return "---\n" + "\n".join(lines) + "\n---\n" + body


# --- the ledger ------------------------------------------------------------

def ledger(path: Path | None = None) -> list[dict]:
    path = path or LEDGER
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def latest(rows: list[dict]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for row in rows:
        out[row["page"]] = row
    return out


def check(pages: Path | None = None, ledger_path: Path | None = None) -> list[str]:
    """Every disagreement between pages and ledger, as a sentence each."""
    pages = pages or PAGES
    # Rows with a `layer` other than candidates are another page type's (terms.py's approvals).
    last = latest([r for r in ledger(ledger_path) if r.get("layer", "candidates") == "candidates"])
    problems = []
    for path in sorted(pages.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        row = last.get(path.stem)
        live = row is not None and row.get("action") == "promote"
        if is_reviewed(text) and not live:
            problems.append(f"{path.stem}: status reviewed, but no promotion in the ledger stands for it")
        elif live and not is_reviewed(text):
            problems.append(f"{path.stem}: promoted {row['on']} in the ledger, but the page says status {status(text)!r}")
        elif live and digest(text) != row["sha256"]:
            problems.append(f"{path.stem}: the reviewed part changed since the author's review of {row['on']} — "
                            f"revert it, or the author re-reviews (`promote.py apply {path.stem} --words …`)")
    for page in last:
        if not (pages / f"{page}.md").exists():
            problems.append(f"{page}: in the ledger, but no page Wiki/candidates/{page}.md")
    return problems


# --- the sheet -------------------------------------------------------------

def fold(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)).lower()


_RECONCILED: set[str] = set()


def reconciled(slug: str) -> bool:
    """A run directory holding a reconcile.json — what `state.py`'s `documents.reconciled` counts.

    The record's name is no test: the first document's reconciliation is one of the three full
    re-comparisons in `Wiki/compare/`, not a `reconcile-NN-<slug>.md`.
    """
    if not _RECONCILED:
        _RECONCILED.update(p.parent.name for p in (ROOT / "Plan" / "runs").glob("*/reconcile.json"))
    return slug in _RECONCILED


_TEXTS: dict[str, str] = {}


def corpus() -> dict[str, str]:
    if not _TEXTS:
        for p in sorted((ROOT / "Sources" / "drive").glob("*.md")):
            _TEXTS[p.stem] = fold(p.read_text(encoding="utf-8", errors="ignore"))
    return _TEXTS


def surfaces(slug: str) -> list[str]:
    index = json.loads((ROOT / "Wiki" / "index.json").read_text(encoding="utf-8"))
    entry = index["terms"].get(slug, {})
    return sorted({s for s in entry.get("surfaces", []) if len(s) >= SHORTEST_SURFACE})


def coverage(slug: str, ingested: list[str]) -> dict:
    """Landed documents that write one of the page's surfaces, read or not — the macron, case and accents folded."""
    folded = sorted({fold(s) for s in surfaces(slug)}, key=len, reverse=True)
    if not folded:
        return {"naming": 0, "on_page": 0, "read_not_on_page": [], "unread": {}}
    pat = re.compile(r"(?<!\w)(?:" + "|".join(map(re.escape, folded)) + r")(?!\w)")
    naming = {}
    for doc, text in corpus().items():
        n = len(pat.findall(text))
        if n:
            naming[doc] = n
    unread = {d: n for d, n in naming.items() if not reconciled(d)}
    read_absent = [d for d in naming if d not in unread and d not in ingested]
    return {"naming": len(naming), "on_page": sum(1 for d in naming if d in ingested),
            "read_not_on_page": sorted(read_absent),
            "unread": dict(sorted(unread.items(), key=lambda kv: (-kv[1], kv[0])))}


def conflicts_of(slug: str) -> list[tuple[str, str]]:
    from wiki_index import frontmatter
    out = []
    for p in sorted((ROOT / "Wiki" / "conflicts").glob("*.md")):
        meta = frontmatter(p.read_text(encoding="utf-8"))
        if slug in meta.get("pages", []):
            out.append((meta.get("id", p.stem), meta.get("status", "")))
    return out


def mechanical(slug: str) -> list[tuple[str, bool, str, bool]]:
    """(check, passed, what it found, blocks a promotion)."""
    import quotes
    from wiki_index import derive_frontmatter, frontmatter, read_documents
    path = PAGES / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    rows = []
    q = quotes.tally([path])
    rows.append(("quotations resolve", q["unresolved"] == 0 and q["unchecked"] == 0,
                 f"{q['checked']} checked, {q['unresolved']} unresolved, {q['unchecked']} unchecked", True))
    ingested = meta.get("ingested", [])
    missing = [s for s in ingested if not (reconciled(s) and (ROOT / "Sources" / "notes" / f"{s}.md").exists()
                                           and (ROOT / "Sources" / "terms" / f"{s}.md").exists())]
    rows.append(("every source read through", not missing,
                 f"{len(ingested) - len(missing)} of {len(ingested)} with census, note and reconciliation"
                 + (": missing " + ", ".join(missing) if missing else ""), True))
    want = derive_frontmatter(text, read_documents())
    drift = [k for k in ("ingested", "sources", "readings") if not want["keep_readings"] or k != "readings"
             if (meta.get(k, []) if k == "ingested" else int(meta.get(k, 0) or 0)) != want[k]]
    rows.append(("frontmatter as derived", not drift, "agrees" if not drift else "drifts: " + ", ".join(drift), True))
    known = {p.stem for d in ("candidates", "chapters") for p in (ROOT / "Wiki" / d).glob("*.md")}
    broken = sorted({t.strip() for t in LINK.findall(text)} - known)
    rows.append(("links resolve", not broken, "all resolve" if not broken else "to no page: " + ", ".join(broken), True))
    since = since_readings(text)
    rows.append(("nothing waiting under Since review", not since,
                 "none" if not since else f"{len(since)}: " + ", ".join(since) + " (apply folds them in)", False))
    cs = conflicts_of(slug)
    open_ = [c for c, s in cs if s == "open"]
    rows.append(("open conflicts on the page", not open_,
                 (", ".join(f"{c} ({s})" for c, s in cs) or "none") + " — an open one is shown, not settled, by a review", False))
    cov = coverage(slug, ingested)
    unread = cov["unread"]
    rows.append(("coverage of the corpus", not unread and not cov["read_not_on_page"],
                 f"{cov['naming']} landed documents name it, {cov['on_page']} have a reading here, "
                 f"{len(cov['read_not_on_page'])} read without one (the sweep decided them), {len(unread)} unread"
                 + ("; unread: " + ", ".join(f"{d} ({n})" for d, n in list(unread.items())[:12]) if unread else ""),
                 False))
    return rows


JUDGEMENT = [
    "The lead paragraph — the one place the page speaks in its own voice — says only what the readings carry.",
    "Each reading's prose around its quotations says what the line says, with its stance (premise, verdict, finding, restatement).",
    "`## Where the sources differ` names every difference the readings show, and none they do not.",
    "Whether a difference listed there should be a conflict record (decision 003) — the author's call.",
    "Whether the unread documents that name the term should be read first.",
]


def sheet(slug: str) -> str:
    path = PAGES / f"{slug}.md"
    if not path.exists():
        raise SystemExit(f"no page Wiki/candidates/{slug}.md")
    text = path.read_text(encoding="utf-8")
    rows = mechanical(slug)
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    out = [f"# Review sheet — `{slug}`", "",
           f"Measured {datetime.date.today().isoformat()} at {head or 'an uncommitted tree'} by `python3 scripts/promote.py sheet {slug}`. "
           f"Status `{status(text)}`; the reviewed part would be {len(reviewed_part(text))} characters, sha256 `{digest(text)[:16]}…`.",
           "", "## Measured", "", "| check | | what it found |", "|---|---|---|"]
    for name, ok, found, blocks in rows:
        mark = "ok" if ok else ("**refuses**" if blocks else "noted")
        out.append(f"| {name} | {mark} | {found} |")
    out += ["", "## For a person — the author decides", ""] + [f"- [ ] {j}" for j in JUDGEMENT]
    blocking = [n for n, ok, _, b in rows if b and not ok]
    out += ["", "**`apply` refuses: " + ", ".join(blocking) + ".**" if blocking else
            "Nothing measured refuses a promotion; the rest is the author's."]
    return "\n".join(out) + "\n"


# --- the verbs -------------------------------------------------------------

def apply(slug: str, words: str, by: str, today: str | None = None) -> dict:
    if not words.strip():
        raise SystemExit("a promotion records the author's words verbatim: --words is required (P0)")
    path = PAGES / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    if since_readings(text):
        text = fold_since(text)
        path.write_text(text, encoding="utf-8")
    rows = mechanical(slug)
    blocking = [f"{n}: {f}" for n, ok, f, b in rows if b and not ok]
    if blocking:
        raise SystemExit("refused — " + "; ".join(blocking))
    today = today or datetime.date.today().isoformat()
    text = set_fields(path.read_text(encoding="utf-8"), {"status": "reviewed", "reviewed": today})
    path.write_text(text, encoding="utf-8")
    from wiki_index import frontmatter
    cov = coverage(slug, frontmatter(text).get("ingested", []))
    row = {"page": slug, "action": "promote", "on": today, "by": by, "words": words,
           "sha256": digest(text), "ingested": frontmatter(text).get("ingested", []),
           "coverage": {"naming": cov["naming"], "on_page": cov["on_page"], "unread": list(cov["unread"])}}
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def withdraw(slug: str, words: str, by: str) -> dict:
    if not words.strip():
        raise SystemExit("a withdrawal records the author's words verbatim: --words is required (P0)")
    path = PAGES / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(set_fields(text, {"status": "candidate", "reviewed": None}), encoding="utf-8")
    row = {"page": slug, "action": "withdraw", "on": datetime.date.today().isoformat(), "by": by, "words": words}
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def ready() -> str:
    out = ["| page | status | refuses | noted |", "|---|---|---|---|"]
    for path in sorted(PAGES.glob("*.md")):
        rows = mechanical(path.stem)
        refuses = [n for n, ok, _, b in rows if b and not ok]
        noted = [n for n, ok, _, b in rows if not b and not ok]
        out.append(f"| {path.stem} | {status(path.read_text(encoding='utf-8'))} | {', '.join(refuses) or '—'} | {', '.join(noted) or '—'} |")
    return "\n".join(out) + "\n"


# --- selftest --------------------------------------------------------------

def selftest() -> int:
    page = ("---\nterm: T\nstatus: candidate\nsources: 1\n---\n\n# T\n\n**Lead.**\n\n"
            "## Reading — `a`, 2025-01-01, first\n\nA said „x“.\n\n"
            "## Reading — `c`, 2025-03-01, third\n\nC said „z“.\n\n"
            "## Where the sources differ\n\n- a against c.\n\n## Open\n\n- nothing.\n")
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "t.md").write_text(page, encoding="utf-8")
        led = d / "promotions.jsonl"
        results.append(("a candidate page and an empty ledger agree", check(d, led) == []))
        reviewed = set_fields(page, {"status": "reviewed", "reviewed": "2026-10-08"})
        (d / "t.md").write_text(reviewed, encoding="utf-8")
        results.append(("status reviewed with no ledger row fails", any("no promotion" in p for p in check(d, led))))
        led.write_text(json.dumps({"page": "t", "action": "promote", "on": "2026-10-08", "by": "author",
                                   "words": "w", "sha256": digest(reviewed)}) + "\n", encoding="utf-8")
        results.append(("a pinned page passes", check(d, led) == []))
        results.append(("the frontmatter is outside the pin",
                        digest(set_fields(reviewed, {"sources": "2", "conflict": "C1"})) == digest(reviewed)))
        (d / "t.md").write_text(reviewed.replace("A said", "A claimed"), encoding="utf-8")
        results.append(("an edit to the reviewed part fails", any("reviewed part changed" in p for p in check(d, led))))
        added = append_since(reviewed, "## Reading — `b`, 2025-02-01, second\n\nB said „y“.\n", ["- b sides with a."])
        (d / "t.md").write_text(added, encoding="utf-8")
        results.append(("a reading after review lands under Since review and passes",
                        check(d, led) == [] and added.index(SINCE) < added.index("`b`")
                        and added.index("## Open") < added.index(SINCE)))
        results.append(("the Since heading names the review date", "review of 2026-10-08" in added))
        added2 = append_since(added, "## Reading — `d`, 2025-04-01, fourth\n\nD said „w“.\n", [])
        results.append(("a second reading appends under the one Since heading", added2.count(SINCE) == 1))
        results.append(("since_readings lists both", since_readings(added2) == ["b", "d"]))
        folded = fold_since(added2)
        order = [m for m in READING.findall(folded)]
        results.append(("a re-review folds them into date order", order == ["a", "b", "c", "d"] and SINCE not in folded))
        results.append(("and their differ lines into the differences",
                        "- b sides with a." in folded.split("## Where the sources differ")[1].split("## Open")[0]))
        results.append(("frozen_end covers frontmatter and reviewed part",
                        added[:frozen_end(added)].rstrip().endswith("- nothing.") and frozen_end(page) == 0))
        led.write_text(led.read_text() + json.dumps({"page": "t", "action": "withdraw", "on": "2026-10-09",
                                                     "by": "author", "words": "w"}) + "\n", encoding="utf-8")
        results.append(("a withdrawn page still marked reviewed fails", any("no promotion" in p for p in check(d, led))))
        led.write_text(json.dumps({"page": "gone", "action": "promote", "on": "x", "by": "a", "words": "w", "sha256": ""}) + "\n")
        (d / "t.md").write_text(page, encoding="utf-8")
        results.append(("a ledger row for no page fails", any("no page" in p for p in check(d, led))))
    try:
        apply("t-does-not-matter", "", "author")
        results.append(("apply refuses without the author's words", False))
    except SystemExit as e:
        results.append(("apply refuses without the author's words", "--words" in str(e)))
    for name, ok in results:
        print(("held  " if ok else "FAILED") + "  " + name)
    failed = sum(1 for _, ok in results if not ok)
    print(f"{len(results) - failed} of {len(results)} held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb, rest = argv[0], argv[1:]

    def opt(name: str, default: str = "") -> str:
        return rest[rest.index(name) + 1] if name in rest and rest.index(name) + 1 < len(rest) else default

    if verb == "selftest":
        return selftest()
    if verb == "check":
        problems = check()
        reviewed = sum(1 for p in PAGES.glob("*.md") if is_reviewed(p.read_text(encoding="utf-8")))
        for p in problems:
            print("FAIL  " + p)
        print(f"{reviewed} reviewed page(s), {len(problems)} problem(s)")
        return 1 if problems else 0
    if verb == "sheet" and rest:
        print(sheet(rest[0]), end="")
        return 0
    if verb == "ready":
        print(ready(), end="")
        return 0
    if verb == "apply" and rest:
        print(json.dumps(apply(rest[0], opt("--words"), opt("--by", "author")), ensure_ascii=False))
        return 0
    if verb == "withdraw" and rest:
        print(json.dumps(withdraw(rest[0], opt("--words"), opt("--by", "author")), ensure_ascii=False))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
