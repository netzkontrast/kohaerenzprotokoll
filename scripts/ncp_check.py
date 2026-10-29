"""The emitted NCP document against the protocol's own schemas, plus what those schemas do not check.

Taken from `netzkontrast/narrative-context-protocol` (Core 3.0.0-rc.1, Dramatica profile 1.0.0-rc.1): the two schemas
are byte-pinned copies in `Plan/storyform/ncp/schema/`, from commit afa8d86b6aa707f0fd864230edc0a9a6c42b0db4, and
`PINS` below refuses a copy whose bytes moved. The protocol's own rule is kept: preserve, do not normalise — this
reads the document `storyform.py` writes and never rewrites it.

    python3 scripts/ncp_check.py            schema validation (needs the `jsonschema` package) and the cross-checks
    python3 scripts/ncp_check.py selftest   the cross-checks, standard library only

The cross-checks are what Core accepts and should not (measured against the pinned schemas on 2026-10-28):
- a payload namespace with no `profiles[]` declaration;
- a declaration whose `profile_version` differs from its payload's;
- a declared profile with no payload.

Schema validation is reported `not run` when `jsonschema` is absent: that is not a pass. A pass prints "schema
validation passed", never "a valid storyform": a schema checks shape, not story.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NCP = ROOT / "Plan" / "storyform" / "ncp" / "kohaerenz-protokoll.ncp.json"
SCHEMA = ROOT / "Plan" / "storyform" / "ncp" / "schema"
PINS = {"ncp-core-schema.json": "fed53f362d91767687773085ff6ec34b97219eab94bbe6f4bda193d9848391cf",
        "profile-schema.json": "905c189549d5f8648452f607cb513d1e295751e7a3486c6369494e431492da31"}
NCP_VERSION = "3.0.0-rc.1"


def pins() -> list[str]:
    out = []
    for name, sha in PINS.items():
        p = SCHEMA / name
        if not p.exists():
            out.append(f"schema copy {name} missing")
        elif hashlib.sha256(p.read_bytes()).hexdigest() != sha:
            out.append(f"schema copy {name} changed since it was pinned — re-pin only from the protocol's repository")
    return out


def cross_check(doc: dict) -> list[str]:
    out = []
    if doc.get("ncp_version") != NCP_VERSION:
        out.append(f"ncp_version {doc.get('ncp_version')!r}, expected {NCP_VERSION!r}")
    decl = {p.get("namespace"): p for p in doc.get("profiles") or []}
    payloads = doc.get("payloads") or {}
    for ns, pay in payloads.items():
        if ns not in decl:
            out.append(f"payload {ns!r} has no profiles[] declaration")
        elif isinstance(pay, dict) and pay.get("profile_version") != decl[ns].get("profile_version"):
            out.append(f"payload {ns!r} profile_version {pay.get('profile_version')!r} ≠ declared {decl[ns].get('profile_version')!r}")
    for ns in decl:
        if ns not in payloads:
            out.append(f"declared profile {ns!r} has no payload")
    return out


def schema_check(doc: dict) -> tuple[str, list[str]]:
    """('passed' | 'failed' | 'not run', messages)."""
    try:
        from jsonschema import Draft7Validator, Draft202012Validator, FormatChecker
    except ImportError:
        return "not run", ["jsonschema absent — pip install jsonschema in a venv; schema validation was not run"]
    core = json.loads((SCHEMA / "ncp-core-schema.json").read_text(encoding="utf-8"))
    prof = json.loads((SCHEMA / "profile-schema.json").read_text(encoding="utf-8"))
    msgs = [f"core {'/'.join(map(str, e.absolute_path)) or '/'}: {e.message}"
            for e in Draft202012Validator(core, format_checker=FormatChecker()).iter_errors(doc)]
    for ns, pay in (doc.get("payloads") or {}).items():
        if ns == "dramatica:":
            msgs += [f"dramatica {'/'.join(map(str, e.absolute_path)) or '/'}: {e.message}"
                     for e in Draft7Validator(prof, format_checker=FormatChecker()).iter_errors(pay)]
    return ("failed" if msgs else "passed"), msgs


def selftest() -> int:
    good = {"ncp_version": NCP_VERSION, "profiles": [{"namespace": "dramatica:", "profile_version": "1.0.0-rc.1"}],
            "payloads": {"dramatica:": {"profile_version": "1.0.0-rc.1"}}}
    results = [("a matching declaration and payload pass the cross-checks", cross_check(good) == [])]
    bad = json.loads(json.dumps(good))
    bad["profiles"] = []
    results.append(("a payload without a declaration is named (Core accepts it)", any("no profiles[]" in m for m in cross_check(bad))))
    bad = json.loads(json.dumps(good))
    bad["payloads"]["dramatica:"]["profile_version"] = "9.9.9"
    results.append(("a profile_version mismatch is named (Core accepts it)", any("≠ declared" in m for m in cross_check(bad))))
    bad = json.loads(json.dumps(good))
    bad["payloads"] = {}
    results.append(("a declared profile without payload is named", any("has no payload" in m for m in cross_check(bad))))
    results.append(("a wrong ncp_version is named", any("ncp_version" in m for m in cross_check({**good, "ncp_version": "1.3.0"}))))
    results.append(("the pinned schema copies are the pinned bytes", pins() == []))
    for name, ok in results:
        print(f"{'held' if ok else 'FAILED':7} {name}")
    held = sum(ok for _, ok in results)
    print(f"{held} of {len(results)} held")
    return 0 if held == len(results) else 1


def main(argv: list[str]) -> int:
    if argv and argv[0] == "selftest":
        return selftest()
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    doc = json.loads(NCP.read_text(encoding="utf-8"))
    problems = pins() + cross_check(doc)
    for p in problems:
        print(f"ERROR {p}")
    status, msgs = schema_check(doc)
    for m in msgs:
        print(("ERROR " if status == "failed" else "      ") + m)
    print(f"schema validation {status}; {len(problems)} cross-check problem(s) — a schema checks shape, not story")
    if status == "not run":
        return 3
    return 1 if problems or status == "failed" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
