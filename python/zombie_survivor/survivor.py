INITIAL_MAX_ITEMS = 5


class Survivor:
    def __init__(self, name: str):
        self.name = name
        self._wound_count = 0
        self._max_items = INITIAL_MAX_ITEMS
        self._equipment: list[str] = []
        self._actions_remaining = 3

    def is_alive(self) -> bool:
        return self.wound_count < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num

    # TODO: Need to differentiate between "in hand" and "in reserve".
    # TODO: Is wound() violating SRP by mutating two properties? Should
    # space_remaining() just use the wound_count in its caclulations?
    @property
    def space_remaining(self) -> int:
        return self._max_items - len(self._equipment)
    
    @property
    def wound_count(self) -> int:
        return self._wound_count
    
    def wound(self):
        self._wound_count += 1
        self._max_items -= 1

    def equip(self, item: str):
        if not self._has_space_remaining():
            return

        self._equipment.append(item)

    def _has_space_remaining(self) -> bool:
        return len(self._equipment) < self._max_items
