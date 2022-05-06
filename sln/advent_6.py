import numpy as np
import colorama


def color_sign(x):
    c = colorama.Fore.GREEN if x > 0 else colorama.Fore.RED
    return f'{c}{x}'


np.set_printoptions(formatter={'int': color_sign})

with open('../data/advent_6.txt') as f:
    data = [tuple(map(int, i.split(', '))) for i in f.read().splitlines()]

print(f'Coordinates: {data}')


def manhattan(p1, p2):
    return sum(abs(v1 - v2) for v1, v2 in zip(p1, p2))


max_x = max([x[0] for x in data])
max_y = max([y[1] for y in data])

grid = np.zeros((max_y + 1, max_x + 1), dtype=int)

for i in range(len(data)):
    grid[data[i][1]][data[i][0]] = i + 1

region_size = 0
region_distance = 10000

for i in range(len(grid)):
    for j in range(len(grid[0])):
        distances = [manhattan((j, i), pos) for pos in data]
        min_value = min(distances)
        if distances.count(min_value) > 1:
            grid[i][j] = 0
        else:
            grid[i][j] = distances.index(min(distances)) + 1

        if sum(distances) < region_distance:
            region_size += 1

edge_values = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 or j == 0 or i == max_y or j == max_x:
            edge_values.add(grid[i][j])

areas = []
for i in range(len(data)):
    if i + 1 not in edge_values:
        areas.append(np.count_nonzero(grid == i + 1))

print(f'Answer to Part 1: {max(areas)}')

print(f'Answer to Part 2: {region_size}')
