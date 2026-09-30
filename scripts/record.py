"""The reconciliation record, drafted by code where it is mechanical.

A reconciliation ends with two files per document: `Plan/runs/<slug>/reconcile.json`
and `Wiki/compare/reconcile-NN-<slug>.md`. Fifty-one of each were written by hand,
and most of what they hold is already on disk once the readings are applied:

- the lookup's counts and the state it ran against — `reconcile-pre.json`;
- the pages that took a reading, and the lines each cites — the pages' own
  `## Reading — `<slug>`` sections and `^[<slug>.md:Lnn]` references;
- the chapter pages with a reading, and the lines `Wiki/overview/plot.md` cites;
- the conflict and question records with an entry — their `## <date> — `<slug>`` headings;
- the judgements and the sweep calls — the ledger rows that name the document;
- the pages it created — pages whose `ingested:` begins with it;
- the state it left — `wiki_index.build_index()`;
- the decision sheets it bears on — `askdb.py touches <slug>`, when `.venv-dspy`
  and `Plan/derived/ask.db` exist.

`draft` writes all of that, and marks what stays judgement with `<reconciler: …>`:
why no page was created, what was not promoted and why, what the rules decided,
what the readers noticed that no record holds. A reading's one-line note is its
heading's own last clause, so it is copied, not written.

`check` compares a saved `reconcile.json` with the pages as they stand, field by
field (P11), and fails on a mark left. `measure` runs the same comparison over
every reconciled document: how far the hand-written records agree with what the
wiki says. Standard library only.

    python3 scripts/record.py draft <slug>      # Plan/runs/<slug>/reconcile-draft.json, record-draft.md
    python3 scripts/record.py check <slug>      # reconcile.json against the pages; exit 1 on a difference
    python3 scripts/record.py measure [--from N] # every record from document N on, field by field
    python3 scripts/record.py selftest

It deliberately does not decide anything a reconciler decides: whether a page is
created, whether a sweep hit is a reading, whether a near match is one term or
two, or whether a reading conflicts with another (never mechanised, CLAUDE.md).
"""

from __future__ import annotations

import datetime
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

MARK = "<reconciler:"
# Fields whose values are derived from the files; everything else in a record is judgement.
MECHANICAL = ("pre_classification", "state_before", "new_readings", "chapters", "plot_overview",
              "conflicts_changed", "questions_changed", "judgements", "new_terms")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def cited(text: str, slug: str) -> list[int]:
    """Every file line of `slug` that `text` cites, sorted and once each."""
    refs = re.findall(rf"\^\[{re.escape(slug)}\.md:([^\]\n]+)\]", text)
    return sorted({int(n) for ref in refs for n in re.findall(r"L(\d+)", ref)})


def section(text: str, start: int) -> str:
    """The section a heading at `start` opens: up to the next `## ` heading."""
    end = text.find("\n## ", start + 3)
    return text[start:end if end >= 0 else len(text)]


def heading(slug: str) -> re.Pattern:
    """A reading of `slug`: its heading, and the clause after the last ` — `."""
    return re.compile(rf"^## Readings? — `{re.escape(slug)}`[^\n]*?(?: — (?P<note>[^\n—]+))?$", re.M)


