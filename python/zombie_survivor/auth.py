from contextlib import contextmanager
from decorator import decorator


roles: dict[str, list[str]] = {"soldiers": []}


class AuthError(Exception):
    pass


@decorator
def soldiers_only(func, *args, **kwargs):
    [survivor, _] = args
    if survivor.name not in roles["soldiers"]:
        raise AuthError
    func(*args, **kwargs)


@contextmanager
def assign_role(survivor, role):
    roles[role].append(survivor.name)
    yield
    roles[role].remove(survivor.name)
