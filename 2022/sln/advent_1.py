with open("../data/advent_1.txt") as f:
    data = [i.split("\n") for i in f.read().split("\n\n")]

weights = []
for i in data:
    weights.append(sum(map(int, i)))

weights.sort(reverse=True)
print(f"Answer to Part 1: {weights[0]}")
print(f"Answer to Part 2: {sum(weights[0:3])}")
