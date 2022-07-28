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

    def test_setter(self):
        self.survivor.actions_remaining = 5
        assert self.survivor.actions_remaining == 5

    def test_can_add_equipment(self):
        current_length = len(self.survivor.equipment)
        self.survivor.equip("Baseball bat")
        assert len(self.survivor.equipment) == current_length + 1

    def test_can_not_equip_above_capacity(self):
        current_length = len(self.survivor.equipment)
        for _ in range(5):
            self.survivor.equip("Baseball bat")
        assert not self.survivor.has_capacity()
