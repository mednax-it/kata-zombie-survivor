import pytest

from zombie_survivor.game import DuplicateNameError, Game
from zombie_survivor.survivor import Survivor


class TestGame:
    game: Game

    def setup(self):
        self.game = Game()

    def test_game_started_with_no_survivors(self):
        assert len(self.game.survivors) == 0

    def test_game_can_add_survivors(self):
        expected_survivor_count = len(self.game.survivors) + 1
        self.game.add_survivor(Survivor("Captain Sparrow"))
        assert len(self.game.survivors) == expected_survivor_count

    def test_game_can_not_add_survivor_with_dupe_name(self):
        self.game.add_survivor(Survivor("Kyle the Dreadful"))
        with pytest.raises(DuplicateNameError):
            self.game.add_survivor(Survivor("Kyle the Dreadful"))

    def test_game_ends_when_no_survivors(self):
        survivor = Survivor("Gabriel le Terrible")
        self.game.add_survivor(survivor)
        self.game.kill_survivor(survivor)
        assert self.game.is_finished
