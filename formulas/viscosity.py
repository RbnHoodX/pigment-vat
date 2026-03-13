"""Viscosity and flow calculations for dye transfer."""

import math


def dynamic_viscosity(shear_stress, shear_rate):
    """Calculate dynamic viscosity from stress and rate."""
    if shear_rate == 0:
        raise ValueError("shear rate cannot be zero")
    return shear_stress / shear_rate


def flow_rate(pressure_drop, viscosity, pipe_radius, pipe_length):
    """Hagen-Poiseuille equation for laminar flow rate."""
    if viscosity <= 0 or pipe_length <= 0:
        raise ValueError("viscosity and pipe length must be positive")
    return (math.pi * pipe_radius**4 * pressure_drop) / (8 * viscosity * pipe_length)


def reynolds_number(velocity, diameter, viscosity, density=1000):
    """Calculate Reynolds number for flow characterization."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return density * velocity * diameter / viscosity


def is_laminar(re_number):
    """Check if flow is laminar (Re < 2300)."""
    return re_number < 2300


def transfer_time(volume, rate):
    """Calculate time to transfer a volume at a given rate."""
    if rate <= 0:
        raise ValueError("rate must be positive")
    return volume / rate
