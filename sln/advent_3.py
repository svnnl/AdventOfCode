TEST = 1
DAY = 3

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = [list(map(str, x)) for x in [list(i)
                                    for i in open(path, 'r').read().splitlines()]]

print(data)

directions = [(0, 1),
              (1, 1),
              (1, 0),
              (-1, 0),
              (-1, -1),
              (0, -1),
              (-1, 1),
              (1, -1)
              ]

sum = 0
nmb = ""


def adj(data, pos):
    max_i = len(data)
    max_j = len(data[0])

    i = pos[0]
    j = pos[1]
    print(f"Checking {pos}")
    for dir in directions:
        ix = i + dir[0]
        ij = j + dir[1]
        if 0 <= ix < max_i and 0 <= ij < max_j:
            # print(f"dir: {dir} -> new pos {(ix, ij)}, {data[ix][ij]}")
            if not data[ix][ij].isdigit() and data[ix][ij] != '.':
                print(f"Found symbol: {data[ix][ij]} on {pos}")
                return True
    return False


sm = 0

valid = False
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j].isdigit():
            nmb += data[i][j]
            if (adj(data, (i, j))):
                valid = True
        else:
            if nmb:
                print(nmb)
            if valid and nmb:
                print(f'Adding {nmb}')
                sm += int(nmb)
            nmb = ""
            valid = False

# Check for * and then find the adjacent numbers and multiply and sum them

print(sm)
