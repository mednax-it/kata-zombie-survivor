from zombie_survivor.survivor import Survivor


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Rob Zombie")

    def test_initial_setup(self):
        assert self.survivor.name == "Rob Zombie"
        assert self.survivor.wound_count == 0
        assert self.survivor.is_alive()
        assert self.survivor.actions_remaining == 3

    def test_setter(self):
        self.survivor.actions_remaining = 5
        assert self.survivor.actions_remaining == 5

    def test_can_add_equipment(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.equip("Baseball bat")
        assert self.survivor.space_remaining == expected_space_remaining

    def test_can_not_equip_above_limit(self):
        for _ in range(5):
            self.survivor.equip("Baseball bat")
        expected_space_remaining = self.survivor.space_remaining
        self.survivor.equip("Baseball bat")
        assert self.survivor.space_remaining == expected_space_remaining
    
    def test_decrements_limit_when_wounded(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.wound()
        assert self.survivor.space_remaining == expected_space_remaining
