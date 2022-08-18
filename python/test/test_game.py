from zombie_survivor.game import Game


class TestGame:
    def setup(self):
        self.game = Game()

    def test_starts_with_no_survivors(self):
        assert len(self.game.survivors) == 0

    def test_can_add_survivors(self):
        expected_length = len(self.game.survivors) + 1
        self.game.add_survivor("Dread Pirate Roberts")
        assert len(self.game.survivors) == expected_length
