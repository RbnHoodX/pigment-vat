"""Statistical analysis of workshop operations."""


def transfer_count_by_vat(workshop):
    """Count transfers per vat."""
    counts = {}
    for vat in workshop.vats():
        counts[vat.name] = len(vat.transfers())
    return counts


def average_transfer_amount(workshop):
    """Calculate the average transfer amount."""
    entries = workshop.mix_entries()
    if not entries:
        return 0
    return sum(t.amount for t in entries) / len(entries)


def max_pigment_level(workshop):
    """Find the vat with the highest pigment level."""
    vats = workshop.vats()
    if not vats:
        return None
    return max(vats, key=lambda v: v.pigment_level)


def min_pigment_level(workshop):
    """Find the vat with the lowest pigment level."""
    vats = workshop.vats()
    if not vats:
        return None
    return min(vats, key=lambda v: v.pigment_level)


def total_pigment_moved(workshop):
    """Calculate total pigment moved through the system."""
    return sum(t.amount for t in workshop.mix_entries())


def busiest_vat(workshop):
    """Find the vat involved in the most transfers."""
    counts = transfer_count_by_vat(workshop)
    if not counts:
        return None
    return max(counts, key=counts.get)
