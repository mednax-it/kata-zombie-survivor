from typing import Sequence

from .survivor import Survivor


class Game:
    def __init__(self):
        self._survivors = []

    @property
    def survivors(self) -> Sequence[Survivor]:
        return tuple(self._survivors)
