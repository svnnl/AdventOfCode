import numpy as np

with open('../data/advent_3.txt') as f:
    data = [i.strip() for i in f.readlines()]


def create_grid(s):
    return np.zeros((s, s), dtype=int)


grid = create_grid(1000)

for row in data:
    id, claim = row.split(' @ ')
    start = tuple(map(int, claim.split(': ')[0].split(',')))
    size = tuple(map(int, claim.split(': ')[1].split('x')))

    for i in range(start[0], start[0] + size[0]):
        for j in range(start[1], start[1] + size[1]):
            if grid[i][j] > 0:
                grid[i][j] = -1
            else:
                grid[i][j] = int(id.replace("#", ""))

print(f'Answer to Part 1: {np.count_nonzero(grid > 1)}')

for row in data:
    id, claim = row.split(' @ ')
    start = tuple(map(int, claim.split(': ')[0].split(',')))
    size = tuple(map(int, claim.split(': ')[1].split('x')))

    if np.count_nonzero(grid == int(id.replace("#", ""))) == size[0] * size[1]:
        print(f'Answer to Part 2: {id}')
        break
