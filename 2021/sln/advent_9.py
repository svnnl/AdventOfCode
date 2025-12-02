import numpy as np


def get_adjacent(data, i, j, m, n):
    adjacent = []

    if i > 0:
        adjacent.append(data[i - 1][j])
    if i + 1 < m:
        adjacent.append(data[i + 1][j])
    if j > 0:
        adjacent.append(data[i][j - 1])
    if j + 1 < n:
        adjacent.append(data[i][j + 1])

    return adjacent


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []

    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))

    return adjacent_indices


def sol9():
    with open("../data/advent_9.txt") as f:
        data = np.array([list(map(int, i)) for i in f.read().splitlines()])

    print(data)

    m = len(data)
    n = len(data[0])

    # PART 1
    risk_level = 0
    low_points = []
    for index, value in np.ndenumerate(data):
        x = index[0]
        y = index[1]
        if all(value < i for i in get_adjacent(data, x, y, m, n)):
            low_points.append((x, y))
            risk_level += value + 1

    # PART 2
    basins = []

    def append_to_basin(basin, point):
        basin.append(point)
        adjacent = get_adjacent_indices(point[0], point[1], m, n)
        for position in adjacent:
            value = data[position[0]][position[1]]
            if value != 9 and position not in basin:
                append_to_basin(basin, position)
        return basin

    for i in low_points:
        basin = []
        append_to_basin(basin, i)
        basins.append(len(basin))

    print("Answer to Part 1: {0}".format(risk_level))
    print("Answer to Part 2: {0}".format(np.prod(sorted(basins, reverse=True)[:3])))


sol9()
