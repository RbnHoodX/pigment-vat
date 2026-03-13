"""Search utilities for workshop data."""


def search_vats(workshop, query):
    """Search vats by name (case-insensitive partial match)."""
    q = query.strip().lower()
    return [v for v in workshop.vats() if q in v.name.lower()]


def search_transfers_by_note(workshop, query):
    """Search transfers by note content (case-insensitive)."""
    q = query.strip().lower()
    return [t for t in workshop.mix_entries() if q in t.note.lower()]


def filter_transfers_by_amount(workshop, min_amount=0, max_amount=None):
    """Filter transfers by amount range."""
    results = []
    for t in workshop.mix_entries():
        if t.amount >= min_amount:
            if max_amount is None or t.amount <= max_amount:
                results.append(t)
    return results


def find_transfers_for_vat(workshop, vat_name):
    """Find all transfers involving a specific vat."""
    return [
        t for t in workshop.mix_entries()
        if t.dest_vat.name == vat_name or t.source_vat.name == vat_name
    ]
