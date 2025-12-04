TEST = 1
day = __file__.split("\\")[-1][:-3]

path = f'2025/test/test_{day}.txt' if TEST else f'2025/data/{day}.txt'

grid = open(path, 'r').read().splitlines()

# Part 1

def traverse_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    removed_positions = set()

    for x in range(rows):
        for y in range(cols):
            total_adj = 0
            dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1)]
            if grid[x][y] != '.':
                for dir in dirs:
                    if 0 <= x + dir[0] < rows and 0 <= y + dir[1] < cols:
                        if grid[x + dir[0]][y + dir[1]] == '@':
                            total_adj += 1
                if total_adj < 4:
                    removed_positions.add((x, y))

    return removed_positions

print(f'Part 1: {len(traverse_grid(grid))}')

# Part 2
has_changed = True
while has_changed:
    has_changed=False
    removed_positions = traverse_grid(grid)
    if removed_positions:
        has_changed = True
        for pos in removed_positions:
            x, y = pos
            
    