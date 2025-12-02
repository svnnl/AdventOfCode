with open("../data/advent_5.txt") as f:
    data = list(map(int, f.read().splitlines()))

steps = 0
index = 0
instr = data.copy()

while True:
    try:
        steps += 1
        prev = index
        index += instr[index]
        if instr[prev] < 3:
            instr[prev] += 1
        else:
            instr[prev] -= 1
    except IndexError:
        print(f"Answer to Part 2: {steps - 1}")
        break

steps = 0
index = 0
instr = data.copy()

while True:
    try:
        steps += 1
        prev = index
        index += data[index]
        data[prev] += 1
    except IndexError:
        print(f"Answer to Part 1: {steps - 1}")
        break
