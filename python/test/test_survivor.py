import pytest

from zombie_survivor.level import Level
from zombie_survivor.survivor import Survivor, NoSpaceRemainingError, EQUIPMENT_LIMIT
from zombie_survivor.history import history

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
        assert self.survivor.experience == 0
        assert self.survivor.level == Level.BLUE

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

    def test_killing_a_zombie_increments_experience(self):
        expected_experience = self.survivor.experience + 1
        self.survivor.kill_zombie()
        assert self.survivor.experience == expected_experience

    @pytest.mark.parametrize(
        ["zombies_killed", "expected_level"],
        [
            *[(kill_count, Level.BLUE) for kill_count in range(0, 7)],
            *[(kill_count, Level.YELLOW) for kill_count in range(7, 19)],
            *[(kill_count, Level.ORANGE) for kill_count in range(19, 43)],
            (43, Level.RED),
        ],
    )
    def test_experience_progression_matches_expected(
        self, zombies_killed, expected_level
    ):
        for _ in range(zombies_killed):
            self.survivor.kill_zombie()

        assert self.survivor.level == expected_level

    def test_brand_new_survivor_has_empty_history(self):
        assert history.records_for(self.survivor) == []

    def test_picked_up_item_has_history_record(self):
        self.survivor.pick_up('Baseball Bat')

        assert history.records_for(self.survivor) == ["Survivor Rob Zombie picked up: Baseball Bat"]