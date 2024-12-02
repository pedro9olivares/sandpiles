import numpy as np
from sandpiles import add_grain, draw
import random

n = 100
grid = np.zeros((n,n))

grains_to_add = 20000

for _ in range(grains_to_add):
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)

    add_grain(x, y, grid, draw_it=False)

    print(_)

print('Final grid')
draw(grid, close = False)