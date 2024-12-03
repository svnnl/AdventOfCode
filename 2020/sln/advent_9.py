with open('../data/advent_9.txt') as f:
    data = list(map(int, f.read().splitlines()))

preamble_length = 25
next_number_index = 0
next_number = 0

for index, number in enumerate(data):
    preamble = data[index:index + preamble_length]
    next_number = data[index + preamble_length]
    next_number_index = index + preamble_length
    found = False
    for i in range(0, len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == next_number:
                found = True
    if not found:
        print('Answer to Part 1: {0}'.format(next_number))
        break

for i in range(0, next_number_index):
    for j in range(i, next_number_index):
        contiguous_list = data[i:j]
        if sum(contiguous_list) == next_number:
            print('Answer to Part 2: {0}'.format(min(contiguous_list) + max(contiguous_list)))
