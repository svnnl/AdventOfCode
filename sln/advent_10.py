import numpy as np

with open('../data/advent_10.txt') as f:
    data = np.array([list(map(str, i)) for i in f.read().splitlines()])

print(data)

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


def get_asteroid_count(pos):
    rows = len(data)
    columns = len(data[0])

    row = pos[0]
    column = pos[1]

    count = 0

    for dir in directions:
        i = row + dir[0]
        j = column + dir[1]
        while 0 <= i < rows and 0 <= j < columns:
            print((i, j))

            i += dir[0]
            j += dir[1]

    return count


get_asteroid_count((0, 0))
