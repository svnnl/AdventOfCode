with open('../data/advent_15.txt') as f:
    data = f.read().split(',')

print(data)

last_position = {}

for i, v in enumerate(data):
    last_position[v] = i

for i in range(2, 2020):
    pass
