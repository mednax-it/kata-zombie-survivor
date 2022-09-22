import pytest
from zombie_survivor.history import History


@pytest.fixture
def history():
    return History()


def test_can_be_initialized(history):
    assert len(history) == 0


def test_can_push_events(history):
    expected_length = len(history) + 1
    history.push("an event")
    assert len(history) == expected_length


def test_can_pop_events(history):
    event = "an event"
    history.push(event)
    expected_length = len(history) - 1
    actual_event = history.pop()
    assert actual_event == event
    assert len(history) == expected_length
