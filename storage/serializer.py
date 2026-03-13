"""Serialize workshop state to portable formats."""

import json


def serialize_vat(vat):
    """Serialize a Vat to a dictionary."""
    return {
        "name": vat.name,
        "kind": vat.kind,
        "pigment_level": vat.pigment_level,
        "transfer_count": len(vat.transfers()),
    }


def serialize_transfer(transfer):
    """Serialize a Transfer to a dictionary."""
    return {
        "id": transfer.id,
        "dest": transfer.dest_vat.name,
        "source": transfer.source_vat.name,
        "amount": transfer.amount,
        "note": transfer.note,
    }


def serialize_workshop(workshop):
    """Serialize entire workshop state."""
    return {
        "vats": [serialize_vat(v) for v in workshop.vats()],
        "transfers": [serialize_transfer(t) for t in workshop.mix_entries()],
        "balance": dict(zip(["inflows", "outflows"], workshop.pigment_balance())),
    }


def to_json(workshop, indent=2):
    """Serialize workshop to JSON string."""
    return json.dumps(serialize_workshop(workshop), indent=indent)
