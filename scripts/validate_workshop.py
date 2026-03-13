"""Validate workshop invariants."""

import sys
sys.path.insert(0, ".")

from scripts.seed_data import seed_medium


def validate(workshop):
    """Check core workshop invariants."""
    errors = []

    # Balance check
    inflows, outflows = workshop.pigment_balance()
    if inflows != outflows:
        errors.append(f"Imbalanced: in={inflows}, out={outflows}")

    # Transfer ID uniqueness
    ids = [t.id for t in workshop.mix_entries()]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate transfer IDs found")

    # Sequential IDs
    for i, tid in enumerate(ids, 1):
        if tid != i:
            errors.append(f"Non-sequential ID: expected {i}, got {tid}")
            break

    # Vat level consistency
    for vat in workshop.vats():
        level = vat.pigment_level
        computed = 0
        for t in vat.transfers():
            if t.dest_vat is vat:
                computed += t.amount
            elif t.source_vat is vat:
                computed -= t.amount
        if level != computed:
            errors.append(f"Vat {vat.name}: level={level} != computed={computed}")

    return errors


if __name__ == "__main__":
    ws = seed_medium()
    errors = validate(ws)
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("All invariants OK")
