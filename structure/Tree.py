from main import Rules
from main.Grid import Drawable
from structure.Filler import Filler
from util.Fonts import *


class Tree(Filler):
    def __init__(self, root, ps=None):
        self.root = root
        self.ps = ps
        self.branches = [(TreeDrawable.branch_vertical, root[0] - 1, root[1])]
        self.roots = [(TreeDrawable.root_vertical, root[0] + 1, root[1])]
        self.leaves = []
        self.fruits = []
        self.water = Rules.initial_water
        self.light = Rules.initial_light
        self.age = Rules.initial_age
        self._drawables = [self.branches, self.roots, self.leaves, self.fruits, [(TreeDrawable.root, root[0], root[1])]]

    def get_priority(self):
        return 10

    def fill(self, grid):
        for ds in self._drawables:
            for t in ds:
                grid.fill(t[0].value, t[1], t[2])


class TreeDrawable(Enum):
    branch_diag_left = Drawable('\\', Background.cyan)
    branch_diag_right = Drawable('/', Background.cyan)
    branch_horizontal = Drawable('-', Background.cyan)
    branch_vertical = Drawable('|', Background.cyan)
    root_diag_left = Drawable('\\', Background.yellow)
    root_diag_right = Drawable('/', Background.yellow)
    root_horizontal = Drawable('-', Background.yellow)
    root_vertical = Drawable('|', Background.yellow)
    leaves = Drawable('♠', Background.green)
    fruit = Drawable('◍', Background.red)
    root = Drawable('O', Color.purple, Background.blue)
