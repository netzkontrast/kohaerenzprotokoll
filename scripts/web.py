"""The project app as a static website, for Vercel.

`ui.py` derives the app into the files of a claude.ai Design canvas. A canvas
supplies each frame's `./support.js`; a website has to supply it itself. This
script runs `ui.py`, then copies the frames beside the vendored runtime
`scripts/web/support.js` into `Plan/derived/web/` — derived, git-ignored, and
what Vercel serves (`vercel.json`). It changes nothing in the app: the bytes of
every `.dc.html` are the bytes the canvas gets. Beside them it serves what `ui.py`
writes for agents: `llms.txt` at the root and `agents/` (`sessions.json`,
`index.json`, `state.json`, `data.json`) — the same snapshot, read by a program.

    python3 scripts/web.py               # ui.py --no-checks, then assemble Plan/derived/web/
    python3 scripts/web.py --no-build    # assemble from the Plan/derived/ui/ already there
    python3 scripts/web.py --check       # assemble, then fail if a frame or the runtime is missing

The runtime is the Design type's `artifact-type/dc-runtime.js` (it loads React
18.3.1 from jsdelivr with integrity hashes), copied from the canvas
https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL on 2026-10-02, type release
1790869903-0489, sha256 454cb23f…. It is pinned, not fetched: a new type release
reaches the website only when someone copies it over again and says so in the
commit. `scripts/web/README.md` has the provenance.

It writes nothing outside `Plan/derived/web/`.
"""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "Plan" / "derived" / "ui"
CANVAS = UI / "canvas" / "project"
RUNTIME = ROOT / "scripts" / "web" / "support.js"
RUNTIME_SHA256 = "454cb23fe5f5b1c4c7cd178795ec6cf3c32047eae4434e975a6104c53183fbd6"
OUT = ROOT / "Plan" / "derived" / "web"


def assemble(out: Path = OUT) -> list[str]:
    """Copy the frames and the runtime into `out`; return the files written."""
    if hashlib.sha256(RUNTIME.read_bytes()).hexdigest() != RUNTIME_SHA256:
        raise SystemExit(f"web: {RUNTIME.relative_to(ROOT)} is not the pinned runtime — copy it again and update RUNTIME_SHA256")
    frames = sorted(CANVAS.glob("*.dc.html"))
    if not any(f.name == "Main.dc.html" for f in frames):
        raise SystemExit(f"web: no Main.dc.html in {CANVAS.relative_to(ROOT)} — run python3 scripts/ui.py first")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for f in frames:
        shutil.copyfile(f, out / f.name)
    shutil.copyfile(RUNTIME, out / "support.js")
    # what an agent reads instead of the screen (`ui.py` writes it beside the canvas)
    if (UI / "llms.txt").exists():
        shutil.copyfile(UI / "llms.txt", out / "llms.txt")
    if (UI / "agents").is_dir():
        shutil.copytree(UI / "agents", out / "agents")
    return sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file())


def main(argv: list[str]) -> int:
    if "--no-build" not in argv:
        proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "ui.py"), "--no-checks"], cwd=ROOT)
        if proc.returncode:
            return proc.returncode
    written = assemble()
    print(f"web: wrote {OUT.relative_to(ROOT)}/ — {', '.join(written)}")
    if "--check" in argv:
        missing = [n for n in ("Main.dc.html", "support.js", "llms.txt", "agents/sessions.json", "agents/index.json")
                   if n not in written]
        for n in missing:
            print(f"  DEFECT  {n} missing")
        return 1 if missing else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
