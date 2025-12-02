with open("../data/advent_2.txt") as f:
    data = list(map(str, f.read().splitlines()))


def checksum(_id):
    return (
        1 if any(_id.count(letter) == 2 for letter in set(_id)) else 0,
        1 if any(_id.count(letter) == 3 for letter in set(_id)) else 0,
    )


two = 0
three = 0
for i in data:
    a, b = checksum(i)
    two += a
    three += b

print(f"Answer to Part 1: {two * three}")


def match(a, b):
    return sum([a[i] != b[i] for i in range(len(a))]) == 1


for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if match(data[i], data[j]):
            print(f"Answer to Part 2: {''.join([l for l in data[i] if l in data[j]])}")
