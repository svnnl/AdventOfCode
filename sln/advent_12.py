with open('../data/advent_12.txt') as f:
    data = f.read().splitlines()

print(data)

directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

R = 90

h = 0
v = 0


def move(h, v, command, value):
    if command == 'N':
        v += value
    elif command == 'S':
        v -= value
    elif command == 'E':
        h += value
    elif command == 'W':
        h -= value

    return h, v


for instruction in data:
    command = instruction[0]
    value = int(instruction[1:])
    print(command, value)
    if command in ['N', 'S', 'E', 'W']:
        h, v = move(h, v, command, value)
    elif command == 'F':
        h, v = move(h, v, directions[R], value)
    elif command == 'R':
        R = (R + value) % 360
    elif command == 'L':
        R = (R - value) % 360

    print(h, v, R)

print('Answer to Part 1: {0}'.format(abs(h) + abs(v)))
