import pytest

from zombie_survivor.history import history


@pytest.fixture(autouse=True)
def prep_history():
    yield
    history.clear()
