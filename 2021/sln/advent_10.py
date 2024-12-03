import numpy as np

with open('../data/advent_10.txt') as f:
    data = f.read().splitlines()

# PART 1

pairs = ['<>', '()', '{}', '[]']

wrong = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incomplete_lines = []
error_score = 0

for index, line in enumerate(data):
    while any(i in line for i in pairs):
        for i in pairs:
            line = line.replace(i, '')
    print('Line {0} has the remaining string: {1}'.format(index, line))
    if not any(i in line for i in wrong.keys()):
        incomplete_lines.append(line)

    for i in line:
        if i in wrong.keys():
            print('Wrong value found in Line {0} -> "{1}"'.format(index, i))
            error_score += wrong[i]
            break

print("Answer to Part 1: {0}".format(error_score))

# PART 2

scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

middle_scores = []

for line in incomplete_lines:
    score = 0
    reversed_string = line[::-1]
    for i in reversed_string:
        score = (score * 5) + scores[i]
    middle_scores.append(score)

print("Answer to Part 2: {0}".format(int(np.median(middle_scores))))
