import math

with open("../data/advent_1.txt") as f:
    data = list(map(int, f.read().splitlines()))

print(f"Answer to Part 1: {sum([math.floor(i / 3) - 2 for i in data])}")

cost = 0
for i in data:
    while math.floor(i / 3) - 2 > 0:
        i = math.floor(i / 3) - 2
        cost += i

print(f"Answer to Part 2: {cost}")
