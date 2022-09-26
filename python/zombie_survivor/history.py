from datetime import datetime
from typing import Any

from decorator import decorator

class History:
    def __init__(self):
        self._records: list[(Any,str)] = []

    def __len__(self):
        return len(self._records)

    def write_record(self, source: Any, record: str):
        self._records.append((source,record))

    def records_for(self, *sources: list[Any]) -> list[str]:
        return [record for (source, record) in self._records if source in sources]


history = History()


@decorator
def game_started(func, *args, **kwargs):
    func(*args, **kwargs)

    [game] = args
    history.write_record(game, f'The game begins at: {datetime.utcnow()}')


@decorator
def survivor_added(func, *args, **kwargs):
    func(*args, **kwargs)

    [game, survivor] = args
    history.write_record(game, f"The game adds a survivor: {survivor.name}")


@decorator
def item_picked_up(func, *args, **kwargs):
    func(*args, **kwargs)

    [survivor, item] = args
    history.write_record(survivor, f"Survivor {survivor.name} picked up: {item}")