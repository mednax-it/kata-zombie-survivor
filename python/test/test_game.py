import pytest

from zombie_survivor.game import Game, DuplicateNameError
from zombie_survivor.survivor import Survivor


class TestGame:
    game: Game

    def setup(self):
        self.game = Game()

    def test_starts_with_no_survivors(self):
        assert len(self.game.survivors) == 0

    def test_can_add_survivors(self):
        expected_length = len(self.game.survivors) + 1
        self.game.add_survivor(Survivor("Dread Pirate Roberts"))
        assert len(self.game.survivors) == expected_length

    def test_can_not_add_survivors_with_same_name(self):
        survivor = Survivor("Dread Pirate Roberts")
        self.game.add_survivor(survivor)
        with pytest.raises(DuplicateNameError):
            self.game.add_survivor(survivor)
