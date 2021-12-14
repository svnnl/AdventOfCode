polymer = ''
rules = {}

with open('../data/advent_14.txt') as f:
    for line in f.readlines():
        if len(line.strip()) == 0:
            continue
        if '->' in line:
            a = line.strip().split(' ')
            rules[a[0]] = a[2]
            continue
        polymer = line.strip()

print(polymer)
print(rules)

pairs = {}
