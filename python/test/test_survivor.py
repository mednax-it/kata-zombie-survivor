import pytest
from zombie_survivor.level import Level
from zombie_survivor.survivor import (
    Skill,
    EQUIPMENT_LIMIT,
    NoSpaceRemainingError,
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

    def test_one_potential_skill_at_level_yellow(self):
        while self.survivor.level != Level.YELLOW:
            self.survivor.kill_zombie()
        assert len(self.survivor.potential_skills) == 1
        assert Skill.PLUS_1_ACTION == self.survivor.potential_skills[0]

    def test_one_unlocked_skill_at_level_yellow(self):
        while self.survivor.level != Level.YELLOW:
            self.survivor.kill_zombie()
        assert len(self.survivor.unlocked_skills) == 1
        assert Skill.PLUS_1_ACTION == self.survivor.unlocked_skills[0]

    def test_additional_action_with_action_skill(self):
        expected_action_limit = self.survivor.action_limit + 1
        while Skill.PLUS_1_ACTION not in self.survivor.unlocked_skills:
            self.survivor.kill_zombie()
        assert expected_action_limit == self.survivor.action_limit

    def test_action_skill_handles_no_actions_properly(self):
        while Skill.PLUS_1_ACTION not in self.survivor.unlocked_skills:
            self.survivor.kill_zombie()
        while self.survivor.has_actions_remaining():
            self.survivor.kill_zombie()
        assert not self.survivor.has_actions_remaining()

    def test_killing_zombie_counts_as_action(self):
        expected_actions_taken = self.survivor.actions_taken + 1
        self.survivor.kill_zombie()
        assert expected_actions_taken == self.survivor.actions_taken
