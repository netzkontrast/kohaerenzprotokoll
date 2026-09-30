"""Readers write reading files; this writes the pages.

Until 2026-09-29 a reader wrote a reading straight onto a wiki page: it read the
whole page first, typed each line number it had asked `read.py --find` for, and
edited a file other readers might be editing. `Plan/concept/pipeline-optimization_2026-09-29.md`
(step 4, decision 015) moves the writing to code:

    Plan/runs/<batch>/readings/<page>--<document>.md     a reader writes this

    ---
    page: aegis                  # term, chapter, record or overview page
    document: <slug>
    date: 2025-10-15             # the document's date, for date order
    ---
    ## Reading — `<slug>`, 2025-10-15, the Inquiry file — what it adds

    Prose with each quotation „…" ^[?] — or ^[?L120] to prefer the hit nearest
    line 120 when the words stand on several lines.
    <!-- differ -->
    - One line for `## Where the sources differ`, if the document takes a side.

`apply` resolves every `^[?]` with `read.py`'s own comparison, so a line it
places cannot fail `quotes.py`; words it cannot place stop the file, with the
nearest lines named (P26: names in, lines by code). A reading goes before the
first reading with a later date on a term, chapter or overview page, and at the
end of a record, which is append-only. Nothing else on a page changes, and no
page is created.

**A file is refused, before anything is written, when** its date is not a date
or not its document's (2,301 of 2,301 dated readings on the pages carry the
manifest's date), its heading names another document or date, its document has
no census, note or `reconcile-pre.json` (a reading follows the lookup), its page
does not exist, a `[[link]]` in it points at no term or chapter page, or a
quotation in it carries no citation (`quotes.py`'s own verdict, P6).

**And `apply` writes only what its checks passed.** Every page is built in
memory; its `ingested:`, `sources:` and `readings:` are derived there (term pages
by `wiki_index.derive_frontmatter`, chapter and overview pages from their
`## Reading` headings); then quotations, count marks, links, frontmatter,
the chapter page rules and `lint_readings` run on the final text of every page,
each reported on its own line (P11). One failure, and nothing is written. Until
2026-09-30 `apply` wrote the pages and *recommended* those checks as next
steps; the review of that day fed it a quotation with no citation, a link to no
page, an invalid date and a heading naming another document, and it wrote all
four, with the frontmatter counts unchanged.

Usage:
    python3 scripts/readings.py check <batch>             # build and check everything, write nothing
    python3 scripts/readings.py apply <batch> [--root DIR] # the same, then write the pages (DIR: a worktree)
    python3 scripts/readings.py selftest
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import lint_readings  # noqa: E402
import quotes  # noqa: E402
import read  # noqa: E402
from digest import page_path  # noqa: E402
from subject import document  # noqa: E402
from wiki_index import derive_frontmatter, frontmatter, read_documents, rewrite_frontmatter  # noqa: E402

QUOTE_ASK = re.compile(r"„(?P<quote>[^„“]{1,400})[“\"](?P<gap>\s*)\^\[\?(?:L(?P<near>\d+))?\]")
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
DATE_IN_HEAD = re.compile(r"^## Readings? — `[^`]+`, (\d{4}-\d{2}-\d{2})")
# What a reading's and a record entry's first line must say: the document, then its date.
# One grammar, the singular: until the review of #120 (2026-09-30) this took `## Readings —`,
# which the chapter and overview frontmatter (READING_HEAD) and chapters.py do not count, so
# a plural reading landed with `sources: 0` and every check held. Some term pages carry the
# plural from before readings.py; DATE_IN_HEAD still reads them to place a reading by date.
HEAD_READING = re.compile(r"^## Reading — `(?P<slug>[^`]+)`, (?P<date>\S+?)(?:,|\s—|$)")
HEAD_RECORD = re.compile(r"^## (?P<entry>\S+) — `(?P<slug>[^`]+)`, (?P<date>\S+?)(?:,|\s—|$)")
# A link as chapters.py and relations.py read it; it may point at a term page or a chapter page.
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
READING_HEAD = re.compile(r"^## Reading — `([^`]+)`", re.M)
END_OF_READINGS = ("## Where the sources differ", "## Open", "## Occurrences only",
                   "## Questions for this chapter", "## Candidate sources", "## Raw qmd answers")


class Refused(Exception):
    pass


def parse(text: str) -> tuple[dict, str, list[str]]:
    m = FRONT.match(text)
    if not m:
        raise Refused("a reading file opens with frontmatter: page, document, date")
    meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    meta = {k.strip(): v.split("#")[0].strip() for k, v in meta.items()}
    for key in ("page", "document", "date"):
        if not meta.get(key):
            raise Refused(f"frontmatter lacks {key}")
    body = text[m.end():]
    differ: list[str] = []
    if "<!-- differ -->" in body:
        body, tail = body.split("<!-- differ -->", 1)
        differ = [line for line in tail.strip().splitlines() if line.strip()]
    return meta, body.strip() + "\n", differ


def resolve(body: str, slug: str) -> str:
    doc = document(slug)
    problems = []

    def place(m: re.Match) -> str:
        hits = read.locate(doc, m.group("quote"))
        if not hits:
            near = ", ".join(f"L{line} ({share:.0%})" for share, line, _ in read.nearest(doc, m.group("quote")))
            problems.append(f"„{m.group('quote')[:60]}…“ not in {slug}: nearest {near}")
            return m.group(0)
        if m.group("near"):
            target = int(m.group("near"))
            hit = min(hits, key=lambda h: abs(h - target))
        else:
            hit = hits[0]  # the first copy, as the readers' brief always asked
        return f"„{m.group('quote')}“{m.group('gap')}^[{slug}.md:L{hit}]"

    out = QUOTE_ASK.sub(place, body)
    if problems:
        raise Refused("; ".join(problems))
    if "^[?" in out:
        raise Refused("a ^[?] stands where no quotation precedes it")
    return out


def insert(page: str, section: str, date: str, record: bool) -> str:
    lines = page.rstrip("\n").split("\n")
    if record:
        return "\n".join(lines) + "\n\n" + section.rstrip("\n") + "\n"
    at = None
    for i, line in enumerate(lines):
        m = DATE_IN_HEAD.match(line)
        if m and m.group(1) > date:
            at = i
            break
        if line.startswith(END_OF_READINGS):
            at = i
            break
    if at is None:
        return "\n".join(lines) + "\n\n" + section.rstrip("\n") + "\n"
    return "\n".join(lines[:at] + section.rstrip("\n").split("\n") + [""] + lines[at:]) + "\n"


def add_differ(page: str, differ: list[str]) -> str:
    if not differ:
        return page
    head = "## Where the sources differ"
    if head in page:
        start = page.index(head)
        nxt = page.find("\n## ", start + len(head))
        end = nxt if nxt != -1 else len(page)
        block = page[start:end].rstrip("\n") + "\n" + "\n".join(differ) + "\n"
        return page[:start] + block + ("\n" + page[end + 1:] if nxt != -1 else "")
    for stop in ("## Open", "## Occurrences only", "## Questions for this chapter"):
        if stop in page:
            i = page.index(stop)
            return page[:i] + head + "\n\n" + "\n".join(differ) + "\n\n" + page[i:]
    return page.rstrip("\n") + "\n\n" + head + "\n\n" + "\n".join(differ) + "\n"


def is_date(text: str) -> bool:
    try:
        datetime.date.fromisoformat(text)
        return len(text) == 10
    except ValueError:
        return False


def link_targets(root: Path) -> set[str]:
    """What a `[[link]]` may point at: a term page or a chapter page (chapters.py's rule)."""
    return ({p.stem for p in (root / "Wiki" / "candidates").glob("*.md")}
            | {p.stem for p in (root / "Wiki" / "chapters").glob("kap-*.md")})


def uncited(text: str) -> list[str]:
    """Quotations `quotes.py` would not check or could not resolve, by its own verdict."""
    out = []
    for match, refs in quotes.pairs(text):
        status, why = quotes.verdict(refs, None, match.group("quote"))
        if status == "unchecked":
            out.append(f"„{match.group('quote')[:50]}…“ carries no citation naming a document")
        elif status == "unresolved":
            out.append(f"„{match.group('quote')[:50]}…“: {why}")
    return out + [f"a count mark: {m.get('why', m)}" for m in quotes.check_marks(text)[1]]


def validate(meta: dict, body: str, root: Path) -> Path:
    """Everything about a reading file that can be refused before a page is touched."""
    slug, date = meta["document"], meta["date"]
    if not is_date(date):
        raise Refused(f"date {date!r} is not a date (YYYY-MM-DD)")
    try:
        doc = document(slug)
    except KeyError:
        raise Refused(f"no landed document {slug!r}") from None
    if doc.date and doc.date != date:
        raise Refused(f"date {date} is not {slug}'s date, {doc.date} (the manifest)")
    for what, path in (("census", root / "Sources" / "terms" / f"{slug}.md"),
                       ("note", root / "Sources" / "notes" / f"{slug}.md"),
                       ("reconcile-pre.json", root / "Plan" / "runs" / slug / "reconcile-pre.json")):
        if not path.exists():
            raise Refused(f"{slug} has no {what} — a reading follows the extraction and the lookup")
    try:
        target = page_path(meta["page"], root)
    except SystemExit:
        raise Refused(f"no page {meta['page']!r} — readings.py creates none") from None
    record = "/conflicts/" in str(target) or "/questions/" in str(target)
    first = body.split("\n", 1)[0]
    head = (HEAD_RECORD if record else HEAD_READING).match(first)
    if not head:
        raise Refused(f"the heading does not read "
                      + ("`## <entry date> — `<slug>`, <date>, …`" if record
                         else "`## Reading — `<slug>`, <date>, …`") + f": {first[:80]}")
    if head.group("slug") != slug or head.group("date") != date:
        raise Refused(f"the heading names `{head.group('slug')}`, {head.group('date')}; "
                      f"the frontmatter says `{slug}`, {date}")
    if record and not is_date(head.group("entry")):
        raise Refused(f"the entry date {head.group('entry')!r} is not a date")
    return target


def build(reading_file: Path, root: Path, staged: dict | None = None) -> tuple[Path, str]:
    meta, body, differ = parse(reading_file.read_text(encoding="utf-8"))
    if not body.startswith("## "):
        raise Refused("the body opens with its heading")
    target = validate(meta, body, root)
    record = "/conflicts/" in str(target) or "/questions/" in str(target)
    section = resolve(body, meta["document"])
    differ = resolve("\n".join(differ), meta["document"]).strip().split("\n") if differ else []
    added = section + "\n".join(differ)
    known = link_targets(root)
    nowhere = sorted({t.strip() for t in LINK.findall(added)} - known)
    if nowhere:
        raise Refused("links to no term or chapter page: " + ", ".join(f"[[{t}]]" for t in nowhere))
    problems = uncited(added)
    if problems:
        raise Refused("; ".join(problems))
    page = (staged or {}).get(target) or target.read_text(encoding="utf-8")
    first = section.split("\n", 1)[0]
    if first in page:
        raise Refused(f"{target.name} already has this heading: {first}")
    return target, add_differ(insert(page, section, meta["date"], record), differ)


def wiki_dirty(root: Path) -> list[str]:
    """Readers write reading files, never pages: a changed page before apply means one did.

    `Wiki/compare/` is out of it: a reconciliation record is the reconciler's, written before or after a batch is applied,
    and a batch cannot half-write one (2026-09-30: a record drafted for the next batch refused the apply and had to be moved away).
    """
    import subprocess
    out = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", "Wiki", ":(exclude)Wiki/compare"],
                         capture_output=True, text=True).stdout
    return [line for line in out.splitlines() if line.strip()]


