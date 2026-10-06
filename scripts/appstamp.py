"""Was the project app rebuilt and checked for this commit?

`ui.py --check` writes `Plan/derived/ui/stamp.json` when what it built has no
defect: the commit's tree id, the time, and the check's verdict. `verify` says
whether the stamp names HEAD's tree — the skill `app-refresh` is what makes it
match. A pre-PR hook ran `verify` and refused a pull request on a mismatch until
the author removed it on 2026-10-06; nothing refuses one now.

The fingerprint is the tree of HEAD, not a list of the files the app reads:
`ui.py` reads NOW.md, the wiki, the manuscript, the decisions, the manifest, the
reconciliation records and every number `state.py` measures across the repository,
and a hand-kept list of inputs would be one more thing to go stale. A commit that
touches none of them costs one rebuild; a stale app never ships unnoticed.

    python3 scripts/appstamp.py verify            # exit 0 when the stamp names HEAD's tree, 2 when not
    python3 scripts/appstamp.py show              # the stamp and HEAD's tree
    python3 scripts/appstamp.py waive "<reason>"  # accept this tree without a build — the reason is kept
                                                  # and belongs in the pull request's description
    python3 scripts/appstamp.py selftest

Uncommitted changes are not in a pull request, so they do not count; `verify`
names them so the session can commit first.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = ROOT / "Plan" / "derived" / "ui" / "stamp.json"


def tree(root: Path = ROOT) -> str:
    proc = subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=root, capture_output=True, text=True)
    return proc.stdout.strip() if proc.returncode == 0 else ""


def dirty(root: Path = ROOT) -> list[str]:
    proc = subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=root, capture_output=True, text=True)
    return [ln[3:] for ln in proc.stdout.splitlines() if ln.strip()]


def write(verdict: str, defects: int = 0, waived: str = "", path: Path = STAMP, root: Path = ROOT) -> dict:
    stamp = {"tree": tree(root), "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "verdict": verdict, "defects": defects, "dirty": dirty(root)}
    if waived:
        stamp["waived"] = waived
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stamp, indent=1) + "\n", encoding="utf-8")
    return stamp


def verify(path: Path = STAMP, root: Path = ROOT) -> tuple[bool, str]:
    head = tree(root)
    if not head:
        return True, "appstamp: not a git checkout — nothing to compare (a Vercel build has no .git)"
    if not path.exists():
        return False, "appstamp: the app was never built and checked in this container"
    stamp = json.loads(path.read_text(encoding="utf-8"))
    if stamp.get("tree") != head:
        return False, (f"appstamp: the app was built for tree {stamp.get('tree', '?')[:10]}, HEAD is {head[:10]} — "
                       "something was committed after the build")
    if stamp.get("verdict") != "clean" and not stamp.get("waived"):
        return False, f"appstamp: the build for this tree had {stamp.get('defects', '?')} defect(s)"
    note = f" (waived: {stamp['waived']})" if stamp.get("waived") else ""
    left = dirty(root)
    tail = f"; {len(left)} uncommitted change(s) are not in it: {', '.join(left[:5])}" if left else ""
    return True, f"appstamp: the app was built and checked for HEAD's tree {head[:10]} at {stamp.get('at')}{note}{tail}"


def selftest() -> list[str]:
    fail = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        git = lambda *a: subprocess.run(["git", *a], cwd=root, capture_output=True, text=True, check=True)  # noqa: E731
        git("init", "-q")
        git("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", "one")
        stamp = root / "stamp.json"
        ok, why = verify(stamp, root)
        if ok or "never built" not in why:
            fail.append(f"no stamp: want refused as never built, got {ok} {why!r}")
        write("defects", 3, path=stamp, root=root)
        ok, why = verify(stamp, root)
        if ok or "3 defect" not in why:
            fail.append(f"a build with defects: want refused, got {ok} {why!r}")
        write("clean", path=stamp, root=root)
        ok, why = verify(stamp, root)
        if not ok:
            fail.append(f"a clean build of this tree: want accepted, got {why!r}")
        (root / "f.txt").write_text("x")
        git("add", "f.txt")
        git("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "two")
        ok, why = verify(stamp, root)
        if ok or "committed after the build" not in why:
            fail.append(f"a commit after the build: want refused, got {ok} {why!r}")
        write("not built", waived="node missing", path=stamp, root=root)
        ok, why = verify(stamp, root)
        if not ok or "waived: node missing" not in why:
            fail.append(f"a waiver: want accepted and named, got {ok} {why!r}")
        (root / "f.txt").write_text("y")
        ok, why = verify(stamp, root)
        if "f.txt" not in why:
            fail.append(f"an uncommitted change: want named, got {why!r}")
    return fail


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "show"
    if cmd == "selftest":
        fail = selftest()
        for f in fail:
            print(f"  FAILED  {f}")
        print(f"appstamp: {'every case held' if not fail else str(len(fail)) + ' case(s) failed'} "
              "(never built, defects, clean, committed after, waiver, uncommitted)")
        return 1 if fail else 0
    if cmd == "verify":
        ok, why = verify()
        print(why, file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 2
    if cmd == "waive":
        reason = " ".join(argv[1:]).strip()
        if not reason:
            print("appstamp: a waiver needs its reason", file=sys.stderr)
            return 1
        print(json.dumps(write("not built", waived=reason), indent=1))
        return 0
    if cmd == "show":
        print(STAMP.read_text(encoding="utf-8") if STAMP.exists() else "no stamp")
        print(f"HEAD tree: {tree()}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
