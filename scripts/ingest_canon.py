#!/usr/bin/env python3
"""Canon → novel-capability ingestion driver (Kohärenz Protokoll).

Reads the 7 extraction manifests in Plan/ingest/, normalizes them into
verb ops, and executes them through `agency execute` (CLI code-mode) in
fault-tolerant batches. Every write goes through a capability verb so
the provenance graph records Invocations + SERVES edges.

Resumable: progress + minted ids land in Plan/ingest/ledger.json.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "Plan" / "ingest"
LEDGER = ING / "ledger.json"
AGENCY = "/root/.local/bin/agency"
INTENT = "intent:081f5ced"
AGENT = "agent:claude"
NOVEL = "novel:9d170c31"
MAX_BATCH_BYTES = 60_000


def load(name: str) -> dict:
    return json.loads((ING / f"{name}.extraction.json").read_text(encoding="utf-8"))


def ledger_load() -> dict:
    if LEDGER.is_file():
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    return {"phases": {}, "ids": {}}


def ledger_save(led: dict) -> None:
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1), encoding="utf-8")


def run_ops(ops: list[dict], _retry: bool = True) -> tuple[list, list]:
    """Run a batch of {tool, args} ops inside ONE agency-execute block.

    Returns (results, errors); results align 1:1 with ops (None on error).
    A verb returning null (ToolResult.failure) counts as an error.
    """
    code = (
        "data = " + repr(ops) + "\n"
        "res = []\n"
        "errs = []\n"
        "for op in data:\n"
        "    try:\n"
        "        r = await call_tool(op['tool'], op['args'])\n"
        "        res.append(r)\n"
        "        if r is None:\n"
        "            errs.append([op['tool'], str(op['args'])[:120], 'NULL_RESULT (ToolResult.failure)'])\n"
        "    except Exception as e:\n"
        "        errs.append([op['tool'], str(op['args'])[:120], str(e)[:300]])\n"
        "        res.append(None)\n"
        "return {'results': res, 'errors': errs}\n"
    )
    proc = subprocess.run(
        [AGENCY, "execute"], input=code, capture_output=True, text=True,
        cwd=str(ROOT), timeout=600,
    )
    line = ""
    for ln in reversed(proc.stdout.strip().splitlines()):
        if ln.strip().startswith("{"):
            line = ln
            break
    if not line:
        raise RuntimeError(f"no JSON from agency execute: rc={proc.returncode} "
                           f"stdout={proc.stdout[-400:]} stderr={proc.stderr[-400:]}")
    out = json.loads(line)
    if "error" in out and "results" not in out:
        # Writes from the failed block PERSIST (no rollback). Callers must be
        # idempotent against ground truth (see existing()) before re-running.
        raise RuntimeError(f"execute failed: {out}")
    return out["results"], out["errors"]


def existing(label: str, key: str, int_key: bool = False) -> dict:
    """Ground truth from the graph (read-only): prop value → string node id."""
    import sqlite3
    c = sqlite3.connect(f"file:{ROOT}/.agency/session.db?mode=ro", uri=True)
    table = "node_props_int" if int_key else "node_props_text"
    q = (f"SELECT t.value, sid.value FROM node_labels l "
         f"JOIN {table} t ON t.node_id=l.node_id "
         f"JOIN property_keys pk ON pk.id=t.key_id "
         f"JOIN node_props_text sid ON sid.node_id=l.node_id "
         f"JOIN property_keys pid ON pid.id=sid.key_id AND pid.key='id' "
         f"WHERE l.label=? AND pk.key=?")
    out = {}
    for val, sid in c.execute(q, (label, key)):
        out[val] = sid
    c.close()
    return out


# Spec 132 — only 5 CodexEntry kinds are valid; everything else maps to one
# of them and keeps its original category in the body header.
KIND_MAP = {
    "location": "location", "faction": "faction", "artefact": "artefact",
    "minor-character": "minor-character", "character": "minor-character",
    "technology": "artefact", "system": "artefact",
}


def map_kind(kind: str) -> str:
    return KIND_MAP.get(kind, "concept")


def batched(ops: list[dict]):
    """Greedy batches capped by bytes AND the engine's 50-call/block limit."""
    cur, size = [], 0
    for op in ops:
        s = len(repr(op))
        if cur and (size + s > MAX_BATCH_BYTES or len(cur) >= 45):
            yield cur
            cur, size = [], 0
        cur.append(op)
        size += s
    if cur:
        yield cur