def derive_reading_frontmatter(text: str) -> str:
    """A chapter or overview page's `ingested:` and `sources:`, from its `## Reading` headings.

    The rule `chapters.py` checks: `ingested` holds exactly the documents with a
    reading, in the order they were read (kept ones first, new ones appended), and
    `sources` counts them.
    """
    meta = frontmatter(text)
    if "ingested" not in meta:
        return text
    readings = list(dict.fromkeys(READING_HEAD.findall(text)))
    have = [s for s in meta.get("ingested", []) if s in readings]
    ingested = have + [s for s in readings if s not in have]
    _, block, rest = text.split("---", 2)
    lines = block.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("ingested:"):
            lines[i] = "ingested: [" + ", ".join(f'"{s}"' for s in ingested) + "]"
        elif line.startswith("sources:"):
            lines[i] = f"sources: {len(ingested)}"
    return "---" + "\n".join(lines) + "---" + rest


def with_frontmatter(target: Path, text: str, root: Path) -> str:
    """The page as it will be written: its derived fields derived here, not afterwards."""
    if target.parent.name == "candidates":
        want = derive_frontmatter(text, read_documents(root / "Sources" / "terms"))
        if want["keep_readings"]:
            want["readings"] = int(frontmatter(text).get("readings", 0) or 0)
        return rewrite_frontmatter(text, want)
    if target.parent.name in ("chapters", "overview"):
        return derive_reading_frontmatter(text)
    return text


