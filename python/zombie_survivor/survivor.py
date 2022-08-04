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

    # TODO: Is capacity the best term for this property?
    # TODO: Need to differentiate between "in hand" and "in reserve"
    # TODO: Need to decrement when wounded
    @property
    def capacity(self) -> int:
        return MAX_ITEMS - len(self._equipment)

    def equip(self, item: str):
        if not self._has_capacity():
            return

        self._equipment.append(item)

    def _has_capacity(self) -> bool:
        return len(self._equipment) < 5
