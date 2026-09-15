#!/usr/bin/env python3
"""Run lit-critic over one or more chapters and gate on what it finds.

    python3 scripts/lit_critic_gate.py --chapter 4
    python3 scripts/lit_critic_gate.py --chapter 1-5 --mode quick
    python3 scripts/lit_critic_gate.py --changed --base origin/main
    python3 scripts/lit_critic_gate.py --chapter 4 --report-only

The gate projects the chapters into lit-critic scenes (see
``lit_critic_project.py``), scans them for chapter-scoped canon-lock violations
(see ``lit_critic_locks.py``), runs the seven editorial lenses over them, maps
every finding back to the chapter file and line the author edits, writes a report
under ``Plan/quality/lit-critic/`` and exits:

    0  no blocking findings — the chapter may move on in the gate ladder
    1  at least one blocking finding
    2  the gate could not run (no API key, missing install, projection error)

The canon locks are lexical and free — they run with no API key, so
``--locks-only`` gives a real (if partial) gate result on any machine.

**Blocking policy:** only ``critical`` findings block. ``major`` and ``minor`` are
reported as advisory. The ``horizon`` lens never blocks at any severity — it
surfaces artistic roads not taken, not defects.

A finding is a proposal, not a verdict. lit-critic argues its case and expects
to be argued with; see .claude/skills/lit-critic/SKILL.md for how to push back.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".lit-critic-src"
VENV = SRC / ".venv"
VENV_PYTHON = VENV / "bin/python"
PROJECT_DIR = ROOT / ".lit-critic/project"
USER_CONFIG = ROOT / ".lit-critic/user-config.json"
REPORT_DIR = ROOT / "Plan/quality/lit-critic"

BLOCKING_SEVERITIES = {"critical"}
NON_BLOCKING_LENSES = {"horizon"}
SEVERITY_ORDER = {"critical": 0, "major": 1, "minor": 2}
LOCKS_ONLY_MODE = "locks-only"

EXIT_PASS, EXIT_BLOCKED, EXIT_UNAVAILABLE = 0, 1, 2

sys.path.insert(0, str(ROOT / "scripts"))
import lit_critic_project as proj  # noqa: E402
import lit_critic_locks as locks  # noqa: E402


def reexec_in_venv() -> None:
    """Re-run this script under the lit-critic virtualenv, which owns the deps."""
    if os.environ.get("LIT_CRITIC_GATE_REEXEC") == "1":
        return
    # sys.prefix, not sys.executable: a venv's python is a symlink to the base
    # interpreter, so resolving the path would make every run look like it is
    # already inside the venv.
    if not VENV_PYTHON.exists() or Path(sys.prefix) == VENV:
        return
    os.environ["LIT_CRITIC_GATE_REEXEC"] = "1"
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


def fail_unavailable(message: str, *hint: str) -> None:
    print(f"lit-critic gate UNAVAILABLE: {message}", file=sys.stderr)
    for line in hint:
        print(f"  {line}", file=sys.stderr)
    sys.exit(EXIT_UNAVAILABLE)


def parse_chapters(values: list[str]) -> list[int]:
    """Accept ``4``, ``4,6`` and ``1-5``."""
    chapters: set[int] = set()
    for value in values:
        for part in value.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part:
                low, _, high = part.partition("-")
                try:
                    chapters.update(range(int(low), int(high) + 1))
                except ValueError:
                    raise SystemExit(f"could not read chapter range: {part!r}")
            else:
                try:
                    chapters.add(int(part))
                except ValueError:
                    raise SystemExit(f"could not read chapter number: {part!r}")
    return sorted(chapters)


def changed_chapters(base: str) -> list[int]:
    """Chapter numbers whose files differ from *base* (staged, unstaged or committed)."""
    chapters_rel = str(proj.CHAPTERS.relative_to(ROOT))
    try:
        diff = subprocess.run(
            ["git", "diff", "--name-only", base, "--", chapters_rel],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise SystemExit(f"could not diff against {base}: {exc}")

    numbers: set[int] = set()
    for line in diff.splitlines():
        name = Path(line).name
        if len(name) >= 2 and name[:2].isdigit():
            numbers.add(int(name[:2]))
    return sorted(numbers)


def load_lit_critic():
    """Import the pinned lit-critic and return the handles the gate needs."""
    if not (SRC / "lit-critic-server.py").exists():
        fail_unavailable(
            f"no lit-critic installation at {SRC}",
            "run: scripts/setup_lit_critic.sh",
        )
    sys.path.insert(0, str(SRC))
    USER_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    # Keep the run off the author's global lit-critic config.
    os.environ.setdefault("LIT_CRITIC_USER_CONFIG_PATH", str(USER_CONFIG))
    try:
        from api.analysis_engine import AnalysisEngine
        from orchestrator.persistence.database import get_connection
        from orchestrator.persistence.snapshot_store import SnapshotStore
        from orchestrator.runtime.config import API_KEY_ENV_VARS, resolve_model
        from orchestrator.runtime.model_slots import resolve_models_for_mode
    except ImportError as exc:
        fail_unavailable(
            f"lit-critic import failed: {exc}",
            "run: scripts/setup_lit_critic.sh --force",
        )
    return AnalysisEngine, get_connection, SnapshotStore, API_KEY_ENV_VARS, resolve_model, resolve_models_for_mode


def resolve_keys(mode: str, resolve_model, resolve_models_for_mode, env_vars) -> tuple[str, str | None, dict]:
    """Pick API keys for the models this mode resolves to."""
    try:
        resolved = resolve_models_for_mode(mode, None)
    except ValueError as exc:
        fail_unavailable(str(exc), "valid modes: quick, deep, or a model name (opus, sonnet, haiku)")

    def key_for(model_name: str, role: str) -> str:
        provider = resolve_model(model_name)["provider"]
        env_var = env_vars.get(provider, "")
        key = os.environ.get(env_var, "").strip()
        if not key:
            fail_unavailable(
                f"no API key for the {role} model '{model_name}' (provider: {provider})",
                f"set {env_var} and re-run — the gate never analyses without one,",
                "and never reports a pass it did not earn.",
            )
        return key

    checker_key = key_for(resolved["checker_model"], "checker")
    frontier = resolved.get("frontier_model")
    frontier_key = key_for(frontier, "frontier") if frontier else None
    return checker_key, frontier_key, resolved


def collect_findings(SnapshotStore, get_connection, project_dir: Path,
                     scene_paths: list[Path]) -> tuple[list[dict], int, dict]:
    """Read back the snapshot lit-critic persisted for these scenes.

    Returns the findings, how many of the requested scenes actually have a
    stored analysis (so a caller can tell "analysed, nothing found" apart from
    "never analysed"), and the models that produced them — the report states
    what ran, not what would run now.
    """
    conn = get_connection(project_dir)
    seen: set[int] = set()
    findings: list[dict] = []
    analysed = 0
    run_models: dict = {}
    try:
        for scene_path in scene_paths:
            snapshot = SnapshotStore.get_latest_for_scene(conn, str(scene_path), project_path=project_dir)
            if snapshot is None:
                continue
            analysed += 1
            if not run_models:
                run_models = {
                    "mode": snapshot.depth_mode,
                    "checker_model": snapshot.checker_model,
                    "frontier_model": snapshot.frontier_model,
                }
            for finding in snapshot.findings:
                if finding.id in seen:
                    continue
                seen.add(finding.id)
                findings.append({
                    "number": finding.number,
                    "severity": finding.severity,
                    "lens": finding.lens,
                    "location": finding.location,
                    "line_start": finding.line_start,
                    "line_end": finding.line_end,
                    "scene_file": Path(finding.scene_path).name if finding.scene_path else "",
                    "evidence": finding.evidence,
                    "impact": finding.impact,
                    "options": list(finding.options or []),
                    "flagged_by": list(finding.flagged_by or []),
                    "state": finding.state,
                })
    finally:
        conn.close()
    return findings, analysed, run_models


def is_blocking(finding: dict) -> bool:
    return (
        finding["state"] == "active"
        and finding["severity"] in BLOCKING_SEVERITIES
        and finding["lens"] not in NON_BLOCKING_LENSES
    )


def attach_locations(findings: list[dict], scenes_by_file: dict[str, dict]) -> None:
    """Point every finding at the chapter file and line the author edits."""
    for finding in findings:
        scene = scenes_by_file.get(finding["scene_file"])
        if scene is None:
            finding["chapter_file"] = ""
            finding["chapter_number"] = None
            finding["chapter_line"] = None
            continue
        finding["chapter_file"] = scene["chapter_file"]
        finding["chapter_number"] = scene["chapter_number"]
        finding["chapter_line"] = proj.chapter_line_for(scene, finding["line_start"])
        finding["chapter_line_end"] = proj.chapter_line_for(scene, finding["line_end"])
        finding["scene_heading"] = scene["heading"]


def sort_key(finding: dict) -> tuple:
    return (
        SEVERITY_ORDER.get(finding["severity"], 9),
        finding.get("chapter_number") or 0,
        finding.get("chapter_line") or 0,
    )


def render_report(chapter: int, findings: list[dict], mode: str, resolved: dict) -> str:
    """Render one chapter's report. A locks-only run says so: it is not a full gate."""
    partial = mode == LOCKS_ONLY_MODE
    blocking = [f for f in findings if is_blocking(f)]
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding["severity"]] = counts.get(finding["severity"], 0) + 1
    tally = ", ".join(f"{count} {severity}" for severity, count in
                      sorted(counts.items(), key=lambda kv: SEVERITY_ORDER.get(kv[0], 9))) or "none"

    lines = [
        f"# lit-critic — Kapitel {chapter}",
        "",
        f"- Lauf: {date.today().isoformat()}",
        f"- Modus: `{mode}` (checker `{resolved['checker_model']}`"
        + (f", frontier `{resolved['frontier_model']}`" if resolved.get("frontier_model") else "")
        + ")",
        f"- Findings: {tally}",
        f"- Gate: **{'BLOCKED' if blocking else ('LOCKS PASS' if partial else 'PASS')}**"
        + (f" — {len(blocking)} blockierend" if blocking
           else (" — Canon-Locks sauber; die sieben Linsen sind NICHT gelaufen, "
                 "das ist kein vollständiges Gate-Ergebnis" if partial
                 else " — keine kritischen Findings")),
        "",
        "Findings sind Vorschläge, keine Urteile. Prüfe jedes gegen `Canon/` und den",
        "Kapitelplan, bevor du Prosa änderst; ein Finding, das Kanon falsch liest, wird",
        "zurückgewiesen, nicht eingebaut.",
        "",
    ]

    if not findings:
        lines += ["Keine Findings.", ""]
        return "\n".join(lines)

    for finding in sorted(findings, key=sort_key):
        marker = "⛔" if is_blocking(finding) else ("·" if finding["lens"] in NON_BLOCKING_LENSES else "—")
        where = finding.get("chapter_file", "")
        line = finding.get("chapter_line")
        anchor = f"{where}:{line}" if where and line else finding.get("location", "")
        lines += [
            f"## {marker} [{finding['severity']}/{finding['lens']}] {anchor}",
            "",
            f"**Szene:** {finding.get('scene_heading', finding['scene_file'])}",
            "",
            f"**Evidenz:** {finding['evidence']}",
            "",
            f"**Wirkung:** {finding['impact']}",
        ]
        if finding["options"]:
            lines += ["", "**Optionen:**"] + [f"- {option}" for option in finding["options"]]
        if len(finding["flagged_by"]) > 1:
            lines += ["", f"**Gemeldet von:** {', '.join(finding['flagged_by'])}"]
        lines.append("")

    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    if args.locks_only:
        return run_locks_only(args)

    (AnalysisEngine, get_connection, SnapshotStore,
     env_vars, resolve_model, resolve_models_for_mode) = load_lit_critic()

    if args.report_only:
        resolved = resolve_models_for_mode(args.mode, None)
        checker_key = frontier_key = None
    else:
        checker_key, frontier_key, resolved = resolve_keys(
            args.mode, resolve_model, resolve_models_for_mode, env_vars
        )

    if not args.no_projection:
        manifest = proj.build_project(PROJECT_DIR)
        print(f"projected {manifest['scene_count']} scenes "
              f"({manifest['_written']} written, {len(manifest['_removed'])} stale removed)")
    else:
        manifest = proj.load_manifest(PROJECT_DIR)

    scenes = proj.scenes_for_chapters(manifest, args.chapters)
    if not scenes:
        fail_unavailable(
            f"no projected scenes for chapter(s) {', '.join(map(str, args.chapters))}",
            "run: python3 scripts/lit_critic_project.py --check",
        )
    scenes_by_file = {scene["scene_file"]: scene for scene in scenes}
    scene_paths = [PROJECT_DIR / "text" / scene["scene_file"] for scene in scenes]

    words = sum(scene["words"] for scene in scenes)
    if args.report_only:
        print(f"re-reporting {len(scene_paths)} scenes ({words:,} words) from the last "
              f"stored analysis — no lens run, no API call")
    else:
        print(f"analysing {len(scene_paths)} scenes ({words:,} words) from "
              f"chapter(s) {', '.join(map(str, args.chapters))} in {args.mode} mode…")

        engine = AnalysisEngine()
        try:
            asyncio.run(engine.start_analysis(
                str(scene_paths[0]),
                str(PROJECT_DIR),
                checker_key,
                scene_paths=[str(path) for path in scene_paths],
                depth_mode=args.mode,
                discussion_api_key=frontier_key,
            ))
        except Exception as exc:  # the run is worthless if the engine failed
            fail_unavailable(f"analysis failed: {exc}")

    lock_findings = locks.scan_scenes(scenes, PROJECT_DIR)
    findings, analysed, run_models = collect_findings(
        SnapshotStore, get_connection, PROJECT_DIR, scene_paths
    )
    if not analysed:
        fail_unavailable(
            "no stored analysis for these scenes — a gate cannot pass a run it never made",
            "drop --report-only to run the lenses (needs an API key)"
            if args.report_only else
            "the engine returned without persisting a snapshot; re-run and check its output",
        )
    findings = lock_findings + findings
    attach_locations(findings, scenes_by_file)
    # Report the run that produced these findings, not the configuration that
    # happens to be active now.
    resolved = {**resolved, **{k: v for k, v in run_models.items() if v}}
    mode = run_models.get("mode") or args.mode

    exit_code = write_reports(args.chapters, findings, mode, resolved)

    orphans = [f for f in findings if f.get("chapter_number") not in args.chapters]
    if orphans:
        print(f"  note: {len(orphans)} findings could not be mapped to a requested chapter")

    return exit_code


