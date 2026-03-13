from vat import Vat
from mixlog import Transfer, MixLog


class Workshop:
    """Dye workshop managing vats and pigment transfers.

    Every pigment movement is a mix log entry that adds pigment to one vat
    (dest) and removes it from another (source) by the same amount.
    This keeps the total pigment balanced: total inflows always equal
    total outflows.
    """

    def __init__(self):
        self._vats = {}
        self._mixlog = MixLog()

    def create_vat(self, name, kind="standard"):
        if name in self._vats:
            raise ValueError(f"vat {name!r} already exists")
        vat = Vat(name, kind)
        self._vats[name] = vat
        return vat

    def get_vat(self, name):
        return self._vats[name]

    def vats(self):
        return list(self._vats.values())

    def pour(self, dest_name, source_name, amount, note=""):
        if amount <= 0:
            raise ValueError("amount must be positive")
        dest_vat = self._vats[dest_name]
        source_vat = self._vats[source_name]
        transfer = Transfer(dest_vat, source_vat, amount, note)
        self._mixlog.record(transfer)
        return transfer

    def mix_entries(self):
        return self._mixlog.transfers()

    def pigment_balance(self):
        total_in = 0
        total_out = 0
        for transfer in self._mixlog.transfers():
            total_in += transfer.amount
            total_out += transfer.amount
        return total_in, total_out
