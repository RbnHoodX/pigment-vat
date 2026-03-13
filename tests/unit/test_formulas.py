"""Unit tests for formula modules."""

from formulas.ratios import normalize_ratios, scale_recipe, parts_to_percentages
from formulas.viscosity import dynamic_viscosity, reynolds_number, is_laminar
from formulas.temperature import celsius_to_kelvin, optimal_dye_temp, temp_correction_factor


def test_normalize_ratios():
    """Ratios normalize to sum of 1.0."""
    result = normalize_ratios([1, 2, 1])
    assert sum(result) == 1.0
    assert result[1] == 0.5


def test_scale_recipe():
    """Recipe scales by factor."""
    result = scale_recipe([10, 20, 30], 2)
    assert result == [20, 40, 60]


def test_parts_to_percentages():
    """Parts convert to percentages."""
    result = parts_to_percentages([1, 1, 2])
    assert result == [25.0, 25.0, 50.0]


def test_dynamic_viscosity():
    """Viscosity from stress and rate."""
    assert dynamic_viscosity(100, 10) == 10.0


def test_reynolds_laminar():
    """Low Reynolds number indicates laminar flow."""
    re = reynolds_number(0.1, 0.01, 1.0)
    assert is_laminar(re)


def test_celsius_to_kelvin():
    """Celsius converts to Kelvin."""
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15


def test_optimal_dye_temp():
    """Known dye types have temperature ranges."""
    low, high = optimal_dye_temp("reactive")
    assert low == 30
    assert high == 60


def test_temp_correction():
    """Temperature within 5 degrees has factor 1.0."""
    assert temp_correction_factor(50, 52) == 1.0
    assert temp_correction_factor(50, 70) == 0.65
