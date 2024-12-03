with open('../data/advent_1.txt') as f:
    data = list(map(int, f.read().splitlines()))

print(f'Answer to Part 1: {sum(data)}')

values = []
freq = 0

for i in (x for _ in range(1000) for x in data):
    freq += i

    if freq in values:
        print(f'Answer to Part 2: {freq}')
        break
    else:
        values.append(freq)
