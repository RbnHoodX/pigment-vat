"""Unit tests for the Vat class."""

from vat import Vat


def test_vat_creation():
    """Vat stores name and kind."""
    v = Vat("crimson", "standard")
    assert v.name == "crimson"
    assert v.kind == "standard"


def test_vat_default_kind():
    """Vat defaults to standard kind."""
    v = Vat("crimson")
    assert v.kind == "standard"


def test_vat_initial_pigment_level():
    """New vat has zero pigment level."""
    v = Vat("crimson")
    assert v.pigment_level == 0


def test_vat_initial_transfers():
    """New vat has no transfers."""
    v = Vat("crimson")
    assert v.transfers() == []


def test_vat_repr():
    """Vat repr includes name and kind."""
    v = Vat("crimson", "overflow")
    assert "crimson" in repr(v)
    assert "overflow" in repr(v)
