import numpy as np

with open('../data/advent_11.txt') as f:
    data = np.array([list(i) for i in f.read().splitlines()])


def neighbours(grid, pos):
    rows = len(grid)
    columns = len(grid[0])

    x = pos[0]
    y = pos[1]

    adjacent = []
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(columns, y + 2)):
            if (i, j) != pos:
                adjacent.append(grid[i][j])
    return adjacent


for x in range(500):
    grid = data.copy()
    for i in range(len(data[0])):
        for j in range(len(data)):
            current_seat = data[j][i]
            adj = neighbours(data, (j, i))
            if current_seat == 'L' and '#' not in adj:
                grid[j][i] = '#'
            if current_seat == '#' and adj.count('#') >= 4:
                grid[j][i] = 'L'
    print(grid)
    if np.array_equal(data, grid):
        print('Answer to Part 1: {0} '.format(np.count_nonzero(grid == '#')))
        break
    else:
        data = grid
