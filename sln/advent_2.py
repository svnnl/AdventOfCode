with open('../data/advent_2.txt') as f:
    data = f.read().splitlines()

rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']


def get_score(input):
    return 1 if input in rock else 2 if input in paper else 3


def rps(a, b):
    if (a in rock and b in rock) or (a in paper and b in paper) or (a in scissors and b in scissors):
        return 3
    elif (b in rock and a in scissors) or (b in paper and a in rock) or (b in scissors and a in paper):
        return 6
    else:
        return 0


def rps_2(a, b):
    score = 3 if b == 'Y' else 0 if b == 'X' else 6
    if b == 'Y':
        score += get_score(a)
    elif b == 'Z':
        if a in rock:
            score += 2
        elif a in paper:
            score += 3
        elif a in scissors:
            score += 1
    else:
        if a in rock:
            score += 3
        elif a in paper:
            score += 1
        elif a in scissors:
            score += 2
    return score


score_1 = 0
score_2 = 0
for i in data:
    opponent, you = i.split(' ')
    score_1 += rps(opponent, you) + get_score(you)
    score_2 += rps_2(opponent, you)

print(f'Answer to Part 1: {score_1}')
print(f'Answer to Part 2: {score_2}')
