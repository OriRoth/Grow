from enum import Enum
from random import choice, random


class Result(Enum):
    pass


class GrowDirection(Result):
    up = 0
    sideways = 1


class GrowType(Result):
    leaf = 0
    branch = 1


def grow_direction(ps):
    return choice([x for x in GrowDirection])


def grow_fruits(ps):
    return True


def grow_type(ps):
    if random() <= 0.333333333333333333:
        return GrowType.branch
    return GrowType.leaf


def root_direction(ps):
    return choice([x for x in GrowDirection])


def wait(ps):
    return random() <= 0.677777777777777777
