"""Unit tests for utility modules."""

from utils.validation import validate_vat_name, validate_amount, validate_vat_kind
from utils.formatting import truncate, format_table
from utils.aggregation import sum_by_dest, net_flow_per_vat
from workshop import Workshop


def test_validate_vat_name():
    """Valid name passes."""
    assert validate_vat_name("crimson") == "crimson"


def test_validate_vat_name_empty():
    """Empty name fails."""
    try:
        validate_vat_name("")
        assert False
    except ValueError:
        pass


def test_validate_amount():
    """Positive amount passes."""
    assert validate_amount(100) == 100


def test_validate_amount_negative():
    """Negative amount fails."""
    try:
        validate_amount(-5)
        assert False
    except ValueError:
        pass


def test_validate_vat_kind():
    """Standard and overflow are valid."""
    assert validate_vat_kind("standard") == "standard"
    assert validate_vat_kind("overflow") == "overflow"


def test_validate_vat_kind_invalid():
    """Invalid kind raises ValueError."""
    try:
        validate_vat_kind("magic")
        assert False
    except ValueError:
        pass


def test_truncate():
    """Long text is truncated with ellipsis."""
    assert truncate("hello", 10) == "hello"
    assert len(truncate("a" * 100, 20)) == 20


def test_format_table():
    """Table formats with headers and rows."""
    result = format_table(["Name", "Value"], [["a", "1"], ["b", "2"]])
    assert "Name" in result
    assert "a" in result


def test_sum_by_dest():
    """Sum pigment by destination vat."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100)
    ws.pour("a", "b", 200)
    totals = sum_by_dest(ws)
    assert totals["a"] == 300


def test_net_flow():
    """Net flow per vat."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100)
    flows = net_flow_per_vat(ws)
    assert flows["a"] == 100
    assert flows["b"] == -100
