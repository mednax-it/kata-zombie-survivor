from datetime import datetime

from .signals import game_started, survivor_added


history = []


@survivor_added.connect
def survivor_added_handler(survivor):
    history.append(f"The game adds a survivor: {survivor.name}")


@game_started.connect
def game_started_handler(_):
    history.append(f"The game begins at: {datetime.utcnow()}")
