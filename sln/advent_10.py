import numpy as np
import math
from collections import defaultdict

with open('../data/advent_10.txt') as f:
    data = np.array([list(map(str, i)) for i in f.read().splitlines()])

asteroids = []

for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == '#':
            asteroids.append((x, y))


def dist(a1, a2):
    return math.sqrt(pow(a1[0] - a2[0], 2) + pow(a1[1] - a2[1], 2))


def visible(p1, p2):
    if p1 == p2:
        return False
    for i in asteroids:
        if p1 == i or p2 == i:
            continue
        if abs((dist(p1, i) + dist(i, p2)) - dist(p1, p2)) < 0.0001:
            return False
    return True


vis = defaultdict(list)

for i in range(len(asteroids)):
    for j in range(i + 1, len(asteroids)):
        if visible(asteroids[i], asteroids[j]):
            vis[asteroids[i]].append(asteroids[j])
            vis[asteroids[j]].append(asteroids[i])

# for key, value in vis.items():
#    print(f'Asteroid{key}: {len(value)} visible Asteroids.')

print(f'Answer to Part 1: {max(len(v) for v in vis.values())}')
