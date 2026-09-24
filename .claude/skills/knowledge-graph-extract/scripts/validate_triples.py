#!/usr/bin/env python3
"""Validate extracted triples against a graph schema.

Reads <output_dir>/triples.jsonl, checks structure, schema conformance and
exact duplicates. By default only reports; with --apply, violations are moved
to rejected.jsonl and triples.jsonl is rewritten atomically.

Python 3 stdlib only. No network, no subprocess.
"""

import argparse
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = ("doc", "chunk", "subject", "relation", "object")


def load_schema(path):
    schema = json.loads(Path(path).read_text(encoding="utf-8"))
    entity_types = set(schema.get("entity_types") or [])
    relations = {}
    for rel in schema.get("relation_types") or []:
        if isinstance(rel, str):
            relations[rel] = {}
        else:
            relations[rel["name"]] = {
                "subject_types": set(rel.get("subject_types") or []),
                "object_types": set(rel.get("object_types") or []),
            }
    return entity_types, relations


def check_triple(triple, entity_types, relations):
    """Return a rejection reason, or None if the triple is valid."""
    for field in REQUIRED_FIELDS:
        value = triple.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            return f"missing or empty field '{field}'"
    if entity_types:
        for side in ("subject_type", "object_type"):
            t = triple.get(side)
            if not t:
                return f"missing '{side}' (schema defines entity_types)"
            if t not in entity_types:
                return f"{side} '{t}' not in schema entity_types"
    if relations:
        rel = triple["relation"]
        if rel not in relations:
            return f"relation '{rel}' not in schema relation_types"
        constraints = relations[rel]
        subj_ok = constraints.get("subject_types")
        obj_ok = constraints.get("object_types")
        if subj_ok and triple.get("subject_type") not in subj_ok:
            return (f"relation '{rel}' requires subject_type in "
                    f"{sorted(subj_ok)}, got '{triple.get('subject_type')}'")
        if obj_ok and triple.get("object_type") not in obj_ok:
            return (f"relation '{rel}' requires object_type in "
                    f"{sorted(obj_ok)}, got '{triple.get('object_type')}'")
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("output_dir", help="extraction output directory")
    parser.add_argument("--schema", help="schema.json path (default: <output_dir>/schema.json if present)")
    parser.add_argument("--apply", action="store_true",
                        help="move violations to rejected.jsonl and rewrite triples.jsonl")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    triples_path = out_dir / "triples.jsonl"
    if not triples_path.exists():
        print(f"error: {triples_path} not found", file=sys.stderr)
        return 1

    schema_path = Path(args.schema) if args.schema else out_dir / "schema.json"
    entity_types, relations = (set(), {})
    if schema_path.exists():
        entity_types, relations = load_schema(schema_path)
        print(f"schema: {schema_path} ({len(entity_types)} entity types, {len(relations)} relation types)")
    else:
        print("schema: none (structural checks and dedup only)")

    valid, rejected = [], []
    seen = set()
    for lineno, line in enumerate(triples_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            triple = json.loads(line)
        except json.JSONDecodeError as exc:
            rejected.append({"raw": line, "reason": f"invalid JSON on line {lineno}: {exc.msg}"})
            continue
        reason = check_triple(triple, entity_types, relations)
        if reason is None:
            key = (triple["subject"], triple["relation"], triple["object"])
            if key in seen:
                reason = "exact duplicate of an earlier triple"
            else:
                seen.add(key)
        if reason is None:
            valid.append(triple)
        else:
            rejected.append({**(triple if isinstance(triple, dict) else {}), "reason": reason})

    print(f"triples: {len(valid) + len(rejected)} total, {len(valid)} valid, {len(rejected)} violations")
    for r in rejected[:20]:
        subject = r.get("subject", "?")
        print(f"  - [{r.get('doc', '?')}#{r.get('chunk', '?')}] {subject}: {r['reason']}")
    if len(rejected) > 20:
        print(f"  ... and {len(rejected) - 20} more")

    if args.apply:
        if rejected:
            rejected_path = out_dir / "rejected.jsonl"
            with rejected_path.open("a", encoding="utf-8") as fh:
                for r in rejected:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            tmp_path = triples_path.with_suffix(".jsonl.tmp")
            with tmp_path.open("w", encoding="utf-8") as fh:
                for t in valid:
                    fh.write(json.dumps(t, ensure_ascii=False) + "\n")
            tmp_path.replace(triples_path)
            print(f"applied: {len(rejected)} triples moved to {rejected_path.name}")
        else:
            print("nothing to apply — all triples valid")
        return 0  # --apply succeeded; the quarantine is the intended outcome, not a failure

    if rejected:
        print("run with --apply to move violations to rejected.jsonl")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
