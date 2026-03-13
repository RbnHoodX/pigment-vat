"""Seed a workshop with sample data for development."""

import sys
sys.path.insert(0, ".")

from workshop import Workshop


def seed_small():
    """Create a small workshop with basic vats."""
    ws = Workshop()
    ws.create_vat("crimson", "standard")
    ws.create_vat("indigo", "standard")
    ws.create_vat("reservoir", "overflow")
    ws.pour("crimson", "reservoir", 500, "initial stock")
    ws.pour("indigo", "reservoir", 300, "initial stock")
    return ws


def seed_medium():
    """Create a medium workshop with several vats and transfers."""
    ws = Workshop()
    ws.create_vat("crimson", "standard")
    ws.create_vat("indigo", "standard")
    ws.create_vat("ochre", "standard")
    ws.create_vat("emerald", "standard")
    ws.create_vat("reservoir", "overflow")
    ws.create_vat("waste", "overflow")

    ws.pour("crimson", "reservoir", 500, "initial")
    ws.pour("indigo", "reservoir", 400, "initial")
    ws.pour("ochre", "reservoir", 350, "initial")
    ws.pour("emerald", "reservoir", 200, "initial")

    ws.pour("indigo", "crimson", 100, "blend test")
    ws.pour("ochre", "indigo", 50, "correction")
    ws.pour("waste", "ochre", 25, "drain excess")
    return ws


if __name__ == "__main__":
    ws = seed_medium()
    print(f"Seeded workshop with {len(ws.vats())} vats, {len(ws.mix_entries())} transfers")
    for v in ws.vats():
        print(f"  {v.name}: {v.pigment_level}mL ({v.kind})")
