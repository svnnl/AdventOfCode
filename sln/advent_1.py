import math

with open('../data/advent_1.txt') as f:
    print(sum([math.floor(i / 3) - 2 for i in list(map(int, f.read().splitlines()))]))
