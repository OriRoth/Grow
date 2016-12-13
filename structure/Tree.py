from main import Parameters
from main.Grid import Drawable
from util.Fonts import *


class Tree:
    def __init__(self, root, ps):
        self.root = root
        self.ps = ps
        self.branches = [(root[0] - 1, root[1])]
        self.roots = [(root[0] + 1, root[1])]
        self.leaves = []
        self.fruits = []
        self.water = Parameters.initial_water
        self.light = Parameters.initial_light
        self.age = Parameters.initial_age


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