def derive(slug: str, root: Path = ROOT, touches: bool = True) -> dict:
    """Everything a record says that the files already say."""
    wiki, runs = root / "Wiki", root / "Plan" / "runs"
    out: dict = {"document": slug}
    pre_file = runs / slug / "reconcile-pre.json"
    pre: dict = {}
    if pre_file.exists():
        pre = json.loads(pre_file.read_text(encoding="utf-8"))
        out["state_before"] = pre.get("state")
        out["pre_classification"] = {"candidates": pre.get("candidates"), "decisions": pre.get("decisions"),
                                     "decided_by_lookup": pre.get("decided_mechanically"),
                                     "needs_judgement": pre.get("needs_judgement")}
    readings = []
    for page in sorted((wiki / "candidates").glob("*.md")):
        text = page.read_text(encoding="utf-8")
        heads = list(heading(slug).finditer(text))
        if heads:
            note = next((h.group("note").strip() for h in heads if h.group("note")), "")
            # The reading's own lines: what its sections cite. A line of it cited under
            # `## Where the sources differ` or `## Occurrences only` belongs to no reading
            # (measured on documents 40–51: the hand records never listed those).
            own = [cited(section(text, h.start()), slug) for h in heads]
            readings.append({"page": page.stem, "lines": sorted({n for ls in own for n in ls}), "note": note})
    out["new_readings"] = readings
    if "pages_at_lookup" in (pre if pre_file.exists() else {}):
        now = sorted(p.stem for p in (wiki / "candidates").glob("*.md"))
        out["new_terms"] = sorted(set(now) - set(pre["pages_at_lookup"]))
    out["chapters"] = {"readings_on": sorted(
        int(re.sub(r"\D", "", p.stem)) for p in (wiki / "chapters").glob("kap-*.md")
        if heading(slug).search(p.read_text(encoding="utf-8")))}
    plot = wiki / "overview" / "plot.md"
    out["plot_overview"] = {"lines": cited(plot.read_text(encoding="utf-8"), slug) if plot.exists() else []}
    entry = re.compile(rf"^## \S+ — `{re.escape(slug)}`", re.M)
    for key, folder in (("conflicts_changed", "conflicts"), ("questions_changed", "questions")):
        found = [p.stem.split("-", 1)[0].upper() for p in sorted((wiki / folder).glob("[cq][0-9]*.md"))
                 if entry.search(p.read_text(encoding="utf-8"))]
        out[key] = sorted(found, key=lambda r: int(r[1:]))
    out["judgements"] = [r["id"] for r in read_jsonl(runs / "judgements.jsonl") if r.get("document") == slug]
    out["sweep"] = [{k: r.get(k) for k in ("page", "surface", "line", "decision", "why")}
                    for r in read_jsonl(runs / "sweep.jsonl") if r.get("document") == slug]
    if touches:
        out["sheets"] = sheets(slug, root)
    return out


def sheets(slug: str, root: Path = ROOT) -> dict | None:
    """The decision sheets `askdb.py touches` finds through the pages this document is on."""
    python = root / ".venv-dspy" / "bin" / "python"
    if not python.exists() or not (root / "Plan" / "derived" / "ask.db").exists():
        return None
    try:
        proc = subprocess.run([str(python), str(root / "scripts" / "askdb.py"), "touches", slug],
                              capture_output=True, text=True, timeout=300, cwd=root)
        found = json.loads(proc.stdout)["sheets"]
    except (subprocess.SubprocessError, ValueError, KeyError):
        return None
    return {sheet: sorted(p.split(":", 1)[-1] for p in pages) for sheet, pages in sorted(found.items())}


def state(root: Path = ROOT) -> dict:
    import wiki_index
    index = wiki_index.build() if root == ROOT else {
        "pages": len(list((root / "Wiki" / "candidates").glob("*.md"))),
        "conflicts": len(list((root / "Wiki" / "conflicts").glob("c[0-9]*.md")))}
    return {"pages": index["pages"], "conflicts": index["conflicts"]}


def next_number(root: Path = ROOT) -> int:
    numbers = [int(m.group(1)) for p in (root / "Wiki" / "compare").glob("reconcile-*.md")
               if (m := re.match(r"reconcile-(\d+)-", p.name))]
    return max(numbers, default=0) + 1


