from enum import Enum


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Level(OrderedEnum):
    BLUE = 1
    YELLOW = 2
    ORANGE = 3
    RED = 4


class LevelThreshold:
    blue_min = 0
    yellow_min = 7
    orange_min = 19
    red_min = 43
