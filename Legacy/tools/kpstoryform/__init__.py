"""Decidable Dramatica checks over an NCP storyform — standard library only.

The novel carries two storyforms: ``ncp.json`` is A (Kael/K₁) and
``ncp-b.json`` is B (AEGIS/K₀). Both used to be checked by an engine plugin
that is no longer installed. The checks are decidable — they read the NCP
payload and the two vendored vocabularies — so they live here instead:

    from tools import kpstoryform
    for result in kpstoryform.run_all(ncp):
        print(result.row, result.name, result.passed, result.violations)

Thirteen rows. Eleven are structural checks over
``ncp["storyform"]["throughlines"]``; two validate every ``appreciation`` and
``narrative_function`` string in the payload against the canonical enums of
the vendored NCP v1.3.0 schema (463 and 144 values).

Row 8 is advisory: an approach that disagrees with its class is a soft signal,
so it reports a warning and still passes. Every other row's violation is a
structural defect.

Storyform B's heterodox rows are Canon-Lock. The checker names them like any
other finding; the project decided deliberately to keep them, and a run that
reports them is working correctly. See the `dramatica` skill.

Vendored data, both read once and cached:

* ``ncp-schema-v1.3.0.json`` — the two canonical vocabularies.
* ``ontology.json`` — 303 Dramatica entries, used by :func:`resolve_term` to
  look a term up by slug regardless of the caller's kind prefix. NCP payloads
  write ``el.self-interest`` where the ontology stores ``var.self-interest``;
  the slug matches and the entry is returned with ``exact_kind_match`` False.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator

DATA = Path(__file__).resolve().parent
SCHEMA_FILE = "ncp-schema-v1.3.0.json"
ONTOLOGY_FILE = "ontology.json"

# The canonical Dramatica signpost sequence for each class.
CANONICAL_SIGNPOST_ORDER = {
    "class.universe": ["t.past", "t.progress", "t.future", "t.present"],
    "class.physics": ["t.learning", "t.doing", "t.obtaining", "t.understanding"],
    "class.mind": ["t.memory", "t.preconscious", "t.subconscious", "t.conscious"],
    "class.psychology": ["t.conceptualizing", "t.being", "t.becoming", "t.conceiving"],
}

# The four canonical Dramatica endings as (mc.resolve, os.outcome, os.judgment).
LEGAL_ENDINGS = {
    ("change", "success", "good"),        # Triumph
    ("steadfast", "failure", "bad"),      # Tragedy
    ("steadfast", "failure", "good"),     # Personal Triumph
    ("change", "success", "bad"),         # Personal Tragedy
}

DOER_CLASSES = {"class.universe", "class.physics"}
BEER_CLASSES = {"class.mind", "class.psychology"}
REQUIRED_SLOTS = ("class_id", "concern_id", "approach", "mental_sex", "resolve")
THROUGHLINES = {"mc", "os", "ic", "rs"}

KIND_PREFIX = {"el": "element", "var": "variation", "t": "type", "type": "type",
               "dp": "dynamic-pair", "quad": "quad", "class": "class",
               "arc": "archetype", "pd": "plot-dynamic", "cd": "character-dynamic",
               "th": "throughline", "con": "concept"}


@dataclass
class CheckResult:
    """One row's verdict. ``warnings`` never block; ``violations`` do."""

    row: int
    name: str
    passed: bool
    violations: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


# --- vendored data ------------------------------------------------------------------