def draft(slug: str, root: Path = ROOT) -> tuple[dict, str]:
    """The record and the compare page, with every judgement marked."""
    from subject import document
    got = derive(slug, root)
    doc = document(slug)
    manifest = next((r for r in read_jsonl(root / "Sources" / "manifest.jsonl") if r.get("slug") == slug), {})
    today = datetime.date.today().isoformat()
    record = {
        "document": slug, "drive_id": manifest.get("drive_id"), "step": "reconcile", "at": today,
        "by": f"{MARK} who read and who wrote the readings, and the brief they followed>",
        "state_before": got.get("state_before"), "state_after": state(root),
        "pre_classification": got.get("pre_classification"),
        "new_terms": got.get("new_terms", f"{MARK} the pages this reconciliation created — its lookup "
                                           f"predates pages_at_lookup>"),
        "why_no_new_terms": f"{MARK} why no candidate became a page>" if not got.get("new_terms") else None,
        "new_readings": [{"page": r["page"], "lines": r["lines"], "attribution": "", "note": r["note"]}
                         for r in got["new_readings"]],
        "chapters": got["chapters"], "plot_overview": got["plot_overview"],
        "new_surfaces": [], "new_conflicts": [],
        "conflicts_changed": got["conflicts_changed"], "questions_changed": got["questions_changed"],
        "judgements": got["judgements"],
        "decided_by_existing_rules": f"{MARK} the rules that settled the near matches, by id>",
        "sweep": got["sweep"], "sheets": got.get("sheets"),
        "not_promoted": [f"{MARK} a candidate that got no page, and where its reading went>"],
        "internal_tension": f"{MARK} what the document says two ways, or none>",
        "baseline_moved": f"{MARK} graphrag.py bench against the last row of baselines.jsonl>",
    }
    record = {k: v for k, v in record.items() if v is not None}
    n = next_number(root)
    pre = got.get("pre_classification") or {}
    pages = [r["page"] for r in got["new_readings"]]
    lines = [
        "---", f"document: {slug}",
        f"against: {(got.get('state_before') or {}).get('pages')} pages, "
        f"{(got.get('state_before') or {}).get('conflicts')} conflicts",
        f'ran: "{today}"', f"candidates: {pre.get('candidates')}", f"decisions: {pre.get('decisions')}",
        f"by_lookup: {pre.get('decided_by_lookup')}", f"judgements: {pre.get('needs_judgement')}",
        f"new_pages: {len(got.get('new_terms') or [])}", f"new_readings: {len(pages)}", "---", "",
        f"# Reconciliation {n} — `{slug}` against the wiki", "",
        f"`python3 scripts/reconcile.py {slug}`", "",
        f"{pre.get('candidates')} candidates, {pre.get('decisions')} decisions — **{pre.get('decided_by_lookup')} "
        f"by lookup, {pre.get('needs_judgement')} to judgement**. Dated {doc.date} by the manifest. "
        f"{MARK} what the document is, in its own words, and its standing as it claims it>", "",
        "## New pages" if got.get("new_terms") else "## No new page", "",
        (", ".join(f"`{p}`" for p in got["new_terms"]) + ". " if got.get("new_terms") else "")
        + f"{MARK} why, from the readings, and what was not promoted>", "",
        "## Judgements", "",
        (", ".join(got["judgements"]) + ", recorded in `Plan/runs/judgements.jsonl`. "
         if got["judgements"] else "No new judgement. ")
        + f"{MARK} the rules that settled the near matches>", "",
        f"## Readings — {len(pages)} pages", "",
        ", ".join(f"`{p}`" for p in pages) + ".", "",
        ("Chapter pages: " + ", ".join(f"Kap {k}" for k in got["chapters"]["readings_on"]) + "."
         if got["chapters"]["readings_on"] else "No chapter page."),
        ("`plot.md` cites lines " + ", ".join(f"L{n}" for n in got["plot_overview"]["lines"]) + "."
         if got["plot_overview"]["lines"] else "`plot.md` cites it nowhere."),
        "Conflicts with an entry from it: " + (", ".join(got["conflicts_changed"]) or "none")
        + ". Questions: " + (", ".join(got["questions_changed"]) or "none") + ".", "",
        "## Sweep", "",
        ("; ".join(f"`{s['surface']}` L{s['line']} {s['decision']}" + (f" — {s['why']}" if s.get("why") else "")
                   for s in got["sweep"]) + "." if got["sweep"] else "No hit the census did not list."), "",
    ]
    if got.get("sheets") is not None:
        lines += ["## Decision sheets", "",
                  ("`askdb.py touches`: " + "; ".join(f"{s} through " + ", ".join(f"`{p}`" for p in ps)
                                                       for s, ps in got["sheets"].items()) + "."
                   if got["sheets"] else "`askdb.py touches`: no sheet names a page this document is on."), ""]
    lines += ["## What the readers noticed and no record holds", "", f"{MARK} or delete this section>", ""]
    return record, "\n".join(lines)


def ids(values) -> list[str]:
    """A list the records wrote as ids or as objects — the early ones wrote objects — as ids."""
    out = []
    for v in values or []:
        if isinstance(v, dict):
            v = v.get("id") or v.get("page") or v.get("slug") or v.get("term") or json.dumps(v, sort_keys=True)
        out.append(str(v))
    return out


