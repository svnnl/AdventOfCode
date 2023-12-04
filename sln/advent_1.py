import re

TEST = 0
DAY = 1

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = open(path, 'r').read().splitlines()


def get_sum(input):
    return sum([int("%d%d" % (int(x[0]), int(x[-1]))) for x in [re.findall(r"\d", i) for i in input]])


part_1 = get_sum(data)
print(f"Answer to Part 1: {part_1}")


mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

new_data = []
for line in data:
    for w in mapping.keys():
        if w in line:
            line = line.replace(w, w[0] + mapping[w] + w[-1])
    new_data.append(line)

part_2 = get_sum(new_data)
print(f"Answer to Part 2: {part_2}")
