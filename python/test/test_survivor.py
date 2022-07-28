from zombie_survivor.survivor import Survivor


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Rob Zombie")

    def test_initial_setup(self):
        assert self.survivor.name == "Rob Zombie"
        assert self.survivor.wounds == 0
        assert self.survivor.is_alive()
        assert self.survivor.actions_remaining == 3
        assert self.survivor.equipment_in_hand == ["Baseball bat", "Frying pan"]
        assert self.survivor.equipment_in_reserve == [
            "Bottled water",
            "Katana",
            "Pistol",
        ]

    def test_setter(self):
        self.survivor.actions_remaining = 5
        assert self.survivor.actions_remaining == 5

    def test_wound_decreases_equipment_carried(self):
        initial_count = len(self.survivor.equipment_in_hand) + len(
            self.survivor.equipment_in_reserve
        )
        self.survivor.wound = 1
        assert initial_count - 1 == len(self.survivor.equipment_in_hand) + len(
            self.survivor.equipment_in_reserve
        )
