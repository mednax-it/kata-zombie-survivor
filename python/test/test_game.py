from datetime import datetime

import pytest

from zombie_survivor.game import DuplicateNameError, Game
from zombie_survivor.level import Level
from zombie_survivor.survivor import Survivor

NOW = datetime.utcnow()


class TestGame:
    game: Game

    def setup(self):
        self.game = Game(now=NOW)

    def test_game_initialized_properly(self):
        assert len(self.game.survivors) == 0
        assert self.game.level == Level.BLUE
        assert self.game.history == [f"The game begins at: {NOW}"]

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

    def test_game_level_equals_highest_survivor_level(self):
        oscar = Survivor("Oscar the Grouch")
        grover = Survivor("Grover")
        self.game.add_survivor(oscar)
        self.game.add_survivor(grover)
        while oscar.level < Level.YELLOW:
            oscar.kill_zombie()
        while grover.level < Level.ORANGE:
            grover.kill_zombie()
        assert self.game.level != oscar.level
        assert self.game.level == grover.level

    def test_game_level_maxes_out(self):
        survivor = Survivor("Godzilla")
        self.game.add_survivor(survivor)
        while survivor.level < Level.RED:
            survivor.kill_zombie()
        assert self.game.level == Level.RED
        survivor.kill_zombie()
        assert self.game.level == Level.RED

    def test_game_history_records_added_survivor(self):
        survivor = Survivor("Peter the Rabbit")
        self.game.add_survivor(survivor)
        assert f"The game adds a survivor: {survivor.name}" in self.game.history
