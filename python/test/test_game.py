from zombie_survivor.game import Game


def test_game_started_with_no_survivors():
    game = Game()
    assert len(game.survivors) == 0
