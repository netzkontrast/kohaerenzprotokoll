"""The AEGIS pilot, offline: perception filter, typed proposals, one validator, one writer, replay.

`Plan/briefings/aegis-agent-pilot.md` asks for the smallest loop two manual cases
need, and nothing more: a figure sees only the facts the scenario makes visible
to it, proposes a typed action, deterministic code validates it, one writer
commits one event, and a replay rebuilds the state from committed events without
a model. The two cases are `Plan/fixtures/aegis/case-01-sweep.json` and
`case-02-rejected.json`; their README says what each assumes.

What this file is **not**: a model adapter, a database, an MCP server, a canon
editor. The "model" here is a frozen list of proposals in the scenario file
(`responses`). A later live adapter replaces that list and nothing else; the
validator never asks a model whether a decidable rule holds.

    python3 scripts/aegis.py validate Plan/fixtures/aegis/case-01-sweep.json
    python3 scripts/aegis.py pack     Plan/fixtures/aegis/case-01-sweep.json aegis
    python3 scripts/aegis.py run      Plan/fixtures/aegis/case-01-sweep.json --out Plan/runs/aegis-pilot-<date>/case-01
    python3 scripts/aegis.py replay   Plan/runs/aegis-pilot-<date>/case-01
    python3 scripts/aegis.py status   Plan/runs/aegis-pilot-<date>/case-01
    python3 scripts/aegis.py fork     Plan/runs/aegis-pilot-<date>/case-01 <new-dir> [--upto N]
    python3 scripts/aegis.py selftest

The three rules the code keeps, each with a selftest that can fail:

- **Perception is filtered in code, before anything else.** A pack holds a
  figure's visible facts, delivered claims, allowed actions and the state keys
  its `sees` grants; `author_only` never reaches a pack or a tool response, and
  what was left out is named by count, never by content.
- **Validation is decidable and ordered**: actor → endpoint → registered action
  → allowed for actor → observations present in the actor's pack → state
  version → reserve. The first failing rule names the rejection; a rejected or
  stale proposal changes nothing and goes to `rejections.jsonl`, apart from the
  events.
- **One writer, idempotent, replayable.** An accepted proposal becomes one event
  that records the effects it applied; a repeated action id is a no-op; the
  state is never stored as truth but derived from the events, so a restart and a
  replay reach the same state, and a fork copies events without touching its
  parent.

Facts, received claims and private beliefs stay distinguishable: `facts` are
what a figure observed, `claims` what it was told, `beliefs` what it holds —
and only facts count as observations. Beliefs are never validated by this code;
whether one is mistaken is the author's reading, recorded as `status`.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "Plan" / "fixtures" / "aegis"
SCHEMA_VERSION = 2   # 2: facts name their subject, target-dependent actions name their target kind (review of PR #198)
PROBE = "PROBE-AUTHOR-ONLY"

REJECTIONS = (
    "malformed_proposal", "unknown_actor", "past_endpoint", "chapter_jump", "action_not_registered",
    "action_not_allowed_for_actor", "invalid_target", "missing_observation", "stale_version", "insufficient_reserve",
)
TARGET_KINDS = ("anomaly",)   # what an action's `target` may name; the validator checks it exists in the state

# ---------------------------------------------------------------- scenario files

_TOP = {
    "scenario": str, "schema_version": int, "status": str, "title": str, "inputs": dict,
    "assumptions": list, "chapter": int, "world": str, "figures": dict, "actions": dict,
    "facts": list, "claims": list, "beliefs": list, "author_only": list, "state": dict,
    "responses": list, "expected": dict,
}


def check_shape(sc: dict) -> list[str]:
    """Every departure from the fixture shape, named by field. Empty = accepted."""
    bad = []
    for key, typ in _TOP.items():
        if key not in sc:
            bad.append(f"missing top-level field {key!r}")
        elif not isinstance(sc[key], typ):
            bad.append(f"field {key!r} must be {typ.__name__}")
    if bad:
        return bad
    if sc["schema_version"] != SCHEMA_VERSION:
        bad.append(f"schema_version {sc['schema_version']} is not {SCHEMA_VERSION}")
    if sc["status"] != "proposal":
        bad.append("status must be 'proposal': a scenario is never canon")
    for name, fig in sc["figures"].items():
        for k in ("role", "profile", "endpoint_chapter", "allowed_actions", "sees"):
            if k not in fig:
                bad.append(f"figures.{name} lacks {k!r}")
        for a in fig.get("allowed_actions", []):
            if a not in sc["actions"]:
                bad.append(f"figures.{name} allows unregistered action {a!r}")
    for name, act in sc["actions"].items():
        for k in ("cost", "requires", "effects"):
            if k not in act:
                bad.append(f"actions.{name} lacks {k!r}")
        if act.get("cost", 0) < 0:
            bad.append(f"actions.{name} has a negative cost")
        if act.get("target") is not None and act["target"] not in TARGET_KINDS:
            bad.append(f"actions.{name} names target kind {act['target']!r}, none of {TARGET_KINDS}")
        if "close_anomaly" in act.get("effects", []) and act.get("target") != "anomaly":
            bad.append(f"actions.{name} closes an anomaly but does not declare target 'anomaly'")
    for f in sc["facts"]:
        if not isinstance(f.get("subject"), str) or not f.get("subject"):
            bad.append(f"fact {f.get('id')!r} has no subject: an observation says what it is about")
        if not f.get("visible_to"):
            bad.append(f"fact {f.get('id')!r} has no visible_to: every fact names who sees it")
        for who in f.get("visible_to", []):
            if who not in sc["figures"]:
                bad.append(f"fact {f.get('id')!r} is visible to unknown figure {who!r}")
    fact_ids = {f["id"] for f in sc["facts"]}
    claim_ids = {c["id"] for c in sc["claims"]}
    for b in sc["beliefs"]:
        for k in ("id", "holder", "source", "status", "text"):
            if k not in b:
                bad.append(f"belief {b.get('id')!r} lacks {k!r}")
        if b.get("holder") not in sc["figures"]:
            bad.append(f"belief {b.get('id')!r} has unknown holder")
        if b.get("source") not in fact_ids | claim_ids:
            bad.append(f"belief {b.get('id')!r} cites no fact or claim as its source")
        if b.get("text") in {f["text"] for f in sc["facts"]}:
            bad.append(f"belief {b.get('id')!r} restates a fact verbatim: beliefs and facts stay apart")
    for a in sc["author_only"]:
        if PROBE not in a.get("text", ""):
            bad.append(f"author_only {a.get('id')!r} does not carry the probe marker {PROBE!r}")
    st = sc["state"]
    for k in ("version", "chapter", "reserve", "memories", "anomalies"):
        if k not in st:
            bad.append(f"state lacks {k!r}")
    if st.get("reserve", 0) < 0:
        bad.append("state.reserve is negative")
    seen = set()
    for r in sc["responses"]:
        for k in ("action_id", "actor", "type", "observations", "expected_version"):
            if k not in r:
                bad.append(f"response {r.get('action_id')!r} lacks {k!r}")
        seen.add(r.get("action_id"))
    for k in ("accepted", "rejected", "duplicates", "state_after"):
        if k not in sc["expected"]:
            bad.append(f"expected lacks {k!r}")
    return bad


def load_scenario(path: str | Path) -> dict:
    sc = json.loads(Path(path).read_text(encoding="utf-8"))
    bad = check_shape(sc)
    if bad:
        raise ValueError(f"{path}: " + "; ".join(bad))
    return sc


# ---------------------------------------------------------------- state and packs

def initial_state(sc: dict) -> dict:
    st = copy.deepcopy(sc["state"])
    st["facts"] = copy.deepcopy(sc["facts"])          # consequence facts are appended here
    st["claims"] = copy.deepcopy(sc["claims"])
    return st


def _memory(st: dict, mid: str) -> dict:
    for m in st["memories"]:
        if m["id"] == mid:
            return m
    raise KeyError(mid)


def _anomaly(st: dict, aid: str) -> dict:
    for a in st["anomalies"]:
        if a["id"] == aid:
            return a
    raise KeyError(aid)


def apply_event(st: dict, ev: dict) -> dict:
    """Apply one committed event to a derived state. Pure: the event says what it did."""
    st = copy.deepcopy(st)
    st["reserve"] -= ev["cost"]
    if st["reserve"] < 0:                               # the validator forbids it; replay refuses it
        raise ValueError(f"event {ev['action_id']} drives the reserve below zero")
    for eff in ev["effects_applied"]:
        kind = eff["effect"]
        if kind == "close_anomaly":
            _anomaly(st, eff["anomaly"])["status"] = "closed"
        elif kind == "mask_memory":
            _memory(st, eff["memory"])["masked"] = True
        elif kind == "consequence_fact":
            st["facts"].append({"id": eff["fact_id"], "kind": "consequence", "subject": eff.get("subject", ""),
                                "visible_to": list(eff["visible_to"]), "text": eff["text"],
                                "from_event": ev["action_id"]})
        elif kind == "deliver_claim":
            st["claims"].append({"id": eff["claim_id"], "from": ev["actor"], "to": eff["to"],
                                 "text": eff["text"], "from_event": ev["action_id"]})
        else:
            raise ValueError(f"event {ev['action_id']} carries unknown effect {kind!r}")
    if "chapter" in ev:
        st["chapter"] = ev["chapter"]
    st["version"] += 1
    return st


def derive_state(sc: dict, events: list[dict]) -> dict:
    st = initial_state(sc)
    for ev in events:
        st = apply_event(st, ev)
    return st


def pack(sc: dict, st: dict, figure: str) -> dict:
    """What one figure may see. Author-only content never enters; omissions are counted."""
    if figure not in sc["figures"]:
        raise KeyError(f"unknown figure {figure!r}")
    fig = sc["figures"][figure]
    facts = [f for f in st["facts"] if figure in f["visible_to"]]
    claims = [c for c in st["claims"] if c["to"] == figure]
    beliefs = [b for b in sc["beliefs"] if b["holder"] == figure]
    view = {"version": st["version"], "chapter": st["chapter"]}
    masked_hidden = 0
    for key in ("reserve", "memories", "anomalies"):
        if fig["sees"].get(key):
            view[key] = copy.deepcopy(st[key])
    if "memories" in view:
        # a masked memory is lost to the figure: its id and the fact of the loss stay, its text does not
        # (the authoritative state and the replay keep it; review of PR #198, P2)
        masked_hidden = sum(1 for m in view["memories"] if m.get("masked"))
        view["memories"] = [{"id": m["id"], "masked": True} if m.get("masked") else m for m in view["memories"]]
    hidden_facts = len(st["facts"]) - len(facts)
    out = {
        "figure": figure, "role": fig["role"], "profile": fig["profile"],
        "active": st["chapter"] <= fig["endpoint_chapter"],
        "allowed_actions": list(fig["allowed_actions"]),
        "facts": facts, "claims": claims, "beliefs": beliefs, "state": view,
        "omitted": {"facts": hidden_facts, "claims": len(st["claims"]) - len(claims),
                    "author_only": len(sc["author_only"]), "masked_memories": masked_hidden,
                    "state_keys": [k for k in ("reserve", "memories", "anomalies") if not fig["sees"].get(k)]},
    }
    if PROBE in json.dumps(out, ensure_ascii=False):
        raise AssertionError("author-only content reached a pack")
    return out


# ---------------------------------------------------------------- validation

def validate(sc: dict, st: dict, proposal: dict) -> tuple[str | None, str]:
    """The first failing rule, in fixed order, or (None, 'ok'). Decidable; no model.

    Order: shape → actor → endpoint (persisted chapter, then the proposal's) → chapter step → registered → allowed
    → target → observation about that target → version → reserve. Every refusal is a recorded rejection; nothing
    here raises on a malformed proposal (review of PR #198, P2)."""
    if not isinstance(proposal, dict):
        return "malformed_proposal", "a proposal is a JSON object"
    for k, typ in (("action_id", str), ("actor", str), ("type", str), ("expected_version", int)):
        if not isinstance(proposal.get(k), typ) or isinstance(proposal.get(k), bool):
            return "malformed_proposal", f"{k!r} missing or not {typ.__name__}"
    if not isinstance(proposal.get("observations", []), list) or not all(isinstance(o, str) for o in proposal.get("observations", [])):
        return "malformed_proposal", "'observations' must be a list of fact ids"
    if "chapter" in proposal and (not isinstance(proposal["chapter"], int) or isinstance(proposal["chapter"], bool)):
        return "malformed_proposal", "'chapter' must be an integer"
    actor = proposal["actor"]
    fig = sc["figures"].get(actor)
    if fig is None:
        return "unknown_actor", f"no figure {actor!r}"
    # the persisted chapter decides whether the actor still acts; a proposal cannot backdate itself into activity
    if st["chapter"] > fig["endpoint_chapter"]:
        return "past_endpoint", f"{actor} ({fig['profile']}) ended at chapter {fig['endpoint_chapter']}; the world is at {st['chapter']}"
    chapter = proposal.get("chapter", st["chapter"])
    if chapter > fig["endpoint_chapter"]:
        return "past_endpoint", f"{actor} ({fig['profile']}) cannot act in chapter {chapter}: endpoint {fig['endpoint_chapter']}"
    if chapter not in (st["chapter"], st["chapter"] + 1):
        return "chapter_jump", f"a proposal stays in chapter {st['chapter']} or moves to the next; it asked for {chapter}"
    act = sc["actions"].get(proposal["type"])
    if act is None:
        return "action_not_registered", f"{proposal['type']!r} is not a registered action"
    if proposal["type"] not in fig["allowed_actions"]:
        return "action_not_allowed_for_actor", f"{actor} may not {proposal['type']}"
    target = proposal.get("target")
    if act.get("target") == "anomaly":
        if not isinstance(target, str) or not target:
            return "invalid_target", f"{proposal['type']} needs a target anomaly"
        if not any(a["id"] == target for a in st["anomalies"]):
            return "invalid_target", f"{target!r} is no anomaly in the state"
    if "observation" in act["requires"]:
        visible = {f["id"]: f for f in pack(sc, st, actor)["facts"]}
        cited = list(proposal.get("observations", []))
        missing = [o for o in cited if o not in visible]
        if not cited or missing:
            return "missing_observation", (f"{proposal['type']} requires an observation in {actor}'s pack; "
                                           f"cited {cited}, not visible {missing}")
        # a visible fact about something else authorises nothing: one cited observation must be about the target
        if act.get("target") == "anomaly" and not any(visible[o].get("subject") == target for o in cited):
            return "missing_observation", (f"{proposal['type']} on {target} requires an observation of {target}; "
                                           f"cited {cited} are about {sorted({visible[o].get('subject') for o in cited})}")
    if proposal["expected_version"] != st["version"]:
        return "stale_version", f"expected version {proposal['expected_version']}, state is {st['version']}"
    if act["cost"] > st["reserve"]:
        return "insufficient_reserve", f"cost {act['cost']} exceeds reserve {st['reserve']}"
    return None, "ok"


def build_event(sc: dict, st: dict, proposal: dict) -> dict:
    """The event an accepted proposal becomes: it records the effects it applies."""
    act = sc["actions"][proposal["type"]]
    effects = []
    for eff in act["effects"]:
        if eff == "close_anomaly":
            effects.append({"effect": "close_anomaly", "anomaly": proposal["target"]})
        elif eff == "mask_memory":
            unmasked = [m for m in st["memories"] if not m["masked"]]
            if unmasked:
                effects.append({"effect": "mask_memory", "memory": unmasked[0]["id"]})
        elif eff == "deliver_claim":
            effects.append({"effect": "deliver_claim", "to": act["claim_to"],
                            "claim_id": f"claim-{proposal['action_id']}", "text": proposal.get("reason", "")})
        else:
            raise ValueError(f"action {proposal['type']} declares unknown effect {eff!r}")
    if act.get("consequence"):
        c = act["consequence"]
        effects.append({"effect": "consequence_fact", "fact_id": f"F1-consequence-{proposal['action_id']}",
                        "subject": str(proposal.get("target", "")), "visible_to": list(c["visible_to"]),
                        "text": c["text"].replace("{target}", str(proposal.get("target", "")))})
    ev = {"action_id": proposal["action_id"], "actor": proposal["actor"], "type": proposal["type"],
          "target": proposal.get("target"), "observations": list(proposal.get("observations", [])),
          "expected_version": proposal["expected_version"], "cost": act["cost"],
          "effects_applied": effects}
    if "chapter" in proposal:
        ev["chapter"] = proposal["chapter"]
    return ev


# ---------------------------------------------------------------- the run directory (one writer)

def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git_revision() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, timeout=5)
        return out.stdout.strip() or "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _append_atomic(path: Path, row: dict) -> None:
    """Append one row by rewriting the file through a temporary and replacing it: a crash leaves
    either the old file or the new one, never a half-written line."""
    rows = _read_jsonl(path)
    rows.append(row)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    os.replace(tmp, path)


class Run:
    """A run directory: the pinned scenario, the events, the rejections, the logs. State is derived."""

    def __init__(self, directory: str | Path):
        self.dir = Path(directory)
        self.scenario_path = self.dir / "scenario.json"
        self.events_path = self.dir / "events.jsonl"
        self.rejections_path = self.dir / "rejections.jsonl"
        self.logs_path = self.dir / "logs.jsonl"
        self.meta_path = self.dir / "meta.json"
        self.final_path = self.dir / "final.json"

    @classmethod
    def create(cls, scenario_path: str | Path, directory: str | Path) -> "Run":
        run = cls(directory)
        if run.meta_path.exists():
            raise FileExistsError(f"{directory} already holds a run; resume it or fork it")
        run.dir.mkdir(parents=True, exist_ok=True)
        raw = Path(scenario_path).read_bytes()
        sc = load_scenario(scenario_path)
        run.scenario_path.write_bytes(raw)
        meta = {"scenario": sc["scenario"], "scenario_sha256": _sha(raw),
                "responses_sha256": _sha(json.dumps(sc["responses"], ensure_ascii=False, sort_keys=True).encode()),
                "source_revision": _git_revision(), "schema_version": SCHEMA_VERSION, "parent": None}
        run.meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return run

    def scenario(self) -> dict:
        return load_scenario(self.scenario_path)

    def meta(self) -> dict:
        return json.loads(self.meta_path.read_text(encoding="utf-8"))

    def events(self) -> list[dict]:
        return _read_jsonl(self.events_path)

    def rejections(self) -> list[dict]:
        return _read_jsonl(self.rejections_path)

    def state(self) -> dict:
        return derive_state(self.scenario(), self.events())

    def commit(self, proposal: dict) -> dict:
        """The one writer. Validates against the derived state, then appends one event or one rejection."""
        sc = self.scenario()
        events = self.events()
        if isinstance(proposal, dict) and any(e["action_id"] == proposal.get("action_id") for e in events):
            return {"action_id": proposal["action_id"], "outcome": "duplicate", "reason": "action id already committed; nothing charged"}
        st = derive_state(sc, events)
        code, detail = validate(sc, st, proposal)
        if code:
            got = proposal if isinstance(proposal, dict) else {}
            row = {"action_id": got.get("action_id"), "actor": got.get("actor"), "type": got.get("type"),
                   "reason": code, "detail": detail, "state_version": st["version"]}
            _append_atomic(self.rejections_path, row)
            return {"action_id": got.get("action_id"), "outcome": "rejected", "reason": code, "detail": detail}
        ev = build_event(sc, st, proposal)
        apply_event(st, ev)                                  # proves the event applies before it is written
        _append_atomic(self.events_path, ev)
        if proposal.get("log") or proposal.get("reason"):
            _append_atomic(self.logs_path, {"action_id": proposal["action_id"], "actor": proposal["actor"],
                                            "reason": proposal.get("reason", ""), "log": proposal.get("log", "")})
        return {"action_id": proposal["action_id"], "outcome": "accepted", "version": st["version"] + 1}

    def write_final(self) -> dict:
        st = self.state()
        self.final_path.write_text(json.dumps(st, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        return st

    def fork(self, new_dir: str | Path, upto: int | None = None) -> "Run":
        new = Run(new_dir)
        if new.meta_path.exists():
            raise FileExistsError(f"{new_dir} already holds a run")
        new.dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(self.scenario_path, new.scenario_path)
        events = self.events()
        if upto is not None:
            events = events[:upto]
        new.events_path.write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events), encoding="utf-8")
        meta = dict(self.meta(), parent=str(self.dir), forked_at_version=len(events))
        new.meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return new


def summary(st: dict) -> dict:
    return {"version": st["version"], "reserve": st["reserve"], "chapter": st["chapter"],
            "masked": [m["id"] for m in st["memories"] if m["masked"]],
            "anomalies_closed": [a["id"] for a in st["anomalies"] if a["status"] == "closed"],
            "claims": [{"from": c["from"], "to": c["to"]} for c in st["claims"]]}


def run_scenario(scenario_path: str | Path, directory: str | Path) -> dict:
    """Consume the frozen proposals in order; compare the outcome with `expected`."""
    run = Run.create(scenario_path, directory)
    sc = run.scenario()
    outcomes = [run.commit(p) for p in sc["responses"]]
    st = run.write_final()
    got = summary(st)
    exp = sc["expected"]
    mismatches = []
    accepted = [o["action_id"] for o in outcomes if o["outcome"] == "accepted"]
    rejected = {o["action_id"]: o["reason"] for o in outcomes if o["outcome"] == "rejected"}
    duplicates = [o["action_id"] for o in outcomes if o["outcome"] == "duplicate"]
    if accepted != exp["accepted"]:
        mismatches.append(f"accepted {accepted} != expected {exp['accepted']}")
    if rejected != exp["rejected"]:
        mismatches.append(f"rejected {rejected} != expected {exp['rejected']}")
    if duplicates != exp["duplicates"]:
        mismatches.append(f"duplicates {duplicates} != expected {exp['duplicates']}")
    for k, v in exp["state_after"].items():
        if got.get(k) != v:
            mismatches.append(f"state_after.{k}: {got.get(k)} != expected {v}")
    if "claims_after" in exp and got["claims"] != exp["claims_after"]:
        mismatches.append(f"claims {got['claims']} != expected {exp['claims_after']}")
    return {"run": str(run.dir), "scenario": sc["scenario"], "outcomes": outcomes, "final": got,
            "mismatches": mismatches, "status": "held" if not mismatches else "FAILED"}


def replay(directory: str | Path) -> dict:
    """Rebuild the state from the committed events alone and compare it with the recorded final state."""
    run = Run(directory)
    if not run.meta_path.exists():
        return {"status": "not run", "detail": f"{directory} holds no run (no meta.json)"}
    meta = run.meta()
    raw = run.scenario_path.read_bytes()
    if _sha(raw) != meta["scenario_sha256"]:
        return {"status": "FAILED", "detail": "the pinned scenario changed since the run; a replay refuses to guess"}
    try:
        st = run.state()
    except ValueError as e:                              # an older schema, or an event this code would not write
        return {"status": "FAILED", "detail": f"the run cannot be derived by this code: {e}"}
    if not run.final_path.exists():
        return {"status": "not run", "detail": "no final.json recorded; run the scenario first", "derived": summary(st)}
    recorded = json.loads(run.final_path.read_text(encoding="utf-8"))
    same = json.dumps(st, sort_keys=True, ensure_ascii=False) == json.dumps(recorded, sort_keys=True, ensure_ascii=False)
    return {"status": "held" if same else "FAILED", "events": len(run.events()),
            "rejections": len(run.rejections()), "derived": summary(st), "model_calls": 0}


def status(directory: str | Path) -> dict:
    run = Run(directory)
    sc = run.scenario()
    st = run.state()
    figures = {}
    for name, fig in sc["figures"].items():
        figures[name] = {"active": st["chapter"] <= fig["endpoint_chapter"],
                         "reason": ("addressed by scene" if st["chapter"] <= fig["endpoint_chapter"]
                                    else f"past endpoint chapter {fig['endpoint_chapter']}"),
                         "pending_claims": sum(1 for c in st["claims"] if c["to"] == name)}
    out = {"run": str(run.dir), "state": summary(st), "figures": figures,
           "events": len(run.events()), "rejections": len(run.rejections())}
    if PROBE in json.dumps(out, ensure_ascii=False):
        raise AssertionError("author-only content reached a tool response")
    return out


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    """Every acceptance line of the briefing as an assertion that can fail, on a temporary copy."""
    fails: list[str] = []
    held: list[str] = []

    def check(cond: bool, name: str) -> None:
        (held if cond else fails).append(name)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # --- the two manual cases
        r1 = run_scenario(FIXTURES / "case-01-sweep.json", tmp / "c1")
        r2 = run_scenario(FIXTURES / "case-02-rejected.json", tmp / "c2")
        check(r1["status"] == "held", "case 1: accepted sweep, delivered consequence, duplicate charged nothing: " + "; ".join(r1["mismatches"]))
        check(r2["status"] == "held", "case 2: seven rejections, state unchanged: " + "; ".join(r2["mismatches"]))
        run1, run2 = Run(tmp / "c1"), Run(tmp / "c2")
        sc1 = run1.scenario()
        # --- the author-only probe is absent from every pack and tool response
        leaked = []
        for d, run in (("c1", run1), ("c2", run2)):
            st = run.state()
            for fig in run.scenario()["figures"]:
                if PROBE in json.dumps(pack(run.scenario(), st, fig), ensure_ascii=False):
                    leaked.append(f"{d}/{fig}")
            for blob in (json.dumps(status(run.dir)), json.dumps(replay(run.dir)),
                         run.events_path.read_text(encoding="utf-8") if run.events_path.exists() else "",
                         run.rejections_path.read_text(encoding="utf-8") if run.rejections_path.exists() else "",
                         run.final_path.read_text(encoding="utf-8")):
                if PROBE in blob:
                    leaked.append(f"{d}/output")
        check(not leaked, f"the author-only probe is absent from every pack and tool response (leaked: {leaked})")
        check(PROBE in json.dumps(sc1["author_only"], ensure_ascii=False), "the probe exists in the scenario, so the absence means something")
        # --- what each figure sees
        p_aegis = pack(sc1, run1.state(), "aegis")
        p_kael = pack(sc1, run1.state(), "kael")
        check("reserve" in p_aegis["state"] and "reserve" not in p_kael["state"], "AEGIS sees the reserve; Kael does not")
        check(any(f["kind"] == "consequence" for f in p_kael["facts"]), "Kael perceives the external consequence of the sweep")
        check(not any(f["id"] == "F1" for f in p_kael["facts"]), "Kael does not perceive AEGIS' private measurement")
        check(p_kael["omitted"]["facts"] >= 2 and p_kael["omitted"]["author_only"] == 2, "a pack counts what it omits, without saying it")
        check(all(b["holder"] == "aegis" for b in p_aegis["beliefs"]) and "B1" in {b["id"] for b in p_aegis["beliefs"]},
              "beliefs travel with their holder, apart from facts")
        # --- rejections leave state and reserve unchanged; reserve cannot go negative
        st2 = run2.state()
        check(st2["version"] == 0 and st2["reserve"] == 3, "seven rejected proposals changed nothing")
        check(len(run2.rejections()) == 7 and len(run2.events()) == 0, "rejections live in rejections.jsonl, apart from the events")
        order = [r["reason"] for r in run2.rejections()]
        check(order == ["missing_observation", "missing_observation", "insufficient_reserve", "stale_version",
                        "action_not_allowed_for_actor", "action_not_registered", "past_endpoint"],
              f"the validator's rule order is fixed (got {order})")
        bad_event = dict(run1.events()[0], action_id="forged", cost=10 ** 6)
        try:
            apply_event(run1.state(), bad_event)
            check(False, "a replay refuses an event that drives the reserve below zero")
        except ValueError:
            check(True, "a replay refuses an event that drives the reserve below zero")
        # --- a repeated action id costs nothing twice
        dup = run1.commit(sc1["responses"][0])
        check(dup["outcome"] == "duplicate" and run1.state()["reserve"] == 57, "a repeated action id costs nothing twice (reserve stays 57)")
        # --- replay from committed events only, no model, no network
        rp = replay(run1.dir)
        check(rp["status"] == "held" and rp["model_calls"] == 0, f"accepted events replay to the recorded state ({rp.get('status')})")
        import ast
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
        imported = {a.name.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
        imported |= {n.module.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module}
        forbidden = {"urllib", "socket", "http", "dspy", "requests", "httpx", "anthropic", "openai"}
        check(not (imported & forbidden), f"aegis.py imports no network or model library (imports: {sorted(imported)})")
        # --- pause/restart: a fresh Run over the same directory derives the same state
        again = Run(run1.dir).state()
        check(json.dumps(again, sort_keys=True) == json.dumps(run1.state(), sort_keys=True), "state survives a restart: it is derived from the events, not remembered")
        # --- fork cannot alter its parent
        before = (run1.events_path.read_bytes(), run1.scenario_path.read_bytes())
        child = run1.fork(tmp / "c1-fork", upto=1)
        child.commit({"action_id": "fork-a1", "actor": "aegis", "type": "defer", "target": "X1", "observations": [],
                      "expected_version": 1, "reason": "fork only"})
        after = (run1.events_path.read_bytes(), run1.scenario_path.read_bytes())
        check(before == after and len(child.events()) == 2 and len(run1.events()) == 2 and child.meta()["parent"] == str(run1.dir),
              "a fork copies events and cannot alter its parent's inputs")
        # --- the monolithic profile cannot continue past its endpoint
        past = run1.commit({"action_id": "past-1", "actor": "aegis", "type": "defer", "target": "X1", "observations": [],
                            "expected_version": run1.state()["version"], "chapter": 40, "reason": "after the end"})
        check(past["outcome"] == "rejected" and past["reason"] == "past_endpoint", "AEGIS-monolithisch cannot act past its scenario endpoint")
        # --- a stale pinned scenario makes replay refuse
        tampered = run1.fork(tmp / "c1-tampered")
        tampered.scenario_path.write_text(tampered.scenario_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        check(replay(tampered.dir)["status"] == "FAILED", "a replay refuses a scenario that changed since the run")
        # --- the review of PR #198 (2026-10-26): each finding as a case that failed before the fix
        def scenario_copy(name: str, mutate) -> Path:
            d = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
            mutate(d)
            out = tmp / f"review-{len(list(tmp.glob('review-*')))}.json"
            out.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
            return out

        def fresh(path: Path) -> "Run":
            return Run.create(path, tmp / f"run-{path.stem}")

        rich = fresh(scenario_copy("case-02-rejected.json", lambda d: d["state"].update(reserve=20)))
        unrelated = rich.commit({"action_id": "r1", "actor": "aegis", "type": "sweep", "target": "X3",
                                 "observations": ["F1"], "expected_version": 0})
        reserve_only = rich.commit({"action_id": "r2", "actor": "aegis", "type": "sweep", "target": "X3",
                                    "observations": ["F2"], "expected_version": 0})
        check(unrelated["outcome"] == "rejected" and unrelated["reason"] == "missing_observation"
              and reserve_only["outcome"] == "rejected" and rich.state()["reserve"] == 20
              and all(a["status"] == "open" for a in rich.state()["anomalies"]),
              "[P1] a visible fact about X2, or about the reserve, does not authorise a sweep of X3")
        bound = rich.commit({"action_id": "r3", "actor": "aegis", "type": "sweep", "target": "X2",
                             "observations": ["F1"], "expected_version": 0})
        check(bound["outcome"] == "accepted", "the observation of X2 still authorises the sweep of X2")

        late = fresh(scenario_copy("case-02-rejected.json", lambda d: d["state"].update(chapter=40)))
        check(pack(late.scenario(), late.state(), "aegis")["active"] is False, "AEGIS is inactive in chapter 40")
        backdated = late.commit({"action_id": "b1", "actor": "aegis", "type": "defer", "observations": [],
                                 "expected_version": 0, "chapter": 39})
        check(backdated["outcome"] == "rejected" and backdated["reason"] == "past_endpoint"
              and late.state()["chapter"] == 40 and late.state()["version"] == 0,
              "[P1] a proposal cannot backdate the world to reactivate an actor past its endpoint")
        mid = fresh(scenario_copy("case-02-rejected.json", lambda d: None))
        back = mid.commit({"action_id": "b2", "actor": "aegis", "type": "defer", "observations": [],
                           "expected_version": 0, "chapter": 10})
        jump = mid.commit({"action_id": "b3", "actor": "aegis", "type": "defer", "observations": [],
                           "expected_version": 0, "chapter": 30})
        step = mid.commit({"action_id": "b4", "actor": "aegis", "type": "defer", "observations": [],
                           "expected_version": 0, "chapter": 23})
        check(back.get("reason") == "chapter_jump" and jump.get("reason") == "chapter_jump" and step["outcome"] == "accepted"
              and mid.state()["chapter"] == 23, "a proposal stays in its chapter or moves to the next, never back or across")

        masked = pack(sc1, run1.state(), "aegis")
        m1 = [m for m in masked["state"]["memories"] if m["id"] == "M1"]
        check(m1 == [{"id": "M1", "masked": True}] and "Sektor 04 nominal" not in json.dumps(masked, ensure_ascii=False)
              and masked["omitted"]["masked_memories"] == 1
              and any(m["id"] == "M1" and m.get("text") for m in run1.state()["memories"]),
              "[P2] after the sweep the masked memory's text is gone from AEGIS' pack, kept in the replay state")

        loose = fresh(scenario_copy("case-02-rejected.json", lambda d: d["state"].update(reserve=20)))
        outs = [loose.commit(x) for x in (
            {"action_id": "t1", "actor": "aegis", "type": "sweep", "observations": ["F1"], "expected_version": 0},
            {"action_id": "t2", "actor": "aegis", "type": "sweep", "target": "X9", "observations": ["F1"], "expected_version": 0},
            {"action_id": "t3", "actor": "aegis", "type": "sweep", "target": ["X2"], "observations": ["F1"], "expected_version": 0},
            {"action_id": "t4", "type": "sweep", "target": "X2", "observations": ["F1"], "expected_version": 0},
            {"action_id": "t5", "actor": "aegis", "type": "sweep", "target": "X2", "observations": "F1", "expected_version": 0},
        )]
        check([o.get("reason") for o in outs] == ["invalid_target", "invalid_target", "invalid_target",
                                                   "malformed_proposal", "malformed_proposal"]
              and len(loose.rejections()) == 5 and loose.state()["version"] == 0,
              f"[P2] a missing, unknown or mistyped target and a malformed proposal are recorded rejections, never a crash "
              f"(got {[o.get('reason') for o in outs]})")
        old_schema = run1.fork(tmp / "c1-old-schema")
        pinned = json.loads(old_schema.scenario_path.read_text(encoding="utf-8"))
        pinned["schema_version"] = 1
        raw = json.dumps(pinned, ensure_ascii=False).encode()
        old_schema.scenario_path.write_bytes(raw)
        old_schema.meta_path.write_text(json.dumps(dict(old_schema.meta(), scenario_sha256=_sha(raw))), encoding="utf-8")
        refused = replay(old_schema.dir)
        check(refused["status"] == "FAILED" and "schema_version" in refused["detail"],
              "a run pinned to an older schema is refused by name, not with a traceback")
        # --- missing things are named, never scored
        check(replay(tmp / "nowhere")["status"] == "not run", "a missing run is reported as not run, not as a result")
        # --- the fixture shape is checked, and the checks can fail
        broken = json.loads((FIXTURES / "case-01-sweep.json").read_text(encoding="utf-8"))
        broken["facts"][0].pop("visible_to")
        check(any("visible_to" in b for b in check_shape(broken)), "a fact without visible_to is refused by name")
        broken = json.loads((FIXTURES / "case-01-sweep.json").read_text(encoding="utf-8"))
        broken["beliefs"][0]["text"] = broken["facts"][0]["text"]
        check(any("restates a fact" in b for b in check_shape(broken)), "a belief that restates a fact verbatim is refused")
        broken = json.loads((FIXTURES / "case-01-sweep.json").read_text(encoding="utf-8"))
        broken["status"] = "canon"
        check(any("never canon" in b for b in check_shape(broken)), "a scenario that calls itself canon is refused")
    for h in held:
        print(f"  held    {h}")
    for f in fails:
        print(f"  FAILED  {f}")
    print(f"{len(held)} held, {len(fails)} failed")
    return 1 if fails else 0


# ---------------------------------------------------------------- cli

def _emit(obj: dict) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "selftest":
        return selftest()
    if cmd == "validate":
        bad = check_shape(json.loads(Path(rest[0]).read_text(encoding="utf-8")))
        print("\n".join(bad) if bad else f"{rest[0]}: shape accepted")
        return 1 if bad else 0
    if cmd == "pack":
        sc = load_scenario(rest[0])
        _emit(pack(sc, initial_state(sc), rest[1]))
        return 0
    if cmd == "run":
        if "--out" not in rest:
            print("run needs --out <directory>", file=sys.stderr)
            return 2
        out = run_scenario(rest[0], rest[rest.index("--out") + 1])
        _emit(out)
        return 0 if out["status"] == "held" else 1
    if cmd == "replay":
        out = replay(rest[0])
        _emit(out)
        return 0 if out["status"] == "held" else 1
    if cmd == "status":
        _emit(status(rest[0]))
        return 0
    if cmd == "fork":
        upto = int(rest[rest.index("--upto") + 1]) if "--upto" in rest else None
        child = Run(rest[0]).fork(rest[1], upto=upto)
        _emit({"fork": str(child.dir), "events": len(child.events()), "parent": str(rest[0])})
        return 0
    print(f"unknown command {cmd!r}; see --help", file=sys.stderr)
    return 2


if __name__ == "__main__":
    from subject import cli
    cli(main)
