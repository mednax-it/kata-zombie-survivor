class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.wounds = 0
        self.equipment: list[str] = []
        self._actions_remaining = 3

    def is_alive(self) -> bool:
        return self.wounds < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num

    def equip(self, item: str):
        self.equipment.append(item)

    def has_capacity(self) -> bool:
        return len(self.equipment) < 5
