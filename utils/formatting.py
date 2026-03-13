"""Formatting utilities for display output."""


def truncate(text, max_length=50):
    """Truncate text with ellipsis if too long."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def pad_right(text, width):
    """Pad text to a fixed width."""
    return text.ljust(width)


def pad_left(text, width):
    """Pad text to a fixed width, right-aligned."""
    return text.rjust(width)


def format_table(headers, rows):
    """Format data as a simple text table."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    header_line = " | ".join(h.ljust(w) for h, w in zip(headers, widths))
    separator = "-+-".join("-" * w for w in widths)
    lines = [header_line, separator]
    for row in rows:
        line = " | ".join(str(c).ljust(w) for c, w in zip(row, widths))
        lines.append(line)
    return "\n".join(lines)
