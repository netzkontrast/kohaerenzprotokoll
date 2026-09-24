#!/usr/bin/env python3
"""Check Hyper-Extract templates against Hyper-Extract and against this project.

    python3 scripts/templates.py check [FILE ...]   # default: Plan/hyperextract/*.yaml
    python3 scripts/templates.py selftest           # every check shown to fail on its defect

Hyper-Extract's own validator (`he template validate`, HE-T001..009) checks the
configuration schema. It passed a template whose field `register` shadows a pydantic
attribute — the warning appears only when the template is *loaded* — so loading is
its own check here. Then the rules that are this project's, not Hyper-Extract's:

| check        | the rule                                                                  |
|--------------|---------------------------------------------------------------------------|
| validate     | `he template validate`: 0 errors, 0 warnings                              |
| load         | localize + parse_* as `he parse` does: 0 warnings                         |
| no-line      | no field carries a line or page: names in, lines by code (P26)            |
| no-llm-merge | no `llm_*` merge strategy: two readings are never merged into one (P13)   |
| merge-set    | set and graph templates name their strategy; the default overwrites (keep_incoming) |
| provisional  | the header says `provisional`, `may not` and `retire when` (CLAUDE.md)     |
| procedural   | no wiki surface or verified entity name in the text a model is sent — a  |
|              | template carries procedural knowledge only (Plan/briefings/extract.md)    |

Each check reports its own status (P11); one that could not run is `not reached`,
never passed (P15); `procedural` says how many names it could not check (P23).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
DIR = ROOT / "Plan" / "hyperextract"
LINE_FIELDS = re.compile(r"^\s*-\s*name:\s*(line|lines|line_number|line_no|page|pages)\s*$", re.M)
STRATEGY = re.compile(r"^\s*(merge_strategy|entity_merge_strategy|relation_merge_strategy):\s*(\S+)", re.M)

LOADER = r"""
import json, sys, warnings, yaml
from hyperextract.utils.template_engine.parsers import (parse_output, parse_guideline,
    parse_identifiers, parse_display, parse_option)
from hyperextract.utils.template_engine.parsers.loader import localize_template
from hyperextract.utils.template_engine.template import TemplateCfg
out = {}
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try:
            cfg = localize_template(TemplateCfg(**raw), "en")
            parse_output(cfg.output, cfg.type); parse_identifiers(cfg.identifiers, cfg.type)
            parse_display(cfg.display, cfg.type); parse_option(cfg.options, cfg.type, override={})
            p = parse_guideline(cfg.guideline, cfg.type, "en")
            out[path] = {"warnings": [str(x.message)[:160] for x in w if not issubclass(x.category, ResourceWarning)],
                         "prompt": p if isinstance(p, str) else "\n".join(p)}
        except Exception as e:
            out[path] = {"error": f"{type(e).__name__}: {e}"[:300]}
print(json.dumps(out))
"""


def he_python() -> Path | None:
    he = shutil.which("he")
    if not he:
        return None
    py = Path(he).resolve().parent / "python"
    return py if py.exists() else None


def sent_text(text: str) -> str:
    """What a model can be sent: everything but the YAML comments."""
    return "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))


def known_names() -> tuple[list[str], list[str]]:
    names: set[str] = set()
    index = ROOT / "Wiki" / "index.json"
    if index.exists():
        for t in json.loads(index.read_text(encoding="utf-8"))["terms"].values():
            names |= set(t["surfaces"])
    try:
        import entities as E
        names |= {r["term"] for e in E.lists() for r in E.verify(e)["rows"] if r.get("verified")}
    except Exception:
        pass
    ordered = sorted(names, key=len, reverse=True)
    return [n for n in ordered if len(n) > 2], [n for n in ordered if len(n) <= 2]


def project_checks(text: str, names: list[str]) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    body = sent_text(text)
    m = LINE_FIELDS.search(body)
    out["no-line"] = ("FAIL", f"field {m.group(1)!r}") if m else ("ok", "")
    strategies = dict(STRATEGY.findall(body))
    llm = [v for v in strategies.values() if v.startswith("llm_")]
    out["no-llm-merge"] = ("FAIL", ", ".join(llm)) if llm else ("ok", "")
    kind = re.search(r"^type:\s*(\S+)", body, re.M)
    kind = kind.group(1) if kind else "?"
    if kind == "set":
        ok = "merge_strategy" in strategies
    elif "graph" in kind:
        ok = "entity_merge_strategy" in strategies and "relation_merge_strategy" in strategies
    else:
        ok = True
    out["merge-set"] = ("ok", "") if ok else ("FAIL", f"{kind} without an explicit merge strategy")
    header = "\n".join(l for l in text.splitlines() if l.lstrip().startswith("#"))
    missing = [k for k in ("provisional", "may not", "retire when") if k not in header]
    out["provisional"] = ("FAIL", "missing " + ", ".join(missing)) if missing else ("ok", "")
    leaked = [n for n in names if re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", body)]
    out["procedural"] = ("FAIL", "corpus names: " + ", ".join(leaked[:6])) if leaked else ("ok", "")
    return out


def check(paths: list[Path]) -> int:
    names, short = known_names()
    print(f"procedural: {len(names)} wiki surfaces and verified entity names checked; "
          f"{len(short)} of two characters or fewer cannot be ({', '.join(short) or 'none'})\n")
    results: dict[Path, dict[str, tuple[str, str]]] = {p: {} for p in paths}
    he = shutil.which("he")
    for p in paths:
        if not he:
            results[p]["validate"] = ("not reached", "he is not installed: scripts/install.sh hyperextract")
            continue
        r = subprocess.run([he, "template", "validate", str(p)], capture_output=True, text=True)
        text = r.stdout + r.stderr
        clean = r.returncode == 0 and "HE-T" not in text
        results[p]["validate"] = ("ok", "") if clean else ("FAIL", " ".join(
            l.strip() for l in text.splitlines() if "HE-T" in l)[:200] or text.strip()[-200:])
    py = he_python()
    if py:
        r = subprocess.run([str(py), "-c", LOADER, *map(str, paths)], capture_output=True, text=True)
        loaded = json.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 and r.stdout.strip() else {}
        for p in paths:
            got = loaded.get(str(p))
            if got is None:
                results[p]["load"] = ("not reached", (r.stderr.strip().splitlines() or ["no output"])[-1][:200])
            elif "error" in got:
                results[p]["load"] = ("FAIL", got["error"])
            else:
                results[p]["load"] = ("FAIL", "; ".join(got["warnings"])) if got["warnings"] else ("ok", "")
    else:
        for p in paths:
            results[p]["load"] = ("not reached", "no hyperextract interpreter beside `he`")
    for p in paths:
        results[p].update(project_checks(p.read_text(encoding="utf-8"), names))
    order = ["validate", "load", "no-line", "no-llm-merge", "merge-set", "provisional", "procedural"]
    failed = unreached = 0
    for p in paths:
        print(p.relative_to(ROOT) if p.is_relative_to(ROOT) else p)
        for k in order:
            status, why = results[p][k]
            failed += status == "FAIL"
            unreached += status == "not reached"
            print(f"  {status:<11} {k:<13} {why}")
    print(f"\n{len(paths)} template(s), {len(order)} checks each: {failed} failed, {unreached} not reached")
    return 1 if failed else (2 if unreached else 0)


GOOD = """# provisional — fixture
# may not: anything
# retire when: never
language: en
name: Fixture
type: set
tags: [fixture]
description: 'A fixture.'
output:
  description: 'Terms.'
  fields:
    - name: term
      type: str
      description: 'The term.'
      required: true
