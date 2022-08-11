INITIAL_EQUIPMENT_LIMIT = 5

class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.wounds = 0
        self._actions_remaining = 3
        self._equipment = []

    def is_alive(self) -> bool:
        return self.wounds < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num

    @property
    def space_remaining(self) -> int:
        return INITIAL_EQUIPMENT_LIMIT - len(self._equipment)

    def pick_up(self, item: str):
        self._equipment.append(item)
