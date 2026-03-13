"""Format workshop data for display."""


def format_pigment_level(level):
    """Format a pigment level with units."""
    if level >= 1000:
        return f"{level / 1000:.1f}L"
    return f"{level}mL"


def format_transfer(transfer):
    """Format a single transfer for display."""
    note_part = f" ({transfer.note})" if transfer.note else ""
    return (f"#{transfer.id}: {transfer.source_vat.name} -> "
            f"{transfer.dest_vat.name} [{transfer.amount}mL]{note_part}")


def format_vat_summary(vat):
    """Format a vat summary line."""
    level = format_pigment_level(vat.pigment_level)
    return f"{vat.name} [{vat.kind}]: {level} ({len(vat.transfers())} transfers)"


def format_balance(inflows, outflows):
    """Format the pigment balance."""
    status = "balanced" if inflows == outflows else "IMBALANCED"
    return f"In: {inflows}mL | Out: {outflows}mL | Status: {status}"
