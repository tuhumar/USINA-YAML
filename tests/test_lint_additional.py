from pathlib import Path

from usina.core import lint, load_yaml

FIXTURES = Path(__file__).parent / "fixtures" / "invalid"


def _codes(filename: str) -> set[str]:
    doc = load_yaml(FIXTURES / filename)
    return {p.code for p in lint(doc)}


def test_unknown_asset_reference_is_reported():
    assert "USINA-REF-008" in _codes("unknown_asset_ref.usina.yaml")


def test_invalid_citation_reference_is_reported():
    assert "USINA-REF-011" in _codes("invalid_citation_ref.usina.yaml")


def test_duration_mismatch_is_reported():
    assert "USINA-LINT-006" in _codes("duration_mismatch.usina.yaml")


def test_audio_track_out_of_bounds_is_reported():
    assert "USINA-LINT-014" in _codes("audio_track_out_of_bounds.usina.yaml")
