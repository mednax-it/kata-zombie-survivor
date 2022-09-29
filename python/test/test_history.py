from zombie_survivor.history import History


class TestHistory:
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
