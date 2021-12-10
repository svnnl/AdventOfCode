with open('../data/advent_10.txt') as f:
    data = f.read().splitlines()

pairs = ['<>', '()', '{}', '[]']
wrong = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

for index, line in enumerate(data):
    while any(i in line for i in pairs):
        for i in pairs:
            line = line.replace(i, '')
    print('Line {0} has the remaining string: {1}'.format(index, line))

    #print([3 for j in line if j == ')'])
