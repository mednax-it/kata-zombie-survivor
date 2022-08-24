from zombie_survivor.survivor import Survivor


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Rob Zombie")

    def test_initial_setup(self):
        assert self.survivor.name == "Rob Zombie"
        assert self.survivor.wounds == 0
        assert self.survivor.is_alive()
        assert self.survivor.actions_remaining() == 3
