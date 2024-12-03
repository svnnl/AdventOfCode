with open('../data/advent_6.txt') as f:
    data = list(map(int, f.read().split('\t')))

banks = data.copy()
found = False
occ = []
steps = 0
state = []

while not found:
    steps += 1
    v = max(banks)
    i = banks.index(v)

    banks[i] = 0
    while v != 0:
        i += 1
        banks[i % len(banks)] += 1
        v -= 1

    if banks in occ:
        found = True
        state = banks
    else:
        occ.append(list(banks))

print(f'Answer to Part 1: {steps}')

banks = state.copy()
found = False
steps = 0

while not found:
    steps += 1
    v = max(banks)
    i = banks.index(v)

    banks[i] = 0
    while v != 0:
        i += 1
        banks[i % len(banks)] += 1
        v -= 1

    if banks == state:
        found = True

print(f'Answer to Part 2: {steps}')
