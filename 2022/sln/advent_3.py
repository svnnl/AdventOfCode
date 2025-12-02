with open("../data/advent_3.txt") as f:
    data = f.read().splitlines()


def get_score(items):
    return sum([ord(i) - 96 if i == i.lower() else ord(i) - 38 for i in items])


items = []
for line in data:
    items.append(
        list(
            set(line[: len(line) // 2]).intersection(
                set(line[len(line) // 2 : len(line)])
            )
        )[0]
    )

print(f"Answer to Part 1: {get_score(items)}")

items_2 = []
for i in range(0, len(data), 3):
    items_2.append(list(set(data[i]) & set(data[i + 1]) & set(data[i + 2]))[0])

print(f"Answer to Part 2: {get_score(items_2)}")
