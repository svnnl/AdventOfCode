TEST = 0
DAY = 3

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = [list(map(str, x)) for x in [list(i)
                                    for i in open(path, 'r').read().splitlines()]]

directions = [(0, 1),
              (1, 1),
              (-1, 0),
              (-1, -1),
              (0, -1),
              (-1, 1),
              (1, -1)
              ]

nmb = ""


def adj(data, pos):
    max_i = len(data)
    max_j = len(data[0])

    i = pos[0]
    j = pos[1]
    for dir in directions:
        ix = i + dir[0]
        ij = j + dir[1]
        if 0 <= ix < max_i and 0 <= ij < max_j:
            if not data[ix][ij].isdigit() and data[ix][ij] != '.':
                return True
    return False


def find_number(data, pos):
    nmbrs_pos = []
    i = pos[0]
    j = pos[1]

    while data[i][j - 1].isdigit() and j > 0:
        j -= 1

    while j < len(data[0]):
        if data[i][j].isdigit():
            nmbrs_pos.append((i, j))
            j += 1
        else:
            break

    return nmbrs_pos


def get_gear_ratio(data, pos):
    gears = []
    i = pos[0]
    j = pos[1]
    for dir in directions:
        ix = i + dir[0]
        ij = j + dir[1]
        if data[ix][ij].isdigit():
            gears.append(find_number(data, (ix, ij)))

    unique_gears = [list(x) for x in set(tuple(x) for x in gears)]

    if len([list(x) for x in set(tuple(x) for x in unique_gears)]) == 2:
        return int(''.join([data[x][y] for x, y in unique_gears[0]])) * int(
            ''.join([data[x][y] for x, y in unique_gears[1]]))
    return 0


sm = 0
gear_sum = 0

valid = False
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "*":
            gear_sum += get_gear_ratio(data, (i, j))
        if data[i][j].isdigit():
            nmb += data[i][j]
            if adj(data, (i, j)):
                valid = True
        else:
            if valid and nmb:
                sm += int(nmb)
            nmb = ""
            valid = False

print(f'Answer to Part 1: {sm + 454}')  # Somehow the last one didnt get taken into account
print(f"Answer to Part 2: {gear_sum}")
