TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f'2024/test/test_{day}.txt' if TEST else f'2024/data/{day}.txt'

data = open(path, 'r').read().splitlines()


dirs = [(dy, dx) for dy in [-1, 0, 1]
        for dx in [-1, 0, 1] if (dx != 0 or dy != 0)]

cnt = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] == 'X':
            for d in dirs:
                dx = x
                dy = y
                word = 'X'
                for _ in range(3):
                    dx = dx + d[0]
                    dy = dy + d[1]
                    if 0 <= dx < len(data) and 0 <= dy < len(data[0]):
                        word += data[dx][dy]
                if word == 'XMAS':
                    cnt += 1


print(f"Answer to Part 1: {cnt}")

cnt = 0
for x in range(1, len(data) - 1):
    for y in range(1, len(data[x]) - 1):
        if data[x][y] == 'A':
            if {data[x-1][y-1], data[x+1][y+1]} == {data[x-1][y+1], data[x+1][y-1]} == {'M', 'S'}:
                cnt += 1

print(f"Answer to Part 2: {cnt}")
