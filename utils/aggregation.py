"""Aggregation utilities for workshop analytics."""


def group_transfers_by_note(workshop):
    """Group transfers by their note field."""
    groups = {}
    for t in workshop.mix_entries():
        key = t.note or "(none)"
        groups.setdefault(key, []).append(t)
    return groups


def sum_by_dest(workshop):
    """Sum total pigment received by each destination vat."""
    totals = {}
    for t in workshop.mix_entries():
        name = t.dest_vat.name
        totals[name] = totals.get(name, 0) + t.amount
    return totals


def sum_by_source(workshop):
    """Sum total pigment sent from each source vat."""
    totals = {}
    for t in workshop.mix_entries():
        name = t.source_vat.name
        totals[name] = totals.get(name, 0) + t.amount
    return totals


def net_flow_per_vat(workshop):
    """Calculate net pigment flow per vat (positive = net inflow)."""
    inflows = sum_by_dest(workshop)
    outflows = sum_by_source(workshop)
    all_names = set(inflows) | set(outflows)
    return {
        name: inflows.get(name, 0) - outflows.get(name, 0)
        for name in all_names
    }
