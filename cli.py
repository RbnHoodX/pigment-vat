"""Command-line interface for dye workshop management."""

import sys
from workshop import Workshop


def main():
    """Run the dye workshop CLI."""
    ws = Workshop()
    print("Dye Workshop CLI")
    print("Commands: create <name> [kind], pour <dest> <source> <amount> [note]")
    print("          vats, balance, entries, quit")

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        if cmd == "quit":
            break
        elif cmd == "create":
            if len(parts) < 2:
                print("Usage: create <name> [kind]")
                continue
            name = parts[1]
            kind = parts[2] if len(parts) > 2 else "standard"
            try:
                vat = ws.create_vat(name, kind)
                print(f"Created vat: {vat}")
            except ValueError as e:
                print(f"Error: {e}")
        elif cmd == "pour":
            if len(parts) < 4:
                print("Usage: pour <dest> <source> <amount> [note]")
                continue
            dest, source = parts[1], parts[2]
            try:
                amount = int(parts[3])
            except ValueError:
                print("Amount must be a number")
                continue
            note = " ".join(parts[4:]) if len(parts) > 4 else ""
            try:
                t = ws.pour(dest, source, amount, note)
                print(f"Recorded: {t}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        elif cmd == "vats":
            for v in ws.vats():
                print(f"  {v.name}: {v.pigment_level} ({v.kind})")
        elif cmd == "balance":
            inflows, outflows = ws.pigment_balance()
            print(f"Inflows: {inflows}, Outflows: {outflows}")
        elif cmd == "entries":
            for t in ws.mix_entries():
                print(f"  {t}")
        else:
            print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
