import pytest

from zombie_survivor.survivor import (
    Level,
    Survivor,
    NoSpaceRemainingError,
    EQUIPMENT_LIMIT,
)


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
        assert self.survivor.experience == 0
        assert self.survivor.level == Level.BLUE

    def test_setter(self):
        self.survivor.actions_remaining = 5
        assert self.survivor.actions_remaining == 5

    def test_can_pick_up_equipment(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.pick_up("baseball bat")
        assert self.survivor.space_remaining == expected_space_remaining

    def test_can_not_pick_up_too_much_equipment(self):
        for _ in range(EQUIPMENT_LIMIT):
            self.survivor.pick_up("baseball bat")
        with pytest.raises(NoSpaceRemainingError):
            self.survivor.pick_up("baseball bat")

    def test_can_be_wounded(self):
        expected_wound_count = self.survivor.wound_count + 1
        self.survivor.wound()
        assert self.survivor.wound_count == expected_wound_count

    def test_wounds_decrease_equipment_space(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.wound()
        assert self.survivor.space_remaining == expected_space_remaining

    def test_killing_a_zombie_increments_experience(self):
        expected_experience = self.survivor.experience + 1
        self.survivor.kill_zombie()
        assert self.survivor.experience == expected_experience

    def test_remains_at_level_blue_initially(self):
        for _ in range(6):
            assert self.survivor.level == Level.BLUE
            self.survivor.kill_zombie()
            assert self.survivor.level == Level.BLUE

    def test_can_level_up_to_yellow(self):
        self.survivor.experience = 6
        self.survivor.kill_zombie()
        assert self.survivor.level == Level.YELLOW

    def test_remains_at_level_yellow_until_boundary_reached(self):
        self.survivor.experience = 7
        self.survivor.level = Level.YELLOW
        for _ in range(11):
            assert self.survivor.level == Level.YELLOW
            self.survivor.kill_zombie()
            assert self.survivor.level == Level.YELLOW

    def test_can_level_up_to_orange(self):
        self.survivor.experience = 18
        self.survivor.kill_zombie()
        assert self.survivor.level == Level.ORANGE

    def test_remains_at_level_orange_until_boundary_reached(self):
        self.survivor.experience = 19
        self.survivor.level = Level.ORANGE
        for _ in range(23):
            assert self.survivor.level == Level.ORANGE
            self.survivor.kill_zombie()
            assert self.survivor.level == Level.ORANGE

    def test_can_level_up_to_red(self):
        self.survivor.experience = 42
        self.survivor.kill_zombie()
        assert self.survivor.level == Level.RED
