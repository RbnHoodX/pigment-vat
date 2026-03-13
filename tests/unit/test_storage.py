"""Unit tests for storage modules."""

import json
import tempfile
import os

from workshop import Workshop
from storage.serializer import serialize_vat, serialize_transfer, serialize_workshop, to_json
from storage.exporter import export_vats_csv, export_transfers_csv, export_summary
from storage.loader import load_vat_config, validate_config


def test_serialize_vat():
    """Vat serializes to dict with expected keys."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100)
    data = serialize_vat(ws.get_vat("crimson"))
    assert data["name"] == "crimson"
    assert data["pigment_level"] == 100


def test_serialize_transfer():
    """Transfer serializes to dict."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    t = ws.pour("a", "b", 100, "test")
    data = serialize_transfer(t)
    assert data["amount"] == 100
    assert data["note"] == "test"


def test_to_json():
    """Workshop serializes to valid JSON."""
    ws = Workshop()
    ws.create_vat("a")
    ws.create_vat("b", "overflow")
    ws.pour("a", "b", 100)
    result = to_json(ws)
    parsed = json.loads(result)
    assert len(parsed["vats"]) == 2


def test_export_vats_csv():
    """Vats export to CSV format."""
    ws = Workshop()
    ws.create_vat("crimson")
    csv_str = export_vats_csv(ws)
    assert "crimson" in csv_str
    assert "name" in csv_str


def test_export_summary():
    """Summary export includes key info."""
    ws = Workshop()
    ws.create_vat("crimson")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 100)
    summary = export_summary(ws)
    assert "Vats: 2" in summary


def test_load_vat_config():
    """Load vat config from JSON file."""
    data = {"vats": [{"name": "a"}, {"name": "b", "kind": "overflow"}]}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        f.flush()
        config = load_vat_config(f.name)
    os.unlink(f.name)
    assert len(config) == 2
    assert config[1]["kind"] == "overflow"


def test_validate_config():
    """Valid config passes validation."""
    config = [{"name": "a"}, {"name": "b"}]
    assert validate_config(config) is True


def test_validate_config_duplicate():
    """Duplicate names fail validation."""
    config = [{"name": "a"}, {"name": "a"}]
    try:
        validate_config(config)
        assert False
    except ValueError:
        pass
