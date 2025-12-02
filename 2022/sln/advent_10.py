import numpy as np

data = open("../data/advent_10.txt").read().splitlines()

register = 1
signal = 0
cycle = 0
executing = False
i = 0

drawing = []

while cycle < 240:
    cycle += 1
    position = (cycle - 1) % 40
    if position in [register - 1, register, register + 1]:
        drawing.append("█")
    else:
        drawing.append(" ")

    if cycle % 40 == 20:
        signal += register * cycle

    if data[i] == "noop":
        i += 1
    else:
        if executing:
            register += int(data[i].split()[1])
            executing = False
            i += 1
        else:
            executing = True

print(f"Answer to Part 1: {signal}")

drawing = np.array_split(np.asarray(drawing), 6)
print(*[" ".join(i) for i in drawing], sep="\n")
