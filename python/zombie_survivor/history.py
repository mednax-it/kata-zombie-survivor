from typing import List


class History:
    def __init__(self):
        self._history: List[str] = []

    def pop(self):
        if not self._history:
            return None
        return self._history.pop()

    def push(self, event):
        self._history.append(event)
