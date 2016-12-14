from main.Grid import Grid
from structure.Ground import Ground
from structure.Tree import Tree


def go():
    grid = Grid(50, 20)
    ground = Ground(50, 10, 5)
    tree = Tree((10, 25))
    grid.register(ground)
    grid.register(tree)
    for i in range(10):
        print(grid.draw())
        input()


if __name__ == '__main__':
    go()
