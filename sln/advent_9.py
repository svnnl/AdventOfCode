TEST = 0
DAY = 9

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = [list(map(int, i)) for i in [line.split()
                                    for line in open(path, 'r').read().splitlines()]]

t1 = 0
t2 = 0
for seq in data:
    curr = seq
    last_elements = []
    first_elements = []

    while not all(v == 0 for v in curr):
        first_elements.append(curr[0])
        last_elements.append(curr[-1])
        curr = [j - i for i, j in zip(curr[:-1], curr[1:])]

    r1 = 0
    for n in last_elements[::-1]:
        r1 += n

    t1 += r1

    # Part 2
    r2 = 0
    for n in first_elements[::-1]:
        r2 = n - r2

    t2 += r2

print(f'Answer to Part 1: {t1}')
print(f'Answer to Part 2: {t2}')
