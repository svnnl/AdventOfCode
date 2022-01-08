import math

with open('../data/advent_13.txt') as f:
    value, busses = f.read().splitlines()

bus_ids = [int(x) for x in busses.split(',') if x != 'x']
print(bus_ids)

earliest_bus = 0
best_diff = 1
best_rounding_diff = 1

for i in bus_ids:
    diff = int(value) / i
    rounding_diff = math.ceil(diff) - diff
    print(diff, rounding_diff)
    if rounding_diff < best_rounding_diff:
        earliest_bus = i
        best_diff = diff
        best_rounding_diff = rounding_diff

print('Answer to Part 1: {}'.format(earliest_bus * ((math.ceil(best_diff) * earliest_bus) - int(value))))
