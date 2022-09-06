import pytest

from zombie_survivor.survivor import Survivor, NoSpaceRemainingError, EQUIPMENT_LIMIT

BASEBALL_BAT = "baseball bat"


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Rob Zombie")

    def test_initial_setup(self):
        assert self.survivor.name == "Rob Zombie"
        assert self.survivor.wound_count == 0
        assert self.survivor.is_alive()
        assert self.survivor.actions_remaining == 3
        assert self.survivor.space_remaining == EQUIPMENT_LIMIT

    def test_setter(self):
        self.survivor.actions_remaining = 5
        assert self.survivor.actions_remaining == 5

    def test_can_pick_up_equipment(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.pick_up(BASEBALL_BAT)
        assert self.survivor.space_remaining == expected_space_remaining

    def test_can_not_pick_up_too_much_equipment(self):
        for _ in range(EQUIPMENT_LIMIT):
            self.survivor.pick_up(BASEBALL_BAT)
        with pytest.raises(NoSpaceRemainingError):
            self.survivor.pick_up(BASEBALL_BAT)

    def test_can_be_wounded(self):
        expected_wound_count = self.survivor.wound_count + 1
        self.survivor.wound()
        assert self.survivor.wound_count == expected_wound_count

    def test_wounds_decrease_equipment_space(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.wound()
        assert self.survivor.space_remaining == expected_space_remaining
