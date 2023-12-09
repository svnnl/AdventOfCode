from collections import defaultdict
import itertools
import re
import math

TEST = 0
DAY = 8

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

instructions, maps = open(path, 'r').read().split('\n\n')

network = defaultdict()

for line in maps.split('\n'):
    network[line.split(' = ')[0]] = [re.sub(r'[^\w]', '', i)
                                     for i in line.split(' = ')[1].split(', ')]


steps = 0
current = 'AAA'

for i in itertools.cycle(instructions):
    if current == 'ZZZ':
        break
    if i == 'L':
        current = network[current][0]
    else:
        current = network[current][1]
    steps += 1

print(f'Answer to Part 1: {(steps)}')

all_steps = []
for current in [x for x in network if x.endswith('A')]:
    steps = 0

    for i in itertools.cycle(instructions):
        if current.endswith('Z'):
            break
        if i == 'L':
            current = network[current][0]
        else:
            current = network[current][1]
        steps += 1

    all_steps.append(steps)

print(f'Answer to Part 2: {math.lcm(*all_steps)}')
