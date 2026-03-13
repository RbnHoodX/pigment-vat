class Vat:
    """A dye vat that tracks its pigment level from mix log transfers.

    The pigment level is always computed from transfers -- never stored directly.
    This guarantees the level is always consistent with the mix log.
    """

    def __init__(self, name, kind="standard"):
        self._name = name
        self._kind = kind
        self._transfers = []

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def pigment_level(self):
        total = 0
        for transfer in self._transfers:
            if transfer.dest_vat is self:
                total += transfer.amount
            elif transfer.source_vat is self:
                total -= transfer.amount
        return total

    def _add_transfer(self, transfer):
        self._transfers.append(transfer)

    def transfers(self):
        return list(self._transfers)

    def __repr__(self):
        return f"Vat(name={self._name!r}, kind={self._kind!r})"
