from datetime import datetime
from typing import Sequence

from .level import Level
from .survivor import Survivor
from .history import game_started, survivor_added, history


class DuplicateNameError(Exception):
    pass


class SurvivorNotFoundError(Exception):
    pass


class Game:
    @game_started
    def __init__(self):
        self._survivors = []

    @property
    def survivors(self) -> Sequence[Survivor]:
        return tuple(self._survivors)

    @property
    def level(self) -> Level:
        return max((s.level for s in self.survivors), default=Level.BLUE)

    @property
    def history(self) -> list[str]:
        return history.records_for(self, *self.survivors)

    @survivor_added
    def add_survivor(self, survivor: Survivor):
        if survivor.name in [s.name for s in self.survivors]:
            raise DuplicateNameError
        self._survivors.append(survivor)

    def is_started(self) -> bool:
        return len(self._survivors) > 0

    def is_finished(self) -> bool:
        return self.is_started() and self._all_survivors_dead()

    def _all_survivors_dead(self) -> bool:
        return all(not s.is_alive() for s in self.survivors)
