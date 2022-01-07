import numpy as np

with open('../data/advent_11.txt') as f:
    data = np.array([list(i) for i in f.read().splitlines()])

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def neighbours(grid, pos):
    rows = len(grid)
    columns = len(grid[0])

    row = pos[0]
    column = pos[1]

    adjacent = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, column - 1), min(columns, column + 2)):
            if (i, j) != pos and grid[i][j] == '#':
                adjacent += 1
    return adjacent


def visible(grid, pos):
    rows = len(grid)
    columns = len(grid[0])

    row = pos[0]
    column = pos[1]

    count = 0
    for dir in directions:
        i = row + dir[0]
        j = column + dir[1]
        while 0 <= i < rows and 0 <= j < columns:
            if (i, j) != pos and grid[i][j] in ['#', 'L']:
                if grid[i][j] == '#':
                    count += 1
                break
            else:
                i += dir[0]
                j += dir[1]

    return count


def solve(data, part):
    if part == 1:
        threshold = 4
    else:
        threshold = 5
    for x in range(500):
        grid = data.copy()
        for i in range(len(data)):
            for j in range(len(data[0])):
                current_seat = data[i][j]
                if part == 1:
                    adj = neighbours(data, (i, j))
                else:
                    adj = visible(data, (i, j))
                if current_seat == 'L' and adj == 0:
                    grid[i][j] = '#'
                if current_seat == '#' and adj >= threshold:
                    grid[i][j] = 'L'
        # print(grid)
        if np.array_equal(data, grid):
            return np.count_nonzero(grid == '#')
        else:
            data = grid


print('Answer to Part 1: {0} '.format(solve(data, 1)))
print('Answer to Part 2: {0} '.format(solve(data, 2)))