def checks(staged: dict[Path, str], root: Path, docs: set[str]) -> list[tuple[str, bool, str, list[str]]]:
    """Every check on the final text of every page: (name, held, summary, failures).

    A check compares the page as it will be written with the page as it is, so a
    defect already on a page does not block a batch that did not cause it, and one
    the batch adds always does.
    """
    import chapters
    known = link_targets(root)
    read_now = {p.parent.name for p in (root / "Plan" / "runs").glob("*/reconcile.json")} | docs
    records = set()
    for folder in ("conflicts", "questions"):
        for path in (root / "Wiki" / folder).glob("*.md"):
            found = frontmatter(path.read_text(encoding="utf-8")).get("id")
            if found:
                records.add(found)
    tallies = {"quotations": [0, 0, 0], "count marks": [0, 0], "links": [0, 0],
               "frontmatter": [0, 0], "chapter rules": [0], "lint": [0, 0]}
    failures: dict[str, list[str]] = {k: [] for k in tallies}
    for target, text in sorted(staged.items()):
        name = str(target.relative_to(root))
        before = target.read_text(encoding="utf-8")
        default = quotes.slug_of(target, text)
        new_bad, new_unchecked = quotes.check_file(target, default, text)
        old_bad, old_unchecked = quotes.check_file(target, default, before)
        tallies["quotations"][0] += len(quotes.pairs(text)) - new_unchecked
        if len(new_bad) > len(old_bad):
            failures["quotations"] += [f"{name}: {b['why']} — „{b['quote']}…“" for b in new_bad][len(old_bad):]
        if new_unchecked > old_unchecked:
            failures["quotations"].append(f"{name}: {new_unchecked - old_unchecked} quotations with no "
                                          "citation naming a document")
        made, wrong = quotes.check_marks(text)
        tallies["count marks"][0] += made
        if len(wrong) > len(quotes.check_marks(before)[1]):
            failures["count marks"] += [f"{name}: {w.get('why', w)}" for w in wrong]
        links = [t.strip() for t in LINK.findall(text)]
        tallies["links"][0] += len(links)
        nowhere = [t for t in links if t not in known]
        if len(nowhere) > len([t for t in LINK.findall(before) if t.strip() not in known]):
            failures["links"].append(f"{name}: " + ", ".join(f"[[{t}]]" for t in sorted(set(nowhere))))
        if target.parent.name == "candidates":
            tallies["frontmatter"][0] += 1
            again = with_frontmatter(target, text, root)
            if again != text:
                failures["frontmatter"].append(f"{name}: the derived fields do not settle")
        elif target.parent.name in ("chapters", "overview") and "ingested" in frontmatter(text):
            tallies["frontmatter"][1] += 1
            meta = frontmatter(text)
            readings = set(READING_HEAD.findall(text))
            if sorted(meta.get("ingested", [])) != sorted(readings) or meta.get("sources") != str(len(readings)):
                failures["frontmatter"].append(f"{name}: ingested/sources do not match the readings")
        if target.parent.name == "chapters":
            tallies["chapter rules"][0] += 1
            new = set(chapters.check_page(target, text, read_now, known, records))
            old = set(chapters.check_page(target, before, read_now, known, records))
            failures["chapter rules"] += sorted(new - old)
        on_page = sorted({d for d in docs if f"`{d}`" in text})
        flags, _ = lint_readings.lint_lines(text.split("\n"), name, on_page)
        for _, line, cls, excerpt in flags:
            if cls in lint_readings.WARN_ONLY:
                tallies["lint"][1] += 1
            else:
                tallies["lint"][0] += 1
                failures["lint"].append(f"{name}:{line} {cls} {excerpt[:60]}")
    q, m, ln, fm, ch, li = (tallies[k] for k in ("quotations", "count marks", "links",
                                                  "frontmatter", "chapter rules", "lint"))
    return [
        ("quotations", not failures["quotations"], f"{q[0]} cited on these pages; none unresolved or uncited "
         "that the pages did not already have" if not failures["quotations"] else "", failures["quotations"]),
        ("count marks", not failures["count marks"], f"{m[0]} marks", failures["count marks"]),
        ("links", not failures["links"], f"{ln[0]} links, each to a term or chapter page", failures["links"]),
        ("frontmatter", not failures["frontmatter"], f"derived on {fm[0]} term pages and "
         f"{fm[1]} chapter or overview pages", failures["frontmatter"]),
        ("chapter rules", not failures["chapter rules"], f"{ch[0]} chapter pages, chapters.py's rules",
         failures["chapter rules"]),
        ("lint", not failures["lint"], f"no defect in the batch's sections; {li[1]} comparison flags "
         "to read (warnings)", failures["lint"]),
    ]


