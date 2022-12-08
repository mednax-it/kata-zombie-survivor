from enum import Enum
from typing import List

from decorator import decorator

from zombie_survivor.history import historian

from .level import Level


EQUIPMENT_LIMIT = 5
WOUND_LIMIT = 2
ACTION_LIMIT = 3


class Skill(Enum):
    PLUS_1_ACTION = "+1 Action"


class NoSpaceRemainingError(Exception):
    pass


class NoActionsRemainingError(Exception):
    pass


@decorator
def action(func, *args, **kwargs):
    [survivor, *_] = args
    if survivor.actions_taken >= ACTION_LIMIT:
        raise NoActionsRemainingError
    func(*args, **kwargs)
    survivor._actions_taken += 1


class Survivor:
    def __init__(self, name: str, experience: int = 0, equipment: List[str] = None):
        self.name = name
        self._wound_count = 0
        self._actions_taken = 0
        self._equipment: List[str] = [] if equipment is None else equipment
        self._experience = experience

    def is_alive(self) -> bool:
        return self.wound_count < WOUND_LIMIT

    @property
    def actions_taken(self) -> int:
        return self._actions_taken

    @property
    def action_limit(self) -> int:
        return (
            ACTION_LIMIT + 1
            if Skill.PLUS_1_ACTION in self.unlocked_skills
            else ACTION_LIMIT
        )

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

    @property
    def potential_skills(self) -> List[Skill]:
        level = self.level
        if level == Level.YELLOW:
            return [Skill.PLUS_1_ACTION]
        return []

    @property
    def unlocked_skills(self) -> List[Skill]:
        level = self.level
        if level == Level.YELLOW:
            return [Skill.PLUS_1_ACTION]
        return []

    def has_space_remaining(self) -> bool:
        return self.space_remaining > 0

    def has_actions_remaining(self) -> bool:
        return max(self.action_limit - self.actions_taken, 0) > 0

    @historian.item_picked_up
    @action
    def pick_up(self, item: str):
        if not self.has_space_remaining():
            raise NoSpaceRemainingError
        self._equipment.append(item)

    @historian.wounded
    def wound(self):
        self._wound_count += 1

    @action
    def kill_zombie(self):
        self._experience += 1
