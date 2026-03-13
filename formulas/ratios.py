"""Mixing ratio calculations for dye formulas."""


def normalize_ratios(ratios):
    """Normalize a list of ratios so they sum to 1.0."""
    total = sum(ratios)
    if total == 0:
        raise ValueError("ratios cannot all be zero")
    return [r / total for r in ratios]


def scale_recipe(base_amounts, scale_factor):
    """Scale a recipe by a factor."""
    return [a * scale_factor for a in base_amounts]


def parts_to_percentages(parts):
    """Convert parts notation to percentages."""
    total = sum(parts)
    if total == 0:
        return [0.0] * len(parts)
    return [p / total * 100 for p in parts]


def grams_per_liter(mass_grams, volume_liters):
    """Calculate concentration in grams per liter."""
    if volume_liters <= 0:
        raise ValueError("volume must be positive")
    return mass_grams / volume_liters


def recipe_cost(amounts, unit_prices):
    """Calculate total cost from amounts and unit prices."""
    return sum(a * p for a, p in zip(amounts, unit_prices))
