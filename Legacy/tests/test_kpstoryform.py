"""Tests for tools/kpstoryform: the decidable Dramatica rows over an NCP payload."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from tools import kpstoryform  # noqa: E402
import storyform_check  # noqa: E402

# A storyform that passes every row: four throughlines, four distinct classes,
# canonical signposts, a legal ending, a paired problem/solution.
GOOD = {
    "storyform": {
        "crucial_element_id": "el.avoid",
        "throughlines": {
            "mc": {"class_id": "class.universe", "concern_id": "t.past",
                   "signposts": ["t.past", "t.progress", "t.future", "t.present"],
                   "approach": "do-er", "mental_sex": "linear", "resolve": "change",
                   "dynamic": "thought", "problem_id": "el.avoid", "solution_id": "el.pursuit"},
            "os": {"class_id": "class.physics", "concern_id": "t.learning",
                   "signposts": ["t.learning", "t.doing", "t.obtaining", "t.understanding"],
                   "dynamic": "knowledge", "outcome": "success", "judgment": "good"},
            "ic": {"class_id": "class.mind", "concern_id": "t.memory",
                   "signposts": ["t.memory", "t.preconscious", "t.subconscious", "t.conscious"],
                   "dynamic": "thought"},
            "rs": {"class_id": "class.psychology", "concern_id": "t.conceptualizing",
                   "signposts": ["t.conceptualizing", "t.being", "t.becoming", "t.conceiving"],
                   "dynamic": "knowledge"},
        },
    },
    "storybeats": [{"id": "sb.1"}],
    "moments": [{"storybeat_ref": "sb.1"}],
}


def rows(ncp: dict) -> dict[str, kpstoryform.CheckResult]:
    return {r.name: r for r in kpstoryform.run_all(ncp)}


def mutate(**path_values) -> dict:
    """A copy of GOOD with `mc__field=value` style overrides applied."""
    ncp = copy.deepcopy(GOOD)
    for key, value in path_values.items():
        throughline, field = key.split("__", 1)
        ncp["storyform"]["throughlines"][throughline][field] = value
    return ncp


def test_the_good_storyform_passes_every_row():
    results = kpstoryform.run_all(GOOD)
    assert [r.row for r in results] == list(range(1, 14))
    assert kpstoryform.summarise(results)["failed"] == []


def test_a_shared_dynamic_collapses_the_pair():
    result = rows(mutate(os__dynamic="thought"))["dynamic_pair_reciprocity"]
    assert not result.passed and "antipodes" in result.violations[0]


def test_a_concern_away_from_its_first_signpost_fails():
    result = rows(mutate(mc__concern_id="t.future"))["ktad_coverage"]
    assert not result.passed and "signposts[0]" in result.violations[0]


def test_an_unpaired_problem_and_solution_fail():
    result = rows(mutate(mc__solution_id="el.faith"))["quad_completeness"]
    assert not result.passed and "pairs with" in result.violations[0]


def test_an_explicit_null_slot_fails_but_an_absent_one_does_not():
    assert not rows(mutate(mc__resolve=None))["slot_fill"].passed
    absent = copy.deepcopy(GOOD)
    del absent["storyform"]["throughlines"]["mc"]["resolve"]
    assert rows(absent)["slot_fill"].passed


def test_a_missing_throughline_and_a_reused_class_both_fail():
    missing = copy.deepcopy(GOOD)
    del missing["storyform"]["throughlines"]["rs"]
    assert "H1: missing throughlines ['rs']" in rows(missing)["throughline_partition"].violations
    reused = rows(mutate(os__class_id="class.universe"))["throughline_partition"]
    assert any("class reuse" in v for v in reused.violations)


def test_a_crucial_element_off_the_mc_problem_fails():
    ncp = copy.deepcopy(GOOD)
    ncp["storyform"]["crucial_element_id"] = "el.pursuit"
    assert not rows(ncp)["crucial_element_placement"].passed


def test_only_the_four_canonical_endings_pass():
    assert rows(GOOD)["resolve_outcome_judgment"].passed
    assert not rows(mutate(os__judgment="bad", mc__resolve="steadfast"))["resolve_outcome_judgment"].passed


def test_approach_mismatch_warns_without_failing():
    result = rows(mutate(mc__approach="be-er"))["approach_concern"]
    assert result.passed and result.warnings and "expected mind/psychology" in result.warnings[0]


def test_mental_sex_mismatch_is_a_violation_not_a_warning():
    result = rows(mutate(mc__mental_sex="holistic"))["mental_sex_problem_solving"]
    assert not result.passed and "class.universe" in result.violations[0]


def test_reordered_signposts_fail():
    result = rows(mutate(mc__signposts=["t.past", "t.present", "t.progress", "t.future"]))
    assert not result["signpost_permutation"].passed


def test_a_dangling_moment_reference_fails():
    ncp = copy.deepcopy(GOOD)
    ncp["moments"] = [{"storybeat_ref": "sb.missing"}]
    assert not rows(ncp)["storybeat_moment_refs"].passed


def test_the_two_vocabularies_load_and_gate():
    assert len(kpstoryform.canonical_appreciations()) == 463
    assert len(kpstoryform.canonical_narrative_functions()) == 144
    ncp = copy.deepcopy(GOOD)
    ncp["cast"] = [{"appreciation": "not-a-real-appreciation"}]
    assert not rows(ncp)["appreciations"].passed


def test_narrative_functions_are_gated_the_same_way():
    ncp = copy.deepcopy(GOOD)
    ncp["cast"] = [{"narrative_function": "not-a-real-function"}]
    result = rows(ncp)["narrative_functions"]
    assert not result.passed and "not canonical" in result.violations[0]


def test_resolve_term_is_kind_agnostic():
    entry, exact = kpstoryform.resolve_term("el.avoid")
    assert entry is not None and exact is True
    assert kpstoryform.resolve_term("nonsense")[0] is None
    assert kpstoryform.resolve_term("el.does-not-exist")[0] is None


def test_walk_field_finds_nested_values():
    payload = {"a": {"appreciation": "x"}, "b": [{"appreciation": "y"}]}
    assert sorted(kpstoryform.walk_field(payload, "appreciation")) == [
        ("a.appreciation", "x"), ("b[0].appreciation", "y")]


def test_the_repo_storyforms_match_their_recorded_state():
    """A passes every row; B fails exactly its two Canon-Lock signpost rows."""
    a = json.loads(storyform_check.ncp_path("ncp.json").read_text(encoding="utf-8"))
    b = json.loads(storyform_check.ncp_path("ncp-b.json").read_text(encoding="utf-8"))
    assert kpstoryform.summarise(kpstoryform.run_all(a))["failed"] == []
    assert kpstoryform.summarise(kpstoryform.run_all(b))["failed"] == [
        "ktad_coverage", "signpost_permutation"]


def test_the_cli_reports_both_storyforms(capsys):
    assert storyform_check.main([]) == storyform_check.EXIT_OK
    out = capsys.readouterr().out
    assert "13/13 rows pass" in out and "11/13 rows pass" in out


def test_strict_turns_a_failing_row_into_exit_1(capsys):
    assert storyform_check.main(["--ncp", "ncp-b.json", "--strict"]) == storyform_check.EXIT_VIOLATION
    assert storyform_check.main(["--ncp", "ncp.json", "--strict"]) == storyform_check.EXIT_OK


def test_a_missing_storyform_exits_2(capsys):
    assert storyform_check.main(["--ncp", "absent.json"]) == storyform_check.EXIT_CANNOT_RUN
    assert "no storyform at" in capsys.readouterr().err
