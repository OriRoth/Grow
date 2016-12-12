from main.Grid import Grid, Drawable
from structure.Filler import Filler
from structure.Ground import Ground
from util.Fonts import Color


class Counter(Filler):
    def __init__(self):
        self.i = 0

    def fill(self, grid):
        grid.fill(Drawable(str(self.i)[0], Color.cyan), 1, 1)
        self.i += 1

    def get_priority(self):
        return 10


def go():
    grid = Grid(50, 20)
    ground = Ground(50, 10, 5)
    grid.register(ground)
    grid.register(Counter())
    for i in range(10):
        print(grid.draw())
        input()


if __name__ == '__main__':
    go()
