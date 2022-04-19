with open('../data/advent_2.txt') as f:
    data = list(map(str, f.read().splitlines()))

print(data)


def checksum(id):
    return (1 if any(id.count(letter) == 2 for letter in set(id)) else 0,
            1 if any(id.count(letter) == 3 for letter in set(id)) else 0)


two = 0
three = 0
for i in data:
    a, b = checksum(i)
    two += a
    three += b

print(two * three)
