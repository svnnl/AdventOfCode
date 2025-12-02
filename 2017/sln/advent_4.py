from collections import defaultdict

with open("../data/advent_4.txt") as f:
    data = [i.split(" ") for i in f.read().splitlines()]

res = 0

for pw in data:
    valid = True
    occ = defaultdict(int)
    for word in pw:
        if word in occ:
            valid = False
        else:
            occ[word] += 1
    if valid:
        res += 1

print(f"Answer to Part 1: {res}")

res = 0

for pw in data:
    valid = True
    occ = defaultdict(int)
    for word in pw:
        if "".join(sorted(word)) in occ:
            valid = False
        else:
            occ["".join(sorted(word))] += 1
    if valid:
        res += 1

print(f"Answer to Part 2: {res}")
