from typing import List


class History:
    def __init__(self):
        self._records: List[str] = []

    def __len__(self):
        return len(self._records)

    def push(self, event: str):
        self._records.append(event)

    def pop(self) -> str:
        return self._records.pop()
