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


def get_asteroid_count(point):
    count = 0

    return count


print([get_asteroid_count(i) for i in data])
