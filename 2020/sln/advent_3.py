import numpy as np
import math

with open('../data/advent_3.txt') as f:
    data = np.array([list(map(str, i)) for i in f.read().splitlines()])


def solve(grid, directions):
    return math.prod([traverse(grid, i) for i in directions])


def traverse(grid, direction):
    grid = np.tile(grid, max(direction) * math.ceil((len(grid) / len(grid[0]))))
    right, down = direction
    x = 0
    y = 0

    tree_count = 0
    while x < len(grid):
        if grid[x][y] == '#':
            tree_count += 1
        x += down
        y += right

    return tree_count


print('Answer to Part 1: {0}'.format(solve(data, [(3, 1)])))
print('Answer to Part 2: {0}'.format(solve(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])))
