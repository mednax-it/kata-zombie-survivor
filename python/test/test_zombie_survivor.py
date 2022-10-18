from zombie_survivor.game import Game
from zombie_survivor.survivor import Survivor, WOUND_LIMIT
from zombie_survivor.history import history


def test_history_messages():
    game = Game()
    survivor = Survivor("Freddy")
    game.add_survivor(survivor)
    survivor.wound()

    assert "wounded" in history.pop()
    assert "adds a survivor" in history.pop()
    assert "game begins" in history.pop()


def test_survivors_die():
    game = Game()
    survivor = Survivor("Jason")
    game.add_survivor(survivor)

    for _ in range(WOUND_LIMIT):
        survivor.wound()

    assert not survivor.is_alive()
