"""Pigment concentration and dilution calculations."""

import math


def dilution_ratio(current_concentration, target_concentration, volume):
    """Calculate the amount of solvent needed to dilute pigment.

    Returns the volume of solvent to add to reach target concentration.
    """
    if target_concentration <= 0 or current_concentration <= 0:
        raise ValueError("concentrations must be positive")
    if target_concentration >= current_concentration:
        return 0
    return volume * (current_concentration / target_concentration - 1)


def concentration_after_mix(conc1, vol1, conc2, vol2):
    """Calculate resulting concentration after mixing two solutions."""
    total_volume = vol1 + vol2
    if total_volume == 0:
        return 0
    return (conc1 * vol1 + conc2 * vol2) / total_volume


def is_saturated(concentration, max_solubility):
    """Check if a solution is at or above saturation point."""
    return concentration >= max_solubility


def evaporation_loss(volume, rate, hours):
    """Estimate pigment volume after evaporation."""
    return volume * math.exp(-rate * hours)


def required_pigment(target_concentration, target_volume):
    """Calculate raw pigment needed for a target solution."""
    return target_concentration * target_volume
