"""Color spectrum analysis for pigment classification."""

# Standard pigment wavelength ranges (nanometers)
WAVELENGTH_RANGES = {
    "red": (620, 750),
    "orange": (590, 620),
    "yellow": (570, 590),
    "green": (495, 570),
    "blue": (450, 495),
    "indigo": (420, 450),
    "violet": (380, 420),
}


def classify_wavelength(nm):
    """Classify a wavelength in nanometers to a color name."""
    for color, (low, high) in WAVELENGTH_RANGES.items():
        if low <= nm <= high:
            return color
    return "unknown"


def complementary_wavelength(nm):
    """Compute the complementary wavelength."""
    if 380 <= nm <= 750:
        return 380 + (750 - nm)
    return None


def is_warm_tone(nm):
    """Determine if a wavelength falls in the warm tone range."""
    return nm >= 570


def is_cool_tone(nm):
    """Determine if a wavelength falls in the cool tone range."""
    return nm < 570


def blend_wavelengths(nm1, nm2, ratio=0.5):
    """Blend two wavelengths at a given ratio."""
    return nm1 * ratio + nm2 * (1 - ratio)


def spectral_distance(nm1, nm2):
    """Calculate the distance between two wavelengths."""
    return abs(nm1 - nm2)
