from main import Rules
from main.Grid import Drawable
from structure.Filler import Filler
from structure.Functions import *
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
        self._leaves_indexes = []
        self._branches_indexes = [(root[0] - 1, root[1])]
        self._roots_indexes = [(root[0] + 1, root[1])]

    def get_priority(self):
        return 10

    def fill(self, grid):
        for ds in self._drawables:
            for t in ds:
                grid.fill_n_claim(self, t[0].value, t[1], t[2])

    def birthday(self):
        self.age += 1

    def add_light(self, light, i, j):
        if (i, j) in self._leaves_indexes:
            self.light += light

    def add_water(self, water, i, j):
        if (i, j) in self._roots_indexes:
            self.water += water

    def round(self, available, is_ground):
        self._grow_fruits(available, is_ground)
        self._grow_leaves_n_branches(available, is_ground)
        self._grow_roots(available, is_ground)

    def _grow_fruits(self, available, is_ground):
        while True:
            if self.light < Rules.fruit_price[0] or self.water < Rules.fruit_price[1] or not grow_fruits(self.ps):
                break
            bd = False
            for b in self._branches_indexes:
                i, j = b[0] + 1, b[1]
                if available(i, j) and not is_ground(i, j):
                    bd = True
                    self._buy_fruit(i, j)
                    break
            if not bd:
                break

    def _grow_leaves_n_branches(self, available, is_ground):
        while True:
            cbl = self.light >= Rules.leaf_price[0] and self.water >= Rules.leaf_price[1]
            cbb = self.light >= Rules.branch_price[0] and self.water >= Rules.branch_price[1]
            if not cbl or not cbb:
                break
            if not cbl:
                if not self._grow_branch(available, is_ground):
                    break
            elif not cbb:
                if not self._grow_leaf(available, is_ground):
                    break
            else:
                t = grow_type(self.ps)
                if t is GrowType.leaf:
                    if not self._grow_leaf(available, is_ground):
                        break
                elif t is GrowType.branch:
                    if not self._grow_branch(available, is_ground):
                        break

    def _grow_branch(self, available, is_ground):
        pass

    def _grow_leaf(self, available, is_ground):
        pass

    def _grow_roots(self, available, is_ground):
        pass

    def _buy_fruit(self, i, j):
        self.light -= Rules.fruit_price[0]
        self.water -= Rules.fruit_price[1]
        self.fruits.append((TreeDrawable.fruit, i, j))

    def _buy_leaf(self, i, j):
        self.light -= Rules.leaf_price[0]
        self.water -= Rules.leaf_price[1]
        self.leaves.append((TreeDrawable.leaves, i, j))
        self._leaves_indexes.append((i, j))

    def _buy_branch(self, i, j, d):
        self.light -= Rules.branch_price[0]
        self.water -= Rules.branch_price[1]
        self.branches.append((d, i, j))
        self._branches_indexes.append((i, j))

    def _buy_root(self, i, j, d):
        self.light -= Rules.root_price[0]
        self.water -= Rules.root_price[1]
        self.roots.append((d, i, j))
        self._roots_indexes.append((i, j))


class TreeDrawable(Enum):
    branch_diag_left = Drawable('\\', Background.cyan)
    branch_diag_right = Drawable('/', Background.cyan)
    branch_horizontal = Drawable('-', Background.cyan)
    branch_vertical = Drawable('|', Background.cyan)
    root_diag_left = Drawable('\\', Background.yellow)
    root_diag_right = Drawable('/', Background.yellow)
    root_horizontal = Drawable('-', Background.yellow)
    root_vertical = Drawable('|', Background.yellow)
    leaves = Drawable('$', Background.green)
    fruit = Drawable('@', Background.red)
    root = Drawable('~', Color.purple, Background.blue)
