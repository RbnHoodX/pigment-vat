"""Configuration constants for the dye workshop."""

# Default vat kinds
STANDARD_VAT = "standard"
OVERFLOW_VAT = "overflow"

# Valid vat kinds
VALID_KINDS = {STANDARD_VAT, OVERFLOW_VAT}

# Precision for pigment measurements (decimal places)
PIGMENT_PRECISION = 2

# Maximum pigment level warning threshold
MAX_PIGMENT_WARNING = 10000

# Default note for manual transfers
DEFAULT_NOTE = ""
