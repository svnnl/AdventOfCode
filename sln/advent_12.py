with open('../data/advent_12.txt') as f:
    data = f.read().splitlines()

directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

# Part 1

R = 90
position = (0, 0)


def move(position, command, value):
    h = position[0]
    v = position[1]

    if command == 'N':
        v += value
    elif command == 'S':
        v -= value
    elif command == 'E':
        h += value
    elif command == 'W':
        h -= value

    return (h, v)


for instruction in data:
    # print('Command : {0}'.format(instruction))
    command = instruction[0]
    value = int(instruction[1:])
    if command in ['N', 'S', 'E', 'W']:
        position = move(position, command, value)
    elif command == 'F':
        position = move(position, directions[R], value)
    elif command == 'R':
        R = (R + value) % 360
    elif command == 'L':
        R = (R - value) % 360

    # print('Position {0}, R {1}'.format(position, R))

print('Answer to Part 1: {0}'.format(abs(position[0]) + abs(position[1])))


# Part 2

def move_forward(position, waypoint, value):
    h = position[0] + (waypoint[0] * value)
    v = position[1] + (waypoint[1] * value)

    return (h, v)


waypoint = (10, 1)
coordinates = (0, 0)

for instruction in data:
    command = instruction[0]
    value = int(instruction[1:])
    # print('Command : {0}'.format(instruction))

    if command in ['N', 'S', 'E', 'W']:
        waypoint = move(waypoint, command, value)
    elif command == 'F':
        coordinates = move_forward(coordinates, waypoint, value)
    elif command == 'R':
        if value == 90:
            waypoint = (waypoint[1], -1 * waypoint[0])
        elif value == 180:
            waypoint = (-1 * waypoint[0], -1 * waypoint[1])
        elif value == 270:
            waypoint = (-1 * waypoint[1], waypoint[0])
    elif command == 'L':
        if value == 90:
            waypoint = (-1 * waypoint[1], waypoint[0])
        elif value == 180:
            waypoint = (-1 * waypoint[0], -1 * waypoint[1])
        elif value == 270:
            waypoint = (waypoint[1], -1 * waypoint[0])

    # print('Coordinates {0}, waypoint {1}'.format(coordinates, waypoint))

print('Answer to Part 2: {0}'.format(abs(coordinates[0]) + abs(coordinates[1])))
