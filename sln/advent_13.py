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

    for i in range(len(dots)):
        print(dots[1])
        print(i, dots[i])
        print('Current point: {0}'.format(dots[i]))
        x = dots[i][0]
        y = dots[i][1]

        if f == 'y':
            if y > v:
                print('Higher than fold value: {0} '.format(dots[i]))
                new_point = (x, max_y - y)
                dots.remove(dots[i])
                dots.append(new_point)
        else:
            if x > v:
                continue

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