def check(slug: str, root: Path = ROOT, record: dict | None = None) -> list[str]:
    """Where a saved record and the pages disagree, field by field, and every mark left."""
    if record is None:
        f = root / "Plan" / "runs" / slug / "reconcile.json"
        if not f.exists():
            return [f"no {f.relative_to(root)}"]
        record = json.loads(f.read_text(encoding="utf-8"))
    got = derive(slug, root, touches=False)
    problems = [f"a `{MARK}` mark is left in `{k}`" for k, v in record.items() if MARK in json.dumps(v)]
    for key in MECHANICAL:
        if key not in record or key not in got:
            continue
        want, have = got[key], record[key]
        # The early records wrote some of these as prose; a sentence is not compared.
        if key in ("chapters", "plot_overview", "pre_classification", "state_before") and not isinstance(have, dict):
            continue
        if key not in ("chapters", "plot_overview", "pre_classification", "state_before") and not isinstance(have, list):
            continue
        if key == "new_readings":
            want = {r["page"]: r["lines"] for r in want}
            have = {r["page"]: sorted(n for n in (r.get("lines") or []) if isinstance(n, int))
                    for r in have if isinstance(r, dict) and "page" in r}
            for page in sorted(set(want) | set(have)):
                if page not in have:
                    problems.append(f"new_readings: `{page}` has a reading of it, the record does not list it")
                elif page not in want:
                    problems.append(f"new_readings: the record lists `{page}`, the page has no reading of it")
                elif want[page] != have[page]:
                    problems.append(f"new_readings: `{page}` cites {want[page]}, the record says {have[page]}")
        elif key in ("conflicts_changed", "questions_changed", "judgements", "new_terms"):
            if sorted(ids(want)) != sorted(ids(have)):
                problems.append(f"{key}: the files say {sorted(ids(want))}, the record says {sorted(ids(have))}")
        elif key == "chapters":
            if sorted(want["readings_on"]) != sorted((have or {}).get("readings_on") or []):
                problems.append(f"chapters: the pages say {want['readings_on']}, "
                                f"the record says {(have or {}).get('readings_on')}")
        elif key == "plot_overview":
            if want["lines"] != sorted((have or {}).get("lines") or []):
                problems.append(f"plot_overview: plot.md cites {want['lines']}, the record says {(have or {}).get('lines')}")
        elif want != have:
            problems.append(f"{key}: the files say {want}, the record says {have}")
    return problems


def measure(first: int = 0, root: Path = ROOT) -> int:
    """Every hand-written record against the pages as they stand now, field by field."""
    numbered = {}
    for p in (root / "Wiki" / "compare").glob("reconcile-*.md"):
        m = re.match(r"reconcile-(\d+)-(.+)\.md$", p.name)
        if m:
            numbered[m.group(2)] = int(m.group(1)) - 1
    rows, fields = [], {}
    for f in sorted((root / "Plan" / "runs").glob("*/reconcile.json")):
        slug = f.parent.name
        if numbered.get(slug, -1) < first:
            continue
        problems = check(slug, root, json.loads(f.read_text(encoding="utf-8")))
        problems = [p for p in problems if MARK not in p]
        rows.append((numbered.get(slug), slug, problems))
        for p in problems:
            fields[p.split(":", 1)[0]] = fields.get(p.split(":", 1)[0], 0) + 1
    for n, slug, problems in sorted(rows, key=lambda r: (r[0] is None, r[0] or 0)):
        print(f"  {n if n is not None else '?':>3}  {slug[:58]:<58}  {'agrees' if not problems else f'{len(problems)} differ'}")
        for p in problems[:4]:
            print(f"         {p[:150]}")
    agree = sum(1 for r in rows if not r[2])
    print(f"\n{agree} of {len(rows)} records agree with the pages in every mechanical field"
          + (f"; differences by field: " + ", ".join(f"{k} {v}" for k, v in sorted(fields.items())) if fields else ""))
    return 0