def run(batch: str, write: bool, root: Path, folder: Path | None = None) -> int:
    folder = folder or ROOT / "Plan" / "runs" / batch / "readings"
    dirty = wiki_dirty(root) if write else []
    if dirty:
        print("REFUSED: Wiki/ has uncommitted changes — a reader edited a page, or a run is half-applied:")
        print("\n".join("  " + d for d in dirty[:20]))
        return 1
    files = sorted(folder.glob("*.md"))
    if not files:
        print(f"no reading files in {folder}")
        return 1
    staged: dict[Path, str] = {}
    docs: set[str] = set()
    failed = 0
    for f in files:
        try:
            target, text = build(f, root, staged)  # several documents on one page: each on the last
            staged[target] = text
            docs.add(parse(f.read_text(encoding="utf-8"))[0]["document"])
            print(f"ok       {f.name} → {target.relative_to(root)}")
        except Refused as e:
            failed += 1
            print(f"REFUSED  {f.name}: {e}")
    if failed:
        print(f"\n{failed} of {len(files)} files refused; nothing written.")
        return 1
    staged = {target: with_frontmatter(target, text, root) for target, text in staged.items()}
    results = checks(staged, root, docs)
    print(f"\nchecks on the {len(staged)} pages as they would be written, each on its own:")
    for name, held, said, problems in results:
        print(f"  {'held' if held else 'FAILED':7} {name:14} {said if held else f'{len(problems)} defects'}")
        for problem in problems[:12]:
            print(f"            {problem}")
    if not all(held for _, held, _, _ in results):
        print("\nA check failed; nothing written.")
        return 1
    if write:
        for target, text in staged.items():
            target.write_text(text, encoding="utf-8")
        stems = " ".join(sorted({target.stem for target in staged}))
        print(f"\n{len(staged)} pages written, frontmatter derived, every check above held. "
              f"Next: `python3 scripts/link.py --only {stems} --apply` marks the mentions the prose already makes "
              "in these pages alone; then one commit per page naming its document.")
    else:
        print(f"\n{len(staged)} pages would be written.")
    return 0


