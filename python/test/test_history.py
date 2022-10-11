from zombie_survivor.history import Historian, History, historian, history
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
    historian: Historian

    def setup(self):
        self.historian = Historian()

    def test_records_wounded(self):
        @historian.wounded
        def test(_):
            # Don't need to actually do anything
            pass

        survivor = Survivor(name="Fred")

        test(survivor)

        message = history.pop()
        assert survivor.name in message
        assert "is wounded" in message

    def test_records_item_picked_up(self):
        @historian.item_picked_up
        def test(_, __):
            # Don't need to actually do anything
            pass

        survivor = Survivor(name="Fred")
        item = "baseball bat"

        test(survivor, item)

        message = history.pop()
        assert survivor.name in message
        assert item in message
        assert "picked up" in message
