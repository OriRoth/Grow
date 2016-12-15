from random import shuffle, getrandbits

from main import Rules
from main.Grid import Drawable
from structure.Filler import Filler
from structure.Functions import *
from util.Fonts import *


class Tree(Filler):
    def __init__(self, root, ps=None):
        self.root = root
        self.ps = ps
        self.branches = [(TreeDrawable.branch_vertical, root[0] - 2, root[1])]
        self.roots = [(TreeDrawable.root_vertical, root[0] + 1, root[1])]
        self.leaves = []
        self.fruits = []
        self.water = Rules.initial_water
        self.light = Rules.initial_light
        self.age = Rules.initial_age
        self._drawables = [self.branches, self.roots, self.leaves, self.fruits,
                           [(TreeDrawable.root, root[0], root[1]), (TreeDrawable.root, root[0] - 1, root[1])]]
        self._leaves_indexes = []
        self._branches_indexes = [(root[0] - 2, root[1])]
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
        self._grow_leaves_n_branches_n_roots(available, is_ground)

    def _grow_fruits(self, available, is_ground):
        while True:
            if self.light < Rules.fruit_price[0] or self.water < Rules.fruit_price[1] or not grow_fruits(self.ps):
                break
            bd = False
            shuffle(self._branches_indexes)
            for b in self._branches_indexes:
                i, j = b[0] + 1, b[1]
                if available(i, j) and not is_ground(i, j):
                    bd = True
                    self._buy_fruit(i, j)
                    break
            if not bd:
                break

    def _grow_leaves_n_branches_n_roots(self, available, is_ground):
        db = dl = dr = False
        while True:
            cbl = not dl and self.light >= Rules.leaf_price[0] and self.water >= Rules.leaf_price[1]
            cbb = not db and self.light >= Rules.branch_price[0] and self.water >= Rules.branch_price[1]
            cbr = not dr and self.light >= Rules.root_price[0] and self.water >= Rules.root_price[1]
            if not cbl and not cbb and not cbr:
                break
            db, dl, dr = cbb, cbl, cbr
            if cbr and (cbl or cbb):
                if bool(getrandbits(1)):
                    cbr = False
                else:
                    cbl = cbb = False
            if cbl and cbb:
                t = grow_type(self.ps)
                if t is GrowType.branch:
                    cbl = False
                elif t is GrowType.leaf:
                    cbb = False
                else:
                    raise Exception("unknown/none type!")
            elif cbb:
                t = grow_type(self.ps)
                if t is GrowType.leaf:
                    cbb = False
                    db = True
            if cbb:
                if not self._grow_branch(available, is_ground):
                    db = True
            elif cbl:
                if not self._grow_leaf(available, is_ground):
                    dl = True
            elif cbr:
                if not self._grow_root(available, is_ground):
                    dr = True

    def _grow_branch(self, available, is_ground):
        shuffle(self._branches_indexes)
        for b in self._branches_indexes:
            au = available(b[0] - 1, b[1]) and not is_ground(b[0] - 1, b[1])
            asr = available(b[0], b[1] + 1) and not is_ground(b[0], b[1] + 1)
            asl = available(b[0], b[1] - 1) and not is_ground(b[0], b[1] - 1)
            if Rules.no_near_vertical_branches:
                au = au and (b[0] - 2, b[1]) not in self._branches_indexes
                asr = asr and (b[0] - 1, b[1] + 1) not in self._branches_indexes and (b[0] + 1, b[
                    1] + 1) not in self._branches_indexes
                asl = asl and (b[0] - 1, b[1] - 1) not in self._branches_indexes and (b[0] + 1, b[
                    1] - 1) not in self._branches_indexes
            if not au and not asr and not asl:
                continue
            if au and (asr or asl):
                d = grow_direction(self.ps)
                if d is GrowDirection.up:
                    asr = asl = False
                elif d is GrowDirection.sideways:
                    au = False
            i = j = dr = None
            if au:
                i, j, dr = b[0] - 1, b[1], TreeDrawable.branch_vertical
            elif asr:
                i, j, dr = b[0], b[1] + 1, TreeDrawable.branch_horizontal
            elif asl:
                i, j, dr = b[0], b[1] - 1, TreeDrawable.branch_horizontal
            assert available(i, j) and not is_ground(i, j) and dr
            self._buy_branch(i, j, dr)
            return True
        return False

    def _grow_leaf(self, available, is_ground):
        shuffle(self._branches_indexes)
        for b in self._branches_indexes:
            au = available(b[0] - 1, b[1]) and not is_ground(b[0] - 1, b[1])
            asr = available(b[0], b[1] + 1) and not is_ground(b[0], b[1] + 1) and b[1] >= self.root[1]
            asl = available(b[0], b[1] - 1) and not is_ground(b[0], b[1] + 1) and b[1] <= self.root[1]
            if not au and not asr and not asl:
                continue
            if au and (asr or asl):
                d = grow_direction(self.ps)
                if d is GrowDirection.up:
                    asr = asl = False
                elif d is GrowDirection.sideways:
                    au = False
            i = j = -1
            if au:
                i, j = b[0] - 1, b[1]
            elif asr:
                i, j = b[0], b[1] + 1
            elif asl:
                i, j = b[0], b[1] - 1
            assert available(i, j) and not is_ground(i, j)
            self._buy_leaf(i, j)
            return True
        return False

    def _grow_root(self, available, is_ground):
        shuffle(self._roots_indexes)
        for r in self._roots_indexes:
            ad = available(r[0] + 1, r[1]) and is_ground(r[0] + 1, r[1])
            asr = available(r[0], r[1] + 1) and is_ground(r[0], r[1] + 1) and r[1] >= self.root[1]
            asl = available(r[0], r[1] - 1) and is_ground(r[0], r[1] + 1) and r[1] <= self.root[1]
            if not ad and not asr and not asl:
                continue
            if ad and (asr or asl):
                d = grow_direction(self.ps)
                if d is GrowDirection.up:
                    asr = asl = False
                elif d is GrowDirection.sideways:
                    ad = False
            i = j = dr = None
            if ad:
                i, j, dr = r[0] + 1, r[1], TreeDrawable.root_vertical
            elif asr:
                i, j, dr = r[0], r[1] + 1, TreeDrawable.root_horizontal
            elif asl:
                i, j, dr = r[0], r[1] - 1, TreeDrawable.root_horizontal
            assert available(i, j) and is_ground(i, j) and dr
            self._buy_root(i, j, dr)
            return True
        return False

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
