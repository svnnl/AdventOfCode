with open('../data/advent_10.txt') as f:
    data = sorted(list(map(int, f.read().splitlines())))

differences = {
    1: 0,
    3: 0
}

data.append(max(data) + 3)
data.insert(0, 0)
print(data)

# Part 1

for index in range(len(data) - 1):
    differences[data[index + 1] - data[index]] += 1

print(differences)
print('Answer to Part 1: {0}'.format(differences[1] * differences[3]))

# Part 2