def selftest() -> int:
    slug = "entropie-aegis"
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for folder in ("Wiki/candidates", "Wiki/chapters", "Wiki/conflicts", "Wiki/questions",
                       "Wiki/overview", "Wiki/compare", f"Plan/runs/{slug}"):
            (root / folder).mkdir(parents=True)
        (root / "Wiki/candidates/probe.md").write_text(
            f'---\ningested: ["{slug}", "other"]\n---\n\n# Probe\n\n'
            f"## Reading — `{slug}`, 2025-04-17, the brief — what it adds\n\n"
            f"„a…“ ^[{slug}.md:L21] and „b…“ ^[{slug}.md:L9]\n\n"
            f"## Where the sources differ\n\n- it says so ^[{slug}.md:L50].\n", encoding="utf-8")
        (root / "Wiki/candidates/other.md").write_text(
            f'---\ningested: ["other"]\n---\n\n## Reading — `other`, 2026-01-01\n\nCites ^[{slug}.md:L3] in passing.\n',
            encoding="utf-8")
        (root / "Wiki/chapters/kap-07.md").write_text(f"## Reading — `{slug}`, 2025-04-17\n\nText.\n",
                                                       encoding="utf-8")
        (root / "Wiki/conflicts/c2-probe.md").write_text(f"# C2\n\n## 2026-09-01 — `{slug}`, 2025-04-17\n\nEntry.\n",
                                                          encoding="utf-8")
        (root / "Wiki/questions/q3-probe.md").write_text("# Q3\n\n## 2026-09-01 — `other`, 2026-01-01\n",
                                                          encoding="utf-8")
        (root / "Wiki/overview/plot.md").write_text(f"Plot ^[{slug}.md:L40].\n", encoding="utf-8")
        (root / f"Plan/runs/{slug}/reconcile-pre.json").write_text(json.dumps(
            {"state": {"pages": 1, "conflicts": 1}, "pages_at_lookup": ["other"], "candidates": 5,
             "decisions": 5, "decided_mechanically": 4, "needs_judgement": 1}), encoding="utf-8")
        (root / "Plan/runs/judgements.jsonl").write_text(json.dumps({"id": "J7", "document": slug}) + "\n",
                                                         encoding="utf-8")
        (root / "Plan/runs/sweep.jsonl").write_text(json.dumps(
            {"document": slug, "page": "other", "surface": "Other", "line": 3, "decision": "occurrence",
             "why": "a title"}) + "\n", encoding="utf-8")
        got = derive(slug, root, touches=False)
        cases.append(("a reading's page and every line it cites, once, sorted",
                      got["new_readings"] == [{"page": "probe", "lines": [9, 21], "note": "what it adds"}]))
        cases.append(("a line cited under the differences is no reading's",
                      50 not in got["new_readings"][0]["lines"]))
        cases.append(("a page that only cites it has no reading of it",
                      all(r["page"] != "other" for r in got["new_readings"])))
        cases.append(("a page it created: there now, not at the lookup", got["new_terms"] == ["probe"]))
        cases.append(("chapters, plot, records, ledgers",
                      got["chapters"] == {"readings_on": [7]} and got["plot_overview"] == {"lines": [40]}
                      and got["conflicts_changed"] == ["C2"] and got["questions_changed"] == []
                      and got["judgements"] == ["J7"] and got["sweep"][0]["decision"] == "occurrence"))
        record = {k: got[k] for k in MECHANICAL}
        cases.append(("a record equal to the files holds", check(slug, root, record) == []))
        wrong = json.loads(json.dumps(record))
        wrong["new_readings"][0]["lines"] = [9]
        cases.append(("a line dropped from a reading is named",
                      any("`probe` cites [9, 21]" in p for p in check(slug, root, wrong))))
        wrong = dict(record, conflicts_changed=["C2", "C9"])
        cases.append(("a record claiming an entry the record page lacks is named",
                      any(p.startswith("conflicts_changed") for p in check(slug, root, wrong))))
        wrong = dict(record, why_no_new_terms=f"{MARK} why>")
        cases.append(("a mark left is named", any("mark is left" in p for p in check(slug, root, wrong))))
    failed = [n for n, ok in cases if not ok]
    print(f"record: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["measure"]:
        first = int(argv[argv.index("--from") + 1]) if "--from" in argv else 0
        return measure(first)
    if len(argv) != 2 or argv[0] not in ("draft", "check"):
        print(__doc__)
        return 2
    verb, slug = argv
    if verb == "draft":
        record, page = draft(slug)
        run = ROOT / "Plan" / "runs" / slug
        (run / "reconcile-draft.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                                                  encoding="utf-8")
        (run / "record-draft.md").write_text(page, encoding="utf-8")
        print(f"wrote {(run / 'reconcile-draft.json').relative_to(ROOT)} and {(run / 'record-draft.md').relative_to(ROOT)}"
              f" — fill every `{MARK}` mark, then save them as reconcile.json and "
              f"Wiki/compare/reconcile-{next_number():02d}-{slug}.md")
        return 0
    problems = check(slug)
    for p in problems:
        print(f"  {p}")
    print(f"record {slug}: " + ("holds" if not problems else f"{len(problems)} differences"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
