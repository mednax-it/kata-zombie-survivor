from zombie_survivor.survivor import Survivor


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Gandalf")

    def test_creating_a_new_survivor(self):
        assert self.survivor.name == "Gandalf"
        assert self.survivor.wounds == 0
        assert self.survivor.remaining_actions == 3
        assert self.survivor.is_alive
