import numpy as np
import colorama


def color_sign(x):
    c = colorama.Fore.RED if x >= 9 else colorama.Fore.GREEN if x == 0 else colorama.Fore.WHITE
    return f'{c}{x}'


np.set_printoptions(formatter={'int': color_sign})

with open('../data/advent_11.txt') as f:
    data = np.array([list(map(int, i)) for i in f.read().splitlines()])


def neighbours(pos):
    rows = len(data)
    columns = len(data[0])

    adjacent = []
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(columns, pos[1] + 2)):
            if (i, j) != pos:
                adjacent.append((i, j))
    return adjacent


def increase_adjacent(pos, flashed):
    adjacent = neighbours(pos)
    for i in adjacent:
        data[i] += 1
        if data[i] > 9 and i not in flashed:
            flashed.append(i)
            increase_adjacent(i, flashed)


print('Initial situation: \n {0}'.format(data))

flash_count = 0
steps = 300
stop_counting = 100
simultaneous = 0

for i in range(steps):
    flashed = []
    for index, value in np.ndenumerate(data):
        data[index] += 1
        if data[index] > 9 and index not in flashed:
            flashed.append(index)
            increase_adjacent(index, flashed)
    for pos in flashed:
        data[pos] = 0
    if i < stop_counting:
        flash_count += len(set(flashed))

    print("Situation after step {0} \n {1}".format(i + 1, data))

    if np.all(data == 0):
        simultaneous = i + 1
        break

print('Answer to Part 1: {0}'.format(flash_count))
print('Answer to Part 2: {0}'.format(simultaneous))
