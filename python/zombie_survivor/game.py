from typing import List, Sequence

from .survivor import Survivor


class DuplicateNameError(Exception):
    pass


class Game:
    def __init__(self):
        self._survivors: List[Survivor] = []

    @property
    def survivors(self) -> Sequence[Survivor]:
        return tuple(self._survivors)

    def add_survivor(self, survivor: Survivor):
        if survivor.name in [s.name for s in self._survivors]:
            raise DuplicateNameError
        self._survivors.append(survivor)
