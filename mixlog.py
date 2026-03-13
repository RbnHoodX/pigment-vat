class Transfer:
    """A pigment movement entry linking two vats."""

    def __init__(self, dest_vat, source_vat, amount, note=""):
        self._id = 0
        self._dest_vat = dest_vat
        self._source_vat = source_vat
        self._amount = amount
        self._note = note

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def dest_vat(self):
        return self._dest_vat

    @property
    def source_vat(self):
        return self._source_vat

    @property
    def amount(self):
        return self._amount

    @property
    def note(self):
        return self._note

    def __repr__(self):
        return (f"Transfer(id={self._id}, dest={self._dest_vat.name!r}, "
                f"source={self._source_vat.name!r}, amount={self._amount})")


class MixLog:
    """Append-only log of pigment transfer records."""

    def __init__(self):
        self._transfers = []
        self._counter = 0

    def record(self, transfer):
        self._counter += 1
        transfer.id = self._counter
        self._transfers.append(transfer)
        transfer.dest_vat._add_transfer(transfer)
        transfer.source_vat._add_transfer(transfer)
        return transfer

    def transfers(self):
        return list(self._transfers)
