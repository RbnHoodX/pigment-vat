"""Validation utilities for workshop operations."""


def validate_vat_name(name):
    """Validate a vat name is non-empty and reasonable."""
    if not name or not name.strip():
        raise ValueError("vat name cannot be empty")
    if len(name) > 100:
        raise ValueError("vat name too long")
    return name.strip()


def validate_amount(amount):
    """Validate a transfer amount is positive."""
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if amount <= 0:
        raise ValueError("amount must be positive")
    return amount


def validate_vat_kind(kind):
    """Validate a vat kind."""
    valid = {"standard", "overflow"}
    if kind not in valid:
        raise ValueError(f"invalid vat kind: {kind!r}, must be one of {valid}")
    return kind


def validate_note(note):
    """Validate a transfer note."""
    if not isinstance(note, str):
        raise TypeError("note must be a string")
    if len(note) > 500:
        raise ValueError("note too long")
    return note
