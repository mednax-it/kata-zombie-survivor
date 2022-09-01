import pytest

from zombie_survivor.game import DuplicateNameError, Game
from zombie_survivor.level import Level
from zombie_survivor.survivor import Survivor


class TestGame:
    game: Game

    def setup(self):
        self.game = Game()

    def test_game_initialized_with_no_survivors(self):
        assert len(self.game.survivors) == 0
        assert self.game.level == Level.BLUE

    def test_game_has_started(self):
        self.game.add_survivor(Survivor("Rob Zombie"))
        assert self.game.is_started()

    def test_game_when_initialized_is_not_finished(self):
        assert not self.game.is_finished()

    def test_game_when_started_is_not_finished(self):
        self.game.add_survivor(Survivor("Rob Zombie"))
        assert not self.game.is_finished()

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
        while survivor.is_alive():
            survivor.wound()
        assert self.game.is_finished()
