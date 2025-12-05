from copy import deepcopy

TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2025/test/test_{day}.txt" if TEST else f"2025/data/{day}.txt"

lines = open(path, "r").read().splitlines()

EMPTY = "."
TP = "@"
DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
]

grid = [list(line) for line in lines]


def traverse_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    removed_positions = set()

    for x in range(rows):
        row = grid[x]
        for y, ch in enumerate(row):
            if ch == EMPTY:
                continue

            adj = sum(
                1
                for dx, dy in DIRECTIONS
                if 0 <= x + dx < rows
                and 0 <= y + dy < cols
                and grid[x + dx][y + dy] == TP
            )
            if adj < 4:
                removed_positions.add((x, y))

    return removed_positions


print(f"Part 1: {len(traverse_grid(grid))}")


grid2 = deepcopy(grid)
cnt = 0
while True:
    removed_positions = traverse_grid(grid2)
    if not removed_positions:
        break
    cnt += len(removed_positions)
    for x, y in removed_positions:
        grid2[x][y] = EMPTY

print(f"Part 2: {cnt}")
