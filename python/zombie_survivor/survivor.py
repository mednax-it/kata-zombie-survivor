MAX_ITEMS = 5


class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.wounds = 0
        self._equipment: list[str] = []
        self._actions_remaining = 3

    def is_alive(self) -> bool:
        return self.wounds < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num

    # TODO: Need to decrement when wounded
    # TODO: Need to differentiate between "in hand" and "in reserve"
    @property
    def space_remaining(self) -> int:
        return MAX_ITEMS - len(self._equipment)

    def equip(self, item: str):
        if not self._has_space_remaining():
            return

        self._equipment.append(item)

    def _has_space_remaining(self) -> bool:
        return len(self._equipment) < MAX_ITEMS
