with open('../data/advent_6.txt') as f:
    data = f.read().split('\n\n')

print('Answer to Part 1 is: {0}'.format(sum([len(set(i.replace('\n', ''))) for i in data])))

count = 0
for i in [list(i.split('\n')) for i in data]:
    values = {}
    for j in i:
        for k in set(j):
            if k in values:
                values[k] += 1
            else:
                values[k] = 1
    count += len([k for k, v in values.items() if int(v) == len(i)])

print('Answer to Part 2 is: {0}'.format(count))
