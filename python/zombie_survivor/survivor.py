class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.wounds = 0
        self.equipment_in_hand: list[str] = ["Baseball bat", "Frying pan"]
        self.equipment_in_reserve: list[str] = [
            "Bottled water",
            "Katana",
            "Pistol",
        ]
        self._actions_remaining = 3

    def is_alive(self) -> bool:
        return self.wounds < 2

    @property
    def actions_remaining(self) -> int:
        return self._actions_remaining

    @actions_remaining.setter
    def actions_remaining(self, num: int):
        self._actions_remaining = num
