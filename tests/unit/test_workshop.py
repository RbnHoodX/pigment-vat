"""Unit tests for the Workshop class."""

from workshop import Workshop


def test_workshop_creation():
    """Workshop can be created empty."""
    ws = Workshop()
    assert ws.vats() == []
    assert ws.mix_entries() == []


def test_create_vat():
    """Workshop can create vats."""
    ws = Workshop()
    v = ws.create_vat("crimson", "standard")
    assert v.name == "crimson"
    assert v.kind == "standard"
    assert len(ws.vats()) == 1


def test_create_duplicate_vat():
    """Creating a duplicate vat raises ValueError."""
    ws = Workshop()
    ws.create_vat("crimson")
    try:
        ws.create_vat("crimson")
        assert False, "should raise ValueError"
    except ValueError:
        pass


def test_get_vat():
    """get_vat retrieves a vat by name."""
    ws = Workshop()
    ws.create_vat("crimson")
    v = ws.get_vat("crimson")
    assert v.name == "crimson"


def test_pour():
    """pour creates a transfer and updates pigment levels."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    t = ws.pour("crimson", "reservoir", 100, "test")
    assert t.amount == 100
    assert ws.get_vat("crimson").pigment_level == 100
    assert ws.get_vat("reservoir").pigment_level == -100


def test_pour_negative_amount():
    """pour rejects non-positive amounts."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    try:
        ws.pour("crimson", "reservoir", 0)
        assert False, "should raise ValueError"
    except ValueError:
        pass


def test_pigment_balance():
    """pigment_balance returns equal inflows and outflows."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100)
    ws.pour("crimson", "reservoir", 200)
    inflows, outflows = ws.pigment_balance()
    assert inflows == outflows == 300


def test_mix_entries():
    """mix_entries returns all recorded transfers."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100)
    ws.pour("crimson", "reservoir", 200)
    assert len(ws.mix_entries()) == 2
