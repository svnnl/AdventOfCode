with open('../data/advent_3.txt') as f:
    data = [i.split(',') for i in f.read().splitlines()]


def get_coordinates(wires: list[list]) -> list:
    result = []
    for commands in wires:
        coordinates = []
        x1 = 0
        y1 = 0
        for i in commands:
            direction = i[0]
            value = int(i[1:])
            if direction == 'R':
                x2 = x1 + value
                while x1 != x2:
                    x1 += 1
                    coordinates.append((x1, y1))
            if direction == 'L':
                x2 = x1 - value
                while x1 != x2:
                    x1 -= 1
                    coordinates.append((x1, y1))
            if direction == 'U':
                y2 = y1 + value
                while y1 != y2:
                    y1 += 1
                    coordinates.append((x1, y1))
            if direction == 'D':
                y2 = y1 - value
                while y1 != y2:
                    y1 -= 1
                    coordinates.append((x1, y1))
        result.append(coordinates)
    return result


def get_intersections(coordinates: list):
    return set(coordinates[0]).intersection(set(coordinates[1]))


def manhattan(intersections):
    return [abs(i[0]) + abs(i[1]) for i in intersections]


def get_steps(coordinates, intersections):
    return [sum(wire.index(i) + 1 for wire in coordinates) for i in intersections]


coordinates = get_coordinates(data)
intersections = get_intersections(coordinates)

print(f'Answer to Part 1: {min(manhattan(intersections))}')
print(f'Answer to Part 2: {min(get_steps(coordinates, intersections))}')
