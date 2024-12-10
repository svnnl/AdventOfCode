TEST = 1
day = __file__.split("\\")[-1][:-3]

path = f'2024/test/test_{day}.txt' if TEST else f'2024/data/{day}.txt'

data = [list(i) for i in open(path, 'r').read().splitlines()]


start = [(x, y) for x in range(len(data))
         for y in range(len(data[0])) if data[x][y] == "^"][0]


def traverse(grid):
    dirs = {
        0: (-1, 0),
        90: (0, 1),
        180: (1, 0),
        270: (0, -1)
    }

    visited = set()
    x, y = start
    dir = 0

    while True:
        visited |= {(x, y)}

        dx, dy = x + dirs[dir][0], y + dirs[dir][1]

        if not (0 <= dx < len(grid) and 0 <= dy < len(grid[0])):
            break

        if grid[dx][dy] == "#":
            dir = (dir + 90) % 360

        x, y = x + dirs[dir][0], y + dirs[dir][1]

    return visited


print(f"Answer to Part 1: {len(traverse(data))}")
