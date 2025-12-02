import math

from termcolor import colored

with open("../data/advent_8.txt") as f:
    data = [list(map(int, x)) for x in [list(i) for i in f.read().splitlines()]]


# print(*data, sep='\n')


def print_forest(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in visible:
                print(colored(grid[i][j], "green"), end="")
            else:
                print(colored(grid[i][j], "grey"), end="")
        print("\t")


def get_edges(grid):
    rows = len(grid)
    columns = len(grid[0])

    edges = []
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                edges.append((i, j))

    return edges


def observe(grid, pos):
    for dir in directions:
        highest_tree = grid[pos[0]][pos[1]]
        new_i = pos[0] + dir[0]
        new_j = pos[1] + dir[1]

        while 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
            next_tree = grid[new_i][new_j]
            if next_tree > highest_tree:
                if (new_i, new_j) not in visible:
                    visible.add((new_i, new_j))
                highest_tree = next_tree

            new_i += dir[0]
            new_j += dir[1]


def scenic_score():
    max_score = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            height = data[i][j]
            scores = []
            for dir in directions:
                score = 0
                new_i = i + dir[0]
                new_j = j + dir[1]

                while 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
                    score += 1
                    if data[new_i][new_j] < height:
                        new_i += dir[0]
                        new_j += dir[1]
                    else:
                        break

                scores.append(score)

            if math.prod(scores) > max_score:
                max_score = math.prod(scores)

    return max_score


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visible = set(get_edges(data))

for pos in get_edges(data):
    observe(data, pos)

print_forest(data)

print(f"Answer to Part 1: {len(visible)}")
print(f"Answer to Part 2: {scenic_score()}")
