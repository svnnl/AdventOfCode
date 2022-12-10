import numpy as np

data = open('../data/advent_10.txt').read().splitlines()

register = 1
checkpoints = []
cycle = 0
executing = False
i = 0

drawing = []

while cycle < 240:
    cycle += 1
    position = cycle % 40 - 1
    if position in range(register - 1, register + 2):
        drawing.append('#')
    else:
        drawing.append('.')

    if (cycle + 20) % 40 == 0:
        checkpoints.append(register * cycle)

    if data[i] != 'noop':
        if executing:
            register += int(data[i].split()[1])
            executing = False
            i += 1
        else:
            executing = True
    else:
        i += 1

print(f'Answer to Part 1: {sum(checkpoints)}')

drawing = np.array_split(np.asarray(drawing), 6)
print(*[' '.join(i) for i in drawing], sep='\n')
