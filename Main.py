import traceback
from random import random
from random import seed
from time import sleep

from main.Grid import Grid
from main.Rules import rounds
from structure.Environment import Environment
from structure.Ground import Ground
from structure.Tree import Tree

SEED = None  # 928453, 588119


def main_loop(sid=None):
    if sid is None:
        sid = int(random() * 1000000)
    seed(sid)
    grid = Grid(50, 20)
    ground = Ground(50, 10, 5)
    env = Environment(ground, grid)
    tree = Tree((10, 25))
    grid.register(ground)
    grid.register(tree)
    env.register(tree)
    print(grid.draw())
    print('random seed is ' + str(sid))
    sleep(2)
    for i in range(rounds):
        env.round()
        print(grid.draw() + "\n\nlight:\t" + str(tree.light) + "\t\twater:\t" + str(tree.water))
        sleep(0.1)
    input('done! score is ' + str(len(tree.fruits)) + " fruits. Random seed was " + str(sid))


if __name__ == '__main__':
    try:
        print(SEED)
        main_loop(SEED)
    except AssertionError:
        traceback.print_exc()
        input()
