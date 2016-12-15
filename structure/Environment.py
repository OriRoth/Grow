from random import shuffle

from main.Rules import *
from structure.Ground import Ground
from structure.Tree import Tree


class Environment:
    def __init__(self, ground, grid):
        self.ground = ground
        self.grid = grid
        self.trees = []

    def register(self, tree):
        self.trees.append(tree)

    def round(self):
        for j in self._shuffle_indexes():
            self.pour_light(j)
            self.drop_rain(j)
            self.raise_ground_waters(j)
        for t in self.trees:
            t.birthday()
            t.round(lambda i, j: self.grid.available(i, j), lambda i, j: self.ground.is_ground(i, j))

    def pour_light(self, j):
        l = light_drop()
        for i in range(self.grid.height):
            c = self.grid.claims[i][j]
            if isinstance(c, Tree):
                c.add_light(l, i, j)
                l = light_diffusion(l)
            elif isinstance(c, Ground) or l == 0:
                break

    def drop_rain(self, j):
        w = rain_drop()
        for i in range(self.ground.height):
            c = self.grid.claims[i + self.grid.height - self.ground.height][j]
            if isinstance(c, Tree):
                c.add_water(w, i, j)
                w = rain_diffusion(w)
            if w == 0:
                break

    def raise_ground_waters(self, j):
        b = ground_waters_bottom()
        for i in range(self.grid.height):
            c = self.grid.claims[self.grid.height - i - 1][j]
            if isinstance(c, Tree):
                c.add_water(b, i, j)
                b = ground_waters_diffusion(b)
            elif not c or b == 0:
                break

    def _shuffle_indexes(self):
        res = list(range(self.ground.length))
        shuffle(res)
        return res
