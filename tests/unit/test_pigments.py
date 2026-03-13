"""Unit tests for pigment science modules."""

from pigments.spectrum import classify_wavelength, complementary_wavelength, is_warm_tone
from pigments.concentration import dilution_ratio, concentration_after_mix, is_saturated
from pigments.saturation import saturation_time, batch_schedule


def test_classify_red():
    """Classify wavelength in red range."""
    assert classify_wavelength(650) == "red"


def test_classify_blue():
    """Classify wavelength in blue range."""
    assert classify_wavelength(470) == "blue"


def test_classify_unknown():
    """Wavelength outside visible range returns unknown."""
    assert classify_wavelength(300) == "unknown"


def test_complementary():
    """Complementary wavelength is computed correctly."""
    result = complementary_wavelength(500)
    assert result == 630


def test_warm_tone():
    """Wavelengths >= 570nm are warm tones."""
    assert is_warm_tone(600) is True
    assert is_warm_tone(500) is False


def test_dilution_ratio():
    """Dilution ratio calculates solvent needed."""
    result = dilution_ratio(100, 50, 10)
    assert result == 10.0


def test_concentration_after_mix():
    """Mixing two solutions gives weighted average concentration."""
    result = concentration_after_mix(100, 5, 50, 5)
    assert result == 75.0


def test_is_saturated():
    """Saturated when concentration meets or exceeds max solubility."""
    assert is_saturated(100, 90) is True
    assert is_saturated(50, 90) is False


def test_saturation_time():
    """Time to saturate a vat."""
    assert saturation_time(100, 10) == 10.0


def test_batch_schedule():
    """Schedule is sequential with correct timing."""
    schedule = batch_schedule([("a", 100), ("b", 200)], 50)
    assert len(schedule) == 2
    assert schedule[0]["start"] == 0
    assert schedule[0]["end"] == 2.0
    assert schedule[1]["start"] == 2.0
    assert schedule[1]["end"] == 6.0
