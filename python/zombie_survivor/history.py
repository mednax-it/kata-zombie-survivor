from datetime import datetime
from typing import List, Optional

from decorator import decorator


class History:
    def __init__(self):
        self._history: List[str] = []

    def pop(self) -> Optional[str]:
        if not self._history:
            return None
        return self._history.pop()

    def push(self, event: str):
        self._history.append(event)


history = History()


class Historian:
    @staticmethod
    @decorator
    def wounded(func, *args, **kwargs):
        func(*args, **kwargs)
        [survivor] = args
        history.push(f"The survivor {survivor.name} is wounded")

    @staticmethod
    @decorator
    def item_picked_up(func, *args, **kwargs):
        func(*args, **kwargs)
        [survivor, item] = args
        history.push(f"The survivor {survivor.name} picked up: {item}")

    @staticmethod
    @decorator
    def game_started(func, *args, **kwargs):
        func(*args, **kwargs)
        history.push(f"The game begins at: {datetime.utcnow()}")

    @staticmethod
    @decorator
    def survivor_added(func, *args, **kwargs):
        func(*args, **kwargs)
        [_, survivor] = args
        history.push(f"The game adds a survivor: {survivor.name}")


historian = Historian()
