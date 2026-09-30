#!/usr/bin/env python3
"""Check Hyper-Extract templates against Hyper-Extract and against this project.

    python3 scripts/templates.py check [FILE ...]   # default: Plan/hyperextract/*.yaml
    python3 scripts/templates.py selftest           # every check shown to fail on its defect
    python3 scripts/templates.py parse <he parse args>  # `he parse`, with `-t <path>.yaml` loadable

`he parse -t Plan/hyperextract/TermCensus.yaml` fails in the installed CLI with
„Template '…' not found" (Plan/concept/tool-review_2026-09-24/hyperextract.md): the
CLI resolves `-t` with `Template.get`, which knows only the bundled gallery, although
`Template.create`, the save step and `he info`/`he search` all handle a file path.
`parse` runs the same CLI with that one lookup extended — an existing `.yaml` path is
loaded by Hyper-Extract's own `load_template` — and changes nothing else, so every
argument is `he parse`'s own and the installed package is not edited. It also saves
the template beside the data, which `he search` needs to find it again. `he feed` does
not look there — it reads the template's name from the metadata — so appending needs
the path once more: `he feed <ka> <doc> -t Plan/hyperextract/<Name>.yaml`.

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
| resolve      | the file loads by path, as `parse` loads it, and its `name` is the file's |
|              | stem — the Knowledge Abstract records the stem and `he info`/`he search`  |
|              | find the template again by `<name>.yaml` beside it                        |
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

# Template.get extended to a file path; everything else is the installed CLI.
PATCH = r"""
from pathlib import Path
from hyperextract.utils.template_engine.parsers import load_template
from hyperextract.utils.template_engine.template import Template
_get = Template.get
def _get_or_load(path):
    if path.endswith(".yaml") and Path(path).is_file():
        return load_template(path)
    return _get(path)
Template.get = staticmethod(_get_or_load)
"""

# The stock save step copies a custom template beside the data only when the lookup
# above *fails*; `he feed`/`he search` find it again by `<name>.yaml` there, so every
# dump of a path-made abstract copies it.
PARSE = PATCH + r"""
import shutil, sys
_create = Template.create
def _create_and_keep(source, *a, **k):
    ka = _create(source, *a, **k)
    if isinstance(source, str) and source.endswith(".yaml") and Path(source).is_file():
        _dump = ka.dump
        def dump(folder, *da, **dk):
            out = _dump(folder, *da, **dk)
            shutil.copy(source, Path(folder) / Path(source).name)
            return out
        ka.dump = dump
    return ka
Template.create = staticmethod(_create_and_keep)
from hyperextract.cli import app
sys.argv = ["he", "parse", *sys.argv[1:]]
sys.exit(app())
"""

RESOLVE = PATCH + r"""
import json, sys
out = {}
for path in sys.argv[1:]:
    try:
        cfg = Template.get(path)
        out[path] = {"name": cfg.name} if cfg is not None else {"error": "not found"}
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


def resolve_status(path: Path, got: dict | None, stderr: str = "") -> tuple[str, str]:
    if got is None:
        return ("not reached", (stderr.strip().splitlines() or ["no output"])[-1][:200])
    if "error" in got:
        return ("FAIL", got["error"])
    if got["name"] != path.stem:
        return ("FAIL", f"name {got['name']!r} is not the file's stem {path.stem!r}")
    return ("ok", "")


def resolve(paths: list[Path]) -> dict:
    r = subprocess.run([str(he_python()), "-c", RESOLVE, *map(str, paths)], capture_output=True, text=True)
    return json.loads(r.stdout.strip().splitlines()[-1])


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
        r = subprocess.run([str(py), "-c", RESOLVE, *map(str, paths)], capture_output=True, text=True)
        try:
            resolved = json.loads(r.stdout.strip().splitlines()[-1])
        except (json.JSONDecodeError, IndexError):
            resolved = {}
        for p in paths:
            results[p]["resolve"] = resolve_status(p, resolved.get(str(p)), r.stderr)
    else:
        for p in paths:
            results[p]["load"] = ("not reached", "no hyperextract interpreter beside `he`")
            results[p]["resolve"] = ("not reached", "no hyperextract interpreter beside `he`")
    for p in paths:
        results[p].update(project_checks(p.read_text(encoding="utf-8"), names))
    order = ["validate", "load", "resolve", "no-line", "no-llm-merge", "merge-set", "provisional", "procedural"]
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
    "resolve": GOOD,  # written as resolve.yaml: its name, Fixture, is not the file's stem
}


def selftest() -> int:
    names, _ = known_names()
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        good = Path(tmp) / "Fixture.yaml"
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
            ok = resolve_status(good, resolve([good])[str(good)])[0] == "ok"
            bad += not ok
            print(f"  {'ok ' if ok else 'BAD'} the clean fixture resolves by path, as `parse` loads it")
            r = subprocess.run([str(he_python()), "-c",
                                "import sys; from hyperextract.utils.template_engine.template import Template;"
                                "print(Template.get(sys.argv[1]) is None)", str(good)],
                               capture_output=True, text=True)
            ok = r.stdout.strip().endswith("True")
            bad += not ok
            print(f"  {'ok ' if ok else 'BAD'} the unpatched CLI lookup still misses a path"
                  f" (if not, `parse` is no longer needed)")
        for check_name, text in DEFECTS.items():
            path = Path(tmp) / f"{check_name}.yaml"
            path.write_text(text, encoding="utf-8")
            if check_name in ("validate", "load", "resolve"):
                if not shutil.which("he"):
                    print(f"  --  {check_name}: he not installed, not reached")
                    continue
                if check_name == "validate":
                    r = subprocess.run(["he", "template", "validate", str(path)], capture_output=True, text=True)
                    failed = r.returncode != 0 or "HE-T" in r.stdout + r.stderr
                elif check_name == "resolve":
                    failed = resolve_status(path, resolve([path])[str(path)])[0] == "FAIL"
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
    if not argv or argv[0] not in ("check", "selftest", "parse"):
        print(__doc__)
        return 2
    if argv[0] == "parse":
        py = he_python()
        if py is None:
            print("no hyperextract interpreter beside `he` — scripts/install.sh hyperextract", file=sys.stderr)
            return 2
        return subprocess.run([str(py), "-c", PARSE, *argv[1:]]).returncode
    if argv[0] == "selftest":
        return selftest()
    paths = [Path(a).resolve() for a in argv[1:]] or sorted(DIR.glob("*.yaml"))
    if not paths:
        print(f"no templates in {DIR.relative_to(ROOT)}")
        return 1
    return check(paths)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
