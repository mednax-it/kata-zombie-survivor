from zombie_survivor.game import Game
from zombie_survivor.history import History, historian, history
from zombie_survivor.survivor import Survivor


class TestHistory:
    history: History

    def setup(self):
        self.history = History()

    def test_can_be_initialized(self):
        assert self.history

    def test_returns_none_when_no_events(self):
        assert self.history.pop() is None

    def test_can_save_events(self):
        event = "An event"
        assert self.history.pop() is None
        self.history.push(event)
        assert self.history.pop() == event


class TestHistorian:
    def test_game_started(self):
        @historian.game_started
        def test():
            # Don't need to do anything
            pass

        test()

        assert "game begins" in history.pop()

    def test_survivor_added(self):
        @historian.survivor_added
        def test(*_args, **_kwargs):
            # Don't need to do anything
            pass

        survivor = Survivor(name="Fred")
        game = Game()

        test(game, survivor)

        message = history.pop()
        assert "adds a survivor" in message
        assert survivor.name in message

    def test_item_picked_up(self):
        @historian.item_picked_up
        def test(*_args, **_kwargs):
            # Don't need to do anything
            pass

        survivor = Survivor(name="Fred")
        item = "baseball bat"

        test(survivor, item)

        message = history.pop()
        assert "picked up" in message
        assert survivor.name in message
        assert item in message

    def test_wounded(self):
        @historian.wounded
        def test(*_args, **_kwargs):
            # Don't need to do anything
            pass

        survivor = Survivor(name="Fred")

        test(survivor)

        message = history.pop()
        assert "wounded" in message
        assert survivor.name in message
