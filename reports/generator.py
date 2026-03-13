"""Generate formatted reports from workshop data."""

from reports.formatter import format_vat_summary, format_transfer, format_balance
from reports.statistics import (
    average_transfer_amount,
    total_pigment_moved,
    transfer_count_by_vat,
)


def generate_workshop_report(workshop):
    """Generate a comprehensive workshop report."""
    lines = ["=== Dye Workshop Report ===", ""]

    lines.append("-- Vats --")
    for vat in workshop.vats():
        lines.append(f"  {format_vat_summary(vat)}")
    lines.append("")

    lines.append("-- Transfer History --")
    for t in workshop.mix_entries():
        lines.append(f"  {format_transfer(t)}")
    lines.append("")

    inflows, outflows = workshop.pigment_balance()
    lines.append(f"-- Balance: {format_balance(inflows, outflows)} --")

    avg = average_transfer_amount(workshop)
    total = total_pigment_moved(workshop)
    lines.append(f"-- Stats: avg={avg:.1f}mL, total={total}mL --")

    return "\n".join(lines)


def generate_vat_report(workshop, vat_name):
    """Generate a report for a specific vat."""
    vat = workshop.get_vat(vat_name)
    lines = [f"=== Vat Report: {vat.name} ==="]
    lines.append(f"Kind: {vat.kind}")
    lines.append(f"Pigment level: {vat.pigment_level}mL")
    lines.append(f"Transfers: {len(vat.transfers())}")
    lines.append("")
    for t in vat.transfers():
        lines.append(f"  {format_transfer(t)}")
    return "\n".join(lines)
