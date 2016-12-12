from main.Grid import Drawable
from structure.Filler import Filler
from util.Fonts import *


class GroundDrawable(Enum):
    ground = Drawable('▓', Color.yellow, Background.red)
    ground_waters = Drawable('░', Color.yellow, Background.blue)


class Ground(Filler):
    def __init__(self, length, height, ground_waters_height, priority=20):
        assert ground_waters_height <= height
        self.length = length
        self.height = height
        self.ground_waters_height = ground_waters_height
        self.priority = priority

    def fill(self, grid):
        assert self.length == grid.length, self.height <= grid.height
        for i in range(self.ground_waters_height):
            for j in range(self.length):
                grid.fill(GroundDrawable.ground_waters, grid.height - i - 1, j)
        for i in range(self.height - self.ground_waters_height):
            for j in range(self.length):
                grid.fill(GroundDrawable.ground_waters, grid.height - i - self.ground_waters_height - 1)

    def get_priority(self):
        return self.priority