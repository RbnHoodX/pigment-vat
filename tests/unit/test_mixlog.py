"""Unit tests for the MixLog and Transfer classes."""

from vat import Vat
from mixlog import Transfer, MixLog


def test_transfer_creation():
    """Transfer stores dest, source, amount, and note."""
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    t = Transfer(a, b, 100, "test")
    assert t.dest_vat is a
    assert t.source_vat is b
    assert t.amount == 100
    assert t.note == "test"


def test_transfer_default_note():
    """Transfer note defaults to empty string."""
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    t = Transfer(a, b, 50)
    assert t.note == ""


def test_transfer_initial_id():
    """Transfer starts with id 0 before recording."""
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    t = Transfer(a, b, 100)
    assert t.id == 0


def test_mixlog_empty():
    """New mix log has no transfers."""
    ml = MixLog()
    assert ml.transfers() == []


def test_mixlog_record():
    """Recording a transfer assigns an id and adds it to the log."""
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    ml = MixLog()
    t = Transfer(a, b, 100)
    result = ml.record(t)
    assert result.id == 1
    assert len(ml.transfers()) == 1


def test_mixlog_sequential_ids():
    """Recorded transfers get sequential IDs."""
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    ml = MixLog()
    t1 = ml.record(Transfer(a, b, 100))
    t2 = ml.record(Transfer(a, b, 200))
    t3 = ml.record(Transfer(a, b, 300))
    assert t1.id == 1
    assert t2.id == 2
    assert t3.id == 3


def test_mixlog_returns_copy():
    """transfers() returns a copy of the internal list."""
    ml = MixLog()
    a = Vat("crimson")
    b = Vat("reservoir", "overflow")
    ml.record(Transfer(a, b, 100))
    transfers = ml.transfers()
    transfers.clear()
    assert len(ml.transfers()) == 1
