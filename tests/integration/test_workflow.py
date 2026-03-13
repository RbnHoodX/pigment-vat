"""Integration tests for end-to-end workshop workflows."""

from workshop import Workshop
from storage.serializer import serialize_workshop, to_json
from reports.generator import generate_workshop_report

import json


def test_full_create_pour_report():
    """Full workflow: create vats, pour pigment, generate report."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 500, "initial stock")
    ws.pour("crimson", "reservoir", 200, "top up")
    report = generate_workshop_report(ws)
    assert "crimson" in report
    assert "700" in report or "0.7L" in report


def test_serialize_roundtrip():
    """Workshop state can be serialized to JSON and parsed back."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100, "test")
    data = json.loads(to_json(ws))
    assert data["vats"][0]["name"] == "a"
    assert data["transfers"][0]["amount"] == 100


def test_validation_passes_on_normal_workshop():
    """A normally-used workshop passes validation."""
    from scripts.validate_workshop import validate
    from scripts.seed_data import seed_medium
    ws = seed_medium()
    errors = validate(ws)
    assert errors == []


def test_multiple_pours_consistent():
    """Multiple pours keep balance consistent."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("indigo")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 500)
    ws.pour("indigo", "reservoir", 300)
    ws.pour("indigo", "crimson", 100)
    inflows, outflows = ws.pigment_balance()
    assert inflows == outflows
    assert ws.get_vat("crimson").pigment_level == 400
    assert ws.get_vat("indigo").pigment_level == 400
    assert ws.get_vat("reservoir").pigment_level == -800
