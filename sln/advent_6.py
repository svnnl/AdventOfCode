with open('../data/advent_6.txt') as f:
    data = f.read()


def solve(n):
    for i in range(len(data)):
        if sorted(list(set(data[i:i + n]))) == sorted(list(data[i:i + n])):
            return i + n


print(f'Answer to Part 1: {solve(4)}')
print(f'Answer to Part 2: {solve(14)}')
