"""Loader for the research-wiki schema contract (``Wiki/schema/*.yaml``).

The YAML files are the single source of truth for page kinds, enums,
lifecycle transitions, edge types, cross-reference rules, ownership zones and
write permissions (concept §3.2, AutoSci schema-as-contract). Scripts and DSPy
programs read them through this module; nothing is generated. The Pydantic
``Literal`` enums in ``tools/kpwiki/schema.py`` are built from these values at
import time and ``tests/test_wiki_schema.py`` guards that derivation.

Only the standard library plus PyYAML is used, so ``scripts/wiki_lint.py`` can
run without the DSPy virtualenv.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "Wiki" / "schema"
FILES = ("entities", "edges", "xref", "conventions", "writers")


@lru_cache(maxsize=None)
def load(name: str) -> dict[str, Any]:
    """Return one schema file as a dict; ``name`` is one of :data:`FILES`."""
    if name not in FILES:
        raise ValueError(f"unknown schema file {name!r}; expected one of {FILES}")
    with (SCHEMA_DIR / f"{name}.yaml").open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{name}.yaml must be a mapping")
    return data


def entities() -> dict[str, Any]:
    return load("entities")


def edges() -> dict[str, Any]:
    return load("edges")


def xref() -> dict[str, Any]:
    return load("xref")


def conventions() -> dict[str, Any]:
    return load("conventions")


def writers() -> dict[str, Any]:
    return load("writers")


def enum_values(name: str) -> list[str]:
    """Values of a shared enum (``tier``, ``category``, ``canon_status`` …)."""
    values = entities()["enums"].get(name)
    if values is None:
        raise KeyError(f"no enum {name!r} in entities.yaml; known: {sorted(entities()['enums'])}")
    return list(values)


def kinds() -> list[str]:
    return list(entities()["kinds"])


def kind(name: str) -> dict[str, Any]:
    try:
        return entities()["kinds"][name]
    except KeyError as exc:
        raise KeyError(f"no page kind {name!r}; known: {kinds()}") from exc


def kind_for_path(path: Path | str) -> str | None:
    """Page kind by directory (``Wiki/sources/x.md`` → ``source``); candidates use their ``kind`` field."""
    rel = Path(path).as_posix()
    for name, spec in entities()["kinds"].items():
        if rel.startswith(spec["dir"].rstrip("/") + "/"):
            return name
    return None


def required_fields(kind_name: str) -> list[str]:
    return list(kind(kind_name)["required"])


def field_enum(kind_name: str, field: str) -> list[str] | None:
    """The closed value set of a frontmatter field, or None when it is free."""
    spec = kind(kind_name).get("fields", {}).get(field, {})
    if "const" in spec:
        return [spec["const"]]
    if spec.get("lifecycle"):
        return list(entities()["lifecycle"]["states"])
    enum_name = spec.get("enum")
    if isinstance(enum_name, list):
        return list(enum_name)
    if isinstance(enum_name, str):
        return enum_values(enum_name)
    return None


def lifecycle() -> dict[str, Any]:
    return entities()["lifecycle"]


def legal_transition(old: str, new: str) -> bool:
    if old == new:
        return True
    return new in lifecycle()["transitions"].get(old, [])


def protected_statuses() -> list[str]:
    return list(lifecycle().get("protected", []))


def slug_pattern() -> re.Pattern[str]:
    return re.compile(conventions()["slug"]["pattern"])


def citation_pattern() -> re.Pattern[str]:
    return re.compile(entities()["citation"]["pattern"])


def edge_types() -> dict[str, Any]:
    return edges()["types"]


def writer_for(skill: str) -> dict[str, Any] | None:
    return writers()["writers"].get(skill)


def mirror_report() -> list[str]:
    """Compare the YAML enums with the Pydantic Literals in ``tools/kpwiki/schema.py``.

    Returns the list of mismatches (empty when in sync; a hard-coded Literal
    re-introduced in ``schema.py`` shows up here). Imported lazily so the
    plain-python scripts never need pydantic.
    """
    from typing import get_args

    from . import schema as py

    pairs = {"tier": py.SourceTier, "category": py.SourceCategory,
             "confidence": py.Confidence, "canon_relation": py.CanonRelation}
    problems = []
    for name, literal in pairs.items():
        yaml_values, py_values = set(enum_values(name)), set(get_args(literal))
        if yaml_values != py_values:
            problems.append(f"{name}: yaml {sorted(yaml_values)} != schema.py {sorted(py_values)}")
    return problems
