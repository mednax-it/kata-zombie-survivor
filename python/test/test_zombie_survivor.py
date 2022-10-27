from zombie_survivor.game import Game
from zombie_survivor.survivor import Survivor, WOUND_LIMIT
from zombie_survivor.history import history


def test_history_messages():
    game = Game()
    survivor = Survivor("Freddy")
    game.add_survivor(survivor)
    survivor.wound()

    assert len(history) == 3
    assert "wounded" in history.current()
    assert "adds a survivor" in history.back()
    assert "game begins" in history.back()


def test_survivors_die():
    game = Game()
    survivor = Survivor("Jason")
    game.add_survivor(survivor)

    for _ in range(WOUND_LIMIT):
        survivor.wound()

    assert not survivor.is_alive()