@lru_cache(maxsize=1)
def _schema() -> dict:
    return json.loads((DATA / SCHEMA_FILE).read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def canonical_appreciations() -> frozenset[str]:
    """The canonical NCP appreciations from the vendored schema."""
    return frozenset(_schema().get("$defs", {}).get("canonical_appreciation", {}).get("enum", []))


@lru_cache(maxsize=1)
def canonical_narrative_functions() -> frozenset[str]:
    """The canonical NCP narrative_function values from the vendored schema."""
    return frozenset(_schema().get("$defs", {}).get("canonical_narrative_function", {}).get("enum", []))


@lru_cache(maxsize=1)
def _ontology_by_slug() -> dict[str, list[dict]]:
    entries = json.loads((DATA / ONTOLOGY_FILE).read_text(encoding="utf-8"))["entries"]
    by_slug: dict[str, list[dict]] = {}
    for entry in entries:
        identifier = entry.get("id", "")
        by_slug.setdefault(identifier.split(".", 1)[1] if "." in identifier else identifier,
                           []).append(entry)
    return by_slug


def resolve_term(term_id: str) -> tuple[dict | None, bool]:
    """``(entry, exact_kind_match)`` for a Dramatica term, matched by slug."""
    if not term_id or "." not in term_id:
        return None, False
    prefix, slug = term_id.split(".", 1)
    entries = _ontology_by_slug().get(slug, [])
    if not entries:
        return None, False
    expected = KIND_PREFIX.get(prefix)
    for entry in entries:
        if entry.get("kind") == expected:
            return entry, True
    return entries[0], False


def walk_field(obj: Any, field_name: str, path: str = "") -> Iterator[tuple[str, str]]:
    """Yield ``(path, value)`` for every ``field_name`` string in a nested payload."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            child = f"{path}.{key}" if path else key
            if key == field_name and isinstance(value, str):
                yield child, value
            else:
                yield from walk_field(value, field_name, child)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from walk_field(item, field_name, f"{path}[{index}]")


def throughlines(ncp: dict) -> dict[str, dict]:
    return (ncp.get("storyform") or {}).get("throughlines") or {}


def _slug(term: str) -> str:
    return term.split(".", 1)[-1]


# --- the structural rows ------------------------------------------------------------


def check_dynamic_pair_reciprocity(ncp: dict) -> CheckResult:
    """Row 1: the mc/os and ic/rs pairs must sit on opposite ends of their axis."""
    tls, violations = throughlines(ncp), []
    for left, right in (("mc", "os"), ("ic", "rs")):
        a = (tls.get(left) or {}).get("dynamic")
        b = (tls.get(right) or {}).get("dynamic")
        if a and b and a == b:
            violations.append(f"row1: {left}.dynamic == {right}.dynamic ({a!r}); pair must be antipodes")
    return CheckResult(1, "dynamic_pair_reciprocity", not violations, violations)


def check_ktad_coverage(ncp: dict) -> CheckResult:
    """Row 2: each throughline's concern must sit at its first signpost."""
    violations = []
    for name, body in throughlines(ncp).items():
        concern, signposts = body.get("concern_id"), body.get("signposts") or []
        if concern and signposts and signposts[0] != concern:
            violations.append(f"row2: {name}.concern_id={concern!r} != signposts[0]={signposts[0]!r}")
    return CheckResult(2, "ktad_coverage", not violations, violations)


def check_quad_completeness(ncp: dict) -> CheckResult:
    """Row 3: the main character's problem and solution must be a dynamic pair."""
    mc, violations = throughlines(ncp).get("mc") or {}, []
    problem, solution = mc.get("problem_id"), mc.get("solution_id")
    if problem and solution:
        problem_entry, _ = resolve_term(problem)
        solution_entry, _ = resolve_term(solution)
        if problem_entry and solution_entry:
            paired = _slug(problem_entry.get("dynamic_pair_id") or "")
            actual = _slug(solution_entry.get("id") or "")
            if paired and actual and paired != actual:
                violations.append(f"row3: mc.problem={problem!r} pairs with "
                                  f"{problem_entry.get('dynamic_pair_id')!r}, not solution={solution!r}")
    return CheckResult(3, "quad_completeness", not violations, violations)


def check_slot_fill(ncp: dict) -> CheckResult:
    """Row 4: a required slot may be absent, but never explicitly null."""
    violations = []
    for name, body in throughlines(ncp).items():
        for slot in REQUIRED_SLOTS:
            if slot in body and body.get(slot) is None:
                violations.append(f"row4: {name}.{slot} is null (use omission, not null)")
    return CheckResult(4, "slot_fill", not violations, violations)


def check_throughline_partition(ncp: dict) -> CheckResult:
    """Row 5: exactly the four throughlines, each holding a distinct class."""
    tls = throughlines(ncp)
    violations: list[str] = []
    actual = set(tls)
    if actual != THROUGHLINES:
        if THROUGHLINES - actual:
            violations.append(f"H1: missing throughlines {sorted(THROUGHLINES - actual)}")
        if actual - THROUGHLINES:
            violations.append(f"H1: unexpected throughlines {sorted(actual - THROUGHLINES)}")
    classes = [body.get("class_id") for body in tls.values() if body.get("class_id")]
    duplicated = sorted({c for c in classes if classes.count(c) > 1})
    if duplicated:
        violations.append(f"H2: class reuse {duplicated}")
    if len(tls) == 4 and len(classes) < 4:
        violations.append("H2: missing class_id on some throughlines")
    return CheckResult(5, "throughline_partition", not violations, violations)


def check_crucial_element_placement(ncp: dict) -> CheckResult:
    """Row 6: the crucial element sits on the main character's problem."""
    story = ncp.get("storyform") or {}
    crucial = story.get("crucial_element_id")
    mc_problem = (throughlines(ncp).get("mc") or {}).get("problem_id")
    violations = []
    if crucial and mc_problem and _slug(crucial) != _slug(mc_problem):
        violations.append(f"row6: crucial_element_id={crucial!r} != mc.problem_id={mc_problem!r}")
    return CheckResult(6, "crucial_element_placement", not violations, violations)


def check_resolve_outcome_judgment(ncp: dict) -> CheckResult:
    """Row 7: resolve/outcome/judgment must form one of the four canonical endings."""
    tls = throughlines(ncp)
    triple = ((tls.get("mc") or {}).get("resolve"), (tls.get("os") or {}).get("outcome"),
              (tls.get("os") or {}).get("judgment"))
    violations = []
    if all(triple) and triple not in LEGAL_ENDINGS:
        violations.append(f"row7: triple (resolve={triple[0]!r}, outcome={triple[1]!r}, "
                          f"judgment={triple[2]!r}) is not a canonical Dramatica ending")
    return CheckResult(7, "resolve_outcome_judgment", not violations, violations)


def check_approach_concern(ncp: dict) -> CheckResult:
    """Row 8 (advisory): do-er pairs with universe/physics, be-er with mind/psychology."""
    mc = throughlines(ncp).get("mc") or {}
    approach, klass = mc.get("approach"), mc.get("class_id")
    warnings = []
    if approach == "do-er" and klass and klass not in DOER_CLASSES:
        warnings.append(f"row8: approach=do-er but class={klass!r} (expected universe/physics)")
    elif approach == "be-er" and klass and klass not in BEER_CLASSES:
        warnings.append(f"row8: approach=be-er but class={klass!r} (expected mind/psychology)")
    return CheckResult(8, "approach_concern", True, [], warnings)


def check_mental_sex_problem_solving(ncp: dict) -> CheckResult:
    """Row 9: linear problem-solving pairs with universe/physics, holistic with mind/psychology."""
    mc = throughlines(ncp).get("mc") or {}
    mental_sex, klass = mc.get("mental_sex"), mc.get("class_id")
    violations = []
    if mental_sex == "linear" and klass and klass not in DOER_CLASSES:
        violations.append(f"row9: mental_sex=linear but class={klass!r}")
    elif mental_sex == "holistic" and klass and klass not in BEER_CLASSES:
        violations.append(f"row9: mental_sex=holistic but class={klass!r}")
    return CheckResult(9, "mental_sex_problem_solving", not violations, violations)


def check_signpost_permutation(ncp: dict) -> CheckResult:
    """Row 10: each throughline's signposts follow its class's canonical order."""
    violations = []
    for name, body in throughlines(ncp).items():
        klass, signposts = body.get("class_id"), body.get("signposts") or []
        expected = CANONICAL_SIGNPOST_ORDER.get(klass)
        if expected and signposts and list(signposts) != expected:
            violations.append(f"row10: {name}.signposts={list(signposts)!r} "
                              f"not canonical order for {klass!r}")
    return CheckResult(10, "signpost_permutation", not violations, violations)


def check_storybeat_moment_refs(ncp: dict) -> CheckResult:
    """Row 11: every moment's storybeat_ref resolves to a declared storybeat."""
    beat_ids = {b.get("id") for b in (ncp.get("storybeats") or []) if b.get("id")}
    violations = []
    for index, moment in enumerate(ncp.get("moments") or []):
        ref = moment.get("storybeat_ref")
        if ref and ref not in beat_ids:
            violations.append(f"row11: moments[{index}].storybeat_ref={ref!r} dangling")
    return CheckResult(11, "storybeat_moment_refs", not violations, violations)


# --- the vocabulary rows ------------------------------------------------------------


def _validate_vocabulary(ncp: dict, field_name: str, canonical: frozenset[str],
                         row: int, name: str) -> CheckResult:
    violations = [f"{name}: {path} = {value!r} is not canonical"
                  for path, value in walk_field(ncp, field_name) if value not in canonical]
    return CheckResult(row, name, not violations, violations)


def validate_appreciations(ncp: dict) -> CheckResult:
    """Row 12: every ``appreciation`` belongs to the canonical vocabulary."""
    return _validate_vocabulary(ncp, "appreciation", canonical_appreciations(), 12, "appreciations")


def validate_narrative_functions(ncp: dict) -> CheckResult:
    """Row 13: every ``narrative_function`` belongs to the canonical vocabulary."""
    return _validate_vocabulary(ncp, "narrative_function", canonical_narrative_functions(),
                                13, "narrative_functions")


CHECKS = (check_dynamic_pair_reciprocity, check_ktad_coverage, check_quad_completeness,
          check_slot_fill, check_throughline_partition, check_crucial_element_placement,
          check_resolve_outcome_judgment, check_approach_concern,
          check_mental_sex_problem_solving, check_signpost_permutation,
          check_storybeat_moment_refs, validate_appreciations, validate_narrative_functions)


def run_all(ncp: dict) -> list[CheckResult]:
    """Every row, in row order."""
    return sorted((check(ncp) for check in CHECKS), key=lambda r: r.row)


def summarise(results: list[CheckResult]) -> dict:
    """Counts plus the flat violation and warning lists, for a report or JSON."""
    return {
        "rows": len(results),
        "passed": sum(1 for r in results if r.passed),
        "failed": [r.name for r in results if not r.passed],
        "violations": [v for r in results for v in r.violations],
        "warnings": [w for r in results for w in r.warnings],
    }
