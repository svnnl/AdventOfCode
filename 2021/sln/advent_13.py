import numpy as np


def get_max_values(dots):
    return list(map(max, zip(*dots)))


def print_paper(dots):
    max_x, max_y = get_max_values(dots)

    paper = np.full((max_y + 1, max_x + 1), '.', dtype=str)
    for point in points:
        x = point[0]
        y = point[1]
        paper[y][x] = '#'

    print(paper)


def fold_paper(dots, f, v):
    print('Folding on: {1} = {0}'.format(v, f))

    new_dots = []
    dots_to_remove = []

    for i, value in enumerate(dots):
        x = value[0]
        y = value[1]

        if f == 'y':
            if y > v:
                new_point = (x, (v * 2) - y)
                dots_to_remove.append(dots[i])
                new_dots.append(new_point)
        else:
            if x > v:
                new_point = (v * 2 - x, y)
                dots_to_remove.append(dots[i])
                new_dots.append(new_point)

    dots = [x for x in dots if x not in dots_to_remove]
    dots.extend(new_dots)

    return dots


with open('../data/advent_13.txt') as f:
    data = f.read().splitlines()

points = []
instructions = []

for i in data:
    if ',' in i:
        points.append((int(i.split(',')[0]), int(i.split(',')[1])))
    if 'f' in i:
        instructions.append((i.split('along ')[1].split('=')[0], int(i.split('along ')[1].split('=')[1])))

for instruction in instructions:
    fold = instruction[0]
    value = instruction[1]

    points = fold_paper(points, fold, value)

    np.set_printoptions(threshold=np.inf, linewidth=np.nan, suppress=True)

    print_paper(points)

    print('Amount of unique points: {0} '.format(len(set(points))))
