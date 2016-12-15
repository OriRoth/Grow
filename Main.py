from main.Grid import Grid
from structure.Environment import Environment
from structure.Ground import Ground
from structure.Tree import Tree


def main_loop():
    grid = Grid(50, 20)
    ground = Ground(50, 10, 5)
    env = Environment(ground, grid)
    tree = Tree((10, 25))
    grid.register(ground)
    grid.register(tree)
    env.register(tree)
    grid.draw()
    for i in range(10):
        env.round()
        print(grid.draw())
        print(tree.light)
        print(tree.water)
        input()


if __name__ == '__main__':
    main_loop()
