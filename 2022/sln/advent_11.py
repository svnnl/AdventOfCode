import math
from collections import defaultdict
from copy import deepcopy

data = open("../data/advent_11.txt").read().split("\n\n")

monkeys = defaultdict(list)
modulos = []

for i in range(len(data)):
    id, items = data[i].split("\n")[0], data[i].split("\n")[1]
    id = int(id.split(" ")[1][0])
    items = items.split(": ")[1].split(", ")
    modulos.append(int(data[i].split("\n")[3].split()[3]))

    for x in items:
        monkeys[id].append(int(x))


def run(monkeys, n, part_2=False):
    inspect = [0] * len(data)

    for _ in range(n):
        for i in range(len(data)):
            id, _, op, test, t, f = data[i].split("\n")
            id = int(id.split(" ")[1][0])
            operator = op.split()[4]
            value = op.split()[5]
            test = int(test.split()[3])
            t = int(t.split()[5])
            f = int(f.split()[5])

            for item in monkeys[id]:
                inspect[id] += 1
                if value == "old":
                    level = item**2
                else:
                    level = item * int(value) if operator == "*" else item + int(value)
                if part_2:
                    level = level % math.lcm(*modulos)
                else:
                    level = level // 3
                throw = t if level % test == 0 else f
                monkeys[throw].append(int(level))

            monkeys[id].clear()

    return inspect


monkeys_2 = deepcopy(monkeys)

print(f"Answer to Part 1: {math.prod(sorted(run(monkeys, 20), reverse=True)[:2])}")
print(
    f"Answer to Part 2: {math.prod(sorted(run(monkeys_2, 10000, True), reverse=True)[:2])}"
)
