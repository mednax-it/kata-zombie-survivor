import pytest

from zombie_survivor.survivor import Survivor
from zombie_survivor.game import DuplicateNameError, Game


def test_game_started_with_no_survivors():
    game = Game()
    assert len(game.survivors) == 0


def test_game_can_add_survivors():
    game = Game()
    expected_survivor_count = len(game.survivors) + 1
    game.add_survivor(Survivor("Dread Pirate Roberts"))
    assert len(game.survivors) == expected_survivor_count


def test_game_can_not_add_survivors_with_same_name():
    game = Game()
    game.add_survivor(Survivor("Dread Pirate Roberts"))
    with pytest.raises(DuplicateNameError):
        game.add_survivor(Survivor("Dread Pirate Roberts"))
