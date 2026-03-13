"""Temperature effects on dye processes."""


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def optimal_dye_temp(dye_type):
    """Return optimal temperature range for a dye type."""
    ranges = {
        "reactive": (30, 60),
        "acid": (85, 100),
        "disperse": (120, 140),
        "vat": (50, 70),
        "direct": (70, 95),
    }
    return ranges.get(dye_type, (20, 100))


def temp_correction_factor(current_temp, optimal_temp):
    """Calculate efficiency correction factor based on temperature deviation."""
    deviation = abs(current_temp - optimal_temp)
    if deviation <= 5:
        return 1.0
    elif deviation <= 15:
        return 0.85
    elif deviation <= 30:
        return 0.65
    else:
        return 0.4


def heat_required(volume_liters, temp_rise, specific_heat=4.186):
    """Calculate heat energy needed in kilojoules."""
    return volume_liters * temp_rise * specific_heat
