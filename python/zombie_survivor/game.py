from typing import Sequence

from .survivor import Survivor


class DuplicateNameError(Exception):
    pass


class SurvivorNotFoundError(Exception):
    pass


class Game:
    def __init__(self):
        self._survivors = []

    @property
    def survivors(self) -> Sequence[Survivor]:
        return tuple(self._survivors)

    def add_survivor(self, survivor: Survivor):
        if survivor.name in [s.name for s in self._survivors]:
            raise DuplicateNameError
        self._survivors.append(survivor)

    def kill_survivor(self, survivor: Survivor):
        if survivor not in self._survivors:
            raise SurvivorNotFoundError
        self._survivors.remove(survivor)

    def is_finished(self) -> bool:
        return len(self._survivors) == 0
