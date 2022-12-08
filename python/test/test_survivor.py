import pytest
from zombie_survivor.level import Level, LevelThreshold
from zombie_survivor.survivor import (
    ACTION_LIMIT,
    EQUIPMENT_LIMIT,
    NoSpaceRemainingError,
    NoActionsRemainingError,
    Skill,
    Survivor,
)

BASEBALL_BAT = "baseball bat"


class TestSurvivor:
    survivor: Survivor

    def setup(self):
        self.survivor = Survivor("Rob Zombie")

    def test_initial_setup(self):
        assert self.survivor.name == "Rob Zombie"
        assert self.survivor.wound_count == 0
        assert self.survivor.is_alive()
        assert self.survivor.space_remaining == EQUIPMENT_LIMIT
        assert self.survivor.experience == 0
        assert self.survivor.level == Level.BLUE
        assert self.survivor.potential_skills == []
        assert self.survivor.unlocked_skills == []

    def test_can_pick_up_equipment(self):
        expected_space_remaining = self.survivor.space_remaining - 1
        self.survivor.pick_up(BASEBALL_BAT)
        assert self.survivor.space_remaining == expected_space_remaining

    def test_can_not_pick_up_too_much_equipment(self):
        initial_equipment = []
        for _ in range(EQUIPMENT_LIMIT):
            initial_equipment.append(BASEBALL_BAT)
        survivor = Survivor("Keyser Soze", equipment=initial_equipment)
        with pytest.raises(NoSpaceRemainingError):
            survivor.pick_up(BASEBALL_BAT)

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
        ["experience", "expected_level"],
        [
            *[
                (experience, Level.BLUE)
                for experience in range(
                    LevelThreshold.blue_min, LevelThreshold.yellow_min
                )
            ],
            *[
                (experience, Level.YELLOW)
                for experience in range(
                    LevelThreshold.yellow_min, LevelThreshold.orange_min
                )
            ],
            *[
                (experience, Level.ORANGE)
                for experience in range(
                    LevelThreshold.orange_min, LevelThreshold.red_min
                )
            ],
            (LevelThreshold.red_min, Level.RED),
        ],
    )
    def test_experience_progression_matches_expected(self, experience, expected_level):
        survivor = Survivor("test", experience=experience)
        assert survivor.level == expected_level

    def test_one_potential_skill_at_level_yellow(self):
        survivor = Survivor("Darth Vader", experience=LevelThreshold.yellow_min)
        assert len(survivor.potential_skills) == 1
        assert Skill.PLUS_1_ACTION == survivor.potential_skills[0]

    def test_one_unlocked_skill_at_level_yellow(self):
        survivor = Survivor("Darth Vader", experience=LevelThreshold.yellow_min)
        assert len(survivor.unlocked_skills) == 1
        assert Skill.PLUS_1_ACTION == survivor.unlocked_skills[0]

    def test_additional_action_with_action_skill(self):
        survivor = Survivor("Marty McFly", experience=LevelThreshold.yellow_min)
        expected_action_limit = ACTION_LIMIT + 1
        assert expected_action_limit == survivor.action_limit

    def test_killing_zombie_counts_as_action(self):
        expected_actions_taken = self.survivor.actions_taken + 1
        self.survivor.kill_zombie()
        assert expected_actions_taken == self.survivor.actions_taken

    def test_picking_up_counts_as_action(self):
        expected_actions_taken = self.survivor.actions_taken + 1
        self.survivor.pick_up(BASEBALL_BAT)
        assert expected_actions_taken == self.survivor.actions_taken

    def test_can_not_exceed_action_limit(self):
        while self.survivor.has_actions_remaining():
            self.survivor.pick_up(BASEBALL_BAT)
        with pytest.raises(NoActionsRemainingError):
            self.survivor.pick_up(BASEBALL_BAT)
