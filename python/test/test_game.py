from zombie_survivor.game import Game
from zombie_survivor.survivor import Survivor


class TestGame:
    def setup(self):
        self.game = Game()

    def test_game_started_with_no_survivors(self):
        assert len(self.game.survivors) == 0

    def test_game_can_add_survivors(self):
        expected_survivor_count = len(self.game.survivors) + 1
        self.game.add_survivor(Survivor("Captain Sparrow"))
        assert len(self.game.survivors) == expected_survivor_count
