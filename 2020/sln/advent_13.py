import math

# Part 1

with open('../data/advent_13.txt') as f:
    value, busses = f.read().splitlines()

bus_ids = [int(x) for x in busses.split(',') if x != 'x']

earliest_bus = 0
best_diff = 1
best_rounding_diff = 1

for i in bus_ids:
    diff = int(value) / i
    rounding_diff = math.ceil(diff) - diff
    if rounding_diff < best_rounding_diff:
        earliest_bus = i
        best_diff = diff
        best_rounding_diff = rounding_diff

print(f'Answer to Part 1: {earliest_bus * ((math.ceil(best_diff) * earliest_bus) - int(value))}')

# Part 2

busses = busses.split(',')
busses = [(int(busses[k]), k) for k in range(len(busses)) if busses[k] != 'x']

multiplier = 1
start = 0
for i in range(len(busses) - 1):
    bus_id = busses[i + 1][0]
    position = busses[i + 1][1]
    multiplier *= busses[i][0]
    while (start + position) % bus_id != 0:
        start += multiplier

print(f'Answer to Part 2: {start}')
