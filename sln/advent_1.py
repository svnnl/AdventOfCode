with open('../data/advent_1.txt') as f:
    data = list(map(int, f.read()))

print(data)

res = 0
for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        res += data[i]
if data[0] == data[len(data) - 1]:
    res += data[0]

print(f'Answer to Part 1: {res}')

res = 0
for i in range(len(data) - 1):
    if data[i] == data[(i + len(data) // 2) % len(data)]:
        res += data[i]

print(f'Answer to Part 2: {res}')
