from zombie_survivor.game import Game
from zombie_survivor.survivor import Survivor
from zombie_survivor.history import history


def test_history_messages():
    game = Game()
    survivor = Survivor("Freddy")
    game.add_survivor(survivor)
    survivor.wound()

    assert "wounded" in history.pop()
    assert "adds a survivor" in history.pop()
    assert "game begins" in history.pop()
