from zombie_survivor.survivor import Survivor


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Fred")

    def test_initial_setup(self):
        assert self.survivor.name == "Fred"
        assert self.survivor.wounds == 0
        assert self.survivor.is_alive()
        assert self.survivor.actions_remaining == 3

    def test_does_survivor_die_after_2_wounds(self):
        self.survivor.wounds = 2
        assert not self.survivor.is_alive()
