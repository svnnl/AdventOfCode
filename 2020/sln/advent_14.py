import re

with open('../data/advent_14.txt') as f:
    data = f.read().splitlines()


def to_binary(num):
    return str(bin(int(num)))[2:]


# Part 1
def mask_1(binary, bitmask):
    temp = list(binary)
    for i, v in enumerate(bitmask):
        if v != 'X':
            temp[i] = str(v)
    return ''.join(temp)


bitmask = ''
memory = {}

for i, v in enumerate(data):
    if 'mask' in v:
        bitmask = v.split(' = ')[1]
    else:
        address = re.search(r"\[([0-9]+)\]", v).group(1)
        value = v.split(' = ')[1]

        binary = ((len(bitmask) - len(to_binary(value))) * '0') + to_binary(value)

        memory[address] = int(mask_1(binary, bitmask), 2)

print(f'Answer to Part 1: {sum(memory.values())}')


# Part 2
def mask_2(binary, bitmask):
    temp = list(binary)
    for i, v in enumerate(bitmask):
        if v in ['X', '1']:
            temp[i] = str(v)

    return ''.join(temp)


def find_combinations(binary, i=0):
    pattern = list(binary)
    # base case
    if not pattern:
        return

    if i == len(pattern):
        combinations.append(''.join(pattern))
        return

    # if the current character is '?'
    if pattern[i] == 'X':
        for ch in '01':
            # replace '?' with 0 and 1
            pattern[i] = str(ch)

            # recur for the remaining pattern
            find_combinations(pattern, i + 1)

            # backtrack
            pattern[i] = 'X'

    else:
        # if the current character is 0 or 1, ignore it and
        # recur for the remaining pattern
        find_combinations(pattern, i + 1)


bitmask = ''
memory = {}

for i, v in enumerate(data):
    if 'mask' in v:
        bitmask = v.split(' = ')[1]
    else:
        address = re.search(r"\[([0-9]+)\]", v).group(1)
        value = v.split(' = ')[1]

        combinations = []

        binary = ((len(bitmask) - len(to_binary(address))) * '0') + to_binary(address)

        find_combinations(mask_2(binary, bitmask))

        for combo in combinations:
            memory[int(combo, 2)] = int(value)

print(f'Answer to Part 2: {sum(memory.values())}')
