"""Integration tests for data pipeline operations."""

from scripts.seed_data import seed_small, seed_medium
from reports.statistics import average_transfer_amount, total_pigment_moved
from pigments.spectrum import classify_wavelength
from pigments.concentration import concentration_after_mix
from pigments.saturation import batch_schedule
from formulas.ratios import normalize_ratios
from formulas.temperature import optimal_dye_temp


def test_seed_data_small():
    """Small seed creates expected structure."""
    ws = seed_small()
    assert len(ws.vats()) == 3
    assert len(ws.mix_entries()) == 2


def test_seed_data_medium():
    """Medium seed creates expected structure."""
    ws = seed_medium()
    assert len(ws.vats()) == 6
    assert len(ws.mix_entries()) == 7


def test_stats_on_seeded_workshop():
    """Statistics work on seeded workshop."""
    ws = seed_medium()
    avg = average_transfer_amount(ws)
    assert avg > 0
    total = total_pigment_moved(ws)
    assert total > 0


def test_color_classification():
    """Classify pigment colors by wavelength."""
    assert classify_wavelength(650) == "red"
    assert classify_wavelength(470) == "blue"
    assert classify_wavelength(550) == "green"


def test_mixing_concentration():
    """Concentration after mixing two pigment solutions."""
    result = concentration_after_mix(80, 10, 40, 10)
    assert result == 60.0


def test_batch_schedule_timing():
    """Batch schedule produces correct sequential timing."""
    schedule = batch_schedule([("crimson", 100), ("indigo", 200)], 50)
    assert schedule[0]["end"] == 2.0
    assert schedule[1]["start"] == 2.0


def test_recipe_normalization():
    """Recipe ratios normalize correctly."""
    result = normalize_ratios([3, 1, 1])
    assert abs(result[0] - 0.6) < 0.001


def test_dye_temperature():
    """Dye temperature ranges are reasonable."""
    low, high = optimal_dye_temp("acid")
    assert low >= 80
    assert high <= 110
