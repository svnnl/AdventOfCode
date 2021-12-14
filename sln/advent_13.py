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
    max_x, max_y = get_max_values(dots)
    print('HERE {0}'.format(dots))

    new_dots = []
    dots_to_remove = []

    for i, value in enumerate(dots):
        print(i, value)
        x = value[0]
        y = value[1]

        if f == 'y':
            if y > v:
                print('Higher than fold value: {0} '.format(dots[i]))
                new_point = (x, max_y - y)
                dots_to_remove.append(dots[i])
                new_dots.append(new_point)
        else:
            if x > v:
                continue

    dots = [x for x in dots if x not in dots_to_remove]
    dots.append(new_dots)

    print(dots)

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
    print_paper(points)
    # size unique points
    break