def op(tool: str, **args) -> dict:
    args.setdefault("intent_id", INTENT)
    args.setdefault("agent_id", AGENT)
    return {"tool": tool, "args": args}


def slug_ascii(s: str) -> str:
    s = (s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
         .replace("ß", "ss"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80] or "x"


# ───────────────────────── normalization ─────────────────────────

def build_codex_entries(m: dict[str, dict]) -> list[dict]:
    """Merge every codex-worthy stream into deduped entries."""
    entries: dict[str, dict] = {}

    def add(slug, name, kind, body, triggers, source):
        slug = slug_ascii(slug)
        body = (f"**Kategorie:** {kind}\n\n## Quelle: {source}\n\n{body.strip()}"
                if map_kind(kind) != kind else
                f"## Quelle: {source}\n\n{body.strip()}")
        kind = map_kind(kind)
        if slug in entries:
            e = entries[slug]
            e["body"] += "\n\n" + body
            if triggers:
                have = {t.strip() for t in e["triggers"].split(",") if t.strip()}
                for t in triggers.split(","):
                    if t.strip() and t.strip() not in have:
                        e["triggers"] += ("," if e["triggers"] else "") + t.strip()
        else:
            entries[slug] = {"slug": slug, "name": name, "kind": kind,
                             "body": body, "triggers": triggers or ""}

    for doc in ["kap0", "storyform", "characters", "begriffe", "kernwelten",
                "philosophie", "sensorik"]:
        d = m[doc]
        src = d.get("source", doc)
        for e in d.get("codex_entries", []):
            add(e["slug"], e.get("name", e["slug"]), e.get("kind", "concept"),
                e.get("body", ""), e.get("triggers", ""), src)

    src = m["kap0"]["source"]
    for r in m["kap0"].get("style_rules", []):
        add(r["id"], f"Stilregel {r['id']}", "rule", r["text"], "", src)
    for mo in m["kap0"].get("motifs", []):
        add(mo["slug"], mo["name"], "motif", mo.get("body", ""), "", src)
    for i, dft in enumerate(m["kap0"].get("defects", []), 1):
        body = dft.get("text", "")
        if dft.get("rule"):
            body += f"\n\n(Verletzte Regel: {dft['rule']})"
        add(f"defekt-kap0-{dft.get('id', i)}", f"Kap-0-Defekt {dft.get('id', i)}",
            "defect", body, "", src)

    src = m["begriffe"]["source"]
    for i, r in enumerate(m["begriffe"].get("usage_rules", []), 1):
        add(f"usage-rule-{r.get('id', i)}", f"Verwendungsregel {r.get('id', i)}",
            "rule", r["text"], "", src)

    src = m["sensorik"]["source"]
    for i, r in enumerate(m["sensorik"].get("drafting_rules", []), 1):
        add(f"drafting-rule-{r.get('id', i)}", f"Drafting-Regel {r.get('id', i)}",
            "rule", r["text"], "", src)
    for i, g in enumerate(m["sensorik"].get("scene_guidance", []), 1):
        body = g["text"]
        if g.get("applies_to"):
            body = f"**Gilt für:** {g['applies_to']}\n\n{body}"
        add(f"szenen-guidance-{i}", f"Szenen-Guidance {i}", "guidance", body, "", src)

    src = m["characters"]["source"]
    dna = m["characters"].get("sprach_dna", {})
    for i, r in enumerate(dna.get("rules", []), 1):
        add(f"sprach-dna-{r.get('id', i)}", f"Sprach-DNA {r.get('id', i)}",
            "rule", r["text"], "", src)
    for reg in dna.get("registers", []):
        add(f"register-{slug_ascii(reg['name'])}", f"Register: {reg['name']}",
            "voice", reg.get("description", ""), "", src)
    for c in m["characters"].get("characters", []):
        body = f"**Rolle:** {c.get('role', '')}\n\n{c.get('body', '')}"
        if c.get("voice_signature"):
            body += f"\n\n### Stimm-Signatur\n{c['voice_signature']}"
        if c.get("known_facts_at_start"):
            body += "\n\n### Wissen zu Story-Beginn\n" + "\n".join(
                f"- {f}" for f in c["known_facts_at_start"])
        add(c["slug"], c["name"], "character", body, c.get("triggers", ""), src)

    src = m["philosophie"]["source"]
    for t in m["philosophie"].get("themes", []):
        body = f"**These:** {t.get('statement', '')}"
        if t.get("counter_statement"):
            body += f"\n\n**Antithese:** {t['counter_statement']}"
        add(f"thema-{slug_ascii(t['name'])}", f"Thema: {t['name']}", "theme",
            body, "", src)
    for i, q in enumerate(m["philosophie"].get("open_questions", []), 1):
        add(f"offene-frage-{i}", f"Offene Frage {i}", "question", q, "", src)

    for doc in ["kap0", "storyform", "characters", "begriffe", "kernwelten",
                "philosophie", "sensorik"]:
        d = m[doc]
        for i, u in enumerate(d.get("unmapped", []), 1):
            u_txt = u if isinstance(u, str) else json.dumps(u, ensure_ascii=False)
            add(f"unmapped-{doc}-{i}", f"Unzugeordnet ({doc} {i})", "note",
                u_txt, "", d.get("source", doc))

    return list(entries.values())


def chapter_body(ch: dict) -> str:
    parts = ["## Outline\n"]
    if ch.get("act"):
        parts.append(f"**Akt:** {ch['act']}\n")
    if ch.get("pov"):
        parts.append(f"**POV:** {ch['pov']}\n")
    if ch.get("summary"):
        parts.append(f"\n{ch['summary']}\n")
    if ch.get("beats"):
        parts.append("\n### Beats\n" + "\n".join(f"- {b}" for b in ch["beats"]))
    return "".join(parts)


# ───────────────────────── phases ─────────────────────────

def main() -> int:
    m = {n: load(n) for n in ["kap0", "storyform", "characters", "begriffe",
                              "kernwelten", "philosophie", "sensorik"]}
    led = ledger_load()
    ids = led["ids"]
    failures: list = []

    def phase_done(name):
        return led["phases"].get(name, {}).get("done")

    def mark(name, errors):
        led["phases"][name] = {"done": True, "errors": errors}
        failures.extend(errors)
        ledger_save(led)
        print(f"[{name}] done, {len(errors)} errors", flush=True)

    # P1 — worlds (6 from kernwelten + 1 meta layer for cross-world axioms)
    if not phase_done("worlds"):
        ops = [op("capability_novel_create_world", slug=w["slug"], name=w["name"])
               for w in m["kernwelten"]["worlds"]]
        ops.append(op("capability_novel_create_world", slug="kosmos-meta",
                      name="Kosmos (Meta-Ebene) — übergreifende Invarianten"))
        errs_all = []
        slugs = [w["slug"] for w in m["kernwelten"]["worlds"]] + ["kosmos-meta"]
        res, errs = run_ops(ops)
        for s, r in zip(slugs, res):
            if r:
                ids[f"world:{s}"] = r.get("world_id", "")
        errs_all += errs
        mark("worlds", errs_all)

    # P2 — axioms: per-world; kernwelten globals → Überwelt;
    # begriffe physics → externe Ebene; philosophie metaphysics → kosmos-meta
    if not phase_done("axioms"):
        ops = []
        for w in m["kernwelten"]["worlds"]:
            wid = ids.get(f"world:{w['slug']}")
            for a in w.get("axioms", []):
                ops.append(op("capability_novel_create_world_axiom", world_id=wid,
                              text=a["text"], severity=a.get("severity", "hard")))
        ueber = ids.get("world:ueberwelt-aegis-maschinenraum")
        for a in m["kernwelten"].get("global_axioms", []):
            ops.append(op("capability_novel_create_world_axiom", world_id=ueber,
                          text=a["text"], severity=a.get("severity", "hard")))
        ext = ids.get("world:externe-ebene-koeln-2026")
        for a in m["begriffe"].get("axioms", []):
            ops.append(op("capability_novel_create_world_axiom", world_id=ext,
                          text=a["text"], severity=a.get("severity", "hard")))
        kosmos = ids.get("world:kosmos-meta")
        for a in m["philosophie"].get("axioms", []):
            ops.append(op("capability_novel_create_world_axiom", world_id=kosmos,
                          text=a["text"], severity=a.get("severity", "hard")))
        errs_all = []
        for batch in batched(ops):
            _, errs = run_ops(batch)
            errs_all += errs
        mark("axioms", errs_all)

    # P3 — codex entries (deduped, all streams; idempotent vs ground truth)
    if not phase_done("codex"):
        entries = build_codex_entries(m)
        have = existing("CodexEntry", "slug")
        for s, sid in have.items():
            ids[f"codex:{s}"] = sid
        entries = [e for e in entries if e["slug"] not in have]
        print(f"[codex] {len(entries)} to create ({len(have)} already exist)",
              flush=True)
        errs_all = []
        for batch in batched([
            op("capability_novel_create_codex_entry", novel_id=NOVEL,
               slug=e["slug"], name=e["name"], kind=e["kind"], body=e["body"],
               triggers=e["triggers"]) for e in entries
        ]):
            res, errs = run_ops(batch)
            for o, r in zip(batch, res):
                if r and r.get("entry_id"):
                    ids[f"codex:{o['args']['slug']}"] = r["entry_id"]
            errs_all += errs
            ledger_save(led)
        mark("codex", errs_all)

    # P4 — chapters 0..40 (storyform = normative; ch0 body = clean prose)
    if not phase_done("chapters"):
        clean = (ING / "kap0-clean-body.md").read_text(encoding="utf-8")
        have = existing("Chapter", "number", int_key=True)
        for n, sid in have.items():
            ids[f"chapter:{n}"] = sid
        ops = []
        for ch in sorted(m["storyform"]["chapters"], key=lambda c: c["number"]):
            if ch["number"] in have:
                continue
            body = clean if ch["number"] == 0 else chapter_body(ch)
            ops.append(op("capability_novel_create_chapter", novel_id=NOVEL,
                          number=ch["number"], title=ch["title"], body=body))
        errs_all = []
        for batch in batched(ops):
            res, errs = run_ops(batch)
            for o, r in zip(batch, res):
                if r and r.get("chapter_id"):
                    ids[f"chapter:{o['args']['number']}"] = r["chapter_id"]
            errs_all += errs
            ledger_save(led)
        if ids.get("chapter:0"):
            _, errs = run_ops([op("capability_novel_set_chapter_status",
                                  chapter_id=ids["chapter:0"], status="revised")])
            errs_all += errs
        mark("chapters", errs_all)

    # P5 — chapter-0 scenes + narrative-beat chain (PRECEDES across the chapter)
    if not phase_done("scenes"):
        ch0 = ids.get("chapter:0")
        errs_all = []
        scenes = sorted(m["kap0"]["scenes"], key=lambda s: s["order"])
        have = existing("Scene", "slug")
        for s2, sid in have.items():
            ids[f"scene:{s2}"] = sid
        todo = [s for s in scenes if s["slug"] not in have]
        if todo:
            res, errs = run_ops([
                op("capability_novel_create_scene", chapter_id=ch0,
                   slug=s["slug"], pov=s["pov"]) for s in todo])
            for s, r in zip(todo, res):
                if r and r.get("scene_id"):
                    ids[f"scene:{s['slug']}"] = r["scene_id"]
            errs_all += errs
        ledger_save(led)
        # beats: chained predecessor across the whole chapter for narrative_order
        have_beats = existing("NarrativeBeat", "label")
        beat_ops, beat_keys = [], []
        for s in scenes:
            sid = ids.get(f"scene:{s['slug']}")
            for j, b in enumerate(s.get("beats", []), 1):
                if b in have_beats:
                    ids[f"beat:{s['slug']}:{j}"] = have_beats[b]
                    continue
                beat_ops.append({"scene": sid, "label": b,
                                 "key": f"beat:{s['slug']}:{j}"})
        prev_key = ""
        for bo in beat_ops:
            args = {"scene_id": bo["scene"], "beat_label": bo["label"]}
            bo["args"] = args
            bo["prev"] = prev_key
            prev_key = bo["key"]
        # run sequentially in chunks; resolve predecessor ids as we go
        chunk = 25
        for i in range(0, len(beat_ops), chunk):
            part = beat_ops[i:i + chunk]
            ops = []
            for bo in part:
                a = dict(bo["args"])
                if bo["prev"] and ids.get(bo["prev"]):
                    a["predecessor_id"] = ids[bo["prev"]]
                ops.append(op("capability_novel_mark_narrative_beat", **a))
            res, errs = run_ops(ops)
            for bo, r in zip(part, res):
                if r and r.get("beat_id"):
                    ids[bo["key"]] = r["beat_id"]
            errs_all += errs
            ledger_save(led)
        mark("scenes", errs_all)

    # P6 — story events (storyform chronology + kap0 events w/ scene reveals)
    if not phase_done("events"):
        errs_all = []
        have_ev = existing("StoryTimeEvent", "label")
        ops, keys = [], []
        for i, ev in enumerate(m["storyform"].get("story_events", [])):
            if ev["label"] in have_ev:
                continue
            ops.append(op("capability_novel_record_story_event", novel_id=NOVEL,
                          label=ev["label"], when_story=ev.get("when_story", "")))
            keys.append((f"event:sf:{i}", None))
        for i, ev in enumerate(m["kap0"].get("story_events", [])):
            if ev["label"] in have_ev:
                continue
            sid = ids.get(f"scene:{ev.get('scene_slug', '')}", "")
            a = {"novel_id": NOVEL, "label": ev["label"],
                 "when_story": ev.get("when_story", "")}
            if sid:
                a["scene_id"] = sid
            ops.append(op("capability_novel_record_story_event", **a))
            keys.append((f"event:k0:{i}", sid))
        for batch_keys, batch in zip(
                [keys[i:i + 30] for i in range(0, len(keys), 30)],
                [ops[i:i + 30] for i in range(0, len(ops), 30)]):
            res, errs = run_ops(batch)
            reveal_ops = []
            for (key, sid), r in zip(batch_keys, res):
                if r and r.get("event_id"):
                    ids[key] = r["event_id"]
                    if sid:
                        reveal_ops.append(op("capability_novel_reveal_in_scene",
                                             event_id=r["event_id"], scene_id=sid))
            if reveal_ops:
                _, errs2 = run_ops(reveal_ops)
                errs += errs2
            errs_all += errs
            ledger_save(led)
        mark("events", errs_all)

    # P7 — canon claims from every manifest
    if not phase_done("claims"):
        have_claims = existing("NovelClaim", "text")
        ops = []
        for doc in m.values():
            src = doc.get("source", "")
            for c in doc.get("claims", []):
                if c["text"] in have_claims:
                    continue
                ops.append(op("capability_novel_capture_claim", text=c["text"],
                              source_uri=src, domain=c.get("domain", "canon")))
        errs_all = []
        for batch in batched(ops):
            _, errs = run_ops(batch)
            errs_all += errs
        mark("claims", errs_all)

    # P8 — contested storyform decisions
    if not phase_done("decisions"):
        ops = [op("capability_novel_record_storyform_decision", novel_id=NOVEL,
                  decision=d["decision"], rationale=d.get("rationale", ""))
               for d in m["storyform"].get("storyform_decisions", [])]
        errs_all = []
        for batch in batched(ops):
            _, errs = run_ops(batch)
            errs_all += errs
        mark("decisions", errs_all)

    # P9 — character → world edges (codex character entries stand in for
    # Character nodes until the ontology ships Slice 2)
    if not phase_done("char_links"):
        ops = []
        for c in m["characters"].get("characters", []):
            cid = ids.get(f"codex:{slug_ascii(c['slug'])}")
            for ln in c.get("world_links", []):
                target = ids.get(f"world:{slug_ascii(ln.get('target', ''))}")
                if cid and target:
                    ops.append(op("capability_novel_link_character_to_world",
                                  character_id=cid, target_id=target,
                                  edge_kind=ln.get("edge", "BELONGS_TO")))
        errs_all = []
        if ops:
            for batch in batched(ops):
                _, errs = run_ops(batch)
                errs_all += errs
        mark("char_links", errs_all)

    ledger_save(led)
    print(json.dumps({"failures": len(failures), "ids_minted": len(ids)},
                     ensure_ascii=False))
    if failures:
        print("FAILURES (first 20):")
        for f in failures[:20]:
            print(" ", f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
