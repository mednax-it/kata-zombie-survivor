from typing import List

from .level import Level


EQUIPMENT_LIMIT = 5


class NoSpaceRemainingError(Exception):
    pass


class Survivor:
    def __init__(self, name: str):
        self.name = name
        self._wound_count = 0
        self._actions_remaining = 3
        self._equipment: List[str] = []
        self._experience = 0
        self._level = Level.BLUE

    def is_alive(self) -> bool:
        return self.wound_count < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num

    @property
    def space_remaining(self) -> int:
        return EQUIPMENT_LIMIT - len(self._equipment) - self.wound_count

    @property
    def wound_count(self) -> int:
        return self._wound_count

    @property
    def experience(self) -> int:
        return self._experience

    @property
    def level(self) -> Level:
        experience = self._experience
        if experience > 42:
            return Level.RED
        if experience > 18:
            return Level.ORANGE
        if experience > 6:
            return Level.YELLOW
        return Level.BLUE

    def has_space_remaining(self) -> bool:
        return self.space_remaining > 0

    def pick_up(self, item: str):
        if not self.has_space_remaining():
            raise NoSpaceRemainingError
        self._equipment.append(item)

    def wound(self):
        self._wound_count += 1

    def kill_zombie(self):
        self._experience += 1
