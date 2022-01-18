import re

with open('../data/advent_14.txt') as f:
    data = f.read().splitlines()


def to_binary(num):
    return str(bin(int(num)))[2:]


def apply_mask(binary, bitmask):
    temp = list(binary)
    for i, v in enumerate(bitmask):
        if v != 'X':
            temp[i] = str(v)
    return ''.join(temp)


# Part 1

bitmask = ''
memory = {}

for i, v in enumerate(data):
    if 'mask' in v:
        bitmask = v.split(' = ')[1]
    else:
        address = re.search(r"\[([0-9]+)\]", v).group(1)
        value = v.split(' = ')[1]

        binary = ((len(bitmask) - len(to_binary(value))) * '0') + to_binary(value)
        print(f'{binary} \n{bitmask}')
        print(apply_mask(binary, bitmask))
        print('-----------------------------------')

        memory[address] = int(apply_mask(binary, bitmask), 2)

print(f'Answer to Part 1: {sum(memory.values())}')

# Part 2