def selftest() -> int:
    slug = "entropie-aegis"
    doc = document(slug)
    date = doc.date
    line_no, line = next((doc.offset + i, l) for i, l in enumerate(doc.lines()) if len(l.split()) > 8)
    words = " ".join(line.split()[:5]).strip("*_#>- ")
    checks: list[tuple[str, bool]] = []

    def refused(name: str, text: str, root: Path, f: Path, want: str = "") -> None:
        f.write_text(text, encoding="utf-8")
        try:
            build(f, root)
            checks.append((name, False))
        except Refused as e:
            checks.append((name, want in str(e)))

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for folder in ("Wiki/candidates", "Wiki/chapters", "Wiki/conflicts", "Sources/terms",
                       "Sources/notes", f"Plan/runs/{slug}", "batch"):
            (root / folder).mkdir(parents=True)
        (root / "Sources/terms" / f"{slug}.md").write_text("census\n", encoding="utf-8")
        (root / "Sources/notes" / f"{slug}.md").write_text("note\n", encoding="utf-8")
        (root / f"Plan/runs/{slug}/reconcile-pre.json").write_text("{}\n", encoding="utf-8")
        page = root / "Wiki/candidates/probe.md"
        original = ("---\ntitle: P\nsources: 0\nreadings: 2\ningested: []\n---\n\n# P\n\nLead.\n\n"
                    "## Reading — `old`, 2025-01-01, old — a\n\nText.\n\n"
                    "## Reading — `new`, 2026-06-01, new — b\n\nText.\n\n"
                    "## Where the sources differ\n\n- old against new.\n")
        page.write_text(original, encoding="utf-8")
        good = (f"---\npage: probe\ndocument: {slug}\ndate: {date}\n---\n"
                f"## Reading — `{slug}`, {date}, E — c\n\nSays „{words}“ ^[?], as [[probe]] has it.\n"
                "<!-- differ -->\n- E takes a third side.\n")
        f = root / "batch" / "probe--e.md"
        f.write_text(good, encoding="utf-8")
        target, text = build(f, root)
        checks.append(("line placed by code", f"^[{slug}.md:L" in text))
        checks.append(("inserted in date order", text.index("`old`") < text.index(f"`{slug}`") < text.index("`new`")))
        checks.append(("differ line appended", "- E takes a third side." in text.split("## Where the sources differ")[1]))
        refused("words not in the document refused",
                good.replace(words, "Wörter die das Dokument nicht enthält und nie enthielt"), root, f, "nearest")
        refused("a ^[?] with no quotation refused", good + "\nStray ^[?] here.\n", root, f)
        # The four the review of 2026-09-30 fed build(), and it took:
        refused("a quotation with no citation refused",
                good.replace("as [[probe]] has it.", "and „eine Behauptung ohne jede Zeile dazu“."), root, f,
                "no citation")
        refused("a link to no page refused", good.replace("[[probe]]", "[[keine-seite]]"), root, f, "[[keine-seite]]")
        refused("an invalid date refused", good.replace(f"date: {date}", "date: 2026-13-45"), root, f, "not a date")
        refused("a date other than the document's refused", good.replace(f"date: {date}", "date: 2001-01-01"),
                root, f, "the manifest")
        refused("a heading naming another document refused",
                good.replace(f"## Reading — `{slug}`", "## Reading — `ein-anderes-dokument`"), root, f, "heading names")
        refused("a heading with another date refused",
                good.replace(f"`{slug}`, {date}, E", f"`{slug}`, 2001-01-01, E"), root, f, "heading names")
        # The review of #120: a plural heading was taken and then counted by nothing.
        refused("a plural heading refused", good.replace("## Reading — ", "## Readings — "), root, f,
                "the heading does not read")
        (root / f"Plan/runs/{slug}/reconcile-pre.json").unlink()
        refused("a document not yet looked up refused", good, root, f, "reconcile-pre.json")
        (root / f"Plan/runs/{slug}/reconcile-pre.json").write_text("{}\n", encoding="utf-8")
        refused("a page that does not exist refused", good.replace("page: probe", "page: keine-seite"), root, f,
                "no page")
        page.write_text(text, encoding="utf-8")
        refused("a heading already on the page refused", good, root, f, "already has")
        page.write_text(original, encoding="utf-8")
        rec = root / "Wiki/conflicts/c99-probe.md"
        rec.write_text("---\ntitle: C99\n---\n\n# C99\n\n## 2026-09-01 — `x`, 2026-01-01, first\n\nEntry.\n",
                       encoding="utf-8")
        f.write_text(good.replace("page: probe", "page: c99").replace("## Reading — ", "## 2026-09-29 — "),
                     encoding="utf-8")
        _, text = build(f, root)
        checks.append(("a record entry is appended at the end",
                       text.rstrip().endswith("third side.") and text.index("`x`") < text.index(f"`{slug}`")))
        # apply: the frontmatter derived in memory, and nothing written unless every check holds
        f.write_text(good, encoding="utf-8")
        chapter = root / "Wiki/chapters/kap-01.md"
        chapter.write_text('---\nchapter: 1\nsources: 1\ningested: ["old"]\n---\n\n# Kap 1\n\n'
                           "## Reading — `old`, 2025-01-01\n\nText.\n", encoding="utf-8")
        (root / "batch" / "kap-01--e.md").write_text(
            good.replace("page: probe", "page: kap-01").replace(", as [[probe]] has it", "")
                .split("<!-- differ -->")[0], encoding="utf-8")
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            status = run("selftest", True, root, root / "batch")
        term, chap = page.read_text(encoding="utf-8"), chapter.read_text(encoding="utf-8")
        checks.append(("apply writes, and derives a term page's frontmatter",
                       status == 0 and f'ingested: ["{slug}"]' in term and "sources: 1" in term
                       and "readings: 3" in term))
        checks.append(("apply derives a chapter page's frontmatter",
                       f'ingested: ["old", "{slug}"]' in chap and "sources: 2" in chap))
        # The same chapter reading with a plural heading: refused, and nothing is written.
        before = chap
        chapter.write_text('---\nchapter: 1\nsources: 1\ningested: ["old"]\n---\n\n# Kap 1\n\n'
                           "## Reading — `old`, 2025-01-01\n\nText.\n", encoding="utf-8")
        page.write_text(original, encoding="utf-8")
        plural = (root / "batch" / "kap-01--e.md")
        plural.write_text(plural.read_text(encoding="utf-8").replace("## Reading — ", "## Readings — "),
                          encoding="utf-8")
        kept = chapter.read_text(encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            status = run("selftest", True, root, root / "batch")
        checks.append(("a plural chapter reading writes nothing, and no frontmatter moves",
                       status == 1 and chapter.read_text(encoding="utf-8") == kept
                       and page.read_text(encoding="utf-8") == original and before != kept))
        page.write_text(original, encoding="utf-8")
        chapter.unlink()
        (root / "batch" / "kap-01--e.md").unlink()
        f.write_text(good.replace("as [[probe]] has it.", "as [[probe]] has it, in ` `."), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()) as out:
            status = run("selftest", True, root, root / "batch")
        checks.append(("a failed check writes nothing", status == 1 and "EMPTY_CODE" in out.getvalue()
                       and page.read_text(encoding="utf-8") == original))
        (root / "batch" / "zz--bad.md").write_text(good.replace(f"date: {date}", "date: 2026-13-45"), encoding="utf-8")
        f.write_text(good, encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            status = run("selftest", True, root, root / "batch")
        checks.append(("one refused file writes nothing", status == 1 and page.read_text(encoding="utf-8") == original))
    # The guard: a page a reader edited refuses an apply, a reconciliation record drafted beside the batch does not.
    import subprocess
    with tempfile.TemporaryDirectory() as tmp:
        g = Path(tmp)

        def git(*args: str) -> None:
            subprocess.run(["git", "-C", str(g), "-c", "user.email=t@t", "-c", "user.name=t", *args],
                           capture_output=True, text=True)

        git("init", "-q")
        (g / "Wiki/candidates").mkdir(parents=True)
        (g / "Wiki/compare").mkdir(parents=True)
        (g / "Wiki/candidates/x.md").write_text("x\n", encoding="utf-8")
        git("add", ".")
        git("commit", "-qm", "x")
        (g / "Wiki/compare/reconcile-1-y.md").write_text("record\n", encoding="utf-8")
        checks.append(("a reconciliation record beside the batch does not refuse an apply", wiki_dirty(g) == []))
        (g / "Wiki/candidates/x.md").write_text("edited\n", encoding="utf-8")
        checks.append(("a page a reader edited does", len(wiki_dirty(g)) == 1))
    failed = [n for n, ok in checks if not ok]
    print(f"readings: {len(checks) - len(failed)} of {len(checks)} cases hold" +
          (f" — FAILED: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if len(argv) < 2 or argv[0] not in ("check", "apply"):
        print(__doc__)
        return 2
    root = Path(argv[argv.index("--root") + 1]).resolve() if "--root" in argv else ROOT
    return run(argv[1], argv[0] == "apply", root)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