guideline:
  target: 'List the terms.'
  rules:
    - 'Copy each term exactly.'
identifiers:
  item_id: term
options:
  merge_strategy: merge_field
display:
  label: '{term}'
"""

DEFECTS = {
    "load": GOOD.replace("name: term\n", "name: register\n").replace("item_id: term", "item_id: register")
                .replace("'{term}'", "'{register}'"),
    "no-line": GOOD.replace("      required: true\nguideline",
                            "      required: true\n    - name: line\n      type: int\n      description: 'x'\nguideline"),
    "no-llm-merge": GOOD.replace("merge_field", "llm_balanced"),
    "merge-set": GOOD.replace("options:\n  merge_strategy: merge_field\n", ""),
    "provisional": GOOD.replace("# retire when: never\n", ""),
    "procedural": GOOD.replace("Copy each term exactly.", "Copy each term exactly, like AEGIS."),
    "validate": GOOD.replace("type: set", "type: sett"),
}


def selftest() -> int:
    names, _ = known_names()
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        good = Path(tmp) / "Good.yaml"
        good.write_text(GOOD, encoding="utf-8")
        baseline = project_checks(GOOD, names)
        ok = all(s == "ok" for s, _ in baseline.values())
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} the clean fixture passes every project check")
        if shutil.which("he"):
            r = subprocess.run(["he", "template", "validate", str(good)], capture_output=True, text=True)
            ok = r.returncode == 0 and "HE-T" not in r.stdout + r.stderr
            bad += not ok
            print(f"  {'ok ' if ok else 'BAD'} the clean fixture passes validate")
            r = subprocess.run([str(he_python()), "-c", LOADER, str(good)], capture_output=True, text=True)
            got = json.loads(r.stdout.strip().splitlines()[-1])[str(good)]
            ok = not got.get("error") and not got.get("warnings")
            bad += not ok
            print(f"  {'ok ' if ok else 'BAD'} the clean fixture loads without a warning")
        for check_name, text in DEFECTS.items():
            path = Path(tmp) / f"{check_name}.yaml"
            path.write_text(text, encoding="utf-8")
            if check_name in ("validate", "load"):
                if not shutil.which("he"):
                    print(f"  --  {check_name}: he not installed, not reached")
                    continue
                if check_name == "validate":
                    r = subprocess.run(["he", "template", "validate", str(path)], capture_output=True, text=True)
                    failed = r.returncode != 0 or "HE-T" in r.stdout + r.stderr
                else:
                    r = subprocess.run([str(he_python()), "-c", LOADER, str(path)], capture_output=True, text=True)
                    got = json.loads(r.stdout.strip().splitlines()[-1])[str(path)]
                    failed = bool(got.get("error") or got.get("warnings"))
            else:
                failed = project_checks(text, names)[check_name][0] == "FAIL"
            bad += not failed
            print(f"  {'ok ' if failed else 'BAD'} {check_name} fails on its defect")
    print(f"\n{'all hold' if not bad else f'{bad} FAILED'}")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in ("check", "selftest"):
        print(__doc__)
        return 2
    if argv[0] == "selftest":
        return selftest()
    paths = [Path(a).resolve() for a in argv[1:]] or sorted(DIR.glob("*.yaml"))
    if not paths:
        print(f"no templates in {DIR.relative_to(ROOT)}")
        return 1
    return check(paths)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
