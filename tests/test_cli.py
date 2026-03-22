from pathlib import Path

from usina.cli import main
from usina.core import lint, load_yaml, validate_schema

FIXTURES = Path(__file__).parent / "fixtures"


def test_schema_validation_passes_for_valid_fixture():
    doc = load_yaml(FIXTURES / "valid" / "minimal_valid.usina.yaml")
    assert validate_schema(doc) == []


def test_lint_passes_for_valid_fixture():
    doc = load_yaml(FIXTURES / "valid" / "minimal_valid.usina.yaml")
    assert lint(doc) == []


def test_lint_detects_overlap_fixture():
    doc = load_yaml(FIXTURES / "invalid" / "timeline_overlap.usina.yaml")
    problems = lint(doc)
    codes = {p.code for p in problems}
    assert "USINA-LINT-002" in codes


def test_validate_command_returns_zero_for_valid_fixture():
    rc = main(["validate", str(FIXTURES / "valid" / "minimal_valid.usina.yaml")])
    assert rc == 0


def test_lint_command_returns_nonzero_for_invalid_fixture():
    rc = main(["lint", str(FIXTURES / "invalid" / "timeline_overlap.usina.yaml")])
    assert rc == 1
