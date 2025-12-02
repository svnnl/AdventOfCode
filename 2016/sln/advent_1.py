with open("../data/advent_1.txt") as f:
    data = [(s[0], int(s[1:])) for s in f.read().split(", ")]

degrees = 0
x = 0
y = 0

visited = set()

for i, v in data:
    if i == "L":
        degrees -= 90
    else:
        degrees += 90

    z = degrees % 360
    if z == 0:
        y += v
    elif z == 90 or z == -270:
        x += v
    elif z == 180 or z == -180:
        y -= v
    elif z == 270 or z == -90:
        x -= v

    if (x, y) in visited:
        print(f"Answer to Part 2: {abs(x) + abs(y)}")
        break
    else:
        visited.add((x, y))

print(f"Answer to Part 1: {abs(x) + abs(y)}")