def run_locks_only(args: argparse.Namespace) -> int:
    """Run only the chapter-scoped canon locks — no API key, no cost."""
    if not args.no_projection:
        proj.build_project(PROJECT_DIR)
    manifest = proj.load_manifest(PROJECT_DIR)
    scenes = proj.scenes_for_chapters(manifest, args.chapters)
    if not scenes:
        fail_unavailable(
            f"no projected scenes for chapter(s) {', '.join(map(str, args.chapters))}",
            "run: python3 scripts/lit_critic_project.py --check",
        )

    findings = locks.scan_scenes(scenes, PROJECT_DIR)
    attach_locations(findings, {scene["scene_file"]: scene for scene in scenes})
    print(f"canon locks over {len(scenes)} scenes in chapter(s) "
          f"{', '.join(map(str, args.chapters))} — lenses skipped")
    return write_reports(args.chapters, findings, LOCKS_ONLY_MODE, {"checker_model": "—"})


def write_reports(chapters: list[int], findings: list[dict], mode: str,
                  resolved: dict) -> int:
    """Write one report per chapter and return the gate's exit code."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    blocking_total = 0
    for chapter in chapters:
        chapter_findings = [f for f in findings if f.get("chapter_number") == chapter]
        blocking = [f for f in chapter_findings if is_blocking(f)]
        blocking_total += len(blocking)

        report = REPORT_DIR / f"kap-{chapter:02d}.md"
        report.write_text(render_report(chapter, chapter_findings, mode, resolved),
                          encoding="utf-8")
        (REPORT_DIR / f"kap-{chapter:02d}.json").write_text(
            json.dumps({
                "chapter": chapter,
                "run_date": date.today().isoformat(),
                "mode": mode,
                "models": resolved,
                "blocking": len(blocking),
                "findings": sorted(chapter_findings, key=sort_key),
            }, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        status = f"BLOCKED ({len(blocking)} critical)" if blocking else "pass"
        print(f"  Kap {chapter:>2}: {len(chapter_findings):>3} findings — {status} "
              f"→ {report.relative_to(ROOT)}")

    if blocking_total:
        print(f"\nlit-critic gate BLOCKED — {blocking_total} critical finding(s). "
              f"Read the report, then fix or reject each one.")
        return EXIT_BLOCKED
    if mode == LOCKS_ONLY_MODE:
        print("\ncanon locks PASS — no lock violations. The seven lenses did NOT run, "
              "so this is not a full gate result.")
        return EXIT_PASS
    print("\nlit-critic gate PASS — no critical findings.")
    return EXIT_PASS


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exit codes: 0 pass · 1 blocking findings · 2 gate could not run",
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--chapter", action="append", metavar="N",
                           help="chapter number, list or range (repeatable): 4 · 4,6 · 1-5")
    selection.add_argument("--changed", action="store_true",
                           help="every chapter whose file differs from --base")
    parser.add_argument("--base", default="origin/main",
                        help="base revision for --changed (default: origin/main)")
    parser.add_argument("--mode", default="deep",
                        help="quick, deep, or a model name (opus, sonnet, haiku); default: deep")
    parser.add_argument("--no-projection", action="store_true",
                        help="analyse the existing projection instead of rebuilding it")
    parser.add_argument("--report-only", action="store_true",
                        help="re-render reports from the last stored analysis "
                             "without running the lenses (no API key needed)")
    parser.add_argument("--locks-only", action="store_true",
                        help="run only the chapter-scoped canon locks "
                             "(lexical, free, no API key needed)")
    args = parser.parse_args(argv)

    args.chapters = changed_chapters(args.base) if args.changed else parse_chapters(args.chapter)
    if not args.chapters:
        print("no changed chapters — nothing to gate.")
        return EXIT_PASS
    return run(args)


if __name__ == "__main__":
    reexec_in_venv()
    sys.exit(main())
