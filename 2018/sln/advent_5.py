with open("../data/advent_5.txt") as f:
    x = f.read().rstrip()

chars = set([i.lower() for i in x])
pairs = [c + c.upper() for c in chars]
pairs += [c.upper() + c for c in chars]


def react(s):
    for p in pairs:
        s = s.replace(p, "")
    return s


def destroy(polymer):
    copy = data
    polymer = data
    while True:
        polymer = react(copy)
        if polymer == copy:
            break
        copy = polymer
    return polymer


data = x
print(f"Answer to Part 1: {len(destroy(data))}")


def transform(polymer, char):
    return "".join([x for x in polymer if x.lower() != char])


l = []

for char in chars:
    data = transform(x, char)
    l.append(len(destroy(data)))

print(f"Answer to Part 2: {min(l)}")
