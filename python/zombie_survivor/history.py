from typing import List, Optional


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
