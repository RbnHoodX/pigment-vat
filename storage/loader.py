"""Load workshop state from files."""

import json
from pathlib import Path


def load_vat_config(filepath):
    """Load vat configuration from a JSON file."""
    data = json.loads(Path(filepath).read_text())
    return [
        {"name": v["name"], "kind": v.get("kind", "standard")}
        for v in data.get("vats", [])
    ]


def load_transfer_history(filepath):
    """Load transfer history from a JSON file."""
    data = json.loads(Path(filepath).read_text())
    return data.get("transfers", [])


def validate_config(config):
    """Validate a vat configuration list."""
    names = set()
    for entry in config:
        name = entry.get("name", "")
        if not name:
            raise ValueError("vat name cannot be empty")
        if name in names:
            raise ValueError(f"duplicate vat name: {name!r}")
        names.add(name)
    return True
