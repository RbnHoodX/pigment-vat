"""Export workshop data to various formats."""

import csv
import io


def export_vats_csv(workshop):
    """Export vat data as CSV string."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["name", "kind", "pigment_level"])
    for vat in workshop.vats():
        writer.writerow([vat.name, vat.kind, vat.pigment_level])
    return buf.getvalue()


def export_transfers_csv(workshop):
    """Export transfer history as CSV string."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["id", "dest", "source", "amount", "note"])
    for t in workshop.mix_entries():
        writer.writerow([t.id, t.dest_vat.name, t.source_vat.name, t.amount, t.note])
    return buf.getvalue()


def export_summary(workshop):
    """Generate a text summary of the workshop."""
    lines = [f"Dye Workshop Summary", f"{'=' * 40}"]
    lines.append(f"Vats: {len(workshop.vats())}")
    lines.append(f"Transfers: {len(workshop.mix_entries())}")
    inflows, outflows = workshop.pigment_balance()
    lines.append(f"Pigment balance: in={inflows}, out={outflows}")
    lines.append("")
    for vat in workshop.vats():
        lines.append(f"  {vat.name} ({vat.kind}): {vat.pigment_level}")
    return "\n".join(lines)
