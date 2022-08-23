from zombie_survivor.game import Game


class TestGame:
    def setup(self):
        self.game = Game()

    def test_game_started_with_no_survivors(self):
        assert len(self.game.survivors) == 0
