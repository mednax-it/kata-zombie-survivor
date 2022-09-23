from typing import List

from decorator import decorator


class History:
    def __init__(self):
        self._records: List[str] = []

    def __len__(self):
        return len(self._records)

    def push(self, record: str):
        self._records.append(record)

    def pop(self) -> str:
        return self._records.pop()

    def reset(self):
        self._records = []


history = History()


def event(tmpl, values):
    @decorator
    def inner(func, *args, **kwargs):
        value = func(*args, **kwargs)
        history.push(tmpl.format(**values(args)))
        return value

    return inner
