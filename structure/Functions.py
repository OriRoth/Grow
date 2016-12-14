from enum import Enum
from random import choice, getrandbits


class Result(Enum):
    pass


class GrowDirection(Result):
    up = 0
    sideways = 1


class GrowType(Result):
    leaf = 0
    branch = 1


def grow_direction(ps):
    return choice(GrowDirection.members)


def grow_fruits(ps):
    return bool(getrandbits(1))


def grow_type(ps):
    return choice(GrowType.members)


def root_direction(ps):
    return choice(GrowDirection.members)
