import math

TEST = 0
DAY = 6

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

times, distances = [[int(i) for i in line.split() if i.isdigit()] for line in open(path, 'r').read().split('\n')]


def race(t, d):
    return math.prod([sum([(v * (t[i] - v)) > d[i] for v in range(t[i])]) for i in range(len(t))])


print(f"Answer to Part 1: {race(times, distances)}")

times, distances = [int(''.join([str(i) for i in times]))], [int(''.join([str(i) for i in distances]))]

print(f"Answer to Part 2: {race(times, distances)}")
