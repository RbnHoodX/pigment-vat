"""Unit tests for report generation."""

from workshop import Workshop
from reports.generator import generate_workshop_report, generate_vat_report
from reports.formatter import format_pigment_level, format_transfer
from reports.statistics import average_transfer_amount, total_pigment_moved, busiest_vat


def test_generate_workshop_report():
    """Workshop report includes vat and transfer info."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100, "test")
    report = generate_workshop_report(ws)
    assert "crimson" in report
    assert "reservoir" in report


def test_generate_vat_report():
    """Vat report includes vat details."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100, "test")
    report = generate_vat_report(ws, "crimson")
    assert "crimson" in report


def test_format_pigment_level_small():
    """Small levels formatted in mL."""
    assert format_pigment_level(500) == "500mL"


def test_format_pigment_level_large():
    """Large levels formatted in L."""
    assert format_pigment_level(1500) == "1.5L"


def test_average_transfer_amount():
    """Average transfer calculation."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100)
    ws.pour("a", "b", 200)
    assert average_transfer_amount(ws) == 150.0


def test_total_pigment_moved():
    """Total pigment moved through system."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100)
    ws.pour("a", "b", 200)
    assert total_pigment_moved(ws) == 300


def test_busiest_vat():
    """Busiest vat has most transfers."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b")
    ws.create_vat("c", "overflow")
    ws.pour("a", "c", 100)
    ws.pour("b", "c", 100)
    ws.pour("a", "c", 50)
    result = busiest_vat(ws)
    assert result == "c"
